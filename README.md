# Jenkins Job Configuration - dev-nsxvpc

This repository contains the memorized configuration and scripts to trigger the Jenkins job `dev-nsxvpc` with the same parameters as build #7355.

## Job Details

- **Jenkins URL**: https://jenkins-vcf-wcp-dev.devops.broadcom.net
- **Job Name**: dev-nsxvpc
- **Original Build**: #7355
- **Build URL**: https://jenkins-vcf-wcp-dev.devops.broadcom.net/view/all/job/dev-nsxvpc/7355/

## Files

### 1. `jenkins_job_config.json`
Contains the complete job configuration in JSON format, including all 51 parameters from build #7355.

### 2. `trigger_jenkins_job.py`
Python script to trigger the Jenkins job via REST API.

**Usage:**
```bash
# Show configuration
python3 trigger_jenkins_job.py --show-config

# Dry run (show what would be sent)
python3 trigger_jenkins_job.py --dry-run

# Trigger job (you'll need a Jenkins API token)
python3 trigger_jenkins_job.py --jenkins-token YOUR_TOKEN

# Trigger job without authentication (if Jenkins allows)
python3 trigger_jenkins_job.py
```

### 3. `trigger_jenkins_job.sh`
Bash script using curl to trigger the Jenkins job.

**Usage:**
```bash
# Make executable
chmod +x trigger_jenkins_job.sh

# Trigger job with token
./trigger_jenkins_job.sh YOUR_JENKINS_TOKEN

# Trigger job without token (if Jenkins allows)
./trigger_jenkins_job.sh
```

## Key Parameters from Build #7355

| Parameter | Value |
|-----------|-------|
| PERFORCE_BRANCH | main |
| OVA_BUILD | ob-24871681 |
| VC_BUILD | ob-24876732 |
| ESX_BUILD | ob-24876735 |
| NSXT_BUILD | ob-24886628 |
| WCP_BUILD | ob-24871682 |
| NSX_VPC | true |
| VLCM_CLUSTER | true |
| NSX_SETUP | true |
| GUESTCLUSTER_SETUP | true |
| TESTBED_POLICY | DELETE_NEVER |
| KEEP_TESTBED_HOURS | 168 |
| VDNET_BRANCH | rtqa-staging |
| NIMBUS_LOCATION | LVN |

## Authentication

To trigger jobs, you'll need a Jenkins API token. You can generate one from:
1. Go to Jenkins → Your Profile → Configure
2. Under "API Token", click "Add new Token"
3. Use this token with the scripts

## CSRF Protection

Jenkins has CSRF protection enabled, which requires a "crumb" to be included with requests. Both scripts have been updated to handle this automatically:

- **Python script**: Automatically fetches the Jenkins crumb using the `/crumbIssuer/api/json` endpoint
- **Bash script**: Uses curl to get the crumb and includes it in the request headers

### Troubleshooting 403 Errors

If you encounter a "403 No valid crumb was included in the request" error:

1. **Ensure you have a valid Jenkins API token**
2. **Check that the scripts can access the crumb issuer endpoint**
3. **Verify your permissions** - you need build permissions for the job

The scripts will automatically handle CSRF protection by:
- Fetching the crumb from Jenkins
- Including it in the request headers
- Using proper authentication

## REST API Endpoint

The job is triggered using:
```
POST https://jenkins-vcf-wcp-dev.devops.broadcom.net/job/dev-nsxvpc/buildWithParameters
```

With parameters sent as form data or JSON payload.

## Features

- **Complete parameter preservation**: All 51 parameters from the original build are included
- **Multiple trigger methods**: Python script and bash/curl script
- **Dry run support**: Test what would be sent without actually triggering
- **Token-based authentication**: Support for Jenkins API tokens
- **Configuration display**: View all memorized parameters

## Example Usage

```bash
# Test the configuration
python3 trigger_jenkins_job.py --show-config

# Do a dry run first
python3 trigger_jenkins_job.py --dry-run

# Actually trigger the job (replace with your token)
python3 trigger_jenkins_job.py --jenkins-token your_api_token_here
```

This setup allows you to reliably reproduce the exact same Jenkins job configuration as build #7355 using REST API calls.
