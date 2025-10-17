# NSX Policy API 101 入门指南

**目标读者**：NSX初学者、开发人员、运维工程师  
**学习时间**：2-3小时  
**前置知识**：基本的网络概念、REST API基础

---

## 📚 目录

1. [什么是NSX](#1-什么是nsx)
2. [NSX Policy API简介](#2-nsx-policy-api简介)
3. [核心架构层级](#3-核心架构层级)
4. [关键资源类型详解](#4-关键资源类型详解)
5. [API调用实战](#5-api调用实战)
6. [常见使用场景](#6-常见使用场景)
7. [学习路径建议](#7-学习路径建议)
8. [常见问题FAQ](#8-常见问题faq)

---

## 1. 什么是NSX

### 1.1 NSX简介

**VMware NSX** 是一个软件定义的网络（SDN）和安全平台，为数据中心提供虚拟化网络和安全服务。

**核心价值**：
- 🌐 **网络虚拟化**：将物理网络抽象为软件定义的逻辑网络
- 🔒 **微分段安全**：细粒度的安全策略控制
- ⚡ **快速部署**：通过API自动化网络配置
- 🔄 **灵活扩展**：支持多云和容器环境

### 1.2 NSX的主要组件

```
┌─────────────────────────────────────────┐
│         NSX Manager (控制平面)           │
│  - 管理界面                              │
│  - Policy API                            │
│  - 配置管理                              │
└─────────────────────────────────────────┘
                 ↓
┌─────────────────────────────────────────┐
│         NSX Edge (边缘节点)              │
│  - 路由 (Tier-0/Tier-1)                 │
│  - 负载均衡                              │
│  - NAT/VPN                               │
└─────────────────────────────────────────┘
                 ↓
┌─────────────────────────────────────────┐
│         ESXi Hosts (数据平面)            │
│  - 虚拟交换机                            │
│  - 分布式防火墙                          │
│  - VPC/Segment                           │
└─────────────────────────────────────────┘
```

### 1.3 NSX的两种架构

1. **NSX-T (传统架构)**
   - Tier-0/Tier-1 网关
   - Segments (逻辑交换机)
   - Distributed Firewall
   
2. **NSX VPC (新一代架构)** ⭐
   - 基于VPC的多租户隔离
   - 组织(Org) → 项目(Project) → VPC 层级
   - 更适合云原生和Kubernetes环境

---

## 2. NSX Policy API简介

### 2.1 什么是Policy API

**NSX Policy API** 是基于**意图驱动**的声明式API：
- 你只需要声明"想要什么"（目标状态）
- NSX会自动计算"如何实现"（实现路径）

### 2.2 Policy API vs Manager API

| 特性 | Policy API | Manager API (旧) |
|------|-----------|-----------------|
| 设计理念 | 声明式（意图） | 命令式（步骤） |
| 复杂度 | 简单 | 复杂 |
| 层级结构 | 清晰 | 扁平 |
| 推荐使用 | ✅ 推荐 | ❌ 逐步淘汰 |

### 2.3 API基础信息

**Base URL**: `https://<nsx-manager>/policy/api/v1/`

**认证方式**: HTTP Basic Authentication
```bash
curl -k -u admin:password \
  -H "Content-Type: application/json" \
  https://10.70.188.176/policy/api/v1/infra
```

**常用HTTP方法**:
- `GET` - 查询资源
- `PATCH` - 更新资源（推荐）
- `PUT` - 创建/替换资源
- `DELETE` - 删除资源

---

## 3. 核心架构层级

### 3.1 整体层级视图

从我们的API分析来看，NSX Policy API遵循清晰的层级结构：

```
Level 4 (最顶层 - 1个端点)
  └─ /policy/api/v1/org-root
      └─ 组织根节点，所有资源的入口

Level 5 (基础设施层 - 6个端点)
  ├─ /policy/api/v1/search/query (搜索API)
  ├─ /policy/api/v1/infra/ip-blocks (IP地址池)
  ├─ /policy/api/v1/infra/certificates (证书管理)
  └─ ...

Level 6 (功能模块层 - 89个端点)
  ├─ /policy/api/v1/infra/lb-pools/* (负载均衡池)
  ├─ /policy/api/v1/infra/lb-virtual-servers/* (虚拟服务器)
  ├─ /policy/api/v1/infra/domains/* (安全域)
  └─ ...

Level 7-14 (详细资源层 - 320个端点)
  └─ /orgs/default/projects/project-quality/vpcs/.../subnets/.../ports/...
      └─ VPC资源的完整层级
```

### 3.2 两种主要架构路径

#### 路径1: 传统 Infra 架构

```
/policy/api/v1/infra/
  ├─ tier-0s/                  # Tier-0网关
  ├─ tier-1s/                  # Tier-1网关
  ├─ segments/                 # 网络段
  ├─ domains/                  # 安全域
  │   ├─ groups/               # 安全组
  │   └─ security-policies/    # 安全策略
  └─ lb-pools/                 # 负载均衡池
```

#### 路径2: VPC 架构 ⭐ (现代化)

```
/policy/api/v1/org-root
  └─ /orgs/{org-id}/                    # 组织
      └─ /projects/{project-id}/        # 项目
          └─ /vpcs/{vpc-id}/            # VPC (隔离的虚拟网络)
              ├─ /subnets/{subnet-id}/  # 子网
              │   └─ /ports/{port-id}/  # 端口 (VM/Pod连接点)
              ├─ /vpc-lbs/{lb-id}/      # VPC负载均衡器
              └─ /security-policies/    # VPC安全策略
```

### 3.3 层级关系详解

**理解要点**：
1. **组织(Org)** = 最高层租户隔离
2. **项目(Project)** = 组织内的资源分组
3. **VPC** = 项目内的隔离网络空间
4. **子网(Subnet)** = VPC内的IP地址段
5. **端口(Port)** = 虚拟机或Pod的网络接口

**实际例子**：
```
组织: default
  └─ 项目: project-quality
      └─ VPC: web-app-vpc
          ├─ 子网: pod-subnet (172.26.0.0/16)
          │   ├─ 端口: web-pod-1 (172.26.1.10)
          │   └─ 端口: web-pod-2 (172.26.1.11)
          └─ 负载均衡器: web-lb
```

---

## 4. 关键资源类型详解

### 4.1 搜索API - 你的起点

**端点**: `/policy/api/v1/search/query`

**作用**: 搜索和发现NSX中的任何资源

**示例查询**：
```bash
# 查找所有VPC
GET /policy/api/v1/search/query?query=resource_type:Vpc

# 查找特定集群的域
GET /policy/api/v1/search/query?query=resource_type:Domain AND tags.scope:ncp/cluster AND tags.tag:cluster-id
```

**响应示例**：
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

### 4.2 组织根 (org-root)

**端点**: `/policy/api/v1/org-root`

**作用**: 所有VPC资源的顶层入口

**用途**:
- 创建整个VPC层级结构
- 批量更新多个VPC
- 获取组织级别配置

**层级结构**：
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

**端点模式**: `/orgs/{org}/projects/{project}/vpcs/{vpc-id}`

**关键属性**：
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

**VPC的作用**：
- 🔒 **网络隔离**：不同VPC之间默认互不通信
- 📦 **资源容器**：包含subnets、ports、security policies
- 🏷️ **标签管理**：通过tags关联到Kubernetes命名空间

### 4.4 子网 (Subnet)

**端点模式**: `/orgs/{org}/projects/{project}/vpcs/{vpc}/subnets/{subnet-id}`

**关键属性**：
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

**子网类型**：
- **Pod子网**: 用于Kubernetes Pod
- **User子网**: 用于虚拟机
- **DHCP子网**: 自动分配IP地址

### 4.5 端口 (Port)

**端点模式**: `/orgs/{org}/projects/{project}/vpcs/{vpc}/subnets/{subnet}/ports/{port-id}`

**关键属性**：
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

**端口的作用**：
- 连接点：VM或Pod连接到网络的接口
- IP分配：获取子网中的IP地址
- 安全策略应用点：防火墙规则在端口级别应用

### 4.6 负载均衡器

#### LB Pool (后端服务器池)
**端点**: `/policy/api/v1/infra/lb-pools/{pool-id}`

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

#### LB Virtual Server (前端监听器)
**端点**: `/policy/api/v1/infra/lb-virtual-servers/{vs-id}`

```json
{
  "id": "web-svc-vs",
  "display_name": "Web Service Virtual Server",
  "ip_address": "10.0.0.100",
  "ports": ["80"],
  "pool_path": "/infra/lb-pools/web-svc-pool"
}
```

### 4.7 安全相关资源

#### Security Domain (安全域)
**端点**: `/policy/api/v1/infra/domains/{domain-id}`

**作用**: 逻辑分组，用于组织安全策略

#### Security Group (安全组)
**端点**: `/policy/api/v1/infra/domains/{domain}/groups/{group-id}`

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

#### Security Policy (安全策略)
**端点**: `/policy/api/v1/infra/domains/{domain}/security-policies/{policy-id}`

**作用**: 定义防火墙规则，控制流量

---

## 5. API调用实战

### 5.1 环境准备

```bash
# 设置环境变量
export NSX_MANAGER="10.70.188.176"
export NSX_USER="admin"
export NSX_PASS="your-password"

# 创建认证头
export AUTH=$(echo -n "${NSX_USER}:${NSX_PASS}" | base64)
```

### 5.2 基础查询操作

#### 获取所有VPC
```bash
curl -k -X GET \
  "https://${NSX_MANAGER}/policy/api/v1/search/query?query=resource_type:Vpc" \
  -H "Authorization: Basic ${AUTH}" \
  -H "Accept: application/json" | jq '.'
```

#### 获取特定VPC详情
```bash
curl -k -X GET \
  "https://${NSX_MANAGER}/policy/api/v1/orgs/default/projects/project-quality/vpcs/web-vpc" \
  -H "Authorization: Basic ${AUTH}" | jq '.'
```

#### 列出VPC下的所有子网
```bash
curl -k -X GET \
  "https://${NSX_MANAGER}/policy/api/v1/orgs/default/projects/project-quality/vpcs/web-vpc/subnets" \
  -H "Authorization: Basic ${AUTH}" | jq '.results[] | {id: .id, display_name: .display_name}'
```

### 5.3 创建资源操作

#### 创建子网
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

#### 创建端口
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

### 5.4 更新资源操作

使用 `PATCH` 方法可以只更新部分字段：

```bash
curl -k -X PATCH \
  "https://${NSX_MANAGER}/policy/api/v1/orgs/default/projects/project-quality/vpcs/web-vpc" \
  -H "Authorization: Basic ${AUTH}" \
  -H "Content-Type: application/json" \
  -d '{
    "display_name": "Web Application VPC (Updated)"
  }'
```

### 5.5 删除资源操作

```bash
curl -k -X DELETE \
  "https://${NSX_MANAGER}/policy/api/v1/orgs/default/projects/project-quality/vpcs/web-vpc/subnets/my-subnet/ports/my-port" \
  -H "Authorization: Basic ${AUTH}"
```

---

## 6. 常见使用场景

### 6.1 Kubernetes集成场景

**场景**: 为Kubernetes集群自动创建网络资源

**流程**：
```
1. NCP/NSX Operator 监听 Kubernetes 事件
2. 创建 Namespace → 在NSX中创建VPC
3. 创建 Pod → 在NSX中创建Port
4. 创建 Service → 在NSX中创建LB Virtual Server
```

**相关API**：
- `/policy/api/v1/org-root` - 创建VPC层级
- `/orgs/{org}/projects/{project}/vpcs/{vpc}/subnets/{subnet}/ports/{port}` - 创建Pod端口
- `/policy/api/v1/infra/lb-virtual-servers/{vs-id}` - 创建Service负载均衡

### 6.2 网络隔离场景

**场景**: 为不同团队创建隔离的网络环境

**实现**：
```
组织: company
  ├─ 项目: team-a
  │   └─ VPC: team-a-prod (10.10.0.0/16)
  └─ 项目: team-b
      └─ VPC: team-b-prod (10.20.0.0/16)
```

### 6.3 负载均衡场景

**场景**: 为Web应用配置负载均衡

**步骤**：
1. 创建 LB Pool (后端服务器)
2. 创建 LB Virtual Server (前端VIP)
3. 配置健康检查
4. 添加后端成员

### 6.4 安全策略场景

**场景**: 实现微分段安全

**步骤**：
1. 创建 Security Group (定义工作负载)
2. 创建 Security Policy (定义规则)
3. 应用策略到特定Domain

---

## 7. 学习路径建议

### 7.1 初级阶段 (1-2周)

**目标**: 理解基本概念和结构

**学习内容**：
1. ✅ 阅读本文档
2. ✅ 理解层级结构：Org → Project → VPC → Subnet → Port
3. ✅ 练习基本的GET操作
4. ✅ 使用Search API查找资源

**练习任务**：
```bash
# 任务1: 列出所有VPC
# 任务2: 查看特定VPC的子网
# 任务3: 查找带有特定标签的资源
```

### 7.2 中级阶段 (2-4周)

**目标**: 掌握资源创建和管理

**学习内容**：
1. 创建VPC和子网
2. 管理端口生命周期
3. 配置负载均衡器
4. 理解标签(Tags)的使用

**练习任务**：
```bash
# 任务1: 创建完整的VPC层级结构
# 任务2: 为应用配置负载均衡
# 任务3: 实现基于标签的资源查询
```

### 7.3 高级阶段 (1-2月)

**目标**: 自动化和集成

**学习内容**：
1. 编写自动化脚本
2. 集成Kubernetes (NCP/NSX Operator)
3. 配置安全策略
4. 性能优化和故障排查

**练习任务**：
```bash
# 任务1: 编写Python/Go SDK调用NSX API
# 任务2: 实现Kubernetes网络自动化
# 任务3: 设计和实现微分段安全策略
```

### 7.4 推荐资源

**官方文档**：
- VMware NSX Documentation: https://docs.vmware.com/en/VMware-NSX/
- NSX Policy API Reference: https://developer.vmware.com/apis/nsx/

**实践环境**：
- VMware Hands-on Labs (免费)
- 搭建本地NSX测试环境

**社区资源**：
- VMware Code GitHub: https://github.com/vmware
- NSX Community Forums

---

## 8. 常见问题FAQ

### Q1: Policy API和Manager API有什么区别？

**A**: Policy API是新一代API，采用声明式设计，更简单易用。Manager API是旧API，正在逐步淘汰。**推荐使用Policy API**。

### Q2: 什么时候用PUT，什么时候用PATCH？

**A**: 
- **PATCH** (推荐): 只更新指定字段，其他字段保持不变
- **PUT**: 完全替换资源，需要提供所有必需字段

### Q3: 如何理解VPC和传统Segment的区别？

**A**:
- **Segment**: 传统NSX-T的网络段，扁平结构
- **VPC**: 新一代架构，有完整的组织层级，提供更好的隔离和管理

### Q4: Tags有什么用？

**A**: Tags用于：
- 资源分类和查找
- 关联到Kubernetes命名空间/Pod
- 安全策略的动态成员匹配
- 自动化工具的资源识别

### Q5: 如何查看资源的状态？

**A**: 大多数资源都有 `/state` 端点：
```bash
GET /orgs/{org}/projects/{project}/vpcs/{vpc}/subnets/{subnet}/ports/{port}/state
```

### Q6: 为什么有些资源返回404？

**A**: 可能原因：
1. 资源已被删除
2. 路径或ID拼写错误
3. 没有权限访问
4. 资源还未创建完成（异步操作）

### Q7: 如何处理大量资源查询？

**A**: 使用分页参数：
```bash
GET /policy/api/v1/search/query?query=...&page_size=100&cursor=xxx
```

### Q8: API调用速率有限制吗？

**A**: 是的，NSX有速率限制。建议：
- 使用批量操作而不是逐个操作
- 实现指数退避重试机制
- 监控响应头中的速率限制信息

---

## 9. 附录：快速参考

### 9.1 常用端点速查

| 功能 | 端点 | 方法 |
|------|------|------|
| 搜索资源 | `/search/query` | GET |
| 组织根 | `/org-root` | GET, PATCH |
| VPC列表 | `/orgs/{org}/projects/{project}/vpcs` | GET |
| 创建子网 | `/orgs/{org}/projects/{project}/vpcs/{vpc}/subnets/{subnet}` | PATCH |
| 端口详情 | `/orgs/{org}/projects/{project}/vpcs/{vpc}/subnets/{subnet}/ports/{port}` | GET |
| LB Pool | `/infra/lb-pools/{pool}` | GET, PATCH, DELETE |
| 证书管理 | `/infra/certificates` | GET |

### 9.2 常用查询参数

```bash
# 按资源类型搜索
?query=resource_type:Vpc

# 按标签搜索
?query=tags.scope:nsx-op/cluster AND tags.tag:cluster-id

# 排序
?sort_by=id

# 分页
?page_size=100&cursor=xxx
```

### 9.3 HTTP状态码

| 状态码 | 含义 | 处理方式 |
|--------|------|---------|
| 200 OK | 成功 | 解析响应 |
| 400 Bad Request | 请求格式错误 | 检查JSON格式 |
| 404 Not Found | 资源不存在 | 检查路径和ID |
| 409 Conflict | 资源已存在 | 使用PATCH代替PUT |
| 500 Internal Server Error | 服务器错误 | 重试或联系管理员 |

---

## 10. 总结

🎯 **关键要点回顾**：

1. **层级理解**: Org → Project → VPC → Subnet → Port
2. **声明式API**: 描述目标状态，NSX自动实现
3. **标签驱动**: 使用tags实现动态管理
4. **Search API**: 你的探索起点
5. **PATCH优先**: 更新操作首选PATCH方法

🚀 **下一步行动**：

1. 使用本文档中的示例进行实际操作
2. 阅读完整的API报告文档（416个端点详情）
3. 在测试环境中创建自己的VPC
4. 编写自动化脚本

📚 **持续学习**：

- 定期查看VMware官方文档更新
- 参与NSX社区讨论
- 实践中遇到问题，使用Search API和实际响应作为参考

---

**文档版本**: v1.0  
**最后更新**: 2025-10-17  
**作者**: Based on real NSX Policy API analysis  
**反馈**: 如有问题或建议，欢迎提出

---

## 相关文档

- 📄 [完整NSX Policy API报告](/Users/zhengxie/Downloads/nsx_policy_api_report_with_log_responses.md) - 416个端点详细文档（含日志响应）
- 📖 [NSX API Template](./nsx_api_template.md) - API使用模板和示例

---

**Happy Learning! 🎉**
