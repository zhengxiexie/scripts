import sys
import time
import logger
import util

from timeout_decorator import timeout_decorator

from kubernetes import client, config
from kubernetes.client.models.v1_container_image import V1ContainerImage

NCP_INI_DIR = "/etc/nsx-ujo/vc"
NCP_INI_FILE =  "/etc/nsx-ujo/ncp.ini"
DEPLOYMENT_NAMESPACE = "vmware-system-nsx"
DEPLOYMENT_NAME = "nsx-ncp"
KUBE_CONFIG = "/root/.kube/config"


log = logger.get_logger(__name__)


def names(self, vs):
    self._names = vs


# bug: https://github.com/kubernetes-client/python/issues/895
V1ContainerImage.names = V1ContainerImage.names.setter(names)

def get_deployment(api):
    resp = api.read_namespaced_deployment(
        name=DEPLOYMENT_NAME,
        namespace=DEPLOYMENT_NAMESPACE,
    )
    return resp


def get_pod_name():
    _, pod_name = util.runcmd("""kubectl get pods -l component=nsx-ncp -n vmware-system-nsx -o=jsonpath="{.items[?(@.status.phase=='Running')].metadata.name}" """)
    log.info(pod_name)
    return pod_name

@util.wait_and_retry()
def dump_ncp_ini():
    _, _ = util.runcmd("mkdir -p %s" % NCP_INI_DIR)
    pod_name = get_pod_name()
    res, _ = util.runcmd("kubectl exec %s -c nsx-ncp -n vmware-system-nsx -- cat %s > "
                         "%s" % (pod_name, NCP_INI_FILE, NCP_INI_FILE))
    if res != 0:
        raise Exception("dump ncp ini from ncp configmap failed")
    res, _ = util.runcmd("kubectl exec %s -c nsx-ncp -n vmware-system-nsx -- cat /etc/nsx-ujo/vc/username > /etc/nsx-ujo/vc/username" % pod_name)
    res, _ = util.runcmd("kubectl exec %s -c nsx-ncp -n vmware-system-nsx -- cat /etc/nsx-ujo/vc/password > /etc/nsx-ujo/vc/password" % pod_name)
    res, _ = util.runcmd("kubectl exec %s -c nsx-ncp -n vmware-system-nsx -- cat /etc/nsx-ujo/nsx_manager_certificate_0 > /etc/nsx-ujo/nsx_manager_certificate_0" % pod_name)


@timeout_decorator.timeout(180, timeout_exception=StopIteration)
def check_pod_status(api):
    while True:
        resp = api.list_namespaced_pod(
            namespace=DEPLOYMENT_NAMESPACE,
            label_selector="component=nsx-ncp",
            timeout_seconds=50
        )
        for pod in resp.items:
            log.info("pod %s status: %s" % (pod.metadata.name, pod.status.phase))
            if pod.status.phase != "Running":
                log.info("pod %s is not running, wait 10s" % pod.metadata.name)
                time.sleep(10)
                continue
            for container in pod.status.container_statuses:
                log.info("pod %s container %s status: %s" % (pod.metadata.name, container.name, container.ready))
                if container.ready is not True:
                    log.info("pod %s container %s is not ready, wait 10s" % (pod.metadata.name, container.name))
                    time.sleep(10)
                    continue
        return True


def update_deployment(api, deployment, hostname, sleep=False):
    if sleep:
        command = ["/bin/bash", "-c", "while true; do echo hello, world!; sleep 1; done"]
    else:
        command = ["/usr/local/bin/manager", "-nsxconfig", NCP_INI_FILE, "-health-probe-bind-address", ":8383", "-log-level", "2"]
    deployment.spec.template.spec.containers[1].command = command
    deployment.spec.template.spec.containers[1].liveness_probe.failure_threshold = 5000
    container = deployment.spec.template.spec.containers[1]
    nsx_operator_volume = client.V1Volume(
        name='nsx-operator-volume',
        host_path=client.V1HostPathVolumeSource(
            path='/root/nsx-operator',
            type='Directory'
        )
    )
    if nsx_operator_volume not in deployment.spec.template.spec.volumes:
        deployment.spec.template.spec.volumes.append(nsx_operator_volume)

    nsx_operator_volume_mount = client.V1VolumeMount(
        name='nsx-operator-volume',
        mount_path='/root/nsx-operator'
    )
    if nsx_operator_volume_mount not in container.volume_mounts:
        container.volume_mounts.append(nsx_operator_volume_mount)
    deployment.spec.replicas = 1
    
    # Add nodeSelector configuration
    deployment.spec.template.spec.node_selector = {
        "node-role.kubernetes.io/control-plane": "",
        "current": "current",
        hostname: hostname
    }
    
    api.patch_namespaced_deployment(
        name=DEPLOYMENT_NAME, namespace=DEPLOYMENT_NAMESPACE, body=deployment
    )

def main():
    log.info("load default kube config")
    config.load_kube_config(KUBE_CONFIG)
    c = client.Configuration()
    # c.debug = True

    apps_v1 = client.AppsV1Api(api_client=client.ApiClient(configuration=c))
    core_v1 = client.CoreV1Api(api_client=client.ApiClient(configuration=c))

    log.info("dump ncp.ini and username and password")
    dump_ncp_ini()

    # Get node name dynamically using the hostname
    _, hostname = util.runcmd("hostname")
    hostname = hostname.strip()
    log.info("got hostname: %s" % hostname)
    
    log.info("label node %s with current=current" % hostname)
    cmd = "kubectl label node %s current=current" % hostname
    _, stdout = util.runcmd(cmd)
    log.info("node labeling result: %s" % stdout)

    log.info("patch nsx-ncp deployment")
    deployment = get_deployment(apps_v1)
    # pass arg from the command line
    sleep = True if int(sys.argv[1]) == 0 else False
    update_deployment(apps_v1, deployment, hostname, sleep)

    log.info("restart nsx-ncp deployment")
    cmd = "kubectl rollout restart deployment nsx-ncp -n nsx-system"
    _, stdout = util.runcmd(cmd)

    log.info("check nsx-ncp pod status")
    check_pod_status(core_v1)




if __name__ == "__main__":
    main()
