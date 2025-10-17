# NSX VPC Best Practices Guide

**Target Audience**: Platform engineers, DevOps teams, Kubernetes administrators  
**Focus**: Real-world usage of Org/Project/VPC/Subnet hierarchy  
**Based on**: Production environment analysis and API logs

---

## 📚 Table of Contents

1. [Hierarchy Design Principles](#1-hierarchy-design-principles)
2. [Kubernetes Integration Patterns](#2-kubernetes-integration-patterns)
3. [Naming Conventions](#3-naming-conventions)
4. [Tagging Strategy](#4-tagging-strategy)
5. [IP Address Planning](#5-ip-address-planning)
6. [Operational Workflows](#6-operational-workflows)
7. [Troubleshooting Guide](#7-troubleshooting-guide)
8. [Common Pitfalls](#8-common-pitfalls)
9. [Production Checklists](#9-production-checklists)

---

## 1. Hierarchy Design Principles

### 1.1 Organization (Org) Level

**Purpose**: Top-level tenant isolation

**Real-world Patterns**:

```
Pattern A: Single Organization (Most Common)
└─ Org: default
    └─ All clusters, all environments

Pattern B: Multi-Organization (Strict Isolation)
├─ Org: production
├─ Org: staging
└─ Org: development

Pattern C: Business Unit Isolation
├─ Org: engineering
├─ Org: sales
└─ Org: operations
```

**Recommendation**: 
- ✅ Start with `default` org for single-tenant environments
- ✅ Use multiple orgs only when billing/compliance requires strict separation
- ❌ Don't create orgs per team (use Projects instead)

### 1.2 Project Level

**Purpose**: Kubernetes cluster or major application grouping

**Real-world Patterns**:

```
Pattern A: One Project per Kubernetes Cluster (Recommended)
default/
├─ project-prod-cluster-1
├─ project-prod-cluster-2
├─ project-staging-cluster
└─ project-dev-cluster

Pattern B: One Project per Team
default/
├─ project-platform-team
├─ project-frontend-team
└─ project-backend-team

Pattern C: One Project per Environment + Workload Type
default/
├─ project-prod-web
├─ project-prod-data
└─ project-staging-web
```

**Recommendation**:
- ✅ **Pattern A (1 cluster = 1 project)** for Kubernetes
- ✅ Naming: `project-{cluster-name}` or `project-{env}-{location}`
- ✅ Example from real logs: `project-quality` (QA cluster)

### 1.3 VPC Level

**Purpose**: Network isolation boundary (typically 1:1 with K8s Namespace)

**Real-world Patterns**:

```
Kubernetes Integration (Auto-managed by NSX Operator)
project-quality/
├─ vpc-default           # K8s namespace: default
├─ vpc-kube-system       # K8s namespace: kube-system
├─ vpc-my-app            # K8s namespace: my-app
└─ vpc-monitoring        # K8s namespace: monitoring

VM Workloads (Manual creation)
project-production/
├─ vpc-web-tier          # Web server VMs
├─ vpc-app-tier          # Application VMs
└─ vpc-data-tier         # Database VMs
```

**Recommendation**:
- ✅ Kubernetes: Let NSX Operator auto-create (1 namespace = 1 VPC)
- ✅ VMs: Create manually with clear naming
- ✅ Each VPC gets dedicated IP range (e.g., /16)

### 1.4 Subnet Level

**Purpose**: IP address pool within a VPC

**Real-world Patterns**:

```
Kubernetes Pods (Most Common)
vpc-my-app/
└─ subnet: pod-subnet (172.26.0.0/16)
   └─ Provides IPs for all pods in namespace

VM Workloads (Multi-subnet)
vpc-web-tier/
├─ subnet: frontend (10.100.1.0/24)
├─ subnet: backend (10.100.2.0/24)
└─ subnet: management (10.100.10.0/24)

Advanced (Separate Pod and Service IPs)
vpc-my-app/
├─ subnet: pod-subnet (172.26.0.0/16)
└─ subnet: service-subnet (10.96.0.0/16)
```

**Recommendation**:
- ✅ Kubernetes: Single `pod-subnet` per VPC (auto-created)
- ✅ Subnet inherits VPC IP range (no separate CIDR needed)
- ✅ No DHCP needed (NSX assigns IPs directly)

---

## 2. Kubernetes Integration Patterns

### 2.1 Automated Workflow (Recommended ⭐)

**NSX Operator handles everything automatically:**

```yaml
# Step 1: Create Kubernetes Namespace
apiVersion: v1
kind: Namespace
metadata:
  name: my-application
  annotations:
    nsx.vmware.com/project: project-quality  # Optional: specify NSX project
```

**What NSX Operator Does Automatically:**

```bash
1. Create VPC
   Path: /orgs/default/projects/project-quality/vpcs/my-application
   IP: Auto-assigned from available pool (e.g., 172.26.0.0/16)
   Tags: nsx-op/cluster=cluster-id, nsx-op/namespace=my-application

2. Create Subnet
   Path: .../vpcs/my-application/subnets/pod-subnet
   Purpose: IP pool for pods

3. Per Pod → Create Port
   Path: .../subnets/pod-subnet/ports/{pod-uuid}
   IP: Auto-assigned from subnet
   Tags: nsx-op/pod_name=my-pod-xyz, nsx-op/namespace=my-application

4. Per Service → Create LB Virtual Server
   Path: /infra/lb-virtual-servers/{service-uuid}
   Purpose: LoadBalancer for K8s Service
```

### 2.2 NetworkPolicy Translation

**Kubernetes NetworkPolicy automatically becomes NSX SecurityPolicy:**

```yaml
# Kubernetes NetworkPolicy
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: deny-all-ingress
  namespace: my-application
spec:
  podSelector: {}
  policyTypes: [Ingress]
```

**NSX Creates SecurityPolicy:**
```
Path: /orgs/default/projects/project-quality/vpcs/my-application/security-policies/deny-all-ingress
Type: DFW (Distributed Firewall) rules
Enforcement: At VPC port level
```

### 2.3 Service Type Integration

| K8s Service Type | NSX Resource | Location |
|------------------|-------------|----------|
| ClusterIP | Internal only | Within VPC |
| NodePort | LB Virtual Server | `/infra/lb-virtual-servers/` |
| LoadBalancer | LB VS + Pool | `/infra/lb-virtual-servers/` + `/infra/lb-pools/` |
| ExternalName | DNS only | No NSX resource |

---

## 3. Naming Conventions

### 3.1 Production-Ready Naming Scheme

Based on real environment analysis:

```bash
# Organization
default                              # Single tenant
{company}-{environment}              # Multi-tenant: acme-prod, acme-dev

# Project
project-{cluster-name}               # Real example: project-quality
project-{env}-{location}             # Example: project-prod-us-west
project-{team}-{workload}            # Example: project-platform-infra

# VPC (Auto-named by NSX Operator)
{kubernetes-namespace}               # Example: my-application
{namespace}-{cluster-id}             # Multi-cluster: my-app-cluster-abc

# Subnet (Standard names)
pod-subnet                           # For Kubernetes pods
service-subnet                       # For Service IPs (if separate)
vm-subnet                            # For VM workloads
management-subnet                    # For admin access
```

### 3.2 Display Name Best Practices

```json
{
  "id": "my-app",                              // Immutable, URL-friendly
  "display_name": "My Application (Production)", // Human-readable
  "tags": [
    {"scope": "env", "tag": "production"},
    {"scope": "team", "tag": "platform"}
  ]
}
```

**Rules**:
- `id`: Lowercase, hyphens, no spaces (immutable)
- `display_name`: Descriptive, can include spaces and special chars
- Tags: For searchability and automation

---

## 4. Tagging Strategy

### 4.1 Essential Tags (From Real Logs)

**NSX Operator Auto-tags:**
```json
{
  "tags": [
    {"scope": "nsx-op/cluster", "tag": "cluster-abc123"},      // K8s cluster ID
    {"scope": "nsx-op/namespace", "tag": "my-application"},   // K8s namespace
    {"scope": "nsx-op/pod_name", "tag": "web-pod-xyz"},       // Pod name
    {"scope": "nsx-op/version", "tag": "v1"}                  // NSX Operator version
  ]
}
```

**Recommended Custom Tags:**
```json
{
  "tags": [
    // Organizational
    {"scope": "env", "tag": "production"},           // Environment
    {"scope": "team", "tag": "platform"},            // Owning team
    {"scope": "cost-center", "tag": "engineering"},  // Billing
    
    // Application Context
    {"scope": "app", "tag": "web-frontend"},         // Application name
    {"scope": "version", "tag": "v2.1.0"},           // App version
    {"scope": "tier", "tag": "frontend"},            // Architecture tier
    
    // Compliance
    {"scope": "compliance", "tag": "pci-dss"},       // Regulatory requirement
    {"scope": "data-classification", "tag": "confidential"}
  ]
}
```

### 4.2 Tag-Based Queries

```bash
# Find all production VPCs
GET /search/query?query=resource_type:Vpc AND tags.scope:env AND tags.tag:production

# Find all resources owned by a team
GET /search/query?query=tags.scope:team AND tags.tag:platform

# Find VPCs for a specific K8s cluster
GET /search/query?query=resource_type:Vpc AND tags.scope:nsx-op/cluster AND tags.tag:cluster-abc123
```

---

## 5. IP Address Planning

### 5.1 Real-World IP Allocation (Based on Logs)

**From actual environment analysis:**

```
Project: project-quality
├─ VPC: namespace-a (172.26.0.0/16) → 65,534 IPs
├─ VPC: namespace-b (172.27.0.0/16) → 65,534 IPs
├─ VPC: namespace-c (172.28.0.0/16) → 65,534 IPs
└─ VPC: namespace-d (172.29.0.0/16) → 65,534 IPs
```

### 5.2 IP Planning Best Practices

**Small Clusters (< 100 pods per namespace)**
```
VPC IP Range: /20 (4,094 usable IPs)
Example: 10.100.0.0/20
```

**Medium Clusters (100-1000 pods per namespace)**
```
VPC IP Range: /16 (65,534 usable IPs)
Example: 172.26.0.0/16  ← Used in real environment
```

**Large Clusters (> 1000 pods per namespace)**
```
VPC IP Range: /12 (1,048,574 usable IPs)
Example: 10.0.0.0/12
```

### 5.3 Avoiding IP Conflicts

**Strategy A: Sequential Allocation**
```
project-prod-cluster/
├─ vpc-default:      172.16.0.0/16
├─ vpc-kube-system:  172.17.0.0/16
├─ vpc-monitoring:   172.18.0.0/16
└─ vpc-app-ns-1:     172.19.0.0/16
```

**Strategy B: Block Reservation**
```
Production:  10.0.0.0/8
├─ Cluster-1: 10.0.0.0/12  (VPCs use /16 slices)
└─ Cluster-2: 10.16.0.0/12

Staging:     172.16.0.0/12
Development: 192.168.0.0/16
```

### 5.4 Checking IP Usage

```bash
# View IP allocations for a subnet
curl -k -u admin:pass \
  "https://${NSX_MANAGER}/policy/api/v1/orgs/default/projects/project-quality/vpcs/${VPC_ID}/subnets/${SUBNET_ID}/ip-address-allocations" \
  | jq '{total: .total_ip_count, used: .allocated_ip_count, available: (.total_ip_count - .allocated_ip_count)}'

# Find all ports in a subnet
curl -k -u admin:pass \
  "https://${NSX_MANAGER}/policy/api/v1/search/query?query=resource_type:VpcSubnetPort AND path:*${SUBNET_ID}*" \
  | jq '.results | length'
```

---

## 6. Operational Workflows

### 6.1 Day 1: Initial Setup

**For Kubernetes Clusters:**

```bash
# 1. NSX Operator creates project automatically
# No manual action needed if using Helm chart with project annotation

# 2. Verify project exists
curl -k -u admin:pass \
  "https://${NSX_MANAGER}/policy/api/v1/search/query?query=resource_type:Project" \
  | jq '.results[] | {id: .id, path: .path}'

# 3. Create K8s namespace (VPC auto-created)
kubectl create namespace my-app

# 4. Verify VPC creation
curl -k -u admin:pass \
  "https://${NSX_MANAGER}/policy/api/v1/search/query?query=resource_type:Vpc AND tags.scope:nsx-op/namespace AND tags.tag:my-app" \
  | jq '.results[0] | {id: .id, ips: .private_ips, state: .status}'
```

**For VM Workloads:**

```bash
# 1. Create Project (if not exists)
curl -k -X PATCH \
  "https://${NSX_MANAGER}/policy/api/v1/orgs/default/projects/project-vms" \
  -u admin:pass \
  -H "Content-Type: application/json" \
  -d '{
    "id": "project-vms",
    "display_name": "VM Workloads"
  }'

# 2. Create VPC with subnet in one call
curl -k -X PATCH \
  "https://${NSX_MANAGER}/policy/api/v1/org-root" \
  -u admin:pass \
  -H "Content-Type: application/json" \
  -d '{
    "OrgRoot": {
      "children": [{
        "Org": {
          "id": "default",
          "children": [{
            "Project": {
              "id": "project-vms",
              "children": [{
                "Vpc": {
                  "id": "web-tier",
                  "display_name": "Web Tier VPC",
                  "private_ips": ["10.100.0.0/16"],
                  "tags": [
                    {"scope": "env", "tag": "production"},
                    {"scope": "tier", "tag": "web"}
                  ],
                  "children": [{
                    "VpcSubnet": {
                      "id": "web-subnet",
                      "display_name": "Web Subnet",
                      "ipv4_subnet_size": 24,
                      "access_mode": "Private_TGW"
                    }
                  }]
                }
              }]
            }
          }]
        }
      }]
    }
  }'
```

### 6.2 Day 2: Monitoring and Maintenance

**Health Check Script:**

```bash
#!/bin/bash
# check_vpc_health.sh

NSX_MANAGER="10.70.188.176"
AUTH="admin:password"

echo "=== VPC Health Check ==="

# Check all VPCs
VPCs=$(curl -sk -u $AUTH \
  "https://${NSX_MANAGER}/policy/api/v1/search/query?query=resource_type:Vpc" \
  | jq -r '.results[] | .id')

for vpc in $VPCs; do
  echo "Checking VPC: $vpc"
  
  # Get VPC state
  state=$(curl -sk -u $AUTH \
    "https://${NSX_MANAGER}/policy/api/v1/search/query?query=resource_type:Vpc AND id:${vpc}" \
    | jq -r '.results[0].status')
  
  echo "  State: $state"
  
  # Count ports
  port_count=$(curl -sk -u $AUTH \
    "https://${NSX_MANAGER}/policy/api/v1/search/query?query=resource_type:VpcSubnetPort AND path:*${vpc}*" \
    | jq '.result_count')
  
  echo "  Active Ports: $port_count"
  echo ""
done
```

### 6.3 Cleanup Workflow

**IMPORTANT: Order matters to avoid errors**

```bash
# 1. Delete all ports first
for port in $(get_all_ports_in_vpc); do
  curl -k -X DELETE \
    "https://${NSX_MANAGER}/policy/api/v1/orgs/default/projects/${PROJECT}/vpcs/${VPC}/subnets/${SUBNET}/ports/${port}" \
    -u admin:pass
done

# 2. Delete subnets
curl -k -X DELETE \
  "https://${NSX_MANAGER}/policy/api/v1/orgs/default/projects/${PROJECT}/vpcs/${VPC}/subnets/${SUBNET}" \
  -u admin:pass

# 3. Delete VPC
curl -k -X DELETE \
  "https://${NSX_MANAGER}/policy/api/v1/orgs/default/projects/${PROJECT}/vpcs/${VPC}" \
  -u admin:pass

# For Kubernetes: Just delete the namespace, NSX Operator handles cleanup
kubectl delete namespace my-app
```

---

## 7. Troubleshooting Guide

### 7.1 Common Issues and Solutions

#### Issue 1: VPC Not Created for K8s Namespace

**Symptoms**: Namespace exists, but no VPC in NSX

**Debug Steps**:
```bash
# 1. Check NSX Operator logs
kubectl logs -n nsx-system-operator deployment/nsx-operator

# 2. Check namespace annotations
kubectl get namespace my-app -o yaml | grep annotations -A 5

# 3. Verify project exists
curl -k -u admin:pass \
  "https://${NSX_MANAGER}/policy/api/v1/search/query?query=resource_type:Project" \
  | jq '.results[].id'
```

**Solutions**:
- Ensure NSX Operator is running
- Check if project annotation is correct
- Verify NSX Manager connectivity

#### Issue 2: Pod Cannot Get IP Address

**Symptoms**: Pod stuck in `ContainerCreating`

**Debug Steps**:
```bash
# 1. Check pod events
kubectl describe pod <pod-name>

# 2. Verify subnet has available IPs
curl -k -u admin:pass \
  "https://${NSX_MANAGER}/policy/api/v1/orgs/default/projects/${PROJECT}/vpcs/${VPC}/subnets/${SUBNET}/ip-address-allocations" \
  | jq '{total: .total_ip_count, used: .allocated_ip_count}'

# 3. Check if port was created
kubectl get pod <pod-name> -o yaml | grep uid
# Use pod UID to search for port
curl -k -u admin:pass \
  "https://${NSX_MANAGER}/policy/api/v1/search/query?query=resource_type:VpcSubnetPort AND tags.tag:<pod-uid>"
```

**Solutions**:
- Check subnet IP exhaustion (expand VPC IP range if needed)
- Verify NSX agent on node is healthy
- Check for NSX API rate limiting

#### Issue 3: Cannot Delete VPC

**Error**: `Resource is still referenced by other resources`

**Solution**:
```bash
# 1. Find all ports in VPC
curl -k -u admin:pass \
  "https://${NSX_MANAGER}/policy/api/v1/search/query?query=resource_type:VpcSubnetPort AND path:*${VPC_ID}*" \
  | jq '.results[].path'

# 2. Delete ports first (or delete pods in K8s)
kubectl delete pods --all -n <namespace>

# 3. Wait for ports to be cleaned up (30-60 seconds)

# 4. Retry VPC deletion
```

### 7.2 Useful Search Queries

```bash
# Find orphaned ports (no associated pod)
GET /search/query?query=resource_type:VpcSubnetPort AND NOT tags.scope:nsx-op/pod_name

# Find VPCs with high port count (potential IP exhaustion)
GET /search/query?query=resource_type:VpcSubnetPort
# Group by VPC ID and count

# Find all resources for a specific namespace
GET /search/query?query=tags.scope:nsx-op/namespace AND tags.tag:<namespace-name>

# Find VPCs without proper tags
GET /search/query?query=resource_type:Vpc AND NOT tags.scope:env
```

---

## 8. Common Pitfalls

### ❌ Pitfall 1: Manual Creation in K8s Environments

**Wrong Approach**:
```bash
# DON'T manually create VPCs for K8s namespaces
curl -X PATCH .../vpcs/my-namespace ...
kubectl create namespace my-namespace
# Result: Conflicts, orphaned resources
```

**Right Approach**:
```bash
# Let NSX Operator manage everything
kubectl create namespace my-namespace
# NSX Operator creates VPC automatically
```

### ❌ Pitfall 2: IP Range Overlap

**Wrong**:
```
vpc-web:  10.0.0.0/16
vpc-data: 10.0.0.0/16  ← CONFLICT!
```

**Right**:
```
vpc-web:  10.0.0.0/16
vpc-data: 10.1.0.0/16  ← Non-overlapping
```

### ❌ Pitfall 3: Deleting in Wrong Order

**Wrong**:
```bash
# Try to delete VPC first
curl -X DELETE .../vpcs/my-vpc
# Error: Still has ports!
```

**Right**:
```bash
# Delete in order: Ports → Subnets → VPC
# Or: Delete K8s namespace (auto-cleanup)
kubectl delete namespace my-app
```

### ❌ Pitfall 4: Undersized IP Ranges

**Wrong**:
```bash
# /24 for a namespace with 100+ pods
"private_ips": ["10.0.0.0/24"]  # Only 254 IPs
```

**Right**:
```bash
# /16 for scalability
"private_ips": ["10.0.0.0/16"]  # 65,534 IPs
```

### ❌ Pitfall 5: Missing Tags

**Wrong**:
```json
{
  "id": "my-vpc",
  "private_ips": ["10.0.0.0/16"]
  // No tags = hard to find, manage, bill
}
```

**Right**:
```json
{
  "id": "my-vpc",
  "private_ips": ["10.0.0.0/16"],
  "tags": [
    {"scope": "env", "tag": "production"},
    {"scope": "team", "tag": "platform"},
    {"scope": "cost-center", "tag": "engineering"}
  ]
}
```

---

## 9. Production Checklists

### 9.1 Pre-Deployment Checklist

Before deploying NSX VPC in production:

- [ ] **IP Planning Complete**
  - [ ] No overlapping IP ranges
  - [ ] Sufficient IPs per VPC (/16 minimum for K8s)
  - [ ] IP ranges documented
  
- [ ] **Naming Convention Defined**
  - [ ] Org naming scheme
  - [ ] Project naming pattern
  - [ ] VPC naming rules
  
- [ ] **Tagging Strategy Implemented**
  - [ ] Required tags defined (env, team, cost-center)
  - [ ] Tag enforcement mechanism (policy/automation)
  
- [ ] **NSX Operator Configured** (for K8s)
  - [ ] Operator deployed and healthy
  - [ ] Project annotation configured
  - [ ] IP pool allocation verified
  
- [ ] **Monitoring Setup**
  - [ ] VPC health checks automated
  - [ ] IP exhaustion alerts configured
  - [ ] Port count monitoring enabled

### 9.2 Post-Deployment Validation

After creating VPC resources:

```bash
# 1. Verify VPC creation
curl -k -u admin:pass \
  "https://${NSX_MANAGER}/policy/api/v1/orgs/default/projects/${PROJECT}/vpcs/${VPC}" \
  | jq '{id: .id, ips: .private_ips, state: .status}'

# 2. Check subnet exists
curl -k -u admin:pass \
  "https://${NSX_MANAGER}/policy/api/v1/orgs/default/projects/${PROJECT}/vpcs/${VPC}/subnets" \
  | jq '.results[] | {id: .id, size: .ipv4_subnet_size}'

# 3. Test pod creation (K8s)
kubectl run test-pod --image=nginx -n ${NAMESPACE}
kubectl get pod test-pod -o wide  # Should have IP from VPC range

# 4. Verify tags
curl -k -u admin:pass \
  "https://${NSX_MANAGER}/policy/api/v1/search/query?query=resource_type:Vpc AND id:${VPC}" \
  | jq '.results[0].tags'

# 5. Test connectivity
kubectl exec test-pod -- ping <another-pod-ip>
```

### 9.3 Regular Maintenance Tasks

**Weekly**:
- [ ] Check IP utilization per VPC
- [ ] Review orphaned ports (pods deleted but ports remain)
- [ ] Verify NSX Operator health

**Monthly**:
- [ ] Audit tag compliance
- [ ] Review IP allocation efficiency
- [ ] Clean up unused VPCs

**Quarterly**:
- [ ] Review naming conventions (update if needed)
- [ ] Audit security policies per VPC
- [ ] Capacity planning (IP ranges, VPC count)

---

## 10. Quick Reference

### 10.1 Common Commands

```bash
# List all VPCs
curl -k -u admin:pass \
  "https://${NSX_MANAGER}/policy/api/v1/search/query?query=resource_type:Vpc" \
  | jq '.results[] | {id: .id, ips: .private_ips}'

# Get VPC by K8s namespace
curl -k -u admin:pass \
  "https://${NSX_MANAGER}/policy/api/v1/search/query?query=resource_type:Vpc AND tags.scope:nsx-op/namespace AND tags.tag:${NAMESPACE}" \
  | jq '.results[0].path'

# Count ports in VPC
curl -k -u admin:pass \
  "https://${NSX_MANAGER}/policy/api/v1/search/query?query=resource_type:VpcSubnetPort AND path:*${VPC_ID}*" \
  | jq '.result_count'

# Get IP allocation
curl -k -u admin:pass \
  "https://${NSX_MANAGER}/policy/api/v1/orgs/default/projects/${PROJECT}/vpcs/${VPC}/subnets/${SUBNET}/ip-address-allocations"

# Find VPCs by tag
curl -k -u admin:pass \
  "https://${NSX_MANAGER}/policy/api/v1/search/query?query=resource_type:Vpc AND tags.scope:env AND tags.tag:production"
```

### 10.2 Decision Tree

```
Need to create network isolation?
│
├─ For Kubernetes?
│  ├─ YES → Create K8s Namespace
│  │        NSX Operator creates VPC automatically
│  │        ✅ 1 Namespace = 1 VPC
│  │
│  └─ NO → Creating for VMs?
│           Manually create VPC in appropriate Project
│           ✅ Group by tier/function
│
└─ Which Project to use?
   ├─ K8s cluster exists? → Use project-{cluster-name}
   ├─ New workload type? → Create new project
   └─ Shared infra? → Use existing project
```

---

## Summary

🎯 **Golden Rules**:

1. **Kubernetes**: Let NSX Operator manage VPC lifecycle (1 namespace = 1 VPC)
2. **IP Planning**: Use /16 per VPC for scalability (65K IPs)
3. **Tagging**: Always tag with env, team, cost-center minimum
4. **Naming**: Follow convention: `project-{cluster}`, vpc auto-named from namespace
5. **Deletion**: Always delete ports before VPC (or use K8s namespace deletion)

🚀 **Quick Start**:

```bash
# For Kubernetes (simplest)
kubectl create namespace my-app
# Done! NSX creates VPC automatically

# For VMs (manual)
curl -k -X PATCH https://${NSX_MANAGER}/policy/api/v1/org-root \
  -u admin:pass -H "Content-Type: application/json" \
  -d @vpc_hierarchy.json
```

📚 **Related Docs**:
- [NSX Policy API 101 Guide](./NSX_Policy_API_101_Guide_EN.md)
- [Complete API Reference](/Users/zhengxie/Downloads/nsx_policy_api_report_with_log_responses.md)

---

**Document Version**: v1.0  
**Last Updated**: 2025-10-17  
**Based On**: Production environment analysis (project-quality cluster)  
**Feedback**: Welcome improvements and real-world additions

---

**Happy Networking! 🎉**
