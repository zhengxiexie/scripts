"""
NSX NCP Deployment Manager

This module manages NSX NCP (Network Control Plane) deployments in Kubernetes,
providing functionality to update deployments, manage volumes, and monitor pod status.
"""

import sys
import time

from util import util
from timeout_decorator import timeout_decorator
from kubernetes import client, config
from kubernetes.client.models.v1_container_image import V1ContainerImage

# Configuration constants
NCP_INI_DIR = "/etc/nsx-ujo/vc"
NCP_INI_FILE = "/etc/nsx-ujo/ncp.ini"
DEPLOYMENT_NAMESPACE = "vmware-system-nsx"
DEPLOYMENT_NAME = "nsx-ncp"
KUBE_CONFIG = "/root/.kube/config"

# Timeout and retry constants
POD_STATUS_TIMEOUT = 180
POD_CHECK_TIMEOUT = 50
SLEEP_INTERVAL = 10
LIVENESS_PROBE_FAILURE_THRESHOLD = 5000

# Volume configuration
NSX_OPERATOR_VOLUME_NAME = 'nsx-operator-volume'
NSX_OPERATOR_HOST_PATH = '/root/nsx-operator'

log = util.logger.get_logger(__name__)


def _names_setter(self, vs):
    """Setter function for V1ContainerImage names property."""
    self._names = vs


# Workaround for Kubernetes client bug
# See: https://github.com/kubernetes-client/python/issues/895
V1ContainerImage.names = V1ContainerImage.names.setter(_names_setter)

def get_deployment(api: client.AppsV1Api) -> client.V1Deployment:
    """
    Retrieve the NSX NCP deployment from Kubernetes.
    
    Args:
        api: Kubernetes Apps V1 API client
        
    Returns:
        V1Deployment: The NSX NCP deployment object
        
    Raises:
        kubernetes.client.exceptions.ApiException: If deployment cannot be found
    """
    resp = api.read_namespaced_deployment(
        name=DEPLOYMENT_NAME,
        namespace=DEPLOYMENT_NAMESPACE,
    )
    return resp


def get_pod_name() -> str:
    """
    Get the name of the running NSX NCP pod.
    
    Returns:
        str: Name of the running NSX NCP pod
        
    Raises:
        RuntimeError: If no running pod is found or command fails
    """
    cmd = (
        'kubectl get pods -l component=nsx-ncp -n vmware-system-nsx '
        '-o=jsonpath="{.items[?(@.status.phase==\'Running\')].metadata.name}"'
    )
    _, pod_name = util.runcmd(cmd)
    log.info(f"Found running pod: {pod_name}")
    return pod_name

@util.wait_and_retry()
def dump_ncp_ini() -> None:
    """
    Dump NCP configuration files from the running pod to the local filesystem.
    
    This function extracts the NCP configuration file, username, password, and
    NSX manager certificate from the running NSX NCP pod.
    
    Raises:
        RuntimeError: If any of the file extraction operations fail
    """
    # Create the NCP configuration directory
    _, _ = util.runcmd(f"mkdir -p {NCP_INI_DIR}")
    
    pod_name = get_pod_name()
    
    # Extract NCP configuration file
    cmd = (
        f"kubectl exec {pod_name} -c nsx-ncp -n vmware-system-nsx -- "
        f"cat {NCP_INI_FILE} > {NCP_INI_FILE}"
    )
    res, _ = util.runcmd(cmd)
    if res != 0:
        raise RuntimeError("Failed to dump NCP configuration file from pod")
    
    # Extract credential files
    credential_files = [
        ("/etc/nsx-ujo/vc/username", "/etc/nsx-ujo/vc/username"),
        ("/etc/nsx-ujo/vc/password", "/etc/nsx-ujo/vc/password"),
        ("/etc/nsx-ujo/nsx_manager_certificate_0", "/etc/nsx-ujo/nsx_manager_certificate_0")
    ]
    
    for source_path, dest_path in credential_files:
        cmd = (
            f"kubectl exec {pod_name} -c nsx-ncp -n vmware-system-nsx -- "
            f"cat {source_path} > {dest_path}"
        )
        res, _ = util.runcmd(cmd)
        if res != 0:
            log.warning(f"Failed to extract {source_path} from pod")


