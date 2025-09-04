#!/usr/bin/env python3
"""
Trigger Jenkins job 'dev-nsxvpc'. Optionally sync parameters from a specific build (e.g., 8454).
"""

import requests
import argparse
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from util.logger import get_logger

# Initialize logger
logger = get_logger(__name__)

# Jenkins configuration
JENKINS_BASE_URL = "https://jenkins-vcf-wcp-dev.devops.broadcom.net"
JOB_NAME = "dev-nsxvpc"

# Job parameters synced from build #8454
JOB_PARAMETERS = {
    "TERA_REF": "",
    "PERFORCE_BRANCH": "main",
    "SKIP_CLEANUP": True,
    "SUPPORT_BUNDLES": True,
    "OVA_BUILD": "ob-24871681",
    "ASYNC_OVA_BUILD": "",
    "VC_BUILD": "ob-24876732",
    "ESX_BUILD": "ob-24876735",
    "NSX_SETUP": True,
    "SHORT_FORM_RUNNAME": True,
    "SPHERELET_BUILD": "",
    "NUM_MASTER_VM": "1",
    "NO_OF_SUPERVISORS": "1",
    "SCALE_OUT_CPVM": False,
    "FORCE_K8S_VERSION": "",
    "KEEP_TESTBED_HOURS": "168",
    "TESTBED_POLICY": "DELETE_NEVER",
    "DHCP_FIP": True,
    "APPROVED_BUILDS_JSON_URL": "https://jenkins-vcfwcp.devops.broadcom.net/job/prod-integ-nsxvpc/lastSuccessfulBuild/artifact/builds.json",
    "GUESTCLUSTER_SETUP": False,
    "GC_OVA_BUILD": "",
    "NSXT_BUILD": "ob-24925967",
    # "NSXT_BUILD": "ob-24942127",
    "VDNET_LAUNCHER_OVF": "vdnet-launcher-ubuntu2004-v6",
    "VDNET_BRANCH": "rtqa-staging",
    "VDNET_COMMIT_ID": "",
    "PERFORM_TEST_CLEANUP": False,
    "NSX_MULTIPLE_MP": False,
    "REPLACE_TLS_CERT": False,
    "SKIP_VC_ESX_CLN_CHECK": "true",
    "DISABLE_NS_ISOLATION": False,
    "NIMBUS_LOCATION": "LVN",
    "WCP_BUILD": "ob-24871682",
    "FEATURE_STATES": "WCP_Workload_Domain_Isolation=enabled,WCP_VPC_Network=enabled,WCP_Simplified_Enablement=enabled,WCP_VM_Reservations=enabled,PAIF_AcceleratorCapacityReservation=enabled,PAIF_CapacityVisualization=enabled",
    "SUPERVISOR_CAPABILITIES": "",
    "NUM_ESX": "",
    "CLUSTER_ROUTED_MODE": False,
    "CLUSTER_SUBNET_PREFIX": "",
    "VLCM_CLUSTER": True,
    "RUN_GCE2E": False,
    "GCE2E_BRANCH": "origin/master",
    "GCE2E_TEST_TAGS": "vmservice",
    "GCE2E_TEST_FOCUS": "VM-VPC",
    "SKIP_SYNC_TO_WCP_CLN": False,
    "ENABLE_VSAN": False,
    "CREATE_VSAN_DIRECT_DATASTORE": False,
    "TESTS_TO_RUN": "None",
    "TEST_GROUPS": "",
    "NSX_VDS_VERSION": "0",
    "TKG_SVS_CONFIG_OVERRIDE": "",
    "NSX_VPC": True,
    "NSX_LOAD_BALANCER": "nsx-lb",
    "TGW_TYPE": "centralized",
    "PRIVATE_INFRA": "PUBLIC",
    "USE_INSTAPP": False
}


def get_jenkins_crumb(session, jenkins_username=None, jenkins_token=None):
    """Get Jenkins CSRF crumb for authentication using session"""
    crumb_url = f"{JENKINS_BASE_URL}/crumbIssuer/api/json"
    
    # Try both Bearer and Basic authentication
    auth_methods = []
    
    if jenkins_username and jenkins_token:
        # Basic auth with username:token
        auth_methods.append(("basic", (jenkins_username, jenkins_token)))
    
    if jenkins_token:
        # Bearer token
        auth_methods.append(("bearer", f"Bearer {jenkins_token}"))
    
    for auth_type, auth_value in auth_methods:
        try:
            if auth_type == "basic":
                response = session.get(crumb_url, auth=auth_value, timeout=10)
            else:
                headers = {"Authorization": auth_value}
                response = session.get(crumb_url, headers=headers, timeout=10)
                
            if response.status_code == 200:
                crumb_data = response.json()
                logger.info(f"Successfully authenticated using {auth_type} auth")
                return crumb_data.get('crumb'), crumb_data.get('crumbRequestField', 'Jenkins-Crumb'), auth_type, auth_value
            else:
                logger.warning(f"{auth_type} auth failed. Status: {response.status_code}")
                
        except Exception as e:
            logger.warning(f"Error with {auth_type} auth: {e}")
    
    logger.warning("All authentication methods failed")
    return None, None, None, None

def fetch_parameters_from_build(session, build_number, auth_type, auth_value):
    """Fetch parameters from a specific Jenkins build"""
    url = f"{JENKINS_BASE_URL}/job/{JOB_NAME}/{build_number}/api/json?tree=actions[parameters[name,value]]"
    try:
        if auth_type == "basic":
            resp = session.get(url, auth=auth_value, timeout=20)
        elif auth_type == "bearer":
            headers = {"Authorization": auth_value}
            resp = session.get(url, headers=headers, timeout=20)
        else:
            logger.error("No valid authentication method to fetch build parameters")
            return None
        if resp.status_code != 200:
            logger.error(f"Failed to fetch build parameters. Status: {resp.status_code}")
            return None
        data = resp.json()
        params = {}
        for action in data.get("actions", []):
            for p in (action.get("parameters", []) or []):
                params[p.get("name")] = p.get("value")
        if not params:
            logger.warning("No parameters found on the specified build")
        return params
    except Exception as e:
        logger.error(f"Error fetching build parameters: {e}")
        return None

