#!/usr/bin/env python3
"""
Script to trigger Jenkins job 'dev-nsxvpc' with the same parameters as build #7355
Usage: python3 trigger_jenkins_job.py [--jenkins-token TOKEN] [--dry-run]
python3 trigger_jenkins_job.py --jenkins-username xz037905 --jenkins-token 116d1f6040d9dafad15f7bcb5869a0a2c7
"""

import json
import requests
import argparse
import sys
from urllib.parse import urljoin

# Jenkins configuration
JENKINS_BASE_URL = "https://jenkins-vcf-wcp-dev.devops.broadcom.net"
JOB_NAME = "dev-nsxvpc"

# Job parameters from build #7355
JOB_PARAMETERS = {
    "TERA_REF": "",
    "PERFORCE_BRANCH": "main",
    "SKIP_CLEANUP": False,
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
    "GUESTCLUSTER_SETUP": True,
    "GC_OVA_BUILD": "",
    "NSXT_BUILD": "ob-24886628",
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
    "TESTS_TO_RUN": "none",
    "TEST_GROUPS": "none",
    "NSX_VDS_VERSION": "0",
    "TKG_SVS_CONFIG_OVERRIDE": "vpc_supported: true\nworkload_domain_isolation_supported: true",
    "NSX_VPC": True,
    "NSX_LOAD_BALANCER": "nsx-lb",
    "TGW_TYPE": "centralized",
    "PRIVATE_INFRA": "PUBLIC",
    "USE_INSTAPP": False
}

def format_parameters_for_jenkins(parameters):
    """Convert parameters to Jenkins REST API format"""
    json_params = []
    for key, value in parameters.items():
        if isinstance(value, bool):
            json_params.append({
                "name": key,
                "value": value
            })
        else:
            json_params.append({
                "name": key,
                "value": str(value)
            })
    return json_params

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
                print(f"Successfully authenticated using {auth_type} auth")
                return crumb_data.get('crumb'), crumb_data.get('crumbRequestField', 'Jenkins-Crumb'), auth_type, auth_value
            else:
                print(f"Warning: {auth_type} auth failed. Status: {response.status_code}")
                
        except Exception as e:
            print(f"Warning: Error with {auth_type} auth: {e}")
    
    print("Warning: All authentication methods failed")
    return None, None, None, None

def trigger_jenkins_job(jenkins_username=None, jenkins_token=None, dry_run=False):
    """Trigger the Jenkins job with the specified parameters"""
    
    # Create a session to maintain cookies
    session = requests.Session()
    
    # Prepare the URL
    build_url = f"{JENKINS_BASE_URL}/job/{JOB_NAME}/buildWithParameters"
    
    # Get Jenkins crumb for CSRF protection and determine auth method
    crumb_value, crumb_field, auth_type, auth_value = get_jenkins_crumb(session, jenkins_username, jenkins_token)
    
    # Prepare form data with job parameters
    form_data = JOB_PARAMETERS.copy()
    
    # Add crumb to form data if available
    if crumb_value and crumb_field:
        form_data[crumb_field] = crumb_value
        print(f"Using CSRF crumb: {crumb_field}")
    
    print(f"Jenkins URL: {build_url}")
    print(f"Job Name: {JOB_NAME}")
    print(f"Number of parameters: {len(JOB_PARAMETERS)}")
    
    if dry_run:
        print("\n=== DRY RUN MODE ===")
        print("Would send the following parameters:")
        for key, value in form_data.items():
            if key != crumb_field:  # Don't print the crumb value
                print(f"  {key}: {value}")
        print(f"\nAuthentication method: {auth_type}")
        if crumb_value:
            print(f"Crumb field '{crumb_field}' included in form data")
        return True
    
    try:
        print("\nTriggering Jenkins job...")
        
        # Send request using the same authentication method that worked for crumb
        if auth_type == "basic":
            response = session.post(build_url, auth=auth_value, data=form_data, timeout=30)
        elif auth_type == "bearer":
            headers = {"Authorization": auth_value}
            response = session.post(build_url, headers=headers, data=form_data, timeout=30)
        else:
            print("❌ No valid authentication method found")
            return False
        
        print(f"Response Status: {response.status_code}")
        
        if response.status_code == 201:
            print("✅ Job triggered successfully!")
            location = response.headers.get('Location')
            if location:
                print(f"Queue item location: {location}")
        elif response.status_code == 200:
            print("✅ Job triggered successfully (status 200)!")
        else:
            print(f"❌ Failed to trigger job. Status code: {response.status_code}")
            print(f"Response body: {response.text}")
            return False
            
    except requests.exceptions.RequestException as e:
        print(f"❌ Error making request: {e}")
        return False
    finally:
        session.close()
    
    return True

def main():
    parser = argparse.ArgumentParser(description="Trigger Jenkins job 'dev-nsxvpc' with memorized parameters")
    parser.add_argument("--jenkins-username", help="Jenkins username for basic authentication")
    parser.add_argument("--jenkins-token", help="Jenkins API token for authentication")
    parser.add_argument("--dry-run", action="store_true", help="Show what would be sent without actually triggering")
    parser.add_argument("--show-config", action="store_true", help="Show the memorized configuration")
    
    args = parser.parse_args()
    
    if args.show_config:
        print("=== Memorized Jenkins Job Configuration ===")
        print(f"Job Name: {JOB_NAME}")
        print(f"Jenkins URL: {JENKINS_BASE_URL}")
        print("\nParameters:")
        for key, value in JOB_PARAMETERS.items():
            print(f"  {key}: {value}")
        return
    
    success = trigger_jenkins_job(jenkins_username=args.jenkins_username, jenkins_token=args.jenkins_token, dry_run=args.dry_run)
    
    if not success and not args.dry_run:
        sys.exit(1)

if __name__ == "__main__":
    main()