@timeout_decorator.timeout(POD_STATUS_TIMEOUT, timeout_exception=StopIteration)
def check_pod_status(api: client.CoreV1Api) -> bool:
    """
    Monitor NSX NCP pod status until all pods and containers are ready.
    
    This function continuously checks the status of NSX NCP pods and their containers
    until they are all running and ready, or until the timeout is reached.
    
    Args:
        api: Kubernetes Core V1 API client
        
    Returns:
        bool: True when all pods and containers are ready
        
    Raises:
        StopIteration: If timeout is reached before pods are ready
    """
    while True:
        resp = api.list_namespaced_pod(
            namespace=DEPLOYMENT_NAMESPACE,
            label_selector="component=nsx-ncp",
            timeout_seconds=POD_CHECK_TIMEOUT
        )
        
        all_pods_ready = True
        
        for pod in resp.items:
            log.info(f"Pod {pod.metadata.name} status: {pod.status.phase}")
            
            if pod.status.phase != "Running":
                log.info(f"Pod {pod.metadata.name} is not running, waiting {SLEEP_INTERVAL}s")
                all_pods_ready = False
                break
                
            # Check container readiness
            if pod.status.container_statuses:
                for container in pod.status.container_statuses:
                    log.info(
                        f"Pod {pod.metadata.name} container {container.name} "
                        f"ready: {container.ready}"
                    )
                    if not container.ready:
                        log.info(
                            f"Pod {pod.metadata.name} container {container.name} "
                            f"is not ready, waiting {SLEEP_INTERVAL}s"
                        )
                        all_pods_ready = False
                        break
                        
                if not all_pods_ready:
                    break
        
        if all_pods_ready:
            return True
            
        time.sleep(SLEEP_INTERVAL)


def update_deployment(
    api: client.AppsV1Api, 
    deployment: client.V1Deployment, 
    sleep: bool = False
) -> None:
    """
    Update the NSX NCP deployment configuration based on the sleep mode.
    
    Args:
        api: Kubernetes Apps V1 API client
        deployment: The deployment object to update
        sleep: If True, configure for debug/sleep mode; if False, normal operation
        
    Raises:
        kubernetes.client.exceptions.ApiException: If deployment update fails
    """
    # Configure container command based on mode
    if sleep:
        command = ["/bin/bash", "-c", "while true; do echo hello, world!; sleep 1; done"]
    else:
        command = [
            "/usr/local/bin/manager", 
            "-nsxconfig", NCP_INI_FILE, 
            "-health-probe-bind-address", ":8383", 
            "-log-level", "2"
        ]
    
    # Update container configuration
    container = deployment.spec.template.spec.containers[1]
    container.command = command
    container.liveness_probe.failure_threshold = LIVENESS_PROBE_FAILURE_THRESHOLD
    
    if sleep:
        _configure_sleep_mode(deployment, container)
    else:
        _configure_normal_mode(deployment, container)
    
    # Apply the deployment update
    api.patch_namespaced_deployment(
        name=DEPLOYMENT_NAME, 
        namespace=DEPLOYMENT_NAMESPACE, 
        body=deployment
    )


def _configure_sleep_mode(deployment: client.V1Deployment, container: client.V1Container) -> None:
    """
    Configure deployment for sleep/debug mode.
    
    Args:
        deployment: The deployment object to configure
        container: The container object to configure
    """
    # Create and add NSX operator volume
    nsx_operator_volume = client.V1Volume(
        name=NSX_OPERATOR_VOLUME_NAME,
        host_path=client.V1HostPathVolumeSource(
            path=NSX_OPERATOR_HOST_PATH,
            type='Directory'
        )
    )
    
    # Add volume if not already present
    if not any(vol.name == NSX_OPERATOR_VOLUME_NAME for vol in deployment.spec.template.spec.volumes):
        deployment.spec.template.spec.volumes.append(nsx_operator_volume)

    # Create and add volume mount
    nsx_operator_volume_mount = client.V1VolumeMount(
        name=NSX_OPERATOR_VOLUME_NAME,
        mount_path=NSX_OPERATOR_HOST_PATH
    )
    
    # Add a volume mount if not already present
    if not any(mount.name == NSX_OPERATOR_VOLUME_NAME for mount in container.volume_mounts):
        container.volume_mounts.append(nsx_operator_volume_mount)
    
    # Configure for a single replica and node selection
    deployment.spec.replicas = 1
    deployment.spec.template.spec.node_selector = {
        "node-role.kubernetes.io/control-plane": "",
        "current": "current",
    }