def trigger_jenkins_job(jenkins_username=None, jenkins_token=None, dry_run=False, override_params=None):
    """Trigger the Jenkins job with the specified parameters"""
    
    # Create a session to maintain cookies
    session = requests.Session()
    
    # Prepare the URL
    build_url = f"{JENKINS_BASE_URL}/job/{JOB_NAME}/buildWithParameters"
    
    # Get Jenkins crumb for CSRF protection and determine auth method
    crumb_value, crumb_field, auth_type, auth_value = get_jenkins_crumb(session, jenkins_username, jenkins_token)
    
    # Prepare form data with job parameters
    form_data = (override_params or JOB_PARAMETERS).copy()
    
    # Add crumb to form data if available
    if crumb_value and crumb_field:
        form_data[crumb_field] = crumb_value
        logger.info(f"Using CSRF crumb: {crumb_field}")
    
    logger.info(f"Jenkins URL: {build_url}")
    logger.info(f"Job Name: {JOB_NAME}")
    logger.info(f"Number of parameters: {len(form_data)}")
    
    if dry_run:
        logger.info("\n=== DRY RUN MODE ===")
        logger.info("Would send the following parameters:")
        for key, value in form_data.items():
            if key != crumb_field:  # Don't print the crumb value
                logger.info(f"  {key}: {value}")
        logger.info(f"\nAuthentication method: {auth_type}")
        if crumb_value:
            logger.info(f"Crumb field '{crumb_field}' included in form data")
        return True
    
    try:
        logger.info("\nTriggering Jenkins job...")
        
        # Send a request using the same authentication method that worked for crumb
        if auth_type == "basic":
            response = session.post(build_url, auth=auth_value, data=form_data, timeout=30)
        elif auth_type == "bearer":
            headers = {"Authorization": auth_value}
            response = session.post(build_url, headers=headers, data=form_data, timeout=30)
        else:
            logger.error("❌ No valid authentication method found")
            return False
        
        logger.info(f"Response Status: {response.status_code}")
        
        if response.status_code == 201:
            logger.info("✅ Job triggered successfully!")
            location = response.headers.get('Location')
            if location:
                logger.info(f"Queue item location: {location}")
        elif response.status_code == 200:
            logger.info("✅ Job triggered successfully (status 200)!")
        else:
            logger.error(f"❌ Failed to trigger job. Status code: {response.status_code}")
            logger.error(f"Response body: {response.text}")
            return False
            
    except requests.exceptions.RequestException as e:
        logger.error(f"❌ Error making request: {e}")
        return False
    finally:
        session.close()

def main():
    parser = argparse.ArgumentParser(description="Trigger Jenkins job 'dev-nsxvpc' with memorized parameters")
    parser.add_argument("--jenkins-username", help="Jenkins username for basic authentication")
    parser.add_argument("--jenkins-token", help="Jenkins API token for authentication")
    parser.add_argument("--dry-run", action="store_true", help="Show what would be sent without actually triggering")
    parser.add_argument("--show-config", action="store_true", help="Show the memorized configuration")
    parser.add_argument("--sync-from-build", help="Fetch parameters from the specified Jenkins build and use them (e.g., 8454)")
    
    args = parser.parse_args()

    # Credentials: prefer CLI args, fallback to env vars
    jenkins_username = args.jenkins_username or os.environ.get("JENKINS_USERNAME")
    jenkins_token = args.jenkins_token or os.environ.get("JENKINS_TOKEN")
    if args.jenkins_username is None and os.environ.get("JENKINS_USERNAME"):
        logger.info("Using JENKINS_USERNAME from environment")
    if args.jenkins_token is None and os.environ.get("JENKINS_TOKEN"):
        logger.info("Using JENKINS_TOKEN from environment")
    
    if args.show_config:
        logger.info("=== Memorized Jenkins Job Configuration ===")
        logger.info(f"Job Name: {JOB_NAME}")
        logger.info(f"Jenkins URL: {JENKINS_BASE_URL}")
        logger.info("\nParameters:")
        for key, value in JOB_PARAMETERS.items():
            logger.info(f"  {key}: {value}")
        return
    
    override = None
    if args.sync_from_build:
        session = requests.Session()
        crumb_value, crumb_field, auth_type, auth_value = get_jenkins_crumb(session, jenkins_username, jenkins_token)
        if not auth_type:
            logger.error("Authentication required to fetch parameters from Jenkins build. Provide --jenkins-username and --jenkins-token.")
            sys.exit(1)
        fetched = fetch_parameters_from_build(session, args.sync_from_build, auth_type, auth_value)
        session.close()
        if not fetched:
            logger.error("Could not fetch parameters from the specified build")
            sys.exit(1)
        override = JOB_PARAMETERS.copy()
        override.update(fetched)
        logger.info(f"Overriding parameters with values from build {args.sync_from_build}. Overridden keys: "
                    f"{[k for k in fetched.keys() if JOB_PARAMETERS.get(k) != fetched[k]]}")

    success = trigger_jenkins_job(
        jenkins_username=jenkins_username,
        jenkins_token=jenkins_token,
        dry_run=args.dry_run,
        override_params=override,
    )
    
    if not success and not args.dry_run:
        sys.exit(1)

if __name__ == "__main__":
    main()
