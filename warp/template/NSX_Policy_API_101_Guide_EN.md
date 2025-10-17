# NSX Policy API 101 Guide

**Target Audience**: NSX beginners, developers, operations engineers  
**Learning Time**: 2-3 hours  
**Prerequisites**: Basic networking concepts, REST API fundamentals

---

## 📚 Table of Contents

1. [What is NSX](#1-what-is-nsx)
2. [NSX Policy API Introduction](#2-nsx-policy-api-introduction)
3. [Core Architecture Hierarchy](#3-core-architecture-hierarchy)
4. [Key Resource Types Explained](#4-key-resource-types-explained)
5. [API Usage in Practice](#5-api-usage-in-practice)
6. [Common Use Cases](#6-common-use-cases)
7. [Learning Path Recommendations](#7-learning-path-recommendations)
8. [FAQ](#8-faq)

---

## 1. What is NSX

### 1.1 NSX Overview

**VMware NSX** is a software-defined networking (SDN) and security platform that provides virtualized network and security services for data centers.

**Core Value**:
- 🌐 **Network Virtualization**: Abstract physical networks into software-defined logical networks
- 🔒 **Micro-segmentation Security**: Granular security policy control
- ⚡ **Rapid Deployment**: Automate network configuration via APIs
- 🔄 **Flexible Scaling**: Support for multi-cloud and container environments

### 1.2 Main NSX Components

```
┌─────────────────────────────────────────┐
│         NSX Manager (Control Plane)      │
│  - Management UI                         │
│  - Policy API                            │
│  - Configuration Management              │
└─────────────────────────────────────────┘
                 ↓
┌─────────────────────────────────────────┐
│         NSX Edge (Edge Nodes)            │
│  - Routing (Tier-0/Tier-1)              │
│  - Load Balancing                        │
│  - NAT/VPN                               │
└─────────────────────────────────────────┘
                 ↓
┌─────────────────────────────────────────┐
│         ESXi Hosts (Data Plane)          │
│  - Virtual Switches                      │
│  - Distributed Firewall                  │
│  - VPC/Segment                           │
└─────────────────────────────────────────┘
```

### 1.3 Two NSX Architectures

1. **NSX-T (Traditional Architecture)**
   - Tier-0/Tier-1 Gateways
   - Segments (Logical Switches)
   - Distributed Firewall
   
2. **NSX VPC (Next-Gen Architecture)** ⭐
   - VPC-based multi-tenancy isolation
   - Organization (Org) → Project → VPC hierarchy
   - Better suited for cloud-native and Kubernetes environments

---

## 2. NSX Policy API Introduction

### 2.1 What is Policy API

**NSX Policy API** is an **intent-driven** declarative API:
- You only declare "what you want" (desired state)
- NSX automatically calculates "how to achieve it" (implementation path)

### 2.2 Policy API vs Manager API

| Feature | Policy API | Manager API (Legacy) |
|---------|-----------|---------------------|
| Design Philosophy | Declarative (Intent) | Imperative (Steps) |
| Complexity | Simple | Complex |
| Hierarchy | Clear | Flat |
| Recommended | ✅ Recommended | ❌ Being Deprecated |

### 2.3 API Basics

**Base URL**: `https://<nsx-manager>/policy/api/v1/`

**Authentication**: HTTP Basic Authentication
```bash
curl -k -u admin:password \
  -H "Content-Type: application/json" \
  https://10.70.188.176/policy/api/v1/infra
```

**Common HTTP Methods**:
- `GET` - Query resources
- `PATCH` - Update resources (recommended)
- `PUT` - Create/replace resources
- `DELETE` - Delete resources

---

## 3. Core Architecture Hierarchy

### 3.1 Overall Hierarchy View

From our API analysis, NSX Policy API follows a clear hierarchical structure:

```
Level 4 (Top Level - 1 endpoint)
  └─ /policy/api/v1/org-root
      └─ Organization root node, entry point for all resources

Level 5 (Infrastructure Layer - 6 endpoints)
  ├─ /policy/api/v1/search/query (Search API)
  ├─ /policy/api/v1/infra/ip-blocks (IP address pools)
  ├─ /policy/api/v1/infra/certificates (Certificate management)
  └─ ...

Level 6 (Functional Module Layer - 89 endpoints)
  ├─ /policy/api/v1/infra/lb-pools/* (Load balancer pools)
  ├─ /policy/api/v1/infra/lb-virtual-servers/* (Virtual servers)
  ├─ /policy/api/v1/infra/domains/* (Security domains)
  └─ ...

Level 7-14 (Detailed Resource Layer - 320 endpoints)
  └─ /orgs/default/projects/project-quality/vpcs/.../subnets/.../ports/...
      └─ Complete VPC resource hierarchy
```

### 3.2 Two Main Architecture Paths

#### Path 1: Traditional Infra Architecture

```
/policy/api/v1/infra/
  ├─ tier-0s/                  # Tier-0 Gateways
  ├─ tier-1s/                  # Tier-1 Gateways
  ├─ segments/                 # Network Segments
  ├─ domains/                  # Security Domains
  │   ├─ groups/               # Security Groups
  │   └─ security-policies/    # Security Policies
  └─ lb-pools/                 # Load Balancer Pools
```

#### Path 2: VPC Architecture ⭐ (Modern)

```
/policy/api/v1/org-root
  └─ /orgs/{org-id}/                    # Organization
      └─ /projects/{project-id}/        # Project
          └─ /vpcs/{vpc-id}/            # VPC (Isolated Virtual Network)
              ├─ /subnets/{subnet-id}/  # Subnet
              │   └─ /ports/{port-id}/  # Port (VM/Pod Connection Point)
              ├─ /vpc-lbs/{lb-id}/      # VPC Load Balancer
              └─ /security-policies/    # VPC Security Policies
```

### 3.3 Hierarchy Relationship Details

**Key Concepts**:
1. **Organization (Org)** = Top-level tenant isolation
2. **Project** = Resource grouping within an organization
3. **VPC** = Isolated network space within a project
4. **Subnet** = IP address range within a VPC
5. **Port** = Network interface for VMs or Pods

**Real Example**:
```
Organization: default
  └─ Project: project-quality
      └─ VPC: web-app-vpc
          ├─ Subnet: pod-subnet (172.26.0.0/16)
          │   ├─ Port: web-pod-1 (172.26.1.10)
          │   └─ Port: web-pod-2 (172.26.1.11)
          └─ Load Balancer: web-lb
```

---

## 4. Key Resource Types Explained

### 4.1 Search API - Your Starting Point

**Endpoint**: `/policy/api/v1/search/query`

**Purpose**: Search and discover any resource in NSX

**Example Queries**:
```bash
# Find all VPCs
GET /policy/api/v1/search/query?query=resource_type:Vpc

# Find domains for a specific cluster
GET /policy/api/v1/search/query?query=resource_type:Domain AND tags.scope:ncp/cluster AND tags.tag:cluster-id
```

**Response Example**:
```json
{
  "results": [
    {
      "resource_type": "Vpc",
      "id": "web-vpc",
      "display_name": "Web Application VPC",
      "path": "/orgs/default/projects/project-1/vpcs/web-vpc"
    }
  ],
  "result_count": 1
}
```

### 4.2 Organization Root (org-root)

**Endpoint**: `/policy/api/v1/org-root`

**Purpose**: Top-level entry point for all VPC resources

**Use Cases**:
- Create entire VPC hierarchy structure
- Batch update multiple VPCs
- Retrieve organization-level configuration

**Hierarchy Structure**:
```json
{
  "OrgRoot": {
    "children": [
      {
        "Org": {
          "id": "default",
          "children": [
            {
              "Project": {
                "id": "project-quality",
                "children": [
                  {
                    "Vpc": {
                      "id": "web-vpc",
                      "private_ips": ["172.26.0.0/16"]
                    }
                  }
                ]
              }
            }
          ]
        }
      }
    ]
  }
}
```

### 4.3 VPC (Virtual Private Cloud)

**Endpoint Pattern**: `/orgs/{org}/projects/{project}/vpcs/{vpc-id}`

**Key Attributes**:
```json
{
  "id": "web-app-vpc",
  "display_name": "Web Application VPC",
  "ip_address_type": "IPV4",
  "private_ips": ["172.26.0.0/16"],
  "tags": [
    {"scope": "nsx-op/cluster", "tag": "cluster-id"},
    {"scope": "nsx-op/namespace", "tag": "web-app"}
  ]
}
```

**VPC Purpose**:
- 🔒 **Network Isolation**: Different VPCs are isolated by default
- 📦 **Resource Container**: Contains subnets, ports, security policies
- 🏷️ **Tag Management**: Associate with Kubernetes namespaces via tags

### 4.4 Subnet

**Endpoint Pattern**: `/orgs/{org}/projects/{project}/vpcs/{vpc}/subnets/{subnet-id}`

**Key Attributes**:
```json
{
  "id": "pod-subnet",
  "display_name": "Pod Network Subnet",
  "ipv4_subnet_size": 16,
  "access_mode": "Private_TGW",
  "subnet_dhcp_config": {
    "mode": "DHCP_DEACTIVATED"
  }
}
```

**Subnet Types**:
- **Pod Subnet**: For Kubernetes Pods
- **User Subnet**: For Virtual Machines
- **DHCP Subnet**: Auto-assign IP addresses

### 4.5 Port

**Endpoint Pattern**: `/orgs/{org}/projects/{project}/vpcs/{vpc}/subnets/{subnet}/ports/{port-id}`

**Key Attributes**:
```json
{
  "id": "web-pod-1",
  "display_name": "web-deployment-abc123",
  "attachment": {
    "type": "INDEPENDENT",
    "app_id": "pod-uuid",
    "allocate_addresses": "BOTH"
  },
  "tags": [
    {"scope": "nsx-op/pod_name", "tag": "web-deployment-abc123"},
    {"scope": "nsx-op/namespace", "tag": "production"}
  ]
}
```

**Port Purpose**:
- Connection point: Interface for VMs or Pods to connect to the network
- IP allocation: Obtain IP addresses from the subnet
- Security policy enforcement point: Firewall rules applied at port level

### 4.6 Load Balancers

#### LB Pool (Backend Server Pool)
**Endpoint**: `/policy/api/v1/infra/lb-pools/{pool-id}`

```json
{
  "id": "web-svc-pool",
  "display_name": "Web Service Pool",
  "members": [
    {"ip_address": "172.26.1.10", "port": "80"},
    {"ip_address": "172.26.1.11", "port": "80"}
  ]
}
```

#### LB Virtual Server (Frontend Listener)
**Endpoint**: `/policy/api/v1/infra/lb-virtual-servers/{vs-id}`

```json
{
  "id": "web-svc-vs",
  "display_name": "Web Service Virtual Server",
  "ip_address": "10.0.0.100",
  "ports": ["80"],
  "pool_path": "/infra/lb-pools/web-svc-pool"
}
```

### 4.7 Security-Related Resources

#### Security Domain
**Endpoint**: `/policy/api/v1/infra/domains/{domain-id}`

**Purpose**: Logical grouping for organizing security policies

#### Security Group
**Endpoint**: `/policy/api/v1/infra/domains/{domain}/groups/{group-id}`

```json
{
  "id": "web-servers",
  "display_name": "Web Server Group",
  "expression": [
    {
      "resource_type": "Condition",
      "member_type": "VirtualMachine",
      "key": "Tag",
      "operator": "EQUALS",
      "value": "web|app"
    }
  ]
}
```

#### Security Policy
**Endpoint**: `/policy/api/v1/infra/domains/{domain}/security-policies/{policy-id}`

**Purpose**: Define firewall rules to control traffic

---

## 5. API Usage in Practice

### 5.1 Environment Setup

```bash
# Set environment variables
export NSX_MANAGER="10.70.188.176"
export NSX_USER="admin"
export NSX_PASS="your-password"

# Create authentication header
export AUTH=$(echo -n "${NSX_USER}:${NSX_PASS}" | base64)
```

### 5.2 Basic Query Operations

#### Get All VPCs
```bash
curl -k -X GET \
  "https://${NSX_MANAGER}/policy/api/v1/search/query?query=resource_type:Vpc" \
  -H "Authorization: Basic ${AUTH}" \
  -H "Accept: application/json" | jq '.'
```

#### Get Specific VPC Details
```bash
curl -k -X GET \
  "https://${NSX_MANAGER}/policy/api/v1/orgs/default/projects/project-quality/vpcs/web-vpc" \
  -H "Authorization: Basic ${AUTH}" | jq '.'
```

#### List All Subnets Under a VPC
```bash
curl -k -X GET \
  "https://${NSX_MANAGER}/policy/api/v1/orgs/default/projects/project-quality/vpcs/web-vpc/subnets" \
  -H "Authorization: Basic ${AUTH}" | jq '.results[] | {id: .id, display_name: .display_name}'
```

### 5.3 Create Resource Operations

#### Create Subnet
```bash
curl -k -X PATCH \
  "https://${NSX_MANAGER}/policy/api/v1/orgs/default/projects/project-quality/vpcs/web-vpc/subnets/my-subnet" \
  -H "Authorization: Basic ${AUTH}" \
  -H "Content-Type: application/json" \
  -d '{
    "id": "my-subnet",
    "display_name": "My Application Subnet",
    "ipv4_subnet_size": 24,
    "access_mode": "Private_TGW"
  }'
```

#### Create Port
```bash
curl -k -X PATCH \
  "https://${NSX_MANAGER}/policy/api/v1/orgs/default/projects/project-quality/vpcs/web-vpc/subnets/my-subnet/ports/my-port" \
  -H "Authorization: Basic ${AUTH}" \
  -H "Content-Type: application/json" \
  -d '{
    "id": "my-port",
    "display_name": "My VM Port",
    "tags": [
      {"scope": "app", "tag": "web"}
    ]
  }'
```

### 5.4 Update Resource Operations

Using `PATCH` method allows updating only specific fields:

```bash
curl -k -X PATCH \
  "https://${NSX_MANAGER}/policy/api/v1/orgs/default/projects/project-quality/vpcs/web-vpc" \
  -H "Authorization: Basic ${AUTH}" \
  -H "Content-Type: application/json" \
  -d '{
    "display_name": "Web Application VPC (Updated)"
  }'
```

### 5.5 Delete Resource Operations

```bash
curl -k -X DELETE \
  "https://${NSX_MANAGER}/policy/api/v1/orgs/default/projects/project-quality/vpcs/web-vpc/subnets/my-subnet/ports/my-port" \
  -H "Authorization: Basic ${AUTH}"
```

---

## 6. Common Use Cases

### 6.1 Kubernetes Integration Scenario

**Scenario**: Automatically create network resources for Kubernetes clusters

**Workflow**:
```
1. NCP/NSX Operator monitors Kubernetes events
2. Create Namespace → Create VPC in NSX
3. Create Pod → Create Port in NSX
4. Create Service → Create LB Virtual Server in NSX
```

**Related APIs**:
- `/policy/api/v1/org-root` - Create VPC hierarchy
- `/orgs/{org}/projects/{project}/vpcs/{vpc}/subnets/{subnet}/ports/{port}` - Create Pod port
- `/policy/api/v1/infra/lb-virtual-servers/{vs-id}` - Create Service load balancer

### 6.2 Network Isolation Scenario

**Scenario**: Create isolated network environments for different teams

**Implementation**:
```
Organization: company
  ├─ Project: team-a
  │   └─ VPC: team-a-prod (10.10.0.0/16)
  └─ Project: team-b
      └─ VPC: team-b-prod (10.20.0.0/16)
```

### 6.3 Load Balancing Scenario

**Scenario**: Configure load balancing for web applications

**Steps**:
1. Create LB Pool (backend servers)
2. Create LB Virtual Server (frontend VIP)
3. Configure health checks
4. Add backend members

### 6.4 Security Policy Scenario

**Scenario**: Implement micro-segmentation security

**Steps**:
1. Create Security Group (define workloads)
2. Create Security Policy (define rules)
3. Apply policy to specific Domain

---

## 7. Learning Path Recommendations

### 7.1 Beginner Stage (1-2 weeks)

**Goal**: Understand basic concepts and structure

**Learning Content**:
1. ✅ Read this document
2. ✅ Understand hierarchy: Org → Project → VPC → Subnet → Port
3. ✅ Practice basic GET operations
4. ✅ Use Search API to find resources

**Practice Tasks**:
```bash
# Task 1: List all VPCs
# Task 2: View subnets of a specific VPC
# Task 3: Find resources with specific tags
```

### 7.2 Intermediate Stage (2-4 weeks)

**Goal**: Master resource creation and management

**Learning Content**:
1. Create VPCs and subnets
2. Manage port lifecycle
3. Configure load balancers
4. Understand tag usage

**Practice Tasks**:
```bash
# Task 1: Create complete VPC hierarchy structure
# Task 2: Configure load balancing for an application
# Task 3: Implement tag-based resource queries
```

### 7.3 Advanced Stage (1-2 months)

**Goal**: Automation and integration

**Learning Content**:
1. Write automation scripts
2. Integrate with Kubernetes (NCP/NSX Operator)
3. Configure security policies
4. Performance optimization and troubleshooting

**Practice Tasks**:
```bash
# Task 1: Write Python/Go SDK to call NSX API
# Task 2: Implement Kubernetes network automation
# Task 3: Design and implement micro-segmentation security policies
```

### 7.4 Recommended Resources

**Official Documentation**:
- VMware NSX Documentation: https://docs.vmware.com/en/VMware-NSX/
- NSX Policy API Reference: https://developer.vmware.com/apis/nsx/

**Practice Environment**:
- VMware Hands-on Labs (free)
- Set up local NSX test environment

**Community Resources**:
- VMware Code GitHub: https://github.com/vmware
- NSX Community Forums

---

## 8. FAQ

### Q1: What's the difference between Policy API and Manager API?

**A**: Policy API is the next-generation API with declarative design, simpler and easier to use. Manager API is the legacy API being gradually deprecated. **Policy API is recommended**.

### Q2: When to use PUT vs PATCH?

**A**: 
- **PATCH** (recommended): Update only specified fields, other fields remain unchanged
- **PUT**: Completely replace the resource, requires all necessary fields

### Q3: How to understand the difference between VPC and traditional Segment?

**A**:
- **Segment**: Traditional NSX-T network segment, flat structure
- **VPC**: Next-generation architecture with complete organizational hierarchy, better isolation and management

### Q4: What are Tags used for?

**A**: Tags are used for:
- Resource classification and search
- Association with Kubernetes namespaces/Pods
- Dynamic membership matching in security policies
- Resource identification by automation tools

### Q5: How to view resource status?

**A**: Most resources have a `/state` endpoint:
```bash
GET /orgs/{org}/projects/{project}/vpcs/{vpc}/subnets/{subnet}/ports/{port}/state
```

### Q6: Why do some resources return 404?

**A**: Possible reasons:
1. Resource has been deleted
2. Path or ID spelling error
3. No permission to access
4. Resource not yet created (async operation)

### Q7: How to handle large-scale resource queries?

**A**: Use pagination parameters:
```bash
GET /policy/api/v1/search/query?query=...&page_size=100&cursor=xxx
```

### Q8: Are there rate limits on API calls?

**A**: Yes, NSX has rate limits. Recommendations:
- Use batch operations instead of individual operations
- Implement exponential backoff retry mechanism
- Monitor rate limit information in response headers

---

## 9. Appendix: Quick Reference

### 9.1 Common Endpoints Cheat Sheet

| Function | Endpoint | Method |
|----------|----------|--------|
| Search Resources | `/search/query` | GET |
| Organization Root | `/org-root` | GET, PATCH |
| VPC List | `/orgs/{org}/projects/{project}/vpcs` | GET |
| Create Subnet | `/orgs/{org}/projects/{project}/vpcs/{vpc}/subnets/{subnet}` | PATCH |
| Port Details | `/orgs/{org}/projects/{project}/vpcs/{vpc}/subnets/{subnet}/ports/{port}` | GET |
| LB Pool | `/infra/lb-pools/{pool}` | GET, PATCH, DELETE |
| Certificate Management | `/infra/certificates` | GET |

### 9.2 Common Query Parameters

```bash
# Search by resource type
?query=resource_type:Vpc

# Search by tags
?query=tags.scope:nsx-op/cluster AND tags.tag:cluster-id

# Sort
?sort_by=id

# Pagination
?page_size=100&cursor=xxx
```

### 9.3 HTTP Status Codes

| Status Code | Meaning | Action |
|------------|---------|--------|
| 200 OK | Success | Parse response |
| 400 Bad Request | Request format error | Check JSON format |
| 404 Not Found | Resource not found | Check path and ID |
| 409 Conflict | Resource already exists | Use PATCH instead of PUT |
| 500 Internal Server Error | Server error | Retry or contact admin |

---

## 10. Summary

🎯 **Key Takeaways**:

1. **Hierarchy Understanding**: Org → Project → VPC → Subnet → Port
2. **Declarative API**: Describe desired state, NSX implements automatically
3. **Tag-Driven**: Use tags for dynamic management
4. **Search API**: Your exploration starting point
5. **PATCH First**: Prefer PATCH method for updates

🚀 **Next Steps**:

1. Use examples in this document for hands-on practice
2. Read the complete API report (416 endpoints details)
3. Create your own VPC in test environment
4. Write automation scripts

📚 **Continuous Learning**:

- Regularly check VMware official documentation updates
- Participate in NSX community discussions
- Use Search API and actual responses as reference when encountering issues

---

**Document Version**: v1.0  
**Last Updated**: 2025-10-17  
**Author**: Based on real NSX Policy API analysis  
**Feedback**: Welcome questions and suggestions

---

## Related Documents

- 📄 [Complete NSX Policy API Report](/Users/zhengxie/Downloads/nsx_policy_api_report_with_log_responses.md) - 416 endpoints detailed documentation (with log responses)
- 📖 [NSX API Template](./nsx_api_template.md) - API usage templates and examples

---

**Happy Learning! 🎉**