def _configure_normal_mode(deployment: client.V1Deployment, container: client.V1Container) -> None:
    """
    Configure deployment for normal operation mode.
    
    Args:
        deployment: The deployment object to configure
        container: The container object to configure
    """
    # Remove NSX operator volume if it exists
    deployment.spec.template.spec.volumes = [
        vol for vol in deployment.spec.template.spec.volumes 
        if vol.name != NSX_OPERATOR_VOLUME_NAME
    ]
    
    # Remove the NSX operator volume mount if it exists
    container.volume_mounts = [
        mount for mount in container.volume_mounts 
        if mount.name != NSX_OPERATOR_VOLUME_NAME
    ]

def main() -> None:
    """
    Main function to manage NSX NCP deployment configuration.
    
    This function orchestrates the entire process of:
    1. Loading Kubernetes configuration
    2. Dumping NCP configuration files
    3. Labeling the current node
    4. Updating the deployment based on command line arguments
    5. Restarting deployment
    6. Monitoring pod status
    
    Raises:
        SystemExit: If invalid command line arguments are provided
        RuntimeError: If any of the operations fail
    """
    # Validate command line arguments
    if len(sys.argv) != 2:
        log.error("Usage: python main.py <sleep_mode>")
        log.error("  sleep_mode: 0 for sleep mode, 1 for normal mode")
        sys.exit(1)
    
    try:
        sleep_mode_arg = int(sys.argv[1])
        if sleep_mode_arg not in [0, 1]:
            raise ValueError("Sleep mode argument must be 0 or 1")
        sleep_mode = sleep_mode_arg == 0
    except ValueError as e:
        log.error(f"Invalid argument: {e}")
        sys.exit(1)
    
    # Load Kubernetes configuration
    log.info("Loading default Kubernetes configuration")
    config.load_kube_config(KUBE_CONFIG)
    
    # Create Kubernetes API clients
    configuration = client.Configuration()
    # configuration.debug = True # Uncomment for debugging
    api_client = client.ApiClient(configuration=configuration)
    apps_v1_api = client.AppsV1Api(api_client=api_client)
    core_v1_api = client.CoreV1Api(api_client=api_client)

    # Dump NCP configuration files
    log.info("Dumping NCP configuration and credentials")
    dump_ncp_ini()

    # Get current hostname
    _, hostname = util.runcmd("hostname")
    hostname = hostname.strip()
    log.info(f"Current hostname: {hostname}")
    
    # Label the current node
    log.info(f"Labeling node {hostname} with current=current")
    label_cmd = f"kubectl label node {hostname} current=current --overwrite"
    _, stdout = util.runcmd(label_cmd)
    log.info(f"Node labeling result: {stdout}")

    # Update the NSX NCP deployment
    log.info("Updating NSX NCP deployment configuration")
    deployment = get_deployment(apps_v1_api)
    update_deployment(apps_v1_api, deployment, sleep_mode)

    # Restart the deployment
    log.info("Restarting NSX NCP deployment")
    restart_cmd = f"kubectl rollout restart deployment {DEPLOYMENT_NAME} -n {DEPLOYMENT_NAMESPACE}"
    _, stdout = util.runcmd(restart_cmd)
    log.info(f"Deployment restart result: {stdout}")

    # Monitor pod status
    log.info("Monitoring NSX NCP pod status")
    check_pod_status(core_v1_api)
    
    log.info("NSX NCP deployment update completed successfully")


if __name__ == "__main__":
    main()
