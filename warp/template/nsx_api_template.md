# NSX Policy API Tutorial: Using curl for Testing and Debugging

A comprehensive guide for interacting with NSX Policy API using curl commands.

---

## Table of Contents

1. [Basic Setup](#1-basic-setup)
2. [Authentication](#2-authentication)
3. [HTTP Methods Overview](#3-http-methods-overview)
4. [Common NSX Resources](#4-common-nsx-resources)
5. [Working with Tier0 Routers](#5-working-with-tier0-routers)
6. [Working with Prefix Lists](#6-working-with-prefix-lists)
7. [Working with Route Maps](#7-working-with-route-maps)
8. [Working with Route Redistribution](#8-working-with-route-redistribution)
9. [Query and Filter Results](#9-query-and-filter-results)
10. [Real-World Testing Scenarios](#10-real-world-testing-scenarios)
11. [Troubleshooting Tips](#11-troubleshooting-tips)

---

## 1. Basic Setup

### Environment Variables

Always set these variables at the beginning of your session:

```bash
# NSX Manager details
NSX_IP="10.161.112.209"
NSX_USER="admin"
NSX_PASS="your_password"

# Resource identifiers
T0_ROUTER="ContainerT0"
LOCALE_SERVICE="tier0localeservices"
CLUSTER_ID="your-cluster-id"

# Create base64 auth header
AUTH=$(echo -n "${NSX_USER}:${NSX_PASS}" | base64)
```
### Base URL Structure

NSX Policy API follows this pattern:
```
https://{NSX_IP}/policy/api/v1/infra/{resource-type}/{resource-id}
```
---

## 2. Authentication

### Basic Authentication

NSX API uses HTTP Basic Authentication:

```bash
# Method 1: Using base64 encoded credentials
AUTH=$(echo -n "${NSX_USER}:${NSX_PASS}" | base64)
curl -k -H "Authorization: Basic ${AUTH}" ...

# Method 2: Using curl's built-in basic auth
curl -k -u "${NSX_USER}:${NSX_PASS}" ...
```
**Note**: Always use `-k` flag to skip certificate verification in test environments.

---

## 3. HTTP Methods Overview

### GET - Retrieve Resources

```bash
# Get single resource
curl -k -s -X GET "https://${NSX_IP}/policy/api/v1/infra/tier-0s/${T0_ROUTER}" \
  -H "Authorization: Basic ${AUTH}" \
  -H "Accept: application/json"

# List all resources
curl -k -s -X GET "https://${NSX_IP}/policy/api/v1/infra/tier-0s/${T0_ROUTER}/prefix-lists" \
  -H "Authorization: Basic ${AUTH}"
```
### POST - Create Resources (Not commonly used in Policy API)

Policy API typically uses PUT for creation.

### PUT - Create or Replace Resources

```bash
# Create a new resource (must include all required fields)
curl -k -X PUT "https://${NSX_IP}/policy/api/v1/infra/tier-0s/${T0_ROUTER}/prefix-lists/my-prefix-list" \
  -H "Authorization: Basic ${AUTH}" \
  -H "Content-Type: application/json" \
  -d '{
  "resource_type": "PrefixList",
  "id": "my-prefix-list",
  "display_name": "My Prefix List",
  "prefixes": [...]
}'
```
**Important**:
- PUT will fail if resource already exists (error 500127)
- Use PATCH to update existing resources

### PATCH - Update Existing Resources

```bash
# Update only specific fields
curl -k -X PATCH "https://${NSX_IP}/policy/api/v1/infra/tier-0s/${T0_ROUTER}/prefix-lists/my-prefix-list" \
  -H "Authorization: Basic ${AUTH}" \
  -H "Content-Type: application/json" \
  -d '{
  "prefixes": [...]
}'
```
**Benefits of PATCH**:
- Updates only specified fields
- No need to send entire resource body
- Safer for partial updates

### DELETE - Remove Resources

```bash
curl -k -X DELETE "https://${NSX_IP}/policy/api/v1/infra/tier-0s/${T0_ROUTER}/prefix-lists/my-prefix-list" \
  -H "Authorization: Basic ${AUTH}"
```
---

## 4. Common NSX Resources

### Resource Hierarchy

```
/infra
  /tier-0s/{tier0-id}
    /locale-services/{service-id}
      /route-redistribution-config
    /route-maps/{route-map-id}
    /prefix-lists/{prefix-list-id}
  /tier-1s/{tier1-id}
  /segments/{segment-id}
```
### Common Resource Types

- **Tier0RouteMap**: BGP route maps
- **PrefixList**: IP prefix lists for routing policies
- **LocaleServices**: Tier0/Tier1 locale-specific configurations
- **Tier0**: Tier-0 gateway configurations

---

## 5. Working with Tier0 Routers

### Get Tier0 Information

```bash
# Get Tier0 basic info
curl -k -s "https://${NSX_IP}/policy/api/v1/infra/tier-0s/${T0_ROUTER}" \
  -H "Authorization: Basic ${AUTH}" | jq '.'

# Get locale services
curl -k -s "https://${NSX_IP}/policy/api/v1/infra/tier-0s/${T0_ROUTER}/locale-services" \
  -H "Authorization: Basic ${AUTH}" | jq '.results[]'
```
### Get BGP Configuration

```bash
curl -k -s "https://${NSX_IP}/policy/api/v1/infra/tier-0s/${T0_ROUTER}/locale-services/${LOCALE_SERVICE}/bgp" \
  -H "Authorization: Basic ${AUTH}" | jq '.'
```
---

## 6. Working with Prefix Lists

### List All Prefix Lists

```bash
# Get all prefix lists
curl -k -s "https://${NSX_IP}/policy/api/v1/infra/tier-0s/${T0_ROUTER}/prefix-lists" \
  -H "Authorization: Basic ${AUTH}" | jq '.results[]'

# Filter specific fields
curl -k -s "https://${NSX_IP}/policy/api/v1/infra/tier-0s/${T0_ROUTER}/prefix-lists" \
  -H "Authorization: Basic ${AUTH}" | jq '.results[] | {id: .id, path: .path, tags: .tags}'

# Filter non-system prefix lists
curl -k -s "https://${NSX_IP}/policy/api/v1/infra/tier-0s/${T0_ROUTER}/prefix-lists" \
  -H "Authorization: Basic ${AUTH}" | jq '.results[] | select(._system_owned == false)'
```
### Get Single Prefix List

```bash
curl -k -s "https://${NSX_IP}/policy/api/v1/infra/tier-0s/${T0_ROUTER}/prefix-lists/pl_my_list" \
  -H "Authorization: Basic ${AUTH}" | jq '.'
```
### Create Prefix List

```bash
# User-created prefix list
curl -k -X PUT "https://${NSX_IP}/policy/api/v1/infra/tier-0s/${T0_ROUTER}/prefix-lists/pl_user_networks" \
  -H "Authorization: Basic ${AUTH}" \
  -H "Content-Type: application/json" \
  -d '{
  "resource_type": "PrefixList",
  "id": "pl_user_networks",
  "display_name": "User Networks",
  "prefixes": [
    {
      "network": "10.10.0.0/16",
      "action": "PERMIT"
    },
    {
      "network": "10.20.0.0/16",
      "le": 24,
      "action": "PERMIT"
    }
  ],
  "tags": [
    {
      "scope": "owner",
      "tag": "network-admin"
    }
  ]
}'

# NCP-created prefix list (with cluster tags)
curl -k -X PUT "https://${NSX_IP}/policy/api/v1/infra/tier-0s/${T0_ROUTER}/prefix-lists/pl_${CLUSTER_ID}_deny_subnets" \
  -H "Authorization: Basic ${AUTH}" \
  -H "Content-Type: application/json" \
  -d '{
  "resource_type": "PrefixList",
  "id": "pl_'${CLUSTER_ID}'_deny_subnets",
  "display_name": "pl-'${CLUSTER_ID}'-deny-subnets",
  "prefixes": [
    {
      "network": "172.26.0.0/16",
      "le": 28,
      "action": "PERMIT"
    }
  ],
  "tags": [
    {
      "scope": "ncp/created_for",
      "tag": "ncp/subnets_deny_rule"
    },
    {
      "scope": "ncp/cluster",
      "tag": "'${CLUSTER_ID}'"
    },
    {
      "scope": "ncp/version",
      "tag": "1.2.0"
    }
  ]
}'
```
### Update Prefix List

```bash
# Update using PATCH (only updates specified fields)
curl -k -X PATCH "https://${NSX_IP}/policy/api/v1/infra/tier-0s/${T0_ROUTER}/prefix-lists/pl_user_networks" \
  -H "Authorization: Basic ${AUTH}" \
  -H "Content-Type: application/json" \
  -d '{
  "prefixes": [
    {
      "network": "10.10.0.0/16",
      "action": "PERMIT"
    },
    {
      "network": "10.30.0.0/16",
      "action": "PERMIT"
    }
  ]
}'
```
### Delete Prefix List

```bash
curl -k -X DELETE "https://${NSX_IP}/policy/api/v1/infra/tier-0s/${T0_ROUTER}/prefix-lists/pl_user_networks" \
  -H "Authorization: Basic ${AUTH}"
```
---

## 7. Working with Route Maps

### List All Route Maps

```bash
curl -k -s "https://${NSX_IP}/policy/api/v1/infra/tier-0s/${T0_ROUTER}/route-maps" \
  -H "Authorization: Basic ${AUTH}" | jq '.results[]'
```
### Get Single Route Map

```bash
curl -k -s "https://${NSX_IP}/policy/api/v1/infra/tier-0s/${T0_ROUTER}/route-maps/rm_deny_t1_subnets" \
  -H "Authorization: Basic ${AUTH}" | jq '.'
```
### Create Route Map

```bash
# Create route map with user ownership
curl -k -X PUT "https://${NSX_IP}/policy/api/v1/infra/tier-0s/${T0_ROUTER}/route-maps/rm_my_routes" \
  -H "Authorization: Basic ${AUTH}" \
  -H "Content-Type: application/json" \
  -d '{
  "resource_type": "Tier0RouteMap",
  "id": "rm_my_routes",
  "display_name": "My Route Map",
  "entries": [
    {
      "action": "DENY",
      "prefix_list_matches": [
        "/infra/tier-0s/'${T0_ROUTER}'/prefix-lists/pl_user_networks"
      ]
    },
    {
      "action": "PERMIT",
      "prefix_list_matches": [
        "/infra/tier-0s/'${T0_ROUTER}'/prefix-lists/prefixlist-out-default"
      ]
    }
  ],
  "tags": [
    {
      "scope": "owner",
      "tag": "manual-config"
    }
  ]
}'

# Create NCP-owned route map
curl -k -X PUT "https://${NSX_IP}/policy/api/v1/infra/tier-0s/${T0_ROUTER}/route-maps/rm_deny_t1_subnets" \
  -H "Authorization: Basic ${AUTH}" \
  -H "Content-Type: application/json" \
  -d '{
  "resource_type": "Tier0RouteMap",
  "id": "rm_deny_t1_subnets",
  "display_name": "rm-deny-t1-subnets",
  "entries": [
    {
      "action": "DENY",
      "prefix_list_matches": [
        "/infra/tier-0s/'${T0_ROUTER}'/prefix-lists/pl_'${CLUSTER_ID}'_deny_t1_subnets"
      ]
    },
    {
      "action": "PERMIT",
      "prefix_list_matches": [
        "/infra/tier-0s/'${T0_ROUTER}'/prefix-lists/prefixlist-out-default"
      ]
    }
  ],
  "tags": [
    {
      "scope": "ncp/created_for",
      "tag": "ncp/subnets_deny_rule"
    },
    {
      "scope": "ncp/cluster",
      "tag": "'${CLUSTER_ID}'"
    }
  ]
}'
```
### Update Route Map

```bash
# Use PATCH to update existing route map
curl -k -X PATCH "https://${NSX_IP}/policy/api/v1/infra/tier-0s/${T0_ROUTER}/route-maps/rm_my_routes" \
  -H "Authorization: Basic ${AUTH}" \
  -H "Content-Type: application/json" \
  -d '{
  "entries": [
    {
      "action": "DENY",
      "prefix_list_matches": [
        "/infra/tier-0s/'${T0_ROUTER}'/prefix-lists/pl_user_networks",
        "/infra/tier-0s/'${T0_ROUTER}'/prefix-lists/pl_additional_list"
      ]
    },
    {
      "action": "PERMIT",
      "prefix_list_matches": [
        "/infra/tier-0s/'${T0_ROUTER}'/prefix-lists/prefixlist-out-default"
      ]
    }
  ]
}'
```
### Delete Route Map

```bash
curl -k -X DELETE "https://${NSX_IP}/policy/api/v1/infra/tier-0s/${T0_ROUTER}/route-maps/rm_my_routes" \
  -H "Authorization: Basic ${AUTH}"
```
---

## 8. Working with Route Redistribution

### Get Route Redistribution Config

```bash
curl -k -s "https://${NSX_IP}/policy/api/v1/infra/tier-0s/${T0_ROUTER}/locale-services/${LOCALE_SERVICE}" \
  -H "Authorization: Basic ${AUTH}" | jq '.route_redistribution_config'
```
### Update Route Redistribution Config

```bash
# Add TIER1_CONNECTED and TIER1_SEGMENT to redistribution types
curl -k -X PATCH "https://${NSX_IP}/policy/api/v1/infra/tier-0s/${T0_ROUTER}/locale-services/${LOCALE_SERVICE}" \
  -H "Authorization: Basic ${AUTH}" \
  -H "Content-Type: application/json" \
  -d '{
  "route_redistribution_config": {
    "bgp_enabled": true,
    "ospf_enabled": false,
    "redistribution_rules": [{
      "route_redistribution_types": [
        "TIER0_EXTERNAL_INTERFACE",
        "TIER0_SEGMENT",
        "TIER0_STATIC",
        "TIER1_LB_VIP",
        "TIER1_LB_SNAT",
        "TIER1_CONNECTED",
        "TIER1_SEGMENT"
      ],
      "destinations": ["BGP"]
    }]
  }
}'
```
### Link Route Map to Redistribution

```bash
curl -k -X PATCH "https://${NSX_IP}/policy/api/v1/infra/tier-0s/${T0_ROUTER}/locale-services/${LOCALE_SERVICE}" \
  -H "Authorization: Basic ${AUTH}" \
  -H "Content-Type: application/json" \
  -d '{
  "route_redistribution_config": {
    "bgp_enabled": true,
    "redistribution_rules": [{
      "route_redistribution_types": [
        "TIER0_EXTERNAL_INTERFACE",
        "TIER0_SEGMENT",
        "TIER0_STATIC",
        "TIER1_LB_VIP",
        "TIER1_LB_SNAT",
        "TIER1_CONNECTED",
        "TIER1_SEGMENT"
      ],
      "destinations": ["BGP"],
      "route_map_path": "/infra/tier-0s/'${T0_ROUTER}'/route-maps/rm_deny_t1_subnets"
    }]
  }
}'
```
---

## 9. Query and Filter Results

### Using jq for JSON Processing

#### Basic Field Selection

```bash
# Select specific fields
curl -k -s "https://${NSX_IP}/policy/api/v1/infra/tier-0s/${T0_ROUTER}/prefix-lists" \
  -H "Authorization: Basic ${AUTH}" | jq '.results[] | {id: .id, path: .path, tags: .tags}'
```
#### Filter by Conditions

```bash
# Filter non-system resources
curl -k -s "https://${NSX_IP}/policy/api/v1/infra/tier-0s/${T0_ROUTER}/prefix-lists" \
  -H "Authorization: Basic ${AUTH}" | jq '.results[] | select(._system_owned == false)'

# Filter by tag
curl -k -s "https://${NSX_IP}/policy/api/v1/infra/tier-0s/${T0_ROUTER}/prefix-lists" \
  -H "Authorization: Basic ${AUTH}" | jq '.results[] | select(.tags[]? | select(.scope == "ncp/cluster"))'
```
#### Extract Nested Fields

```bash
# Get route map entries
curl -k -s "https://${NSX_IP}/policy/api/v1/infra/tier-0s/${T0_ROUTER}/route-maps/rm_deny_t1_subnets" \
  -H "Authorization: Basic ${AUTH}" | jq '.entries[0].prefix_list_matches'

# Get redistribution route types
curl -k -s "https://${NSX_IP}/policy/api/v1/infra/tier-0s/${T0_ROUTER}/locale-services/${LOCALE_SERVICE}" \
  -H "Authorization: Basic ${AUTH}" | jq '.route_redistribution_config.redistribution_rules[0].route_redistribution_types'
```
#### Count Results

```bash
# Count total prefix lists
curl -k -s "https://${NSX_IP}/policy/api/v1/infra/tier-0s/${T0_ROUTER}/prefix-lists" \
  -H "Authorization: Basic ${AUTH}" | jq '.results | length'
```
#### Pretty Print

```bash
# Format JSON output nicely
curl -k -s "https://${NSX_IP}/policy/api/v1/infra/tier-0s/${T0_ROUTER}/route-maps/rm_deny_t1_subnets" \
  -H "Authorization: Basic ${AUTH}" | jq '.'
```
---

## 10. Real-World Testing Scenarios

### Scenario 1: Test NCP-Owned Route Map Cleanup

**Setup**: Create resources owned by current NCP cluster

```bash
# 1. Create NCP-owned prefix list
curl -k -X PUT "https://${NSX_IP}/policy/api/v1/infra/tier-0s/${T0_ROUTER}/prefix-lists/pl_${CLUSTER_ID}_deny_t1_subnets" \
  -H "Authorization: Basic ${AUTH}" \
  -H "Content-Type: application/json" \
  -d '{
  "resource_type": "PrefixList",
  "id": "pl_'${CLUSTER_ID}'_deny_t1_subnets",
  "display_name": "pl-'${CLUSTER_ID}'-deny-t1-subnets",
  "prefixes": [{
    "network": "172.26.0.0/16",
    "le": 28,
    "action": "PERMIT"
  }],
  "tags": [
    {"scope": "ncp/created_for", "tag": "ncp/subnets_deny_rule"},
    {"scope": "ncp/cluster", "tag": "'${CLUSTER_ID}'"},
    {"scope": "ncp/version", "tag": "1.2.0"}
  ]
}'

# 2. Create NCP-owned route map (with cluster tag)
curl -k -X PUT "https://${NSX_IP}/policy/api/v1/infra/tier-0s/${T0_ROUTER}/route-maps/rm_deny_t1_subnets" \
  -H "Authorization: Basic ${AUTH}" \
  -H "Content-Type: application/json" \
  -d '{
  "resource_type": "Tier0RouteMap",
  "id": "rm_deny_t1_subnets",
  "display_name": "rm-deny-t1-subnets",
  "entries": [
    {
      "action": "DENY",
      "prefix_list_matches": ["/infra/tier-0s/'${T0_ROUTER}'/prefix-lists/pl_'${CLUSTER_ID}'_deny_t1_subnets"]
    },
    {
      "action": "PERMIT",
      "prefix_list_matches": ["/infra/tier-0s/'${T0_ROUTER}'/prefix-lists/prefixlist-out-default"]
    }
  ],
  "tags": [
    {"scope": "ncp/created_for", "tag": "ncp/subnets_deny_rule"},
    {"scope": "ncp/cluster", "tag": "'${CLUSTER_ID}'"}
  ]
}'
```
**Verify Before Cleanup**:

```bash
echo "=== Route Map ==="
curl -k -s "https://${NSX_IP}/policy/api/v1/infra/tier-0s/${T0_ROUTER}/route-maps/rm_deny_t1_subnets" \
  -H "Authorization: Basic ${AUTH}" | jq '{id: .id, tags: .tags}'

echo -e "\n=== Prefix List ==="
curl -k -s "https://${NSX_IP}/policy/api/v1/infra/tier-0s/${T0_ROUTER}/prefix-lists/pl_${CLUSTER_ID}_deny_t1_subnets" \
  -H "Authorization: Basic ${AUTH}" | jq '{id: .id, tags: .tags}'
```
**Expected After Cleanup**: Both resources completely deleted.

---

### Scenario 2: Test Mixed Ownership Route Map

**Setup**: Create route map with both user and NCP prefix lists

```bash
# 1. Create user-owned prefix lists
curl -k -X PUT "https://${NSX_IP}/policy/api/v1/infra/tier-0s/${T0_ROUTER}/prefix-lists/pl_user_prod_networks" \
  -H "Authorization: Basic ${AUTH}" \
  -H "Content-Type: application/json" \
  -d '{
  "resource_type": "PrefixList",
  "id": "pl_user_prod_networks",
  "display_name": "User Production Networks",
  "prefixes": [{"network": "10.10.0.0/16", "action": "PERMIT"}],
  "tags": [{"scope": "owner", "tag": "network-admin"}]
}'

curl -k -X PUT "https://${NSX_IP}/policy/api/v1/infra/tier-0s/${T0_ROUTER}/prefix-lists/pl_user_dmz_networks" \
  -H "Authorization: Basic ${AUTH}" \
  -H "Content-Type: application/json" \
  -d '{
  "resource_type": "PrefixList",
  "id": "pl_user_dmz_networks",
  "display_name": "User DMZ Networks",
  "prefixes": [{"network": "192.168.100.0/24", "action": "PERMIT"}],
  "tags": [{"scope": "owner", "tag": "security-team"}]
}'

# 2. Create NCP-owned prefix lists
curl -k -X PUT "https://${NSX_IP}/policy/api/v1/infra/tier-0s/${T0_ROUTER}/prefix-lists/pl_${CLUSTER_ID}_deny_t1_subnets" \
  -H "Authorization: Basic ${AUTH}" \
  -H "Content-Type: application/json" \
  -d '{
  "resource_type": "PrefixList",
  "id": "pl_'${CLUSTER_ID}'_deny_t1_subnets",
  "display_name": "pl-'${CLUSTER_ID}'-deny-t1-subnets",
  "prefixes": [{"network": "172.26.0.0/16", "le": 28, "action": "PERMIT"}],
  "tags": [
    {"scope": "ncp/created_for", "tag": "ncp/subnets_deny_rule"},
    {"scope": "ncp/cluster", "tag": "'${CLUSTER_ID}'"}
  ]
}'

curl -k -X PUT "https://${NSX_IP}/policy/api/v1/infra/tier-0s/${T0_ROUTER}/prefix-lists/pl_${CLUSTER_ID}_deny_services" \
  -H "Authorization: Basic ${AUTH}" \
  -H "Content-Type: application/json" \
  -d '{
  "resource_type": "PrefixList",
  "id": "pl_'${CLUSTER_ID}'_deny_services",
  "display_name": "pl-'${CLUSTER_ID}'-deny-services",
  "prefixes": [{"network": "172.27.0.0/16", "le": 24, "action": "PERMIT"}],
  "tags": [
    {"scope": "ncp/created_for", "tag": "ncp/subnets_deny_rule"},
    {"scope": "ncp/cluster", "tag": "'${CLUSTER_ID}'"}
  ]
}'

# 3. Create user-owned route map with mixed prefix lists (PATCH or DELETE+PUT)
curl -k -X DELETE "https://${NSX_IP}/policy/api/v1/infra/tier-0s/${T0_ROUTER}/route-maps/rm_deny_t1_subnets" \
  -H "Authorization: Basic ${AUTH}"

curl -k -X PUT "https://${NSX_IP}/policy/api/v1/infra/tier-0s/${T0_ROUTER}/route-maps/rm_deny_t1_subnets" \
  -H "Authorization: Basic ${AUTH}" \
  -H "Content-Type: application/json" \
  -d '{
  "resource_type": "Tier0RouteMap",
  "id": "rm_deny_t1_subnets",
  "display_name": "rm-deny-t1-subnets",
  "entries": [
    {
      "action": "DENY",
      "prefix_list_matches": [
        "/infra/tier-0s/'${T0_ROUTER}'/prefix-lists/pl_user_prod_networks",
        "/infra/tier-0s/'${T0_ROUTER}'/prefix-lists/pl_'${CLUSTER_ID}'_deny_t1_subnets",
        "/infra/tier-0s/'${T0_ROUTER}'/prefix-lists/pl_user_dmz_networks",
        "/infra/tier-0s/'${T0_ROUTER}'/prefix-lists/pl_'${CLUSTER_ID}'_deny_services"
      ]
    },
    {
      "action": "PERMIT",
      "prefix_list_matches": ["/infra/tier-0s/'${T0_ROUTER}'/prefix-lists/prefixlist-out-default"]
    }
  ],
  "tags": [
    {"scope": "ncp/created_for", "tag": "ncp/subnets_deny_rule"},
    {"scope": "owner", "tag": "manual-config"}
  ]
}'
```
**Verify Before Cleanup**:

```bash
echo "=== Route Map (Mixed Ownership) ==="
curl -k -s "https://${NSX_IP}/policy/api/v1/infra/tier-0s/${T0_ROUTER}/route-maps/rm_deny_t1_subnets" \
  -H "Authorization: Basic ${AUTH}" | jq '{id: .id, tags: .tags, deny_entries: .entries[0].prefix_list_matches}'
```
**Expected After Cleanup**:
- Route map still exists
- Only user prefix lists remain in DENY entry
- NCP prefix lists deleted

---

## 11. Troubleshooting Tips

### Common Errors

#### Error 500127: Resource Already Exists

```json
{
  "httpStatus": "BAD_REQUEST",
  "error_code": 500127,
  "error_message": "Cannot create an object... as it already exists."
}
```
**Solution**: Use `PATCH` instead of `PUT`, or delete the resource first.

#### Error 220: JSON Parse Error

```json
{
  "httpStatus": "BAD_REQUEST",
  "error_code": 220,
  "error_message": "Error during JSON data processing: Unexpected character"
}
```
**Solution**: Check for:
- Trailing commas in JSON arrays
- Unescaped quotes in string values
- Missing commas between elements

#### Resource Not Found (404)

**Solution**:
- Verify resource ID is correct
- Check if resource was already deleted
- Ensure proper path structure

### Debugging Tips

1. **Use `-v` flag to see full request/response**:
```bash
   curl -k -v "https://${NSX_IP}/policy/api/v1/..." \
     -H "Authorization: Basic ${AUTH}"
```
2. **Save response to file for inspection**:
```bash
   curl -k -s "https://${NSX_IP}/policy/api/v1/..." \
     -H "Authorization: Basic ${AUTH}" > response.json
```
3. **Check HTTP status code**:
```bash
   curl -k -w "\nHTTP Status: %{http_code}\n" "https://${NSX_IP}/policy/api/v1/..." \
     -H "Authorization: Basic ${AUTH}"
```
4. **Pretty print JSON for readability**:
```bash
   curl -k -s "https://${NSX_IP}/policy/api/v1/..." \
     -H "Authorization: Basic ${AUTH}" | jq '.' | less
```
5. **Test JSON payload before sending**:
```bash
   echo '{...}' | jq '.'  # Will show error if invalid JSON
```
---

## Quick Reference Card

```bash
# Setup
NSX_IP="10.161.112.209"
AUTH=$(echo -n "admin:password" | base64)

# GET - Retrieve
curl -k -s -X GET "https://${NSX_IP}/policy/api/v1/infra/..." -H "Authorization: Basic ${AUTH}"

# PUT - Create (fails if exists)
curl -k -X PUT "https://${NSX_IP}/policy/api/v1/infra/..." -H "Authorization: Basic ${AUTH}" -H "Content-Type: application/json" -d '{...}'

# PATCH - Update (only specified fields)
curl -k -X PATCH "https://${NSX_IP}/policy/api/v1/infra/..." -H "Authorization: Basic ${AUTH}" -H "Content-Type: application/json" -d '{...}'

# DELETE - Remove
curl -k -X DELETE "https://${NSX_IP}/policy/api/v1/infra/..." -H "Authorization: Basic ${AUTH}"

# Filter with jq
| jq '.results[] | {id: .id, tags: .tags}'
| jq '.results[] | select(._system_owned == false)'
```
---

**End of Tutorial**

This guide covers the essential patterns for interacting with NSX Policy API using curl. For specific API endpoints and parameters, refer to the official NSX-T API documentation.