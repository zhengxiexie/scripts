# NSX Policy API Endpoints Report

**Generated from log analysis**
**Total unique endpoints:** 416

---

## Summary Statistics

- **Total endpoints:** 416
- **By HTTP method:**
  - DELETE: 147
  - GET: 414
  - PATCH: 185
- **Endpoints with request bodies:** 72

---


**📊 Log-Based Enhancement:**
- ✨ 151 endpoints enhanced with responses from logs
- 📁 Source: NSX pod logs (nsx-ncp, nsx-operator, nsx-ncp-upgrade)
- 💡 Real production data from your NSX deployment
- ⏱️ Data captured: 2025-10-17

## 📑 Table of Contents - API Endpoints

**Quick Navigation:** Click any path to jump to its details

### By Hierarchy Level

#### Level 4 (1 endpoints)

1. [`/policy/api/v1/org-root`](#1-policy-api-v1-org-root)

#### Level 5 (6 endpoints)

2. [`/policy/api/v1/search/query`](#2-policy-api-v1-search-query)
3. [`/policy/api/v1/infra/ip-blocks`](#3-policy-api-v1-infra-ip-blocks)
4. [`/policy/api/v1/infra/certificates`](#4-policy-api-v1-infra-certificates)
5. [`/policy/api/v1/infra/lb-app-profiles`](#5-policy-api-v1-infra-lb-app-profiles)
6. [`/policy/api/v1/infra/lb-client-ssl-profiles`](#6-policy-api-v1-infra-lb-client-ssl-profiles)
7. [`/policy/api/v1/infra/lb-server-ssl-profiles`](#7-policy-api-v1-infra-lb-server-ssl-profiles)

#### Level 6 (89 endpoints)

8. [`/policy/api/v1/infra/lb-pools/tea-svc_80_TCP_39r0c`](#8-policy-api-v1-infra-lb-pools-tea-svc-80-tcp-39r0c)
9. [`/policy/api/v1/infra/lb-pools/tea-svc_80_TCP_p5j45`](#9-policy-api-v1-infra-lb-pools-tea-svc-80-tcp-p5j45)
10. [`/policy/api/v1/infra/lb-pools/tea-svc_80_UDP_39r0c`](#10-policy-api-v1-infra-lb-pools-tea-svc-80-udp-39r0c)
11. [`/policy/api/v1/infra/realized-state/realized-entity`](#11-policy-api-v1-infra-realized-state-realized-entity)
12. [`/policy/api/v1/infra/lb-pools/coffee-svc_80_TCP_cnml1`](#12-policy-api-v1-infra-lb-pools-coffee-svc-80-tcp-cnml1)
13. [`/policy/api/v1/infra/realized-state/realized-entities`](#13-policy-api-v1-infra-realized-state-realized-entities)
14. [`/policy/api/v1/infra/lb-pools/default-svc_80_TCP_i3q14`](#14-policy-api-v1-infra-lb-pools-default-svc-80-tcp-i3q14)
15. [`/policy/api/v1/infra/lb-pools/default-svc_80_UDP_i3q14`](#15-policy-api-v1-infra-lb-pools-default-svc-80-udp-i3q14)
16. [`/policy/api/v1/infra/lb-pools/nsx-operator_8093_TCP_s6pir`](#16-policy-api-v1-infra-lb-pools-nsx-operator-8093-tcp-s6pir)
17. [`/policy/api/v1/infra/lb-virtual-servers/tea-svc_80_TCP_39r0c`](#17-policy-api-v1-infra-lb-virtual-servers-tea-svc-80-tcp-39r0c)
18. [`/policy/api/v1/infra/lb-virtual-servers/tea-svc_80_TCP_p5j45`](#18-policy-api-v1-infra-lb-virtual-servers-tea-svc-80-tcp-p5j45)
19. [`/policy/api/v1/infra/lb-virtual-servers/tea-svc_80_UDP_39r0c`](#19-policy-api-v1-infra-lb-virtual-servers-tea-svc-80-udp-39r0c)
20. [`/policy/api/v1/infra/lb-virtual-servers/kube-dns_53_TCP_hof1c`](#20-policy-api-v1-infra-lb-virtual-servers-kube-dns-53-tcp-hof1c)
21. [`/policy/api/v1/infra/lb-virtual-servers/kube-dns_53_UDP_hof1c`](#21-policy-api-v1-infra-lb-virtual-servers-kube-dns-53-udp-hof1c)
22. [`/policy/api/v1/infra/lb-virtual-servers/coffee-svc_80_TCP_cnml1`](#22-policy-api-v1-infra-lb-virtual-servers-coffee-svc-80-tcp-cnml1)
23. [`/policy/api/v1/infra/lb-pools/prevpc-loadbalancer_8080_TCP_j7n9u`](#23-policy-api-v1-infra-lb-pools-prevpc-loadbalancer-8080-tcp-j7n9u)
24. [`/policy/api/v1/infra/lb-pools/test-service-1bcb333c_80_TCP_9rdbd`](#24-policy-api-v1-infra-lb-pools-test-service-1bcb333c-80-tcp-9rdbd)
25. [`/policy/api/v1/infra/lb-pools/test-service-da1e3736_80_TCP_2bcu3`](#25-policy-api-v1-infra-lb-pools-test-service-da1e3736-80-tcp-2bcu3)
26. [`/policy/api/v1/infra/lb-virtual-servers/default-svc_80_TCP_i3q14`](#26-policy-api-v1-infra-lb-virtual-servers-default-svc-80-tcp-i3q14)
27. [`/policy/api/v1/infra/lb-virtual-servers/default-svc_80_UDP_i3q14`](#27-policy-api-v1-infra-lb-virtual-servers-default-svc-80-udp-i3q14)
28. [`/policy/api/v1/infra/lb-virtual-servers/kube-dns-lb_53_TCP_aajir`](#28-policy-api-v1-infra-lb-virtual-servers-kube-dns-lb-53-tcp-aajir)
29. [`/policy/api/v1/infra/lb-virtual-servers/kube-dns-lb_53_UDP_aajir`](#29-policy-api-v1-infra-lb-virtual-servers-kube-dns-lb-53-udp-aajir)
30. [`/policy/api/v1/infra/lb-virtual-servers/kubernetes_443_TCP_6mqcw`](#30-policy-api-v1-infra-lb-virtual-servers-kubernetes-443-tcp-6mqcw)
31. [`/policy/api/v1/infra/domains/f06fd228-8088-4439-a9e6-26c90a829c57`](#31-policy-api-v1-infra-domains-f06fd228-8088-4439-a9e6-26c90a829c57)
32. [`/policy/api/v1/infra/lb-virtual-servers/cert-manager_9402_TCP_gk8qf`](#32-policy-api-v1-infra-lb-virtual-servers-cert-manager-9402-tcp-gk8qf)
33. [`/policy/api/v1/infra/lb-virtual-servers/nsx-operator_8093_TCP_s6pir`](#33-policy-api-v1-infra-lb-virtual-servers-nsx-operator-8093-tcp-s6pir)
34. [`/policy/api/v1/infra/lb-virtual-servers/packaging-api_443_TCP_oa5ep`](#34-policy-api-v1-infra-lb-virtual-servers-packaging-api-443-tcp-oa5ep)
35. [`/policy/api/v1/infra/lb-virtual-servers/packaging-api_8080_TCP_oa5ep`](#35-policy-api-v1-infra-lb-virtual-servers-packaging-api-8080-tcp-oa5ep)
36. [`/policy/api/v1/infra/lb-virtual-servers/webhook-service_443_TCP_tuo3j`](#36-policy-api-v1-infra-lb-virtual-servers-webhook-service-443-tcp-tuo3j)
37. [`/policy/api/v1/infra/lb-virtual-servers/docker-registry_5000_TCP_goaln`](#37-policy-api-v1-infra-lb-virtual-servers-docker-registry-5000-tcp-goaln)
38. [`/policy/api/v1/infra/lb-virtual-servers/mgmt-image-proxy_443_TCP_1k4gd`](#38-policy-api-v1-infra-lb-virtual-servers-mgmt-image-proxy-443-tcp-1k4gd)
39. [`/policy/api/v1/infra/lb-virtual-servers/kube-dns-metrics_9153_TCP_ea0v8`](#39-policy-api-v1-infra-lb-virtual-servers-kube-dns-metrics-9153-tcp-ea0v8)
40. [`/policy/api/v1/infra/lb-virtual-servers/telegraf-deploy_10013_TCP_6o1fu`](#40-policy-api-v1-infra-lb-virtual-servers-telegraf-deploy-10013-tcp-6o1fu)
41. [`/policy/api/v1/infra/lb-virtual-servers/kubernetes-internal_443_TCP_p5727`](#41-policy-api-v1-infra-lb-virtual-servers-kubernetes-internal-443-tcp-p5727)
42. [`/policy/api/v1/infra/lb-virtual-servers/capi-webhook-service_443_TCP_r0p2b`](#42-policy-api-v1-infra-lb-virtual-servers-capi-webhook-service-443-tcp-r0p2b)
43. [`/policy/api/v1/infra/lb-virtual-servers/capv-webhook-service_443_TCP_6heqj`](#43-policy-api-v1-infra-lb-virtual-servers-capv-webhook-service-443-tcp-6heqj)
44. [`/policy/api/v1/infra/lb-virtual-servers/cert-manager-webhook_443_TCP_chss8`](#44-policy-api-v1-infra-lb-virtual-servers-cert-manager-webhook-443-tcp-chss8)
45. [`/policy/api/v1/infra/lb-virtual-servers/prevpc-loadbalancer_8080_TCP_j7n9u`](#45-policy-api-v1-infra-lb-virtual-servers-prevpc-loadbalancer-8080-tcp-j7n9u)
46. [`/policy/api/v1/infra/lb-virtual-servers/test-service-1bcb333c_80_TCP_9rdbd`](#46-policy-api-v1-infra-lb-virtual-servers-test-service-1bcb333c-80-tcp-9rdbd)
47. [`/policy/api/v1/infra/lb-virtual-servers/test-service-da1e3736_80_TCP_2bcu3`](#47-policy-api-v1-infra-lb-virtual-servers-test-service-da1e3736-80-tcp-2bcu3)
48. [`/policy/api/v1/infra/lb-virtual-servers/tkgs-plugin-service_8099_TCP_b6qai`](#48-policy-api-v1-infra-lb-virtual-servers-tkgs-plugin-service-8099-tcp-b6qai)
49. [`/policy/api/v1/infra/lb-virtual-servers/kube-apiserver-lb-svc_443_TCP_671rx`](#49-policy-api-v1-infra-lb-virtual-servers-kube-apiserver-lb-svc-443-tcp-671rx)
50. [`/policy/api/v1/infra/lb-virtual-servers/pinniped-supervisor_12001_TCP_ie6ph`](#50-policy-api-v1-infra-lb-virtual-servers-pinniped-supervisor-12001-tcp-ie6ph)
51. [`/policy/api/v1/infra/lb-virtual-servers/kube-apiserver-lb-svc_6443_TCP_671rx`](#51-policy-api-v1-infra-lb-virtual-servers-kube-apiserver-lb-svc-6443-tcp-671rx)
52. [`/policy/api/v1/infra/lb-virtual-servers/machine-agent-service_9443_TCP_6iexa`](#52-policy-api-v1-infra-lb-virtual-servers-machine-agent-service-9443-tcp-6iexa)
53. [`/policy/api/v1/infra/lb-virtual-servers/pinniped-concierge-api_443_TCP_62uni`](#53-policy-api-v1-infra-lb-virtual-servers-pinniped-concierge-api-443-tcp-62uni)
54. [`/policy/api/v1/infra/lb-virtual-servers/pinniped-supervisor-api_443_TCP_l261w`](#54-policy-api-v1-infra-lb-virtual-servers-pinniped-supervisor-api-443-tcp-l261w)
55. [`/policy/api/v1/infra/lb-virtual-servers/vsphere-csi-controller_2112_TCP_rz7ds`](#55-policy-api-v1-infra-lb-virtual-servers-vsphere-csi-controller-2112-tcp-rz7ds)
56. [`/policy/api/v1/infra/lb-virtual-servers/vsphere-csi-controller_2113_TCP_rz7ds`](#56-policy-api-v1-infra-lb-virtual-servers-vsphere-csi-controller-2113-tcp-rz7ds)
57. [`/policy/api/v1/infra/lb-virtual-servers/pinniped-concierge-proxy_443_TCP_1miab`](#57-policy-api-v1-infra-lb-virtual-servers-pinniped-concierge-proxy-443-tcp-1miab)
58. [`/policy/api/v1/infra/lb-virtual-servers/snapshot-validation-service_443_TCP_8p66x`](#58-policy-api-v1-infra-lb-virtual-servers-snapshot-validation-service-443-tcp-8p66x)
59. [`/policy/api/v1/infra/lb-virtual-servers/upgrade-compatibility-service_80_TCP_gdqw0`](#59-policy-api-v1-infra-lb-virtual-servers-upgrade-compatibility-service-80-tcp-gdqw0)
60. [`/policy/api/v1/infra/lb-virtual-servers/kube-apiserver-authproxy-svc_8443_TCP_hwe7d`](#60-policy-api-v1-infra-lb-virtual-servers-kube-apiserver-authproxy-svc-8443-tcp-hwe7d)
61. [`/policy/api/v1/infra/lb-virtual-servers/storage-quota-webhook-service_443_TCP_q6397`](#61-policy-api-v1-infra-lb-virtual-servers-storage-quota-webhook-service-443-tcp-q6397)
62. [`/policy/api/v1/infra/lb-virtual-servers/cns-vsphere-vmware-com-service_443_TCP_fbd1t`](#62-policy-api-v1-infra-lb-virtual-servers-cns-vsphere-vmware-com-service-443-tcp-fbd1t)
63. [`/policy/api/v1/infra/lb-virtual-servers/tkr-conversion-webhook-service_443_TCP_sxd9x`](#63-policy-api-v1-infra-lb-virtual-servers-tkr-conversion-webhook-service-443-tcp-sxd9x)
64. [`/policy/api/v1/infra/lb-pools/vmware-system-nsx-operator-webhook-service_443_TCP_apze8`](#64-policy-api-v1-infra-lb-pools-vmware-system-nsx-operator-webhook-service-443-tcp-apze8)
65. [`/policy/api/v1/infra/lb-virtual-servers/runtime-extension-webhook-service_443_TCP_snr9y`](#65-policy-api-v1-infra-lb-virtual-servers-runtime-extension-webhook-service-443-tcp-snr9y)
66. [`/policy/api/v1/infra/lb-virtual-servers/vmware-system-csi-webhook-service_443_TCP_2ypm7`](#66-policy-api-v1-infra-lb-virtual-servers-vmware-system-csi-webhook-service-443-tcp-2ypm7)
67. [`/policy/api/v1/infra/lb-virtual-servers/vmware-system-tkg-webhook-service_443_TCP_7jv1e`](#67-policy-api-v1-infra-lb-virtual-servers-vmware-system-tkg-webhook-service-443-tcp-7jv1e)
68. [`/policy/api/v1/infra/lb-virtual-servers/runtime-extension-metrics-service_9876_TCP_axzz2`](#68-policy-api-v1-infra-lb-virtual-servers-runtime-extension-metrics-service-9876-tcp-axzz2)
69. [`/policy/api/v1/infra/lb-virtual-servers/vmware-system-nsop-webhook-service_443_TCP_l6xiz`](#69-policy-api-v1-infra-lb-virtual-servers-vmware-system-nsop-webhook-service-443-tcp-l6xiz)
70. [`/policy/api/v1/infra/lb-virtual-servers/vmware-system-vmop-webhook-service_443_TCP_qduvo`](#70-policy-api-v1-infra-lb-virtual-servers-vmware-system-vmop-webhook-service-443-tcp-qduvo)
71. [`/policy/api/v1/infra/lb-virtual-servers/tanzu-addons-manager-webhook-service_443_TCP_diwwz`](#71-policy-api-v1-infra-lb-virtual-servers-tanzu-addons-manager-webhook-service-443-tcp-diwwz)
72. [`/policy/api/v1/infra/lb-virtual-servers/tkr-resolver-cluster-webhook-service_443_TCP_nc6lk`](#72-policy-api-v1-infra-lb-virtual-servers-tkr-resolver-cluster-webhook-service-443-tcp-nc6lk)
73. [`/policy/api/v1/infra/lb-virtual-servers/tanzu-addons-manager-metrics-service_9946_TCP_jqdpt`](#73-policy-api-v1-infra-lb-virtual-servers-tanzu-addons-manager-metrics-service-9946-tcp-jqdpt)
74. [`/policy/api/v1/infra/lb-virtual-servers/capi-kubeadm-bootstrap-webhook-service_443_TCP_6xo5g`](#74-policy-api-v1-infra-lb-virtual-servers-capi-kubeadm-bootstrap-webhook-service-443-tcp-6xo5g)
75. [`/policy/api/v1/infra/lb-virtual-servers/vmware-system-vmop-web-console-validator_80_TCP_lzxdi`](#75-policy-api-v1-infra-lb-virtual-servers-vmware-system-vmop-web-console-validator-80-tcp-lzxdi)
76. [`/policy/api/v1/infra/lb-virtual-servers/capi-controller-manager-metrics-service_9844_TCP_47mar`](#76-policy-api-v1-infra-lb-virtual-servers-capi-controller-manager-metrics-service-9844-tcp-47mar)
77. [`/policy/api/v1/infra/lb-virtual-servers/capv-controller-manager-metrics-service_9846_TCP_7af8y`](#77-policy-api-v1-infra-lb-virtual-servers-capv-controller-manager-metrics-service-9846-tcp-7af8y)
78. [`/policy/api/v1/infra/lb-virtual-servers/vmware-system-tkg-state-metrics-service_9855_TCP_86h2q`](#78-policy-api-v1-infra-lb-virtual-servers-vmware-system-tkg-state-metrics-service-9855-tcp-86h2q)
79. [`/policy/api/v1/infra/lb-virtual-servers/vmware-system-ako-ako-vks-webhook-service_443_TCP_gdbxh`](#79-policy-api-v1-infra-lb-virtual-servers-vmware-system-ako-ako-vks-webhook-service-443-tcp-gdbxh)
80. [`/policy/api/v1/infra/lb-virtual-servers/vmware-system-appplatform-webhook-service_443_TCP_3myq0`](#80-policy-api-v1-infra-lb-virtual-servers-vmware-system-appplatform-webhook-service-443-tcp-3myq0)
81. [`/policy/api/v1/infra/lb-virtual-servers/capi-kubeadm-control-plane-webhook-service_443_TCP_29ytg`](#81-policy-api-v1-infra-lb-virtual-servers-capi-kubeadm-control-plane-webhook-service-443-tcp-29ytg)
82. [`/policy/api/v1/infra/lb-virtual-servers/vmware-system-nsx-operator-webhook-service_443_TCP_apze8`](#82-policy-api-v1-infra-lb-virtual-servers-vmware-system-nsx-operator-webhook-service-443-tcp-apze8)
83. [`/policy/api/v1/infra/lb-virtual-servers/vmware-system-psp-operator-webhook-service_443_TCP_n4jep`](#83-policy-api-v1-infra-lb-virtual-servers-vmware-system-psp-operator-webhook-service-443-tcp-n4jep)
84. [`/policy/api/v1/infra/lb-virtual-servers/vmware-system-tkg-webhook-metrics-service_9947_TCP_ie9jg`](#84-policy-api-v1-infra-lb-virtual-servers-vmware-system-tkg-webhook-metrics-service-9947-tcp-ie9jg)
85. [`/policy/api/v1/infra/lb-virtual-servers/vmware-system-imageregistry-webhook-service_443_TCP_ebvnb`](#85-policy-api-v1-infra-lb-virtual-servers-vmware-system-imageregistry-webhook-service-443-tcp-ebvnb)
86. [`/policy/api/v1/infra/lb-virtual-servers/vmware-system-observability-webhook-service_443_TCP_mh1m0`](#86-policy-api-v1-infra-lb-virtual-servers-vmware-system-observability-webhook-service-443-tcp-mh1m0)
87. [`/policy/api/v1/infra/lb-virtual-servers/vmware-system-mobility-operator-webhook-service_443_TCP_2u6xd`](#87-policy-api-v1-infra-lb-virtual-servers-vmware-system-mobility-operator-webhook-service-443-tcp-2u6xd)
88. [`/policy/api/v1/infra/lb-virtual-servers/vmware-system-tkg-controller-manager-metrics-service_9847_TCP_e9fxc`](#88-policy-api-v1-infra-lb-virtual-servers-vmware-system-tkg-controller-manager-metrics-service-9847-tcp-e9fxc)
89. [`/policy/api/v1/infra/lb-virtual-servers/vmware-system-vmop-controller-manager-metrics-service_9848_TCP_qgstw`](#89-policy-api-v1-infra-lb-virtual-servers-vmware-system-vmop-controller-manager-metrics-service-9848-tcp-qgstw)
90. [`/policy/api/v1/infra/lb-virtual-servers/vmware-system-netop-controller-manager-metrics-service_9851_TCP_rfjax`](#90-policy-api-v1-infra-lb-virtual-servers-vmware-system-netop-controller-manager-metrics-service-9851-tcp-rfjax)
91. [`/policy/api/v1/infra/lb-virtual-servers/vmware-system-psp-operator-k8s-cloud-operator-service_29002_TCP_dcp8m`](#91-policy-api-v1-infra-lb-virtual-servers-vmware-system-psp-operator-k8s-cloud-operator-service-29002-tcp-dcp8m)
92. [`/policy/api/v1/infra/lb-virtual-servers/capi-kubeadm-bootstrap-controller-manager-metrics-service_9845_TCP_1rbtg`](#92-policy-api-v1-infra-lb-virtual-servers-capi-kubeadm-bootstrap-controller-manager-metrics-service-9845-tcp-1rbtg)
93. [`/policy/api/v1/infra/lb-virtual-servers/vmware-system-mobility-operator-controller-manager-metrics_9859_TCP_3y8qy`](#93-policy-api-v1-infra-lb-virtual-servers-vmware-system-mobility-operator-controller-manager-metrics-9859-tcp-3y8qy)
94. [`/policy/api/v1/infra/lb-virtual-servers/capi-kubeadm-control-plane-controller-manager-metrics-service_9850_TCP_7eapm`](#94-policy-api-v1-infra-lb-virtual-servers-capi-kubeadm-control-plane-controller-manager-metrics-service-9850-tcp-7eapm)
95. [`/policy/api/v1/infra/lb-virtual-servers/vmware-system-imageregistry-controller-manager-metrics-service_9857_TCP_k3hd3`](#95-policy-api-v1-infra-lb-virtual-servers-vmware-system-imageregistry-controller-manager-metrics-service-9857-tcp-k3hd3)
96. [`/policy/api/v1/infra/lb-virtual-servers/vmware-system-observability-controller-manager-metrics-service_9889_TCP_nus7f`](#96-policy-api-v1-infra-lb-virtual-servers-vmware-system-observability-controller-manager-metrics-service-9889-tcp-nus7f)

#### Level 7 (3 endpoints)

97. [`/policy/api/v1/infra/tier-0s/None/locale-services`](#97-policy-api-v1-infra-tier-0s-none-locale-services)
98. [`/policy/api/v1/orgs/default/projects/project-quality`](#98-policy-api-v1-orgs-default-projects-project-quality)
99. [`/policy/api/v1/infra/shares/f06fd228-8088-4439-a9e6-26c90a829c57_vpc-share-resources/resources`](#99-policy-api-v1-infra-shares-f06fd228-8088-4439-a9e6-26c90a829c57-vpc-share-resources-resources)

#### Level 8 (2 endpoints)

100. [`/policy/api/v1/infra/sites/default/enforcement-points/alb-endpoint`](#100-policy-api-v1-infra-sites-default-enforcement-points-alb-endpoint)
101. [`/policy/api/v1/infra/domains/f06fd228-8088-4439-a9e6-26c90a829c57/groups/clusterip_f06fd228-8088-4439-a9e6-26c90a829c57_all_segments`](#101-policy-api-v1-infra-domains-f06fd228-8088-4439-a9e6-26c90a829c57-groups-clusterip-f06fd228-8088-4439-a9e6-26c90a829c57-all-segments)

#### Level 9 (35 endpoints)

102. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/testvpc-3658f2b5`](#102-policy-api-v1-orgs-default-projects-project-quality-vpcs-testvpc-3658f2b5)
103. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/testvpc-461b1395`](#103-policy-api-v1-orgs-default-projects-project-quality-vpcs-testvpc-461b1395)
104. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/testvpc-7ab2d8aa`](#104-policy-api-v1-orgs-default-projects-project-quality-vpcs-testvpc-7ab2d8aa)
105. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/testvpc-d15ad1fd`](#105-policy-api-v1-orgs-default-projects-project-quality-vpcs-testvpc-d15ad1fd)
106. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/testvpc-e65918e1`](#106-policy-api-v1-orgs-default-projects-project-quality-vpcs-testvpc-e65918e1)
107. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/web-da775e6f_6o7ts`](#107-policy-api-v1-orgs-default-projects-project-quality-vpcs-web-da775e6f-6o7ts)
108. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/client-91c3f484_qzuxu`](#108-policy-api-v1-orgs-default-projects-project-quality-vpcs-client-91c3f484-qzuxu)
109. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/test-lb-50fedbb3_mv836`](#109-policy-api-v1-orgs-default-projects-project-quality-vpcs-test-lb-50fedbb3-mv836)
110. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/test-pod-1dd9a577_fu9t5`](#110-policy-api-v1-orgs-default-projects-project-quality-vpcs-test-pod-1dd9a577-fu9t5)
111. [`/policy/api/v1/infra/sites/default/enforcement-points/default/host-transport-nodes`](#111-policy-api-v1-infra-sites-default-enforcement-points-default-host-transport-nodes)
112. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/target-ns-56446c91_6zdip`](#112-policy-api-v1-orgs-default-projects-project-quality-vpcs-target-ns-56446c91-6zdip)
113. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/update-ns-8eb115ed_baxdx`](#113-policy-api-v1-orgs-default-projects-project-quality-vpcs-update-ns-8eb115ed-baxdx)
114. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/subnet-e2e-1f11082b_56qvy`](#114-policy-api-v1-orgs-default-projects-project-quality-vpcs-subnet-e2e-1f11082b-56qvy)
115. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/staticroute-eb4f3a68_rxtge`](#115-policy-api-v1-orgs-default-projects-project-quality-vpcs-staticroute-eb4f3a68-rxtge)
116. [`/policy/api/v1/orgs/default/projects/project-quality/vpc-connectivity-profiles/no-nat`](#116-policy-api-v1-orgs-default-projects-project-quality-vpc-connectivity-profiles-no-nat)
117. [`/policy/api/v1/orgs/default/projects/project-quality/vpc-connectivity-profiles/default`](#117-policy-api-v1-orgs-default-projects-project-quality-vpc-connectivity-profiles-default)
118. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/customized-ns-99beca1e_yleom`](#118-policy-api-v1-orgs-default-projects-project-quality-vpcs-customized-ns-99beca1e-yleom)
119. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/test-pod-sync-e8b8a7ca_m404i`](#119-policy-api-v1-orgs-default-projects-project-quality-vpcs-test-pod-sync-e8b8a7ca-m404i)
120. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/shared-vpc-ns-0-3bc799ba_nwr40`](#120-policy-api-v1-orgs-default-projects-project-quality-vpcs-shared-vpc-ns-0-3bc799ba-nwr40)
121. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/test-netpol-sync-c2cf40cd_65gvf`](#121-policy-api-v1-orgs-default-projects-project-quality-vpcs-test-netpol-sync-c2cf40cd-65gvf)
122. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/test-ingress-sync-73e76bf1_rbp33`](#122-policy-api-v1-orgs-default-projects-project-quality-vpcs-test-ingress-sync-73e76bf1-rbp33)
123. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/test-service-sync-f1d17bff_5230b`](#123-policy-api-v1-orgs-default-projects-project-quality-vpcs-test-service-sync-f1d17bff-5230b)
124. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/networkinfo-default-efa7e691_1fkak`](#124-policy-api-v1-orgs-default-projects-project-quality-vpcs-networkinfo-default-efa7e691-1fkak)
125. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/test-namespace-sync-49fbe5bd_p9u70`](#125-policy-api-v1-orgs-default-projects-project-quality-vpcs-test-namespace-sync-49fbe5bd-p9u70)
126. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/precreated-target-ns-3c7c1821_v5ml5`](#126-policy-api-v1-orgs-default-projects-project-quality-vpcs-precreated-target-ns-3c7c1821-v5ml5)
127. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/test-create-vm-basic-f449d9bf_3ehn6`](#127-policy-api-v1-orgs-default-projects-project-quality-vpcs-test-create-vm-basic-f449d9bf-3ehn6)
128. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/precreated-subnet-ns1-a72a2a9d_8m6zu`](#128-policy-api-v1-orgs-default-projects-project-quality-vpcs-precreated-subnet-ns1-a72a2a9d-8m6zu)
129. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/precreated-subnet-ns2-42ff4c1a_tpi2w`](#129-policy-api-v1-orgs-default-projects-project-quality-vpcs-precreated-subnet-ns2-42ff4c1a-tpi2w)
130. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/test-security-policy-web-a2b779b4_f6e79`](#130-policy-api-v1-orgs-default-projects-project-quality-vpcs-test-security-policy-web-a2b779b4-f6e79)
131. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/test-ipaddress-allocation-40d5699d_2p2tu`](#131-policy-api-v1-orgs-default-projects-project-quality-vpcs-test-ipaddress-allocation-40d5699d-2p2tu)
132. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/test-security-policy-basic-72ecfa65_ib6li`](#132-policy-api-v1-orgs-default-projects-project-quality-vpcs-test-security-policy-basic-72ecfa65-ib6li)
133. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/test-security-policy-client-3a06d660_qiyvu`](#133-policy-api-v1-orgs-default-projects-project-quality-vpcs-test-security-policy-client-3a06d660-qiyvu)
134. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/vmware-system-supervisor-services-vpc_kzc7e`](#134-policy-api-v1-orgs-default-projects-project-quality-vpcs-vmware-system-supervisor-services-vpc-kzc7e)
135. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/test-security-policy-add-delete-0e034260_aruoj`](#135-policy-api-v1-orgs-default-projects-project-quality-vpcs-test-security-policy-add-delete-0e034260-aruoj)
136. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/test-security-policy-match-expression-ff1dafa9_bgm74`](#136-policy-api-v1-orgs-default-projects-project-quality-vpcs-test-security-policy-match-expression-ff1dafa9-bgm74)

#### Level 10 (12 endpoints)

137. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/testvpc-3658f2b5/vpc-lbs`](#137-policy-api-v1-orgs-default-projects-project-quality-vpcs-testvpc-3658f2b5-vpc-lbs)
138. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/testvpc-7ab2d8aa/vpc-lbs`](#138-policy-api-v1-orgs-default-projects-project-quality-vpcs-testvpc-7ab2d8aa-vpc-lbs)
139. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/testvpc-d15ad1fd/vpc-lbs`](#139-policy-api-v1-orgs-default-projects-project-quality-vpcs-testvpc-d15ad1fd-vpc-lbs)
140. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/testvpc-e65918e1/vpc-lbs`](#140-policy-api-v1-orgs-default-projects-project-quality-vpcs-testvpc-e65918e1-vpc-lbs)
141. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/testvpc-3658f2b5/attachments`](#141-policy-api-v1-orgs-default-projects-project-quality-vpcs-testvpc-3658f2b5-attachments)
142. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/testvpc-461b1395/attachments`](#142-policy-api-v1-orgs-default-projects-project-quality-vpcs-testvpc-461b1395-attachments)
143. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/testvpc-7ab2d8aa/attachments`](#143-policy-api-v1-orgs-default-projects-project-quality-vpcs-testvpc-7ab2d8aa-attachments)
144. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/testvpc-d15ad1fd/attachments`](#144-policy-api-v1-orgs-default-projects-project-quality-vpcs-testvpc-d15ad1fd-attachments)
145. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/testvpc-e65918e1/attachments`](#145-policy-api-v1-orgs-default-projects-project-quality-vpcs-testvpc-e65918e1-attachments)
146. [`/policy/api/v1/orgs/default/projects/project-quality/transit-gateways/default/attachments`](#146-policy-api-v1-orgs-default-projects-project-quality-transit-gateways-default-attachments)
147. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/vmware-system-supervisor-services-vpc_kzc7e/vpc-lbs`](#147-policy-api-v1-orgs-default-projects-project-quality-vpcs-vmware-system-supervisor-services-vpc-kzc7e-vpc-lbs)
148. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/vmware-system-supervisor-services-vpc_kzc7e/attachments`](#148-policy-api-v1-orgs-default-projects-project-quality-vpcs-vmware-system-supervisor-services-vpc-kzc7e-attachments)

#### Level 11 (119 endpoints)

149. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/testvpc-3658f2b5/vpc-lbs/default`](#149-policy-api-v1-orgs-default-projects-project-quality-vpcs-testvpc-3658f2b5-vpc-lbs-default)
150. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/testvpc-d15ad1fd/vpc-lbs/default`](#150-policy-api-v1-orgs-default-projects-project-quality-vpcs-testvpc-d15ad1fd-vpc-lbs-default)
151. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/web-da775e6f_6o7ts/vpc-lbs/default`](#151-policy-api-v1-orgs-default-projects-project-quality-vpcs-web-da775e6f-6o7ts-vpc-lbs-default)
152. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/client-91c3f484_qzuxu/vpc-lbs/default`](#152-policy-api-v1-orgs-default-projects-project-quality-vpcs-client-91c3f484-qzuxu-vpc-lbs-default)
153. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/test-lb-50fedbb3_mv836/vpc-lbs/default`](#153-policy-api-v1-orgs-default-projects-project-quality-vpcs-test-lb-50fedbb3-mv836-vpc-lbs-default)
154. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/web-da775e6f_6o7ts/attachments/default`](#154-policy-api-v1-orgs-default-projects-project-quality-vpcs-web-da775e6f-6o7ts-attachments-default)
155. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/test-pod-1dd9a577_fu9t5/vpc-lbs/default`](#155-policy-api-v1-orgs-default-projects-project-quality-vpcs-test-pod-1dd9a577-fu9t5-vpc-lbs-default)
156. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/target-ns-56446c91_6zdip/vpc-lbs/default`](#156-policy-api-v1-orgs-default-projects-project-quality-vpcs-target-ns-56446c91-6zdip-vpc-lbs-default)
157. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/update-ns-8eb115ed_baxdx/vpc-lbs/default`](#157-policy-api-v1-orgs-default-projects-project-quality-vpcs-update-ns-8eb115ed-baxdx-vpc-lbs-default)
158. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/client-91c3f484_qzuxu/attachments/default`](#158-policy-api-v1-orgs-default-projects-project-quality-vpcs-client-91c3f484-qzuxu-attachments-default)
159. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/subnet-e2e-1f11082b_56qvy/vpc-lbs/default`](#159-policy-api-v1-orgs-default-projects-project-quality-vpcs-subnet-e2e-1f11082b-56qvy-vpc-lbs-default)
160. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/staticroute-eb4f3a68_rxtge/vpc-lbs/default`](#160-policy-api-v1-orgs-default-projects-project-quality-vpcs-staticroute-eb4f3a68-rxtge-vpc-lbs-default)
161. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/test-lb-50fedbb3_mv836/attachments/default`](#161-policy-api-v1-orgs-default-projects-project-quality-vpcs-test-lb-50fedbb3-mv836-attachments-default)
162. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/test-pod-1dd9a577_fu9t5/attachments/default`](#162-policy-api-v1-orgs-default-projects-project-quality-vpcs-test-pod-1dd9a577-fu9t5-attachments-default)
163. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/customized-ns-99beca1e_yleom/vpc-lbs/default`](#163-policy-api-v1-orgs-default-projects-project-quality-vpcs-customized-ns-99beca1e-yleom-vpc-lbs-default)
164. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/target-ns-56446c91_6zdip/attachments/default`](#164-policy-api-v1-orgs-default-projects-project-quality-vpcs-target-ns-56446c91-6zdip-attachments-default)
165. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/test-pod-sync-e8b8a7ca_m404i/vpc-lbs/default`](#165-policy-api-v1-orgs-default-projects-project-quality-vpcs-test-pod-sync-e8b8a7ca-m404i-vpc-lbs-default)
166. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/update-ns-8eb115ed_baxdx/attachments/default`](#166-policy-api-v1-orgs-default-projects-project-quality-vpcs-update-ns-8eb115ed-baxdx-attachments-default)
167. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/subnet-e2e-1f11082b_56qvy/attachments/default`](#167-policy-api-v1-orgs-default-projects-project-quality-vpcs-subnet-e2e-1f11082b-56qvy-attachments-default)
168. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/testvpc-3658f2b5/ip-address-allocations/j7n9u`](#168-policy-api-v1-orgs-default-projects-project-quality-vpcs-testvpc-3658f2b5-ip-address-allocations-j7n9u)
169. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/shared-vpc-ns-0-3bc799ba_nwr40/vpc-lbs/default`](#169-policy-api-v1-orgs-default-projects-project-quality-vpcs-shared-vpc-ns-0-3bc799ba-nwr40-vpc-lbs-default)
170. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/staticroute-eb4f3a68_rxtge/attachments/default`](#170-policy-api-v1-orgs-default-projects-project-quality-vpcs-staticroute-eb4f3a68-rxtge-attachments-default)
171. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/test-netpol-sync-c2cf40cd_65gvf/vpc-lbs/default`](#171-policy-api-v1-orgs-default-projects-project-quality-vpcs-test-netpol-sync-c2cf40cd-65gvf-vpc-lbs-default)
172. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/customized-ns-99beca1e_yleom/attachments/default`](#172-policy-api-v1-orgs-default-projects-project-quality-vpcs-customized-ns-99beca1e-yleom-attachments-default)
173. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/test-ingress-sync-73e76bf1_rbp33/vpc-lbs/default`](#173-policy-api-v1-orgs-default-projects-project-quality-vpcs-test-ingress-sync-73e76bf1-rbp33-vpc-lbs-default)
174. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/test-pod-sync-e8b8a7ca_m404i/attachments/default`](#174-policy-api-v1-orgs-default-projects-project-quality-vpcs-test-pod-sync-e8b8a7ca-m404i-attachments-default)
175. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/test-service-sync-f1d17bff_5230b/vpc-lbs/default`](#175-policy-api-v1-orgs-default-projects-project-quality-vpcs-test-service-sync-f1d17bff-5230b-vpc-lbs-default)
176. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/networkinfo-default-efa7e691_1fkak/vpc-lbs/default`](#176-policy-api-v1-orgs-default-projects-project-quality-vpcs-networkinfo-default-efa7e691-1fkak-vpc-lbs-default)
177. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/shared-vpc-ns-0-3bc799ba_nwr40/attachments/default`](#177-policy-api-v1-orgs-default-projects-project-quality-vpcs-shared-vpc-ns-0-3bc799ba-nwr40-attachments-default)
178. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/test-namespace-sync-49fbe5bd_p9u70/vpc-lbs/default`](#178-policy-api-v1-orgs-default-projects-project-quality-vpcs-test-namespace-sync-49fbe5bd-p9u70-vpc-lbs-default)
179. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/kube-system_fyr99/subnets/vm-default-637336f2_fyr99`](#179-policy-api-v1-orgs-default-projects-project-quality-vpcs-kube-system-fyr99-subnets-vm-default-637336f2-fyr99)
180. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/precreated-target-ns-3c7c1821_v5ml5/vpc-lbs/default`](#180-policy-api-v1-orgs-default-projects-project-quality-vpcs-precreated-target-ns-3c7c1821-v5ml5-vpc-lbs-default)
181. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/subnet-e2e-1f11082b_56qvy/subnets/subnet-cidr_56qvy`](#181-policy-api-v1-orgs-default-projects-project-quality-vpcs-subnet-e2e-1f11082b-56qvy-subnets-subnet-cidr-56qvy)
182. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/subnet-e2e-1f11082b_56qvy/subnets/subnet-dhcp_56qvy`](#182-policy-api-v1-orgs-default-projects-project-quality-vpcs-subnet-e2e-1f11082b-56qvy-subnets-subnet-dhcp-56qvy)
183. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/test-create-vm-basic-f449d9bf_3ehn6/vpc-lbs/default`](#183-policy-api-v1-orgs-default-projects-project-quality-vpcs-test-create-vm-basic-f449d9bf-3ehn6-vpc-lbs-default)
184. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/test-lb-50fedbb3_mv836/ip-address-allocations/39r0c`](#184-policy-api-v1-orgs-default-projects-project-quality-vpcs-test-lb-50fedbb3-mv836-ip-address-allocations-39r0c)
185. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/test-lb-50fedbb3_mv836/ip-address-allocations/cnml1`](#185-policy-api-v1-orgs-default-projects-project-quality-vpcs-test-lb-50fedbb3-mv836-ip-address-allocations-cnml1)
186. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/test-lb-50fedbb3_mv836/ip-address-allocations/i3q14`](#186-policy-api-v1-orgs-default-projects-project-quality-vpcs-test-lb-50fedbb3-mv836-ip-address-allocations-i3q14)
187. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/test-lb-50fedbb3_mv836/ip-address-allocations/o2zx3`](#187-policy-api-v1-orgs-default-projects-project-quality-vpcs-test-lb-50fedbb3-mv836-ip-address-allocations-o2zx3)
188. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/test-netpol-sync-c2cf40cd_65gvf/attachments/default`](#188-policy-api-v1-orgs-default-projects-project-quality-vpcs-test-netpol-sync-c2cf40cd-65gvf-attachments-default)
189. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/testvpc-3658f2b5/subnets/pod-default-ec7c1039_d5d7u`](#189-policy-api-v1-orgs-default-projects-project-quality-vpcs-testvpc-3658f2b5-subnets-pod-default-ec7c1039-d5d7u)
190. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/testvpc-7ab2d8aa/subnets/pod-default-e0268dd8_5583h`](#190-policy-api-v1-orgs-default-projects-project-quality-vpcs-testvpc-7ab2d8aa-subnets-pod-default-e0268dd8-5583h)
191. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/precreated-subnet-ns1-a72a2a9d_8m6zu/vpc-lbs/default`](#191-policy-api-v1-orgs-default-projects-project-quality-vpcs-precreated-subnet-ns1-a72a2a9d-8m6zu-vpc-lbs-default)
192. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/precreated-subnet-ns2-42ff4c1a_tpi2w/vpc-lbs/default`](#192-policy-api-v1-orgs-default-projects-project-quality-vpcs-precreated-subnet-ns2-42ff4c1a-tpi2w-vpc-lbs-default)
193. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/subnet-e2e-1f11082b_56qvy/subnets/subnet-no-ip_56qvy`](#193-policy-api-v1-orgs-default-projects-project-quality-vpcs-subnet-e2e-1f11082b-56qvy-subnets-subnet-no-ip-56qvy)
194. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/test-ingress-sync-73e76bf1_rbp33/attachments/default`](#194-policy-api-v1-orgs-default-projects-project-quality-vpcs-test-ingress-sync-73e76bf1-rbp33-attachments-default)
195. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/test-service-sync-f1d17bff_5230b/attachments/default`](#195-policy-api-v1-orgs-default-projects-project-quality-vpcs-test-service-sync-f1d17bff-5230b-attachments-default)
196. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/web-da775e6f_6o7ts/subnets/pod-default-a734dd59_6o7ts`](#196-policy-api-v1-orgs-default-projects-project-quality-vpcs-web-da775e6f-6o7ts-subnets-pod-default-a734dd59-6o7ts)
197. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/networkinfo-default-efa7e691_1fkak/attachments/default`](#197-policy-api-v1-orgs-default-projects-project-quality-vpcs-networkinfo-default-efa7e691-1fkak-attachments-default)
198. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/test-namespace-sync-49fbe5bd_p9u70/attachments/default`](#198-policy-api-v1-orgs-default-projects-project-quality-vpcs-test-namespace-sync-49fbe5bd-p9u70-attachments-default)
199. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/precreated-target-ns-3c7c1821_v5ml5/attachments/default`](#199-policy-api-v1-orgs-default-projects-project-quality-vpcs-precreated-target-ns-3c7c1821-v5ml5-attachments-default)
200. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/test-create-vm-basic-f449d9bf_3ehn6/attachments/default`](#200-policy-api-v1-orgs-default-projects-project-quality-vpcs-test-create-vm-basic-f449d9bf-3ehn6-attachments-default)
201. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/test-security-policy-web-a2b779b4_f6e79/vpc-lbs/default`](#201-policy-api-v1-orgs-default-projects-project-quality-vpcs-test-security-policy-web-a2b779b4-f6e79-vpc-lbs-default)
202. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/client-91c3f484_qzuxu/subnets/pod-default-075e5037_qzuxu`](#202-policy-api-v1-orgs-default-projects-project-quality-vpcs-client-91c3f484-qzuxu-subnets-pod-default-075e5037-qzuxu)
203. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/precreated-subnet-ns1-a72a2a9d_8m6zu/attachments/default`](#203-policy-api-v1-orgs-default-projects-project-quality-vpcs-precreated-subnet-ns1-a72a2a9d-8m6zu-attachments-default)
204. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/precreated-subnet-ns2-42ff4c1a_tpi2w/attachments/default`](#204-policy-api-v1-orgs-default-projects-project-quality-vpcs-precreated-subnet-ns2-42ff4c1a-tpi2w-attachments-default)
205. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/subnet-e2e-1f11082b_56qvy/subnets/subnet-dhcp-cidr_56qvy`](#205-policy-api-v1-orgs-default-projects-project-quality-vpcs-subnet-e2e-1f11082b-56qvy-subnets-subnet-dhcp-cidr-56qvy)
206. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/subnet-e2e-1f11082b_56qvy/subnets/subnet-only-dhcp_56qvy`](#206-policy-api-v1-orgs-default-projects-project-quality-vpcs-subnet-e2e-1f11082b-56qvy-subnets-subnet-only-dhcp-56qvy)
207. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/test-ipaddress-allocation-40d5699d_2p2tu/vpc-lbs/default`](#207-policy-api-v1-orgs-default-projects-project-quality-vpcs-test-ipaddress-allocation-40d5699d-2p2tu-vpc-lbs-default)
208. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/test-lb-50fedbb3_mv836/subnets/pod-default-3cc5e9c8_mv836`](#208-policy-api-v1-orgs-default-projects-project-quality-vpcs-test-lb-50fedbb3-mv836-subnets-pod-default-3cc5e9c8-mv836)
209. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/test-security-policy-basic-72ecfa65_ib6li/vpc-lbs/default`](#209-policy-api-v1-orgs-default-projects-project-quality-vpcs-test-security-policy-basic-72ecfa65-ib6li-vpc-lbs-default)
210. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/target-ns-56446c91_6zdip/subnets/vm-default-eb532fd0_c6gls`](#210-policy-api-v1-orgs-default-projects-project-quality-vpcs-target-ns-56446c91-6zdip-subnets-vm-default-eb532fd0-c6gls)
211. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/test-lb-50fedbb3_mv836/vpc-lb-pools/tea-svc_80_mv836_scsoh`](#211-policy-api-v1-orgs-default-projects-project-quality-vpcs-test-lb-50fedbb3-mv836-vpc-lb-pools-tea-svc-80-mv836-scsoh)
212. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/test-lb-50fedbb3_mv836/vpc-lb-pools/tea-svc_80_mv836_xirvk`](#212-policy-api-v1-orgs-default-projects-project-quality-vpcs-test-lb-50fedbb3-mv836-vpc-lb-pools-tea-svc-80-mv836-xirvk)
213. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/test-pod-1dd9a577_fu9t5/subnets/pod-default-5cf92338_fu9t5`](#213-policy-api-v1-orgs-default-projects-project-quality-vpcs-test-pod-1dd9a577-fu9t5-subnets-pod-default-5cf92338-fu9t5)
214. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/test-security-policy-client-3a06d660_qiyvu/vpc-lbs/default`](#214-policy-api-v1-orgs-default-projects-project-quality-vpcs-test-security-policy-client-3a06d660-qiyvu-vpc-lbs-default)
215. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/subnet-e2e-1f11082b_56qvy/subnets/subnet-only-no-dhcp_56qvy`](#215-policy-api-v1-orgs-default-projects-project-quality-vpcs-subnet-e2e-1f11082b-56qvy-subnets-subnet-only-no-dhcp-56qvy)
216. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/test-security-policy-web-a2b779b4_f6e79/attachments/default`](#216-policy-api-v1-orgs-default-projects-project-quality-vpcs-test-security-policy-web-a2b779b4-f6e79-attachments-default)
217. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/subnet-e2e-1f11082b_56qvy/subnets/pod-default-6a81803a_56qvy`](#217-policy-api-v1-orgs-default-projects-project-quality-vpcs-subnet-e2e-1f11082b-56qvy-subnets-pod-default-6a81803a-56qvy)
218. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/subnet-e2e-1f11082b_56qvy/subnets/subnet-dhcp-modify-1_56qvy`](#218-policy-api-v1-orgs-default-projects-project-quality-vpcs-subnet-e2e-1f11082b-56qvy-subnets-subnet-dhcp-modify-1-56qvy)
219. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/test-ipaddress-allocation-40d5699d_2p2tu/attachments/default`](#219-policy-api-v1-orgs-default-projects-project-quality-vpcs-test-ipaddress-allocation-40d5699d-2p2tu-attachments-default)
220. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/test-ingress-sync-73e76bf1_rbp33/ip-address-allocations/9ca2y`](#220-policy-api-v1-orgs-default-projects-project-quality-vpcs-test-ingress-sync-73e76bf1-rbp33-ip-address-allocations-9ca2y)
221. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/test-lb-50fedbb3_mv836/ip-address-allocations/coffee-ip_mv836`](#221-policy-api-v1-orgs-default-projects-project-quality-vpcs-test-lb-50fedbb3-mv836-ip-address-allocations-coffee-ip-mv836)
222. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/test-lb-50fedbb3_mv836/vpc-lb-pools/coffee-svc_80_mv836_eyftl`](#222-policy-api-v1-orgs-default-projects-project-quality-vpcs-test-lb-50fedbb3-mv836-vpc-lb-pools-coffee-svc-80-mv836-eyftl)
223. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/test-security-policy-basic-72ecfa65_ib6li/attachments/default`](#223-policy-api-v1-orgs-default-projects-project-quality-vpcs-test-security-policy-basic-72ecfa65-ib6li-attachments-default)
224. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/test-lb-50fedbb3_mv836/vpc-lb-pools/default-svc_80_mv836_iszzt`](#224-policy-api-v1-orgs-default-projects-project-quality-vpcs-test-lb-50fedbb3-mv836-vpc-lb-pools-default-svc-80-mv836-iszzt)
225. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/test-lb-50fedbb3_mv836/vpc-lb-pools/default-svc_80_mv836_rmigv`](#225-policy-api-v1-orgs-default-projects-project-quality-vpcs-test-lb-50fedbb3-mv836-vpc-lb-pools-default-svc-80-mv836-rmigv)
226. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/test-security-policy-add-delete-0e034260_aruoj/vpc-lbs/default`](#226-policy-api-v1-orgs-default-projects-project-quality-vpcs-test-security-policy-add-delete-0e034260-aruoj-vpc-lbs-default)
227. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/test-security-policy-client-3a06d660_qiyvu/attachments/default`](#227-policy-api-v1-orgs-default-projects-project-quality-vpcs-test-security-policy-client-3a06d660-qiyvu-attachments-default)
228. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/test-create-vm-basic-f449d9bf_3ehn6/subnets/public-subnet_3ehn6`](#228-policy-api-v1-orgs-default-projects-project-quality-vpcs-test-create-vm-basic-f449d9bf-3ehn6-subnets-public-subnet-3ehn6)
229. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/test-pod-sync-e8b8a7ca_m404i/subnets/pod-default-0dd88421_m404i`](#229-policy-api-v1-orgs-default-projects-project-quality-vpcs-test-pod-sync-e8b8a7ca-m404i-subnets-pod-default-0dd88421-m404i)
230. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/precreated-subnet-ns1-a72a2a9d_8m6zu/subnets/normal-subnet_8m6zu`](#230-policy-api-v1-orgs-default-projects-project-quality-vpcs-precreated-subnet-ns1-a72a2a9d-8m6zu-subnets-normal-subnet-8m6zu)
231. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/test-lb-50fedbb3_mv836/vpc-lb-virtual-servers/tea-svc_80_TCP_39r0c`](#231-policy-api-v1-orgs-default-projects-project-quality-vpcs-test-lb-50fedbb3-mv836-vpc-lb-virtual-servers-tea-svc-80-tcp-39r0c)
232. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/test-lb-50fedbb3_mv836/vpc-lb-virtual-servers/tea-svc_80_UDP_39r0c`](#232-policy-api-v1-orgs-default-projects-project-quality-vpcs-test-lb-50fedbb3-mv836-vpc-lb-virtual-servers-tea-svc-80-udp-39r0c)
233. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/test-security-policy-add-delete-0e034260_aruoj/attachments/default`](#233-policy-api-v1-orgs-default-projects-project-quality-vpcs-test-security-policy-add-delete-0e034260-aruoj-attachments-default)
234. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/testvpc-3658f2b5/vpc-lb-pools/prevpc-loadbalancer_8080_d5d7u_icdrq`](#234-policy-api-v1-orgs-default-projects-project-quality-vpcs-testvpc-3658f2b5-vpc-lb-pools-prevpc-loadbalancer-8080-d5d7u-icdrq)
235. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/subnet-e2e-1f11082b_56qvy/subnets/user-subnetset-dhcp-c85186d8_56qvy`](#235-policy-api-v1-orgs-default-projects-project-quality-vpcs-subnet-e2e-1f11082b-56qvy-subnets-user-subnetset-dhcp-c85186d8-56qvy)
236. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/test-security-policy-match-expression-ff1dafa9_bgm74/vpc-lbs/default`](#236-policy-api-v1-orgs-default-projects-project-quality-vpcs-test-security-policy-match-expression-ff1dafa9-bgm74-vpc-lbs-default)
237. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/precreated-target-ns-3c7c1821_v5ml5/subnets/shared-subnet-892e2_v5ml5`](#237-policy-api-v1-orgs-default-projects-project-quality-vpcs-precreated-target-ns-3c7c1821-v5ml5-subnets-shared-subnet-892e2-v5ml5)
238. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/test-ipaddress-allocation-40d5699d_2p2tu/ip-address-allocations/p5j45`](#238-policy-api-v1-orgs-default-projects-project-quality-vpcs-test-ipaddress-allocation-40d5699d-2p2tu-ip-address-allocations-p5j45)
239. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/test-lb-50fedbb3_mv836/vpc-lb-virtual-servers/coffee-svc_80_TCP_cnml1`](#239-policy-api-v1-orgs-default-projects-project-quality-vpcs-test-lb-50fedbb3-mv836-vpc-lb-virtual-servers-coffee-svc-80-tcp-cnml1)
240. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/web-da775e6f_6o7ts/security-policies/named-port-policy-with-pod_d3qx0`](#240-policy-api-v1-orgs-default-projects-project-quality-vpcs-web-da775e6f-6o7ts-security-policies-named-port-policy-with-pod-d3qx0)
241. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/subnet-e2e-1f11082b_56qvy/subnets/user-subnetset-static-948a4c45_56qvy`](#241-policy-api-v1-orgs-default-projects-project-quality-vpcs-subnet-e2e-1f11082b-56qvy-subnets-user-subnetset-static-948a4c45-56qvy)
242. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/test-lb-50fedbb3_mv836/vpc-lb-virtual-servers/default-svc_80_TCP_i3q14`](#242-policy-api-v1-orgs-default-projects-project-quality-vpcs-test-lb-50fedbb3-mv836-vpc-lb-virtual-servers-default-svc-80-tcp-i3q14)
243. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/test-lb-50fedbb3_mv836/vpc-lb-virtual-servers/default-svc_80_UDP_i3q14`](#243-policy-api-v1-orgs-default-projects-project-quality-vpcs-test-lb-50fedbb3-mv836-vpc-lb-virtual-servers-default-svc-80-udp-i3q14)
244. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/precreated-target-ns-3c7c1821_v5ml5/subnets/shared-subnet-2-421d2_v5ml5`](#244-policy-api-v1-orgs-default-projects-project-quality-vpcs-precreated-target-ns-3c7c1821-v5ml5-subnets-shared-subnet-2-421d2-v5ml5)
245. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/test-security-policy-match-expression-ff1dafa9_bgm74/attachments/default`](#245-policy-api-v1-orgs-default-projects-project-quality-vpcs-test-security-policy-match-expression-ff1dafa9-bgm74-attachments-default)
246. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/staticroute-eb4f3a68_rxtge/static-routes/guestcluster-staticroute-2_rxtge`](#246-policy-api-v1-orgs-default-projects-project-quality-vpcs-staticroute-eb4f3a68-rxtge-static-routes-guestcluster-staticroute-2-rxtge)
247. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/test-lb-50fedbb3_mv836/vpc-lb-virtual-servers/test-lb-50fedbb3_mv836_http`](#247-policy-api-v1-orgs-default-projects-project-quality-vpcs-test-lb-50fedbb3-mv836-vpc-lb-virtual-servers-test-lb-50fedbb3-mv836-http)
248. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/testvpc-3658f2b5/vpc-lb-virtual-servers/prevpc-loadbalancer_8080_TCP_j7n9u`](#248-policy-api-v1-orgs-default-projects-project-quality-vpcs-testvpc-3658f2b5-vpc-lb-virtual-servers-prevpc-loadbalancer-8080-tcp-j7n9u)
249. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/staticroute-eb4f3a68_rxtge/ip-address-allocations/staticroute-ipalloc_rxtge`](#249-policy-api-v1-orgs-default-projects-project-quality-vpcs-staticroute-eb4f3a68-rxtge-ip-address-allocations-staticroute-ipalloc-rxtge)
250. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/test-ipaddress-allocation-40d5699d_2p2tu/vpc-lb-pools/tea-svc_80_2p2tu_cusgz`](#250-policy-api-v1-orgs-default-projects-project-quality-vpcs-test-ipaddress-allocation-40d5699d-2p2tu-vpc-lb-pools-tea-svc-80-2p2tu-cusgz)
251. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/test-security-policy-basic-72ecfa65_ib6li/subnets/pod-default-db03dc29_ib6li`](#251-policy-api-v1-orgs-default-projects-project-quality-vpcs-test-security-policy-basic-72ecfa65-ib6li-subnets-pod-default-db03dc29-ib6li)
252. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/test-ipaddress-allocation-40d5699d_2p2tu/ip-address-allocations/ipalloc-vip_2p2tu`](#252-policy-api-v1-orgs-default-projects-project-quality-vpcs-test-ipaddress-allocation-40d5699d-2p2tu-ip-address-allocations-ipalloc-vip-2p2tu)
253. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/test-ingress-sync-73e76bf1_rbp33/vpc-lb-pools/test-service-da1e3736_80_rbp33_xmlel`](#253-policy-api-v1-orgs-default-projects-project-quality-vpcs-test-ingress-sync-73e76bf1-rbp33-vpc-lb-pools-test-service-da1e3736-80-rbp33-xmlel)
254. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/test-security-policy-basic-72ecfa65_ib6li/security-policies/isolate-policy-1_f3sgl`](#254-policy-api-v1-orgs-default-projects-project-quality-vpcs-test-security-policy-basic-72ecfa65-ib6li-security-policies-isolate-policy-1-f3sgl)
255. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/test-ipaddress-allocation-40d5699d_2p2tu/vpc-lb-virtual-servers/tea-svc_80_TCP_p5j45`](#255-policy-api-v1-orgs-default-projects-project-quality-vpcs-test-ipaddress-allocation-40d5699d-2p2tu-vpc-lb-virtual-servers-tea-svc-80-tcp-p5j45)
256. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/test-lb-50fedbb3_mv836/vpc-lb-virtual-servers/test-lb-50fedbb3_mv836_https_terminated`](#256-policy-api-v1-orgs-default-projects-project-quality-vpcs-test-lb-50fedbb3-mv836-vpc-lb-virtual-servers-test-lb-50fedbb3-mv836-https-terminated)
257. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/test-security-policy-add-delete-0e034260_aruoj/security-policies/isolate-policy-1_6nt7g`](#257-policy-api-v1-orgs-default-projects-project-quality-vpcs-test-security-policy-add-delete-0e034260-aruoj-security-policies-isolate-policy-1-6nt7g)
258. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/test-security-policy-match-expression-ff1dafa9_bgm74/subnets/pod-default-1289f64d_bgm74`](#258-policy-api-v1-orgs-default-projects-project-quality-vpcs-test-security-policy-match-expression-ff1dafa9-bgm74-subnets-pod-default-1289f64d-bgm74)
259. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/test-netpol-sync-c2cf40cd_65gvf/security-policies/test-network-policy-b6db586a-allow_qgq7e`](#259-policy-api-v1-orgs-default-projects-project-quality-vpcs-test-netpol-sync-c2cf40cd-65gvf-security-policies-test-network-policy-b6db586a-allow-qgq7e)
260. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/test-ipaddress-allocation-40d5699d_2p2tu/ip-address-allocations/guestcluster-workers-a_2p2tu`](#260-policy-api-v1-orgs-default-projects-project-quality-vpcs-test-ipaddress-allocation-40d5699d-2p2tu-ip-address-allocations-guestcluster-workers-a-2p2tu)
261. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/test-ipaddress-allocation-40d5699d_2p2tu/ip-address-allocations/guestcluster-workers-b_2p2tu`](#261-policy-api-v1-orgs-default-projects-project-quality-vpcs-test-ipaddress-allocation-40d5699d-2p2tu-ip-address-allocations-guestcluster-workers-b-2p2tu)
262. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/test-ipaddress-allocation-40d5699d_2p2tu/ip-address-allocations/guestcluster-workers-c_2p2tu`](#262-policy-api-v1-orgs-default-projects-project-quality-vpcs-test-ipaddress-allocation-40d5699d-2p2tu-ip-address-allocations-guestcluster-workers-c-2p2tu)
263. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/test-ingress-sync-73e76bf1_rbp33/vpc-lb-virtual-servers/test-ingress-sync-73e76bf1_rbp33_http`](#263-policy-api-v1-orgs-default-projects-project-quality-vpcs-test-ingress-sync-73e76bf1-rbp33-vpc-lb-virtual-servers-test-ingress-sync-73e76bf1-rbp33-http)
264. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/test-security-policy-web-a2b779b4_f6e79/security-policies/named-port-policy-without-pod_ncmij`](#264-policy-api-v1-orgs-default-projects-project-quality-vpcs-test-security-policy-web-a2b779b4-f6e79-security-policies-named-port-policy-without-pod-ncmij)
265. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/test-netpol-sync-c2cf40cd_65gvf/security-policies/test-network-policy-b6db586a-isolation_qgq7e`](#265-policy-api-v1-orgs-default-projects-project-quality-vpcs-test-netpol-sync-c2cf40cd-65gvf-security-policies-test-network-policy-b6db586a-isolation-qgq7e)
266. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/test-security-policy-match-expression-ff1dafa9_bgm74/security-policies/expression-policy-1_jo4yz`](#266-policy-api-v1-orgs-default-projects-project-quality-vpcs-test-security-policy-match-expression-ff1dafa9-bgm74-security-policies-expression-policy-1-jo4yz)
267. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/test-ingress-sync-73e76bf1_rbp33/vpc-lb-virtual-servers/test-ingress-sync-73e76bf1_rbp33_https_terminated`](#267-policy-api-v1-orgs-default-projects-project-quality-vpcs-test-ingress-sync-73e76bf1-rbp33-vpc-lb-virtual-servers-test-ingress-sync-73e76bf1-rbp33-https-terminated)

#### Level 12 (56 endpoints)

268. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/testvpc-3658f2b5/nat/DEFAULT/nat-rules`](#268-policy-api-v1-orgs-default-projects-project-quality-vpcs-testvpc-3658f2b5-nat-default-nat-rules)
269. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/testvpc-7ab2d8aa/nat/DEFAULT/nat-rules`](#269-policy-api-v1-orgs-default-projects-project-quality-vpcs-testvpc-7ab2d8aa-nat-default-nat-rules)
270. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/kube-system_fyr99/nat/DEFAULT/nat-rules`](#270-policy-api-v1-orgs-default-projects-project-quality-vpcs-kube-system-fyr99-nat-default-nat-rules)
271. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/web-da775e6f_6o7ts/nat/DEFAULT/nat-rules`](#271-policy-api-v1-orgs-default-projects-project-quality-vpcs-web-da775e6f-6o7ts-nat-default-nat-rules)
272. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/client-91c3f484_qzuxu/nat/DEFAULT/nat-rules`](#272-policy-api-v1-orgs-default-projects-project-quality-vpcs-client-91c3f484-qzuxu-nat-default-nat-rules)
273. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/test-lb-50fedbb3_mv836/nat/DEFAULT/nat-rules`](#273-policy-api-v1-orgs-default-projects-project-quality-vpcs-test-lb-50fedbb3-mv836-nat-default-nat-rules)
274. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/test-pod-1dd9a577_fu9t5/nat/DEFAULT/nat-rules`](#274-policy-api-v1-orgs-default-projects-project-quality-vpcs-test-pod-1dd9a577-fu9t5-nat-default-nat-rules)
275. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/target-ns-56446c91_6zdip/nat/DEFAULT/nat-rules`](#275-policy-api-v1-orgs-default-projects-project-quality-vpcs-target-ns-56446c91-6zdip-nat-default-nat-rules)
276. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/update-ns-8eb115ed_baxdx/nat/DEFAULT/nat-rules`](#276-policy-api-v1-orgs-default-projects-project-quality-vpcs-update-ns-8eb115ed-baxdx-nat-default-nat-rules)
277. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/subnet-e2e-1f11082b_56qvy/nat/DEFAULT/nat-rules`](#277-policy-api-v1-orgs-default-projects-project-quality-vpcs-subnet-e2e-1f11082b-56qvy-nat-default-nat-rules)
278. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/staticroute-eb4f3a68_rxtge/nat/DEFAULT/nat-rules`](#278-policy-api-v1-orgs-default-projects-project-quality-vpcs-staticroute-eb4f3a68-rxtge-nat-default-nat-rules)
279. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/customized-ns-99beca1e_yleom/nat/DEFAULT/nat-rules`](#279-policy-api-v1-orgs-default-projects-project-quality-vpcs-customized-ns-99beca1e-yleom-nat-default-nat-rules)
280. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/test-pod-sync-e8b8a7ca_m404i/nat/DEFAULT/nat-rules`](#280-policy-api-v1-orgs-default-projects-project-quality-vpcs-test-pod-sync-e8b8a7ca-m404i-nat-default-nat-rules)
281. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/shared-vpc-ns-0-3bc799ba_nwr40/nat/DEFAULT/nat-rules`](#281-policy-api-v1-orgs-default-projects-project-quality-vpcs-shared-vpc-ns-0-3bc799ba-nwr40-nat-default-nat-rules)
282. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/test-netpol-sync-c2cf40cd_65gvf/nat/DEFAULT/nat-rules`](#282-policy-api-v1-orgs-default-projects-project-quality-vpcs-test-netpol-sync-c2cf40cd-65gvf-nat-default-nat-rules)
283. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/test-ingress-sync-73e76bf1_rbp33/nat/DEFAULT/nat-rules`](#283-policy-api-v1-orgs-default-projects-project-quality-vpcs-test-ingress-sync-73e76bf1-rbp33-nat-default-nat-rules)
284. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/test-service-sync-f1d17bff_5230b/nat/DEFAULT/nat-rules`](#284-policy-api-v1-orgs-default-projects-project-quality-vpcs-test-service-sync-f1d17bff-5230b-nat-default-nat-rules)
285. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/networkinfo-default-efa7e691_1fkak/nat/DEFAULT/nat-rules`](#285-policy-api-v1-orgs-default-projects-project-quality-vpcs-networkinfo-default-efa7e691-1fkak-nat-default-nat-rules)
286. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/test-namespace-sync-49fbe5bd_p9u70/nat/DEFAULT/nat-rules`](#286-policy-api-v1-orgs-default-projects-project-quality-vpcs-test-namespace-sync-49fbe5bd-p9u70-nat-default-nat-rules)
287. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/precreated-target-ns-3c7c1821_v5ml5/nat/DEFAULT/nat-rules`](#287-policy-api-v1-orgs-default-projects-project-quality-vpcs-precreated-target-ns-3c7c1821-v5ml5-nat-default-nat-rules)
288. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/test-create-vm-basic-f449d9bf_3ehn6/nat/DEFAULT/nat-rules`](#288-policy-api-v1-orgs-default-projects-project-quality-vpcs-test-create-vm-basic-f449d9bf-3ehn6-nat-default-nat-rules)
289. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/kube-system_fyr99/subnets/vm-default-637336f2_fyr99/status`](#289-policy-api-v1-orgs-default-projects-project-quality-vpcs-kube-system-fyr99-subnets-vm-default-637336f2-fyr99-status)
290. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/precreated-subnet-ns1-a72a2a9d_8m6zu/nat/DEFAULT/nat-rules`](#290-policy-api-v1-orgs-default-projects-project-quality-vpcs-precreated-subnet-ns1-a72a2a9d-8m6zu-nat-default-nat-rules)
291. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/precreated-subnet-ns2-42ff4c1a_tpi2w/nat/DEFAULT/nat-rules`](#291-policy-api-v1-orgs-default-projects-project-quality-vpcs-precreated-subnet-ns2-42ff4c1a-tpi2w-nat-default-nat-rules)
292. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/subnet-e2e-1f11082b_56qvy/subnets/subnet-cidr_56qvy/status`](#292-policy-api-v1-orgs-default-projects-project-quality-vpcs-subnet-e2e-1f11082b-56qvy-subnets-subnet-cidr-56qvy-status)
293. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/subnet-e2e-1f11082b_56qvy/subnets/subnet-dhcp_56qvy/status`](#293-policy-api-v1-orgs-default-projects-project-quality-vpcs-subnet-e2e-1f11082b-56qvy-subnets-subnet-dhcp-56qvy-status)
294. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/testvpc-3658f2b5/subnets/pod-default-ec7c1039_d5d7u/status`](#294-policy-api-v1-orgs-default-projects-project-quality-vpcs-testvpc-3658f2b5-subnets-pod-default-ec7c1039-d5d7u-status)
295. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/testvpc-7ab2d8aa/subnets/pod-default-e0268dd8_5583h/status`](#295-policy-api-v1-orgs-default-projects-project-quality-vpcs-testvpc-7ab2d8aa-subnets-pod-default-e0268dd8-5583h-status)
296. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/subnet-e2e-1f11082b_56qvy/subnets/subnet-no-ip_56qvy/status`](#296-policy-api-v1-orgs-default-projects-project-quality-vpcs-subnet-e2e-1f11082b-56qvy-subnets-subnet-no-ip-56qvy-status)
297. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/web-da775e6f_6o7ts/subnets/pod-default-a734dd59_6o7ts/status`](#297-policy-api-v1-orgs-default-projects-project-quality-vpcs-web-da775e6f-6o7ts-subnets-pod-default-a734dd59-6o7ts-status)
298. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/test-security-policy-web-a2b779b4_f6e79/nat/DEFAULT/nat-rules`](#298-policy-api-v1-orgs-default-projects-project-quality-vpcs-test-security-policy-web-a2b779b4-f6e79-nat-default-nat-rules)
299. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/test-ipaddress-allocation-40d5699d_2p2tu/nat/DEFAULT/nat-rules`](#299-policy-api-v1-orgs-default-projects-project-quality-vpcs-test-ipaddress-allocation-40d5699d-2p2tu-nat-default-nat-rules)
300. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/client-91c3f484_qzuxu/subnets/pod-default-075e5037_qzuxu/status`](#300-policy-api-v1-orgs-default-projects-project-quality-vpcs-client-91c3f484-qzuxu-subnets-pod-default-075e5037-qzuxu-status)
301. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/subnet-e2e-1f11082b_56qvy/subnets/subnet-dhcp-cidr_56qvy/status`](#301-policy-api-v1-orgs-default-projects-project-quality-vpcs-subnet-e2e-1f11082b-56qvy-subnets-subnet-dhcp-cidr-56qvy-status)
302. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/subnet-e2e-1f11082b_56qvy/subnets/subnet-only-dhcp_56qvy/status`](#302-policy-api-v1-orgs-default-projects-project-quality-vpcs-subnet-e2e-1f11082b-56qvy-subnets-subnet-only-dhcp-56qvy-status)
303. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/test-security-policy-basic-72ecfa65_ib6li/nat/DEFAULT/nat-rules`](#303-policy-api-v1-orgs-default-projects-project-quality-vpcs-test-security-policy-basic-72ecfa65-ib6li-nat-default-nat-rules)
304. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/test-lb-50fedbb3_mv836/subnets/pod-default-3cc5e9c8_mv836/status`](#304-policy-api-v1-orgs-default-projects-project-quality-vpcs-test-lb-50fedbb3-mv836-subnets-pod-default-3cc5e9c8-mv836-status)
305. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/test-security-policy-client-3a06d660_qiyvu/nat/DEFAULT/nat-rules`](#305-policy-api-v1-orgs-default-projects-project-quality-vpcs-test-security-policy-client-3a06d660-qiyvu-nat-default-nat-rules)
306. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/target-ns-56446c91_6zdip/subnets/vm-default-eb532fd0_c6gls/status`](#306-policy-api-v1-orgs-default-projects-project-quality-vpcs-target-ns-56446c91-6zdip-subnets-vm-default-eb532fd0-c6gls-status)
307. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/test-pod-1dd9a577_fu9t5/subnets/pod-default-5cf92338_fu9t5/status`](#307-policy-api-v1-orgs-default-projects-project-quality-vpcs-test-pod-1dd9a577-fu9t5-subnets-pod-default-5cf92338-fu9t5-status)
308. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/vmware-system-supervisor-services-vpc_kzc7e/nat/DEFAULT/nat-rules`](#308-policy-api-v1-orgs-default-projects-project-quality-vpcs-vmware-system-supervisor-services-vpc-kzc7e-nat-default-nat-rules)
309. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/subnet-e2e-1f11082b_56qvy/subnets/subnet-only-no-dhcp_56qvy/status`](#309-policy-api-v1-orgs-default-projects-project-quality-vpcs-subnet-e2e-1f11082b-56qvy-subnets-subnet-only-no-dhcp-56qvy-status)
310. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/subnet-e2e-1f11082b_56qvy/subnets/pod-default-6a81803a_56qvy/status`](#310-policy-api-v1-orgs-default-projects-project-quality-vpcs-subnet-e2e-1f11082b-56qvy-subnets-pod-default-6a81803a-56qvy-status)
311. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/subnet-e2e-1f11082b_56qvy/subnets/subnet-dhcp-modify-1_56qvy/status`](#311-policy-api-v1-orgs-default-projects-project-quality-vpcs-subnet-e2e-1f11082b-56qvy-subnets-subnet-dhcp-modify-1-56qvy-status)
312. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/test-security-policy-add-delete-0e034260_aruoj/nat/DEFAULT/nat-rules`](#312-policy-api-v1-orgs-default-projects-project-quality-vpcs-test-security-policy-add-delete-0e034260-aruoj-nat-default-nat-rules)
313. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/test-create-vm-basic-f449d9bf_3ehn6/subnets/public-subnet_3ehn6/status`](#313-policy-api-v1-orgs-default-projects-project-quality-vpcs-test-create-vm-basic-f449d9bf-3ehn6-subnets-public-subnet-3ehn6-status)
314. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/test-pod-sync-e8b8a7ca_m404i/subnets/pod-default-0dd88421_m404i/status`](#314-policy-api-v1-orgs-default-projects-project-quality-vpcs-test-pod-sync-e8b8a7ca-m404i-subnets-pod-default-0dd88421-m404i-status)
315. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/precreated-subnet-ns1-a72a2a9d_8m6zu/subnets/normal-subnet_8m6zu/status`](#315-policy-api-v1-orgs-default-projects-project-quality-vpcs-precreated-subnet-ns1-a72a2a9d-8m6zu-subnets-normal-subnet-8m6zu-status)
316. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/test-security-policy-match-expression-ff1dafa9_bgm74/nat/DEFAULT/nat-rules`](#316-policy-api-v1-orgs-default-projects-project-quality-vpcs-test-security-policy-match-expression-ff1dafa9-bgm74-nat-default-nat-rules)
317. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/kube-system_fyr99/subnets/vm-default-637336f2_fyr99/dynamic-ip-reservations`](#317-policy-api-v1-orgs-default-projects-project-quality-vpcs-kube-system-fyr99-subnets-vm-default-637336f2-fyr99-dynamic-ip-reservations)
318. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/subnet-e2e-1f11082b_56qvy/subnets/user-subnetset-dhcp-c85186d8_56qvy/status`](#318-policy-api-v1-orgs-default-projects-project-quality-vpcs-subnet-e2e-1f11082b-56qvy-subnets-user-subnetset-dhcp-c85186d8-56qvy-status)
319. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/precreated-target-ns-3c7c1821_v5ml5/subnets/shared-subnet-892e2_v5ml5/status`](#319-policy-api-v1-orgs-default-projects-project-quality-vpcs-precreated-target-ns-3c7c1821-v5ml5-subnets-shared-subnet-892e2-v5ml5-status)
320. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/subnet-e2e-1f11082b_56qvy/subnets/user-subnetset-static-948a4c45_56qvy/status`](#320-policy-api-v1-orgs-default-projects-project-quality-vpcs-subnet-e2e-1f11082b-56qvy-subnets-user-subnetset-static-948a4c45-56qvy-status)
321. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/precreated-target-ns-3c7c1821_v5ml5/subnets/shared-subnet-2-421d2_v5ml5/status`](#321-policy-api-v1-orgs-default-projects-project-quality-vpcs-precreated-target-ns-3c7c1821-v5ml5-subnets-shared-subnet-2-421d2-v5ml5-status)
322. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/test-security-policy-basic-72ecfa65_ib6li/subnets/pod-default-db03dc29_ib6li/status`](#322-policy-api-v1-orgs-default-projects-project-quality-vpcs-test-security-policy-basic-72ecfa65-ib6li-subnets-pod-default-db03dc29-ib6li-status)
323. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/test-security-policy-match-expression-ff1dafa9_bgm74/subnets/pod-default-1289f64d_bgm74/status`](#323-policy-api-v1-orgs-default-projects-project-quality-vpcs-test-security-policy-match-expression-ff1dafa9-bgm74-subnets-pod-default-1289f64d-bgm74-status)

#### Level 13 (55 endpoints)

324. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/test-lb-50fedbb3_mv836/subnets/pod-default-3cc5e9c8_mv836/ports/tea_mv836`](#324-policy-api-v1-orgs-default-projects-project-quality-vpcs-test-lb-50fedbb3-mv836-subnets-pod-default-3cc5e9c8-mv836-ports-tea-mv836)
325. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/client-91c3f484_qzuxu/subnets/pod-default-075e5037_qzuxu/ports/client_qzuxu`](#325-policy-api-v1-orgs-default-projects-project-quality-vpcs-client-91c3f484-qzuxu-subnets-pod-default-075e5037-qzuxu-ports-client-qzuxu)
326. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/subnet-e2e-1f11082b_56qvy/subnets/subnet-dhcp_56qvy/dhcp-server-config/stats`](#326-policy-api-v1-orgs-default-projects-project-quality-vpcs-subnet-e2e-1f11082b-56qvy-subnets-subnet-dhcp-56qvy-dhcp-server-config-stats)
327. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/test-lb-50fedbb3_mv836/subnets/pod-default-3cc5e9c8_mv836/ports/coffee_mv836`](#327-policy-api-v1-orgs-default-projects-project-quality-vpcs-test-lb-50fedbb3-mv836-subnets-pod-default-3cc5e9c8-mv836-ports-coffee-mv836)
328. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/testvpc-7ab2d8aa/subnets/pod-default-e0268dd8_5583h/ports/prevpc-podvm_5583h`](#328-policy-api-v1-orgs-default-projects-project-quality-vpcs-testvpc-7ab2d8aa-subnets-pod-default-e0268dd8-5583h-ports-prevpc-podvm-5583h)
329. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/test-lb-50fedbb3_mv836/subnets/pod-default-3cc5e9c8_mv836/ports/default_mv836`](#329-policy-api-v1-orgs-default-projects-project-quality-vpcs-test-lb-50fedbb3-mv836-subnets-pod-default-3cc5e9c8-mv836-ports-default-mv836)
330. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/subnet-e2e-1f11082b_56qvy/subnets/subnet-cidr_56qvy/ports/port-with-ip-1_56qvy`](#330-policy-api-v1-orgs-default-projects-project-quality-vpcs-subnet-e2e-1f11082b-56qvy-subnets-subnet-cidr-56qvy-ports-port-with-ip-1-56qvy)
331. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/subnet-e2e-1f11082b_56qvy/subnets/subnet-cidr_56qvy/ports/port-with-ip-2_56qvy`](#331-policy-api-v1-orgs-default-projects-project-quality-vpcs-subnet-e2e-1f11082b-56qvy-subnets-subnet-cidr-56qvy-ports-port-with-ip-2-56qvy)
332. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/subnet-e2e-1f11082b_56qvy/subnets/subnet-cidr_56qvy/ports/port-with-ip-3_56qvy`](#332-policy-api-v1-orgs-default-projects-project-quality-vpcs-subnet-e2e-1f11082b-56qvy-subnets-subnet-cidr-56qvy-ports-port-with-ip-3-56qvy)
333. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/subnet-e2e-1f11082b_56qvy/subnets/subnet-cidr_56qvy/ip-pools/static-ipv4-default`](#333-policy-api-v1-orgs-default-projects-project-quality-vpcs-subnet-e2e-1f11082b-56qvy-subnets-subnet-cidr-56qvy-ip-pools-static-ipv4-default)
334. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/testvpc-3658f2b5/subnets/pod-default-ec7c1039_d5d7u/ip-pools/static-ipv4-default`](#334-policy-api-v1-orgs-default-projects-project-quality-vpcs-testvpc-3658f2b5-subnets-pod-default-ec7c1039-d5d7u-ip-pools-static-ipv4-default)
335. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/testvpc-7ab2d8aa/subnets/pod-default-e0268dd8_5583h/ip-pools/static-ipv4-default`](#335-policy-api-v1-orgs-default-projects-project-quality-vpcs-testvpc-7ab2d8aa-subnets-pod-default-e0268dd8-5583h-ip-pools-static-ipv4-default)
336. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/testvpc-3658f2b5/subnets/pod-default-ec7c1039_d5d7u/ports/prevpc-client-pod_d5d7u`](#336-policy-api-v1-orgs-default-projects-project-quality-vpcs-testvpc-3658f2b5-subnets-pod-default-ec7c1039-d5d7u-ports-prevpc-client-pod-d5d7u)
337. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/testvpc-3658f2b5/subnets/pod-default-ec7c1039_d5d7u/ports/prevpc-service-pod_d5d7u`](#337-policy-api-v1-orgs-default-projects-project-quality-vpcs-testvpc-3658f2b5-subnets-pod-default-ec7c1039-d5d7u-ports-prevpc-service-pod-d5d7u)
338. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/web-da775e6f_6o7ts/subnets/pod-default-a734dd59_6o7ts/ip-pools/static-ipv4-default`](#338-policy-api-v1-orgs-default-projects-project-quality-vpcs-web-da775e6f-6o7ts-subnets-pod-default-a734dd59-6o7ts-ip-pools-static-ipv4-default)
339. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/client-91c3f484_qzuxu/subnets/pod-default-075e5037_qzuxu/ip-pools/static-ipv4-default`](#339-policy-api-v1-orgs-default-projects-project-quality-vpcs-client-91c3f484-qzuxu-subnets-pod-default-075e5037-qzuxu-ip-pools-static-ipv4-default)
340. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/subnet-e2e-1f11082b_56qvy/subnets/subnet-no-ip_56qvy/ports/port-in-no-ip-subnet_56qvy`](#340-policy-api-v1-orgs-default-projects-project-quality-vpcs-subnet-e2e-1f11082b-56qvy-subnets-subnet-no-ip-56qvy-ports-port-in-no-ip-subnet-56qvy)
341. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/target-ns-56446c91_6zdip/subnets/vm-default-eb532fd0_c6gls/ports/port-e2e-test-3_c6gls`](#341-policy-api-v1-orgs-default-projects-project-quality-vpcs-target-ns-56446c91-6zdip-subnets-vm-default-eb532fd0-c6gls-ports-port-e2e-test-3-c6gls)
342. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/test-lb-50fedbb3_mv836/subnets/pod-default-3cc5e9c8_mv836/ip-pools/static-ipv4-default`](#342-policy-api-v1-orgs-default-projects-project-quality-vpcs-test-lb-50fedbb3-mv836-subnets-pod-default-3cc5e9c8-mv836-ip-pools-static-ipv4-default)
343. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/target-ns-56446c91_6zdip/subnets/vm-default-eb532fd0_c6gls/ip-pools/static-ipv4-default`](#343-policy-api-v1-orgs-default-projects-project-quality-vpcs-target-ns-56446c91-6zdip-subnets-vm-default-eb532fd0-c6gls-ip-pools-static-ipv4-default)
344. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/test-pod-1dd9a577_fu9t5/subnets/pod-default-5cf92338_fu9t5/ip-pools/static-ipv4-default`](#344-policy-api-v1-orgs-default-projects-project-quality-vpcs-test-pod-1dd9a577-fu9t5-subnets-pod-default-5cf92338-fu9t5-ip-pools-static-ipv4-default)
345. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/subnet-e2e-1f11082b_56qvy/subnets/pod-default-6a81803a_56qvy/ports/port-e2e-test-1_56qvy`](#345-policy-api-v1-orgs-default-projects-project-quality-vpcs-subnet-e2e-1f11082b-56qvy-subnets-pod-default-6a81803a-56qvy-ports-port-e2e-test-1-56qvy)
346. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/subnet-e2e-1f11082b_56qvy/subnets/pod-default-6a81803a_56qvy/ip-pools/static-ipv4-default`](#346-policy-api-v1-orgs-default-projects-project-quality-vpcs-subnet-e2e-1f11082b-56qvy-subnets-pod-default-6a81803a-56qvy-ip-pools-static-ipv4-default)
347. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/test-create-vm-basic-f449d9bf_3ehn6/subnets/public-subnet_3ehn6/ip-pools/static-ipv4-default`](#347-policy-api-v1-orgs-default-projects-project-quality-vpcs-test-create-vm-basic-f449d9bf-3ehn6-subnets-public-subnet-3ehn6-ip-pools-static-ipv4-default)
348. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/test-pod-sync-e8b8a7ca_m404i/subnets/pod-default-0dd88421_m404i/ip-pools/static-ipv4-default`](#348-policy-api-v1-orgs-default-projects-project-quality-vpcs-test-pod-sync-e8b8a7ca-m404i-subnets-pod-default-0dd88421-m404i-ip-pools-static-ipv4-default)
349. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/subnet-e2e-1f11082b_56qvy/subnets/user-subnetset-dhcp-c85186d8_56qvy/dhcp-server-config/stats`](#349-policy-api-v1-orgs-default-projects-project-quality-vpcs-subnet-e2e-1f11082b-56qvy-subnets-user-subnetset-dhcp-c85186d8-56qvy-dhcp-server-config-stats)
350. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/test-pod-sync-e8b8a7ca_m404i/subnets/pod-default-0dd88421_m404i/ports/test-pod-32c0f6bc_m404i`](#350-policy-api-v1-orgs-default-projects-project-quality-vpcs-test-pod-sync-e8b8a7ca-m404i-subnets-pod-default-0dd88421-m404i-ports-test-pod-32c0f6bc-m404i)
351. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/test-pod-1dd9a577_fu9t5/subnets/pod-default-5cf92338_fu9t5/ports/test-source-pod-f9ba0670_fu9t5`](#351-policy-api-v1-orgs-default-projects-project-quality-vpcs-test-pod-1dd9a577-fu9t5-subnets-pod-default-5cf92338-fu9t5-ports-test-source-pod-f9ba0670-fu9t5)
352. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/web-da775e6f_6o7ts/subnets/pod-default-a734dd59_6o7ts/ports/tcp-deployment-56bcbfc896-s7rng_6o7ts`](#352-policy-api-v1-orgs-default-projects-project-quality-vpcs-web-da775e6f-6o7ts-subnets-pod-default-a734dd59-6o7ts-ports-tcp-deployment-56bcbfc896-s7rng-6o7ts)
353. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/web-da775e6f_6o7ts/subnets/pod-default-a734dd59_6o7ts/ports/tcp-deployment-56bcbfc896-xs2hs_6o7ts`](#353-policy-api-v1-orgs-default-projects-project-quality-vpcs-web-da775e6f-6o7ts-subnets-pod-default-a734dd59-6o7ts-ports-tcp-deployment-56bcbfc896-xs2hs-6o7ts)
354. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/subnet-e2e-1f11082b_56qvy/subnets/user-subnetset-static-948a4c45_56qvy/ip-pools/static-ipv4-default`](#354-policy-api-v1-orgs-default-projects-project-quality-vpcs-subnet-e2e-1f11082b-56qvy-subnets-user-subnetset-static-948a4c45-56qvy-ip-pools-static-ipv4-default)
355. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/subnet-e2e-1f11082b_56qvy/subnets/user-subnetset-dhcp-c85186d8_56qvy/ports/port-in-dhcp-subnetset_56qvy`](#355-policy-api-v1-orgs-default-projects-project-quality-vpcs-subnet-e2e-1f11082b-56qvy-subnets-user-subnetset-dhcp-c85186d8-56qvy-ports-port-in-dhcp-subnetset-56qvy)
356. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/test-create-vm-basic-f449d9bf_3ehn6/subnets/public-subnet_3ehn6/ports/public-vm-public-subnet-eth0_3ehn6`](#356-policy-api-v1-orgs-default-projects-project-quality-vpcs-test-create-vm-basic-f449d9bf-3ehn6-subnets-public-subnet-3ehn6-ports-public-vm-public-subnet-eth0-3ehn6)
357. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/test-security-policy-basic-72ecfa65_ib6li/subnets/pod-default-db03dc29_ib6li/ip-pools/static-ipv4-default`](#357-policy-api-v1-orgs-default-projects-project-quality-vpcs-test-security-policy-basic-72ecfa65-ib6li-subnets-pod-default-db03dc29-ib6li-ip-pools-static-ipv4-default)
358. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/test-security-policy-match-expression-ff1dafa9_bgm74/subnets/pod-default-1289f64d_bgm74/ports/pod-a_bgm74`](#358-policy-api-v1-orgs-default-projects-project-quality-vpcs-test-security-policy-match-expression-ff1dafa9-bgm74-subnets-pod-default-1289f64d-bgm74-ports-pod-a-bgm74)
359. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/subnet-e2e-1f11082b_56qvy/subnets/user-subnetset-static-948a4c45_56qvy/ports/port-in-static-subnetset_56qvy`](#359-policy-api-v1-orgs-default-projects-project-quality-vpcs-subnet-e2e-1f11082b-56qvy-subnets-user-subnetset-static-948a4c45-56qvy-ports-port-in-static-subnetset-56qvy)
360. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/test-security-policy-match-expression-ff1dafa9_bgm74/subnets/pod-default-1289f64d_bgm74/ports/client-a_bgm74`](#360-policy-api-v1-orgs-default-projects-project-quality-vpcs-test-security-policy-match-expression-ff1dafa9-bgm74-subnets-pod-default-1289f64d-bgm74-ports-client-a-bgm74)
361. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/test-security-policy-match-expression-ff1dafa9_bgm74/subnets/pod-default-1289f64d_bgm74/ports/client-b_bgm74`](#361-policy-api-v1-orgs-default-projects-project-quality-vpcs-test-security-policy-match-expression-ff1dafa9-bgm74-subnets-pod-default-1289f64d-bgm74-ports-client-b-bgm74)
362. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/subnet-e2e-1f11082b_56qvy/subnets/subnet-dhcp_56qvy/ports/port-in-dhcp-subnet-with-address-bindings-vc-macpool_56qvy`](#362-policy-api-v1-orgs-default-projects-project-quality-vpcs-subnet-e2e-1f11082b-56qvy-subnets-subnet-dhcp-56qvy-ports-port-in-dhcp-subnet-with-address-bindings-vc-macpool-56qvy)
363. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/test-security-policy-match-expression-ff1dafa9_bgm74/subnets/pod-default-1289f64d_bgm74/ip-pools/static-ipv4-default`](#363-policy-api-v1-orgs-default-projects-project-quality-vpcs-test-security-policy-match-expression-ff1dafa9-bgm74-subnets-pod-default-1289f64d-bgm74-ip-pools-static-ipv4-default)
364. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/subnet-e2e-1f11082b_56qvy/subnets/subnet-dhcp_56qvy/ports/port-in-dhcp-subnet-with-address-bindings-nsx-macpool_56qvy`](#364-policy-api-v1-orgs-default-projects-project-quality-vpcs-subnet-e2e-1f11082b-56qvy-subnets-subnet-dhcp-56qvy-ports-port-in-dhcp-subnet-with-address-bindings-nsx-macpool-56qvy)
365. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/test-security-policy-basic-72ecfa65_ib6li/subnets/pod-default-db03dc29_ib6li/ports/server-client-68f86f99bc-2xkkv_ib6li`](#365-policy-api-v1-orgs-default-projects-project-quality-vpcs-test-security-policy-basic-72ecfa65-ib6li-subnets-pod-default-db03dc29-ib6li-ports-server-client-68f86f99bc-2xkkv-ib6li)
366. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/test-security-policy-basic-72ecfa65_ib6li/subnets/pod-default-db03dc29_ib6li/ports/server-client-68f86f99bc-c2xvr_ib6li`](#366-policy-api-v1-orgs-default-projects-project-quality-vpcs-test-security-policy-basic-72ecfa65-ib6li-subnets-pod-default-db03dc29-ib6li-ports-server-client-68f86f99bc-c2xvr-ib6li)
367. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/testvpc-3658f2b5/subnets/pod-default-ec7c1039_d5d7u/ports/vmware-system-image-280f8fa0-3f96-4aaf-bf38-390fbf5915ae_d5d7u`](#367-policy-api-v1-orgs-default-projects-project-quality-vpcs-testvpc-3658f2b5-subnets-pod-default-ec7c1039-d5d7u-ports-vmware-system-image-280f8fa0-3f96-4aaf-bf38-390fbf5915ae-d5d7u)
368. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/testvpc-7ab2d8aa/subnets/pod-default-e0268dd8_5583h/ports/vmware-system-image-1a52a8a8-37d8-4ae2-b433-4a96be950051_5583h`](#368-policy-api-v1-orgs-default-projects-project-quality-vpcs-testvpc-7ab2d8aa-subnets-pod-default-e0268dd8-5583h-ports-vmware-system-image-1a52a8a8-37d8-4ae2-b433-4a96be950051-5583h)
369. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/web-da775e6f_6o7ts/subnets/pod-default-a734dd59_6o7ts/ports/vmware-system-image-67d253b4-2743-45dd-86ca-a5de1909fc68_6o7ts`](#369-policy-api-v1-orgs-default-projects-project-quality-vpcs-web-da775e6f-6o7ts-subnets-pod-default-a734dd59-6o7ts-ports-vmware-system-image-67d253b4-2743-45dd-86ca-a5de1909fc68-6o7ts)
370. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/web-da775e6f_6o7ts/subnets/pod-default-a734dd59_6o7ts/ports/vmware-system-image-b3305f6d-fd0d-4c43-9b16-78dc0b9f7ce2_6o7ts`](#370-policy-api-v1-orgs-default-projects-project-quality-vpcs-web-da775e6f-6o7ts-subnets-pod-default-a734dd59-6o7ts-ports-vmware-system-image-b3305f6d-fd0d-4c43-9b16-78dc0b9f7ce2-6o7ts)
371. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/client-91c3f484_qzuxu/subnets/pod-default-075e5037_qzuxu/ports/vmware-system-image-b16a63d0-2b48-4e25-9222-ed24d7a5c67c_qzuxu`](#371-policy-api-v1-orgs-default-projects-project-quality-vpcs-client-91c3f484-qzuxu-subnets-pod-default-075e5037-qzuxu-ports-vmware-system-image-b16a63d0-2b48-4e25-9222-ed24d7a5c67c-qzuxu)
372. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/test-lb-50fedbb3_mv836/subnets/pod-default-3cc5e9c8_mv836/ports/vmware-system-image-90dc9354-d875-41fe-b545-01332c956b5a_mv836`](#372-policy-api-v1-orgs-default-projects-project-quality-vpcs-test-lb-50fedbb3-mv836-subnets-pod-default-3cc5e9c8-mv836-ports-vmware-system-image-90dc9354-d875-41fe-b545-01332c956b5a-mv836)
373. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/test-pod-1dd9a577_fu9t5/subnets/pod-default-5cf92338_fu9t5/ports/vmware-system-image-cd289a18-4ce4-4dff-a025-39f9d0636310_fu9t5`](#373-policy-api-v1-orgs-default-projects-project-quality-vpcs-test-pod-1dd9a577-fu9t5-subnets-pod-default-5cf92338-fu9t5-ports-vmware-system-image-cd289a18-4ce4-4dff-a025-39f9d0636310-fu9t5)
374. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/test-pod-sync-e8b8a7ca_m404i/subnets/pod-default-0dd88421_m404i/ports/vmware-system-image-38f4d4f7-1fae-4270-9eb3-e8e9f2c5f08a_m404i`](#374-policy-api-v1-orgs-default-projects-project-quality-vpcs-test-pod-sync-e8b8a7ca-m404i-subnets-pod-default-0dd88421-m404i-ports-vmware-system-image-38f4d4f7-1fae-4270-9eb3-e8e9f2c5f08a-m404i)
375. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/test-security-policy-basic-72ecfa65_ib6li/subnets/pod-default-db03dc29_ib6li/ports/vmware-system-image-7f80e1f0-a3f7-4d67-87e3-16162d5cdcc8_ib6li`](#375-policy-api-v1-orgs-default-projects-project-quality-vpcs-test-security-policy-basic-72ecfa65-ib6li-subnets-pod-default-db03dc29-ib6li-ports-vmware-system-image-7f80e1f0-a3f7-4d67-87e3-16162d5cdcc8-ib6li)
376. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/test-security-policy-match-expression-ff1dafa9_bgm74/subnets/pod-default-1289f64d_bgm74/ports/vmware-system-image-78efc28d-50fb-4bf5-8eb3-5ff538be370c_bgm74`](#376-policy-api-v1-orgs-default-projects-project-quality-vpcs-test-security-policy-match-expression-ff1dafa9-bgm74-subnets-pod-default-1289f64d-bgm74-ports-vmware-system-image-78efc28d-50fb-4bf5-8eb3-5ff538be370c-bgm74)
377. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/test-security-policy-match-expression-ff1dafa9_bgm74/subnets/pod-default-1289f64d_bgm74/ports/vmware-system-image-849fb668-f3ab-48bc-846b-38c485bd8f1f_bgm74`](#377-policy-api-v1-orgs-default-projects-project-quality-vpcs-test-security-policy-match-expression-ff1dafa9-bgm74-subnets-pod-default-1289f64d-bgm74-ports-vmware-system-image-849fb668-f3ab-48bc-846b-38c485bd8f1f-bgm74)
378. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/test-security-policy-match-expression-ff1dafa9_bgm74/subnets/pod-default-1289f64d_bgm74/ports/vmware-system-image-92b67ea7-200d-4a00-92d3-c6974f97422f_bgm74`](#378-policy-api-v1-orgs-default-projects-project-quality-vpcs-test-security-policy-match-expression-ff1dafa9-bgm74-subnets-pod-default-1289f64d-bgm74-ports-vmware-system-image-92b67ea7-200d-4a00-92d3-c6974f97422f-bgm74)

#### Level 14 (38 endpoints)

379. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/test-lb-50fedbb3_mv836/subnets/pod-default-3cc5e9c8_mv836/ports/tea_mv836/state`](#379-policy-api-v1-orgs-default-projects-project-quality-vpcs-test-lb-50fedbb3-mv836-subnets-pod-default-3cc5e9c8-mv836-ports-tea-mv836-state)
380. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/client-91c3f484_qzuxu/subnets/pod-default-075e5037_qzuxu/ports/client_qzuxu/state`](#380-policy-api-v1-orgs-default-projects-project-quality-vpcs-client-91c3f484-qzuxu-subnets-pod-default-075e5037-qzuxu-ports-client-qzuxu-state)
381. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/test-lb-50fedbb3_mv836/subnets/pod-default-3cc5e9c8_mv836/ports/coffee_mv836/state`](#381-policy-api-v1-orgs-default-projects-project-quality-vpcs-test-lb-50fedbb3-mv836-subnets-pod-default-3cc5e9c8-mv836-ports-coffee-mv836-state)
382. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/testvpc-7ab2d8aa/subnets/pod-default-e0268dd8_5583h/ports/prevpc-podvm_5583h/state`](#382-policy-api-v1-orgs-default-projects-project-quality-vpcs-testvpc-7ab2d8aa-subnets-pod-default-e0268dd8-5583h-ports-prevpc-podvm-5583h-state)
383. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/test-lb-50fedbb3_mv836/subnets/pod-default-3cc5e9c8_mv836/ports/default_mv836/state`](#383-policy-api-v1-orgs-default-projects-project-quality-vpcs-test-lb-50fedbb3-mv836-subnets-pod-default-3cc5e9c8-mv836-ports-default-mv836-state)
384. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/subnet-e2e-1f11082b_56qvy/subnets/subnet-cidr_56qvy/ports/port-with-ip-1_56qvy/state`](#384-policy-api-v1-orgs-default-projects-project-quality-vpcs-subnet-e2e-1f11082b-56qvy-subnets-subnet-cidr-56qvy-ports-port-with-ip-1-56qvy-state)
385. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/subnet-e2e-1f11082b_56qvy/subnets/subnet-cidr_56qvy/ports/port-with-ip-2_56qvy/state`](#385-policy-api-v1-orgs-default-projects-project-quality-vpcs-subnet-e2e-1f11082b-56qvy-subnets-subnet-cidr-56qvy-ports-port-with-ip-2-56qvy-state)
386. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/testvpc-3658f2b5/subnets/pod-default-ec7c1039_d5d7u/ports/prevpc-client-pod_d5d7u/state`](#386-policy-api-v1-orgs-default-projects-project-quality-vpcs-testvpc-3658f2b5-subnets-pod-default-ec7c1039-d5d7u-ports-prevpc-client-pod-d5d7u-state)
387. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/testvpc-3658f2b5/subnets/pod-default-ec7c1039_d5d7u/ports/prevpc-service-pod_d5d7u/state`](#387-policy-api-v1-orgs-default-projects-project-quality-vpcs-testvpc-3658f2b5-subnets-pod-default-ec7c1039-d5d7u-ports-prevpc-service-pod-d5d7u-state)
388. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/subnet-e2e-1f11082b_56qvy/subnets/subnet-no-ip_56qvy/ports/port-in-no-ip-subnet_56qvy/state`](#388-policy-api-v1-orgs-default-projects-project-quality-vpcs-subnet-e2e-1f11082b-56qvy-subnets-subnet-no-ip-56qvy-ports-port-in-no-ip-subnet-56qvy-state)
389. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/target-ns-56446c91_6zdip/subnets/vm-default-eb532fd0_c6gls/ports/port-e2e-test-3_c6gls/state`](#389-policy-api-v1-orgs-default-projects-project-quality-vpcs-target-ns-56446c91-6zdip-subnets-vm-default-eb532fd0-c6gls-ports-port-e2e-test-3-c6gls-state)
390. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/subnet-e2e-1f11082b_56qvy/subnets/pod-default-6a81803a_56qvy/ports/port-e2e-test-1_56qvy/state`](#390-policy-api-v1-orgs-default-projects-project-quality-vpcs-subnet-e2e-1f11082b-56qvy-subnets-pod-default-6a81803a-56qvy-ports-port-e2e-test-1-56qvy-state)
391. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/test-pod-sync-e8b8a7ca_m404i/subnets/pod-default-0dd88421_m404i/ports/test-pod-32c0f6bc_m404i/state`](#391-policy-api-v1-orgs-default-projects-project-quality-vpcs-test-pod-sync-e8b8a7ca-m404i-subnets-pod-default-0dd88421-m404i-ports-test-pod-32c0f6bc-m404i-state)
392. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/test-pod-1dd9a577_fu9t5/subnets/pod-default-5cf92338_fu9t5/ports/test-source-pod-f9ba0670_fu9t5/state`](#392-policy-api-v1-orgs-default-projects-project-quality-vpcs-test-pod-1dd9a577-fu9t5-subnets-pod-default-5cf92338-fu9t5-ports-test-source-pod-f9ba0670-fu9t5-state)
393. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/web-da775e6f_6o7ts/subnets/pod-default-a734dd59_6o7ts/ports/tcp-deployment-56bcbfc896-s7rng_6o7ts/state`](#393-policy-api-v1-orgs-default-projects-project-quality-vpcs-web-da775e6f-6o7ts-subnets-pod-default-a734dd59-6o7ts-ports-tcp-deployment-56bcbfc896-s7rng-6o7ts-state)
394. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/web-da775e6f_6o7ts/subnets/pod-default-a734dd59_6o7ts/ports/tcp-deployment-56bcbfc896-xs2hs_6o7ts/state`](#394-policy-api-v1-orgs-default-projects-project-quality-vpcs-web-da775e6f-6o7ts-subnets-pod-default-a734dd59-6o7ts-ports-tcp-deployment-56bcbfc896-xs2hs-6o7ts-state)
395. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/subnet-e2e-1f11082b_56qvy/subnets/user-subnetset-dhcp-c85186d8_56qvy/ports/port-in-dhcp-subnetset_56qvy/state`](#395-policy-api-v1-orgs-default-projects-project-quality-vpcs-subnet-e2e-1f11082b-56qvy-subnets-user-subnetset-dhcp-c85186d8-56qvy-ports-port-in-dhcp-subnetset-56qvy-state)
396. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/test-create-vm-basic-f449d9bf_3ehn6/subnets/public-subnet_3ehn6/ports/public-vm-public-subnet-eth0_3ehn6/state`](#396-policy-api-v1-orgs-default-projects-project-quality-vpcs-test-create-vm-basic-f449d9bf-3ehn6-subnets-public-subnet-3ehn6-ports-public-vm-public-subnet-eth0-3ehn6-state)
397. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/test-security-policy-match-expression-ff1dafa9_bgm74/subnets/pod-default-1289f64d_bgm74/ports/pod-a_bgm74/state`](#397-policy-api-v1-orgs-default-projects-project-quality-vpcs-test-security-policy-match-expression-ff1dafa9-bgm74-subnets-pod-default-1289f64d-bgm74-ports-pod-a-bgm74-state)
398. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/subnet-e2e-1f11082b_56qvy/subnets/user-subnetset-static-948a4c45_56qvy/ports/port-in-static-subnetset_56qvy/state`](#398-policy-api-v1-orgs-default-projects-project-quality-vpcs-subnet-e2e-1f11082b-56qvy-subnets-user-subnetset-static-948a4c45-56qvy-ports-port-in-static-subnetset-56qvy-state)
399. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/test-security-policy-match-expression-ff1dafa9_bgm74/subnets/pod-default-1289f64d_bgm74/ports/client-a_bgm74/state`](#399-policy-api-v1-orgs-default-projects-project-quality-vpcs-test-security-policy-match-expression-ff1dafa9-bgm74-subnets-pod-default-1289f64d-bgm74-ports-client-a-bgm74-state)
400. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/test-security-policy-match-expression-ff1dafa9_bgm74/subnets/pod-default-1289f64d_bgm74/ports/client-b_bgm74/state`](#400-policy-api-v1-orgs-default-projects-project-quality-vpcs-test-security-policy-match-expression-ff1dafa9-bgm74-subnets-pod-default-1289f64d-bgm74-ports-client-b-bgm74-state)
401. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/subnet-e2e-1f11082b_56qvy/subnets/subnet-dhcp_56qvy/ports/port-in-dhcp-subnet-with-address-bindings-vc-macpool_56qvy/state`](#401-policy-api-v1-orgs-default-projects-project-quality-vpcs-subnet-e2e-1f11082b-56qvy-subnets-subnet-dhcp-56qvy-ports-port-in-dhcp-subnet-with-address-bindings-vc-macpool-56qvy-state)
402. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/subnet-e2e-1f11082b_56qvy/subnets/subnet-dhcp_56qvy/ports/port-in-dhcp-subnet-with-address-bindings-nsx-macpool_56qvy/state`](#402-policy-api-v1-orgs-default-projects-project-quality-vpcs-subnet-e2e-1f11082b-56qvy-subnets-subnet-dhcp-56qvy-ports-port-in-dhcp-subnet-with-address-bindings-nsx-macpool-56qvy-state)
403. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/test-security-policy-basic-72ecfa65_ib6li/subnets/pod-default-db03dc29_ib6li/ports/server-client-68f86f99bc-2xkkv_ib6li/state`](#403-policy-api-v1-orgs-default-projects-project-quality-vpcs-test-security-policy-basic-72ecfa65-ib6li-subnets-pod-default-db03dc29-ib6li-ports-server-client-68f86f99bc-2xkkv-ib6li-state)
404. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/test-security-policy-basic-72ecfa65_ib6li/subnets/pod-default-db03dc29_ib6li/ports/server-client-68f86f99bc-c2xvr_ib6li/state`](#404-policy-api-v1-orgs-default-projects-project-quality-vpcs-test-security-policy-basic-72ecfa65-ib6li-subnets-pod-default-db03dc29-ib6li-ports-server-client-68f86f99bc-c2xvr-ib6li-state)
405. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/testvpc-3658f2b5/subnets/pod-default-ec7c1039_d5d7u/ports/vmware-system-image-280f8fa0-3f96-4aaf-bf38-390fbf5915ae_d5d7u/state`](#405-policy-api-v1-orgs-default-projects-project-quality-vpcs-testvpc-3658f2b5-subnets-pod-default-ec7c1039-d5d7u-ports-vmware-system-image-280f8fa0-3f96-4aaf-bf38-390fbf5915ae-d5d7u-state)
406. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/testvpc-7ab2d8aa/subnets/pod-default-e0268dd8_5583h/ports/vmware-system-image-1a52a8a8-37d8-4ae2-b433-4a96be950051_5583h/state`](#406-policy-api-v1-orgs-default-projects-project-quality-vpcs-testvpc-7ab2d8aa-subnets-pod-default-e0268dd8-5583h-ports-vmware-system-image-1a52a8a8-37d8-4ae2-b433-4a96be950051-5583h-state)
407. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/web-da775e6f_6o7ts/subnets/pod-default-a734dd59_6o7ts/ports/vmware-system-image-67d253b4-2743-45dd-86ca-a5de1909fc68_6o7ts/state`](#407-policy-api-v1-orgs-default-projects-project-quality-vpcs-web-da775e6f-6o7ts-subnets-pod-default-a734dd59-6o7ts-ports-vmware-system-image-67d253b4-2743-45dd-86ca-a5de1909fc68-6o7ts-state)
408. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/web-da775e6f_6o7ts/subnets/pod-default-a734dd59_6o7ts/ports/vmware-system-image-b3305f6d-fd0d-4c43-9b16-78dc0b9f7ce2_6o7ts/state`](#408-policy-api-v1-orgs-default-projects-project-quality-vpcs-web-da775e6f-6o7ts-subnets-pod-default-a734dd59-6o7ts-ports-vmware-system-image-b3305f6d-fd0d-4c43-9b16-78dc0b9f7ce2-6o7ts-state)
409. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/client-91c3f484_qzuxu/subnets/pod-default-075e5037_qzuxu/ports/vmware-system-image-b16a63d0-2b48-4e25-9222-ed24d7a5c67c_qzuxu/state`](#409-policy-api-v1-orgs-default-projects-project-quality-vpcs-client-91c3f484-qzuxu-subnets-pod-default-075e5037-qzuxu-ports-vmware-system-image-b16a63d0-2b48-4e25-9222-ed24d7a5c67c-qzuxu-state)
410. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/test-lb-50fedbb3_mv836/subnets/pod-default-3cc5e9c8_mv836/ports/vmware-system-image-90dc9354-d875-41fe-b545-01332c956b5a_mv836/state`](#410-policy-api-v1-orgs-default-projects-project-quality-vpcs-test-lb-50fedbb3-mv836-subnets-pod-default-3cc5e9c8-mv836-ports-vmware-system-image-90dc9354-d875-41fe-b545-01332c956b5a-mv836-state)
411. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/test-pod-1dd9a577_fu9t5/subnets/pod-default-5cf92338_fu9t5/ports/vmware-system-image-cd289a18-4ce4-4dff-a025-39f9d0636310_fu9t5/state`](#411-policy-api-v1-orgs-default-projects-project-quality-vpcs-test-pod-1dd9a577-fu9t5-subnets-pod-default-5cf92338-fu9t5-ports-vmware-system-image-cd289a18-4ce4-4dff-a025-39f9d0636310-fu9t5-state)
412. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/test-pod-sync-e8b8a7ca_m404i/subnets/pod-default-0dd88421_m404i/ports/vmware-system-image-38f4d4f7-1fae-4270-9eb3-e8e9f2c5f08a_m404i/state`](#412-policy-api-v1-orgs-default-projects-project-quality-vpcs-test-pod-sync-e8b8a7ca-m404i-subnets-pod-default-0dd88421-m404i-ports-vmware-system-image-38f4d4f7-1fae-4270-9eb3-e8e9f2c5f08a-m404i-state)
413. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/test-security-policy-basic-72ecfa65_ib6li/subnets/pod-default-db03dc29_ib6li/ports/vmware-system-image-7f80e1f0-a3f7-4d67-87e3-16162d5cdcc8_ib6li/state`](#413-policy-api-v1-orgs-default-projects-project-quality-vpcs-test-security-policy-basic-72ecfa65-ib6li-subnets-pod-default-db03dc29-ib6li-ports-vmware-system-image-7f80e1f0-a3f7-4d67-87e3-16162d5cdcc8-ib6li-state)
414. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/test-security-policy-match-expression-ff1dafa9_bgm74/subnets/pod-default-1289f64d_bgm74/ports/vmware-system-image-78efc28d-50fb-4bf5-8eb3-5ff538be370c_bgm74/state`](#414-policy-api-v1-orgs-default-projects-project-quality-vpcs-test-security-policy-match-expression-ff1dafa9-bgm74-subnets-pod-default-1289f64d-bgm74-ports-vmware-system-image-78efc28d-50fb-4bf5-8eb3-5ff538be370c-bgm74-state)
415. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/test-security-policy-match-expression-ff1dafa9_bgm74/subnets/pod-default-1289f64d_bgm74/ports/vmware-system-image-849fb668-f3ab-48bc-846b-38c485bd8f1f_bgm74/state`](#415-policy-api-v1-orgs-default-projects-project-quality-vpcs-test-security-policy-match-expression-ff1dafa9-bgm74-subnets-pod-default-1289f64d-bgm74-ports-vmware-system-image-849fb668-f3ab-48bc-846b-38c485bd8f1f-bgm74-state)
416. [`/policy/api/v1/orgs/default/projects/project-quality/vpcs/test-security-policy-match-expression-ff1dafa9_bgm74/subnets/pod-default-1289f64d_bgm74/ports/vmware-system-image-92b67ea7-200d-4a00-92d3-c6974f97422f_bgm74/state`](#416-policy-api-v1-orgs-default-projects-project-quality-vpcs-test-security-policy-match-expression-ff1dafa9-bgm74-subnets-pod-default-1289f64d-bgm74-ports-vmware-system-image-92b67ea7-200d-4a00-92d3-c6974f97422f-bgm74-state)

---
## API Endpoint Details


<a id="1-policy-api-v1-org-root"></a>
### 1. /policy/api/v1/org-root

**HTTP Methods:** PATCH

**Explanation:**
Root organization resource for NSX VPC management. Used to manage the hierarchical structure of organizations, projects, and VPCs.

**Request Body (PATCH):**
```json
{
  "children": [
    {
      "children": [
        {
          "children": [
            {
              "Vpc": {
                "children": [
                  {
                    "LBService": {
                      "connectivity_path": "/orgs/default/projects/project-quality/vpcs/default",
                      "display_name": "default",
                      "id": "default",
                      "relax_scale_validation": true,
                      "resource_type": "LBService",
                      "size": "SMALL",
                      "tags": [
                        {
                          "scope": "nsx-op/cluster",
                          "tag": "f06fd228-8088-4439-a9e6-26c90a829c57"
                        },
                        {
                          "scope": "nsx-op/version",
                          "tag": "1.0.0"
                        },
                        {
                          "scope": "nsx-op/namespace",
                          "tag": "test-security-policy-client-3a06d660"
                        },
                        {
                          "scope": "nsx-op/namespace_uid",
                          "tag": "a84abf99-2aca-4594-854f-381bc44d868b"
                        },
                        {
                          "scope": "nsx-op/created_for",
                          "tag": "SLB"
                        }
                      ]
                    },
                    "id": "default",
                    "resource_type": "ChildLBService"
                  },
                  {
                    "VpcAttachment": {
                      "display_name": "default",
                      "id": "default",
                      "resource_type": "VpcAttachment",
                      "tags": [
                        {
                          "scope": "nsx-op/cluster",
                          "tag": "f06fd228-8088-4439-a9e6-26c90a829c57"
                        },
                        {
                          "scope": "nsx-op/version",
                          "tag": "1.0.0"
                        },
                        {
                          "scope": "nsx-op/namespace",
                          "tag": "test-security-policy-client-3a06d660"
                        },
                        {
                          "scope": "nsx-op/namespace_uid",
                          "tag": "a84abf99-2aca-4594-854f-381bc44d868b"
                        }
                      ],
                      "vpc_connectivity_profile": "/orgs/default/projects/project-quality/vpc-connectivity-profiles/default"
                    },
                    "id": "default",
                    "resource_type": "ChildVpcAttachment"
                  }
                ],
                "display_name": "test-security-policy-client-3a06d660_qiyvu",
                "id": "test-security-policy-client-3a06d660_qiyvu",
                "ip_address_type": "IPV4",
                "private_ips": [
                  "172.26.0.0/16"
                ],
                "resource_type": "Vpc",
                "tags": [
                  {
                    "scope": "nsx-op/cluster",
                    "tag": "f06fd228-8088-4439-a9e6-26c90a829c57"
                  },
                  {
                    "scope": "nsx-op/version",
                    "tag": "1.0.0"
                  },
                  {
                    "scope": "nsx-op/namespace",
                    "tag": "test-security-policy-client-3a06d660"
                  },
                  {
                    "scope": "nsx-op/namespace_uid",
                    "tag": "a84abf99-2aca-4594-854f-381bc44d868b"
                  },
                  {
                    "scope": "nsx/managed-by",
                    "tag": "nsx-op"
                  }
                ]
              },
              "id": "test-security-policy-client-3a06d660_qiyvu",
              "resource_type": "ChildVpc"
            }
          ],
          "id": "project-quality",
          "resource_type": "ChildResourceReference",
          "target_type": "Project"
        }
      ],
      "id": "default",
      "resource_type": "ChildResourceReference",
      "target_type": "Org"
    }
  ],
  "resource_type": "OrgRoot"
}
```

---

<a id="2-policy-api-v1-search-query"></a>
### 2. /policy/api/v1/search/query

**HTTP Methods:** GET

**Explanation:**
Search API endpoint for querying NSX resources by type and tags. Supports filtering with query parameters for resource_type, tags, and sorting.

---


**Sample Response Body (GET, from logs):**
```json
{
  "results": [
    {
      "unique_id": "7a5abfb3-90df-4abb-ba3e-3e07db09687c",
      "_last_modified_user": "wcp-cluster-user-f06fd228-8088-4439-a9e6-26c90a829c57-d34133d7-0fdf-4c9d-abcf-df83bd050a59",
      "_revision": 0,
      "owner_id": "42495ba4-8c0b-49c9-b645-84cc39c2df30",
      "_system_owned": false,
      "resource_type": "Domain",
      "realization_id": "7a5abfb3-90df-4abb-ba3e-3e07db09687c",
      "_last_modified_time": 1760503429406,
      "overridden": false,
      "display_name": "f06fd228-8088-4439-a9e6-26c90a829c57",
      "remote_path": "",
      "_create_user": "wcp-cluster-user-f06fd228-8088-4439-a9e6-26c90a829c57-d34133d7-0fdf-4c9d-abcf-df83bd050a59",
      "tags": [
        {
          "scope": "ncp/cluster_domain",
          "tag": "true"
        },
        {
          "scope": "ncp/cluster",
          "tag": "f06fd228-8088-4439-a9e6-26c90a829c57"
        }
      ],
      "_create_time": 1760503429406,
      "path": "/infra/domains/f06fd228-8088-4439-a9e6-26c90a829c57",
      "marked_for_delete": false,
      "parent_path": "/infra",
      "id": "f06fd228-8088-4439-a9e6-26c90a829c57",
      "relative_path": "f06fd228-8088-4439-a9e6-26c90a829c57",
      "status": {
        "intent_version": "0",
        "consolidated_status": {
          "consolidated_status": "UNINITIALIZED"
        },
        "intent_path": "/infra/domains/f06fd228-8088-4439-a9e6-26c90a829c57",
        "publish_status": "UNAVAILABLE"
      },
      "_protection": "NOT_PROTECTED"
    }
  ],
  "result_count": 1,
  "cursor": "1"
}
```
<a id="3-policy-api-v1-infra-ip-blocks"></a>
### 3. /policy/api/v1/infra/ip-blocks

**HTTP Methods:** GET

**Explanation:**
NSX Policy API endpoint for resource management.

---


**Sample Response Body (GET, from logs):**
```json
{
  "results": [
    {
      "cidr": "169.254.64.0/18",
      "cidrs": [
        "169.254.64.0/18"
      ],
      "visibility": "PRIVATE",
      "ip_address_type": "IPV4",
      "sync_realization": false,
      "is_subnet_exclusive": false,
      "usage_percentage": 0.0,
      "total_size": "16384",
      "used_size": "0",
      "resource_type": "IpAddressBlock",
      "id": "global-tgw-transit-subnet-block",
      "display_name": "global-tgw-transit-subnet-block",
      "path": "/infra/ip-blocks/global-tgw-transit-subnet-block",
      "relative_path": "global-tgw-transit-subnet-block",
      "parent_path": "/infra",
      "remote_path": "",
      "unique_id": "3360063f-24e4-4747-b361-953de49fc857",
      "realization_id": "3360063f-24e4-4747-b361-953de49fc857",
      "owner_id": "42495ba4-8c0b-49c9-b645-84cc39c2df30",
      "marked_for_delete": false,
      "overridden": false,
      "_system_owned": false,
      "_protection": "NOT_PROTECTED",
      "_create_time": 1760496489729,
      "_create_user": "system",
      "_last_modified_time": 1760496489729,
      "_last_modified_user": "system",
      "_revision": 0
    },
    {
      "cidr": "192.168.0.0/16",
      "cidrs": [
        "192.168.0.0/16"
      ],
      "visibility": "EXTERNAL",
      "ip_address_type": "IPV4",
      "sync_realization": true,
      "is_subnet_exclusive": false,
      "usage_percentage": 0.01,
      "total_size": "65536",
      "used_size": "7",
      "resource_type": "IpAddressBlock",
      "id": "ipblock-192.168.0.0-netmask-16",
      "display_name": "ipblock-192.168.0.0-netmask-16",
      "description": "WCP IPBlock ipblock-192.168.0.0-netmask-16 created by VDNet",
      "path": "/infra/ip-blocks/ipblock-192.168.0.0-netmask-16",
      "relative_path": "ipblock-192.168.0.0-netmask-16",
      "parent_path": "/infra",
      "remote_path": "",
      "unique_id": "2a0c9d0f-8b79-417f-bde3-5d34a33c405e",
      "realization_id": "2a0c9d0f-8b79-417f-bde3-5d34a33c405e",
      "owner_id": "42495ba4-8c0b-49c9-b645-84cc39c2df30",
      "marked_for_delete": false,
      "overridden": false,
      "_system_owned": false,
      "_protection": "NOT_PROTECTED",
      "_create_time": 1760501561601,
      "_create_user": "admin",
      "_last_modified_time": 1760688092362,
      "_last_modified_user": "system",
      "_revision": 553
    }
  ],
  "result_count": 2,
  "sort_by": "display_name",
  "sort_ascending": true
}
```
<a id="4-policy-api-v1-infra-certificates"></a>
### 4. /policy/api/v1/infra/certificates

**HTTP Methods:** GET

**Explanation:**
NSX Policy API endpoint for resource management.

---


**Sample Response Body (GET, from logs):**
```json
{
  "results": [
    {
      "pem_encoded": "-----BEGIN CERTIFICATE-----\nMIIFLDCCA5SgAwIBAgIJANYi6D1rMVcZMA0GCSqGSIb3DQEBCwUAMIGwMQswCQYD\nVQQDDAJDQTEXMBUGCgmSJomT8ixkARkWB3ZzcGhlcmUxFTATBgoJkiaJk/IsZAEZ\nFgVsb2NhbDELMAkGA1UEBhMCVVMxEzARBgNVBAgMCkNhbGlmb3JuaWExMjAwBgNV\nBAoMKWx2bi1kdm0tMTAtNzAtMTkwLTY4LmR2bS5sdm4uYnJvYWRjb20ubmV0MRsw\nGQYDVQQLDBJWTXdhcmUgRW5naW5lZXJpbmcwHhcNMjUxMDE1MDQyMDQxWhcNMjYx\nMDE1MDQyMDQxWjBTMTIwMAYDVQQLEylsdm4tZHZtLTEwLTcwLTE5MC02OC5kdm0u\nbHZuLmJyb2FkY29tLm5ldDEdMBsGA1UEAxMUZGVmYXVsdGluZ3Jlc3MubG9jYWww\nggGiMA0GCSqGSIb3DQEBAQUAA4IBjwAwggGKAoIBgQDGinax5+kxWT6xWuuZxYqx\n/6HC4KRv4mXRaAiMe7MdXvbmkIiyM+SSDQhIVXWGgekYfhLsPlWYpWi4AMe/qfub\nTe9xaHvhPHICMFjJs69MFK3i4A/bZbOyYrrHAEqQbLsGIxpSN22pvuQtHjF8FZxu\njzqnmzuG/tAmv/eLTG0rChpzvV+gpjz24cQkgOi7JMexev1QsFv93tk807poKi6G\n8lLibMtpOxgxGI/fLuIdhcAfWiqDW/xf1OaNQ4lZD36AfN13PY6PKsQOoAPhwHPJ\n4Kr/yUZeVFgdaqxQ33GZzQhpkIPPsfSMakOcYexuZ7TX1JTjKSIiRC5jmATdJ4i3\nAQ7eMRjj/U24g5gZzjxeIPI7h7/2i0MNgJBlQK6ms/FqEuVBDDbS0I/Y48U7VJdr\npI36eErP3pKvJBFzFmiXSR4lkVA6Y7sJS+T+8eE1jdUsPhPu+RfLPGkhoumjxZfG\nVwGpZPq7XHoyrK6A2HtfjTvZv9GRnbsvAWb/uJe7am0CAwEAAaOBpDCBoTAOBgNV\nHQ8BAf8EBAMCAKAwEwYDVR0lBAwwCgYIKwYBBQUHAwEwHwYDVR0jBBgwFoAUkPyy\nObYKIcJKQJ1/9Fg98wpciyEwWQYIKwYBBQUHAQEETTBLMEkGCCsGAQUFBzAChj1o\ndHRwczovL2x2bi1kdm0tMTAtNzAtMTkwLTY4LmR2bS5sdm4uYnJvYWRjb20ubmV0\nL2FmZC92ZWNzL2NhMA0GCSqGSIb3DQEBCwUAA4IBgQCYJVoTKMyWZZ9WXY5Jn753\nTqkBoPX/OFj6uf36I5iqUFJrc5BskwZzlhb3tOJ6tg36IElBzbcp/hpGYZKynldE\nzsdTjKXnwgc1QGW0TBHPBPKPXZHUe1S5QjVi0bXWDnK/5pMenxo4xvKMbLjbzmpu\nypTmQoG2IqLhjmp8V62uMOYY62+/LEFg2gq/AFJVhgbHXXQrzaDlDCUp+5bLRI+t\nDBIr5wkFz+Zsw3Lr9uI3UZ9W5sAkZb3fc2DUP3NofrRUFcOlpN7bqTvfiwJJ2QiK\nttPaGNZIW+dw+3rPzx1uAfaoJKctCXiaWMCmzI2FQLi5qIkDee+wKCNunzurj7xf\nXsCrk+0evLrAu43/za/JU+vjeCBVLBqqecun3mBZSGXIWsTOHuntzEyEPwvCLsDD\nylHl6PIFLf4mZOCXLZG1BONtSF0TyBvfJp5sdwIE+jeBn00GEFb3t+QOxRLdhbcT\nG+PnY3t4JUrLHEeHot1D6P1FBrnvDs4qQ3yGkNW1UKw=\n-----END CERTIFICATE-----\n",
      "has_private_key": true,
      "tls_certificate_type": "CERTIFICATE_SIGNED",
      "category": "SERVICE_CERTIFICATE",
      "resource_type": "TlsCertificate",
      "id": "lb_f06fd228-8088-4439-a9e6-26c90a829c57_prftk",
      "display_name": "lb-f06fd228-8088-4439-a9e6-26c90a829c57",
      "tags": [
        {
          "scope": "ncp/version",
          "tag": "1.2.0"
        },
        {
          "scope": "ncp/cluster",
          "tag": "f06fd228-8088-4439-a9e6-26c90a829c57"
        },
        {
          "scope": "ncp/lb_default_cert",
          "tag": "true"
        },
        {
          "scope": "external_id",
          "tag": "2003591b-b187-556a-9c82-e308c09a273c"
        }
      ],
      "path": "/infra/certificates/lb_f06fd228-8088-4439-a9e6-26c90a829c57_prftk",
      "relative_path": "lb_f06fd228-8088-4439-a9e6-26c90a829c57_prftk",
      "parent_path": "/infra",
      "remote_path": "",
      "unique_id": "4f4334bf-5c7c-436a-ae28-898047b7697b",
      "realization_id": "4f4334bf-5c7c-436a-ae28-898047b7697b",
      "owner_id": "42495ba4-8c
  ...
}
```
<a id="5-policy-api-v1-infra-lb-app-profiles"></a>
### 5. /policy/api/v1/infra/lb-app-profiles

**HTTP Methods:** GET

**Explanation:**
NSX Policy API endpoint for resource management.

---


**Sample Response Body (GET, from logs):**
```json
{
  "results": [
    {
      "http_redirect_to_https": false,
      "ntlm": false,
      "idle_timeout": 15,
      "request_header_size": 1024,
      "response_timeout": 60,
      "response_header_size": 4096,
      "response_buffering": false,
      "server_keep_alive": false,
      "resource_type": "LBHttpProfile",
      "id": "default-http-lb-app-profile",
      "display_name": "default-http-lb-app-profile",
      "path": "/infra/lb-app-profiles/default-http-lb-app-profile",
      "relative_path": "default-http-lb-app-profile",
      "parent_path": "/infra",
      "remote_path": "",
      "unique_id": "bc4c38a5-468a-42b6-9296-13e8b4d2b641",
      "realization_id": "bc4c38a5-468a-42b6-9296-13e8b4d2b641",
      "owner_id": "42495ba4-8c0b-49c9-b645-84cc39c2df30",
      "marked_for_delete": false,
      "overridden": false,
      "_system_owned": true,
      "_protection": "NOT_PROTECTED",
      "_create_time": 1760496491019,
      "_create_user": "system",
      "_last_modified_time": 1760496491019,
      "_last_modified_user": "system",
      "_revision": 0
    },
    {
      "idle_timeout": 1800,
      "close_timeout": 8,
      "ha_flow_mirroring_enabled": false,
      "resource_type": "LBFastTcpProfile",
      "id": "default-tcp-lb-app-profile",
      "display_name": "default-tcp-lb-app-profile",
      "path": "/infra/lb-app-profiles/default-tcp-lb-app-profile",
      "relative_path": "default-tcp-lb-app-profile",
      "parent_path": "/infra",
      "remote_path": "",
      "unique_id": "782229ab-bdc8-4141-b9cb-a422fb902d26",
      "realization_id": "782229ab-bdc8-4141-b9cb-a422fb902d26",
      "owner_id": "42495ba4-8c0b-49c9-b645-84cc39c2df30",
      "marked_for_delete": false,
      "overridden": false,
      "_system_owned": true,
      "_protection": "NOT_PROTECTED",
      "_create_time": 1760496491029,
      "_create_user": "system",
      "_last_modified_time": 1760496491029,
      "_last_modified_user": "system",
      "_revision": 0
    },
    {
      "idle_timeout": 300,
      "flow_mirroring_enabled": false,
      "resource_type": "LBFastUdpProfile",
      "id": "default-udp-lb-app-profile",
      "display_name": "default-udp-lb-app-profile",
      "path": "/infra/lb-app-profiles/default-udp-lb-app-profile",
      "relative_path": "default-udp-lb-app-profile",
      "parent_path": "/infra",
      "remote_path": "",
      "unique_id": "157ddf75-a5a4-4b2d-9f5b-a3a2ef0853ae",
      "realization_id": "157ddf75-a5a4-4b2d-9f5b-a3a2ef0853ae",
      "owner_id": "42495ba4-8c0b-49c9-b645-84cc39c2df30",
      "marked_for_delete": false,
      "overridden": false,
      "_system_owned": true,
      "_protection": "NOT_PROTECTED",
      "_create_time": 1760496491040,
      "_create_user": "system",
      "_last_modified_time": 1760496491040,
      "_last_modified_user": "system",
      "_revision": 0
    },
    {
      "idle_timeout": 1800,
      "close_timeout": 8,
      "ha_flow_mirroring_enabled": false,
      "resource_type": "LBFastTcpProfi
  ...
}
```
<a id="6-policy-api-v1-infra-lb-client-ssl-profiles"></a>
### 6. /policy/api/v1/infra/lb-client-ssl-profiles

**HTTP Methods:** GET

**Explanation:**
NSX Policy API endpoint for resource management.

---


**Sample Response Body (GET, from logs):**
```json
{
  "results": [
    {
      "cipher_group_label": "BALANCED",
      "ciphers": [
        "TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256",
        "TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA256",
        "TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384",
        "TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256",
        "TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA",
        "TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA",
        "TLS_RSA_WITH_AES_128_GCM_SHA256",
        "TLS_RSA_WITH_AES_128_CBC_SHA256",
        "TLS_RSA_WITH_AES_128_CBC_SHA",
        "TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384"
      ],
      "protocols": [
        "TLS_V1_2"
      ],
      "session_cache_enabled": true,
      "session_cache_timeout": 300,
      "prefer_server_ciphers": true,
      "is_secure": true,
      "is_fips": true,
      "resource_type": "LBClientSslProfile",
      "id": "default-balanced-client-ssl-profile",
      "display_name": "default-balanced-client-ssl-profile",
      "path": "/infra/lb-client-ssl-profiles/default-balanced-client-ssl-profile",
      "relative_path": "default-balanced-client-ssl-profile",
      "parent_path": "/infra",
      "remote_path": "",
      "unique_id": "05df8dce-6186-40cd-8dbc-4c7883d4a055",
      "realization_id": "05df8dce-6186-40cd-8dbc-4c7883d4a055",
      "owner_id": "42495ba4-8c0b-49c9-b645-84cc39c2df30",
      "marked_for_delete": false,
      "overridden": false,
      "_system_owned": true,
      "_protection": "NOT_PROTECTED",
      "_create_time": 1760496491104,
      "_create_user": "system",
      "_last_modified_time": 1760496491104,
      "_last_modified_user": "system",
      "_revision": 0
    },
    {
      "cipher_group_label": "HIGH_COMPATIBILITY",
      "ciphers": [
        "TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256",
        "TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA256",
        "TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384",
        "TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256",
        "TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA",
        "TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA",
        "TLS_RSA_WITH_AES_128_GCM_SHA256",
        "TLS_RSA_WITH_AES_128_CBC_SHA256",
        "TLS_RSA_WITH_AES_128_CBC_SHA",
        "TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384"
      ],
      "protocols": [
        "TLS_V1_2"
      ],
      "session_cache_enabled": true,
      "session_cache_timeout": 300,
      "prefer_server_ciphers": true,
      "is_secure": true,
      "is_fips": true,
      "resource_type": "LBClientSslProfile",
      "id": "default-high-compatibility-client-ssl-profile",
      "display_name": "default-high-compatibility-client-ssl-profile",
      "path": "/infra/lb-client-ssl-profiles/default-high-compatibility-client-ssl-profile",
      "relative_path": "default-high-compatibility-client-ssl-profile",
      "parent_path": "/infra",
      "remote_path": "",
      "unique_id": "33b592a8-206c-4ad9-b81a-7db5a70b8df7",
      "realization_id": "33b592a8-206c-4ad9-b81a-7db5a70b8df7",
      "owner_id": "42495ba4-8c0b-49c9-b645-84cc39c2df30",
      "marked_for_delete": false,
      "overridd
  ...
}
```
<a id="7-policy-api-v1-infra-lb-server-ssl-profiles"></a>
### 7. /policy/api/v1/infra/lb-server-ssl-profiles

**HTTP Methods:** GET

**Explanation:**
NSX Policy API endpoint for resource management.

---


**Sample Response Body (GET, from logs):**
```json
{
  "results": [
    {
      "cipher_group_label": "BALANCED",
      "ciphers": [
        "TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256",
        "TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA256",
        "TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384",
        "TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256",
        "TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA",
        "TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA",
        "TLS_RSA_WITH_AES_128_GCM_SHA256",
        "TLS_RSA_WITH_AES_128_CBC_SHA256",
        "TLS_RSA_WITH_AES_128_CBC_SHA",
        "TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384"
      ],
      "protocols": [
        "TLS_V1_2"
      ],
      "session_cache_enabled": true,
      "is_secure": true,
      "is_fips": true,
      "resource_type": "LBServerSslProfile",
      "id": "default-balanced-server-ssl-profile",
      "display_name": "default-balanced-server-ssl-profile",
      "path": "/infra/lb-server-ssl-profiles/default-balanced-server-ssl-profile",
      "relative_path": "default-balanced-server-ssl-profile",
      "parent_path": "/infra",
      "remote_path": "",
      "unique_id": "99037ec3-a201-41f1-9020-becec8186581",
      "realization_id": "99037ec3-a201-41f1-9020-becec8186581",
      "owner_id": "42495ba4-8c0b-49c9-b645-84cc39c2df30",
      "marked_for_delete": false,
      "overridden": false,
      "_system_owned": true,
      "_protection": "NOT_PROTECTED",
      "_create_time": 1760496491112,
      "_create_user": "system",
      "_last_modified_time": 1760496491112,
      "_last_modified_user": "system",
      "_revision": 0
    },
    {
      "cipher_group_label": "HIGH_COMPATIBILITY",
      "ciphers": [
        "TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256",
        "TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA256",
        "TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384",
        "TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256",
        "TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA",
        "TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA",
        "TLS_RSA_WITH_AES_128_GCM_SHA256",
        "TLS_RSA_WITH_AES_128_CBC_SHA256",
        "TLS_RSA_WITH_AES_128_CBC_SHA",
        "TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384"
      ],
      "protocols": [
        "TLS_V1_2"
      ],
      "session_cache_enabled": true,
      "is_secure": true,
      "is_fips": true,
      "resource_type": "LBServerSslProfile",
      "id": "default-high-compatibility-server-ssl-profile",
      "display_name": "default-high-compatibility-server-ssl-profile",
      "path": "/infra/lb-server-ssl-profiles/default-high-compatibility-server-ssl-profile",
      "relative_path": "default-high-compatibility-server-ssl-profile",
      "parent_path": "/infra",
      "remote_path": "",
      "unique_id": "ac469730-526a-462d-b769-a668ad118b20",
      "realization_id": "ac469730-526a-462d-b769-a668ad118b20",
      "owner_id": "42495ba4-8c0b-49c9-b645-84cc39c2df30",
      "marked_for_delete": false,
      "overridden": false,
      "_system_owned": true,
      "_protection": "NOT_PROTECTED",
      "_create_time": 1760496491111,
      "_create_user": "system"
  ...
}
```
<a id="8-policy-api-v1-infra-lb-pools-tea-svc-80-tcp-39r0c"></a>
### 8. /policy/api/v1/infra/lb-pools/tea-svc_80_TCP_39r0c

**HTTP Methods:** DELETE, GET, PATCH

**Explanation:**
NSX Policy API endpoint for resource management.

---


**Sample Response Body (GET, from logs):**
```json
{
  "algorithm": "ROUND_ROBIN",
  "snat_translation": {
    "type": "LBSnatDisabled"
  },
  "min_active_members": 1,
  "resource_type": "LBPool",
  "id": "tea-svc_80_TCP_39r0c",
  "display_name": "tea-svc_80_TCP",
  "tags": [
    {
      "scope": "ncp/version",
      "tag": "1.2.0"
    },
    {
      "scope": "ncp/cluster",
      "tag": "f06fd228-8088-4439-a9e6-26c90a829c57"
    },
    {
      "scope": "ncp/project",
      "tag": "test-lb-50fedbb3"
    },
    {
      "scope": "external_id",
      "tag": "f8572ed6-448c-4830-8e1d-5c00326ab97f"
    },
    {
      "scope": "ncp/service",
      "tag": "tea-svc"
    },
    {
      "scope": "ncp/service_uid",
      "tag": "f8572ed6-448c-4830-8e1d-5c00326ab97f"
    },
    {
      "scope": "ncp/service_port",
      "tag": "80"
    },
    {
      "scope": "ncp/service_port_protocol",
      "tag": "TCP"
    },
    {
      "scope": "ncp/created_for",
      "tag": "DLB"
    }
  ],
  "path": "/infra/lb-pools/tea-svc_80_TCP_39r0c",
  "relative_path": "tea-svc_80_TCP_39r0c",
  "parent_path": "/infra",
  "remote_path": "",
  "unique_id": "cd823642-ff17-40d3-8e87-51cb1eb03e89",
  "realization_id": "cd823642-ff17-40d3-8e87-51cb1eb03e89",
  "owner_id": "42495ba4-8c0b-49c9-b645-84cc39c2df30",
  "marked_for_delete": false,
  "overridden": false,
  "_system_owned": false,
  "_protection": "NOT_PROTECTED",
  "_create_time": 1760689212216,
  "_create_user": "wcp-cluster-user-f06fd228-8088-4439-a9e6-26c90a829c57-d34133d7-0fdf-4c9d-abcf-df83bd050a59",
  "_last_modified_time": 1760689212216,
  "_last_modified_user": "wcp-cluster-user-f06fd228-8088-4439-a9e6-26c90a829c57-d34133d7-0fdf-4c9d-abcf-df83bd050a59",
  "_revision": 0
}
```
<a id="9-policy-api-v1-infra-lb-pools-tea-svc-80-tcp-p5j45"></a>
### 9. /policy/api/v1/infra/lb-pools/tea-svc_80_TCP_p5j45

**HTTP Methods:** DELETE, GET, PATCH

**Explanation:**
NSX Policy API endpoint for resource management.

---


**Sample Response Body (GET, from logs):**
```json
{
  "algorithm": "ROUND_ROBIN",
  "snat_translation": {
    "type": "LBSnatDisabled"
  },
  "min_active_members": 1,
  "resource_type": "LBPool",
  "id": "tea-svc_80_TCP_p5j45",
  "display_name": "tea-svc_80_TCP",
  "tags": [
    {
      "scope": "ncp/version",
      "tag": "1.2.0"
    },
    {
      "scope": "ncp/cluster",
      "tag": "f06fd228-8088-4439-a9e6-26c90a829c57"
    },
    {
      "scope": "ncp/project",
      "tag": "test-ipaddress-allocation-40d5699d"
    },
    {
      "scope": "external_id",
      "tag": "55c7492b-a285-4cba-9d71-bb6305d8c977"
    },
    {
      "scope": "ncp/service",
      "tag": "tea-svc"
    },
    {
      "scope": "ncp/service_uid",
      "tag": "55c7492b-a285-4cba-9d71-bb6305d8c977"
    },
    {
      "scope": "ncp/service_port",
      "tag": "80"
    },
    {
      "scope": "ncp/service_port_protocol",
      "tag": "TCP"
    },
    {
      "scope": "ncp/created_for",
      "tag": "DLB"
    }
  ],
  "path": "/infra/lb-pools/tea-svc_80_TCP_p5j45",
  "relative_path": "tea-svc_80_TCP_p5j45",
  "parent_path": "/infra",
  "remote_path": "",
  "unique_id": "91a1f3df-7364-4594-a377-6d60ab8ffae2",
  "realization_id": "91a1f3df-7364-4594-a377-6d60ab8ffae2",
  "owner_id": "42495ba4-8c0b-49c9-b645-84cc39c2df30",
  "marked_for_delete": false,
  "overridden": false,
  "_system_owned": false,
  "_protection": "NOT_PROTECTED",
  "_create_time": 1760689104663,
  "_create_user": "wcp-cluster-user-f06fd228-8088-4439-a9e6-26c90a829c57-d34133d7-0fdf-4c9d-abcf-df83bd050a59",
  "_last_modified_time": 1760689104663,
  "_last_modified_user": "wcp-cluster-user-f06fd228-8088-4439-a9e6-26c90a829c57-d34133d7-0fdf-4c9d-abcf-df83bd050a59",
  "_revision": 0
}
```
<a id="10-policy-api-v1-infra-lb-pools-tea-svc-80-udp-39r0c"></a>
### 10. /policy/api/v1/infra/lb-pools/tea-svc_80_UDP_39r0c

**HTTP Methods:** DELETE, GET, PATCH

**Explanation:**
NSX Policy API endpoint for resource management.

---


**Sample Response Body (GET, from logs):**
```json
{
  "algorithm": "ROUND_ROBIN",
  "snat_translation": {
    "type": "LBSnatDisabled"
  },
  "min_active_members": 1,
  "resource_type": "LBPool",
  "id": "tea-svc_80_UDP_39r0c",
  "display_name": "tea-svc_80_UDP",
  "tags": [
    {
      "scope": "ncp/version",
      "tag": "1.2.0"
    },
    {
      "scope": "ncp/cluster",
      "tag": "f06fd228-8088-4439-a9e6-26c90a829c57"
    },
    {
      "scope": "ncp/project",
      "tag": "test-lb-50fedbb3"
    },
    {
      "scope": "external_id",
      "tag": "f8572ed6-448c-4830-8e1d-5c00326ab97f"
    },
    {
      "scope": "ncp/service",
      "tag": "tea-svc"
    },
    {
      "scope": "ncp/service_uid",
      "tag": "f8572ed6-448c-4830-8e1d-5c00326ab97f"
    },
    {
      "scope": "ncp/service_port",
      "tag": "80"
    },
    {
      "scope": "ncp/service_port_protocol",
      "tag": "UDP"
    },
    {
      "scope": "ncp/created_for",
      "tag": "DLB"
    }
  ],
  "path": "/infra/lb-pools/tea-svc_80_UDP_39r0c",
  "relative_path": "tea-svc_80_UDP_39r0c",
  "parent_path": "/infra",
  "remote_path": "",
  "unique_id": "7c9d6248-d144-4277-bdd4-a9dea29cf47f",
  "realization_id": "7c9d6248-d144-4277-bdd4-a9dea29cf47f",
  "owner_id": "42495ba4-8c0b-49c9-b645-84cc39c2df30",
  "marked_for_delete": false,
  "overridden": false,
  "_system_owned": false,
  "_protection": "NOT_PROTECTED",
  "_create_time": 1760689215554,
  "_create_user": "wcp-cluster-user-f06fd228-8088-4439-a9e6-26c90a829c57-d34133d7-0fdf-4c9d-abcf-df83bd050a59",
  "_last_modified_time": 1760689215554,
  "_last_modified_user": "wcp-cluster-user-f06fd228-8088-4439-a9e6-26c90a829c57-d34133d7-0fdf-4c9d-abcf-df83bd050a59",
  "_revision": 0
}
```
<a id="11-policy-api-v1-infra-realized-state-realized-entity"></a>
### 11. /policy/api/v1/infra/realized-state/realized-entity

**HTTP Methods:** GET

**Explanation:**
NSX Policy API endpoint for resource management.

---

<a id="12-policy-api-v1-infra-lb-pools-coffee-svc-80-tcp-cnml1"></a>
### 12. /policy/api/v1/infra/lb-pools/coffee-svc_80_TCP_cnml1

**HTTP Methods:** DELETE, GET, PATCH

**Explanation:**
NSX Policy API endpoint for resource management.

---


**Sample Response Body (GET, from logs):**
```json
{
  "algorithm": "ROUND_ROBIN",
  "snat_translation": {
    "type": "LBSnatDisabled"
  },
  "min_active_members": 1,
  "resource_type": "LBPool",
  "id": "coffee-svc_80_TCP_cnml1",
  "display_name": "coffee-svc_80_TCP",
  "tags": [
    {
      "scope": "ncp/version",
      "tag": "1.2.0"
    },
    {
      "scope": "ncp/cluster",
      "tag": "f06fd228-8088-4439-a9e6-26c90a829c57"
    },
    {
      "scope": "ncp/project",
      "tag": "test-lb-50fedbb3"
    },
    {
      "scope": "external_id",
      "tag": "75a666bb-cb7a-45dd-a6a6-6d0f0e7d685e"
    },
    {
      "scope": "ncp/service",
      "tag": "coffee-svc"
    },
    {
      "scope": "ncp/service_uid",
      "tag": "75a666bb-cb7a-45dd-a6a6-6d0f0e7d685e"
    },
    {
      "scope": "ncp/service_port",
      "tag": "80"
    },
    {
      "scope": "ncp/service_port_protocol",
      "tag": "TCP"
    },
    {
      "scope": "ncp/created_for",
      "tag": "DLB"
    }
  ],
  "path": "/infra/lb-pools/coffee-svc_80_TCP_cnml1",
  "relative_path": "coffee-svc_80_TCP_cnml1",
  "parent_path": "/infra",
  "remote_path": "",
  "unique_id": "9d071cd6-adea-4d78-9bc4-68c0df6f6ca6",
  "realization_id": "9d071cd6-adea-4d78-9bc4-68c0df6f6ca6",
  "owner_id": "42495ba4-8c0b-49c9-b645-84cc39c2df30",
  "marked_for_delete": false,
  "overridden": false,
  "_system_owned": false,
  "_protection": "NOT_PROTECTED",
  "_create_time": 1760689287050,
  "_create_user": "wcp-cluster-user-f06fd228-8088-4439-a9e6-26c90a829c57-d34133d7-0fdf-4c9d-abcf-df83bd050a59",
  "_last_modified_time": 1760689287050,
  "_last_modified_user": "wcp-cluster-user-f06fd228-8088-4439-a9e6-26c90a829c57-d34133d7-0fdf-4c9d-abcf-df83bd050a59",
  "_revision": 0
}
```
<a id="13-policy-api-v1-infra-realized-state-realized-entities"></a>
### 13. /policy/api/v1/infra/realized-state/realized-entities

**HTTP Methods:** GET

**Explanation:**
NSX Policy API endpoint for resource management.

---

<a id="14-policy-api-v1-infra-lb-pools-default-svc-80-tcp-i3q14"></a>
### 14. /policy/api/v1/infra/lb-pools/default-svc_80_TCP_i3q14

**HTTP Methods:** DELETE, GET, PATCH

**Explanation:**
NSX Policy API endpoint for resource management.

---


**Sample Response Body (GET, from logs):**
```json
{
  "algorithm": "ROUND_ROBIN",
  "snat_translation": {
    "type": "LBSnatDisabled"
  },
  "min_active_members": 1,
  "resource_type": "LBPool",
  "id": "default-svc_80_TCP_i3q14",
  "display_name": "default-svc_80_TCP",
  "tags": [
    {
      "scope": "ncp/version",
      "tag": "1.2.0"
    },
    {
      "scope": "ncp/cluster",
      "tag": "f06fd228-8088-4439-a9e6-26c90a829c57"
    },
    {
      "scope": "ncp/project",
      "tag": "test-lb-50fedbb3"
    },
    {
      "scope": "external_id",
      "tag": "413462da-ad49-4afb-b755-88770ab32637"
    },
    {
      "scope": "ncp/service",
      "tag": "default-svc"
    },
    {
      "scope": "ncp/service_uid",
      "tag": "413462da-ad49-4afb-b755-88770ab32637"
    },
    {
      "scope": "ncp/service_port",
      "tag": "80"
    },
    {
      "scope": "ncp/service_port_protocol",
      "tag": "TCP"
    },
    {
      "scope": "ncp/created_for",
      "tag": "DLB"
    }
  ],
  "path": "/infra/lb-pools/default-svc_80_TCP_i3q14",
  "relative_path": "default-svc_80_TCP_i3q14",
  "parent_path": "/infra",
  "remote_path": "",
  "unique_id": "6ca05851-9a46-48f5-bcc7-49bc229f677b",
  "realization_id": "6ca05851-9a46-48f5-bcc7-49bc229f677b",
  "owner_id": "42495ba4-8c0b-49c9-b645-84cc39c2df30",
  "marked_for_delete": false,
  "overridden": false,
  "_system_owned": false,
  "_protection": "NOT_PROTECTED",
  "_create_time": 1760689221221,
  "_create_user": "wcp-cluster-user-f06fd228-8088-4439-a9e6-26c90a829c57-d34133d7-0fdf-4c9d-abcf-df83bd050a59",
  "_last_modified_time": 1760689221221,
  "_last_modified_user": "wcp-cluster-user-f06fd228-8088-4439-a9e6-26c90a829c57-d34133d7-0fdf-4c9d-abcf-df83bd050a59",
  "_revision": 0
}
```
<a id="15-policy-api-v1-infra-lb-pools-default-svc-80-udp-i3q14"></a>
### 15. /policy/api/v1/infra/lb-pools/default-svc_80_UDP_i3q14

**HTTP Methods:** DELETE, GET, PATCH

**Explanation:**
NSX Policy API endpoint for resource management.

---


**Sample Response Body (GET, from logs):**
```json
{
  "algorithm": "ROUND_ROBIN",
  "snat_translation": {
    "type": "LBSnatDisabled"
  },
  "min_active_members": 1,
  "resource_type": "LBPool",
  "id": "default-svc_80_UDP_i3q14",
  "display_name": "default-svc_80_UDP",
  "tags": [
    {
      "scope": "ncp/version",
      "tag": "1.2.0"
    },
    {
      "scope": "ncp/cluster",
      "tag": "f06fd228-8088-4439-a9e6-26c90a829c57"
    },
    {
      "scope": "ncp/project",
      "tag": "test-lb-50fedbb3"
    },
    {
      "scope": "external_id",
      "tag": "413462da-ad49-4afb-b755-88770ab32637"
    },
    {
      "scope": "ncp/service",
      "tag": "default-svc"
    },
    {
      "scope": "ncp/service_uid",
      "tag": "413462da-ad49-4afb-b755-88770ab32637"
    },
    {
      "scope": "ncp/service_port",
      "tag": "80"
    },
    {
      "scope": "ncp/service_port_protocol",
      "tag": "UDP"
    },
    {
      "scope": "ncp/created_for",
      "tag": "DLB"
    }
  ],
  "path": "/infra/lb-pools/default-svc_80_UDP_i3q14",
  "relative_path": "default-svc_80_UDP_i3q14",
  "parent_path": "/infra",
  "remote_path": "",
  "unique_id": "6229ca15-1607-47f3-9e74-ccea38d40745",
  "realization_id": "6229ca15-1607-47f3-9e74-ccea38d40745",
  "owner_id": "42495ba4-8c0b-49c9-b645-84cc39c2df30",
  "marked_for_delete": false,
  "overridden": false,
  "_system_owned": false,
  "_protection": "NOT_PROTECTED",
  "_create_time": 1760689223180,
  "_create_user": "wcp-cluster-user-f06fd228-8088-4439-a9e6-26c90a829c57-d34133d7-0fdf-4c9d-abcf-df83bd050a59",
  "_last_modified_time": 1760689223180,
  "_last_modified_user": "wcp-cluster-user-f06fd228-8088-4439-a9e6-26c90a829c57-d34133d7-0fdf-4c9d-abcf-df83bd050a59",
  "_revision": 0
}
```
<a id="16-policy-api-v1-infra-lb-pools-nsx-operator-8093-tcp-s6pir"></a>
### 16. /policy/api/v1/infra/lb-pools/nsx-operator_8093_TCP_s6pir

**HTTP Methods:** GET, PATCH

**Explanation:**
NSX Policy API endpoint for resource management.

---


**Sample Response Body (GET, from logs):**
```json
{
  "algorithm": "ROUND_ROBIN",
  "members": [
    {
      "display_name": "nsx-operator.nsx-ncp-85ddc8954f-bln7h",
      "ip_address": "172.26.0.2",
      "port": "8093",
      "admin_state": "ENABLED",
      "backup_member": false,
      "weight": 1
    }
  ],
  "snat_translation": {
    "type": "LBSnatDisabled"
  },
  "tcp_multiplexing_enabled": false,
  "tcp_multiplexing_number": 6,
  "min_active_members": 1,
  "resource_type": "LBPool",
  "id": "nsx-operator_8093_TCP_s6pir",
  "display_name": "nsx-operator_8093_TCP",
  "tags": [
    {
      "scope": "ncp/version",
      "tag": "1.2.0"
    },
    {
      "scope": "ncp/cluster",
      "tag": "f06fd228-8088-4439-a9e6-26c90a829c57"
    },
    {
      "scope": "ncp/project",
      "tag": "vmware-system-nsx"
    },
    {
      "scope": "external_id",
      "tag": "d17bbdc7-ea76-4ab8-8548-b432e7c51915"
    },
    {
      "scope": "ncp/service",
      "tag": "nsx-operator"
    },
    {
      "scope": "ncp/service_uid",
      "tag": "d17bbdc7-ea76-4ab8-8548-b432e7c51915"
    },
    {
      "scope": "ncp/service_port",
      "tag": "8093"
    },
    {
      "scope": "ncp/service_port_protocol",
      "tag": "TCP"
    },
    {
      "scope": "ncp/created_for",
      "tag": "DLB"
    }
  ],
  "path": "/infra/lb-pools/nsx-operator_8093_TCP_s6pir",
  "relative_path": "nsx-operator_8093_TCP_s6pir",
  "parent_path": "/infra",
  "remote_path": "",
  "unique_id": "738bc0cc-b290-4bdb-a279-2350fa5c3554",
  "realization_id": "738bc0cc-b290-4bdb-a279-2350fa5c3554",
  "owner_id": "42495ba4-8c0b-49c9-b645-84cc39c2df30",
  "marked_for_delete": false,
  "overridden": false,
  "_system_owned": false,
  "_protection": "NOT_PROTECTED",
  "_create_time": 1760503449084,
  "_create_user": "wcp-cluster-user-f06fd228-8088-4439-a9e6-26c90a829c57-d34133d7-0fdf-4c9d-abcf-df83bd050a59",
  "_last_modified_time": 1760688836101,
  "_last_modified_user": "wcp-cluster-user-f06fd228-8088-4439-a9e6-26c90a829c57-d34133d7-0fdf-4c9d-abcf-df83bd050a59",
  "_revision": 11
}
```
<a id="17-policy-api-v1-infra-lb-virtual-servers-tea-svc-80-tcp-39r0c"></a>
### 17. /policy/api/v1/infra/lb-virtual-servers/tea-svc_80_TCP_39r0c

**HTTP Methods:** DELETE, GET, PATCH

**Explanation:**
NSX Policy API endpoint for resource management.

---


**Sample Response Body (GET, from logs):**
```json
{
  "enabled": true,
  "ip_address": "172.24.94.103",
  "ports": [
    "80"
  ],
  "lb_service_path": "/infra/lb-services/clusterip_f06fd228-8088-4439-a9e6-26c90a829c57_dlb",
  "pool_path": "/infra/lb-pools/tea-svc_80_TCP_39r0c",
  "application_profile_path": "/infra/lb-app-profiles/default-tcp-lb-app-profile",
  "log_significant_event_only": false,
  "resource_type": "LBVirtualServer",
  "id": "tea-svc_80_TCP_39r0c",
  "display_name": "tea-svc_80_TCP",
  "tags": [
    {
      "scope": "ncp/version",
      "tag": "1.2.0"
    },
    {
      "scope": "ncp/cluster",
      "tag": "f06fd228-8088-4439-a9e6-26c90a829c57"
    },
    {
      "scope": "ncp/project",
      "tag": "test-lb-50fedbb3"
    },
    {
      "scope": "external_id",
      "tag": "f8572ed6-448c-4830-8e1d-5c00326ab97f"
    },
    {
      "scope": "ncp/service",
      "tag": "tea-svc"
    },
    {
      "scope": "ncp/service_uid",
      "tag": "f8572ed6-448c-4830-8e1d-5c00326ab97f"
    },
    {
      "scope": "ncp/service_port",
      "tag": "80"
    },
    {
      "scope": "ncp/service_port_protocol",
      "tag": "TCP"
    },
    {
      "scope": "ncp/created_for",
      "tag": "DLB"
    }
  ],
  "path": "/infra/lb-virtual-servers/tea-svc_80_TCP_39r0c",
  "relative_path": "tea-svc_80_TCP_39r0c",
  "parent_path": "/infra",
  "remote_path": "",
  "unique_id": "14368bcd-f319-4e35-b49d-d1bc2e96d11c",
  "realization_id": "14368bcd-f319-4e35-b49d-d1bc2e96d11c",
  "owner_id": "42495ba4-8c0b-49c9-b645-84cc39c2df30",
  "marked_for_delete": false,
  "overridden": false,
  "_system_owned": false,
  "_protection": "NOT_PROTECTED",
  "_create_time": 1760689214290,
  "_create_user": "wcp-cluster-user-f06fd228-8088-4439-a9e6-26c90a829c57-d34133d7-0fdf-4c9d-abcf-df83bd050a59",
  "_last_modified_time": 1760689214290,
  "_last_modified_user": "wcp-cluster-user-f06fd228-8088-4439-a9e6-26c90a829c57-d34133d7-0fdf-4c9d-abcf-df83bd050a59",
  "_revision": 0
}
```
<a id="18-policy-api-v1-infra-lb-virtual-servers-tea-svc-80-tcp-p5j45"></a>
### 18. /policy/api/v1/infra/lb-virtual-servers/tea-svc_80_TCP_p5j45

**HTTP Methods:** DELETE, GET, PATCH

**Explanation:**
NSX Policy API endpoint for resource management.

---


**Sample Response Body (GET, from logs):**
```json
{
  "enabled": true,
  "ip_address": "172.24.6.95",
  "ports": [
    "80"
  ],
  "lb_service_path": "/infra/lb-services/clusterip_f06fd228-8088-4439-a9e6-26c90a829c57_dlb",
  "pool_path": "/infra/lb-pools/tea-svc_80_TCP_p5j45",
  "application_profile_path": "/infra/lb-app-profiles/default-tcp-lb-app-profile",
  "log_significant_event_only": false,
  "resource_type": "LBVirtualServer",
  "id": "tea-svc_80_TCP_p5j45",
  "display_name": "tea-svc_80_TCP",
  "tags": [
    {
      "scope": "ncp/version",
      "tag": "1.2.0"
    },
    {
      "scope": "ncp/cluster",
      "tag": "f06fd228-8088-4439-a9e6-26c90a829c57"
    },
    {
      "scope": "ncp/project",
      "tag": "test-ipaddress-allocation-40d5699d"
    },
    {
      "scope": "external_id",
      "tag": "55c7492b-a285-4cba-9d71-bb6305d8c977"
    },
    {
      "scope": "ncp/service",
      "tag": "tea-svc"
    },
    {
      "scope": "ncp/service_uid",
      "tag": "55c7492b-a285-4cba-9d71-bb6305d8c977"
    },
    {
      "scope": "ncp/service_port",
      "tag": "80"
    },
    {
      "scope": "ncp/service_port_protocol",
      "tag": "TCP"
    },
    {
      "scope": "ncp/created_for",
      "tag": "DLB"
    }
  ],
  "path": "/infra/lb-virtual-servers/tea-svc_80_TCP_p5j45",
  "relative_path": "tea-svc_80_TCP_p5j45",
  "parent_path": "/infra",
  "remote_path": "",
  "unique_id": "736e5523-3cb9-4123-87fc-6b0c37aa5fb3",
  "realization_id": "736e5523-3cb9-4123-87fc-6b0c37aa5fb3",
  "owner_id": "42495ba4-8c0b-49c9-b645-84cc39c2df30",
  "marked_for_delete": false,
  "overridden": false,
  "_system_owned": false,
  "_protection": "NOT_PROTECTED",
  "_create_time": 1760689105706,
  "_create_user": "wcp-cluster-user-f06fd228-8088-4439-a9e6-26c90a829c57-d34133d7-0fdf-4c9d-abcf-df83bd050a59",
  "_last_modified_time": 1760689105706,
  "_last_modified_user": "wcp-cluster-user-f06fd228-8088-4439-a9e6-26c90a829c57-d34133d7-0fdf-4c9d-abcf-df83bd050a59",
  "_revision": 0
}
```
<a id="19-policy-api-v1-infra-lb-virtual-servers-tea-svc-80-udp-39r0c"></a>
### 19. /policy/api/v1/infra/lb-virtual-servers/tea-svc_80_UDP_39r0c

**HTTP Methods:** DELETE, GET, PATCH

**Explanation:**
NSX Policy API endpoint for resource management.

---


**Sample Response Body (GET, from logs):**
```json
{
  "enabled": true,
  "ip_address": "172.24.94.103",
  "ports": [
    "80"
  ],
  "lb_service_path": "/infra/lb-services/clusterip_f06fd228-8088-4439-a9e6-26c90a829c57_dlb",
  "pool_path": "/infra/lb-pools/tea-svc_80_UDP_39r0c",
  "application_profile_path": "/infra/lb-app-profiles/default-udp-lb-app-profile",
  "log_significant_event_only": false,
  "resource_type": "LBVirtualServer",
  "id": "tea-svc_80_UDP_39r0c",
  "display_name": "tea-svc_80_UDP",
  "tags": [
    {
      "scope": "ncp/version",
      "tag": "1.2.0"
    },
    {
      "scope": "ncp/cluster",
      "tag": "f06fd228-8088-4439-a9e6-26c90a829c57"
    },
    {
      "scope": "ncp/project",
      "tag": "test-lb-50fedbb3"
    },
    {
      "scope": "external_id",
      "tag": "f8572ed6-448c-4830-8e1d-5c00326ab97f"
    },
    {
      "scope": "ncp/service",
      "tag": "tea-svc"
    },
    {
      "scope": "ncp/service_uid",
      "tag": "f8572ed6-448c-4830-8e1d-5c00326ab97f"
    },
    {
      "scope": "ncp/service_port",
      "tag": "80"
    },
    {
      "scope": "ncp/service_port_protocol",
      "tag": "UDP"
    },
    {
      "scope": "ncp/created_for",
      "tag": "DLB"
    }
  ],
  "path": "/infra/lb-virtual-servers/tea-svc_80_UDP_39r0c",
  "relative_path": "tea-svc_80_UDP_39r0c",
  "parent_path": "/infra",
  "remote_path": "",
  "unique_id": "991ac0cd-b39d-491b-bd0d-e54d046a361c",
  "realization_id": "991ac0cd-b39d-491b-bd0d-e54d046a361c",
  "owner_id": "42495ba4-8c0b-49c9-b645-84cc39c2df30",
  "marked_for_delete": false,
  "overridden": false,
  "_system_owned": false,
  "_protection": "NOT_PROTECTED",
  "_create_time": 1760689216651,
  "_create_user": "wcp-cluster-user-f06fd228-8088-4439-a9e6-26c90a829c57-d34133d7-0fdf-4c9d-abcf-df83bd050a59",
  "_last_modified_time": 1760689216651,
  "_last_modified_user": "wcp-cluster-user-f06fd228-8088-4439-a9e6-26c90a829c57-d34133d7-0fdf-4c9d-abcf-df83bd050a59",
  "_revision": 0
}
```
<a id="20-policy-api-v1-infra-lb-virtual-servers-kube-dns-53-tcp-hof1c"></a>
### 20. /policy/api/v1/infra/lb-virtual-servers/kube-dns_53_TCP_hof1c

**HTTP Methods:** GET, PATCH

**Explanation:**
NSX Policy API endpoint for resource management.

---


**Sample Response Body (GET, from logs):**
```json
{
  "enabled": true,
  "ip_address": "172.24.0.10",
  "ports": [
    "53"
  ],
  "access_log_enabled": false,
  "lb_service_path": "/infra/lb-services/clusterip_f06fd228-8088-4439-a9e6-26c90a829c57_dlb",
  "pool_path": "/infra/lb-pools/kube-dns_53_TCP_hof1c",
  "application_profile_path": "/infra/lb-app-profiles/default-tcp-lb-app-profile",
  "log_significant_event_only": false,
  "resource_type": "LBVirtualServer",
  "id": "kube-dns_53_TCP_hof1c",
  "display_name": "kube-dns_53_TCP",
  "tags": [
    {
      "scope": "ncp/version",
      "tag": "1.2.0"
    },
    {
      "scope": "ncp/cluster",
      "tag": "f06fd228-8088-4439-a9e6-26c90a829c57"
    },
    {
      "scope": "ncp/project",
      "tag": "kube-system"
    },
    {
      "scope": "external_id",
      "tag": "e3afa8bf-6257-472a-85da-4e03843a15a1"
    },
    {
      "scope": "ncp/service",
      "tag": "kube-dns"
    },
    {
      "scope": "ncp/service_uid",
      "tag": "e3afa8bf-6257-472a-85da-4e03843a15a1"
    },
    {
      "scope": "ncp/service_port",
      "tag": "53"
    },
    {
      "scope": "ncp/service_port_protocol",
      "tag": "TCP"
    },
    {
      "scope": "ncp/created_for",
      "tag": "DLB"
    }
  ],
  "path": "/infra/lb-virtual-servers/kube-dns_53_TCP_hof1c",
  "relative_path": "kube-dns_53_TCP_hof1c",
  "parent_path": "/infra",
  "remote_path": "",
  "unique_id": "32c52452-e8d6-4915-a580-2087d93ad19b",
  "realization_id": "32c52452-e8d6-4915-a580-2087d93ad19b",
  "owner_id": "42495ba4-8c0b-49c9-b645-84cc39c2df30",
  "marked_for_delete": false,
  "overridden": false,
  "_system_owned": false,
  "_protection": "NOT_PROTECTED",
  "_create_time": 1760503471322,
  "_create_user": "wcp-cluster-user-f06fd228-8088-4439-a9e6-26c90a829c57-d34133d7-0fdf-4c9d-abcf-df83bd050a59",
  "_last_modified_time": 1760503622175,
  "_last_modified_user": "wcp-cluster-user-f06fd228-8088-4439-a9e6-26c90a829c57-d34133d7-0fdf-4c9d-abcf-df83bd050a59",
  "_revision": 1
}
```
<a id="21-policy-api-v1-infra-lb-virtual-servers-kube-dns-53-udp-hof1c"></a>
### 21. /policy/api/v1/infra/lb-virtual-servers/kube-dns_53_UDP_hof1c

**HTTP Methods:** GET, PATCH

**Explanation:**
NSX Policy API endpoint for resource management.

---


**Sample Response Body (GET, from logs):**
```json
{
  "enabled": true,
  "ip_address": "172.24.0.10",
  "ports": [
    "53"
  ],
  "access_log_enabled": false,
  "lb_service_path": "/infra/lb-services/clusterip_f06fd228-8088-4439-a9e6-26c90a829c57_dlb",
  "pool_path": "/infra/lb-pools/kube-dns_53_UDP_hof1c",
  "application_profile_path": "/infra/lb-app-profiles/default-udp-lb-app-profile",
  "log_significant_event_only": false,
  "resource_type": "LBVirtualServer",
  "id": "kube-dns_53_UDP_hof1c",
  "display_name": "kube-dns_53_UDP",
  "tags": [
    {
      "scope": "ncp/version",
      "tag": "1.2.0"
    },
    {
      "scope": "ncp/cluster",
      "tag": "f06fd228-8088-4439-a9e6-26c90a829c57"
    },
    {
      "scope": "ncp/project",
      "tag": "kube-system"
    },
    {
      "scope": "external_id",
      "tag": "e3afa8bf-6257-472a-85da-4e03843a15a1"
    },
    {
      "scope": "ncp/service",
      "tag": "kube-dns"
    },
    {
      "scope": "ncp/service_uid",
      "tag": "e3afa8bf-6257-472a-85da-4e03843a15a1"
    },
    {
      "scope": "ncp/service_port",
      "tag": "53"
    },
    {
      "scope": "ncp/service_port_protocol",
      "tag": "UDP"
    },
    {
      "scope": "ncp/created_for",
      "tag": "DLB"
    }
  ],
  "path": "/infra/lb-virtual-servers/kube-dns_53_UDP_hof1c",
  "relative_path": "kube-dns_53_UDP_hof1c",
  "parent_path": "/infra",
  "remote_path": "",
  "unique_id": "72efd2eb-7040-4b43-b3dc-a7c8d9291506",
  "realization_id": "72efd2eb-7040-4b43-b3dc-a7c8d9291506",
  "owner_id": "42495ba4-8c0b-49c9-b645-84cc39c2df30",
  "marked_for_delete": false,
  "overridden": false,
  "_system_owned": false,
  "_protection": "NOT_PROTECTED",
  "_create_time": 1760503468598,
  "_create_user": "wcp-cluster-user-f06fd228-8088-4439-a9e6-26c90a829c57-d34133d7-0fdf-4c9d-abcf-df83bd050a59",
  "_last_modified_time": 1760503622020,
  "_last_modified_user": "wcp-cluster-user-f06fd228-8088-4439-a9e6-26c90a829c57-d34133d7-0fdf-4c9d-abcf-df83bd050a59",
  "_revision": 1
}
```
<a id="22-policy-api-v1-infra-lb-virtual-servers-coffee-svc-80-tcp-cnml1"></a>
### 22. /policy/api/v1/infra/lb-virtual-servers/coffee-svc_80_TCP_cnml1

**HTTP Methods:** DELETE, GET, PATCH

**Explanation:**
NSX Policy API endpoint for resource management.

---


**Sample Response Body (GET, from logs):**
```json
{
  "enabled": true,
  "ip_address": "172.24.47.198",
  "ports": [
    "80"
  ],
  "lb_service_path": "/infra/lb-services/clusterip_f06fd228-8088-4439-a9e6-26c90a829c57_dlb",
  "pool_path": "/infra/lb-pools/coffee-svc_80_TCP_cnml1",
  "application_profile_path": "/infra/lb-app-profiles/default-tcp-lb-app-profile",
  "log_significant_event_only": false,
  "resource_type": "LBVirtualServer",
  "id": "coffee-svc_80_TCP_cnml1",
  "display_name": "coffee-svc_80_TCP",
  "tags": [
    {
      "scope": "ncp/version",
      "tag": "1.2.0"
    },
    {
      "scope": "ncp/cluster",
      "tag": "f06fd228-8088-4439-a9e6-26c90a829c57"
    },
    {
      "scope": "ncp/project",
      "tag": "test-lb-50fedbb3"
    },
    {
      "scope": "external_id",
      "tag": "75a666bb-cb7a-45dd-a6a6-6d0f0e7d685e"
    },
    {
      "scope": "ncp/service",
      "tag": "coffee-svc"
    },
    {
      "scope": "ncp/service_uid",
      "tag": "75a666bb-cb7a-45dd-a6a6-6d0f0e7d685e"
    },
    {
      "scope": "ncp/service_port",
      "tag": "80"
    },
    {
      "scope": "ncp/service_port_protocol",
      "tag": "TCP"
    },
    {
      "scope": "ncp/created_for",
      "tag": "DLB"
    }
  ],
  "path": "/infra/lb-virtual-servers/coffee-svc_80_TCP_cnml1",
  "relative_path": "coffee-svc_80_TCP_cnml1",
  "parent_path": "/infra",
  "remote_path": "",
  "unique_id": "494d1655-3c97-4bb9-8013-04861d91d82c",
  "realization_id": "494d1655-3c97-4bb9-8013-04861d91d82c",
  "owner_id": "42495ba4-8c0b-49c9-b645-84cc39c2df30",
  "marked_for_delete": false,
  "overridden": false,
  "_system_owned": false,
  "_protection": "NOT_PROTECTED",
  "_create_time": 1760689289918,
  "_create_user": "wcp-cluster-user-f06fd228-8088-4439-a9e6-26c90a829c57-d34133d7-0fdf-4c9d-abcf-df83bd050a59",
  "_last_modified_time": 1760689289918,
  "_last_modified_user": "wcp-cluster-user-f06fd228-8088-4439-a9e6-26c90a829c57-d34133d7-0fdf-4c9d-abcf-df83bd050a59",
  "_revision": 0
}
```
<a id="23-policy-api-v1-infra-lb-pools-prevpc-loadbalancer-8080-tcp-j7n9u"></a>
### 23. /policy/api/v1/infra/lb-pools/prevpc-loadbalancer_8080_TCP_j7n9u

**HTTP Methods:** DELETE, GET, PATCH

**Explanation:**
NSX Policy API endpoint for resource management.

---


**Sample Response Body (GET, from logs):**
```json
{
  "algorithm": "ROUND_ROBIN",
  "snat_translation": {
    "type": "LBSnatDisabled"
  },
  "min_active_members": 1,
  "resource_type": "LBPool",
  "id": "prevpc-loadbalancer_8080_TCP_j7n9u",
  "display_name": "prevpc-loadbalancer_8080_TCP",
  "tags": [
    {
      "scope": "ncp/version",
      "tag": "1.2.0"
    },
    {
      "scope": "ncp/cluster",
      "tag": "f06fd228-8088-4439-a9e6-26c90a829c57"
    },
    {
      "scope": "ncp/project",
      "tag": "test-prevpc-8f1a464f"
    },
    {
      "scope": "external_id",
      "tag": "64af7175-c755-4315-9cf7-28c21bd6fc0a"
    },
    {
      "scope": "ncp/service",
      "tag": "prevpc-loadbalancer"
    },
    {
      "scope": "ncp/service_uid",
      "tag": "64af7175-c755-4315-9cf7-28c21bd6fc0a"
    },
    {
      "scope": "ncp/service_port",
      "tag": "8080"
    },
    {
      "scope": "ncp/service_port_protocol",
      "tag": "TCP"
    },
    {
      "scope": "ncp/created_for",
      "tag": "DLB"
    }
  ],
  "path": "/infra/lb-pools/prevpc-loadbalancer_8080_TCP_j7n9u",
  "relative_path": "prevpc-loadbalancer_8080_TCP_j7n9u",
  "parent_path": "/infra",
  "remote_path": "",
  "unique_id": "77ee0fcc-9e0a-4afd-94fe-f1026e15f741",
  "realization_id": "77ee0fcc-9e0a-4afd-94fe-f1026e15f741",
  "owner_id": "42495ba4-8c0b-49c9-b645-84cc39c2df30",
  "marked_for_delete": false,
  "overridden": false,
  "_system_owned": false,
  "_protection": "NOT_PROTECTED",
  "_create_time": 1760690632424,
  "_create_user": "wcp-cluster-user-f06fd228-8088-4439-a9e6-26c90a829c57-d34133d7-0fdf-4c9d-abcf-df83bd050a59",
  "_last_modified_time": 1760690632424,
  "_last_modified_user": "wcp-cluster-user-f06fd228-8088-4439-a9e6-26c90a829c57-d34133d7-0fdf-4c9d-abcf-df83bd050a59",
  "_revision": 0
}
```
<a id="24-policy-api-v1-infra-lb-pools-test-service-1bcb333c-80-tcp-9rdbd"></a>
### 24. /policy/api/v1/infra/lb-pools/test-service-1bcb333c_80_TCP_9rdbd

**HTTP Methods:** DELETE, GET, PATCH

**Explanation:**
NSX Policy API endpoint for resource management.

---


**Sample Response Body (GET, from logs):**
```json
{
  "algorithm": "ROUND_ROBIN",
  "snat_translation": {
    "type": "LBSnatDisabled"
  },
  "min_active_members": 1,
  "resource_type": "LBPool",
  "id": "test-service-1bcb333c_80_TCP_9rdbd",
  "display_name": "test-service-1bcb333c_80_TCP",
  "tags": [
    {
      "scope": "ncp/version",
      "tag": "1.2.0"
    },
    {
      "scope": "ncp/cluster",
      "tag": "f06fd228-8088-4439-a9e6-26c90a829c57"
    },
    {
      "scope": "ncp/project",
      "tag": "test-service-sync-f1d17bff"
    },
    {
      "scope": "external_id",
      "tag": "dbf60d60-30b2-4792-9bf0-ba4ed1235cb6"
    },
    {
      "scope": "ncp/service",
      "tag": "test-service-1bcb333c"
    },
    {
      "scope": "ncp/service_uid",
      "tag": "dbf60d60-30b2-4792-9bf0-ba4ed1235cb6"
    },
    {
      "scope": "ncp/service_port",
      "tag": "80"
    },
    {
      "scope": "ncp/service_port_protocol",
      "tag": "TCP"
    },
    {
      "scope": "ncp/created_for",
      "tag": "DLB"
    }
  ],
  "path": "/infra/lb-pools/test-service-1bcb333c_80_TCP_9rdbd",
  "relative_path": "test-service-1bcb333c_80_TCP_9rdbd",
  "parent_path": "/infra",
  "remote_path": "",
  "unique_id": "526b80e8-2b93-44c5-b628-860496fe27aa",
  "realization_id": "526b80e8-2b93-44c5-b628-860496fe27aa",
  "owner_id": "42495ba4-8c0b-49c9-b645-84cc39c2df30",
  "marked_for_delete": false,
  "overridden": false,
  "_system_owned": false,
  "_protection": "NOT_PROTECTED",
  "_create_time": 1760688957409,
  "_create_user": "wcp-cluster-user-f06fd228-8088-4439-a9e6-26c90a829c57-d34133d7-0fdf-4c9d-abcf-df83bd050a59",
  "_last_modified_time": 1760688957409,
  "_last_modified_user": "wcp-cluster-user-f06fd228-8088-4439-a9e6-26c90a829c57-d34133d7-0fdf-4c9d-abcf-df83bd050a59",
  "_revision": 0
}
```
<a id="25-policy-api-v1-infra-lb-pools-test-service-da1e3736-80-tcp-2bcu3"></a>
### 25. /policy/api/v1/infra/lb-pools/test-service-da1e3736_80_TCP_2bcu3

**HTTP Methods:** DELETE, GET, PATCH

**Explanation:**
NSX Policy API endpoint for resource management.

---


**Sample Response Body (GET, from logs):**
```json
{
  "algorithm": "ROUND_ROBIN",
  "snat_translation": {
    "type": "LBSnatDisabled"
  },
  "min_active_members": 1,
  "resource_type": "LBPool",
  "id": "test-service-da1e3736_80_TCP_2bcu3",
  "display_name": "test-service-da1e3736_80_TCP",
  "tags": [
    {
      "scope": "ncp/version",
      "tag": "1.2.0"
    },
    {
      "scope": "ncp/cluster",
      "tag": "f06fd228-8088-4439-a9e6-26c90a829c57"
    },
    {
      "scope": "ncp/project",
      "tag": "test-ingress-sync-73e76bf1"
    },
    {
      "scope": "external_id",
      "tag": "6d949a82-837a-4062-9914-4138a1bf61ca"
    },
    {
      "scope": "ncp/service",
      "tag": "test-service-da1e3736"
    },
    {
      "scope": "ncp/service_uid",
      "tag": "6d949a82-837a-4062-9914-4138a1bf61ca"
    },
    {
      "scope": "ncp/service_port",
      "tag": "80"
    },
    {
      "scope": "ncp/service_port_protocol",
      "tag": "TCP"
    },
    {
      "scope": "ncp/created_for",
      "tag": "DLB"
    }
  ],
  "path": "/infra/lb-pools/test-service-da1e3736_80_TCP_2bcu3",
  "relative_path": "test-service-da1e3736_80_TCP_2bcu3",
  "parent_path": "/infra",
  "remote_path": "",
  "unique_id": "ed5a41eb-ae91-4e8d-9299-743e0041585a",
  "realization_id": "ed5a41eb-ae91-4e8d-9299-743e0041585a",
  "owner_id": "42495ba4-8c0b-49c9-b645-84cc39c2df30",
  "marked_for_delete": false,
  "overridden": false,
  "_system_owned": false,
  "_protection": "NOT_PROTECTED",
  "_create_time": 1760689048500,
  "_create_user": "wcp-cluster-user-f06fd228-8088-4439-a9e6-26c90a829c57-d34133d7-0fdf-4c9d-abcf-df83bd050a59",
  "_last_modified_time": 1760689048500,
  "_last_modified_user": "wcp-cluster-user-f06fd228-8088-4439-a9e6-26c90a829c57-d34133d7-0fdf-4c9d-abcf-df83bd050a59",
  "_revision": 0
}
```
<a id="26-policy-api-v1-infra-lb-virtual-servers-default-svc-80-tcp-i3q14"></a>
### 26. /policy/api/v1/infra/lb-virtual-servers/default-svc_80_TCP_i3q14

**HTTP Methods:** DELETE, GET, PATCH

**Explanation:**
NSX Policy API endpoint for resource management.

---


**Sample Response Body (GET, from logs):**
```json
{
  "enabled": true,
  "ip_address": "172.24.151.216",
  "ports": [
    "80"
  ],
  "lb_service_path": "/infra/lb-services/clusterip_f06fd228-8088-4439-a9e6-26c90a829c57_dlb",
  "pool_path": "/infra/lb-pools/default-svc_80_TCP_i3q14",
  "application_profile_path": "/infra/lb-app-profiles/default-tcp-lb-app-profile",
  "log_significant_event_only": false,
  "resource_type": "LBVirtualServer",
  "id": "default-svc_80_TCP_i3q14",
  "display_name": "default-svc_80_TCP",
  "tags": [
    {
      "scope": "ncp/version",
      "tag": "1.2.0"
    },
    {
      "scope": "ncp/cluster",
      "tag": "f06fd228-8088-4439-a9e6-26c90a829c57"
    },
    {
      "scope": "ncp/project",
      "tag": "test-lb-50fedbb3"
    },
    {
      "scope": "external_id",
      "tag": "413462da-ad49-4afb-b755-88770ab32637"
    },
    {
      "scope": "ncp/service",
      "tag": "default-svc"
    },
    {
      "scope": "ncp/service_uid",
      "tag": "413462da-ad49-4afb-b755-88770ab32637"
    },
    {
      "scope": "ncp/service_port",
      "tag": "80"
    },
    {
      "scope": "ncp/service_port_protocol",
      "tag": "TCP"
    },
    {
      "scope": "ncp/created_for",
      "tag": "DLB"
    }
  ],
  "path": "/infra/lb-virtual-servers/default-svc_80_TCP_i3q14",
  "relative_path": "default-svc_80_TCP_i3q14",
  "parent_path": "/infra",
  "remote_path": "",
  "unique_id": "eed6caf2-349f-4772-a2e1-ef697ac33af1",
  "realization_id": "eed6caf2-349f-4772-a2e1-ef697ac33af1",
  "owner_id": "42495ba4-8c0b-49c9-b645-84cc39c2df30",
  "marked_for_delete": false,
  "overridden": false,
  "_system_owned": false,
  "_protection": "NOT_PROTECTED",
  "_create_time": 1760689222809,
  "_create_user": "wcp-cluster-user-f06fd228-8088-4439-a9e6-26c90a829c57-d34133d7-0fdf-4c9d-abcf-df83bd050a59",
  "_last_modified_time": 1760689222809,
  "_last_modified_user": "wcp-cluster-user-f06fd228-8088-4439-a9e6-26c90a829c57-d34133d7-0fdf-4c9d-abcf-df83bd050a59",
  "_revision": 0
}
```
<a id="27-policy-api-v1-infra-lb-virtual-servers-default-svc-80-udp-i3q14"></a>
### 27. /policy/api/v1/infra/lb-virtual-servers/default-svc_80_UDP_i3q14

**HTTP Methods:** DELETE, GET, PATCH

**Explanation:**
NSX Policy API endpoint for resource management.

---


**Sample Response Body (GET, from logs):**
```json
{
  "enabled": true,
  "ip_address": "172.24.151.216",
  "ports": [
    "80"
  ],
  "lb_service_path": "/infra/lb-services/clusterip_f06fd228-8088-4439-a9e6-26c90a829c57_dlb",
  "pool_path": "/infra/lb-pools/default-svc_80_UDP_i3q14",
  "application_profile_path": "/infra/lb-app-profiles/default-udp-lb-app-profile",
  "log_significant_event_only": false,
  "resource_type": "LBVirtualServer",
  "id": "default-svc_80_UDP_i3q14",
  "display_name": "default-svc_80_UDP",
  "tags": [
    {
      "scope": "ncp/version",
      "tag": "1.2.0"
    },
    {
      "scope": "ncp/cluster",
      "tag": "f06fd228-8088-4439-a9e6-26c90a829c57"
    },
    {
      "scope": "ncp/project",
      "tag": "test-lb-50fedbb3"
    },
    {
      "scope": "external_id",
      "tag": "413462da-ad49-4afb-b755-88770ab32637"
    },
    {
      "scope": "ncp/service",
      "tag": "default-svc"
    },
    {
      "scope": "ncp/service_uid",
      "tag": "413462da-ad49-4afb-b755-88770ab32637"
    },
    {
      "scope": "ncp/service_port",
      "tag": "80"
    },
    {
      "scope": "ncp/service_port_protocol",
      "tag": "UDP"
    },
    {
      "scope": "ncp/created_for",
      "tag": "DLB"
    }
  ],
  "path": "/infra/lb-virtual-servers/default-svc_80_UDP_i3q14",
  "relative_path": "default-svc_80_UDP_i3q14",
  "parent_path": "/infra",
  "remote_path": "",
  "unique_id": "daa42f26-a864-4a82-9165-53bb403acd4c",
  "realization_id": "daa42f26-a864-4a82-9165-53bb403acd4c",
  "owner_id": "42495ba4-8c0b-49c9-b645-84cc39c2df30",
  "marked_for_delete": false,
  "overridden": false,
  "_system_owned": false,
  "_protection": "NOT_PROTECTED",
  "_create_time": 1760689224356,
  "_create_user": "wcp-cluster-user-f06fd228-8088-4439-a9e6-26c90a829c57-d34133d7-0fdf-4c9d-abcf-df83bd050a59",
  "_last_modified_time": 1760689224356,
  "_last_modified_user": "wcp-cluster-user-f06fd228-8088-4439-a9e6-26c90a829c57-d34133d7-0fdf-4c9d-abcf-df83bd050a59",
  "_revision": 0
}
```
<a id="28-policy-api-v1-infra-lb-virtual-servers-kube-dns-lb-53-tcp-aajir"></a>
### 28. /policy/api/v1/infra/lb-virtual-servers/kube-dns-lb_53_TCP_aajir

**HTTP Methods:** GET, PATCH

**Explanation:**
NSX Policy API endpoint for resource management.

---


**Sample Response Body (GET, from logs):**
```json
{
  "enabled": true,
  "ip_address": "172.24.52.234",
  "ports": [
    "53"
  ],
  "access_log_enabled": false,
  "lb_service_path": "/infra/lb-services/clusterip_f06fd228-8088-4439-a9e6-26c90a829c57_dlb",
  "pool_path": "/infra/lb-pools/kube-dns-lb_53_TCP_aajir",
  "application_profile_path": "/infra/lb-app-profiles/default-tcp-lb-app-profile",
  "log_significant_event_only": false,
  "resource_type": "LBVirtualServer",
  "id": "kube-dns-lb_53_TCP_aajir",
  "display_name": "kube-dns-lb_53_TCP",
  "tags": [
    {
      "scope": "ncp/version",
      "tag": "1.2.0"
    },
    {
      "scope": "ncp/cluster",
      "tag": "f06fd228-8088-4439-a9e6-26c90a829c57"
    },
    {
      "scope": "ncp/project",
      "tag": "kube-system"
    },
    {
      "scope": "external_id",
      "tag": "555f1d78-69f6-4b28-9bea-10467cf5e388"
    },
    {
      "scope": "ncp/service",
      "tag": "kube-dns-lb"
    },
    {
      "scope": "ncp/service_uid",
      "tag": "555f1d78-69f6-4b28-9bea-10467cf5e388"
    },
    {
      "scope": "ncp/service_port",
      "tag": "53"
    },
    {
      "scope": "ncp/service_port_protocol",
      "tag": "TCP"
    },
    {
      "scope": "ncp/created_for",
      "tag": "DLB"
    }
  ],
  "path": "/infra/lb-virtual-servers/kube-dns-lb_53_TCP_aajir",
  "relative_path": "kube-dns-lb_53_TCP_aajir",
  "parent_path": "/infra",
  "remote_path": "",
  "unique_id": "e4dbf645-4608-4039-bdfd-82c0927c49ce",
  "realization_id": "e4dbf645-4608-4039-bdfd-82c0927c49ce",
  "owner_id": "42495ba4-8c0b-49c9-b645-84cc39c2df30",
  "marked_for_delete": false,
  "overridden": false,
  "_system_owned": false,
  "_protection": "NOT_PROTECTED",
  "_create_time": 1760503448911,
  "_create_user": "wcp-cluster-user-f06fd228-8088-4439-a9e6-26c90a829c57-d34133d7-0fdf-4c9d-abcf-df83bd050a59",
  "_last_modified_time": 1760503616705,
  "_last_modified_user": "wcp-cluster-user-f06fd228-8088-4439-a9e6-26c90a829c57-d34133d7-0fdf-4c9d-abcf-df83bd050a59",
  "_revision": 1
}
```
<a id="29-policy-api-v1-infra-lb-virtual-servers-kube-dns-lb-53-udp-aajir"></a>
### 29. /policy/api/v1/infra/lb-virtual-servers/kube-dns-lb_53_UDP_aajir

**HTTP Methods:** GET, PATCH

**Explanation:**
NSX Policy API endpoint for resource management.

---


**Sample Response Body (GET, from logs):**
```json
{
  "enabled": true,
  "ip_address": "172.24.52.234",
  "ports": [
    "53"
  ],
  "access_log_enabled": false,
  "lb_service_path": "/infra/lb-services/clusterip_f06fd228-8088-4439-a9e6-26c90a829c57_dlb",
  "pool_path": "/infra/lb-pools/kube-dns-lb_53_UDP_aajir",
  "application_profile_path": "/infra/lb-app-profiles/default-udp-lb-app-profile",
  "log_significant_event_only": false,
  "resource_type": "LBVirtualServer",
  "id": "kube-dns-lb_53_UDP_aajir",
  "display_name": "kube-dns-lb_53_UDP",
  "tags": [
    {
      "scope": "ncp/version",
      "tag": "1.2.0"
    },
    {
      "scope": "ncp/cluster",
      "tag": "f06fd228-8088-4439-a9e6-26c90a829c57"
    },
    {
      "scope": "ncp/project",
      "tag": "kube-system"
    },
    {
      "scope": "external_id",
      "tag": "555f1d78-69f6-4b28-9bea-10467cf5e388"
    },
    {
      "scope": "ncp/service",
      "tag": "kube-dns-lb"
    },
    {
      "scope": "ncp/service_uid",
      "tag": "555f1d78-69f6-4b28-9bea-10467cf5e388"
    },
    {
      "scope": "ncp/service_port",
      "tag": "53"
    },
    {
      "scope": "ncp/service_port_protocol",
      "tag": "UDP"
    },
    {
      "scope": "ncp/created_for",
      "tag": "DLB"
    }
  ],
  "path": "/infra/lb-virtual-servers/kube-dns-lb_53_UDP_aajir",
  "relative_path": "kube-dns-lb_53_UDP_aajir",
  "parent_path": "/infra",
  "remote_path": "",
  "unique_id": "09c86652-19bb-4e1b-a370-3ff6bb7dc00d",
  "realization_id": "09c86652-19bb-4e1b-a370-3ff6bb7dc00d",
  "owner_id": "42495ba4-8c0b-49c9-b645-84cc39c2df30",
  "marked_for_delete": false,
  "overridden": false,
  "_system_owned": false,
  "_protection": "NOT_PROTECTED",
  "_create_time": 1760503445871,
  "_create_user": "wcp-cluster-user-f06fd228-8088-4439-a9e6-26c90a829c57-d34133d7-0fdf-4c9d-abcf-df83bd050a59",
  "_last_modified_time": 1760503615609,
  "_last_modified_user": "wcp-cluster-user-f06fd228-8088-4439-a9e6-26c90a829c57-d34133d7-0fdf-4c9d-abcf-df83bd050a59",
  "_revision": 1
}
```
<a id="30-policy-api-v1-infra-lb-virtual-servers-kubernetes-443-tcp-6mqcw"></a>
### 30. /policy/api/v1/infra/lb-virtual-servers/kubernetes_443_TCP_6mqcw

**HTTP Methods:** GET, PATCH

**Explanation:**
NSX Policy API endpoint for resource management.

---


**Sample Response Body (GET, from logs):**
```json
{
  "enabled": true,
  "ip_address": "172.24.0.1",
  "ports": [
    "443"
  ],
  "access_log_enabled": false,
  "lb_service_path": "/infra/lb-services/clusterip_f06fd228-8088-4439-a9e6-26c90a829c57_dlb",
  "pool_path": "/infra/lb-pools/kubernetes_443_TCP_6mqcw",
  "application_profile_path": "/infra/lb-app-profiles/default-tcp-lb-app-profile",
  "log_significant_event_only": false,
  "resource_type": "LBVirtualServer",
  "id": "kubernetes_443_TCP_6mqcw",
  "display_name": "kubernetes_443_TCP",
  "tags": [
    {
      "scope": "ncp/version",
      "tag": "1.2.0"
    },
    {
      "scope": "ncp/cluster",
      "tag": "f06fd228-8088-4439-a9e6-26c90a829c57"
    },
    {
      "scope": "ncp/project",
      "tag": "default"
    },
    {
      "scope": "external_id",
      "tag": "5263fbbb-721f-4757-9adc-07a4c89d4a96"
    },
    {
      "scope": "ncp/service",
      "tag": "kubernetes"
    },
    {
      "scope": "ncp/service_uid",
      "tag": "5263fbbb-721f-4757-9adc-07a4c89d4a96"
    },
    {
      "scope": "ncp/service_port",
      "tag": "443"
    },
    {
      "scope": "ncp/service_port_protocol",
      "tag": "TCP"
    },
    {
      "scope": "ncp/created_for",
      "tag": "DLB"
    }
  ],
  "path": "/infra/lb-virtual-servers/kubernetes_443_TCP_6mqcw",
  "relative_path": "kubernetes_443_TCP_6mqcw",
  "parent_path": "/infra",
  "remote_path": "",
  "unique_id": "74b6fda6-c96a-4f13-a8d4-84ecd6e0eca9",
  "realization_id": "74b6fda6-c96a-4f13-a8d4-84ecd6e0eca9",
  "owner_id": "42495ba4-8c0b-49c9-b645-84cc39c2df30",
  "marked_for_delete": false,
  "overridden": false,
  "_system_owned": false,
  "_protection": "NOT_PROTECTED",
  "_create_time": 1760503467040,
  "_create_user": "wcp-cluster-user-f06fd228-8088-4439-a9e6-26c90a829c57-d34133d7-0fdf-4c9d-abcf-df83bd050a59",
  "_last_modified_time": 1760503616738,
  "_last_modified_user": "wcp-cluster-user-f06fd228-8088-4439-a9e6-26c90a829c57-d34133d7-0fdf-4c9d-abcf-df83bd050a59",
  "_revision": 1
}
```
<a id="31-policy-api-v1-infra-domains-f06fd228-8088-4439-a9e6-26c90a829c57"></a>
### 31. /policy/api/v1/infra/domains/f06fd228-8088-4439-a9e6-26c90a829c57

**HTTP Methods:** GET

**Explanation:**
NSX domain management. Domains are logical containers for security and networking objects.

---


**Sample Response Body (GET, from logs):**
```json
{
  "resource_type": "Domain",
  "id": "f06fd228-8088-4439-a9e6-26c90a829c57",
  "display_name": "f06fd228-8088-4439-a9e6-26c90a829c57",
  "tags": [
    {
      "scope": "ncp/cluster_domain",
      "tag": "true"
    },
    {
      "scope": "ncp/cluster",
      "tag": "f06fd228-8088-4439-a9e6-26c90a829c57"
    }
  ],
  "path": "/infra/domains/f06fd228-8088-4439-a9e6-26c90a829c57",
  "relative_path": "f06fd228-8088-4439-a9e6-26c90a829c57",
  "parent_path": "/infra",
  "remote_path": "",
  "unique_id": "7a5abfb3-90df-4abb-ba3e-3e07db09687c",
  "realization_id": "7a5abfb3-90df-4abb-ba3e-3e07db09687c",
  "owner_id": "42495ba4-8c0b-49c9-b645-84cc39c2df30",
  "marked_for_delete": false,
  "overridden": false,
  "_system_owned": false,
  "_protection": "NOT_PROTECTED",
  "_create_time": 1760503429406,
  "_create_user": "wcp-cluster-user-f06fd228-8088-4439-a9e6-26c90a829c57-d34133d7-0fdf-4c9d-abcf-df83bd050a59",
  "_last_modified_time": 1760503429406,
  "_last_modified_user": "wcp-cluster-user-f06fd228-8088-4439-a9e6-26c90a829c57-d34133d7-0fdf-4c9d-abcf-df83bd050a59",
  "_revision": 0
}
```
<a id="32-policy-api-v1-infra-lb-virtual-servers-cert-manager-9402-tcp-gk8qf"></a>
### 32. /policy/api/v1/infra/lb-virtual-servers/cert-manager_9402_TCP_gk8qf

**HTTP Methods:** GET, PATCH

**Explanation:**
NSX Policy API endpoint for resource management.

---


**Sample Response Body (GET, from logs):**
```json
{
  "enabled": true,
  "ip_address": "172.24.7.217",
  "ports": [
    "9402"
  ],
  "access_log_enabled": false,
  "lb_service_path": "/infra/lb-services/clusterip_f06fd228-8088-4439-a9e6-26c90a829c57_dlb",
  "pool_path": "/infra/lb-pools/cert-manager_9402_TCP_gk8qf",
  "application_profile_path": "/infra/lb-app-profiles/default-tcp-lb-app-profile",
  "log_significant_event_only": false,
  "resource_type": "LBVirtualServer",
  "id": "cert-manager_9402_TCP_gk8qf",
  "display_name": "cert-manager_9402_TCP",
  "tags": [
    {
      "scope": "ncp/version",
      "tag": "1.2.0"
    },
    {
      "scope": "ncp/cluster",
      "tag": "f06fd228-8088-4439-a9e6-26c90a829c57"
    },
    {
      "scope": "ncp/project",
      "tag": "vmware-system-cert-manager"
    },
    {
      "scope": "external_id",
      "tag": "a4aed87f-f628-4898-8fdc-cf48cfd5e75a"
    },
    {
      "scope": "ncp/service",
      "tag": "cert-manager"
    },
    {
      "scope": "ncp/service_uid",
      "tag": "a4aed87f-f628-4898-8fdc-cf48cfd5e75a"
    },
    {
      "scope": "ncp/service_port",
      "tag": "9402"
    },
    {
      "scope": "ncp/service_port_protocol",
      "tag": "TCP"
    },
    {
      "scope": "ncp/created_for",
      "tag": "DLB"
    }
  ],
  "path": "/infra/lb-virtual-servers/cert-manager_9402_TCP_gk8qf",
  "relative_path": "cert-manager_9402_TCP_gk8qf",
  "parent_path": "/infra",
  "remote_path": "",
  "unique_id": "7472d201-df8d-4c0c-9047-e0a8bac9cf8b",
  "realization_id": "7472d201-df8d-4c0c-9047-e0a8bac9cf8b",
  "owner_id": "42495ba4-8c0b-49c9-b645-84cc39c2df30",
  "marked_for_delete": false,
  "overridden": false,
  "_system_owned": false,
  "_protection": "NOT_PROTECTED",
  "_create_time": 1760503452529,
  "_create_user": "wcp-cluster-user-f06fd228-8088-4439-a9e6-26c90a829c57-d34133d7-0fdf-4c9d-abcf-df83bd050a59",
  "_last_modified_time": 1760503620881,
  "_last_modified_user": "wcp-cluster-user-f06fd228-8088-4439-a9e6-26c90a829c57-d34133d7-0fdf-4c9d-abcf-df83bd050a59",
  "_revision": 1
}
```
<a id="33-policy-api-v1-infra-lb-virtual-servers-nsx-operator-8093-tcp-s6pir"></a>
### 33. /policy/api/v1/infra/lb-virtual-servers/nsx-operator_8093_TCP_s6pir

**HTTP Methods:** GET, PATCH

**Explanation:**
NSX Policy API endpoint for resource management.

---


**Sample Response Body (GET, from logs):**
```json
{
  "enabled": true,
  "ip_address": "172.24.234.249",
  "ports": [
    "8093"
  ],
  "access_log_enabled": false,
  "lb_service_path": "/infra/lb-services/clusterip_f06fd228-8088-4439-a9e6-26c90a829c57_dlb",
  "pool_path": "/infra/lb-pools/nsx-operator_8093_TCP_s6pir",
  "application_profile_path": "/infra/lb-app-profiles/default-tcp-lb-app-profile",
  "log_significant_event_only": false,
  "resource_type": "LBVirtualServer",
  "id": "nsx-operator_8093_TCP_s6pir",
  "display_name": "nsx-operator_8093_TCP",
  "tags": [
    {
      "scope": "ncp/version",
      "tag": "1.2.0"
    },
    {
      "scope": "ncp/cluster",
      "tag": "f06fd228-8088-4439-a9e6-26c90a829c57"
    },
    {
      "scope": "ncp/project",
      "tag": "vmware-system-nsx"
    },
    {
      "scope": "external_id",
      "tag": "d17bbdc7-ea76-4ab8-8548-b432e7c51915"
    },
    {
      "scope": "ncp/service",
      "tag": "nsx-operator"
    },
    {
      "scope": "ncp/service_uid",
      "tag": "d17bbdc7-ea76-4ab8-8548-b432e7c51915"
    },
    {
      "scope": "ncp/service_port",
      "tag": "8093"
    },
    {
      "scope": "ncp/service_port_protocol",
      "tag": "TCP"
    },
    {
      "scope": "ncp/created_for",
      "tag": "DLB"
    }
  ],
  "path": "/infra/lb-virtual-servers/nsx-operator_8093_TCP_s6pir",
  "relative_path": "nsx-operator_8093_TCP_s6pir",
  "parent_path": "/infra",
  "remote_path": "",
  "unique_id": "9f8e91b0-9b0c-4697-8a9d-f5e416c4a345",
  "realization_id": "9f8e91b0-9b0c-4697-8a9d-f5e416c4a345",
  "owner_id": "42495ba4-8c0b-49c9-b645-84cc39c2df30",
  "marked_for_delete": false,
  "overridden": false,
  "_system_owned": false,
  "_protection": "NOT_PROTECTED",
  "_create_time": 1760503452329,
  "_create_user": "wcp-cluster-user-f06fd228-8088-4439-a9e6-26c90a829c57-d34133d7-0fdf-4c9d-abcf-df83bd050a59",
  "_last_modified_time": 1760503613748,
  "_last_modified_user": "wcp-cluster-user-f06fd228-8088-4439-a9e6-26c90a829c57-d34133d7-0fdf-4c9d-abcf-df83bd050a59",
  "_revision": 1
}
```
<a id="34-policy-api-v1-infra-lb-virtual-servers-packaging-api-443-tcp-oa5ep"></a>
### 34. /policy/api/v1/infra/lb-virtual-servers/packaging-api_443_TCP_oa5ep

**HTTP Methods:** GET, PATCH

**Explanation:**
NSX Policy API endpoint for resource management.

---


**Sample Response Body (GET, from logs):**
```json
{
  "enabled": true,
  "ip_address": "172.24.255.225",
  "ports": [
    "443"
  ],
  "access_log_enabled": false,
  "lb_service_path": "/infra/lb-services/clusterip_f06fd228-8088-4439-a9e6-26c90a829c57_dlb",
  "pool_path": "/infra/lb-pools/packaging-api_443_TCP_oa5ep",
  "application_profile_path": "/infra/lb-app-profiles/default-tcp-lb-app-profile",
  "log_significant_event_only": false,
  "resource_type": "LBVirtualServer",
  "id": "packaging-api_443_TCP_oa5ep",
  "display_name": "packaging-api_443_TCP",
  "tags": [
    {
      "scope": "ncp/version",
      "tag": "1.2.0"
    },
    {
      "scope": "ncp/cluster",
      "tag": "f06fd228-8088-4439-a9e6-26c90a829c57"
    },
    {
      "scope": "ncp/project",
      "tag": "vmware-system-appplatform-operator-system"
    },
    {
      "scope": "external_id",
      "tag": "03c99412-7a4c-47d5-9539-80270e165975"
    },
    {
      "scope": "ncp/service",
      "tag": "packaging-api"
    },
    {
      "scope": "ncp/service_uid",
      "tag": "03c99412-7a4c-47d5-9539-80270e165975"
    },
    {
      "scope": "ncp/service_port",
      "tag": "443"
    },
    {
      "scope": "ncp/service_port_protocol",
      "tag": "TCP"
    },
    {
      "scope": "ncp/created_for",
      "tag": "DLB"
    }
  ],
  "path": "/infra/lb-virtual-servers/packaging-api_443_TCP_oa5ep",
  "relative_path": "packaging-api_443_TCP_oa5ep",
  "parent_path": "/infra",
  "remote_path": "",
  "unique_id": "b28722f5-1f66-4b2c-a247-8ff671c05501",
  "realization_id": "b28722f5-1f66-4b2c-a247-8ff671c05501",
  "owner_id": "42495ba4-8c0b-49c9-b645-84cc39c2df30",
  "marked_for_delete": false,
  "overridden": false,
  "_system_owned": false,
  "_protection": "NOT_PROTECTED",
  "_create_time": 1760503448848,
  "_create_user": "wcp-cluster-user-f06fd228-8088-4439-a9e6-26c90a829c57-d34133d7-0fdf-4c9d-abcf-df83bd050a59",
  "_last_modified_time": 1760503619928,
  "_last_modified_user": "wcp-cluster-user-f06fd228-8088-4439-a9e6-26c90a829c57-d34133d7-0fdf-4c9d-abcf-df83bd050a59",
  "_revision": 1
}
```
<a id="35-policy-api-v1-infra-lb-virtual-servers-packaging-api-8080-tcp-oa5ep"></a>
### 35. /policy/api/v1/infra/lb-virtual-servers/packaging-api_8080_TCP_oa5ep

**HTTP Methods:** GET, PATCH

**Explanation:**
NSX Policy API endpoint for resource management.

---


**Sample Response Body (GET, from logs):**
```json
{
  "enabled": true,
  "ip_address": "172.24.255.225",
  "ports": [
    "8080"
  ],
  "access_log_enabled": false,
  "lb_service_path": "/infra/lb-services/clusterip_f06fd228-8088-4439-a9e6-26c90a829c57_dlb",
  "pool_path": "/infra/lb-pools/packaging-api_8080_TCP_oa5ep",
  "application_profile_path": "/infra/lb-app-profiles/default-tcp-lb-app-profile",
  "log_significant_event_only": false,
  "resource_type": "LBVirtualServer",
  "id": "packaging-api_8080_TCP_oa5ep",
  "display_name": "packaging-api_8080_TCP",
  "tags": [
    {
      "scope": "ncp/version",
      "tag": "1.2.0"
    },
    {
      "scope": "ncp/cluster",
      "tag": "f06fd228-8088-4439-a9e6-26c90a829c57"
    },
    {
      "scope": "ncp/project",
      "tag": "vmware-system-appplatform-operator-system"
    },
    {
      "scope": "external_id",
      "tag": "03c99412-7a4c-47d5-9539-80270e165975"
    },
    {
      "scope": "ncp/service",
      "tag": "packaging-api"
    },
    {
      "scope": "ncp/service_uid",
      "tag": "03c99412-7a4c-47d5-9539-80270e165975"
    },
    {
      "scope": "ncp/service_port",
      "tag": "8080"
    },
    {
      "scope": "ncp/service_port_protocol",
      "tag": "TCP"
    },
    {
      "scope": "ncp/created_for",
      "tag": "DLB"
    }
  ],
  "path": "/infra/lb-virtual-servers/packaging-api_8080_TCP_oa5ep",
  "relative_path": "packaging-api_8080_TCP_oa5ep",
  "parent_path": "/infra",
  "remote_path": "",
  "unique_id": "4e60010e-234d-4e3d-87ac-0e4cd0ce5c2d",
  "realization_id": "4e60010e-234d-4e3d-87ac-0e4cd0ce5c2d",
  "owner_id": "42495ba4-8c0b-49c9-b645-84cc39c2df30",
  "marked_for_delete": false,
  "overridden": false,
  "_system_owned": false,
  "_protection": "NOT_PROTECTED",
  "_create_time": 1760503453363,
  "_create_user": "wcp-cluster-user-f06fd228-8088-4439-a9e6-26c90a829c57-d34133d7-0fdf-4c9d-abcf-df83bd050a59",
  "_last_modified_time": 1760503620173,
  "_last_modified_user": "wcp-cluster-user-f06fd228-8088-4439-a9e6-26c90a829c57-d34133d7-0fdf-4c9d-abcf-df83bd050a59",
  "_revision": 1
}
```
<a id="36-policy-api-v1-infra-lb-virtual-servers-webhook-service-443-tcp-tuo3j"></a>
### 36. /policy/api/v1/infra/lb-virtual-servers/webhook-service_443_TCP_tuo3j

**HTTP Methods:** GET, PATCH

**Explanation:**
NSX Policy API endpoint for resource management.

---


**Sample Response Body (GET, from logs):**
```json
{
  "enabled": true,
  "ip_address": "172.24.44.13",
  "ports": [
    "443"
  ],
  "access_log_enabled": false,
  "lb_service_path": "/infra/lb-services/clusterip_f06fd228-8088-4439-a9e6-26c90a829c57_dlb",
  "pool_path": "/infra/lb-pools/webhook-service_443_TCP_tuo3j",
  "application_profile_path": "/infra/lb-app-profiles/default-tcp-lb-app-profile",
  "log_significant_event_only": false,
  "resource_type": "LBVirtualServer",
  "id": "webhook-service_443_TCP_tuo3j",
  "display_name": "webhook-service_443_TCP",
  "tags": [
    {
      "scope": "ncp/version",
      "tag": "1.2.0"
    },
    {
      "scope": "ncp/cluster",
      "tag": "f06fd228-8088-4439-a9e6-26c90a829c57"
    },
    {
      "scope": "ncp/project",
      "tag": "svc-velero-2wquv"
    },
    {
      "scope": "external_id",
      "tag": "87fc6722-2422-43c8-98dc-3b5e7fe5ff41"
    },
    {
      "scope": "ncp/service",
      "tag": "webhook-service"
    },
    {
      "scope": "ncp/service_uid",
      "tag": "87fc6722-2422-43c8-98dc-3b5e7fe5ff41"
    },
    {
      "scope": "ncp/service_port",
      "tag": "443"
    },
    {
      "scope": "ncp/service_port_protocol",
      "tag": "TCP"
    },
    {
      "scope": "ncp/created_for",
      "tag": "DLB"
    }
  ],
  "path": "/infra/lb-virtual-servers/webhook-service_443_TCP_tuo3j",
  "relative_path": "webhook-service_443_TCP_tuo3j",
  "parent_path": "/infra",
  "remote_path": "",
  "unique_id": "317218c9-b647-473c-80fd-1976a2cd2e6c",
  "realization_id": "317218c9-b647-473c-80fd-1976a2cd2e6c",
  "owner_id": "42495ba4-8c0b-49c9-b645-84cc39c2df30",
  "marked_for_delete": false,
  "overridden": false,
  "_system_owned": false,
  "_protection": "NOT_PROTECTED",
  "_create_time": 1760504043543,
  "_create_user": "wcp-cluster-user-f06fd228-8088-4439-a9e6-26c90a829c57-d34133d7-0fdf-4c9d-abcf-df83bd050a59",
  "_last_modified_time": 1760504045080,
  "_last_modified_user": "wcp-cluster-user-f06fd228-8088-4439-a9e6-26c90a829c57-d34133d7-0fdf-4c9d-abcf-df83bd050a59",
  "_revision": 1
}
```
<a id="37-policy-api-v1-infra-lb-virtual-servers-docker-registry-5000-tcp-goaln"></a>
### 37. /policy/api/v1/infra/lb-virtual-servers/docker-registry_5000_TCP_goaln

**HTTP Methods:** GET, PATCH

**Explanation:**
NSX Policy API endpoint for resource management.

---


**Sample Response Body (GET, from logs):**
```json
{
  "enabled": true,
  "ip_address": "172.24.49.39",
  "ports": [
    "5000"
  ],
  "access_log_enabled": false,
  "lb_service_path": "/infra/lb-services/clusterip_f06fd228-8088-4439-a9e6-26c90a829c57_dlb",
  "pool_path": "/infra/lb-pools/docker-registry_5000_TCP_goaln",
  "application_profile_path": "/infra/lb-app-profiles/default-tcp-lb-app-profile",
  "log_significant_event_only": false,
  "resource_type": "LBVirtualServer",
  "id": "docker-registry_5000_TCP_goaln",
  "display_name": "docker-registry_5000_TCP",
  "tags": [
    {
      "scope": "ncp/version",
      "tag": "1.2.0"
    },
    {
      "scope": "ncp/cluster",
      "tag": "f06fd228-8088-4439-a9e6-26c90a829c57"
    },
    {
      "scope": "ncp/project",
      "tag": "kube-system"
    },
    {
      "scope": "external_id",
      "tag": "897eb950-b522-4bbd-8d01-5ab4f7277672"
    },
    {
      "scope": "ncp/service",
      "tag": "docker-registry"
    },
    {
      "scope": "ncp/service_uid",
      "tag": "897eb950-b522-4bbd-8d01-5ab4f7277672"
    },
    {
      "scope": "ncp/service_port",
      "tag": "5000"
    },
    {
      "scope": "ncp/service_port_protocol",
      "tag": "TCP"
    },
    {
      "scope": "ncp/created_for",
      "tag": "DLB"
    }
  ],
  "path": "/infra/lb-virtual-servers/docker-registry_5000_TCP_goaln",
  "relative_path": "docker-registry_5000_TCP_goaln",
  "parent_path": "/infra",
  "remote_path": "",
  "unique_id": "417d0e9e-7cc3-4544-a2a6-f69e4f735856",
  "realization_id": "417d0e9e-7cc3-4544-a2a6-f69e4f735856",
  "owner_id": "42495ba4-8c0b-49c9-b645-84cc39c2df30",
  "marked_for_delete": false,
  "overridden": false,
  "_system_owned": false,
  "_protection": "NOT_PROTECTED",
  "_create_time": 1760503465698,
  "_create_user": "wcp-cluster-user-f06fd228-8088-4439-a9e6-26c90a829c57-d34133d7-0fdf-4c9d-abcf-df83bd050a59",
  "_last_modified_time": 1760503620852,
  "_last_modified_user": "wcp-cluster-user-f06fd228-8088-4439-a9e6-26c90a829c57-d34133d7-0fdf-4c9d-abcf-df83bd050a59",
  "_revision": 1
}
```
<a id="38-policy-api-v1-infra-lb-virtual-servers-mgmt-image-proxy-443-tcp-1k4gd"></a>
### 38. /policy/api/v1/infra/lb-virtual-servers/mgmt-image-proxy_443_TCP_1k4gd

**HTTP Methods:** GET, PATCH

**Explanation:**
NSX Policy API endpoint for resource management.

---


**Sample Response Body (GET, from logs):**
```json
{
  "enabled": true,
  "ip_address": "172.24.95.105",
  "ports": [
    "443"
  ],
  "access_log_enabled": false,
  "lb_service_path": "/infra/lb-services/clusterip_f06fd228-8088-4439-a9e6-26c90a829c57_dlb",
  "pool_path": "/infra/lb-pools/mgmt-image-proxy_443_TCP_1k4gd",
  "application_profile_path": "/infra/lb-app-profiles/default-tcp-lb-app-profile",
  "log_significant_event_only": false,
  "resource_type": "LBVirtualServer",
  "id": "mgmt-image-proxy_443_TCP_1k4gd",
  "display_name": "mgmt-image-proxy_443_TCP",
  "tags": [
    {
      "scope": "ncp/version",
      "tag": "1.2.0"
    },
    {
      "scope": "ncp/cluster",
      "tag": "f06fd228-8088-4439-a9e6-26c90a829c57"
    },
    {
      "scope": "ncp/project",
      "tag": "kube-system"
    },
    {
      "scope": "external_id",
      "tag": "256a50db-8a7e-45ef-992a-7cbb29678c55"
    },
    {
      "scope": "ncp/service",
      "tag": "mgmt-image-proxy"
    },
    {
      "scope": "ncp/service_uid",
      "tag": "256a50db-8a7e-45ef-992a-7cbb29678c55"
    },
    {
      "scope": "ncp/service_port",
      "tag": "443"
    },
    {
      "scope": "ncp/service_port_protocol",
      "tag": "TCP"
    },
    {
      "scope": "ncp/created_for",
      "tag": "DLB"
    }
  ],
  "path": "/infra/lb-virtual-servers/mgmt-image-proxy_443_TCP_1k4gd",
  "relative_path": "mgmt-image-proxy_443_TCP_1k4gd",
  "parent_path": "/infra",
  "remote_path": "",
  "unique_id": "cfe98bba-a5f0-41c2-b59c-ae078b616a0c",
  "realization_id": "cfe98bba-a5f0-41c2-b59c-ae078b616a0c",
  "owner_id": "42495ba4-8c0b-49c9-b645-84cc39c2df30",
  "marked_for_delete": false,
  "overridden": false,
  "_system_owned": false,
  "_protection": "NOT_PROTECTED",
  "_create_time": 1760503720375,
  "_create_user": "wcp-cluster-user-f06fd228-8088-4439-a9e6-26c90a829c57-d34133d7-0fdf-4c9d-abcf-df83bd050a59",
  "_last_modified_time": 1760503721533,
  "_last_modified_user": "wcp-cluster-user-f06fd228-8088-4439-a9e6-26c90a829c57-d34133d7-0fdf-4c9d-abcf-df83bd050a59",
  "_revision": 1
}
```
<a id="39-policy-api-v1-infra-lb-virtual-servers-kube-dns-metrics-9153-tcp-ea0v8"></a>
### 39. /policy/api/v1/infra/lb-virtual-servers/kube-dns-metrics_9153_TCP_ea0v8

**HTTP Methods:** GET, PATCH

**Explanation:**
NSX Policy API endpoint for resource management.

---


**Sample Response Body (GET, from logs):**
```json
{
  "enabled": true,
  "ip_address": "172.24.136.237",
  "ports": [
    "9153"
  ],
  "access_log_enabled": false,
  "lb_service_path": "/infra/lb-services/clusterip_f06fd228-8088-4439-a9e6-26c90a829c57_dlb",
  "pool_path": "/infra/lb-pools/kube-dns-metrics_9153_TCP_ea0v8",
  "application_profile_path": "/infra/lb-app-profiles/default-tcp-lb-app-profile",
  "log_significant_event_only": false,
  "resource_type": "LBVirtualServer",
  "id": "kube-dns-metrics_9153_TCP_ea0v8",
  "display_name": "kube-dns-metrics_9153_TCP",
  "tags": [
    {
      "scope": "ncp/version",
      "tag": "1.2.0"
    },
    {
      "scope": "ncp/cluster",
      "tag": "f06fd228-8088-4439-a9e6-26c90a829c57"
    },
    {
      "scope": "ncp/project",
      "tag": "kube-system"
    },
    {
      "scope": "external_id",
      "tag": "1c19e038-cd0e-4d07-b391-81fd53606800"
    },
    {
      "scope": "ncp/service",
      "tag": "kube-dns-metrics"
    },
    {
      "scope": "ncp/service_uid",
      "tag": "1c19e038-cd0e-4d07-b391-81fd53606800"
    },
    {
      "scope": "ncp/service_port",
      "tag": "9153"
    },
    {
      "scope": "ncp/service_port_protocol",
      "tag": "TCP"
    },
    {
      "scope": "ncp/created_for",
      "tag": "DLB"
    }
  ],
  "path": "/infra/lb-virtual-servers/kube-dns-metrics_9153_TCP_ea0v8",
  "relative_path": "kube-dns-metrics_9153_TCP_ea0v8",
  "parent_path": "/infra",
  "remote_path": "",
  "unique_id": "89ff6c27-c4b8-4282-bdaf-f07ef2d7b519",
  "realization_id": "89ff6c27-c4b8-4282-bdaf-f07ef2d7b519",
  "owner_id": "42495ba4-8c0b-49c9-b645-84cc39c2df30",
  "marked_for_delete": false,
  "overridden": false,
  "_system_owned": false,
  "_protection": "NOT_PROTECTED",
  "_create_time": 1760503468456,
  "_create_user": "wcp-cluster-user-f06fd228-8088-4439-a9e6-26c90a829c57-d34133d7-0fdf-4c9d-abcf-df83bd050a59",
  "_last_modified_time": 1760503622023,
  "_last_modified_user": "wcp-cluster-user-f06fd228-8088-4439-a9e6-26c90a829c57-d34133d7-0fdf-4c9d-abcf-df83bd050a59",
  "_revision": 1
}
```
<a id="40-policy-api-v1-infra-lb-virtual-servers-telegraf-deploy-10013-tcp-6o1fu"></a>
### 40. /policy/api/v1/infra/lb-virtual-servers/telegraf-deploy_10013_TCP_6o1fu

**HTTP Methods:** GET, PATCH

**Explanation:**
NSX Policy API endpoint for resource management.

---


**Sample Response Body (GET, from logs):**
```json
{
  "enabled": true,
  "ip_address": "172.24.26.37",
  "ports": [
    "10013"
  ],
  "access_log_enabled": false,
  "lb_service_path": "/infra/lb-services/clusterip_f06fd228-8088-4439-a9e6-26c90a829c57_dlb",
  "pool_path": "/infra/lb-pools/telegraf-deploy_10013_TCP_6o1fu",
  "application_profile_path": "/infra/lb-app-profiles/default-tcp-lb-app-profile",
  "log_significant_event_only": false,
  "resource_type": "LBVirtualServer",
  "id": "telegraf-deploy_10013_TCP_6o1fu",
  "display_name": "telegraf-deploy_10013_TCP",
  "tags": [
    {
      "scope": "ncp/version",
      "tag": "1.2.0"
    },
    {
      "scope": "ncp/cluster",
      "tag": "f06fd228-8088-4439-a9e6-26c90a829c57"
    },
    {
      "scope": "ncp/project",
      "tag": "vmware-system-monitoring"
    },
    {
      "scope": "external_id",
      "tag": "7c35da88-fa4c-4832-97b5-56738b67b243"
    },
    {
      "scope": "ncp/service",
      "tag": "telegraf-deploy"
    },
    {
      "scope": "ncp/service_uid",
      "tag": "7c35da88-fa4c-4832-97b5-56738b67b243"
    },
    {
      "scope": "ncp/service_port",
      "tag": "10013"
    },
    {
      "scope": "ncp/service_port_protocol",
      "tag": "TCP"
    },
    {
      "scope": "ncp/created_for",
      "tag": "DLB"
    }
  ],
  "path": "/infra/lb-virtual-servers/telegraf-deploy_10013_TCP_6o1fu",
  "relative_path": "telegraf-deploy_10013_TCP_6o1fu",
  "parent_path": "/infra",
  "remote_path": "",
  "unique_id": "fe601d16-108b-46df-8634-04500b27b2e6",
  "realization_id": "fe601d16-108b-46df-8634-04500b27b2e6",
  "owner_id": "42495ba4-8c0b-49c9-b645-84cc39c2df30",
  "marked_for_delete": false,
  "overridden": false,
  "_system_owned": false,
  "_protection": "NOT_PROTECTED",
  "_create_time": 1760503464398,
  "_create_user": "wcp-cluster-user-f06fd228-8088-4439-a9e6-26c90a829c57-d34133d7-0fdf-4c9d-abcf-df83bd050a59",
  "_last_modified_time": 1760503615717,
  "_last_modified_user": "wcp-cluster-user-f06fd228-8088-4439-a9e6-26c90a829c57-d34133d7-0fdf-4c9d-abcf-df83bd050a59",
  "_revision": 1
}
```
<a id="41-policy-api-v1-infra-lb-virtual-servers-kubernetes-internal-443-tcp-p5727"></a>
### 41. /policy/api/v1/infra/lb-virtual-servers/kubernetes-internal_443_TCP_p5727

**HTTP Methods:** GET, PATCH

**Explanation:**
NSX Policy API endpoint for resource management.

---


**Sample Response Body (GET, from logs):**
```json
{
  "enabled": true,
  "ip_address": "172.24.97.127",
  "ports": [
    "443"
  ],
  "access_log_enabled": false,
  "lb_service_path": "/infra/lb-services/clusterip_f06fd228-8088-4439-a9e6-26c90a829c57_dlb",
  "pool_path": "/infra/lb-pools/kubernetes-internal_443_TCP_p5727",
  "application_profile_path": "/infra/lb-app-profiles/default-tcp-lb-app-profile",
  "log_significant_event_only": false,
  "resource_type": "LBVirtualServer",
  "id": "kubernetes-internal_443_TCP_p5727",
  "display_name": "kubernetes-internal_443_TCP",
  "tags": [
    {
      "scope": "ncp/version",
      "tag": "1.2.0"
    },
    {
      "scope": "ncp/cluster",
      "tag": "f06fd228-8088-4439-a9e6-26c90a829c57"
    },
    {
      "scope": "ncp/project",
      "tag": "kube-system"
    },
    {
      "scope": "external_id",
      "tag": "2abc5d00-ad9b-49cf-acf2-5cbf5f7cac74"
    },
    {
      "scope": "ncp/service",
      "tag": "kubernetes-internal"
    },
    {
      "scope": "ncp/service_uid",
      "tag": "2abc5d00-ad9b-49cf-acf2-5cbf5f7cac74"
    },
    {
      "scope": "ncp/service_port",
      "tag": "443"
    },
    {
      "scope": "ncp/service_port_protocol",
      "tag": "TCP"
    },
    {
      "scope": "ncp/created_for",
      "tag": "DLB"
    }
  ],
  "path": "/infra/lb-virtual-servers/kubernetes-internal_443_TCP_p5727",
  "relative_path": "kubernetes-internal_443_TCP_p5727",
  "parent_path": "/infra",
  "remote_path": "",
  "unique_id": "68688a92-dc8a-40f9-a019-560a5ace9adf",
  "realization_id": "68688a92-dc8a-40f9-a019-560a5ace9adf",
  "owner_id": "42495ba4-8c0b-49c9-b645-84cc39c2df30",
  "marked_for_delete": false,
  "overridden": false,
  "_system_owned": false,
  "_protection": "NOT_PROTECTED",
  "_create_time": 1760503456013,
  "_create_user": "wcp-cluster-user-f06fd228-8088-4439-a9e6-26c90a829c57-d34133d7-0fdf-4c9d-abcf-df83bd050a59",
  "_last_modified_time": 1760503618773,
  "_last_modified_user": "wcp-cluster-user-f06fd228-8088-4439-a9e6-26c90a829c57-d34133d7-0fdf-4c9d-abcf-df83bd050a59",
  "_revision": 1
}
```
<a id="42-policy-api-v1-infra-lb-virtual-servers-capi-webhook-service-443-tcp-r0p2b"></a>
### 42. /policy/api/v1/infra/lb-virtual-servers/capi-webhook-service_443_TCP_r0p2b

**HTTP Methods:** GET, PATCH

**Explanation:**
NSX Policy API endpoint for resource management.

---


**Sample Response Body (GET, from logs):**
```json
{
  "enabled": true,
  "ip_address": "172.24.77.246",
  "ports": [
    "443"
  ],
  "access_log_enabled": false,
  "lb_service_path": "/infra/lb-services/clusterip_f06fd228-8088-4439-a9e6-26c90a829c57_dlb",
  "pool_path": "/infra/lb-pools/capi-webhook-service_443_TCP_r0p2b",
  "application_profile_path": "/infra/lb-app-profiles/default-tcp-lb-app-profile",
  "log_significant_event_only": false,
  "resource_type": "LBVirtualServer",
  "id": "capi-webhook-service_443_TCP_r0p2b",
  "display_name": "capi-webhook-service_443_TCP",
  "tags": [
    {
      "scope": "ncp/version",
      "tag": "1.2.0"
    },
    {
      "scope": "ncp/cluster",
      "tag": "f06fd228-8088-4439-a9e6-26c90a829c57"
    },
    {
      "scope": "ncp/project",
      "tag": "svc-tkg-jrsvf"
    },
    {
      "scope": "external_id",
      "tag": "ca2a88db-a098-455f-ad43-b0c38225e422"
    },
    {
      "scope": "ncp/service",
      "tag": "capi-webhook-service"
    },
    {
      "scope": "ncp/service_uid",
      "tag": "ca2a88db-a098-455f-ad43-b0c38225e422"
    },
    {
      "scope": "ncp/service_port",
      "tag": "443"
    },
    {
      "scope": "ncp/service_port_protocol",
      "tag": "TCP"
    },
    {
      "scope": "ncp/created_for",
      "tag": "DLB"
    }
  ],
  "path": "/infra/lb-virtual-servers/capi-webhook-service_443_TCP_r0p2b",
  "relative_path": "capi-webhook-service_443_TCP_r0p2b",
  "parent_path": "/infra",
  "remote_path": "",
  "unique_id": "48633026-27a8-4dfc-9e18-ba835780b444",
  "realization_id": "48633026-27a8-4dfc-9e18-ba835780b444",
  "owner_id": "42495ba4-8c0b-49c9-b645-84cc39c2df30",
  "marked_for_delete": false,
  "overridden": false,
  "_system_owned": false,
  "_protection": "NOT_PROTECTED",
  "_create_time": 1760504055704,
  "_create_user": "wcp-cluster-user-f06fd228-8088-4439-a9e6-26c90a829c57-d34133d7-0fdf-4c9d-abcf-df83bd050a59",
  "_last_modified_time": 1760504058013,
  "_last_modified_user": "wcp-cluster-user-f06fd228-8088-4439-a9e6-26c90a829c57-d34133d7-0fdf-4c9d-abcf-df83bd050a59",
  "_revision": 1
}
```
<a id="43-policy-api-v1-infra-lb-virtual-servers-capv-webhook-service-443-tcp-6heqj"></a>
### 43. /policy/api/v1/infra/lb-virtual-servers/capv-webhook-service_443_TCP_6heqj

**HTTP Methods:** GET, PATCH

**Explanation:**
NSX Policy API endpoint for resource management.

---


**Sample Response Body (GET, from logs):**
```json
{
  "enabled": true,
  "ip_address": "172.24.196.102",
  "ports": [
    "443"
  ],
  "access_log_enabled": false,
  "lb_service_path": "/infra/lb-services/clusterip_f06fd228-8088-4439-a9e6-26c90a829c57_dlb",
  "pool_path": "/infra/lb-pools/capv-webhook-service_443_TCP_6heqj",
  "application_profile_path": "/infra/lb-app-profiles/default-tcp-lb-app-profile",
  "log_significant_event_only": false,
  "resource_type": "LBVirtualServer",
  "id": "capv-webhook-service_443_TCP_6heqj",
  "display_name": "capv-webhook-service_443_TCP",
  "tags": [
    {
      "scope": "ncp/version",
      "tag": "1.2.0"
    },
    {
      "scope": "ncp/cluster",
      "tag": "f06fd228-8088-4439-a9e6-26c90a829c57"
    },
    {
      "scope": "ncp/project",
      "tag": "svc-tkg-jrsvf"
    },
    {
      "scope": "external_id",
      "tag": "7d3dfbeb-0ee9-433e-8452-bdca8cf0933a"
    },
    {
      "scope": "ncp/service",
      "tag": "capv-webhook-service"
    },
    {
      "scope": "ncp/service_uid",
      "tag": "7d3dfbeb-0ee9-433e-8452-bdca8cf0933a"
    },
    {
      "scope": "ncp/service_port",
      "tag": "443"
    },
    {
      "scope": "ncp/service_port_protocol",
      "tag": "TCP"
    },
    {
      "scope": "ncp/created_for",
      "tag": "DLB"
    }
  ],
  "path": "/infra/lb-virtual-servers/capv-webhook-service_443_TCP_6heqj",
  "relative_path": "capv-webhook-service_443_TCP_6heqj",
  "parent_path": "/infra",
  "remote_path": "",
  "unique_id": "13b3e1ef-ac6d-4689-a6b2-f1cac4cb4b21",
  "realization_id": "13b3e1ef-ac6d-4689-a6b2-f1cac4cb4b21",
  "owner_id": "42495ba4-8c0b-49c9-b645-84cc39c2df30",
  "marked_for_delete": false,
  "overridden": false,
  "_system_owned": false,
  "_protection": "NOT_PROTECTED",
  "_create_time": 1760504049837,
  "_create_user": "wcp-cluster-user-f06fd228-8088-4439-a9e6-26c90a829c57-d34133d7-0fdf-4c9d-abcf-df83bd050a59",
  "_last_modified_time": 1760504052363,
  "_last_modified_user": "wcp-cluster-user-f06fd228-8088-4439-a9e6-26c90a829c57-d34133d7-0fdf-4c9d-abcf-df83bd050a59",
  "_revision": 1
}
```
<a id="44-policy-api-v1-infra-lb-virtual-servers-cert-manager-webhook-443-tcp-chss8"></a>
### 44. /policy/api/v1/infra/lb-virtual-servers/cert-manager-webhook_443_TCP_chss8

**HTTP Methods:** GET, PATCH

**Explanation:**
NSX Policy API endpoint for resource management.

---


**Sample Response Body (GET, from logs):**
```json
{
  "enabled": true,
  "ip_address": "172.24.155.56",
  "ports": [
    "443"
  ],
  "access_log_enabled": false,
  "lb_service_path": "/infra/lb-services/clusterip_f06fd228-8088-4439-a9e6-26c90a829c57_dlb",
  "pool_path": "/infra/lb-pools/cert-manager-webhook_443_TCP_chss8",
  "application_profile_path": "/infra/lb-app-profiles/default-tcp-lb-app-profile",
  "log_significant_event_only": false,
  "resource_type": "LBVirtualServer",
  "id": "cert-manager-webhook_443_TCP_chss8",
  "display_name": "cert-manager-webhook_443_TCP",
  "tags": [
    {
      "scope": "ncp/version",
      "tag": "1.2.0"
    },
    {
      "scope": "ncp/cluster",
      "tag": "f06fd228-8088-4439-a9e6-26c90a829c57"
    },
    {
      "scope": "ncp/project",
      "tag": "vmware-system-cert-manager"
    },
    {
      "scope": "external_id",
      "tag": "4485b757-c172-4919-a8b2-44f6a05e475d"
    },
    {
      "scope": "ncp/service",
      "tag": "cert-manager-webhook"
    },
    {
      "scope": "ncp/service_uid",
      "tag": "4485b757-c172-4919-a8b2-44f6a05e475d"
    },
    {
      "scope": "ncp/service_port",
      "tag": "443"
    },
    {
      "scope": "ncp/service_port_protocol",
      "tag": "TCP"
    },
    {
      "scope": "ncp/created_for",
      "tag": "DLB"
    }
  ],
  "path": "/infra/lb-virtual-servers/cert-manager-webhook_443_TCP_chss8",
  "relative_path": "cert-manager-webhook_443_TCP_chss8",
  "parent_path": "/infra",
  "remote_path": "",
  "unique_id": "7d71948b-4e7f-4a4d-af18-0683de387b3b",
  "realization_id": "7d71948b-4e7f-4a4d-af18-0683de387b3b",
  "owner_id": "42495ba4-8c0b-49c9-b645-84cc39c2df30",
  "marked_for_delete": false,
  "overridden": false,
  "_system_owned": false,
  "_protection": "NOT_PROTECTED",
  "_create_time": 1760503460380,
  "_create_user": "wcp-cluster-user-f06fd228-8088-4439-a9e6-26c90a829c57-d34133d7-0fdf-4c9d-abcf-df83bd050a59",
  "_last_modified_time": 1760503619942,
  "_last_modified_user": "wcp-cluster-user-f06fd228-8088-4439-a9e6-26c90a829c57-d34133d7-0fdf-4c9d-abcf-df83bd050a59",
  "_revision": 1
}
```
<a id="45-policy-api-v1-infra-lb-virtual-servers-prevpc-loadbalancer-8080-tcp-j7n9u"></a>
### 45. /policy/api/v1/infra/lb-virtual-servers/prevpc-loadbalancer_8080_TCP_j7n9u

**HTTP Methods:** DELETE, GET, PATCH

**Explanation:**
NSX Policy API endpoint for resource management.

---


**Sample Response Body (GET, from logs):**
```json
{
  "enabled": true,
  "ip_address": "172.24.99.198",
  "ports": [
    "8080"
  ],
  "lb_service_path": "/infra/lb-services/clusterip_f06fd228-8088-4439-a9e6-26c90a829c57_dlb",
  "pool_path": "/infra/lb-pools/prevpc-loadbalancer_8080_TCP_j7n9u",
  "application_profile_path": "/infra/lb-app-profiles/default-tcp-lb-app-profile",
  "log_significant_event_only": false,
  "resource_type": "LBVirtualServer",
  "id": "prevpc-loadbalancer_8080_TCP_j7n9u",
  "display_name": "prevpc-loadbalancer_8080_TCP",
  "tags": [
    {
      "scope": "ncp/version",
      "tag": "1.2.0"
    },
    {
      "scope": "ncp/cluster",
      "tag": "f06fd228-8088-4439-a9e6-26c90a829c57"
    },
    {
      "scope": "ncp/project",
      "tag": "test-prevpc-8f1a464f"
    },
    {
      "scope": "external_id",
      "tag": "64af7175-c755-4315-9cf7-28c21bd6fc0a"
    },
    {
      "scope": "ncp/service",
      "tag": "prevpc-loadbalancer"
    },
    {
      "scope": "ncp/service_uid",
      "tag": "64af7175-c755-4315-9cf7-28c21bd6fc0a"
    },
    {
      "scope": "ncp/service_port",
      "tag": "8080"
    },
    {
      "scope": "ncp/service_port_protocol",
      "tag": "TCP"
    },
    {
      "scope": "ncp/created_for",
      "tag": "DLB"
    }
  ],
  "path": "/infra/lb-virtual-servers/prevpc-loadbalancer_8080_TCP_j7n9u",
  "relative_path": "prevpc-loadbalancer_8080_TCP_j7n9u",
  "parent_path": "/infra",
  "remote_path": "",
  "unique_id": "ab681c73-63b4-4b6b-96e4-acda529b031c",
  "realization_id": "ab681c73-63b4-4b6b-96e4-acda529b031c",
  "owner_id": "42495ba4-8c0b-49c9-b645-84cc39c2df30",
  "marked_for_delete": false,
  "overridden": false,
  "_system_owned": false,
  "_protection": "NOT_PROTECTED",
  "_create_time": 1760690633836,
  "_create_user": "wcp-cluster-user-f06fd228-8088-4439-a9e6-26c90a829c57-d34133d7-0fdf-4c9d-abcf-df83bd050a59",
  "_last_modified_time": 1760690633836,
  "_last_modified_user": "wcp-cluster-user-f06fd228-8088-4439-a9e6-26c90a829c57-d34133d7-0fdf-4c9d-abcf-df83bd050a59",
  "_revision": 0
}
```
<a id="46-policy-api-v1-infra-lb-virtual-servers-test-service-1bcb333c-80-tcp-9rdbd"></a>
### 46. /policy/api/v1/infra/lb-virtual-servers/test-service-1bcb333c_80_TCP_9rdbd

**HTTP Methods:** DELETE, GET, PATCH

**Explanation:**
NSX Policy API endpoint for resource management.

---


**Sample Response Body (GET, from logs):**
```json
{
  "enabled": true,
  "ip_address": "172.24.27.108",
  "ports": [
    "80"
  ],
  "lb_service_path": "/infra/lb-services/clusterip_f06fd228-8088-4439-a9e6-26c90a829c57_dlb",
  "pool_path": "/infra/lb-pools/test-service-1bcb333c_80_TCP_9rdbd",
  "application_profile_path": "/infra/lb-app-profiles/default-tcp-lb-app-profile",
  "log_significant_event_only": false,
  "resource_type": "LBVirtualServer",
  "id": "test-service-1bcb333c_80_TCP_9rdbd",
  "display_name": "test-service-1bcb333c_80_TCP",
  "tags": [
    {
      "scope": "ncp/version",
      "tag": "1.2.0"
    },
    {
      "scope": "ncp/cluster",
      "tag": "f06fd228-8088-4439-a9e6-26c90a829c57"
    },
    {
      "scope": "ncp/project",
      "tag": "test-service-sync-f1d17bff"
    },
    {
      "scope": "external_id",
      "tag": "dbf60d60-30b2-4792-9bf0-ba4ed1235cb6"
    },
    {
      "scope": "ncp/service",
      "tag": "test-service-1bcb333c"
    },
    {
      "scope": "ncp/service_uid",
      "tag": "dbf60d60-30b2-4792-9bf0-ba4ed1235cb6"
    },
    {
      "scope": "ncp/service_port",
      "tag": "80"
    },
    {
      "scope": "ncp/service_port_protocol",
      "tag": "TCP"
    },
    {
      "scope": "ncp/created_for",
      "tag": "DLB"
    }
  ],
  "path": "/infra/lb-virtual-servers/test-service-1bcb333c_80_TCP_9rdbd",
  "relative_path": "test-service-1bcb333c_80_TCP_9rdbd",
  "parent_path": "/infra",
  "remote_path": "",
  "unique_id": "78d98478-c9cf-4dca-91c9-6c8a41f18317",
  "realization_id": "78d98478-c9cf-4dca-91c9-6c8a41f18317",
  "owner_id": "42495ba4-8c0b-49c9-b645-84cc39c2df30",
  "marked_for_delete": false,
  "overridden": false,
  "_system_owned": false,
  "_protection": "NOT_PROTECTED",
  "_create_time": 1760688958306,
  "_create_user": "wcp-cluster-user-f06fd228-8088-4439-a9e6-26c90a829c57-d34133d7-0fdf-4c9d-abcf-df83bd050a59",
  "_last_modified_time": 1760688958306,
  "_last_modified_user": "wcp-cluster-user-f06fd228-8088-4439-a9e6-26c90a829c57-d34133d7-0fdf-4c9d-abcf-df83bd050a59",
  "_revision": 0
}
```
<a id="47-policy-api-v1-infra-lb-virtual-servers-test-service-da1e3736-80-tcp-2bcu3"></a>
### 47. /policy/api/v1/infra/lb-virtual-servers/test-service-da1e3736_80_TCP_2bcu3

**HTTP Methods:** DELETE, GET, PATCH

**Explanation:**
NSX Policy API endpoint for resource management.

---


**Sample Response Body (GET, from logs):**
```json
{
  "enabled": true,
  "ip_address": "172.24.237.178",
  "ports": [
    "80"
  ],
  "lb_service_path": "/infra/lb-services/clusterip_f06fd228-8088-4439-a9e6-26c90a829c57_dlb",
  "pool_path": "/infra/lb-pools/test-service-da1e3736_80_TCP_2bcu3",
  "application_profile_path": "/infra/lb-app-profiles/default-tcp-lb-app-profile",
  "log_significant_event_only": false,
  "resource_type": "LBVirtualServer",
  "id": "test-service-da1e3736_80_TCP_2bcu3",
  "display_name": "test-service-da1e3736_80_TCP",
  "tags": [
    {
      "scope": "ncp/version",
      "tag": "1.2.0"
    },
    {
      "scope": "ncp/cluster",
      "tag": "f06fd228-8088-4439-a9e6-26c90a829c57"
    },
    {
      "scope": "ncp/project",
      "tag": "test-ingress-sync-73e76bf1"
    },
    {
      "scope": "external_id",
      "tag": "6d949a82-837a-4062-9914-4138a1bf61ca"
    },
    {
      "scope": "ncp/service",
      "tag": "test-service-da1e3736"
    },
    {
      "scope": "ncp/service_uid",
      "tag": "6d949a82-837a-4062-9914-4138a1bf61ca"
    },
    {
      "scope": "ncp/service_port",
      "tag": "80"
    },
    {
      "scope": "ncp/service_port_protocol",
      "tag": "TCP"
    },
    {
      "scope": "ncp/created_for",
      "tag": "DLB"
    }
  ],
  "path": "/infra/lb-virtual-servers/test-service-da1e3736_80_TCP_2bcu3",
  "relative_path": "test-service-da1e3736_80_TCP_2bcu3",
  "parent_path": "/infra",
  "remote_path": "",
  "unique_id": "7ca2a2c4-dbae-465f-851b-262657a5ec29",
  "realization_id": "7ca2a2c4-dbae-465f-851b-262657a5ec29",
  "owner_id": "42495ba4-8c0b-49c9-b645-84cc39c2df30",
  "marked_for_delete": false,
  "overridden": false,
  "_system_owned": false,
  "_protection": "NOT_PROTECTED",
  "_create_time": 1760689049171,
  "_create_user": "wcp-cluster-user-f06fd228-8088-4439-a9e6-26c90a829c57-d34133d7-0fdf-4c9d-abcf-df83bd050a59",
  "_last_modified_time": 1760689049171,
  "_last_modified_user": "wcp-cluster-user-f06fd228-8088-4439-a9e6-26c90a829c57-d34133d7-0fdf-4c9d-abcf-df83bd050a59",
  "_revision": 0
}
```
<a id="48-policy-api-v1-infra-lb-virtual-servers-tkgs-plugin-service-8099-tcp-b6qai"></a>
### 48. /policy/api/v1/infra/lb-virtual-servers/tkgs-plugin-service_8099_TCP_b6qai

**HTTP Methods:** GET, PATCH

**Explanation:**
NSX Policy API endpoint for resource management.

---


**Sample Response Body (GET, from logs):**
```json
{
  "enabled": true,
  "ip_address": "172.24.23.173",
  "ports": [
    "8099"
  ],
  "access_log_enabled": false,
  "lb_service_path": "/infra/lb-services/clusterip_f06fd228-8088-4439-a9e6-26c90a829c57_dlb",
  "pool_path": "/infra/lb-pools/tkgs-plugin-service_8099_TCP_b6qai",
  "application_profile_path": "/infra/lb-app-profiles/default-tcp-lb-app-profile",
  "log_significant_event_only": false,
  "resource_type": "LBVirtualServer",
  "id": "tkgs-plugin-service_8099_TCP_b6qai",
  "display_name": "tkgs-plugin-service_8099_TCP",
  "tags": [
    {
      "scope": "ncp/version",
      "tag": "1.2.0"
    },
    {
      "scope": "ncp/cluster",
      "tag": "f06fd228-8088-4439-a9e6-26c90a829c57"
    },
    {
      "scope": "ncp/project",
      "tag": "svc-tkg-jrsvf"
    },
    {
      "scope": "external_id",
      "tag": "6ca99d17-4b8a-4b24-a18b-a6ff0592b7c5"
    },
    {
      "scope": "ncp/service",
      "tag": "tkgs-plugin-service"
    },
    {
      "scope": "ncp/service_uid",
      "tag": "6ca99d17-4b8a-4b24-a18b-a6ff0592b7c5"
    },
    {
      "scope": "ncp/service_port",
      "tag": "8099"
    },
    {
      "scope": "ncp/service_port_protocol",
      "tag": "TCP"
    },
    {
      "scope": "ncp/created_for",
      "tag": "DLB"
    }
  ],
  "path": "/infra/lb-virtual-servers/tkgs-plugin-service_8099_TCP_b6qai",
  "relative_path": "tkgs-plugin-service_8099_TCP_b6qai",
  "parent_path": "/infra",
  "remote_path": "",
  "unique_id": "039b19e4-2eeb-4123-b10c-c13d9d372f6a",
  "realization_id": "039b19e4-2eeb-4123-b10c-c13d9d372f6a",
  "owner_id": "42495ba4-8c0b-49c9-b645-84cc39c2df30",
  "marked_for_delete": false,
  "overridden": false,
  "_system_owned": false,
  "_protection": "NOT_PROTECTED",
  "_create_time": 1760504110248,
  "_create_user": "wcp-cluster-user-f06fd228-8088-4439-a9e6-26c90a829c57-d34133d7-0fdf-4c9d-abcf-df83bd050a59",
  "_last_modified_time": 1760513242237,
  "_last_modified_user": "wcp-cluster-user-f06fd228-8088-4439-a9e6-26c90a829c57-d34133d7-0fdf-4c9d-abcf-df83bd050a59",
  "_revision": 1
}
```
<a id="49-policy-api-v1-infra-lb-virtual-servers-kube-apiserver-lb-svc-443-tcp-671rx"></a>
### 49. /policy/api/v1/infra/lb-virtual-servers/kube-apiserver-lb-svc_443_TCP_671rx

**HTTP Methods:** GET, PATCH

**Explanation:**
NSX Policy API endpoint for resource management.

---


**Sample Response Body (GET, from logs):**
```json
{
  "enabled": true,
  "ip_address": "172.24.94.45",
  "ports": [
    "443"
  ],
  "access_log_enabled": false,
  "lb_service_path": "/infra/lb-services/clusterip_f06fd228-8088-4439-a9e6-26c90a829c57_dlb",
  "pool_path": "/infra/lb-pools/kube-apiserver-lb-svc_443_TCP_671rx",
  "application_profile_path": "/infra/lb-app-profiles/default-tcp-lb-app-profile",
  "log_significant_event_only": false,
  "resource_type": "LBVirtualServer",
  "id": "kube-apiserver-lb-svc_443_TCP_671rx",
  "display_name": "kube-apiserver-lb-svc_443_TCP",
  "tags": [
    {
      "scope": "ncp/version",
      "tag": "1.2.0"
    },
    {
      "scope": "ncp/cluster",
      "tag": "f06fd228-8088-4439-a9e6-26c90a829c57"
    },
    {
      "scope": "ncp/project",
      "tag": "kube-system"
    },
    {
      "scope": "external_id",
      "tag": "a01886f2-3a06-4c6d-a70a-9a70601fc544"
    },
    {
      "scope": "ncp/service",
      "tag": "kube-apiserver-lb-svc"
    },
    {
      "scope": "ncp/service_uid",
      "tag": "a01886f2-3a06-4c6d-a70a-9a70601fc544"
    },
    {
      "scope": "ncp/service_port",
      "tag": "443"
    },
    {
      "scope": "ncp/service_port_protocol",
      "tag": "TCP"
    },
    {
      "scope": "ncp/created_for",
      "tag": "DLB"
    }
  ],
  "path": "/infra/lb-virtual-servers/kube-apiserver-lb-svc_443_TCP_671rx",
  "relative_path": "kube-apiserver-lb-svc_443_TCP_671rx",
  "parent_path": "/infra",
  "remote_path": "",
  "unique_id": "b780b700-5012-4583-beb1-cf889ff2a259",
  "realization_id": "b780b700-5012-4583-beb1-cf889ff2a259",
  "owner_id": "42495ba4-8c0b-49c9-b645-84cc39c2df30",
  "marked_for_delete": false,
  "overridden": false,
  "_system_owned": false,
  "_protection": "NOT_PROTECTED",
  "_create_time": 1760503483589,
  "_create_user": "wcp-cluster-user-f06fd228-8088-4439-a9e6-26c90a829c57-d34133d7-0fdf-4c9d-abcf-df83bd050a59",
  "_last_modified_time": 1760503490451,
  "_last_modified_user": "wcp-cluster-user-f06fd228-8088-4439-a9e6-26c90a829c57-d34133d7-0fdf-4c9d-abcf-df83bd050a59",
  "_revision": 1
}
```
<a id="50-policy-api-v1-infra-lb-virtual-servers-pinniped-supervisor-12001-tcp-ie6ph"></a>
### 50. /policy/api/v1/infra/lb-virtual-servers/pinniped-supervisor_12001_TCP_ie6ph

**HTTP Methods:** GET, PATCH

**Explanation:**
NSX Policy API endpoint for resource management.

---


**Sample Response Body (GET, from logs):**
```json
{
  "enabled": true,
  "ip_address": "172.24.103.74",
  "ports": [
    "12001"
  ],
  "access_log_enabled": false,
  "lb_service_path": "/infra/lb-services/clusterip_f06fd228-8088-4439-a9e6-26c90a829c57_dlb",
  "pool_path": "/infra/lb-pools/pinniped-supervisor_12001_TCP_ie6ph",
  "application_profile_path": "/infra/lb-app-profiles/default-tcp-lb-app-profile",
  "log_significant_event_only": false,
  "resource_type": "LBVirtualServer",
  "id": "pinniped-supervisor_12001_TCP_ie6ph",
  "display_name": "pinniped-supervisor_12001_TCP",
  "tags": [
    {
      "scope": "ncp/version",
      "tag": "1.2.0"
    },
    {
      "scope": "ncp/cluster",
      "tag": "f06fd228-8088-4439-a9e6-26c90a829c57"
    },
    {
      "scope": "ncp/project",
      "tag": "vmware-system-pinniped"
    },
    {
      "scope": "external_id",
      "tag": "1004cf52-f84d-4cc2-a96e-a8c7a1d0ab1a"
    },
    {
      "scope": "ncp/service",
      "tag": "pinniped-supervisor"
    },
    {
      "scope": "ncp/service_uid",
      "tag": "1004cf52-f84d-4cc2-a96e-a8c7a1d0ab1a"
    },
    {
      "scope": "ncp/service_port",
      "tag": "12001"
    },
    {
      "scope": "ncp/service_port_protocol",
      "tag": "TCP"
    },
    {
      "scope": "ncp/created_for",
      "tag": "DLB"
    }
  ],
  "path": "/infra/lb-virtual-servers/pinniped-supervisor_12001_TCP_ie6ph",
  "relative_path": "pinniped-supervisor_12001_TCP_ie6ph",
  "parent_path": "/infra",
  "remote_path": "",
  "unique_id": "53df1a69-f5ed-4c83-acad-41355659c36d",
  "realization_id": "53df1a69-f5ed-4c83-acad-41355659c36d",
  "owner_id": "42495ba4-8c0b-49c9-b645-84cc39c2df30",
  "marked_for_delete": false,
  "overridden": false,
  "_system_owned": false,
  "_protection": "NOT_PROTECTED",
  "_create_time": 1760503616750,
  "_create_user": "wcp-cluster-user-f06fd228-8088-4439-a9e6-26c90a829c57-d34133d7-0fdf-4c9d-abcf-df83bd050a59",
  "_last_modified_time": 1760513243103,
  "_last_modified_user": "wcp-cluster-user-f06fd228-8088-4439-a9e6-26c90a829c57-d34133d7-0fdf-4c9d-abcf-df83bd050a59",
  "_revision": 1
}
```
<a id="51-policy-api-v1-infra-lb-virtual-servers-kube-apiserver-lb-svc-6443-tcp-671rx"></a>
### 51. /policy/api/v1/infra/lb-virtual-servers/kube-apiserver-lb-svc_6443_TCP_671rx

**HTTP Methods:** GET, PATCH

**Explanation:**
NSX Policy API endpoint for resource management.

---


**Sample Response Body (GET, from logs):**
```json
{
  "enabled": true,
  "ip_address": "172.24.94.45",
  "ports": [
    "6443"
  ],
  "access_log_enabled": false,
  "lb_service_path": "/infra/lb-services/clusterip_f06fd228-8088-4439-a9e6-26c90a829c57_dlb",
  "pool_path": "/infra/lb-pools/kube-apiserver-lb-svc_6443_TCP_671rx",
  "application_profile_path": "/infra/lb-app-profiles/default-tcp-lb-app-profile",
  "log_significant_event_only": false,
  "resource_type": "LBVirtualServer",
  "id": "kube-apiserver-lb-svc_6443_TCP_671rx",
  "display_name": "kube-apiserver-lb-svc_6443_TCP",
  "tags": [
    {
      "scope": "ncp/version",
      "tag": "1.2.0"
    },
    {
      "scope": "ncp/cluster",
      "tag": "f06fd228-8088-4439-a9e6-26c90a829c57"
    },
    {
      "scope": "ncp/project",
      "tag": "kube-system"
    },
    {
      "scope": "external_id",
      "tag": "a01886f2-3a06-4c6d-a70a-9a70601fc544"
    },
    {
      "scope": "ncp/service",
      "tag": "kube-apiserver-lb-svc"
    },
    {
      "scope": "ncp/service_uid",
      "tag": "a01886f2-3a06-4c6d-a70a-9a70601fc544"
    },
    {
      "scope": "ncp/service_port",
      "tag": "6443"
    },
    {
      "scope": "ncp/service_port_protocol",
      "tag": "TCP"
    },
    {
      "scope": "ncp/created_for",
      "tag": "DLB"
    }
  ],
  "path": "/infra/lb-virtual-servers/kube-apiserver-lb-svc_6443_TCP_671rx",
  "relative_path": "kube-apiserver-lb-svc_6443_TCP_671rx",
  "parent_path": "/infra",
  "remote_path": "",
  "unique_id": "45691736-479f-437d-ad55-3239d48b4569",
  "realization_id": "45691736-479f-437d-ad55-3239d48b4569",
  "owner_id": "42495ba4-8c0b-49c9-b645-84cc39c2df30",
  "marked_for_delete": false,
  "overridden": false,
  "_system_owned": false,
  "_protection": "NOT_PROTECTED",
  "_create_time": 1760503486284,
  "_create_user": "wcp-cluster-user-f06fd228-8088-4439-a9e6-26c90a829c57-d34133d7-0fdf-4c9d-abcf-df83bd050a59",
  "_last_modified_time": 1760503490525,
  "_last_modified_user": "wcp-cluster-user-f06fd228-8088-4439-a9e6-26c90a829c57-d34133d7-0fdf-4c9d-abcf-df83bd050a59",
  "_revision": 1
}
```
<a id="52-policy-api-v1-infra-lb-virtual-servers-machine-agent-service-9443-tcp-6iexa"></a>
### 52. /policy/api/v1/infra/lb-virtual-servers/machine-agent-service_9443_TCP_6iexa

**HTTP Methods:** GET, PATCH

**Explanation:**
NSX Policy API endpoint for resource management.

---


**Sample Response Body (GET, from logs):**
```json
{
  "enabled": true,
  "ip_address": "172.24.215.39",
  "ports": [
    "9443"
  ],
  "access_log_enabled": false,
  "lb_service_path": "/infra/lb-services/clusterip_f06fd228-8088-4439-a9e6-26c90a829c57_dlb",
  "pool_path": "/infra/lb-pools/machine-agent-service_9443_TCP_6iexa",
  "application_profile_path": "/infra/lb-app-profiles/default-tcp-lb-app-profile",
  "log_significant_event_only": false,
  "resource_type": "LBVirtualServer",
  "id": "machine-agent-service_9443_TCP_6iexa",
  "display_name": "machine-agent-service_9443_TCP",
  "tags": [
    {
      "scope": "ncp/version",
      "tag": "1.2.0"
    },
    {
      "scope": "ncp/cluster",
      "tag": "f06fd228-8088-4439-a9e6-26c90a829c57"
    },
    {
      "scope": "ncp/project",
      "tag": "svc-tkg-jrsvf"
    },
    {
      "scope": "external_id",
      "tag": "7f54725a-3823-45cd-850f-21103284ec91"
    },
    {
      "scope": "ncp/service",
      "tag": "machine-agent-service"
    },
    {
      "scope": "ncp/service_uid",
      "tag": "7f54725a-3823-45cd-850f-21103284ec91"
    },
    {
      "scope": "ncp/service_port",
      "tag": "9443"
    },
    {
      "scope": "ncp/service_port_protocol",
      "tag": "TCP"
    },
    {
      "scope": "ncp/created_for",
      "tag": "DLB"
    }
  ],
  "path": "/infra/lb-virtual-servers/machine-agent-service_9443_TCP_6iexa",
  "relative_path": "machine-agent-service_9443_TCP_6iexa",
  "parent_path": "/infra",
  "remote_path": "",
  "unique_id": "a9edc24c-3bda-41e7-b8db-ec2ed12cb98c",
  "realization_id": "a9edc24c-3bda-41e7-b8db-ec2ed12cb98c",
  "owner_id": "42495ba4-8c0b-49c9-b645-84cc39c2df30",
  "marked_for_delete": false,
  "overridden": false,
  "_system_owned": false,
  "_protection": "NOT_PROTECTED",
  "_create_time": 1760504089660,
  "_create_user": "wcp-cluster-user-f06fd228-8088-4439-a9e6-26c90a829c57-d34133d7-0fdf-4c9d-abcf-df83bd050a59",
  "_last_modified_time": 1760504090841,
  "_last_modified_user": "wcp-cluster-user-f06fd228-8088-4439-a9e6-26c90a829c57-d34133d7-0fdf-4c9d-abcf-df83bd050a59",
  "_revision": 1
}
```
<a id="53-policy-api-v1-infra-lb-virtual-servers-pinniped-concierge-api-443-tcp-62uni"></a>
### 53. /policy/api/v1/infra/lb-virtual-servers/pinniped-concierge-api_443_TCP_62uni

**HTTP Methods:** GET, PATCH

**Explanation:**
NSX Policy API endpoint for resource management.

---


**Sample Response Body (GET, from logs):**
```json
{
  "enabled": true,
  "ip_address": "172.24.58.255",
  "ports": [
    "443"
  ],
  "access_log_enabled": false,
  "lb_service_path": "/infra/lb-services/clusterip_f06fd228-8088-4439-a9e6-26c90a829c57_dlb",
  "pool_path": "/infra/lb-pools/pinniped-concierge-api_443_TCP_62uni",
  "application_profile_path": "/infra/lb-app-profiles/default-tcp-lb-app-profile",
  "log_significant_event_only": false,
  "resource_type": "LBVirtualServer",
  "id": "pinniped-concierge-api_443_TCP_62uni",
  "display_name": "pinniped-concierge-api_443_TCP",
  "tags": [
    {
      "scope": "ncp/version",
      "tag": "1.2.0"
    },
    {
      "scope": "ncp/cluster",
      "tag": "f06fd228-8088-4439-a9e6-26c90a829c57"
    },
    {
      "scope": "ncp/project",
      "tag": "vmware-system-pinniped"
    },
    {
      "scope": "external_id",
      "tag": "c5862237-e4da-46b6-895d-8f3160d21288"
    },
    {
      "scope": "ncp/service",
      "tag": "pinniped-concierge-api"
    },
    {
      "scope": "ncp/service_uid",
      "tag": "c5862237-e4da-46b6-895d-8f3160d21288"
    },
    {
      "scope": "ncp/service_port",
      "tag": "443"
    },
    {
      "scope": "ncp/service_port_protocol",
      "tag": "TCP"
    },
    {
      "scope": "ncp/created_for",
      "tag": "DLB"
    }
  ],
  "path": "/infra/lb-virtual-servers/pinniped-concierge-api_443_TCP_62uni",
  "relative_path": "pinniped-concierge-api_443_TCP_62uni",
  "parent_path": "/infra",
  "remote_path": "",
  "unique_id": "131d030c-cff5-488a-9ea7-ea2162602ce6",
  "realization_id": "131d030c-cff5-488a-9ea7-ea2162602ce6",
  "owner_id": "42495ba4-8c0b-49c9-b645-84cc39c2df30",
  "marked_for_delete": false,
  "overridden": false,
  "_system_owned": false,
  "_protection": "NOT_PROTECTED",
  "_create_time": 1760503623337,
  "_create_user": "wcp-cluster-user-f06fd228-8088-4439-a9e6-26c90a829c57-d34133d7-0fdf-4c9d-abcf-df83bd050a59",
  "_last_modified_time": 1760513238301,
  "_last_modified_user": "wcp-cluster-user-f06fd228-8088-4439-a9e6-26c90a829c57-d34133d7-0fdf-4c9d-abcf-df83bd050a59",
  "_revision": 1
}
```
<a id="54-policy-api-v1-infra-lb-virtual-servers-pinniped-supervisor-api-443-tcp-l261w"></a>
### 54. /policy/api/v1/infra/lb-virtual-servers/pinniped-supervisor-api_443_TCP_l261w

**HTTP Methods:** GET, PATCH

**Explanation:**
NSX Policy API endpoint for resource management.

---


**Sample Response Body (GET, from logs):**
```json
{
  "enabled": true,
  "ip_address": "172.24.254.237",
  "ports": [
    "443"
  ],
  "access_log_enabled": false,
  "lb_service_path": "/infra/lb-services/clusterip_f06fd228-8088-4439-a9e6-26c90a829c57_dlb",
  "pool_path": "/infra/lb-pools/pinniped-supervisor-api_443_TCP_l261w",
  "application_profile_path": "/infra/lb-app-profiles/default-tcp-lb-app-profile",
  "log_significant_event_only": false,
  "resource_type": "LBVirtualServer",
  "id": "pinniped-supervisor-api_443_TCP_l261w",
  "display_name": "pinniped-supervisor-api_443_TCP",
  "tags": [
    {
      "scope": "ncp/version",
      "tag": "1.2.0"
    },
    {
      "scope": "ncp/cluster",
      "tag": "f06fd228-8088-4439-a9e6-26c90a829c57"
    },
    {
      "scope": "ncp/project",
      "tag": "vmware-system-pinniped"
    },
    {
      "scope": "external_id",
      "tag": "df00cd38-ecae-421c-93cb-85e002473ae9"
    },
    {
      "scope": "ncp/service",
      "tag": "pinniped-supervisor-api"
    },
    {
      "scope": "ncp/service_uid",
      "tag": "df00cd38-ecae-421c-93cb-85e002473ae9"
    },
    {
      "scope": "ncp/service_port",
      "tag": "443"
    },
    {
      "scope": "ncp/service_port_protocol",
      "tag": "TCP"
    },
    {
      "scope": "ncp/created_for",
      "tag": "DLB"
    }
  ],
  "path": "/infra/lb-virtual-servers/pinniped-supervisor-api_443_TCP_l261w",
  "relative_path": "pinniped-supervisor-api_443_TCP_l261w",
  "parent_path": "/infra",
  "remote_path": "",
  "unique_id": "3134c388-e6cc-4ad1-a8f6-9971ff254151",
  "realization_id": "3134c388-e6cc-4ad1-a8f6-9971ff254151",
  "owner_id": "42495ba4-8c0b-49c9-b645-84cc39c2df30",
  "marked_for_delete": false,
  "overridden": false,
  "_system_owned": false,
  "_protection": "NOT_PROTECTED",
  "_create_time": 1760503626454,
  "_create_user": "wcp-cluster-user-f06fd228-8088-4439-a9e6-26c90a829c57-d34133d7-0fdf-4c9d-abcf-df83bd050a59",
  "_last_modified_time": 1760513235223,
  "_last_modified_user": "wcp-cluster-user-f06fd228-8088-4439-a9e6-26c90a829c57-d34133d7-0fdf-4c9d-abcf-df83bd050a59",
  "_revision": 1
}
```
<a id="55-policy-api-v1-infra-lb-virtual-servers-vsphere-csi-controller-2112-tcp-rz7ds"></a>
### 55. /policy/api/v1/infra/lb-virtual-servers/vsphere-csi-controller_2112_TCP_rz7ds

**HTTP Methods:** GET, PATCH

**Explanation:**
NSX Policy API endpoint for resource management.

---


**Sample Response Body (GET, from logs):**
```json
{
  "enabled": true,
  "ip_address": "172.24.149.47",
  "ports": [
    "2112"
  ],
  "access_log_enabled": false,
  "lb_service_path": "/infra/lb-services/clusterip_f06fd228-8088-4439-a9e6-26c90a829c57_dlb",
  "pool_path": "/infra/lb-pools/vsphere-csi-controller_2112_TCP_rz7ds",
  "application_profile_path": "/infra/lb-app-profiles/default-tcp-lb-app-profile",
  "log_significant_event_only": false,
  "resource_type": "LBVirtualServer",
  "id": "vsphere-csi-controller_2112_TCP_rz7ds",
  "display_name": "vsphere-csi-controller_2112_TCP",
  "tags": [
    {
      "scope": "ncp/version",
      "tag": "1.2.0"
    },
    {
      "scope": "ncp/cluster",
      "tag": "f06fd228-8088-4439-a9e6-26c90a829c57"
    },
    {
      "scope": "ncp/project",
      "tag": "vmware-system-csi"
    },
    {
      "scope": "external_id",
      "tag": "6b7df57d-9733-4dec-9cc9-e8d91da2c850"
    },
    {
      "scope": "ncp/service",
      "tag": "vsphere-csi-controller"
    },
    {
      "scope": "ncp/service_uid",
      "tag": "6b7df57d-9733-4dec-9cc9-e8d91da2c850"
    },
    {
      "scope": "ncp/service_port",
      "tag": "2112"
    },
    {
      "scope": "ncp/service_port_protocol",
      "tag": "TCP"
    },
    {
      "scope": "ncp/created_for",
      "tag": "DLB"
    }
  ],
  "path": "/infra/lb-virtual-servers/vsphere-csi-controller_2112_TCP_rz7ds",
  "relative_path": "vsphere-csi-controller_2112_TCP_rz7ds",
  "parent_path": "/infra",
  "remote_path": "",
  "unique_id": "51237650-4dcd-4cac-ac95-309e64f746f4",
  "realization_id": "51237650-4dcd-4cac-ac95-309e64f746f4",
  "owner_id": "42495ba4-8c0b-49c9-b645-84cc39c2df30",
  "marked_for_delete": false,
  "overridden": false,
  "_system_owned": false,
  "_protection": "NOT_PROTECTED",
  "_create_time": 1760503452419,
  "_create_user": "wcp-cluster-user-f06fd228-8088-4439-a9e6-26c90a829c57-d34133d7-0fdf-4c9d-abcf-df83bd050a59",
  "_last_modified_time": 1760503622028,
  "_last_modified_user": "wcp-cluster-user-f06fd228-8088-4439-a9e6-26c90a829c57-d34133d7-0fdf-4c9d-abcf-df83bd050a59",
  "_revision": 1
}
```
<a id="56-policy-api-v1-infra-lb-virtual-servers-vsphere-csi-controller-2113-tcp-rz7ds"></a>
### 56. /policy/api/v1/infra/lb-virtual-servers/vsphere-csi-controller_2113_TCP_rz7ds

**HTTP Methods:** GET, PATCH

**Explanation:**
NSX Policy API endpoint for resource management.

---


**Sample Response Body (GET, from logs):**
```json
{
  "enabled": true,
  "ip_address": "172.24.149.47",
  "ports": [
    "2113"
  ],
  "access_log_enabled": false,
  "lb_service_path": "/infra/lb-services/clusterip_f06fd228-8088-4439-a9e6-26c90a829c57_dlb",
  "pool_path": "/infra/lb-pools/vsphere-csi-controller_2113_TCP_rz7ds",
  "application_profile_path": "/infra/lb-app-profiles/default-tcp-lb-app-profile",
  "log_significant_event_only": false,
  "resource_type": "LBVirtualServer",
  "id": "vsphere-csi-controller_2113_TCP_rz7ds",
  "display_name": "vsphere-csi-controller_2113_TCP",
  "tags": [
    {
      "scope": "ncp/version",
      "tag": "1.2.0"
    },
    {
      "scope": "ncp/cluster",
      "tag": "f06fd228-8088-4439-a9e6-26c90a829c57"
    },
    {
      "scope": "ncp/project",
      "tag": "vmware-system-csi"
    },
    {
      "scope": "external_id",
      "tag": "6b7df57d-9733-4dec-9cc9-e8d91da2c850"
    },
    {
      "scope": "ncp/service",
      "tag": "vsphere-csi-controller"
    },
    {
      "scope": "ncp/service_uid",
      "tag": "6b7df57d-9733-4dec-9cc9-e8d91da2c850"
    },
    {
      "scope": "ncp/service_port",
      "tag": "2113"
    },
    {
      "scope": "ncp/service_port_protocol",
      "tag": "TCP"
    },
    {
      "scope": "ncp/created_for",
      "tag": "DLB"
    }
  ],
  "path": "/infra/lb-virtual-servers/vsphere-csi-controller_2113_TCP_rz7ds",
  "relative_path": "vsphere-csi-controller_2113_TCP_rz7ds",
  "parent_path": "/infra",
  "remote_path": "",
  "unique_id": "34949171-2166-4191-b1bb-62bbac3ba2cb",
  "realization_id": "34949171-2166-4191-b1bb-62bbac3ba2cb",
  "owner_id": "42495ba4-8c0b-49c9-b645-84cc39c2df30",
  "marked_for_delete": false,
  "overridden": false,
  "_system_owned": false,
  "_protection": "NOT_PROTECTED",
  "_create_time": 1760503456768,
  "_create_user": "wcp-cluster-user-f06fd228-8088-4439-a9e6-26c90a829c57-d34133d7-0fdf-4c9d-abcf-df83bd050a59",
  "_last_modified_time": 1760503622194,
  "_last_modified_user": "wcp-cluster-user-f06fd228-8088-4439-a9e6-26c90a829c57-d34133d7-0fdf-4c9d-abcf-df83bd050a59",
  "_revision": 1
}
```
<a id="57-policy-api-v1-infra-lb-virtual-servers-pinniped-concierge-proxy-443-tcp-1miab"></a>
### 57. /policy/api/v1/infra/lb-virtual-servers/pinniped-concierge-proxy_443_TCP_1miab

**HTTP Methods:** GET, PATCH

**Explanation:**
NSX Policy API endpoint for resource management.

---


**Sample Response Body (GET, from logs):**
```json
{
  "enabled": true,
  "ip_address": "172.24.186.168",
  "ports": [
    "443"
  ],
  "access_log_enabled": false,
  "lb_service_path": "/infra/lb-services/clusterip_f06fd228-8088-4439-a9e6-26c90a829c57_dlb",
  "pool_path": "/infra/lb-pools/pinniped-concierge-proxy_443_TCP_1miab",
  "application_profile_path": "/infra/lb-app-profiles/default-tcp-lb-app-profile",
  "log_significant_event_only": false,
  "resource_type": "LBVirtualServer",
  "id": "pinniped-concierge-proxy_443_TCP_1miab",
  "display_name": "pinniped-concierge-proxy_443_TCP",
  "tags": [
    {
      "scope": "ncp/version",
      "tag": "1.2.0"
    },
    {
      "scope": "ncp/cluster",
      "tag": "f06fd228-8088-4439-a9e6-26c90a829c57"
    },
    {
      "scope": "ncp/project",
      "tag": "vmware-system-pinniped"
    },
    {
      "scope": "external_id",
      "tag": "3dc1d4ce-5cb6-4572-af1b-ae9541018986"
    },
    {
      "scope": "ncp/service",
      "tag": "pinniped-concierge-proxy"
    },
    {
      "scope": "ncp/service_uid",
      "tag": "3dc1d4ce-5cb6-4572-af1b-ae9541018986"
    },
    {
      "scope": "ncp/service_port",
      "tag": "443"
    },
    {
      "scope": "ncp/service_port_protocol",
      "tag": "TCP"
    },
    {
      "scope": "ncp/created_for",
      "tag": "DLB"
    }
  ],
  "path": "/infra/lb-virtual-servers/pinniped-concierge-proxy_443_TCP_1miab",
  "relative_path": "pinniped-concierge-proxy_443_TCP_1miab",
  "parent_path": "/infra",
  "remote_path": "",
  "unique_id": "731e4375-4be4-4ff0-bdc5-d0e2027a7ca2",
  "realization_id": "731e4375-4be4-4ff0-bdc5-d0e2027a7ca2",
  "owner_id": "42495ba4-8c0b-49c9-b645-84cc39c2df30",
  "marked_for_delete": false,
  "overridden": false,
  "_system_owned": false,
  "_protection": "NOT_PROTECTED",
  "_create_time": 1760503615714,
  "_create_user": "wcp-cluster-user-f06fd228-8088-4439-a9e6-26c90a829c57-d34133d7-0fdf-4c9d-abcf-df83bd050a59",
  "_last_modified_time": 1760513239475,
  "_last_modified_user": "wcp-cluster-user-f06fd228-8088-4439-a9e6-26c90a829c57-d34133d7-0fdf-4c9d-abcf-df83bd050a59",
  "_revision": 1
}
```
<a id="58-policy-api-v1-infra-lb-virtual-servers-snapshot-validation-service-443-tcp-8p66x"></a>
### 58. /policy/api/v1/infra/lb-virtual-servers/snapshot-validation-service_443_TCP_8p66x

**HTTP Methods:** GET, PATCH

**Explanation:**
NSX Policy API endpoint for resource management.

---


**Sample Response Body (GET, from logs):**
```json
{
  "enabled": true,
  "ip_address": "172.24.4.242",
  "ports": [
    "443"
  ],
  "access_log_enabled": false,
  "lb_service_path": "/infra/lb-services/clusterip_f06fd228-8088-4439-a9e6-26c90a829c57_dlb",
  "pool_path": "/infra/lb-pools/snapshot-validation-service_443_TCP_8p66x",
  "application_profile_path": "/infra/lb-app-profiles/default-tcp-lb-app-profile",
  "log_significant_event_only": false,
  "resource_type": "LBVirtualServer",
  "id": "snapshot-validation-service_443_TCP_8p66x",
  "display_name": "snapshot-validation-service_443_TCP",
  "tags": [
    {
      "scope": "ncp/version",
      "tag": "1.2.0"
    },
    {
      "scope": "ncp/cluster",
      "tag": "f06fd228-8088-4439-a9e6-26c90a829c57"
    },
    {
      "scope": "ncp/project",
      "tag": "kube-system"
    },
    {
      "scope": "external_id",
      "tag": "9a3955ca-e0d6-4379-b1c1-66550c4a592c"
    },
    {
      "scope": "ncp/service",
      "tag": "snapshot-validation-service"
    },
    {
      "scope": "ncp/service_uid",
      "tag": "9a3955ca-e0d6-4379-b1c1-66550c4a592c"
    },
    {
      "scope": "ncp/service_port",
      "tag": "443"
    },
    {
      "scope": "ncp/service_port_protocol",
      "tag": "TCP"
    },
    {
      "scope": "ncp/created_for",
      "tag": "DLB"
    }
  ],
  "path": "/infra/lb-virtual-servers/snapshot-validation-service_443_TCP_8p66x",
  "relative_path": "snapshot-validation-service_443_TCP_8p66x",
  "parent_path": "/infra",
  "remote_path": "",
  "unique_id": "1dc95a6b-49e5-4088-ad6d-c0feef3dfb69",
  "realization_id": "1dc95a6b-49e5-4088-ad6d-c0feef3dfb69",
  "owner_id": "42495ba4-8c0b-49c9-b645-84cc39c2df30",
  "marked_for_delete": false,
  "overridden": false,
  "_system_owned": false,
  "_protection": "NOT_PROTECTED",
  "_create_time": 1760503456574,
  "_create_user": "wcp-cluster-user-f06fd228-8088-4439-a9e6-26c90a829c57-d34133d7-0fdf-4c9d-abcf-df83bd050a59",
  "_last_modified_time": 1760503623218,
  "_last_modified_user": "wcp-cluster-user-f06fd228-8088-4439-a9e6-26c90a829c57-d34133d7-0fdf-4c9d-abcf-df83bd050a59",
  "_revision": 1
}
```
<a id="59-policy-api-v1-infra-lb-virtual-servers-upgrade-compatibility-service-80-tcp-gdqw0"></a>
### 59. /policy/api/v1/infra/lb-virtual-servers/upgrade-compatibility-service_80_TCP_gdqw0

**HTTP Methods:** GET, PATCH

**Explanation:**
NSX Policy API endpoint for resource management.

---


**Sample Response Body (GET, from logs):**
```json
{
  "enabled": true,
  "ip_address": "172.24.114.119",
  "ports": [
    "80"
  ],
  "access_log_enabled": false,
  "lb_service_path": "/infra/lb-services/clusterip_f06fd228-8088-4439-a9e6-26c90a829c57_dlb",
  "pool_path": "/infra/lb-pools/upgrade-compatibility-service_80_TCP_gdqw0",
  "application_profile_path": "/infra/lb-app-profiles/default-tcp-lb-app-profile",
  "log_significant_event_only": false,
  "resource_type": "LBVirtualServer",
  "id": "upgrade-compatibility-service_80_TCP_gdqw0",
  "display_name": "upgrade-compatibility-service_80_TCP",
  "tags": [
    {
      "scope": "ncp/version",
      "tag": "1.2.0"
    },
    {
      "scope": "ncp/cluster",
      "tag": "f06fd228-8088-4439-a9e6-26c90a829c57"
    },
    {
      "scope": "ncp/project",
      "tag": "svc-tkg-jrsvf"
    },
    {
      "scope": "external_id",
      "tag": "081d01a3-773f-42f5-8b42-c616fc95d7fa"
    },
    {
      "scope": "ncp/service",
      "tag": "upgrade-compatibility-service"
    },
    {
      "scope": "ncp/service_uid",
      "tag": "081d01a3-773f-42f5-8b42-c616fc95d7fa"
    },
    {
      "scope": "ncp/service_port",
      "tag": "80"
    },
    {
      "scope": "ncp/service_port_protocol",
      "tag": "TCP"
    },
    {
      "scope": "ncp/created_for",
      "tag": "DLB"
    }
  ],
  "path": "/infra/lb-virtual-servers/upgrade-compatibility-service_80_TCP_gdqw0",
  "relative_path": "upgrade-compatibility-service_80_TCP_gdqw0",
  "parent_path": "/infra",
  "remote_path": "",
  "unique_id": "19561b7b-56bd-4fe5-ae1d-056662b5f9c1",
  "realization_id": "19561b7b-56bd-4fe5-ae1d-056662b5f9c1",
  "owner_id": "42495ba4-8c0b-49c9-b645-84cc39c2df30",
  "marked_for_delete": false,
  "overridden": false,
  "_system_owned": false,
  "_protection": "NOT_PROTECTED",
  "_create_time": 1760504252264,
  "_create_user": "wcp-cluster-user-f06fd228-8088-4439-a9e6-26c90a829c57-d34133d7-0fdf-4c9d-abcf-df83bd050a59",
  "_last_modified_time": 1760504253920,
  "_last_modified_user": "wcp-cluster-user-f06fd228-8088-4439-a9e6-26c90a829c57-d34133d7-0fdf-4c9d-abcf-df83bd050a59",
  "_revision": 1
}
```
<a id="60-policy-api-v1-infra-lb-virtual-servers-kube-apiserver-authproxy-svc-8443-tcp-hwe7d"></a>
### 60. /policy/api/v1/infra/lb-virtual-servers/kube-apiserver-authproxy-svc_8443_TCP_hwe7d

**HTTP Methods:** GET, PATCH

**Explanation:**
NSX Policy API endpoint for resource management.

---


**Sample Response Body (GET, from logs):**
```json
{
  "enabled": true,
  "ip_address": "172.24.31.48",
  "ports": [
    "8443"
  ],
  "access_log_enabled": false,
  "lb_service_path": "/infra/lb-services/clusterip_f06fd228-8088-4439-a9e6-26c90a829c57_dlb",
  "pool_path": "/infra/lb-pools/kube-apiserver-authproxy-svc_8443_TCP_hwe7d",
  "application_profile_path": "/infra/lb-app-profiles/default-tcp-lb-app-profile",
  "log_significant_event_only": false,
  "resource_type": "LBVirtualServer",
  "id": "kube-apiserver-authproxy-svc_8443_TCP_hwe7d",
  "display_name": "kube-apiserver-authproxy-svc_8443_TCP",
  "tags": [
    {
      "scope": "ncp/version",
      "tag": "1.2.0"
    },
    {
      "scope": "ncp/cluster",
      "tag": "f06fd228-8088-4439-a9e6-26c90a829c57"
    },
    {
      "scope": "ncp/project",
      "tag": "kube-system"
    },
    {
      "scope": "external_id",
      "tag": "5d58effa-6c7c-4122-8a88-e89fd8981636"
    },
    {
      "scope": "ncp/service",
      "tag": "kube-apiserver-authproxy-svc"
    },
    {
      "scope": "ncp/service_uid",
      "tag": "5d58effa-6c7c-4122-8a88-e89fd8981636"
    },
    {
      "scope": "ncp/service_port",
      "tag": "8443"
    },
    {
      "scope": "ncp/service_port_protocol",
      "tag": "TCP"
    },
    {
      "scope": "ncp/created_for",
      "tag": "DLB"
    }
  ],
  "path": "/infra/lb-virtual-servers/kube-apiserver-authproxy-svc_8443_TCP_hwe7d",
  "relative_path": "kube-apiserver-authproxy-svc_8443_TCP_hwe7d",
  "parent_path": "/infra",
  "remote_path": "",
  "unique_id": "75b63a92-ad68-431b-a61a-7d68b797e30c",
  "realization_id": "75b63a92-ad68-431b-a61a-7d68b797e30c",
  "owner_id": "42495ba4-8c0b-49c9-b645-84cc39c2df30",
  "marked_for_delete": false,
  "overridden": false,
  "_system_owned": false,
  "_protection": "NOT_PROTECTED",
  "_create_time": 1760504034948,
  "_create_user": "wcp-cluster-user-f06fd228-8088-4439-a9e6-26c90a829c57-d34133d7-0fdf-4c9d-abcf-df83bd050a59",
  "_last_modified_time": 1760513234022,
  "_last_modified_user": "wcp-cluster-user-f06fd228-8088-4439-a9e6-26c90a829c57-d34133d7-0fdf-4c9d-abcf-df83bd050a59",
  "_revision": 1
}
```
<a id="61-policy-api-v1-infra-lb-virtual-servers-storage-quota-webhook-service-443-tcp-q6397"></a>
### 61. /policy/api/v1/infra/lb-virtual-servers/storage-quota-webhook-service_443_TCP_q6397

**HTTP Methods:** GET, PATCH

**Explanation:**
NSX Policy API endpoint for resource management.

---


**Sample Response Body (GET, from logs):**
```json
{
  "enabled": true,
  "ip_address": "172.24.125.158",
  "ports": [
    "443"
  ],
  "access_log_enabled": false,
  "lb_service_path": "/infra/lb-services/clusterip_f06fd228-8088-4439-a9e6-26c90a829c57_dlb",
  "pool_path": "/infra/lb-pools/storage-quota-webhook-service_443_TCP_q6397",
  "application_profile_path": "/infra/lb-app-profiles/default-tcp-lb-app-profile",
  "log_significant_event_only": false,
  "resource_type": "LBVirtualServer",
  "id": "storage-quota-webhook-service_443_TCP_q6397",
  "display_name": "storage-quota-webhook-service_443_TCP",
  "tags": [
    {
      "scope": "ncp/version",
      "tag": "1.2.0"
    },
    {
      "scope": "ncp/cluster",
      "tag": "f06fd228-8088-4439-a9e6-26c90a829c57"
    },
    {
      "scope": "ncp/project",
      "tag": "kube-system"
    },
    {
      "scope": "external_id",
      "tag": "5911a025-1a7f-45bb-8930-a7cc1770c42e"
    },
    {
      "scope": "ncp/service",
      "tag": "storage-quota-webhook-service"
    },
    {
      "scope": "ncp/service_uid",
      "tag": "5911a025-1a7f-45bb-8930-a7cc1770c42e"
    },
    {
      "scope": "ncp/service_port",
      "tag": "443"
    },
    {
      "scope": "ncp/service_port_protocol",
      "tag": "TCP"
    },
    {
      "scope": "ncp/created_for",
      "tag": "DLB"
    }
  ],
  "path": "/infra/lb-virtual-servers/storage-quota-webhook-service_443_TCP_q6397",
  "relative_path": "storage-quota-webhook-service_443_TCP_q6397",
  "parent_path": "/infra",
  "remote_path": "",
  "unique_id": "5d1f2661-9fb3-4bf1-af05-b1156e6612bb",
  "realization_id": "5d1f2661-9fb3-4bf1-af05-b1156e6612bb",
  "owner_id": "42495ba4-8c0b-49c9-b645-84cc39c2df30",
  "marked_for_delete": false,
  "overridden": false,
  "_system_owned": false,
  "_protection": "NOT_PROTECTED",
  "_create_time": 1760503462839,
  "_create_user": "wcp-cluster-user-f06fd228-8088-4439-a9e6-26c90a829c57-d34133d7-0fdf-4c9d-abcf-df83bd050a59",
  "_last_modified_time": 1760503622029,
  "_last_modified_user": "wcp-cluster-user-f06fd228-8088-4439-a9e6-26c90a829c57-d34133d7-0fdf-4c9d-abcf-df83bd050a59",
  "_revision": 1
}
```
<a id="62-policy-api-v1-infra-lb-virtual-servers-cns-vsphere-vmware-com-service-443-tcp-fbd1t"></a>
### 62. /policy/api/v1/infra/lb-virtual-servers/cns-vsphere-vmware-com-service_443_TCP_fbd1t

**HTTP Methods:** GET, PATCH

**Explanation:**
NSX Policy API endpoint for resource management.

---


**Sample Response Body (GET, from logs):**
```json
{
  "enabled": true,
  "ip_address": "172.24.179.51",
  "ports": [
    "443"
  ],
  "access_log_enabled": false,
  "lb_service_path": "/infra/lb-services/clusterip_f06fd228-8088-4439-a9e6-26c90a829c57_dlb",
  "pool_path": "/infra/lb-pools/cns-vsphere-vmware-com-service_443_TCP_fbd1t",
  "application_profile_path": "/infra/lb-app-profiles/default-tcp-lb-app-profile",
  "log_significant_event_only": false,
  "resource_type": "LBVirtualServer",
  "id": "cns-vsphere-vmware-com-service_443_TCP_fbd1t",
  "display_name": "cns-vsphere-vmware-com-service_443_TCP",
  "tags": [
    {
      "scope": "ncp/version",
      "tag": "1.2.0"
    },
    {
      "scope": "ncp/cluster",
      "tag": "f06fd228-8088-4439-a9e6-26c90a829c57"
    },
    {
      "scope": "ncp/project",
      "tag": "kube-system"
    },
    {
      "scope": "external_id",
      "tag": "7b73380a-d3d3-44c9-92ad-83b257b86911"
    },
    {
      "scope": "ncp/service",
      "tag": "cns-vsphere-vmware-com-service"
    },
    {
      "scope": "ncp/service_uid",
      "tag": "7b73380a-d3d3-44c9-92ad-83b257b86911"
    },
    {
      "scope": "ncp/service_port",
      "tag": "443"
    },
    {
      "scope": "ncp/service_port_protocol",
      "tag": "TCP"
    },
    {
      "scope": "ncp/created_for",
      "tag": "DLB"
    }
  ],
  "path": "/infra/lb-virtual-servers/cns-vsphere-vmware-com-service_443_TCP_fbd1t",
  "relative_path": "cns-vsphere-vmware-com-service_443_TCP_fbd1t",
  "parent_path": "/infra",
  "remote_path": "",
  "unique_id": "4105c0c6-bd98-442d-a80e-e0c869f9588e",
  "realization_id": "4105c0c6-bd98-442d-a80e-e0c869f9588e",
  "owner_id": "42495ba4-8c0b-49c9-b645-84cc39c2df30",
  "marked_for_delete": false,
  "overridden": false,
  "_system_owned": false,
  "_protection": "NOT_PROTECTED",
  "_create_time": 1760503466446,
  "_create_user": "wcp-cluster-user-f06fd228-8088-4439-a9e6-26c90a829c57-d34133d7-0fdf-4c9d-abcf-df83bd050a59",
  "_last_modified_time": 1760503613730,
  "_last_modified_user": "wcp-cluster-user-f06fd228-8088-4439-a9e6-26c90a829c57-d34133d7-0fdf-4c9d-abcf-df83bd050a59",
  "_revision": 1
}
```
<a id="63-policy-api-v1-infra-lb-virtual-servers-tkr-conversion-webhook-service-443-tcp-sxd9x"></a>
### 63. /policy/api/v1/infra/lb-virtual-servers/tkr-conversion-webhook-service_443_TCP_sxd9x

**HTTP Methods:** GET, PATCH

**Explanation:**
NSX Policy API endpoint for resource management.

---


**Sample Response Body (GET, from logs):**
```json
{
  "enabled": true,
  "ip_address": "172.24.254.72",
  "ports": [
    "443"
  ],
  "access_log_enabled": false,
  "lb_service_path": "/infra/lb-services/clusterip_f06fd228-8088-4439-a9e6-26c90a829c57_dlb",
  "pool_path": "/infra/lb-pools/tkr-conversion-webhook-service_443_TCP_sxd9x",
  "application_profile_path": "/infra/lb-app-profiles/default-tcp-lb-app-profile",
  "log_significant_event_only": false,
  "resource_type": "LBVirtualServer",
  "id": "tkr-conversion-webhook-service_443_TCP_sxd9x",
  "display_name": "tkr-conversion-webhook-service_443_TCP",
  "tags": [
    {
      "scope": "ncp/version",
      "tag": "1.2.0"
    },
    {
      "scope": "ncp/cluster",
      "tag": "f06fd228-8088-4439-a9e6-26c90a829c57"
    },
    {
      "scope": "ncp/project",
      "tag": "svc-tkg-jrsvf"
    },
    {
      "scope": "external_id",
      "tag": "f387c6c0-4b5e-4a5a-8799-d40498defb5a"
    },
    {
      "scope": "ncp/service",
      "tag": "tkr-conversion-webhook-service"
    },
    {
      "scope": "ncp/service_uid",
      "tag": "f387c6c0-4b5e-4a5a-8799-d40498defb5a"
    },
    {
      "scope": "ncp/service_port",
      "tag": "443"
    },
    {
      "scope": "ncp/service_port_protocol",
      "tag": "TCP"
    },
    {
      "scope": "ncp/created_for",
      "tag": "DLB"
    }
  ],
  "path": "/infra/lb-virtual-servers/tkr-conversion-webhook-service_443_TCP_sxd9x",
  "relative_path": "tkr-conversion-webhook-service_443_TCP_sxd9x",
  "parent_path": "/infra",
  "remote_path": "",
  "unique_id": "2382f514-4821-4fe4-b157-9d664b1919ef",
  "realization_id": "2382f514-4821-4fe4-b157-9d664b1919ef",
  "owner_id": "42495ba4-8c0b-49c9-b645-84cc39c2df30",
  "marked_for_delete": false,
  "overridden": false,
  "_system_owned": false,
  "_protection": "NOT_PROTECTED",
  "_create_time": 1760504041514,
  "_create_user": "wcp-cluster-user-f06fd228-8088-4439-a9e6-26c90a829c57-d34133d7-0fdf-4c9d-abcf-df83bd050a59",
  "_last_modified_time": 1760504043101,
  "_last_modified_user": "wcp-cluster-user-f06fd228-8088-4439-a9e6-26c90a829c57-d34133d7-0fdf-4c9d-abcf-df83bd050a59",
  "_revision": 1
}
```
<a id="64-policy-api-v1-infra-lb-pools-vmware-system-nsx-operator-webhook-service-443-tcp-apze8"></a>
### 64. /policy/api/v1/infra/lb-pools/vmware-system-nsx-operator-webhook-service_443_TCP_apze8

**HTTP Methods:** GET, PATCH

**Explanation:**
NSX Policy API endpoint for resource management.

---


**Sample Response Body (GET, from logs):**
```json
{
  "algorithm": "ROUND_ROBIN",
  "snat_translation": {
    "type": "LBSnatDisabled"
  },
  "tcp_multiplexing_enabled": false,
  "tcp_multiplexing_number": 6,
  "min_active_members": 1,
  "resource_type": "LBPool",
  "id": "vmware-system-nsx-operator-webhook-service_443_TCP_apze8",
  "display_name": "vmware-system-nsx-operator-webhook-service_443_TCP",
  "tags": [
    {
      "scope": "ncp/version",
      "tag": "1.2.0"
    },
    {
      "scope": "ncp/cluster",
      "tag": "f06fd228-8088-4439-a9e6-26c90a829c57"
    },
    {
      "scope": "ncp/project",
      "tag": "vmware-system-nsx"
    },
    {
      "scope": "external_id",
      "tag": "417c1230-e1f1-4049-9bdc-8f619032b163"
    },
    {
      "scope": "ncp/service",
      "tag": "vmware-system-nsx-operator-webhook-service"
    },
    {
      "scope": "ncp/service_uid",
      "tag": "417c1230-e1f1-4049-9bdc-8f619032b163"
    },
    {
      "scope": "ncp/service_port",
      "tag": "443"
    },
    {
      "scope": "ncp/service_port_protocol",
      "tag": "TCP"
    },
    {
      "scope": "ncp/created_for",
      "tag": "DLB"
    }
  ],
  "path": "/infra/lb-pools/vmware-system-nsx-operator-webhook-service_443_TCP_apze8",
  "relative_path": "vmware-system-nsx-operator-webhook-service_443_TCP_apze8",
  "parent_path": "/infra",
  "remote_path": "",
  "unique_id": "ecd14e0c-42e1-49fc-a260-a5b71a4f9326",
  "realization_id": "ecd14e0c-42e1-49fc-a260-a5b71a4f9326",
  "owner_id": "42495ba4-8c0b-49c9-b645-84cc39c2df30",
  "marked_for_delete": false,
  "overridden": false,
  "_system_owned": false,
  "_protection": "NOT_PROTECTED",
  "_create_time": 1760503462317,
  "_create_user": "wcp-cluster-user-f06fd228-8088-4439-a9e6-26c90a829c57-d34133d7-0fdf-4c9d-abcf-df83bd050a59",
  "_last_modified_time": 1760688836098,
  "_last_modified_user": "wcp-cluster-user-f06fd228-8088-4439-a9e6-26c90a829c57-d34133d7-0fdf-4c9d-abcf-df83bd050a59",
  "_revision": 13
}
```
<a id="65-policy-api-v1-infra-lb-virtual-servers-runtime-extension-webhook-service-443-tcp-snr9y"></a>
### 65. /policy/api/v1/infra/lb-virtual-servers/runtime-extension-webhook-service_443_TCP_snr9y

**HTTP Methods:** GET, PATCH

**Explanation:**
NSX Policy API endpoint for resource management.

---


**Sample Response Body (GET, from logs):**
```json
{
  "enabled": true,
  "ip_address": "172.24.195.117",
  "ports": [
    "443"
  ],
  "access_log_enabled": false,
  "lb_service_path": "/infra/lb-services/clusterip_f06fd228-8088-4439-a9e6-26c90a829c57_dlb",
  "pool_path": "/infra/lb-pools/runtime-extension-webhook-service_443_TCP_snr9y",
  "application_profile_path": "/infra/lb-app-profiles/default-tcp-lb-app-profile",
  "log_significant_event_only": false,
  "resource_type": "LBVirtualServer",
  "id": "runtime-extension-webhook-service_443_TCP_snr9y",
  "display_name": "runtime-extension-webhook-service_443_TCP",
  "tags": [
    {
      "scope": "ncp/version",
      "tag": "1.2.0"
    },
    {
      "scope": "ncp/cluster",
      "tag": "f06fd228-8088-4439-a9e6-26c90a829c57"
    },
    {
      "scope": "ncp/project",
      "tag": "svc-tkg-jrsvf"
    },
    {
      "scope": "external_id",
      "tag": "4a5eb61c-293d-47c4-bcce-feb1413e5155"
    },
    {
      "scope": "ncp/service",
      "tag": "runtime-extension-webhook-service"
    },
    {
      "scope": "ncp/service_uid",
      "tag": "4a5eb61c-293d-47c4-bcce-feb1413e5155"
    },
    {
      "scope": "ncp/service_port",
      "tag": "443"
    },
    {
      "scope": "ncp/service_port_protocol",
      "tag": "TCP"
    },
    {
      "scope": "ncp/created_for",
      "tag": "DLB"
    }
  ],
  "path": "/infra/lb-virtual-servers/runtime-extension-webhook-service_443_TCP_snr9y",
  "relative_path": "runtime-extension-webhook-service_443_TCP_snr9y",
  "parent_path": "/infra",
  "remote_path": "",
  "unique_id": "81b2c308-638f-407e-94a6-626b05cd67e2",
  "realization_id": "81b2c308-638f-407e-94a6-626b05cd67e2",
  "owner_id": "42495ba4-8c0b-49c9-b645-84cc39c2df30",
  "marked_for_delete": false,
  "overridden": false,
  "_system_owned": false,
  "_protection": "NOT_PROTECTED",
  "_create_time": 1760504088597,
  "_create_user": "wcp-cluster-user-f06fd228-8088-4439-a9e6-26c90a829c57-d34133d7-0fdf-4c9d-abcf-df83bd050a59",
  "_last_modified_time": 1760504090216,
  "_last_modified_user": "wcp-cluster-user-f06fd228-8088-4439-a9e6-26c90a829c57-d34133d7-0fdf-4c9d-abcf-df83bd050a59",
  "_revision": 1
}
```
<a id="66-policy-api-v1-infra-lb-virtual-servers-vmware-system-csi-webhook-service-443-tcp-2ypm7"></a>
### 66. /policy/api/v1/infra/lb-virtual-servers/vmware-system-csi-webhook-service_443_TCP_2ypm7

**HTTP Methods:** GET, PATCH

**Explanation:**
NSX Policy API endpoint for resource management.

---


**Sample Response Body (GET, from logs):**
```json
{
  "enabled": true,
  "ip_address": "172.24.28.140",
  "ports": [
    "443"
  ],
  "access_log_enabled": false,
  "lb_service_path": "/infra/lb-services/clusterip_f06fd228-8088-4439-a9e6-26c90a829c57_dlb",
  "pool_path": "/infra/lb-pools/vmware-system-csi-webhook-service_443_TCP_2ypm7",
  "application_profile_path": "/infra/lb-app-profiles/default-tcp-lb-app-profile",
  "log_significant_event_only": false,
  "resource_type": "LBVirtualServer",
  "id": "vmware-system-csi-webhook-service_443_TCP_2ypm7",
  "display_name": "vmware-system-csi-webhook-service_443_TCP",
  "tags": [
    {
      "scope": "ncp/version",
      "tag": "1.2.0"
    },
    {
      "scope": "ncp/cluster",
      "tag": "f06fd228-8088-4439-a9e6-26c90a829c57"
    },
    {
      "scope": "ncp/project",
      "tag": "vmware-system-csi"
    },
    {
      "scope": "external_id",
      "tag": "97cab78f-68ee-4911-851e-e6610eaf129f"
    },
    {
      "scope": "ncp/service",
      "tag": "vmware-system-csi-webhook-service"
    },
    {
      "scope": "ncp/service_uid",
      "tag": "97cab78f-68ee-4911-851e-e6610eaf129f"
    },
    {
      "scope": "ncp/service_port",
      "tag": "443"
    },
    {
      "scope": "ncp/service_port_protocol",
      "tag": "TCP"
    },
    {
      "scope": "ncp/created_for",
      "tag": "DLB"
    }
  ],
  "path": "/infra/lb-virtual-servers/vmware-system-csi-webhook-service_443_TCP_2ypm7",
  "relative_path": "vmware-system-csi-webhook-service_443_TCP_2ypm7",
  "parent_path": "/infra",
  "remote_path": "",
  "unique_id": "42fb87e5-6886-403d-97f1-c848be1ced58",
  "realization_id": "42fb87e5-6886-403d-97f1-c848be1ced58",
  "owner_id": "42495ba4-8c0b-49c9-b645-84cc39c2df30",
  "marked_for_delete": false,
  "overridden": false,
  "_system_owned": false,
  "_protection": "NOT_PROTECTED",
  "_create_time": 1760503464039,
  "_create_user": "wcp-cluster-user-f06fd228-8088-4439-a9e6-26c90a829c57-d34133d7-0fdf-4c9d-abcf-df83bd050a59",
  "_last_modified_time": 1760503618685,
  "_last_modified_user": "wcp-cluster-user-f06fd228-8088-4439-a9e6-26c90a829c57-d34133d7-0fdf-4c9d-abcf-df83bd050a59",
  "_revision": 1
}
```
<a id="67-policy-api-v1-infra-lb-virtual-servers-vmware-system-tkg-webhook-service-443-tcp-7jv1e"></a>
### 67. /policy/api/v1/infra/lb-virtual-servers/vmware-system-tkg-webhook-service_443_TCP_7jv1e

**HTTP Methods:** GET, PATCH

**Explanation:**
NSX Policy API endpoint for resource management.

---


**Sample Response Body (GET, from logs):**
```json
{
  "enabled": true,
  "ip_address": "172.24.166.108",
  "ports": [
    "443"
  ],
  "access_log_enabled": false,
  "lb_service_path": "/infra/lb-services/clusterip_f06fd228-8088-4439-a9e6-26c90a829c57_dlb",
  "pool_path": "/infra/lb-pools/vmware-system-tkg-webhook-service_443_TCP_7jv1e",
  "application_profile_path": "/infra/lb-app-profiles/default-tcp-lb-app-profile",
  "log_significant_event_only": false,
  "resource_type": "LBVirtualServer",
  "id": "vmware-system-tkg-webhook-service_443_TCP_7jv1e",
  "display_name": "vmware-system-tkg-webhook-service_443_TCP",
  "tags": [
    {
      "scope": "ncp/version",
      "tag": "1.2.0"
    },
    {
      "scope": "ncp/cluster",
      "tag": "f06fd228-8088-4439-a9e6-26c90a829c57"
    },
    {
      "scope": "ncp/project",
      "tag": "svc-tkg-jrsvf"
    },
    {
      "scope": "external_id",
      "tag": "01043fe3-e833-4bc7-ab8b-613814f32d94"
    },
    {
      "scope": "ncp/service",
      "tag": "vmware-system-tkg-webhook-service"
    },
    {
      "scope": "ncp/service_uid",
      "tag": "01043fe3-e833-4bc7-ab8b-613814f32d94"
    },
    {
      "scope": "ncp/service_port",
      "tag": "443"
    },
    {
      "scope": "ncp/service_port_protocol",
      "tag": "TCP"
    },
    {
      "scope": "ncp/created_for",
      "tag": "DLB"
    }
  ],
  "path": "/infra/lb-virtual-servers/vmware-system-tkg-webhook-service_443_TCP_7jv1e",
  "relative_path": "vmware-system-tkg-webhook-service_443_TCP_7jv1e",
  "parent_path": "/infra",
  "remote_path": "",
  "unique_id": "8f19c1f5-d139-4de4-9c32-4eebf81c0fb8",
  "realization_id": "8f19c1f5-d139-4de4-9c32-4eebf81c0fb8",
  "owner_id": "42495ba4-8c0b-49c9-b645-84cc39c2df30",
  "marked_for_delete": false,
  "overridden": false,
  "_system_owned": false,
  "_protection": "NOT_PROTECTED",
  "_create_time": 1760504109641,
  "_create_user": "wcp-cluster-user-f06fd228-8088-4439-a9e6-26c90a829c57-d34133d7-0fdf-4c9d-abcf-df83bd050a59",
  "_last_modified_time": 1760504111526,
  "_last_modified_user": "wcp-cluster-user-f06fd228-8088-4439-a9e6-26c90a829c57-d34133d7-0fdf-4c9d-abcf-df83bd050a59",
  "_revision": 1
}
```
<a id="68-policy-api-v1-infra-lb-virtual-servers-runtime-extension-metrics-service-9876-tcp-axzz2"></a>
### 68. /policy/api/v1/infra/lb-virtual-servers/runtime-extension-metrics-service_9876_TCP_axzz2

**HTTP Methods:** GET, PATCH

**Explanation:**
NSX Policy API endpoint for resource management.

---


**Sample Response Body (GET, from logs):**
```json
{
  "enabled": true,
  "ip_address": "172.24.3.209",
  "ports": [
    "9876"
  ],
  "access_log_enabled": false,
  "lb_service_path": "/infra/lb-services/clusterip_f06fd228-8088-4439-a9e6-26c90a829c57_dlb",
  "pool_path": "/infra/lb-pools/runtime-extension-metrics-service_9876_TCP_axzz2",
  "application_profile_path": "/infra/lb-app-profiles/default-tcp-lb-app-profile",
  "log_significant_event_only": false,
  "resource_type": "LBVirtualServer",
  "id": "runtime-extension-metrics-service_9876_TCP_axzz2",
  "display_name": "runtime-extension-metrics-service_9876_TCP",
  "tags": [
    {
      "scope": "ncp/version",
      "tag": "1.2.0"
    },
    {
      "scope": "ncp/cluster",
      "tag": "f06fd228-8088-4439-a9e6-26c90a829c57"
    },
    {
      "scope": "ncp/project",
      "tag": "svc-tkg-jrsvf"
    },
    {
      "scope": "external_id",
      "tag": "1b3a0aea-39bb-4730-bd52-24718d892533"
    },
    {
      "scope": "ncp/service",
      "tag": "runtime-extension-metrics-service"
    },
    {
      "scope": "ncp/service_uid",
      "tag": "1b3a0aea-39bb-4730-bd52-24718d892533"
    },
    {
      "scope": "ncp/service_port",
      "tag": "9876"
    },
    {
      "scope": "ncp/service_port_protocol",
      "tag": "TCP"
    },
    {
      "scope": "ncp/created_for",
      "tag": "DLB"
    }
  ],
  "path": "/infra/lb-virtual-servers/runtime-extension-metrics-service_9876_TCP_axzz2",
  "relative_path": "runtime-extension-metrics-service_9876_TCP_axzz2",
  "parent_path": "/infra",
  "remote_path": "",
  "unique_id": "d9397828-4623-46f3-ab93-f28652fd377b",
  "realization_id": "d9397828-4623-46f3-ab93-f28652fd377b",
  "owner_id": "42495ba4-8c0b-49c9-b645-84cc39c2df30",
  "marked_for_delete": false,
  "overridden": false,
  "_system_owned": false,
  "_protection": "NOT_PROTECTED",
  "_create_time": 1760504088236,
  "_create_user": "wcp-cluster-user-f06fd228-8088-4439-a9e6-26c90a829c57-d34133d7-0fdf-4c9d-abcf-df83bd050a59",
  "_last_modified_time": 1760504090926,
  "_last_modified_user": "wcp-cluster-user-f06fd228-8088-4439-a9e6-26c90a829c57-d34133d7-0fdf-4c9d-abcf-df83bd050a59",
  "_revision": 1
}
```
<a id="69-policy-api-v1-infra-lb-virtual-servers-vmware-system-nsop-webhook-service-443-tcp-l6xiz"></a>
### 69. /policy/api/v1/infra/lb-virtual-servers/vmware-system-nsop-webhook-service_443_TCP_l6xiz

**HTTP Methods:** GET, PATCH

**Explanation:**
NSX Policy API endpoint for resource management.

---


**Sample Response Body (GET, from logs):**
```json
{
  "enabled": true,
  "ip_address": "172.24.200.222",
  "ports": [
    "443"
  ],
  "access_log_enabled": false,
  "lb_service_path": "/infra/lb-services/clusterip_f06fd228-8088-4439-a9e6-26c90a829c57_dlb",
  "pool_path": "/infra/lb-pools/vmware-system-nsop-webhook-service_443_TCP_l6xiz",
  "application_profile_path": "/infra/lb-app-profiles/default-tcp-lb-app-profile",
  "log_significant_event_only": false,
  "resource_type": "LBVirtualServer",
  "id": "vmware-system-nsop-webhook-service_443_TCP_l6xiz",
  "display_name": "vmware-system-nsop-webhook-service_443_TCP",
  "tags": [
    {
      "scope": "ncp/version",
      "tag": "1.2.0"
    },
    {
      "scope": "ncp/cluster",
      "tag": "f06fd228-8088-4439-a9e6-26c90a829c57"
    },
    {
      "scope": "ncp/project",
      "tag": "vmware-system-nsop"
    },
    {
      "scope": "external_id",
      "tag": "641f6791-5f90-4d75-bc51-f560a0c6bdc3"
    },
    {
      "scope": "ncp/service",
      "tag": "vmware-system-nsop-webhook-service"
    },
    {
      "scope": "ncp/service_uid",
      "tag": "641f6791-5f90-4d75-bc51-f560a0c6bdc3"
    },
    {
      "scope": "ncp/service_port",
      "tag": "443"
    },
    {
      "scope": "ncp/service_port_protocol",
      "tag": "TCP"
    },
    {
      "scope": "ncp/created_for",
      "tag": "DLB"
    }
  ],
  "path": "/infra/lb-virtual-servers/vmware-system-nsop-webhook-service_443_TCP_l6xiz",
  "relative_path": "vmware-system-nsop-webhook-service_443_TCP_l6xiz",
  "parent_path": "/infra",
  "remote_path": "",
  "unique_id": "d810805c-ca6f-497a-bd3b-fb84255f06de",
  "realization_id": "d810805c-ca6f-497a-bd3b-fb84255f06de",
  "owner_id": "42495ba4-8c0b-49c9-b645-84cc39c2df30",
  "marked_for_delete": false,
  "overridden": false,
  "_system_owned": false,
  "_protection": "NOT_PROTECTED",
  "_create_time": 1760503445528,
  "_create_user": "wcp-cluster-user-f06fd228-8088-4439-a9e6-26c90a829c57-d34133d7-0fdf-4c9d-abcf-df83bd050a59",
  "_last_modified_time": 1760503618607,
  "_last_modified_user": "wcp-cluster-user-f06fd228-8088-4439-a9e6-26c90a829c57-d34133d7-0fdf-4c9d-abcf-df83bd050a59",
  "_revision": 1
}
```
<a id="70-policy-api-v1-infra-lb-virtual-servers-vmware-system-vmop-webhook-service-443-tcp-qduvo"></a>
### 70. /policy/api/v1/infra/lb-virtual-servers/vmware-system-vmop-webhook-service_443_TCP_qduvo

**HTTP Methods:** GET, PATCH

**Explanation:**
NSX Policy API endpoint for resource management.

---


**Sample Response Body (GET, from logs):**
```json
{
  "enabled": true,
  "ip_address": "172.24.228.55",
  "ports": [
    "443"
  ],
  "access_log_enabled": false,
  "lb_service_path": "/infra/lb-services/clusterip_f06fd228-8088-4439-a9e6-26c90a829c57_dlb",
  "pool_path": "/infra/lb-pools/vmware-system-vmop-webhook-service_443_TCP_qduvo",
  "application_profile_path": "/infra/lb-app-profiles/default-tcp-lb-app-profile",
  "log_significant_event_only": false,
  "resource_type": "LBVirtualServer",
  "id": "vmware-system-vmop-webhook-service_443_TCP_qduvo",
  "display_name": "vmware-system-vmop-webhook-service_443_TCP",
  "tags": [
    {
      "scope": "ncp/version",
      "tag": "1.2.0"
    },
    {
      "scope": "ncp/cluster",
      "tag": "f06fd228-8088-4439-a9e6-26c90a829c57"
    },
    {
      "scope": "ncp/project",
      "tag": "vmware-system-vmop"
    },
    {
      "scope": "external_id",
      "tag": "6b805d1c-f1fc-4898-9f04-c8b61df325bb"
    },
    {
      "scope": "ncp/service",
      "tag": "vmware-system-vmop-webhook-service"
    },
    {
      "scope": "ncp/service_uid",
      "tag": "6b805d1c-f1fc-4898-9f04-c8b61df325bb"
    },
    {
      "scope": "ncp/service_port",
      "tag": "443"
    },
    {
      "scope": "ncp/service_port_protocol",
      "tag": "TCP"
    },
    {
      "scope": "ncp/created_for",
      "tag": "DLB"
    }
  ],
  "path": "/infra/lb-virtual-servers/vmware-system-vmop-webhook-service_443_TCP_qduvo",
  "relative_path": "vmware-system-vmop-webhook-service_443_TCP_qduvo",
  "parent_path": "/infra",
  "remote_path": "",
  "unique_id": "eedc8d80-45dd-4d07-a19e-d315e14a316b",
  "realization_id": "eedc8d80-45dd-4d07-a19e-d315e14a316b",
  "owner_id": "42495ba4-8c0b-49c9-b645-84cc39c2df30",
  "marked_for_delete": false,
  "overridden": false,
  "_system_owned": false,
  "_protection": "NOT_PROTECTED",
  "_create_time": 1760503473090,
  "_create_user": "wcp-cluster-user-f06fd228-8088-4439-a9e6-26c90a829c57-d34133d7-0fdf-4c9d-abcf-df83bd050a59",
  "_last_modified_time": 1760503623389,
  "_last_modified_user": "wcp-cluster-user-f06fd228-8088-4439-a9e6-26c90a829c57-d34133d7-0fdf-4c9d-abcf-df83bd050a59",
  "_revision": 1
}
```
<a id="71-policy-api-v1-infra-lb-virtual-servers-tanzu-addons-manager-webhook-service-443-tcp-diwwz"></a>
### 71. /policy/api/v1/infra/lb-virtual-servers/tanzu-addons-manager-webhook-service_443_TCP_diwwz

**HTTP Methods:** GET, PATCH

**Explanation:**
NSX Policy API endpoint for resource management.

---


**Sample Response Body (GET, from logs):**
```json
{
  "enabled": true,
  "ip_address": "172.24.248.235",
  "ports": [
    "443"
  ],
  "access_log_enabled": false,
  "lb_service_path": "/infra/lb-services/clusterip_f06fd228-8088-4439-a9e6-26c90a829c57_dlb",
  "pool_path": "/infra/lb-pools/tanzu-addons-manager-webhook-service_443_TCP_diwwz",
  "application_profile_path": "/infra/lb-app-profiles/default-tcp-lb-app-profile",
  "log_significant_event_only": false,
  "resource_type": "LBVirtualServer",
  "id": "tanzu-addons-manager-webhook-service_443_TCP_diwwz",
  "display_name": "tanzu-addons-manager-webhook-service_443_TCP",
  "tags": [
    {
      "scope": "ncp/version",
      "tag": "1.2.0"
    },
    {
      "scope": "ncp/cluster",
      "tag": "f06fd228-8088-4439-a9e6-26c90a829c57"
    },
    {
      "scope": "ncp/project",
      "tag": "svc-tkg-jrsvf"
    },
    {
      "scope": "external_id",
      "tag": "8ed97d5d-3a2b-4b6b-8fb9-3e3f304d2084"
    },
    {
      "scope": "ncp/service",
      "tag": "tanzu-addons-manager-webhook-service"
    },
    {
      "scope": "ncp/service_uid",
      "tag": "8ed97d5d-3a2b-4b6b-8fb9-3e3f304d2084"
    },
    {
      "scope": "ncp/service_port",
      "tag": "443"
    },
    {
      "scope": "ncp/service_port_protocol",
      "tag": "TCP"
    },
    {
      "scope": "ncp/created_for",
      "tag": "DLB"
    }
  ],
  "path": "/infra/lb-virtual-servers/tanzu-addons-manager-webhook-service_443_TCP_diwwz",
  "relative_path": "tanzu-addons-manager-webhook-service_443_TCP_diwwz",
  "parent_path": "/infra",
  "remote_path": "",
  "unique_id": "cc6baf8c-bb4a-4e44-969d-58c8c6b5a696",
  "realization_id": "cc6baf8c-bb4a-4e44-969d-58c8c6b5a696",
  "owner_id": "42495ba4-8c0b-49c9-b645-84cc39c2df30",
  "marked_for_delete": false,
  "overridden": false,
  "_system_owned": false,
  "_protection": "NOT_PROTECTED",
  "_create_time": 1760504114807,
  "_create_user": "wcp-cluster-user-f06fd228-8088-4439-a9e6-26c90a829c57-d34133d7-0fdf-4c9d-abcf-df83bd050a59",
  "_last_modified_time": 1760504116564,
  "_last_modified_user": "wcp-cluster-user-f06fd228-8088-4439-a9e6-26c90a829c57-d34133d7-0fdf-4c9d-abcf-df83bd050a59",
  "_revision": 1
}
```
<a id="72-policy-api-v1-infra-lb-virtual-servers-tkr-resolver-cluster-webhook-service-443-tcp-nc6lk"></a>
### 72. /policy/api/v1/infra/lb-virtual-servers/tkr-resolver-cluster-webhook-service_443_TCP_nc6lk

**HTTP Methods:** GET, PATCH

**Explanation:**
NSX Policy API endpoint for resource management.

---


**Sample Response Body (GET, from logs):**
```json
{
  "enabled": true,
  "ip_address": "172.24.38.90",
  "ports": [
    "443"
  ],
  "access_log_enabled": false,
  "lb_service_path": "/infra/lb-services/clusterip_f06fd228-8088-4439-a9e6-26c90a829c57_dlb",
  "pool_path": "/infra/lb-pools/tkr-resolver-cluster-webhook-service_443_TCP_nc6lk",
  "application_profile_path": "/infra/lb-app-profiles/default-tcp-lb-app-profile",
  "log_significant_event_only": false,
  "resource_type": "LBVirtualServer",
  "id": "tkr-resolver-cluster-webhook-service_443_TCP_nc6lk",
  "display_name": "tkr-resolver-cluster-webhook-service_443_TCP",
  "tags": [
    {
      "scope": "ncp/version",
      "tag": "1.2.0"
    },
    {
      "scope": "ncp/cluster",
      "tag": "f06fd228-8088-4439-a9e6-26c90a829c57"
    },
    {
      "scope": "ncp/project",
      "tag": "svc-tkg-jrsvf"
    },
    {
      "scope": "external_id",
      "tag": "fff7bc81-4ef6-4b92-a5f5-f3bbcfc65651"
    },
    {
      "scope": "ncp/service",
      "tag": "tkr-resolver-cluster-webhook-service"
    },
    {
      "scope": "ncp/service_uid",
      "tag": "fff7bc81-4ef6-4b92-a5f5-f3bbcfc65651"
    },
    {
      "scope": "ncp/service_port",
      "tag": "443"
    },
    {
      "scope": "ncp/service_port_protocol",
      "tag": "TCP"
    },
    {
      "scope": "ncp/created_for",
      "tag": "DLB"
    }
  ],
  "path": "/infra/lb-virtual-servers/tkr-resolver-cluster-webhook-service_443_TCP_nc6lk",
  "relative_path": "tkr-resolver-cluster-webhook-service_443_TCP_nc6lk",
  "parent_path": "/infra",
  "remote_path": "",
  "unique_id": "1ff58804-88e3-4942-be14-fa8520178bd1",
  "realization_id": "1ff58804-88e3-4942-be14-fa8520178bd1",
  "owner_id": "42495ba4-8c0b-49c9-b645-84cc39c2df30",
  "marked_for_delete": false,
  "overridden": false,
  "_system_owned": false,
  "_protection": "NOT_PROTECTED",
  "_create_time": 1760504043076,
  "_create_user": "wcp-cluster-user-f06fd228-8088-4439-a9e6-26c90a829c57-d34133d7-0fdf-4c9d-abcf-df83bd050a59",
  "_last_modified_time": 1760504046546,
  "_last_modified_user": "wcp-cluster-user-f06fd228-8088-4439-a9e6-26c90a829c57-d34133d7-0fdf-4c9d-abcf-df83bd050a59",
  "_revision": 1
}
```
<a id="73-policy-api-v1-infra-lb-virtual-servers-tanzu-addons-manager-metrics-service-9946-tcp-jqdpt"></a>
### 73. /policy/api/v1/infra/lb-virtual-servers/tanzu-addons-manager-metrics-service_9946_TCP_jqdpt

**HTTP Methods:** GET, PATCH

**Explanation:**
NSX Policy API endpoint for resource management.

---


**Sample Response Body (GET, from logs):**
```json
{
  "enabled": true,
  "ip_address": "172.24.74.145",
  "ports": [
    "9946"
  ],
  "access_log_enabled": false,
  "lb_service_path": "/infra/lb-services/clusterip_f06fd228-8088-4439-a9e6-26c90a829c57_dlb",
  "pool_path": "/infra/lb-pools/tanzu-addons-manager-metrics-service_9946_TCP_jqdpt",
  "application_profile_path": "/infra/lb-app-profiles/default-tcp-lb-app-profile",
  "log_significant_event_only": false,
  "resource_type": "LBVirtualServer",
  "id": "tanzu-addons-manager-metrics-service_9946_TCP_jqdpt",
  "display_name": "tanzu-addons-manager-metrics-service_9946_TCP",
  "tags": [
    {
      "scope": "ncp/version",
      "tag": "1.2.0"
    },
    {
      "scope": "ncp/cluster",
      "tag": "f06fd228-8088-4439-a9e6-26c90a829c57"
    },
    {
      "scope": "ncp/project",
      "tag": "svc-tkg-jrsvf"
    },
    {
      "scope": "external_id",
      "tag": "8714827f-1087-49d5-9b10-de83e0bde284"
    },
    {
      "scope": "ncp/service",
      "tag": "tanzu-addons-manager-metrics-service"
    },
    {
      "scope": "ncp/service_uid",
      "tag": "8714827f-1087-49d5-9b10-de83e0bde284"
    },
    {
      "scope": "ncp/service_port",
      "tag": "9946"
    },
    {
      "scope": "ncp/service_port_protocol",
      "tag": "TCP"
    },
    {
      "scope": "ncp/created_for",
      "tag": "DLB"
    }
  ],
  "path": "/infra/lb-virtual-servers/tanzu-addons-manager-metrics-service_9946_TCP_jqdpt",
  "relative_path": "tanzu-addons-manager-metrics-service_9946_TCP_jqdpt",
  "parent_path": "/infra",
  "remote_path": "",
  "unique_id": "67df2648-1098-41b8-ae15-56f0da0f9e1d",
  "realization_id": "67df2648-1098-41b8-ae15-56f0da0f9e1d",
  "owner_id": "42495ba4-8c0b-49c9-b645-84cc39c2df30",
  "marked_for_delete": false,
  "overridden": false,
  "_system_owned": false,
  "_protection": "NOT_PROTECTED",
  "_create_time": 1760504112899,
  "_create_user": "wcp-cluster-user-f06fd228-8088-4439-a9e6-26c90a829c57-d34133d7-0fdf-4c9d-abcf-df83bd050a59",
  "_last_modified_time": 1760504113609,
  "_last_modified_user": "wcp-cluster-user-f06fd228-8088-4439-a9e6-26c90a829c57-d34133d7-0fdf-4c9d-abcf-df83bd050a59",
  "_revision": 1
}
```
<a id="74-policy-api-v1-infra-lb-virtual-servers-capi-kubeadm-bootstrap-webhook-service-443-tcp-6xo5g"></a>
### 74. /policy/api/v1/infra/lb-virtual-servers/capi-kubeadm-bootstrap-webhook-service_443_TCP_6xo5g

**HTTP Methods:** GET, PATCH

**Explanation:**
NSX Policy API endpoint for resource management.

---


**Sample Response Body (GET, from logs):**
```json
{
  "enabled": true,
  "ip_address": "172.24.219.114",
  "ports": [
    "443"
  ],
  "access_log_enabled": false,
  "lb_service_path": "/infra/lb-services/clusterip_f06fd228-8088-4439-a9e6-26c90a829c57_dlb",
  "pool_path": "/infra/lb-pools/capi-kubeadm-bootstrap-webhook-service_443_TCP_6xo5g",
  "application_profile_path": "/infra/lb-app-profiles/default-tcp-lb-app-profile",
  "log_significant_event_only": false,
  "resource_type": "LBVirtualServer",
  "id": "capi-kubeadm-bootstrap-webhook-service_443_TCP_6xo5g",
  "display_name": "capi-kubeadm-bootstrap-webhook-service_443_TCP",
  "tags": [
    {
      "scope": "ncp/version",
      "tag": "1.2.0"
    },
    {
      "scope": "ncp/cluster",
      "tag": "f06fd228-8088-4439-a9e6-26c90a829c57"
    },
    {
      "scope": "ncp/project",
      "tag": "svc-tkg-jrsvf"
    },
    {
      "scope": "external_id",
      "tag": "ee224c09-10d1-4f57-a412-4fc8a1d643a6"
    },
    {
      "scope": "ncp/service",
      "tag": "capi-kubeadm-bootstrap-webhook-service"
    },
    {
      "scope": "ncp/service_uid",
      "tag": "ee224c09-10d1-4f57-a412-4fc8a1d643a6"
    },
    {
      "scope": "ncp/service_port",
      "tag": "443"
    },
    {
      "scope": "ncp/service_port_protocol",
      "tag": "TCP"
    },
    {
      "scope": "ncp/created_for",
      "tag": "DLB"
    }
  ],
  "path": "/infra/lb-virtual-servers/capi-kubeadm-bootstrap-webhook-service_443_TCP_6xo5g",
  "relative_path": "capi-kubeadm-bootstrap-webhook-service_443_TCP_6xo5g",
  "parent_path": "/infra",
  "remote_path": "",
  "unique_id": "164b4d57-02e3-4bd4-a8df-558839f096be",
  "realization_id": "164b4d57-02e3-4bd4-a8df-558839f096be",
  "owner_id": "42495ba4-8c0b-49c9-b645-84cc39c2df30",
  "marked_for_delete": false,
  "overridden": false,
  "_system_owned": false,
  "_protection": "NOT_PROTECTED",
  "_create_time": 1760504058156,
  "_create_user": "wcp-cluster-user-f06fd228-8088-4439-a9e6-26c90a829c57-d34133d7-0fdf-4c9d-abcf-df83bd050a59",
  "_last_modified_time": 1760513240448,
  "_last_modified_user": "wcp-cluster-user-f06fd228-8088-4439-a9e6-26c90a829c57-d34133d7-0fdf-4c9d-abcf-df83bd050a59",
  "_revision": 1
}
```
<a id="75-policy-api-v1-infra-lb-virtual-servers-vmware-system-vmop-web-console-validator-80-tcp-lzxdi"></a>
### 75. /policy/api/v1/infra/lb-virtual-servers/vmware-system-vmop-web-console-validator_80_TCP_lzxdi

**HTTP Methods:** GET, PATCH

**Explanation:**
NSX Policy API endpoint for resource management.

---


**Sample Response Body (GET, from logs):**
```json
{
  "enabled": true,
  "ip_address": "172.24.79.137",
  "ports": [
    "80"
  ],
  "access_log_enabled": false,
  "lb_service_path": "/infra/lb-services/clusterip_f06fd228-8088-4439-a9e6-26c90a829c57_dlb",
  "pool_path": "/infra/lb-pools/vmware-system-vmop-web-console-validator_80_TCP_lzxdi",
  "application_profile_path": "/infra/lb-app-profiles/default-tcp-lb-app-profile",
  "log_significant_event_only": false,
  "resource_type": "LBVirtualServer",
  "id": "vmware-system-vmop-web-console-validator_80_TCP_lzxdi",
  "display_name": "vmware-system-vmop-web-console-validator_80_TCP",
  "tags": [
    {
      "scope": "ncp/version",
      "tag": "1.2.0"
    },
    {
      "scope": "ncp/cluster",
      "tag": "f06fd228-8088-4439-a9e6-26c90a829c57"
    },
    {
      "scope": "ncp/project",
      "tag": "vmware-system-vmop"
    },
    {
      "scope": "external_id",
      "tag": "90afe0fa-3a88-40db-8b3e-c40ae2525f1a"
    },
    {
      "scope": "ncp/service",
      "tag": "vmware-system-vmop-web-console-validator"
    },
    {
      "scope": "ncp/service_uid",
      "tag": "90afe0fa-3a88-40db-8b3e-c40ae2525f1a"
    },
    {
      "scope": "ncp/service_port",
      "tag": "80"
    },
    {
      "scope": "ncp/service_port_protocol",
      "tag": "TCP"
    },
    {
      "scope": "ncp/created_for",
      "tag": "DLB"
    }
  ],
  "path": "/infra/lb-virtual-servers/vmware-system-vmop-web-console-validator_80_TCP_lzxdi",
  "relative_path": "vmware-system-vmop-web-console-validator_80_TCP_lzxdi",
  "parent_path": "/infra",
  "remote_path": "",
  "unique_id": "69bbb6da-7377-4b16-9dcc-a95c32209057",
  "realization_id": "69bbb6da-7377-4b16-9dcc-a95c32209057",
  "owner_id": "42495ba4-8c0b-49c9-b645-84cc39c2df30",
  "marked_for_delete": false,
  "overridden": false,
  "_system_owned": false,
  "_protection": "NOT_PROTECTED",
  "_create_time": 1760503460727,
  "_create_user": "wcp-cluster-user-f06fd228-8088-4439-a9e6-26c90a829c57-d34133d7-0fdf-4c9d-abcf-df83bd050a59",
  "_last_modified_time": 1760503621147,
  "_last_modified_user": "wcp-cluster-user-f06fd228-8088-4439-a9e6-26c90a829c57-d34133d7-0fdf-4c9d-abcf-df83bd050a59",
  "_revision": 1
}
```
<a id="76-policy-api-v1-infra-lb-virtual-servers-capi-controller-manager-metrics-service-9844-tcp-47mar"></a>
### 76. /policy/api/v1/infra/lb-virtual-servers/capi-controller-manager-metrics-service_9844_TCP_47mar

**HTTP Methods:** GET, PATCH

**Explanation:**
NSX Policy API endpoint for resource management.

---


**Sample Response Body (GET, from logs):**
```json
{
  "enabled": true,
  "ip_address": "172.24.109.208",
  "ports": [
    "9844"
  ],
  "access_log_enabled": false,
  "lb_service_path": "/infra/lb-services/clusterip_f06fd228-8088-4439-a9e6-26c90a829c57_dlb",
  "pool_path": "/infra/lb-pools/capi-controller-manager-metrics-service_9844_TCP_47mar",
  "application_profile_path": "/infra/lb-app-profiles/default-tcp-lb-app-profile",
  "log_significant_event_only": false,
  "resource_type": "LBVirtualServer",
  "id": "capi-controller-manager-metrics-service_9844_TCP_47mar",
  "display_name": "capi-controller-manager-metrics-service_9844_TCP",
  "tags": [
    {
      "scope": "ncp/version",
      "tag": "1.2.0"
    },
    {
      "scope": "ncp/cluster",
      "tag": "f06fd228-8088-4439-a9e6-26c90a829c57"
    },
    {
      "scope": "ncp/project",
      "tag": "svc-tkg-jrsvf"
    },
    {
      "scope": "external_id",
      "tag": "ac294cae-d3f2-4aab-b2ed-bb906363e231"
    },
    {
      "scope": "ncp/service",
      "tag": "capi-controller-manager-metrics-service"
    },
    {
      "scope": "ncp/service_uid",
      "tag": "ac294cae-d3f2-4aab-b2ed-bb906363e231"
    },
    {
      "scope": "ncp/service_port",
      "tag": "9844"
    },
    {
      "scope": "ncp/service_port_protocol",
      "tag": "TCP"
    },
    {
      "scope": "ncp/created_for",
      "tag": "DLB"
    }
  ],
  "path": "/infra/lb-virtual-servers/capi-controller-manager-metrics-service_9844_TCP_47mar",
  "relative_path": "capi-controller-manager-metrics-service_9844_TCP_47mar",
  "parent_path": "/infra",
  "remote_path": "",
  "unique_id": "e6b98bac-3a6f-4f1e-9a53-fcd307bad03c",
  "realization_id": "e6b98bac-3a6f-4f1e-9a53-fcd307bad03c",
  "owner_id": "42495ba4-8c0b-49c9-b645-84cc39c2df30",
  "marked_for_delete": false,
  "overridden": false,
  "_system_owned": false,
  "_protection": "NOT_PROTECTED",
  "_create_time": 1760504059576,
  "_create_user": "wcp-cluster-user-f06fd228-8088-4439-a9e6-26c90a829c57-d34133d7-0fdf-4c9d-abcf-df83bd050a59",
  "_last_modified_time": 1760513238076,
  "_last_modified_user": "wcp-cluster-user-f06fd228-8088-4439-a9e6-26c90a829c57-d34133d7-0fdf-4c9d-abcf-df83bd050a59",
  "_revision": 1
}
```
<a id="77-policy-api-v1-infra-lb-virtual-servers-capv-controller-manager-metrics-service-9846-tcp-7af8y"></a>
### 77. /policy/api/v1/infra/lb-virtual-servers/capv-controller-manager-metrics-service_9846_TCP_7af8y

**HTTP Methods:** GET, PATCH

**Explanation:**
NSX Policy API endpoint for resource management.

---


**Sample Response Body (GET, from logs):**
```json
{
  "enabled": true,
  "ip_address": "172.24.38.221",
  "ports": [
    "9846"
  ],
  "access_log_enabled": false,
  "lb_service_path": "/infra/lb-services/clusterip_f06fd228-8088-4439-a9e6-26c90a829c57_dlb",
  "pool_path": "/infra/lb-pools/capv-controller-manager-metrics-service_9846_TCP_7af8y",
  "application_profile_path": "/infra/lb-app-profiles/default-tcp-lb-app-profile",
  "log_significant_event_only": false,
  "resource_type": "LBVirtualServer",
  "id": "capv-controller-manager-metrics-service_9846_TCP_7af8y",
  "display_name": "capv-controller-manager-metrics-service_9846_TCP",
  "tags": [
    {
      "scope": "ncp/version",
      "tag": "1.2.0"
    },
    {
      "scope": "ncp/cluster",
      "tag": "f06fd228-8088-4439-a9e6-26c90a829c57"
    },
    {
      "scope": "ncp/project",
      "tag": "svc-tkg-jrsvf"
    },
    {
      "scope": "external_id",
      "tag": "eaa2170f-4494-4185-841a-5a3d5deeb4e9"
    },
    {
      "scope": "ncp/service",
      "tag": "capv-controller-manager-metrics-service"
    },
    {
      "scope": "ncp/service_uid",
      "tag": "eaa2170f-4494-4185-841a-5a3d5deeb4e9"
    },
    {
      "scope": "ncp/service_port",
      "tag": "9846"
    },
    {
      "scope": "ncp/service_port_protocol",
      "tag": "TCP"
    },
    {
      "scope": "ncp/created_for",
      "tag": "DLB"
    }
  ],
  "path": "/infra/lb-virtual-servers/capv-controller-manager-metrics-service_9846_TCP_7af8y",
  "relative_path": "capv-controller-manager-metrics-service_9846_TCP_7af8y",
  "parent_path": "/infra",
  "remote_path": "",
  "unique_id": "4b61f8b5-6348-43dd-9ad5-d251883bdc9b",
  "realization_id": "4b61f8b5-6348-43dd-9ad5-d251883bdc9b",
  "owner_id": "42495ba4-8c0b-49c9-b645-84cc39c2df30",
  "marked_for_delete": false,
  "overridden": false,
  "_system_owned": false,
  "_protection": "NOT_PROTECTED",
  "_create_time": 1760504049986,
  "_create_user": "wcp-cluster-user-f06fd228-8088-4439-a9e6-26c90a829c57-d34133d7-0fdf-4c9d-abcf-df83bd050a59",
  "_last_modified_time": 1760504052364,
  "_last_modified_user": "wcp-cluster-user-f06fd228-8088-4439-a9e6-26c90a829c57-d34133d7-0fdf-4c9d-abcf-df83bd050a59",
  "_revision": 1
}
```
<a id="78-policy-api-v1-infra-lb-virtual-servers-vmware-system-tkg-state-metrics-service-9855-tcp-86h2q"></a>
### 78. /policy/api/v1/infra/lb-virtual-servers/vmware-system-tkg-state-metrics-service_9855_TCP_86h2q

**HTTP Methods:** GET, PATCH

**Explanation:**
NSX Policy API endpoint for resource management.

---


**Sample Response Body (GET, from logs):**
```json
{
  "enabled": true,
  "ip_address": "172.24.155.178",
  "ports": [
    "9855"
  ],
  "access_log_enabled": false,
  "lb_service_path": "/infra/lb-services/clusterip_f06fd228-8088-4439-a9e6-26c90a829c57_dlb",
  "pool_path": "/infra/lb-pools/vmware-system-tkg-state-metrics-service_9855_TCP_86h2q",
  "application_profile_path": "/infra/lb-app-profiles/default-tcp-lb-app-profile",
  "log_significant_event_only": false,
  "resource_type": "LBVirtualServer",
  "id": "vmware-system-tkg-state-metrics-service_9855_TCP_86h2q",
  "display_name": "vmware-system-tkg-state-metrics-service_9855_TCP",
  "tags": [
    {
      "scope": "ncp/version",
      "tag": "1.2.0"
    },
    {
      "scope": "ncp/cluster",
      "tag": "f06fd228-8088-4439-a9e6-26c90a829c57"
    },
    {
      "scope": "ncp/project",
      "tag": "svc-tkg-jrsvf"
    },
    {
      "scope": "external_id",
      "tag": "bc265014-24c9-4866-9023-0cd5e29cdfbf"
    },
    {
      "scope": "ncp/service",
      "tag": "vmware-system-tkg-state-metrics-service"
    },
    {
      "scope": "ncp/service_uid",
      "tag": "bc265014-24c9-4866-9023-0cd5e29cdfbf"
    },
    {
      "scope": "ncp/service_port",
      "tag": "9855"
    },
    {
      "scope": "ncp/service_port_protocol",
      "tag": "TCP"
    },
    {
      "scope": "ncp/created_for",
      "tag": "DLB"
    }
  ],
  "path": "/infra/lb-virtual-servers/vmware-system-tkg-state-metrics-service_9855_TCP_86h2q",
  "relative_path": "vmware-system-tkg-state-metrics-service_9855_TCP_86h2q",
  "parent_path": "/infra",
  "remote_path": "",
  "unique_id": "4b609abb-9e50-4f58-a2eb-6aec90bbe164",
  "realization_id": "4b609abb-9e50-4f58-a2eb-6aec90bbe164",
  "owner_id": "42495ba4-8c0b-49c9-b645-84cc39c2df30",
  "marked_for_delete": false,
  "overridden": false,
  "_system_owned": false,
  "_protection": "NOT_PROTECTED",
  "_create_time": 1760504109684,
  "_create_user": "wcp-cluster-user-f06fd228-8088-4439-a9e6-26c90a829c57-d34133d7-0fdf-4c9d-abcf-df83bd050a59",
  "_last_modified_time": 1760504110698,
  "_last_modified_user": "wcp-cluster-user-f06fd228-8088-4439-a9e6-26c90a829c57-d34133d7-0fdf-4c9d-abcf-df83bd050a59",
  "_revision": 1
}
```
<a id="79-policy-api-v1-infra-lb-virtual-servers-vmware-system-ako-ako-vks-webhook-service-443-tcp-gdbxh"></a>
### 79. /policy/api/v1/infra/lb-virtual-servers/vmware-system-ako-ako-vks-webhook-service_443_TCP_gdbxh

**HTTP Methods:** GET, PATCH

**Explanation:**
NSX Policy API endpoint for resource management.

---


**Sample Response Body (GET, from logs):**
```json
{
  "enabled": true,
  "ip_address": "172.24.226.251",
  "ports": [
    "443"
  ],
  "access_log_enabled": false,
  "lb_service_path": "/infra/lb-services/clusterip_f06fd228-8088-4439-a9e6-26c90a829c57_dlb",
  "pool_path": "/infra/lb-pools/vmware-system-ako-ako-vks-webhook-service_443_TCP_gdbxh",
  "application_profile_path": "/infra/lb-app-profiles/default-tcp-lb-app-profile",
  "log_significant_event_only": false,
  "resource_type": "LBVirtualServer",
  "id": "vmware-system-ako-ako-vks-webhook-service_443_TCP_gdbxh",
  "display_name": "vmware-system-ako-ako-vks-webhook-service_443_TCP",
  "tags": [
    {
      "scope": "ncp/version",
      "tag": "1.2.0"
    },
    {
      "scope": "ncp/cluster",
      "tag": "f06fd228-8088-4439-a9e6-26c90a829c57"
    },
    {
      "scope": "ncp/project",
      "tag": "vmware-system-ako"
    },
    {
      "scope": "external_id",
      "tag": "50c9038d-f84e-4d17-891d-e6da6706e5b1"
    },
    {
      "scope": "ncp/service",
      "tag": "vmware-system-ako-ako-vks-webhook-service"
    },
    {
      "scope": "ncp/service_uid",
      "tag": "50c9038d-f84e-4d17-891d-e6da6706e5b1"
    },
    {
      "scope": "ncp/service_port",
      "tag": "443"
    },
    {
      "scope": "ncp/service_port_protocol",
      "tag": "TCP"
    },
    {
      "scope": "ncp/created_for",
      "tag": "DLB"
    }
  ],
  "path": "/infra/lb-virtual-servers/vmware-system-ako-ako-vks-webhook-service_443_TCP_gdbxh",
  "relative_path": "vmware-system-ako-ako-vks-webhook-service_443_TCP_gdbxh",
  "parent_path": "/infra",
  "remote_path": "",
  "unique_id": "9328e761-f3a5-4a60-987f-afa36793dcb7",
  "realization_id": "9328e761-f3a5-4a60-987f-afa36793dcb7",
  "owner_id": "42495ba4-8c0b-49c9-b645-84cc39c2df30",
  "marked_for_delete": false,
  "overridden": false,
  "_system_owned": false,
  "_protection": "NOT_PROTECTED",
  "_create_time": 1760503470567,
  "_create_user": "wcp-cluster-user-f06fd228-8088-4439-a9e6-26c90a829c57-d34133d7-0fdf-4c9d-abcf-df83bd050a59",
  "_last_modified_time": 1760503619924,
  "_last_modified_user": "wcp-cluster-user-f06fd228-8088-4439-a9e6-26c90a829c57-d34133d7-0fdf-4c9d-abcf-df83bd050a59",
  "_revision": 1
}
```
<a id="80-policy-api-v1-infra-lb-virtual-servers-vmware-system-appplatform-webhook-service-443-tcp-3myq0"></a>
### 80. /policy/api/v1/infra/lb-virtual-servers/vmware-system-appplatform-webhook-service_443_TCP_3myq0

**HTTP Methods:** GET, PATCH

**Explanation:**
NSX Policy API endpoint for resource management.

---


**Sample Response Body (GET, from logs):**
```json
{
  "enabled": true,
  "ip_address": "172.24.108.149",
  "ports": [
    "443"
  ],
  "access_log_enabled": false,
  "lb_service_path": "/infra/lb-services/clusterip_f06fd228-8088-4439-a9e6-26c90a829c57_dlb",
  "pool_path": "/infra/lb-pools/vmware-system-appplatform-webhook-service_443_TCP_3myq0",
  "application_profile_path": "/infra/lb-app-profiles/default-tcp-lb-app-profile",
  "log_significant_event_only": false,
  "resource_type": "LBVirtualServer",
  "id": "vmware-system-appplatform-webhook-service_443_TCP_3myq0",
  "display_name": "vmware-system-appplatform-webhook-service_443_TCP",
  "tags": [
    {
      "scope": "ncp/version",
      "tag": "1.2.0"
    },
    {
      "scope": "ncp/cluster",
      "tag": "f06fd228-8088-4439-a9e6-26c90a829c57"
    },
    {
      "scope": "ncp/project",
      "tag": "vmware-system-appplatform-operator-system"
    },
    {
      "scope": "external_id",
      "tag": "4f7813f6-3f26-4b71-8b48-9105d1922190"
    },
    {
      "scope": "ncp/service",
      "tag": "vmware-system-appplatform-webhook-service"
    },
    {
      "scope": "ncp/service_uid",
      "tag": "4f7813f6-3f26-4b71-8b48-9105d1922190"
    },
    {
      "scope": "ncp/service_port",
      "tag": "443"
    },
    {
      "scope": "ncp/service_port_protocol",
      "tag": "TCP"
    },
    {
      "scope": "ncp/created_for",
      "tag": "DLB"
    }
  ],
  "path": "/infra/lb-virtual-servers/vmware-system-appplatform-webhook-service_443_TCP_3myq0",
  "relative_path": "vmware-system-appplatform-webhook-service_443_TCP_3myq0",
  "parent_path": "/infra",
  "remote_path": "",
  "unique_id": "b48021b4-c89a-454d-9473-0d3859e91687",
  "realization_id": "b48021b4-c89a-454d-9473-0d3859e91687",
  "owner_id": "42495ba4-8c0b-49c9-b645-84cc39c2df30",
  "marked_for_delete": false,
  "overridden": false,
  "_system_owned": false,
  "_protection": "NOT_PROTECTED",
  "_create_time": 1760503475725,
  "_create_user": "wcp-cluster-user-f06fd228-8088-4439-a9e6-26c90a829c57-d34133d7-0fdf-4c9d-abcf-df83bd050a59",
  "_last_modified_time": 1760503623127,
  "_last_modified_user": "wcp-cluster-user-f06fd228-8088-4439-a9e6-26c90a829c57-d34133d7-0fdf-4c9d-abcf-df83bd050a59",
  "_revision": 1
}
```
<a id="81-policy-api-v1-infra-lb-virtual-servers-capi-kubeadm-control-plane-webhook-service-443-tcp-29ytg"></a>
### 81. /policy/api/v1/infra/lb-virtual-servers/capi-kubeadm-control-plane-webhook-service_443_TCP_29ytg

**HTTP Methods:** GET, PATCH

**Explanation:**
NSX Policy API endpoint for resource management.

---


**Sample Response Body (GET, from logs):**
```json
{
  "enabled": true,
  "ip_address": "172.24.13.161",
  "ports": [
    "443"
  ],
  "access_log_enabled": false,
  "lb_service_path": "/infra/lb-services/clusterip_f06fd228-8088-4439-a9e6-26c90a829c57_dlb",
  "pool_path": "/infra/lb-pools/capi-kubeadm-control-plane-webhook-service_443_TCP_29ytg",
  "application_profile_path": "/infra/lb-app-profiles/default-tcp-lb-app-profile",
  "log_significant_event_only": false,
  "resource_type": "LBVirtualServer",
  "id": "capi-kubeadm-control-plane-webhook-service_443_TCP_29ytg",
  "display_name": "capi-kubeadm-control-plane-webhook-service_443_TCP",
  "tags": [
    {
      "scope": "ncp/version",
      "tag": "1.2.0"
    },
    {
      "scope": "ncp/cluster",
      "tag": "f06fd228-8088-4439-a9e6-26c90a829c57"
    },
    {
      "scope": "ncp/project",
      "tag": "svc-tkg-jrsvf"
    },
    {
      "scope": "external_id",
      "tag": "2e18eda1-629c-47e0-a6d4-8a6dec2099e1"
    },
    {
      "scope": "ncp/service",
      "tag": "capi-kubeadm-control-plane-webhook-service"
    },
    {
      "scope": "ncp/service_uid",
      "tag": "2e18eda1-629c-47e0-a6d4-8a6dec2099e1"
    },
    {
      "scope": "ncp/service_port",
      "tag": "443"
    },
    {
      "scope": "ncp/service_port_protocol",
      "tag": "TCP"
    },
    {
      "scope": "ncp/created_for",
      "tag": "DLB"
    }
  ],
  "path": "/infra/lb-virtual-servers/capi-kubeadm-control-plane-webhook-service_443_TCP_29ytg",
  "relative_path": "capi-kubeadm-control-plane-webhook-service_443_TCP_29ytg",
  "parent_path": "/infra",
  "remote_path": "",
  "unique_id": "835fe5ff-655a-42c7-b713-daa1dabc7794",
  "realization_id": "835fe5ff-655a-42c7-b713-daa1dabc7794",
  "owner_id": "42495ba4-8c0b-49c9-b645-84cc39c2df30",
  "marked_for_delete": false,
  "overridden": false,
  "_system_owned": false,
  "_protection": "NOT_PROTECTED",
  "_create_time": 1760504056759,
  "_create_user": "wcp-cluster-user-f06fd228-8088-4439-a9e6-26c90a829c57-d34133d7-0fdf-4c9d-abcf-df83bd050a59",
  "_last_modified_time": 1760504058915,
  "_last_modified_user": "wcp-cluster-user-f06fd228-8088-4439-a9e6-26c90a829c57-d34133d7-0fdf-4c9d-abcf-df83bd050a59",
  "_revision": 1
}
```
<a id="82-policy-api-v1-infra-lb-virtual-servers-vmware-system-nsx-operator-webhook-service-443-tcp-apze8"></a>
### 82. /policy/api/v1/infra/lb-virtual-servers/vmware-system-nsx-operator-webhook-service_443_TCP_apze8

**HTTP Methods:** GET, PATCH

**Explanation:**
NSX Policy API endpoint for resource management.

---


**Sample Response Body (GET, from logs):**
```json
{
  "enabled": true,
  "ip_address": "172.24.13.55",
  "ports": [
    "443"
  ],
  "access_log_enabled": false,
  "lb_service_path": "/infra/lb-services/clusterip_f06fd228-8088-4439-a9e6-26c90a829c57_dlb",
  "pool_path": "/infra/lb-pools/vmware-system-nsx-operator-webhook-service_443_TCP_apze8",
  "application_profile_path": "/infra/lb-app-profiles/default-tcp-lb-app-profile",
  "log_significant_event_only": false,
  "resource_type": "LBVirtualServer",
  "id": "vmware-system-nsx-operator-webhook-service_443_TCP_apze8",
  "display_name": "vmware-system-nsx-operator-webhook-service_443_TCP",
  "tags": [
    {
      "scope": "ncp/version",
      "tag": "1.2.0"
    },
    {
      "scope": "ncp/cluster",
      "tag": "f06fd228-8088-4439-a9e6-26c90a829c57"
    },
    {
      "scope": "ncp/project",
      "tag": "vmware-system-nsx"
    },
    {
      "scope": "external_id",
      "tag": "417c1230-e1f1-4049-9bdc-8f619032b163"
    },
    {
      "scope": "ncp/service",
      "tag": "vmware-system-nsx-operator-webhook-service"
    },
    {
      "scope": "ncp/service_uid",
      "tag": "417c1230-e1f1-4049-9bdc-8f619032b163"
    },
    {
      "scope": "ncp/service_port",
      "tag": "443"
    },
    {
      "scope": "ncp/service_port_protocol",
      "tag": "TCP"
    },
    {
      "scope": "ncp/created_for",
      "tag": "DLB"
    }
  ],
  "path": "/infra/lb-virtual-servers/vmware-system-nsx-operator-webhook-service_443_TCP_apze8",
  "relative_path": "vmware-system-nsx-operator-webhook-service_443_TCP_apze8",
  "parent_path": "/infra",
  "remote_path": "",
  "unique_id": "faf50da2-6677-4bdf-a41e-93e7929cf0ce",
  "realization_id": "faf50da2-6677-4bdf-a41e-93e7929cf0ce",
  "owner_id": "42495ba4-8c0b-49c9-b645-84cc39c2df30",
  "marked_for_delete": false,
  "overridden": false,
  "_system_owned": false,
  "_protection": "NOT_PROTECTED",
  "_create_time": 1760503464356,
  "_create_user": "wcp-cluster-user-f06fd228-8088-4439-a9e6-26c90a829c57-d34133d7-0fdf-4c9d-abcf-df83bd050a59",
  "_last_modified_time": 1760503623850,
  "_last_modified_user": "wcp-cluster-user-f06fd228-8088-4439-a9e6-26c90a829c57-d34133d7-0fdf-4c9d-abcf-df83bd050a59",
  "_revision": 1
}
```
<a id="83-policy-api-v1-infra-lb-virtual-servers-vmware-system-psp-operator-webhook-service-443-tcp-n4jep"></a>
### 83. /policy/api/v1/infra/lb-virtual-servers/vmware-system-psp-operator-webhook-service_443_TCP_n4jep

**HTTP Methods:** GET, PATCH

**Explanation:**
NSX Policy API endpoint for resource management.

---


**Sample Response Body (GET, from logs):**
```json
{
  "enabled": true,
  "ip_address": "172.24.138.148",
  "ports": [
    "443"
  ],
  "access_log_enabled": false,
  "lb_service_path": "/infra/lb-services/clusterip_f06fd228-8088-4439-a9e6-26c90a829c57_dlb",
  "pool_path": "/infra/lb-pools/vmware-system-psp-operator-webhook-service_443_TCP_n4jep",
  "application_profile_path": "/infra/lb-app-profiles/default-tcp-lb-app-profile",
  "log_significant_event_only": false,
  "resource_type": "LBVirtualServer",
  "id": "vmware-system-psp-operator-webhook-service_443_TCP_n4jep",
  "display_name": "vmware-system-psp-operator-webhook-service_443_TCP",
  "tags": [
    {
      "scope": "ncp/version",
      "tag": "1.2.0"
    },
    {
      "scope": "ncp/cluster",
      "tag": "f06fd228-8088-4439-a9e6-26c90a829c57"
    },
    {
      "scope": "ncp/project",
      "tag": "vmware-system-appplatform-operator-system"
    },
    {
      "scope": "external_id",
      "tag": "437e404b-bfdd-41ee-832d-d36d2c669b07"
    },
    {
      "scope": "ncp/service",
      "tag": "vmware-system-psp-operator-webhook-service"
    },
    {
      "scope": "ncp/service_uid",
      "tag": "437e404b-bfdd-41ee-832d-d36d2c669b07"
    },
    {
      "scope": "ncp/service_port",
      "tag": "443"
    },
    {
      "scope": "ncp/service_port_protocol",
      "tag": "TCP"
    },
    {
      "scope": "ncp/created_for",
      "tag": "DLB"
    }
  ],
  "path": "/infra/lb-virtual-servers/vmware-system-psp-operator-webhook-service_443_TCP_n4jep",
  "relative_path": "vmware-system-psp-operator-webhook-service_443_TCP_n4jep",
  "parent_path": "/infra",
  "remote_path": "",
  "unique_id": "d8dbbd7b-da69-4373-91b0-c5ee87b48338",
  "realization_id": "d8dbbd7b-da69-4373-91b0-c5ee87b48338",
  "owner_id": "42495ba4-8c0b-49c9-b645-84cc39c2df30",
  "marked_for_delete": false,
  "overridden": false,
  "_system_owned": false,
  "_protection": "NOT_PROTECTED",
  "_create_time": 1760503474926,
  "_create_user": "wcp-cluster-user-f06fd228-8088-4439-a9e6-26c90a829c57-d34133d7-0fdf-4c9d-abcf-df83bd050a59",
  "_last_modified_time": 1760503618699,
  "_last_modified_user": "wcp-cluster-user-f06fd228-8088-4439-a9e6-26c90a829c57-d34133d7-0fdf-4c9d-abcf-df83bd050a59",
  "_revision": 1
}
```
<a id="84-policy-api-v1-infra-lb-virtual-servers-vmware-system-tkg-webhook-metrics-service-9947-tcp-ie9jg"></a>
### 84. /policy/api/v1/infra/lb-virtual-servers/vmware-system-tkg-webhook-metrics-service_9947_TCP_ie9jg

**HTTP Methods:** GET, PATCH

**Explanation:**
NSX Policy API endpoint for resource management.

---


**Sample Response Body (GET, from logs):**
```json
{
  "enabled": true,
  "ip_address": "172.24.63.29",
  "ports": [
    "9947"
  ],
  "access_log_enabled": false,
  "lb_service_path": "/infra/lb-services/clusterip_f06fd228-8088-4439-a9e6-26c90a829c57_dlb",
  "pool_path": "/infra/lb-pools/vmware-system-tkg-webhook-metrics-service_9947_TCP_ie9jg",
  "application_profile_path": "/infra/lb-app-profiles/default-tcp-lb-app-profile",
  "log_significant_event_only": false,
  "resource_type": "LBVirtualServer",
  "id": "vmware-system-tkg-webhook-metrics-service_9947_TCP_ie9jg",
  "display_name": "vmware-system-tkg-webhook-metrics-service_9947_TCP",
  "tags": [
    {
      "scope": "ncp/version",
      "tag": "1.2.0"
    },
    {
      "scope": "ncp/cluster",
      "tag": "f06fd228-8088-4439-a9e6-26c90a829c57"
    },
    {
      "scope": "ncp/project",
      "tag": "svc-tkg-jrsvf"
    },
    {
      "scope": "external_id",
      "tag": "38a86354-1337-4207-ad73-40c8a572091d"
    },
    {
      "scope": "ncp/service",
      "tag": "vmware-system-tkg-webhook-metrics-service"
    },
    {
      "scope": "ncp/service_uid",
      "tag": "38a86354-1337-4207-ad73-40c8a572091d"
    },
    {
      "scope": "ncp/service_port",
      "tag": "9947"
    },
    {
      "scope": "ncp/service_port_protocol",
      "tag": "TCP"
    },
    {
      "scope": "ncp/created_for",
      "tag": "DLB"
    }
  ],
  "path": "/infra/lb-virtual-servers/vmware-system-tkg-webhook-metrics-service_9947_TCP_ie9jg",
  "relative_path": "vmware-system-tkg-webhook-metrics-service_9947_TCP_ie9jg",
  "parent_path": "/infra",
  "remote_path": "",
  "unique_id": "512e6dd6-7ffd-4fed-80ba-73e5ca938347",
  "realization_id": "512e6dd6-7ffd-4fed-80ba-73e5ca938347",
  "owner_id": "42495ba4-8c0b-49c9-b645-84cc39c2df30",
  "marked_for_delete": false,
  "overridden": false,
  "_system_owned": false,
  "_protection": "NOT_PROTECTED",
  "_create_time": 1760504108522,
  "_create_user": "wcp-cluster-user-f06fd228-8088-4439-a9e6-26c90a829c57-d34133d7-0fdf-4c9d-abcf-df83bd050a59",
  "_last_modified_time": 1760504110315,
  "_last_modified_user": "wcp-cluster-user-f06fd228-8088-4439-a9e6-26c90a829c57-d34133d7-0fdf-4c9d-abcf-df83bd050a59",
  "_revision": 1
}
```
<a id="85-policy-api-v1-infra-lb-virtual-servers-vmware-system-imageregistry-webhook-service-443-tcp-ebvnb"></a>
### 85. /policy/api/v1/infra/lb-virtual-servers/vmware-system-imageregistry-webhook-service_443_TCP_ebvnb

**HTTP Methods:** GET, PATCH

**Explanation:**
NSX Policy API endpoint for resource management.

---


**Sample Response Body (GET, from logs):**
```json
{
  "enabled": true,
  "ip_address": "172.24.58.82",
  "ports": [
    "443"
  ],
  "access_log_enabled": false,
  "lb_service_path": "/infra/lb-services/clusterip_f06fd228-8088-4439-a9e6-26c90a829c57_dlb",
  "pool_path": "/infra/lb-pools/vmware-system-imageregistry-webhook-service_443_TCP_ebvnb",
  "application_profile_path": "/infra/lb-app-profiles/default-tcp-lb-app-profile",
  "log_significant_event_only": false,
  "resource_type": "LBVirtualServer",
  "id": "vmware-system-imageregistry-webhook-service_443_TCP_ebvnb",
  "display_name": "vmware-system-imageregistry-webhook-service_443_TCP",
  "tags": [
    {
      "scope": "ncp/version",
      "tag": "1.2.0"
    },
    {
      "scope": "ncp/cluster",
      "tag": "f06fd228-8088-4439-a9e6-26c90a829c57"
    },
    {
      "scope": "ncp/project",
      "tag": "vmware-system-imageregistry"
    },
    {
      "scope": "external_id",
      "tag": "466f67d3-8565-4c36-a51c-c065212afd2b"
    },
    {
      "scope": "ncp/service",
      "tag": "vmware-system-imageregistry-webhook-service"
    },
    {
      "scope": "ncp/service_uid",
      "tag": "466f67d3-8565-4c36-a51c-c065212afd2b"
    },
    {
      "scope": "ncp/service_port",
      "tag": "443"
    },
    {
      "scope": "ncp/service_port_protocol",
      "tag": "TCP"
    },
    {
      "scope": "ncp/created_for",
      "tag": "DLB"
    }
  ],
  "path": "/infra/lb-virtual-servers/vmware-system-imageregistry-webhook-service_443_TCP_ebvnb",
  "relative_path": "vmware-system-imageregistry-webhook-service_443_TCP_ebvnb",
  "parent_path": "/infra",
  "remote_path": "",
  "unique_id": "e93d0f19-98b6-4e63-91bb-9d369e204e2b",
  "realization_id": "e93d0f19-98b6-4e63-91bb-9d369e204e2b",
  "owner_id": "42495ba4-8c0b-49c9-b645-84cc39c2df30",
  "marked_for_delete": false,
  "overridden": false,
  "_system_owned": false,
  "_protection": "NOT_PROTECTED",
  "_create_time": 1760503477687,
  "_create_user": "wcp-cluster-user-f06fd228-8088-4439-a9e6-26c90a829c57-d34133d7-0fdf-4c9d-abcf-df83bd050a59",
  "_last_modified_time": 1760503619922,
  "_last_modified_user": "wcp-cluster-user-f06fd228-8088-4439-a9e6-26c90a829c57-d34133d7-0fdf-4c9d-abcf-df83bd050a59",
  "_revision": 1
}
```
<a id="86-policy-api-v1-infra-lb-virtual-servers-vmware-system-observability-webhook-service-443-tcp-mh1m0"></a>
### 86. /policy/api/v1/infra/lb-virtual-servers/vmware-system-observability-webhook-service_443_TCP_mh1m0

**HTTP Methods:** GET, PATCH

**Explanation:**
NSX Policy API endpoint for resource management.

---


**Sample Response Body (GET, from logs):**
```json
{
  "enabled": true,
  "ip_address": "172.24.96.93",
  "ports": [
    "443"
  ],
  "access_log_enabled": false,
  "lb_service_path": "/infra/lb-services/clusterip_f06fd228-8088-4439-a9e6-26c90a829c57_dlb",
  "pool_path": "/infra/lb-pools/vmware-system-observability-webhook-service_443_TCP_mh1m0",
  "application_profile_path": "/infra/lb-app-profiles/default-tcp-lb-app-profile",
  "log_significant_event_only": false,
  "resource_type": "LBVirtualServer",
  "id": "vmware-system-observability-webhook-service_443_TCP_mh1m0",
  "display_name": "vmware-system-observability-webhook-service_443_TCP",
  "tags": [
    {
      "scope": "ncp/version",
      "tag": "1.2.0"
    },
    {
      "scope": "ncp/cluster",
      "tag": "f06fd228-8088-4439-a9e6-26c90a829c57"
    },
    {
      "scope": "ncp/project",
      "tag": "vmware-system-monitoring"
    },
    {
      "scope": "external_id",
      "tag": "13642ebb-a490-45a8-9a32-d557f9188066"
    },
    {
      "scope": "ncp/service",
      "tag": "vmware-system-observability-webhook-service"
    },
    {
      "scope": "ncp/service_uid",
      "tag": "13642ebb-a490-45a8-9a32-d557f9188066"
    },
    {
      "scope": "ncp/service_port",
      "tag": "443"
    },
    {
      "scope": "ncp/service_port_protocol",
      "tag": "TCP"
    },
    {
      "scope": "ncp/created_for",
      "tag": "DLB"
    }
  ],
  "path": "/infra/lb-virtual-servers/vmware-system-observability-webhook-service_443_TCP_mh1m0",
  "relative_path": "vmware-system-observability-webhook-service_443_TCP_mh1m0",
  "parent_path": "/infra",
  "remote_path": "",
  "unique_id": "8dd97110-39b4-41d0-ab56-36e9cb436c9e",
  "realization_id": "8dd97110-39b4-41d0-ab56-36e9cb436c9e",
  "owner_id": "42495ba4-8c0b-49c9-b645-84cc39c2df30",
  "marked_for_delete": false,
  "overridden": false,
  "_system_owned": false,
  "_protection": "NOT_PROTECTED",
  "_create_time": 1760503446085,
  "_create_user": "wcp-cluster-user-f06fd228-8088-4439-a9e6-26c90a829c57-d34133d7-0fdf-4c9d-abcf-df83bd050a59",
  "_last_modified_time": 1760503623848,
  "_last_modified_user": "wcp-cluster-user-f06fd228-8088-4439-a9e6-26c90a829c57-d34133d7-0fdf-4c9d-abcf-df83bd050a59",
  "_revision": 1
}
```
<a id="87-policy-api-v1-infra-lb-virtual-servers-vmware-system-mobility-operator-webhook-service-443-tcp-2u6xd"></a>
### 87. /policy/api/v1/infra/lb-virtual-servers/vmware-system-mobility-operator-webhook-service_443_TCP_2u6xd

**HTTP Methods:** GET, PATCH

**Explanation:**
NSX Policy API endpoint for resource management.

---


**Sample Response Body (GET, from logs):**
```json
{
  "enabled": true,
  "ip_address": "172.24.156.249",
  "ports": [
    "443"
  ],
  "access_log_enabled": false,
  "lb_service_path": "/infra/lb-services/clusterip_f06fd228-8088-4439-a9e6-26c90a829c57_dlb",
  "pool_path": "/infra/lb-pools/vmware-system-mobility-operator-webhook-service_443_TCP_2u6xd",
  "application_profile_path": "/infra/lb-app-profiles/default-tcp-lb-app-profile",
  "log_significant_event_only": false,
  "resource_type": "LBVirtualServer",
  "id": "vmware-system-mobility-operator-webhook-service_443_TCP_2u6xd",
  "display_name": "vmware-system-mobility-operator-webhook-service_443_TCP",
  "tags": [
    {
      "scope": "ncp/version",
      "tag": "1.2.0"
    },
    {
      "scope": "ncp/cluster",
      "tag": "f06fd228-8088-4439-a9e6-26c90a829c57"
    },
    {
      "scope": "ncp/project",
      "tag": "vmware-system-mobility-operator"
    },
    {
      "scope": "external_id",
      "tag": "5639ed56-79a1-4660-8cdc-27df7f45583d"
    },
    {
      "scope": "ncp/service",
      "tag": "vmware-system-mobility-operator-webhook-service"
    },
    {
      "scope": "ncp/service_uid",
      "tag": "5639ed56-79a1-4660-8cdc-27df7f45583d"
    },
    {
      "scope": "ncp/service_port",
      "tag": "443"
    },
    {
      "scope": "ncp/service_port_protocol",
      "tag": "TCP"
    },
    {
      "scope": "ncp/created_for",
      "tag": "DLB"
    }
  ],
  "path": "/infra/lb-virtual-servers/vmware-system-mobility-operator-webhook-service_443_TCP_2u6xd",
  "relative_path": "vmware-system-mobility-operator-webhook-service_443_TCP_2u6xd",
  "parent_path": "/infra",
  "remote_path": "",
  "unique_id": "001d9968-f583-4f4c-aab2-cba2b61eef74",
  "realization_id": "001d9968-f583-4f4c-aab2-cba2b61eef74",
  "owner_id": "42495ba4-8c0b-49c9-b645-84cc39c2df30",
  "marked_for_delete": false,
  "overridden": false,
  "_system_owned": false,
  "_protection": "NOT_PROTECTED",
  "_create_time": 1760503446657,
  "_create_user": "wcp-cluster-user-f06fd228-8088-4439-a9e6-26c90a829c57-d34133d7-0fdf-4c9d-abcf-df83bd050a59",
  "_last_modified_time": 1760503622837,
  "_last_modified_user": "wcp-cluster-user-f06fd228-8088-4439-a9e6-26c90a829c57-d34133d7-0fdf-4c9d-abcf-df83bd050a59",
  "_revision": 1
}
```
<a id="88-policy-api-v1-infra-lb-virtual-servers-vmware-system-tkg-controller-manager-metrics-service-9847-tcp-e9fxc"></a>
### 88. /policy/api/v1/infra/lb-virtual-servers/vmware-system-tkg-controller-manager-metrics-service_9847_TCP_e9fxc

**HTTP Methods:** GET, PATCH

**Explanation:**
NSX Policy API endpoint for resource management.

---


**Sample Response Body (GET, from logs):**
```json
{
  "enabled": true,
  "ip_address": "172.24.124.94",
  "ports": [
    "9847"
  ],
  "access_log_enabled": false,
  "lb_service_path": "/infra/lb-services/clusterip_f06fd228-8088-4439-a9e6-26c90a829c57_dlb",
  "pool_path": "/infra/lb-pools/vmware-system-tkg-controller-manager-metrics-service_9847_TCP_e9fxc",
  "application_profile_path": "/infra/lb-app-profiles/default-tcp-lb-app-profile",
  "log_significant_event_only": false,
  "resource_type": "LBVirtualServer",
  "id": "vmware-system-tkg-controller-manager-metrics-service_9847_TCP_e9fxc",
  "display_name": "vmware-system-tkg-controller-manager-metrics-service_9847_TCP",
  "tags": [
    {
      "scope": "ncp/version",
      "tag": "1.2.0"
    },
    {
      "scope": "ncp/cluster",
      "tag": "f06fd228-8088-4439-a9e6-26c90a829c57"
    },
    {
      "scope": "ncp/project",
      "tag": "svc-tkg-jrsvf"
    },
    {
      "scope": "external_id",
      "tag": "41568c96-bb56-4da1-8c88-cedeff46a148"
    },
    {
      "scope": "ncp/service",
      "tag": "vmware-system-tkg-controller-manager-metrics-service"
    },
    {
      "scope": "ncp/service_uid",
      "tag": "41568c96-bb56-4da1-8c88-cedeff46a148"
    },
    {
      "scope": "ncp/service_port",
      "tag": "9847"
    },
    {
      "scope": "ncp/service_port_protocol",
      "tag": "TCP"
    },
    {
      "scope": "ncp/created_for",
      "tag": "DLB"
    }
  ],
  "path": "/infra/lb-virtual-servers/vmware-system-tkg-controller-manager-metrics-service_9847_TCP_e9fxc",
  "relative_path": "vmware-system-tkg-controller-manager-metrics-service_9847_TCP_e9fxc",
  "parent_path": "/infra",
  "remote_path": "",
  "unique_id": "f89e4b32-b967-457d-81a7-8b6d0d6410b5",
  "realization_id": "f89e4b32-b967-457d-81a7-8b6d0d6410b5",
  "owner_id": "42495ba4-8c0b-49c9-b645-84cc39c2df30",
  "marked_for_delete": false,
  "overridden": false,
  "_system_owned": false,
  "_protection": "NOT_PROTECTED",
  "_create_time": 1760504108561,
  "_create_user": "wcp-cluster-user-f06fd228-8088-4439-a9e6-26c90a829c57-d34133d7-0fdf-4c9d-abcf-df83bd050a59",
  "_last_modified_time": 1760504110610,
  "_last_modified_user": "wcp-cluster-user-f06fd228-8088-4439-a9e6-26c90a829c57-d34133d7-0fdf-4c9d-abcf-df83bd050a59",
  "_revision": 1
}
```
<a id="89-policy-api-v1-infra-lb-virtual-servers-vmware-system-vmop-controller-manager-metrics-service-9848-tcp-qgstw"></a>
### 89. /policy/api/v1/infra/lb-virtual-servers/vmware-system-vmop-controller-manager-metrics-service_9848_TCP_qgstw

**HTTP Methods:** GET, PATCH

**Explanation:**
NSX Policy API endpoint for resource management.

---


**Sample Response Body (GET, from logs):**
```json
{
  "enabled": true,
  "ip_address": "172.24.179.65",
  "ports": [
    "9848"
  ],
  "access_log_enabled": false,
  "lb_service_path": "/infra/lb-services/clusterip_f06fd228-8088-4439-a9e6-26c90a829c57_dlb",
  "pool_path": "/infra/lb-pools/vmware-system-vmop-controller-manager-metrics-service_9848_TCP_qgstw",
  "application_profile_path": "/infra/lb-app-profiles/default-tcp-lb-app-profile",
  "log_significant_event_only": false,
  "resource_type": "LBVirtualServer",
  "id": "vmware-system-vmop-controller-manager-metrics-service_9848_TCP_qgstw",
  "display_name": "vmware-system-vmop-controller-manager-metrics-service_9848_TCP",
  "tags": [
    {
      "scope": "ncp/version",
      "tag": "1.2.0"
    },
    {
      "scope": "ncp/cluster",
      "tag": "f06fd228-8088-4439-a9e6-26c90a829c57"
    },
    {
      "scope": "ncp/project",
      "tag": "vmware-system-vmop"
    },
    {
      "scope": "external_id",
      "tag": "b0a0a35b-a011-4421-a900-97a0ceab15f6"
    },
    {
      "scope": "ncp/service",
      "tag": "vmware-system-vmop-controller-manager-metrics-service"
    },
    {
      "scope": "ncp/service_uid",
      "tag": "b0a0a35b-a011-4421-a900-97a0ceab15f6"
    },
    {
      "scope": "ncp/service_port",
      "tag": "9848"
    },
    {
      "scope": "ncp/service_port_protocol",
      "tag": "TCP"
    },
    {
      "scope": "ncp/created_for",
      "tag": "DLB"
    }
  ],
  "path": "/infra/lb-virtual-servers/vmware-system-vmop-controller-manager-metrics-service_9848_TCP_qgstw",
  "relative_path": "vmware-system-vmop-controller-manager-metrics-service_9848_TCP_qgstw",
  "parent_path": "/infra",
  "remote_path": "",
  "unique_id": "f48faea8-46cd-4d6d-93c9-ea0cb491cc44",
  "realization_id": "f48faea8-46cd-4d6d-93c9-ea0cb491cc44",
  "owner_id": "42495ba4-8c0b-49c9-b645-84cc39c2df30",
  "marked_for_delete": false,
  "overridden": false,
  "_system_owned": false,
  "_protection": "NOT_PROTECTED",
  "_create_time": 1760503459657,
  "_create_user": "wcp-cluster-user-f06fd228-8088-4439-a9e6-26c90a829c57-d34133d7-0fdf-4c9d-abcf-df83bd050a59",
  "_last_modified_time": 1760503621095,
  "_last_modified_user": "wcp-cluster-user-f06fd228-8088-4439-a9e6-26c90a829c57-d34133d7-0fdf-4c9d-abcf-df83bd050a59",
  "_revision": 1
}
```
<a id="90-policy-api-v1-infra-lb-virtual-servers-vmware-system-netop-controller-manager-metrics-service-9851-tcp-rfjax"></a>
### 90. /policy/api/v1/infra/lb-virtual-servers/vmware-system-netop-controller-manager-metrics-service_9851_TCP_rfjax

**HTTP Methods:** GET, PATCH

**Explanation:**
NSX Policy API endpoint for resource management.

---


**Sample Response Body (GET, from logs):**
```json
{
  "enabled": true,
  "ip_address": "172.24.51.129",
  "ports": [
    "9851"
  ],
  "access_log_enabled": false,
  "lb_service_path": "/infra/lb-services/clusterip_f06fd228-8088-4439-a9e6-26c90a829c57_dlb",
  "pool_path": "/infra/lb-pools/vmware-system-netop-controller-manager-metrics-service_9851_TCP_rfjax",
  "application_profile_path": "/infra/lb-app-profiles/default-tcp-lb-app-profile",
  "log_significant_event_only": false,
  "resource_type": "LBVirtualServer",
  "id": "vmware-system-netop-controller-manager-metrics-service_9851_TCP_rfjax",
  "display_name": "vmware-system-netop-controller-manager-metrics-service_9851_TCP",
  "tags": [
    {
      "scope": "ncp/version",
      "tag": "1.2.0"
    },
    {
      "scope": "ncp/cluster",
      "tag": "f06fd228-8088-4439-a9e6-26c90a829c57"
    },
    {
      "scope": "ncp/project",
      "tag": "vmware-system-netop"
    },
    {
      "scope": "external_id",
      "tag": "96f2c2c7-2fbd-4efb-92a6-233f4d5ec552"
    },
    {
      "scope": "ncp/service",
      "tag": "vmware-system-netop-controller-manager-metrics-service"
    },
    {
      "scope": "ncp/service_uid",
      "tag": "96f2c2c7-2fbd-4efb-92a6-233f4d5ec552"
    },
    {
      "scope": "ncp/service_port",
      "tag": "9851"
    },
    {
      "scope": "ncp/service_port_protocol",
      "tag": "TCP"
    },
    {
      "scope": "ncp/created_for",
      "tag": "DLB"
    }
  ],
  "path": "/infra/lb-virtual-servers/vmware-system-netop-controller-manager-metrics-service_9851_TCP_rfjax",
  "relative_path": "vmware-system-netop-controller-manager-metrics-service_9851_TCP_rfjax",
  "parent_path": "/infra",
  "remote_path": "",
  "unique_id": "26e8d5bf-c485-4b51-aeeb-62195b933054",
  "realization_id": "26e8d5bf-c485-4b51-aeeb-62195b933054",
  "owner_id": "42495ba4-8c0b-49c9-b645-84cc39c2df30",
  "marked_for_delete": false,
  "overridden": false,
  "_system_owned": false,
  "_protection": "NOT_PROTECTED",
  "_create_time": 1760503460627,
  "_create_user": "wcp-cluster-user-f06fd228-8088-4439-a9e6-26c90a829c57-d34133d7-0fdf-4c9d-abcf-df83bd050a59",
  "_last_modified_time": 1760503623127,
  "_last_modified_user": "wcp-cluster-user-f06fd228-8088-4439-a9e6-26c90a829c57-d34133d7-0fdf-4c9d-abcf-df83bd050a59",
  "_revision": 1
}
```
<a id="91-policy-api-v1-infra-lb-virtual-servers-vmware-system-psp-operator-k8s-cloud-operator-service-29002-tcp-dcp8m"></a>
### 91. /policy/api/v1/infra/lb-virtual-servers/vmware-system-psp-operator-k8s-cloud-operator-service_29002_TCP_dcp8m

**HTTP Methods:** GET, PATCH

**Explanation:**
NSX Policy API endpoint for resource management.

---


**Sample Response Body (GET, from logs):**
```json
{
  "enabled": true,
  "ip_address": "172.24.188.23",
  "ports": [
    "29002"
  ],
  "access_log_enabled": false,
  "lb_service_path": "/infra/lb-services/clusterip_f06fd228-8088-4439-a9e6-26c90a829c57_dlb",
  "pool_path": "/infra/lb-pools/vmware-system-psp-operator-k8s-cloud-operator-service_29002_TCP_dcp8m",
  "application_profile_path": "/infra/lb-app-profiles/default-tcp-lb-app-profile",
  "log_significant_event_only": false,
  "resource_type": "LBVirtualServer",
  "id": "vmware-system-psp-operator-k8s-cloud-operator-service_29002_TCP_dcp8m",
  "display_name": "vmware-system-psp-operator-k8s-cloud-operator-service_29002_TCP",
  "tags": [
    {
      "scope": "ncp/version",
      "tag": "1.2.0"
    },
    {
      "scope": "ncp/cluster",
      "tag": "f06fd228-8088-4439-a9e6-26c90a829c57"
    },
    {
      "scope": "ncp/project",
      "tag": "vmware-system-appplatform-operator-system"
    },
    {
      "scope": "external_id",
      "tag": "91c6c267-f1fe-47b1-b881-e950d29d7ae1"
    },
    {
      "scope": "ncp/service",
      "tag": "vmware-system-psp-operator-k8s-cloud-operator-service"
    },
    {
      "scope": "ncp/service_uid",
      "tag": "91c6c267-f1fe-47b1-b881-e950d29d7ae1"
    },
    {
      "scope": "ncp/service_port",
      "tag": "29002"
    },
    {
      "scope": "ncp/service_port_protocol",
      "tag": "TCP"
    },
    {
      "scope": "ncp/created_for",
      "tag": "DLB"
    }
  ],
  "path": "/infra/lb-virtual-servers/vmware-system-psp-operator-k8s-cloud-operator-service_29002_TCP_dcp8m",
  "relative_path": "vmware-system-psp-operator-k8s-cloud-operator-service_29002_TCP_dcp8m",
  "parent_path": "/infra",
  "remote_path": "",
  "unique_id": "8abe688a-6ef2-4715-b2b8-35d79bb7e7f2",
  "realization_id": "8abe688a-6ef2-4715-b2b8-35d79bb7e7f2",
  "owner_id": "42495ba4-8c0b-49c9-b645-84cc39c2df30",
  "marked_for_delete": false,
  "overridden": false,
  "_system_owned": false,
  "_protection": "NOT_PROTECTED",
  "_create_time": 1760503475949,
  "_create_user": "wcp-cluster-user-f06fd228-8088-4439-a9e6-26c90a829c57-d34133d7-0fdf-4c9d-abcf-df83bd050a59",
  "_last_modified_time": 1760503621064,
  "_last_modified_user": "wcp-cluster-user-f06fd228-8088-4439-a9e6-26c90a829c57-d34133d7-0fdf-4c9d-abcf-df83bd050a59",
  "_revision": 1
}
```
<a id="92-policy-api-v1-infra-lb-virtual-servers-capi-kubeadm-bootstrap-controller-manager-metrics-service-9845-tcp-1rbtg"></a>
### 92. /policy/api/v1/infra/lb-virtual-servers/capi-kubeadm-bootstrap-controller-manager-metrics-service_9845_TCP_1rbtg

**HTTP Methods:** GET, PATCH

**Explanation:**
NSX Policy API endpoint for resource management.

---


**Sample Response Body (GET, from logs):**
```json
{
  "enabled": true,
  "ip_address": "172.24.45.32",
  "ports": [
    "9845"
  ],
  "access_log_enabled": false,
  "lb_service_path": "/infra/lb-services/clusterip_f06fd228-8088-4439-a9e6-26c90a829c57_dlb",
  "pool_path": "/infra/lb-pools/capi-kubeadm-bootstrap-controller-manager-metrics-service_9845_TCP_1rbtg",
  "application_profile_path": "/infra/lb-app-profiles/default-tcp-lb-app-profile",
  "log_significant_event_only": false,
  "resource_type": "LBVirtualServer",
  "id": "capi-kubeadm-bootstrap-controller-manager-metrics-service_9845_TCP_1rbtg",
  "display_name": "capi-kubeadm-bootstrap-controller-manager-metrics-service_9845_TCP",
  "tags": [
    {
      "scope": "ncp/version",
      "tag": "1.2.0"
    },
    {
      "scope": "ncp/cluster",
      "tag": "f06fd228-8088-4439-a9e6-26c90a829c57"
    },
    {
      "scope": "ncp/project",
      "tag": "svc-tkg-jrsvf"
    },
    {
      "scope": "external_id",
      "tag": "9de0ca41-e8f2-4377-8af9-70aa004353d2"
    },
    {
      "scope": "ncp/service",
      "tag": "capi-kubeadm-bootstrap-controller-manager-metrics-service"
    },
    {
      "scope": "ncp/service_uid",
      "tag": "9de0ca41-e8f2-4377-8af9-70aa004353d2"
    },
    {
      "scope": "ncp/service_port",
      "tag": "9845"
    },
    {
      "scope": "ncp/service_port_protocol",
      "tag": "TCP"
    },
    {
      "scope": "ncp/created_for",
      "tag": "DLB"
    }
  ],
  "path": "/infra/lb-virtual-servers/capi-kubeadm-bootstrap-controller-manager-metrics-service_9845_TCP_1rbtg",
  "relative_path": "capi-kubeadm-bootstrap-controller-manager-metrics-service_9845_TCP_1rbtg",
  "parent_path": "/infra",
  "remote_path": "",
  "unique_id": "1fa392a5-c20c-4dec-91b8-3f4ae54bffd6",
  "realization_id": "1fa392a5-c20c-4dec-91b8-3f4ae54bffd6",
  "owner_id": "42495ba4-8c0b-49c9-b645-84cc39c2df30",
  "marked_for_delete": false,
  "overridden": false,
  "_system_owned": false,
  "_protection": "NOT_PROTECTED",
  "_create_time": 1760504056759,
  "_create_user": "wcp-cluster-user-f06fd228-8088-4439-a9e6-26c90a829c57-d34133d7-0fdf-4c9d-abcf-df83bd050a59",
  "_last_modified_time": 1760504058446,
  "_last_modified_user": "wcp-cluster-user-f06fd228-8088-4439-a9e6-26c90a829c57-d34133d7-0fdf-4c9d-abcf-df83bd050a59",
  "_revision": 1
}
```
<a id="93-policy-api-v1-infra-lb-virtual-servers-vmware-system-mobility-operator-controller-manager-metrics-9859-tcp-3y8qy"></a>
### 93. /policy/api/v1/infra/lb-virtual-servers/vmware-system-mobility-operator-controller-manager-metrics_9859_TCP_3y8qy

**HTTP Methods:** GET, PATCH

**Explanation:**
NSX Policy API endpoint for resource management.

---


**Sample Response Body (GET, from logs):**
```json
{
  "enabled": true,
  "ip_address": "172.24.38.61",
  "ports": [
    "9859"
  ],
  "access_log_enabled": false,
  "lb_service_path": "/infra/lb-services/clusterip_f06fd228-8088-4439-a9e6-26c90a829c57_dlb",
  "pool_path": "/infra/lb-pools/vmware-system-mobility-operator-controller-manager-metrics_9859_TCP_3y8qy",
  "application_profile_path": "/infra/lb-app-profiles/default-tcp-lb-app-profile",
  "log_significant_event_only": false,
  "resource_type": "LBVirtualServer",
  "id": "vmware-system-mobility-operator-controller-manager-metrics_9859_TCP_3y8qy",
  "display_name": "vmware-system-mobility-operator-controller-manager-metrics_9859_TCP",
  "tags": [
    {
      "scope": "ncp/version",
      "tag": "1.2.0"
    },
    {
      "scope": "ncp/cluster",
      "tag": "f06fd228-8088-4439-a9e6-26c90a829c57"
    },
    {
      "scope": "ncp/project",
      "tag": "vmware-system-mobility-operator"
    },
    {
      "scope": "external_id",
      "tag": "ea8f89d9-aa4b-46c8-870b-7a00e90120ae"
    },
    {
      "scope": "ncp/service",
      "tag": "vmware-system-mobility-operator-controller-manager-metrics"
    },
    {
      "scope": "ncp/service_uid",
      "tag": "ea8f89d9-aa4b-46c8-870b-7a00e90120ae"
    },
    {
      "scope": "ncp/service_port",
      "tag": "9859"
    },
    {
      "scope": "ncp/service_port_protocol",
      "tag": "TCP"
    },
    {
      "scope": "ncp/created_for",
      "tag": "DLB"
    }
  ],
  "path": "/infra/lb-virtual-servers/vmware-system-mobility-operator-controller-manager-metrics_9859_TCP_3y8qy",
  "relative_path": "vmware-system-mobility-operator-controller-manager-metrics_9859_TCP_3y8qy",
  "parent_path": "/infra",
  "remote_path": "",
  "unique_id": "3de6856a-c4e7-4690-958b-f9674ba0b6ca",
  "realization_id": "3de6856a-c4e7-4690-958b-f9674ba0b6ca",
  "owner_id": "42495ba4-8c0b-49c9-b645-84cc39c2df30",
  "marked_for_delete": false,
  "overridden": false,
  "_system_owned": false,
  "_protection": "NOT_PROTECTED",
  "_create_time": 1760503471464,
  "_create_user": "wcp-cluster-user-f06fd228-8088-4439-a9e6-26c90a829c57-d34133d7-0fdf-4c9d-abcf-df83bd050a59",
  "_last_modified_time": 1760503620852,
  "_last_modified_user": "wcp-cluster-user-f06fd228-8088-4439-a9e6-26c90a829c57-d34133d7-0fdf-4c9d-abcf-df83bd050a59",
  "_revision": 1
}
```
<a id="94-policy-api-v1-infra-lb-virtual-servers-capi-kubeadm-control-plane-controller-manager-metrics-service-9850-tcp-7eapm"></a>
### 94. /policy/api/v1/infra/lb-virtual-servers/capi-kubeadm-control-plane-controller-manager-metrics-service_9850_TCP_7eapm

**HTTP Methods:** GET, PATCH

**Explanation:**
NSX Policy API endpoint for resource management.

---


**Sample Response Body (GET, from logs):**
```json
{
  "enabled": true,
  "ip_address": "172.24.35.63",
  "ports": [
    "9850"
  ],
  "access_log_enabled": false,
  "lb_service_path": "/infra/lb-services/clusterip_f06fd228-8088-4439-a9e6-26c90a829c57_dlb",
  "pool_path": "/infra/lb-pools/capi-kubeadm-control-plane-controller-manager-metrics-service_9850_TCP_7eapm",
  "application_profile_path": "/infra/lb-app-profiles/default-tcp-lb-app-profile",
  "log_significant_event_only": false,
  "resource_type": "LBVirtualServer",
  "id": "capi-kubeadm-control-plane-controller-manager-metrics-service_9850_TCP_7eapm",
  "display_name": "capi-kubeadm-control-plane-controller-manager-metrics-service_9850_TCP",
  "tags": [
    {
      "scope": "ncp/version",
      "tag": "1.2.0"
    },
    {
      "scope": "ncp/cluster",
      "tag": "f06fd228-8088-4439-a9e6-26c90a829c57"
    },
    {
      "scope": "ncp/project",
      "tag": "svc-tkg-jrsvf"
    },
    {
      "scope": "external_id",
      "tag": "4a9f3b96-7c0c-4b36-9ca0-c54732e9454b"
    },
    {
      "scope": "ncp/service",
      "tag": "capi-kubeadm-control-plane-controller-manager-metrics-service"
    },
    {
      "scope": "ncp/service_uid",
      "tag": "4a9f3b96-7c0c-4b36-9ca0-c54732e9454b"
    },
    {
      "scope": "ncp/service_port",
      "tag": "9850"
    },
    {
      "scope": "ncp/service_port_protocol",
      "tag": "TCP"
    },
    {
      "scope": "ncp/created_for",
      "tag": "DLB"
    }
  ],
  "path": "/infra/lb-virtual-servers/capi-kubeadm-control-plane-controller-manager-metrics-service_9850_TCP_7eapm",
  "relative_path": "capi-kubeadm-control-plane-controller-manager-metrics-service_9850_TCP_7eapm",
  "parent_path": "/infra",
  "remote_path": "",
  "unique_id": "4160e525-ce10-4e38-9c02-32b6cdc7fd5a",
  "realization_id": "4160e525-ce10-4e38-9c02-32b6cdc7fd5a",
  "owner_id": "42495ba4-8c0b-49c9-b645-84cc39c2df30",
  "marked_for_delete": false,
  "overridden": false,
  "_system_owned": false,
  "_protection": "NOT_PROTECTED",
  "_create_time": 1760504056759,
  "_create_user": "wcp-cluster-user-f06fd228-8088-4439-a9e6-26c90a829c57-d34133d7-0fdf-4c9d-abcf-df83bd050a59",
  "_last_modified_time": 1760504058846,
  "_last_modified_user": "wcp-cluster-user-f06fd228-8088-4439-a9e6-26c90a829c57-d34133d7-0fdf-4c9d-abcf-df83bd050a59",
  "_revision": 1
}
```
<a id="95-policy-api-v1-infra-lb-virtual-servers-vmware-system-imageregistry-controller-manager-metrics-service-9857-tcp-k3hd3"></a>
### 95. /policy/api/v1/infra/lb-virtual-servers/vmware-system-imageregistry-controller-manager-metrics-service_9857_TCP_k3hd3

**HTTP Methods:** GET, PATCH

**Explanation:**
NSX Policy API endpoint for resource management.

---


**Sample Response Body (GET, from logs):**
```json
{
  "enabled": true,
  "ip_address": "172.24.106.156",
  "ports": [
    "9857"
  ],
  "access_log_enabled": false,
  "lb_service_path": "/infra/lb-services/clusterip_f06fd228-8088-4439-a9e6-26c90a829c57_dlb",
  "pool_path": "/infra/lb-pools/vmware-system-imageregistry-controller-manager-metrics-service_9857_TCP_k3hd3",
  "application_profile_path": "/infra/lb-app-profiles/default-tcp-lb-app-profile",
  "log_significant_event_only": false,
  "resource_type": "LBVirtualServer",
  "id": "vmware-system-imageregistry-controller-manager-metrics-service_9857_TCP_k3hd3",
  "display_name": "vmware-system-imageregistry-controller-manager-metrics-service_9857_TCP",
  "tags": [
    {
      "scope": "ncp/version",
      "tag": "1.2.0"
    },
    {
      "scope": "ncp/cluster",
      "tag": "f06fd228-8088-4439-a9e6-26c90a829c57"
    },
    {
      "scope": "ncp/project",
      "tag": "vmware-system-imageregistry"
    },
    {
      "scope": "external_id",
      "tag": "f06cf673-0808-4934-9190-5ea20b2e295d"
    },
    {
      "scope": "ncp/service",
      "tag": "vmware-system-imageregistry-controller-manager-metrics-service"
    },
    {
      "scope": "ncp/service_uid",
      "tag": "f06cf673-0808-4934-9190-5ea20b2e295d"
    },
    {
      "scope": "ncp/service_port",
      "tag": "9857"
    },
    {
      "scope": "ncp/service_port_protocol",
      "tag": "TCP"
    },
    {
      "scope": "ncp/created_for",
      "tag": "DLB"
    }
  ],
  "path": "/infra/lb-virtual-servers/vmware-system-imageregistry-controller-manager-metrics-service_9857_TCP_k3hd3",
  "relative_path": "vmware-system-imageregistry-controller-manager-metrics-service_9857_TCP_k3hd3",
  "parent_path": "/infra",
  "remote_path": "",
  "unique_id": "f833b3c6-c028-49b5-960d-df346d20a65b",
  "realization_id": "f833b3c6-c028-49b5-960d-df346d20a65b",
  "owner_id": "42495ba4-8c0b-49c9-b645-84cc39c2df30",
  "marked_for_delete": false,
  "overridden": false,
  "_system_owned": false,
  "_protection": "NOT_PROTECTED",
  "_create_time": 1760503477227,
  "_create_user": "wcp-cluster-user-f06fd228-8088-4439-a9e6-26c90a829c57-d34133d7-0fdf-4c9d-abcf-df83bd050a59",
  "_last_modified_time": 1760503480257,
  "_last_modified_user": "wcp-cluster-user-f06fd228-8088-4439-a9e6-26c90a829c57-d34133d7-0fdf-4c9d-abcf-df83bd050a59",
  "_revision": 1
}
```
<a id="96-policy-api-v1-infra-lb-virtual-servers-vmware-system-observability-controller-manager-metrics-service-9889-tcp-nus7f"></a>
### 96. /policy/api/v1/infra/lb-virtual-servers/vmware-system-observability-controller-manager-metrics-service_9889_TCP_nus7f

**HTTP Methods:** GET, PATCH

**Explanation:**
NSX Policy API endpoint for resource management.

---


**Sample Response Body (GET, from logs):**
```json
{
  "enabled": true,
  "ip_address": "172.24.227.194",
  "ports": [
    "9889"
  ],
  "access_log_enabled": false,
  "lb_service_path": "/infra/lb-services/clusterip_f06fd228-8088-4439-a9e6-26c90a829c57_dlb",
  "pool_path": "/infra/lb-pools/vmware-system-observability-controller-manager-metrics-service_9889_TCP_nus7f",
  "application_profile_path": "/infra/lb-app-profiles/default-tcp-lb-app-profile",
  "log_significant_event_only": false,
  "resource_type": "LBVirtualServer",
  "id": "vmware-system-observability-controller-manager-metrics-service_9889_TCP_nus7f",
  "display_name": "vmware-system-observability-controller-manager-metrics-service_9889_TCP",
  "tags": [
    {
      "scope": "ncp/version",
      "tag": "1.2.0"
    },
    {
      "scope": "ncp/cluster",
      "tag": "f06fd228-8088-4439-a9e6-26c90a829c57"
    },
    {
      "scope": "ncp/project",
      "tag": "vmware-system-monitoring"
    },
    {
      "scope": "external_id",
      "tag": "31cc116f-3337-4404-bff3-fbf08275cde2"
    },
    {
      "scope": "ncp/service",
      "tag": "vmware-system-observability-controller-manager-metrics-service"
    },
    {
      "scope": "ncp/service_uid",
      "tag": "31cc116f-3337-4404-bff3-fbf08275cde2"
    },
    {
      "scope": "ncp/service_port",
      "tag": "9889"
    },
    {
      "scope": "ncp/service_port_protocol",
      "tag": "TCP"
    },
    {
      "scope": "ncp/created_for",
      "tag": "DLB"
    }
  ],
  "path": "/infra/lb-virtual-servers/vmware-system-observability-controller-manager-metrics-service_9889_TCP_nus7f",
  "relative_path": "vmware-system-observability-controller-manager-metrics-service_9889_TCP_nus7f",
  "parent_path": "/infra",
  "remote_path": "",
  "unique_id": "f7f0c5e3-2091-4a0f-b86e-ae697e664dfa",
  "realization_id": "f7f0c5e3-2091-4a0f-b86e-ae697e664dfa",
  "owner_id": "42495ba4-8c0b-49c9-b645-84cc39c2df30",
  "marked_for_delete": false,
  "overridden": false,
  "_system_owned": false,
  "_protection": "NOT_PROTECTED",
  "_create_time": 1760503457520,
  "_create_user": "wcp-cluster-user-f06fd228-8088-4439-a9e6-26c90a829c57-d34133d7-0fdf-4c9d-abcf-df83bd050a59",
  "_last_modified_time": 1760503623016,
  "_last_modified_user": "wcp-cluster-user-f06fd228-8088-4439-a9e6-26c90a829c57-d34133d7-0fdf-4c9d-abcf-df83bd050a59",
  "_revision": 1
}
```
<a id="97-policy-api-v1-infra-tier-0s-none-locale-services"></a>
### 97. /policy/api/v1/infra/tier-0s/None/locale-services

**HTTP Methods:** GET

**Explanation:**
Tier-0 gateway management. Provides connectivity to external networks and BGP peering.

---


**Sample Response Body (GET, from logs):**
```json
{
  "httpStatus": "BAD_REQUEST",
  "error_code": 500012,
  "module_name": "Policy",
  "error_message": "The path=[/infra/tier-0s/None] is invalid"
}
```
<a id="98-policy-api-v1-orgs-default-projects-project-quality"></a>
### 98. /policy/api/v1/orgs/default/projects/project-quality

**HTTP Methods:** GET

**Explanation:**
Project management within an organization. Projects group related VPCs and resources.

---

<a id="99-policy-api-v1-infra-shares-f06fd228-8088-4439-a9e6-26c90a829c57-vpc-share-resources-resources"></a>
### 99. /policy/api/v1/infra/shares/f06fd228-8088-4439-a9e6-26c90a829c57_vpc-share-resources/resources

**HTTP Methods:** GET

**Explanation:**
NSX Policy API endpoint for resource management.

---


**Sample Response Body (GET, from logs):**
```json
{
  "results": [
    {
      "resource_objects": [
        {
          "resource_path": "/infra/lb-app-profiles/ncp_f06fd228-8088-4439-a9e6-26c90a829c57_LBHttpProfile",
          "include_children": false
        }
      ],
      "with_permission": "READ_ONLY",
      "resource_type": "SharedResource",
      "id": "ncp_f06fd228-8088-4439-a9e6-26c90a829c57_LBHttpProfile",
      "display_name": "ncp_f06fd228-8088-4439-a9e6-26c90a829c57_LBHttpProfile",
      "tags": [
        {
          "scope": "ncp/version",
          "tag": "1.2.0"
        },
        {
          "scope": "ncp/cluster",
          "tag": "f06fd228-8088-4439-a9e6-26c90a829c57"
        },
        {
          "scope": "created_for",
          "tag": "ncp_f06fd228-8088-4439-a9e6-26c90a829c57_LBHttpProfile"
        }
      ],
      "path": "/infra/shares/f06fd228-8088-4439-a9e6-26c90a829c57_vpc-share-resources/resources/ncp_f06fd228-8088-4439-a9e6-26c90a829c57_LBHttpProfile",
      "relative_path": "ncp_f06fd228-8088-4439-a9e6-26c90a829c57_LBHttpProfile",
      "parent_path": "/infra/shares/f06fd228-8088-4439-a9e6-26c90a829c57_vpc-share-resources",
      "remote_path": "",
      "unique_id": "e1a6bf2a-8e34-4059-976d-44a300d0d37f",
      "realization_id": "e1a6bf2a-8e34-4059-976d-44a300d0d37f",
      "owner_id": "42495ba4-8c0b-49c9-b645-84cc39c2df30",
      "marked_for_delete": false,
      "overridden": false,
      "_system_owned": false,
      "_protection": "NOT_PROTECTED",
      "_create_time": 1760503432813,
      "_create_user": "wcp-cluster-user-f06fd228-8088-4439-a9e6-26c90a829c57-d34133d7-0fdf-4c9d-abcf-df83bd050a59",
      "_last_modified_time": 1760503432813,
      "_last_modified_user": "wcp-cluster-user-f06fd228-8088-4439-a9e6-26c90a829c57-d34133d7-0fdf-4c9d-abcf-df83bd050a59",
      "_revision": 0
    },
    {
      "resource_objects": [
        {
          "resource_path": "/infra/lb-persistence-profiles/f06fd228-8088-4439-a9e6-26c90a829c57_source_ip_layer4",
          "include_children": false
        }
      ],
      "with_permission": "READ_ONLY",
      "resource_type": "SharedResource",
      "id": "f06fd228-8088-4439-a9e6-26c90a829c57_source_ip_layer4",
      "display_name": "f06fd228-8088-4439-a9e6-26c90a829c57_source_ip_layer4",
      "tags": [
        {
          "scope": "ncp/version",
          "tag": "1.2.0"
        },
        {
          "scope": "ncp/cluster",
          "tag": "f06fd228-8088-4439-a9e6-26c90a829c57"
        },
        {
          "scope": "external_id",
          "tag": "2003591b-b187-556a-9c82-e308c09a273c"
        },
        {
          "scope": "ncp/created_for",
          "tag": "SLB"
        },
        {
          "scope": "created_for",
          "tag": "f06fd228-8088-4439-a9e6-26c90a829c57_source_ip_layer4"
        }
      ],
      "path": "/infra/shares/f06fd228-8088-4439-a9e6-26c90a829c57_vpc-share-resources/resources/f06fd228-8088-4439-a9e6-26c90a829c57_source_ip_layer4",
      "relative_path": "f06fd228-8088-4439-a9e6-26c90a829c57_s
  ...
}
```
<a id="100-policy-api-v1-infra-sites-default-enforcement-points-alb-endpoint"></a>
### 100. /policy/api/v1/infra/sites/default/enforcement-points/alb-endpoint

**HTTP Methods:** GET

**Explanation:**
Advanced Load Balancer (ALB) enforcement point. Integration point for NSX Advanced Load Balancer.

---


**Sample Response Body (GET, from logs):**
```json
{
  "httpStatus": "NOT_FOUND",
  "error_code": 600,
  "module_name": "common-services",
  "error_message": "The requested object : /infra/sites/default/enforcement-points/alb-endpoint could not be found. Object identifiers are case sensitive."
}
```
<a id="101-policy-api-v1-infra-domains-f06fd228-8088-4439-a9e6-26c90a829c57-groups-clusterip-f06fd228-8088-4439-a9e6-26c90a829c57-all-segments"></a>
### 101. /policy/api/v1/infra/domains/f06fd228-8088-4439-a9e6-26c90a829c57/groups/clusterip_f06fd228-8088-4439-a9e6-26c90a829c57_all_segments

**HTTP Methods:** GET, PATCH

**Explanation:**
Security group management in NSX domain. Groups define collections of workloads for policy application.

---


**Sample Response Body (GET, from logs):**
```json
{
  "expression": [
    {
      "expressions": [
        {
          "member_type": "Segment",
          "key": "Tag",
          "operator": "EQUALS",
          "scope_operator": "EQUALS",
          "value": "nsx-op/cluster|f06fd228-8088-4439-a9e6-26c90a829c57",
          "resource_type": "Condition",
          "id": "c196a67b-8c87-4f4e-ba95-9c0a99ec052f",
          "path": "/infra/domains/f06fd228-8088-4439-a9e6-26c90a829c57/groups/clusterip_f06fd228-8088-4439-a9e6-26c90a829c57_all_segments/condition-expressions/c196a67b-8c87-4f4e-ba95-9c0a99ec052f",
          "relative_path": "c196a67b-8c87-4f4e-ba95-9c0a99ec052f",
          "parent_path": "/infra/domains/f06fd228-8088-4439-a9e6-26c90a829c57/groups/clusterip_f06fd228-8088-4439-a9e6-26c90a829c57_all_segments",
          "remote_path": "",
          "marked_for_delete": false,
          "overridden": false,
          "_protection": "NOT_PROTECTED"
        },
        {
          "conjunction_operator": "AND",
          "resource_type": "ConjunctionOperator",
          "id": "7f8702a2-ad80-4dbc-b16b-4a2b5e7d9281",
          "path": "/infra/domains/f06fd228-8088-4439-a9e6-26c90a829c57/groups/clusterip_f06fd228-8088-4439-a9e6-26c90a829c57_all_segments/conjunction-expressions/7f8702a2-ad80-4dbc-b16b-4a2b5e7d9281",
          "relative_path": "7f8702a2-ad80-4dbc-b16b-4a2b5e7d9281",
          "parent_path": "/infra/domains/f06fd228-8088-4439-a9e6-26c90a829c57/groups/clusterip_f06fd228-8088-4439-a9e6-26c90a829c57_all_segments",
          "remote_path": "",
          "marked_for_delete": false,
          "overridden": false,
          "_protection": "NOT_PROTECTED"
        },
        {
          "member_type": "Segment",
          "key": "Tag",
          "operator": "EQUALS",
          "scope_operator": "EQUALS",
          "value": "nsx-op/namespace_uid|",
          "resource_type": "Condition",
          "id": "6fa670d4-f162-4650-a61d-7556799aa31f",
          "path": "/infra/domains/f06fd228-8088-4439-a9e6-26c90a829c57/groups/clusterip_f06fd228-8088-4439-a9e6-26c90a829c57_all_segments/condition-expressions/6fa670d4-f162-4650-a61d-7556799aa31f",
          "relative_path": "6fa670d4-f162-4650-a61d-7556799aa31f",
          "parent_path": "/infra/domains/f06fd228-8088-4439-a9e6-26c90a829c57/groups/clusterip_f06fd228-8088-4439-a9e6-26c90a829c57_all_segments",
          "remote_path": "",
          "marked_for_delete": false,
          "overridden": false,
          "_protection": "NOT_PROTECTED"
        }
      ],
      "resource_type": "NestedExpression",
      "id": "fdfbb6df-a3d9-4fe7-8b54-21ffd1c74760",
      "path": "/infra/domains/f06fd228-8088-4439-a9e6-26c90a829c57/groups/clusterip_f06fd228-8088-4439-a9e6-26c90a829c57_all_segments/nested-expressions/fdfbb6df-a3d9-4fe7-8b54-21ffd1c74760",
      "relative_path": "fdfbb6df-a3d9-4fe7-8b54-21ffd1c74760",
      "parent_path": "/infra/domains/f06fd228-8088-4439-a9e6-26c90a829c57/groups/clusterip_f06fd228-8088-4439-a9e6-26c90a829c57_all_segments",
      "remot
  ...
}
```
<a id="102-policy-api-v1-orgs-default-projects-project-quality-vpcs-testvpc-3658f2b5"></a>
### 102. /policy/api/v1/orgs/default/projects/project-quality/vpcs/testvpc-3658f2b5

**HTTP Methods:** GET

**Explanation:**
VPC (Virtual Private Cloud) management within a project. Manages isolated network environments for workloads.

---

<a id="103-policy-api-v1-orgs-default-projects-project-quality-vpcs-testvpc-461b1395"></a>
### 103. /policy/api/v1/orgs/default/projects/project-quality/vpcs/testvpc-461b1395

**HTTP Methods:** GET

**Explanation:**
VPC (Virtual Private Cloud) management within a project. Manages isolated network environments for workloads.

---

<a id="104-policy-api-v1-orgs-default-projects-project-quality-vpcs-testvpc-7ab2d8aa"></a>
### 104. /policy/api/v1/orgs/default/projects/project-quality/vpcs/testvpc-7ab2d8aa

**HTTP Methods:** GET

**Explanation:**
VPC (Virtual Private Cloud) management within a project. Manages isolated network environments for workloads.

---

<a id="105-policy-api-v1-orgs-default-projects-project-quality-vpcs-testvpc-d15ad1fd"></a>
### 105. /policy/api/v1/orgs/default/projects/project-quality/vpcs/testvpc-d15ad1fd

**HTTP Methods:** GET

**Explanation:**
VPC (Virtual Private Cloud) management within a project. Manages isolated network environments for workloads.

---

<a id="106-policy-api-v1-orgs-default-projects-project-quality-vpcs-testvpc-e65918e1"></a>
### 106. /policy/api/v1/orgs/default/projects/project-quality/vpcs/testvpc-e65918e1

**HTTP Methods:** GET

**Explanation:**
VPC (Virtual Private Cloud) management within a project. Manages isolated network environments for workloads.

---

<a id="107-policy-api-v1-orgs-default-projects-project-quality-vpcs-web-da775e6f-6o7ts"></a>
### 107. /policy/api/v1/orgs/default/projects/project-quality/vpcs/web-da775e6f_6o7ts

**HTTP Methods:** DELETE, GET

**Explanation:**
VPC (Virtual Private Cloud) management within a project. Manages isolated network environments for workloads.

---

<a id="108-policy-api-v1-orgs-default-projects-project-quality-vpcs-client-91c3f484-qzuxu"></a>
### 108. /policy/api/v1/orgs/default/projects/project-quality/vpcs/client-91c3f484_qzuxu

**HTTP Methods:** DELETE, GET

**Explanation:**
VPC (Virtual Private Cloud) management within a project. Manages isolated network environments for workloads.

---

<a id="109-policy-api-v1-orgs-default-projects-project-quality-vpcs-test-lb-50fedbb3-mv836"></a>
### 109. /policy/api/v1/orgs/default/projects/project-quality/vpcs/test-lb-50fedbb3_mv836

**HTTP Methods:** DELETE, GET

**Explanation:**
VPC (Virtual Private Cloud) management within a project. Manages isolated network environments for workloads.

---

<a id="110-policy-api-v1-orgs-default-projects-project-quality-vpcs-test-pod-1dd9a577-fu9t5"></a>
### 110. /policy/api/v1/orgs/default/projects/project-quality/vpcs/test-pod-1dd9a577_fu9t5

**HTTP Methods:** DELETE, GET

**Explanation:**
VPC (Virtual Private Cloud) management within a project. Manages isolated network environments for workloads.

---

<a id="111-policy-api-v1-infra-sites-default-enforcement-points-default-host-transport-nodes"></a>
### 111. /policy/api/v1/infra/sites/default/enforcement-points/default/host-transport-nodes

**HTTP Methods:** GET

**Explanation:**
Enforcement point management. Defines where NSX policies are applied (e.g., hosts, edges).

---

<a id="112-policy-api-v1-orgs-default-projects-project-quality-vpcs-target-ns-56446c91-6zdip"></a>
### 112. /policy/api/v1/orgs/default/projects/project-quality/vpcs/target-ns-56446c91_6zdip

**HTTP Methods:** DELETE, GET

**Explanation:**
VPC (Virtual Private Cloud) management within a project. Manages isolated network environments for workloads.

---

<a id="113-policy-api-v1-orgs-default-projects-project-quality-vpcs-update-ns-8eb115ed-baxdx"></a>
### 113. /policy/api/v1/orgs/default/projects/project-quality/vpcs/update-ns-8eb115ed_baxdx

**HTTP Methods:** DELETE, GET

**Explanation:**
VPC (Virtual Private Cloud) management within a project. Manages isolated network environments for workloads.

---

<a id="114-policy-api-v1-orgs-default-projects-project-quality-vpcs-subnet-e2e-1f11082b-56qvy"></a>
### 114. /policy/api/v1/orgs/default/projects/project-quality/vpcs/subnet-e2e-1f11082b_56qvy

**HTTP Methods:** DELETE, GET

**Explanation:**
VPC (Virtual Private Cloud) management within a project. Manages isolated network environments for workloads.

---

<a id="115-policy-api-v1-orgs-default-projects-project-quality-vpcs-staticroute-eb4f3a68-rxtge"></a>
### 115. /policy/api/v1/orgs/default/projects/project-quality/vpcs/staticroute-eb4f3a68_rxtge

**HTTP Methods:** DELETE, GET

**Explanation:**
VPC (Virtual Private Cloud) management within a project. Manages isolated network environments for workloads.

---

<a id="116-policy-api-v1-orgs-default-projects-project-quality-vpc-connectivity-profiles-no-nat"></a>
### 116. /policy/api/v1/orgs/default/projects/project-quality/vpc-connectivity-profiles/no-nat

**HTTP Methods:** GET

**Explanation:**
Project management within an organization. Projects group related VPCs and resources.

---

<a id="117-policy-api-v1-orgs-default-projects-project-quality-vpc-connectivity-profiles-default"></a>
### 117. /policy/api/v1/orgs/default/projects/project-quality/vpc-connectivity-profiles/default

**HTTP Methods:** GET

**Explanation:**
Project management within an organization. Projects group related VPCs and resources.

---

<a id="118-policy-api-v1-orgs-default-projects-project-quality-vpcs-customized-ns-99beca1e-yleom"></a>
### 118. /policy/api/v1/orgs/default/projects/project-quality/vpcs/customized-ns-99beca1e_yleom

**HTTP Methods:** DELETE, GET

**Explanation:**
VPC (Virtual Private Cloud) management within a project. Manages isolated network environments for workloads.

---

<a id="119-policy-api-v1-orgs-default-projects-project-quality-vpcs-test-pod-sync-e8b8a7ca-m404i"></a>
### 119. /policy/api/v1/orgs/default/projects/project-quality/vpcs/test-pod-sync-e8b8a7ca_m404i

**HTTP Methods:** DELETE, GET

**Explanation:**
VPC (Virtual Private Cloud) management within a project. Manages isolated network environments for workloads.

---

<a id="120-policy-api-v1-orgs-default-projects-project-quality-vpcs-shared-vpc-ns-0-3bc799ba-nwr40"></a>
### 120. /policy/api/v1/orgs/default/projects/project-quality/vpcs/shared-vpc-ns-0-3bc799ba_nwr40

**HTTP Methods:** DELETE, GET

**Explanation:**
VPC (Virtual Private Cloud) management within a project. Manages isolated network environments for workloads.

---

<a id="121-policy-api-v1-orgs-default-projects-project-quality-vpcs-test-netpol-sync-c2cf40cd-65gvf"></a>
### 121. /policy/api/v1/orgs/default/projects/project-quality/vpcs/test-netpol-sync-c2cf40cd_65gvf

**HTTP Methods:** DELETE, GET

**Explanation:**
VPC (Virtual Private Cloud) management within a project. Manages isolated network environments for workloads.

---

<a id="122-policy-api-v1-orgs-default-projects-project-quality-vpcs-test-ingress-sync-73e76bf1-rbp33"></a>
### 122. /policy/api/v1/orgs/default/projects/project-quality/vpcs/test-ingress-sync-73e76bf1_rbp33

**HTTP Methods:** DELETE, GET

**Explanation:**
VPC (Virtual Private Cloud) management within a project. Manages isolated network environments for workloads.

---

<a id="123-policy-api-v1-orgs-default-projects-project-quality-vpcs-test-service-sync-f1d17bff-5230b"></a>
### 123. /policy/api/v1/orgs/default/projects/project-quality/vpcs/test-service-sync-f1d17bff_5230b

**HTTP Methods:** DELETE, GET

**Explanation:**
VPC (Virtual Private Cloud) management within a project. Manages isolated network environments for workloads.

---

<a id="124-policy-api-v1-orgs-default-projects-project-quality-vpcs-networkinfo-default-efa7e691-1fkak"></a>
### 124. /policy/api/v1/orgs/default/projects/project-quality/vpcs/networkinfo-default-efa7e691_1fkak

**HTTP Methods:** DELETE, GET

**Explanation:**
VPC (Virtual Private Cloud) management within a project. Manages isolated network environments for workloads.

---

<a id="125-policy-api-v1-orgs-default-projects-project-quality-vpcs-test-namespace-sync-49fbe5bd-p9u70"></a>
### 125. /policy/api/v1/orgs/default/projects/project-quality/vpcs/test-namespace-sync-49fbe5bd_p9u70

**HTTP Methods:** DELETE, GET

**Explanation:**
VPC (Virtual Private Cloud) management within a project. Manages isolated network environments for workloads.

---

<a id="126-policy-api-v1-orgs-default-projects-project-quality-vpcs-precreated-target-ns-3c7c1821-v5ml5"></a>
### 126. /policy/api/v1/orgs/default/projects/project-quality/vpcs/precreated-target-ns-3c7c1821_v5ml5

**HTTP Methods:** DELETE, GET

**Explanation:**
VPC (Virtual Private Cloud) management within a project. Manages isolated network environments for workloads.

---

<a id="127-policy-api-v1-orgs-default-projects-project-quality-vpcs-test-create-vm-basic-f449d9bf-3ehn6"></a>
### 127. /policy/api/v1/orgs/default/projects/project-quality/vpcs/test-create-vm-basic-f449d9bf_3ehn6

**HTTP Methods:** DELETE, GET

**Explanation:**
VPC (Virtual Private Cloud) management within a project. Manages isolated network environments for workloads.

---

<a id="128-policy-api-v1-orgs-default-projects-project-quality-vpcs-precreated-subnet-ns1-a72a2a9d-8m6zu"></a>
### 128. /policy/api/v1/orgs/default/projects/project-quality/vpcs/precreated-subnet-ns1-a72a2a9d_8m6zu

**HTTP Methods:** DELETE, GET

**Explanation:**
VPC (Virtual Private Cloud) management within a project. Manages isolated network environments for workloads.

---

<a id="129-policy-api-v1-orgs-default-projects-project-quality-vpcs-precreated-subnet-ns2-42ff4c1a-tpi2w"></a>
### 129. /policy/api/v1/orgs/default/projects/project-quality/vpcs/precreated-subnet-ns2-42ff4c1a_tpi2w

**HTTP Methods:** DELETE, GET

**Explanation:**
VPC (Virtual Private Cloud) management within a project. Manages isolated network environments for workloads.

---

<a id="130-policy-api-v1-orgs-default-projects-project-quality-vpcs-test-security-policy-web-a2b779b4-f6e79"></a>
### 130. /policy/api/v1/orgs/default/projects/project-quality/vpcs/test-security-policy-web-a2b779b4_f6e79

**HTTP Methods:** DELETE, GET

**Explanation:**
VPC (Virtual Private Cloud) management within a project. Manages isolated network environments for workloads.

---

<a id="131-policy-api-v1-orgs-default-projects-project-quality-vpcs-test-ipaddress-allocation-40d5699d-2p2tu"></a>
### 131. /policy/api/v1/orgs/default/projects/project-quality/vpcs/test-ipaddress-allocation-40d5699d_2p2tu

**HTTP Methods:** DELETE, GET

**Explanation:**
VPC (Virtual Private Cloud) management within a project. Manages isolated network environments for workloads.

---

<a id="132-policy-api-v1-orgs-default-projects-project-quality-vpcs-test-security-policy-basic-72ecfa65-ib6li"></a>
### 132. /policy/api/v1/orgs/default/projects/project-quality/vpcs/test-security-policy-basic-72ecfa65_ib6li

**HTTP Methods:** DELETE, GET

**Explanation:**
VPC (Virtual Private Cloud) management within a project. Manages isolated network environments for workloads.

---

<a id="133-policy-api-v1-orgs-default-projects-project-quality-vpcs-test-security-policy-client-3a06d660-qiyvu"></a>
### 133. /policy/api/v1/orgs/default/projects/project-quality/vpcs/test-security-policy-client-3a06d660_qiyvu

**HTTP Methods:** DELETE, GET

**Explanation:**
VPC (Virtual Private Cloud) management within a project. Manages isolated network environments for workloads.

---

<a id="134-policy-api-v1-orgs-default-projects-project-quality-vpcs-vmware-system-supervisor-services-vpc-kzc7e"></a>
### 134. /policy/api/v1/orgs/default/projects/project-quality/vpcs/vmware-system-supervisor-services-vpc_kzc7e

**HTTP Methods:** GET

**Explanation:**
VPC (Virtual Private Cloud) management within a project. Manages isolated network environments for workloads.

---

<a id="135-policy-api-v1-orgs-default-projects-project-quality-vpcs-test-security-policy-add-delete-0e034260-aruoj"></a>
### 135. /policy/api/v1/orgs/default/projects/project-quality/vpcs/test-security-policy-add-delete-0e034260_aruoj

**HTTP Methods:** DELETE, GET

**Explanation:**
VPC (Virtual Private Cloud) management within a project. Manages isolated network environments for workloads.

---

<a id="136-policy-api-v1-orgs-default-projects-project-quality-vpcs-test-security-policy-match-expression-ff1dafa9-bgm74"></a>
### 136. /policy/api/v1/orgs/default/projects/project-quality/vpcs/test-security-policy-match-expression-ff1dafa9_bgm74

**HTTP Methods:** DELETE, GET

**Explanation:**
VPC (Virtual Private Cloud) management within a project. Manages isolated network environments for workloads.

---

<a id="137-policy-api-v1-orgs-default-projects-project-quality-vpcs-testvpc-3658f2b5-vpc-lbs"></a>
### 137. /policy/api/v1/orgs/default/projects/project-quality/vpcs/testvpc-3658f2b5/vpc-lbs

**HTTP Methods:** GET

**Explanation:**
VPC (Virtual Private Cloud) management within a project. Manages isolated network environments for workloads.

---

<a id="138-policy-api-v1-orgs-default-projects-project-quality-vpcs-testvpc-7ab2d8aa-vpc-lbs"></a>
### 138. /policy/api/v1/orgs/default/projects/project-quality/vpcs/testvpc-7ab2d8aa/vpc-lbs

**HTTP Methods:** GET

**Explanation:**
VPC (Virtual Private Cloud) management within a project. Manages isolated network environments for workloads.

---

<a id="139-policy-api-v1-orgs-default-projects-project-quality-vpcs-testvpc-d15ad1fd-vpc-lbs"></a>
### 139. /policy/api/v1/orgs/default/projects/project-quality/vpcs/testvpc-d15ad1fd/vpc-lbs

**HTTP Methods:** GET

**Explanation:**
VPC (Virtual Private Cloud) management within a project. Manages isolated network environments for workloads.

---

<a id="140-policy-api-v1-orgs-default-projects-project-quality-vpcs-testvpc-e65918e1-vpc-lbs"></a>
### 140. /policy/api/v1/orgs/default/projects/project-quality/vpcs/testvpc-e65918e1/vpc-lbs

**HTTP Methods:** GET

**Explanation:**
VPC (Virtual Private Cloud) management within a project. Manages isolated network environments for workloads.

---

<a id="141-policy-api-v1-orgs-default-projects-project-quality-vpcs-testvpc-3658f2b5-attachments"></a>
### 141. /policy/api/v1/orgs/default/projects/project-quality/vpcs/testvpc-3658f2b5/attachments

**HTTP Methods:** GET

**Explanation:**
VPC (Virtual Private Cloud) management within a project. Manages isolated network environments for workloads.

---

<a id="142-policy-api-v1-orgs-default-projects-project-quality-vpcs-testvpc-461b1395-attachments"></a>
### 142. /policy/api/v1/orgs/default/projects/project-quality/vpcs/testvpc-461b1395/attachments

**HTTP Methods:** GET

**Explanation:**
VPC (Virtual Private Cloud) management within a project. Manages isolated network environments for workloads.

---

<a id="143-policy-api-v1-orgs-default-projects-project-quality-vpcs-testvpc-7ab2d8aa-attachments"></a>
### 143. /policy/api/v1/orgs/default/projects/project-quality/vpcs/testvpc-7ab2d8aa/attachments

**HTTP Methods:** GET

**Explanation:**
VPC (Virtual Private Cloud) management within a project. Manages isolated network environments for workloads.

---

<a id="144-policy-api-v1-orgs-default-projects-project-quality-vpcs-testvpc-d15ad1fd-attachments"></a>
### 144. /policy/api/v1/orgs/default/projects/project-quality/vpcs/testvpc-d15ad1fd/attachments

**HTTP Methods:** GET

**Explanation:**
VPC (Virtual Private Cloud) management within a project. Manages isolated network environments for workloads.

---

<a id="145-policy-api-v1-orgs-default-projects-project-quality-vpcs-testvpc-e65918e1-attachments"></a>
### 145. /policy/api/v1/orgs/default/projects/project-quality/vpcs/testvpc-e65918e1/attachments

**HTTP Methods:** GET

**Explanation:**
VPC (Virtual Private Cloud) management within a project. Manages isolated network environments for workloads.

---

<a id="146-policy-api-v1-orgs-default-projects-project-quality-transit-gateways-default-attachments"></a>
### 146. /policy/api/v1/orgs/default/projects/project-quality/transit-gateways/default/attachments

**HTTP Methods:** GET

**Explanation:**
Project management within an organization. Projects group related VPCs and resources.

---

<a id="147-policy-api-v1-orgs-default-projects-project-quality-vpcs-vmware-system-supervisor-services-vpc-kzc7e-vpc-lbs"></a>
### 147. /policy/api/v1/orgs/default/projects/project-quality/vpcs/vmware-system-supervisor-services-vpc_kzc7e/vpc-lbs

**HTTP Methods:** GET

**Explanation:**
VPC (Virtual Private Cloud) management within a project. Manages isolated network environments for workloads.

---

<a id="148-policy-api-v1-orgs-default-projects-project-quality-vpcs-vmware-system-supervisor-services-vpc-kzc7e-attachments"></a>
### 148. /policy/api/v1/orgs/default/projects/project-quality/vpcs/vmware-system-supervisor-services-vpc_kzc7e/attachments

**HTTP Methods:** GET

**Explanation:**
VPC (Virtual Private Cloud) management within a project. Manages isolated network environments for workloads.

---

<a id="149-policy-api-v1-orgs-default-projects-project-quality-vpcs-testvpc-3658f2b5-vpc-lbs-default"></a>
### 149. /policy/api/v1/orgs/default/projects/project-quality/vpcs/testvpc-3658f2b5/vpc-lbs/default

**HTTP Methods:** GET

**Explanation:**
VPC (Virtual Private Cloud) management within a project. Manages isolated network environments for workloads.

---


**Sample Response Body (GET, from logs):**
```json
{
  "connectivity_path": "/orgs/default/projects/project-quality/vpcs/testvpc-3658f2b5",
  "enabled": true,
  "relax_scale_validation": true,
  "size": "SMALL",
  "error_log_level": "INFO",
  "resource_type": "LBService",
  "id": "default",
  "display_name": "default",
  "path": "/orgs/default/projects/project-quality/vpcs/testvpc-3658f2b5/vpc-lbs/default",
  "relative_path": "default",
  "parent_path": "/orgs/default/projects/project-quality/vpcs/testvpc-3658f2b5",
  "remote_path": "",
  "unique_id": "d6f43a84-942b-4baf-b67b-ab6df2131177",
  "realization_id": "d6f43a84-942b-4baf-b67b-ab6df2131177",
  "owner_id": "42495ba4-8c0b-49c9-b645-84cc39c2df30",
  "marked_for_delete": false,
  "overridden": false,
  "_system_owned": false,
  "_protection": "NOT_PROTECTED",
  "_create_time": 1760690624229,
  "_create_user": "wcp-cluster-user-f06fd228-8088-4439-a9e6-26c90a829c57-d34133d7-0fdf-4c9d-abcf-df83bd050a59",
  "_last_modified_time": 1760690624229,
  "_last_modified_user": "wcp-cluster-user-f06fd228-8088-4439-a9e6-26c90a829c57-d34133d7-0fdf-4c9d-abcf-df83bd050a59",
  "_revision": 0
}
```
<a id="150-policy-api-v1-orgs-default-projects-project-quality-vpcs-testvpc-d15ad1fd-vpc-lbs-default"></a>
### 150. /policy/api/v1/orgs/default/projects/project-quality/vpcs/testvpc-d15ad1fd/vpc-lbs/default

**HTTP Methods:** GET

**Explanation:**
VPC (Virtual Private Cloud) management within a project. Manages isolated network environments for workloads.

---


**Sample Response Body (GET, from logs):**
```json
{
  "connectivity_path": "/orgs/default/projects/project-quality/vpcs/testvpc-d15ad1fd",
  "enabled": true,
  "relax_scale_validation": true,
  "size": "SMALL",
  "error_log_level": "INFO",
  "resource_type": "LBService",
  "id": "default",
  "display_name": "default",
  "path": "/orgs/default/projects/project-quality/vpcs/testvpc-d15ad1fd/vpc-lbs/default",
  "relative_path": "default",
  "parent_path": "/orgs/default/projects/project-quality/vpcs/testvpc-d15ad1fd",
  "remote_path": "",
  "unique_id": "281e6a2e-9562-415f-b92a-93df415a0a2d",
  "realization_id": "281e6a2e-9562-415f-b92a-93df415a0a2d",
  "owner_id": "42495ba4-8c0b-49c9-b645-84cc39c2df30",
  "marked_for_delete": false,
  "overridden": false,
  "_system_owned": false,
  "_protection": "NOT_PROTECTED",
  "_create_time": 1760690740240,
  "_create_user": "wcp-cluster-user-f06fd228-8088-4439-a9e6-26c90a829c57-d34133d7-0fdf-4c9d-abcf-df83bd050a59",
  "_last_modified_time": 1760690740240,
  "_last_modified_user": "wcp-cluster-user-f06fd228-8088-4439-a9e6-26c90a829c57-d34133d7-0fdf-4c9d-abcf-df83bd050a59",
  "_revision": 0
}
```
<a id="151-policy-api-v1-orgs-default-projects-project-quality-vpcs-web-da775e6f-6o7ts-vpc-lbs-default"></a>
### 151. /policy/api/v1/orgs/default/projects/project-quality/vpcs/web-da775e6f_6o7ts/vpc-lbs/default

**HTTP Methods:** GET

**Explanation:**
VPC (Virtual Private Cloud) management within a project. Manages isolated network environments for workloads.

---


**Sample Response Body (GET, from logs):**
```json
{
  "connectivity_path": "/orgs/default/projects/project-quality/vpcs/web-da775e6f_6o7ts",
  "enabled": true,
  "relax_scale_validation": true,
  "size": "SMALL",
  "error_log_level": "INFO",
  "resource_type": "LBService",
  "id": "default",
  "display_name": "default",
  "tags": [
    {
      "scope": "nsx-op/cluster",
      "tag": "f06fd228-8088-4439-a9e6-26c90a829c57"
    },
    {
      "scope": "nsx-op/version",
      "tag": "1.0.0"
    },
    {
      "scope": "nsx-op/namespace",
      "tag": "web-da775e6f"
    },
    {
      "scope": "nsx-op/namespace_uid",
      "tag": "d114a0e0-d12c-41ac-9435-213fd199fa7b"
    },
    {
      "scope": "nsx-op/created_for",
      "tag": "SLB"
    }
  ],
  "path": "/orgs/default/projects/project-quality/vpcs/web-da775e6f_6o7ts/vpc-lbs/default",
  "relative_path": "default",
  "parent_path": "/orgs/default/projects/project-quality/vpcs/web-da775e6f_6o7ts",
  "remote_path": "",
  "unique_id": "fc9d975b-a133-41e7-8dc6-3f53250f24d1",
  "realization_id": "fc9d975b-a133-41e7-8dc6-3f53250f24d1",
  "owner_id": "42495ba4-8c0b-49c9-b645-84cc39c2df30",
  "marked_for_delete": false,
  "overridden": false,
  "_system_owned": false,
  "_protection": "NOT_PROTECTED",
  "_create_time": 1760690032587,
  "_create_user": "wcp-cluster-user-f06fd228-8088-4439-a9e6-26c90a829c57-d34133d7-0fdf-4c9d-abcf-df83bd050a59",
  "_last_modified_time": 1760690032587,
  "_last_modified_user": "wcp-cluster-user-f06fd228-8088-4439-a9e6-26c90a829c57-d34133d7-0fdf-4c9d-abcf-df83bd050a59",
  "_revision": 0
}
```
<a id="152-policy-api-v1-orgs-default-projects-project-quality-vpcs-client-91c3f484-qzuxu-vpc-lbs-default"></a>
### 152. /policy/api/v1/orgs/default/projects/project-quality/vpcs/client-91c3f484_qzuxu/vpc-lbs/default

**HTTP Methods:** GET

**Explanation:**
VPC (Virtual Private Cloud) management within a project. Manages isolated network environments for workloads.

---


**Sample Response Body (GET, from logs):**
```json
{
  "connectivity_path": "/orgs/default/projects/project-quality/vpcs/client-91c3f484_qzuxu",
  "enabled": true,
  "relax_scale_validation": true,
  "size": "SMALL",
  "error_log_level": "INFO",
  "resource_type": "LBService",
  "id": "default",
  "display_name": "default",
  "tags": [
    {
      "scope": "nsx-op/cluster",
      "tag": "f06fd228-8088-4439-a9e6-26c90a829c57"
    },
    {
      "scope": "nsx-op/version",
      "tag": "1.0.0"
    },
    {
      "scope": "nsx-op/namespace",
      "tag": "client-91c3f484"
    },
    {
      "scope": "nsx-op/namespace_uid",
      "tag": "e19581fd-dbb5-4b0c-b896-e4fcff60f0ed"
    },
    {
      "scope": "nsx-op/created_for",
      "tag": "SLB"
    }
  ],
  "path": "/orgs/default/projects/project-quality/vpcs/client-91c3f484_qzuxu/vpc-lbs/default",
  "relative_path": "default",
  "parent_path": "/orgs/default/projects/project-quality/vpcs/client-91c3f484_qzuxu",
  "remote_path": "",
  "unique_id": "623e9bdd-5c6c-4fbd-b1ef-6a7a61b5a35e",
  "realization_id": "623e9bdd-5c6c-4fbd-b1ef-6a7a61b5a35e",
  "owner_id": "42495ba4-8c0b-49c9-b645-84cc39c2df30",
  "marked_for_delete": false,
  "overridden": false,
  "_system_owned": false,
  "_protection": "NOT_PROTECTED",
  "_create_time": 1760690010077,
  "_create_user": "wcp-cluster-user-f06fd228-8088-4439-a9e6-26c90a829c57-d34133d7-0fdf-4c9d-abcf-df83bd050a59",
  "_last_modified_time": 1760690010077,
  "_last_modified_user": "wcp-cluster-user-f06fd228-8088-4439-a9e6-26c90a829c57-d34133d7-0fdf-4c9d-abcf-df83bd050a59",
  "_revision": 0
}
```
<a id="153-policy-api-v1-orgs-default-projects-project-quality-vpcs-test-lb-50fedbb3-mv836-vpc-lbs-default"></a>
### 153. /policy/api/v1/orgs/default/projects/project-quality/vpcs/test-lb-50fedbb3_mv836/vpc-lbs/default

**HTTP Methods:** GET

**Explanation:**
VPC (Virtual Private Cloud) management within a project. Manages isolated network environments for workloads.

---


**Sample Response Body (GET, from logs):**
```json
{
  "connectivity_path": "/orgs/default/projects/project-quality/vpcs/test-lb-50fedbb3_mv836",
  "enabled": true,
  "relax_scale_validation": true,
  "size": "SMALL",
  "error_log_level": "INFO",
  "resource_type": "LBService",
  "id": "default",
  "display_name": "default",
  "tags": [
    {
      "scope": "nsx-op/cluster",
      "tag": "f06fd228-8088-4439-a9e6-26c90a829c57"
    },
    {
      "scope": "nsx-op/version",
      "tag": "1.0.0"
    },
    {
      "scope": "nsx-op/namespace",
      "tag": "test-lb-50fedbb3"
    },
    {
      "scope": "nsx-op/namespace_uid",
      "tag": "2506fba2-2bca-42a9-9fb0-35aa09b1d33c"
    },
    {
      "scope": "nsx-op/created_for",
      "tag": "SLB"
    }
  ],
  "path": "/orgs/default/projects/project-quality/vpcs/test-lb-50fedbb3_mv836/vpc-lbs/default",
  "relative_path": "default",
  "parent_path": "/orgs/default/projects/project-quality/vpcs/test-lb-50fedbb3_mv836",
  "remote_path": "",
  "unique_id": "64616c44-c13d-4cee-8e55-7cb222d329ba",
  "realization_id": "64616c44-c13d-4cee-8e55-7cb222d329ba",
  "owner_id": "42495ba4-8c0b-49c9-b645-84cc39c2df30",
  "marked_for_delete": false,
  "overridden": false,
  "_system_owned": false,
  "_protection": "NOT_PROTECTED",
  "_create_time": 1760689160864,
  "_create_user": "wcp-cluster-user-f06fd228-8088-4439-a9e6-26c90a829c57-d34133d7-0fdf-4c9d-abcf-df83bd050a59",
  "_last_modified_time": 1760689160864,
  "_last_modified_user": "wcp-cluster-user-f06fd228-8088-4439-a9e6-26c90a829c57-d34133d7-0fdf-4c9d-abcf-df83bd050a59",
  "_revision": 0
}
```
<a id="154-policy-api-v1-orgs-default-projects-project-quality-vpcs-web-da775e6f-6o7ts-attachments-default"></a>
### 154. /policy/api/v1/orgs/default/projects/project-quality/vpcs/web-da775e6f_6o7ts/attachments/default

**HTTP Methods:** GET

**Explanation:**
VPC (Virtual Private Cloud) management within a project. Manages isolated network environments for workloads.

---

<a id="155-policy-api-v1-orgs-default-projects-project-quality-vpcs-test-pod-1dd9a577-fu9t5-vpc-lbs-default"></a>
### 155. /policy/api/v1/orgs/default/projects/project-quality/vpcs/test-pod-1dd9a577_fu9t5/vpc-lbs/default

**HTTP Methods:** GET

**Explanation:**
VPC (Virtual Private Cloud) management within a project. Manages isolated network environments for workloads.

---


**Sample Response Body (GET, from logs):**
```json
{
  "connectivity_path": "/orgs/default/projects/project-quality/vpcs/test-pod-1dd9a577_fu9t5",
  "enabled": true,
  "relax_scale_validation": true,
  "size": "SMALL",
  "error_log_level": "INFO",
  "resource_type": "LBService",
  "id": "default",
  "display_name": "default",
  "tags": [
    {
      "scope": "nsx-op/cluster",
      "tag": "f06fd228-8088-4439-a9e6-26c90a829c57"
    },
    {
      "scope": "nsx-op/version",
      "tag": "1.0.0"
    },
    {
      "scope": "nsx-op/namespace",
      "tag": "test-pod-1dd9a577"
    },
    {
      "scope": "nsx-op/namespace_uid",
      "tag": "6c0816d9-ed05-4f26-91d1-b87dae8e9c1b"
    },
    {
      "scope": "nsx-op/created_for",
      "tag": "SLB"
    }
  ],
  "path": "/orgs/default/projects/project-quality/vpcs/test-pod-1dd9a577_fu9t5/vpc-lbs/default",
  "relative_path": "default",
  "parent_path": "/orgs/default/projects/project-quality/vpcs/test-pod-1dd9a577_fu9t5",
  "remote_path": "",
  "unique_id": "deea50dd-8094-4cd5-8c82-00483100fb2b",
  "realization_id": "deea50dd-8094-4cd5-8c82-00483100fb2b",
  "owner_id": "42495ba4-8c0b-49c9-b645-84cc39c2df30",
  "marked_for_delete": false,
  "overridden": false,
  "_system_owned": false,
  "_protection": "NOT_PROTECTED",
  "_create_time": 1760689182732,
  "_create_user": "wcp-cluster-user-f06fd228-8088-4439-a9e6-26c90a829c57-d34133d7-0fdf-4c9d-abcf-df83bd050a59",
  "_last_modified_time": 1760689182732,
  "_last_modified_user": "wcp-cluster-user-f06fd228-8088-4439-a9e6-26c90a829c57-d34133d7-0fdf-4c9d-abcf-df83bd050a59",
  "_revision": 0
}
```
<a id="156-policy-api-v1-orgs-default-projects-project-quality-vpcs-target-ns-56446c91-6zdip-vpc-lbs-default"></a>
### 156. /policy/api/v1/orgs/default/projects/project-quality/vpcs/target-ns-56446c91_6zdip/vpc-lbs/default

**HTTP Methods:** GET

**Explanation:**
VPC (Virtual Private Cloud) management within a project. Manages isolated network environments for workloads.

---


**Sample Response Body (GET, from logs):**
```json
{
  "connectivity_path": "/orgs/default/projects/project-quality/vpcs/target-ns-56446c91_6zdip",
  "enabled": true,
  "relax_scale_validation": true,
  "size": "SMALL",
  "error_log_level": "INFO",
  "resource_type": "LBService",
  "id": "default",
  "display_name": "default",
  "tags": [
    {
      "scope": "nsx-op/cluster",
      "tag": "f06fd228-8088-4439-a9e6-26c90a829c57"
    },
    {
      "scope": "nsx-op/version",
      "tag": "1.0.0"
    },
    {
      "scope": "nsx-op/namespace",
      "tag": "target-ns-56446c91"
    },
    {
      "scope": "nsx-op/namespace_uid",
      "tag": "d8e6bcb8-3d9b-4288-862c-4a5ca005ade7"
    },
    {
      "scope": "nsx-op/created_for",
      "tag": "SLB"
    }
  ],
  "path": "/orgs/default/projects/project-quality/vpcs/target-ns-56446c91_6zdip/vpc-lbs/default",
  "relative_path": "default",
  "parent_path": "/orgs/default/projects/project-quality/vpcs/target-ns-56446c91_6zdip",
  "remote_path": "",
  "unique_id": "b076b195-e334-4b88-97f5-d9c87e146734",
  "realization_id": "b076b195-e334-4b88-97f5-d9c87e146734",
  "owner_id": "42495ba4-8c0b-49c9-b645-84cc39c2df30",
  "marked_for_delete": false,
  "overridden": false,
  "_system_owned": false,
  "_protection": "NOT_PROTECTED",
  "_create_time": 1760690186014,
  "_create_user": "wcp-cluster-user-f06fd228-8088-4439-a9e6-26c90a829c57-d34133d7-0fdf-4c9d-abcf-df83bd050a59",
  "_last_modified_time": 1760690186014,
  "_last_modified_user": "wcp-cluster-user-f06fd228-8088-4439-a9e6-26c90a829c57-d34133d7-0fdf-4c9d-abcf-df83bd050a59",
  "_revision": 0
}
```
<a id="157-policy-api-v1-orgs-default-projects-project-quality-vpcs-update-ns-8eb115ed-baxdx-vpc-lbs-default"></a>
### 157. /policy/api/v1/orgs/default/projects/project-quality/vpcs/update-ns-8eb115ed_baxdx/vpc-lbs/default

**HTTP Methods:** GET

**Explanation:**
VPC (Virtual Private Cloud) management within a project. Manages isolated network environments for workloads.

---


**Sample Response Body (GET, from logs):**
```json
{
  "connectivity_path": "/orgs/default/projects/project-quality/vpcs/update-ns-8eb115ed_baxdx",
  "enabled": true,
  "relax_scale_validation": true,
  "size": "SMALL",
  "error_log_level": "INFO",
  "resource_type": "LBService",
  "id": "default",
  "display_name": "default",
  "tags": [
    {
      "scope": "nsx-op/cluster",
      "tag": "f06fd228-8088-4439-a9e6-26c90a829c57"
    },
    {
      "scope": "nsx-op/version",
      "tag": "1.0.0"
    },
    {
      "scope": "nsx-op/namespace",
      "tag": "update-ns-8eb115ed"
    },
    {
      "scope": "nsx-op/namespace_uid",
      "tag": "48590efa-84b0-41cb-a18d-6135d77af577"
    },
    {
      "scope": "nsx-op/created_for",
      "tag": "SLB"
    }
  ],
  "path": "/orgs/default/projects/project-quality/vpcs/update-ns-8eb115ed_baxdx/vpc-lbs/default",
  "relative_path": "default",
  "parent_path": "/orgs/default/projects/project-quality/vpcs/update-ns-8eb115ed_baxdx",
  "remote_path": "",
  "unique_id": "202f8064-8aae-4f46-8b2a-af522ab02adf",
  "realization_id": "202f8064-8aae-4f46-8b2a-af522ab02adf",
  "owner_id": "42495ba4-8c0b-49c9-b645-84cc39c2df30",
  "marked_for_delete": false,
  "overridden": false,
  "_system_owned": false,
  "_protection": "NOT_PROTECTED",
  "_create_time": 1760689440389,
  "_create_user": "wcp-cluster-user-f06fd228-8088-4439-a9e6-26c90a829c57-d34133d7-0fdf-4c9d-abcf-df83bd050a59",
  "_last_modified_time": 1760689440389,
  "_last_modified_user": "wcp-cluster-user-f06fd228-8088-4439-a9e6-26c90a829c57-d34133d7-0fdf-4c9d-abcf-df83bd050a59",
  "_revision": 0
}
```
<a id="158-policy-api-v1-orgs-default-projects-project-quality-vpcs-client-91c3f484-qzuxu-attachments-default"></a>
### 158. /policy/api/v1/orgs/default/projects/project-quality/vpcs/client-91c3f484_qzuxu/attachments/default

**HTTP Methods:** GET

**Explanation:**
VPC (Virtual Private Cloud) management within a project. Manages isolated network environments for workloads.

---

<a id="159-policy-api-v1-orgs-default-projects-project-quality-vpcs-subnet-e2e-1f11082b-56qvy-vpc-lbs-default"></a>
### 159. /policy/api/v1/orgs/default/projects/project-quality/vpcs/subnet-e2e-1f11082b_56qvy/vpc-lbs/default

**HTTP Methods:** GET

**Explanation:**
VPC (Virtual Private Cloud) management within a project. Manages isolated network environments for workloads.

---


**Sample Response Body (GET, from logs):**
```json
{
  "connectivity_path": "/orgs/default/projects/project-quality/vpcs/subnet-e2e-1f11082b_56qvy",
  "enabled": true,
  "relax_scale_validation": true,
  "size": "SMALL",
  "error_log_level": "INFO",
  "resource_type": "LBService",
  "id": "default",
  "display_name": "default",
  "tags": [
    {
      "scope": "nsx-op/cluster",
      "tag": "f06fd228-8088-4439-a9e6-26c90a829c57"
    },
    {
      "scope": "nsx-op/version",
      "tag": "1.0.0"
    },
    {
      "scope": "nsx-op/namespace",
      "tag": "subnet-e2e-1f11082b"
    },
    {
      "scope": "nsx-op/namespace_uid",
      "tag": "f629b82e-5ea2-4298-b1cf-3bafcea373fa"
    },
    {
      "scope": "nsx-op/created_for",
      "tag": "SLB"
    }
  ],
  "path": "/orgs/default/projects/project-quality/vpcs/subnet-e2e-1f11082b_56qvy/vpc-lbs/default",
  "relative_path": "default",
  "parent_path": "/orgs/default/projects/project-quality/vpcs/subnet-e2e-1f11082b_56qvy",
  "remote_path": "",
  "unique_id": "c325390c-3fc0-4721-bf55-a2c453d6ae9c",
  "realization_id": "c325390c-3fc0-4721-bf55-a2c453d6ae9c",
  "owner_id": "42495ba4-8c0b-49c9-b645-84cc39c2df30",
  "marked_for_delete": false,
  "overridden": false,
  "_system_owned": false,
  "_protection": "NOT_PROTECTED",
  "_create_time": 1760690185606,
  "_create_user": "wcp-cluster-user-f06fd228-8088-4439-a9e6-26c90a829c57-d34133d7-0fdf-4c9d-abcf-df83bd050a59",
  "_last_modified_time": 1760690185606,
  "_last_modified_user": "wcp-cluster-user-f06fd228-8088-4439-a9e6-26c90a829c57-d34133d7-0fdf-4c9d-abcf-df83bd050a59",
  "_revision": 0
}
```
<a id="160-policy-api-v1-orgs-default-projects-project-quality-vpcs-staticroute-eb4f3a68-rxtge-vpc-lbs-default"></a>
### 160. /policy/api/v1/orgs/default/projects/project-quality/vpcs/staticroute-eb4f3a68_rxtge/vpc-lbs/default

**HTTP Methods:** GET

**Explanation:**
VPC (Virtual Private Cloud) management within a project. Manages isolated network environments for workloads.

---


**Sample Response Body (GET, from logs):**
```json
{
  "connectivity_path": "/orgs/default/projects/project-quality/vpcs/staticroute-eb4f3a68_rxtge",
  "enabled": true,
  "relax_scale_validation": true,
  "size": "SMALL",
  "error_log_level": "INFO",
  "resource_type": "LBService",
  "id": "default",
  "display_name": "default",
  "tags": [
    {
      "scope": "nsx-op/cluster",
      "tag": "f06fd228-8088-4439-a9e6-26c90a829c57"
    },
    {
      "scope": "nsx-op/version",
      "tag": "1.0.0"
    },
    {
      "scope": "nsx-op/namespace",
      "tag": "staticroute-eb4f3a68"
    },
    {
      "scope": "nsx-op/namespace_uid",
      "tag": "d379ee54-20b6-4fa3-b6f9-413d233226b6"
    },
    {
      "scope": "nsx-op/created_for",
      "tag": "SLB"
    }
  ],
  "path": "/orgs/default/projects/project-quality/vpcs/staticroute-eb4f3a68_rxtge/vpc-lbs/default",
  "relative_path": "default",
  "parent_path": "/orgs/default/projects/project-quality/vpcs/staticroute-eb4f3a68_rxtge",
  "remote_path": "",
  "unique_id": "cbb1d26a-f070-4639-9635-5c31503925a7",
  "realization_id": "cbb1d26a-f070-4639-9635-5c31503925a7",
  "owner_id": "42495ba4-8c0b-49c9-b645-84cc39c2df30",
  "marked_for_delete": false,
  "overridden": false,
  "_system_owned": false,
  "_protection": "NOT_PROTECTED",
  "_create_time": 1760690167666,
  "_create_user": "wcp-cluster-user-f06fd228-8088-4439-a9e6-26c90a829c57-d34133d7-0fdf-4c9d-abcf-df83bd050a59",
  "_last_modified_time": 1760690167666,
  "_last_modified_user": "wcp-cluster-user-f06fd228-8088-4439-a9e6-26c90a829c57-d34133d7-0fdf-4c9d-abcf-df83bd050a59",
  "_revision": 0
}
```
<a id="161-policy-api-v1-orgs-default-projects-project-quality-vpcs-test-lb-50fedbb3-mv836-attachments-default"></a>
### 161. /policy/api/v1/orgs/default/projects/project-quality/vpcs/test-lb-50fedbb3_mv836/attachments/default

**HTTP Methods:** GET

**Explanation:**
VPC (Virtual Private Cloud) management within a project. Manages isolated network environments for workloads.

---

<a id="162-policy-api-v1-orgs-default-projects-project-quality-vpcs-test-pod-1dd9a577-fu9t5-attachments-default"></a>
### 162. /policy/api/v1/orgs/default/projects/project-quality/vpcs/test-pod-1dd9a577_fu9t5/attachments/default

**HTTP Methods:** GET

**Explanation:**
VPC (Virtual Private Cloud) management within a project. Manages isolated network environments for workloads.

---

<a id="163-policy-api-v1-orgs-default-projects-project-quality-vpcs-customized-ns-99beca1e-yleom-vpc-lbs-default"></a>
### 163. /policy/api/v1/orgs/default/projects/project-quality/vpcs/customized-ns-99beca1e_yleom/vpc-lbs/default

**HTTP Methods:** GET

**Explanation:**
VPC (Virtual Private Cloud) management within a project. Manages isolated network environments for workloads.

---


**Sample Response Body (GET, from logs):**
```json
{
  "connectivity_path": "/orgs/default/projects/project-quality/vpcs/customized-ns-99beca1e_yleom",
  "enabled": true,
  "relax_scale_validation": true,
  "size": "SMALL",
  "error_log_level": "INFO",
  "resource_type": "LBService",
  "id": "default",
  "display_name": "default",
  "tags": [
    {
      "scope": "nsx-op/cluster",
      "tag": "f06fd228-8088-4439-a9e6-26c90a829c57"
    },
    {
      "scope": "nsx-op/version",
      "tag": "1.0.0"
    },
    {
      "scope": "nsx-op/namespace",
      "tag": "customized-ns-99beca1e"
    },
    {
      "scope": "nsx-op/namespace_uid",
      "tag": "69a298b8-9cbb-4cb1-bfc2-ea1cb20a9901"
    },
    {
      "scope": "nsx-op/created_for",
      "tag": "SLB"
    }
  ],
  "path": "/orgs/default/projects/project-quality/vpcs/customized-ns-99beca1e_yleom/vpc-lbs/default",
  "relative_path": "default",
  "parent_path": "/orgs/default/projects/project-quality/vpcs/customized-ns-99beca1e_yleom",
  "remote_path": "",
  "unique_id": "a06007d0-5609-4d99-9371-32518c7d4abd",
  "realization_id": "a06007d0-5609-4d99-9371-32518c7d4abd",
  "owner_id": "42495ba4-8c0b-49c9-b645-84cc39c2df30",
  "marked_for_delete": false,
  "overridden": false,
  "_system_owned": false,
  "_protection": "NOT_PROTECTED",
  "_create_time": 1760689397967,
  "_create_user": "wcp-cluster-user-f06fd228-8088-4439-a9e6-26c90a829c57-d34133d7-0fdf-4c9d-abcf-df83bd050a59",
  "_last_modified_time": 1760689397967,
  "_last_modified_user": "wcp-cluster-user-f06fd228-8088-4439-a9e6-26c90a829c57-d34133d7-0fdf-4c9d-abcf-df83bd050a59",
  "_revision": 0
}
```
<a id="164-policy-api-v1-orgs-default-projects-project-quality-vpcs-target-ns-56446c91-6zdip-attachments-default"></a>
### 164. /policy/api/v1/orgs/default/projects/project-quality/vpcs/target-ns-56446c91_6zdip/attachments/default

**HTTP Methods:** GET

**Explanation:**
VPC (Virtual Private Cloud) management within a project. Manages isolated network environments for workloads.

---

<a id="165-policy-api-v1-orgs-default-projects-project-quality-vpcs-test-pod-sync-e8b8a7ca-m404i-vpc-lbs-default"></a>
### 165. /policy/api/v1/orgs/default/projects/project-quality/vpcs/test-pod-sync-e8b8a7ca_m404i/vpc-lbs/default

**HTTP Methods:** GET

**Explanation:**
VPC (Virtual Private Cloud) management within a project. Manages isolated network environments for workloads.

---


**Sample Response Body (GET, from logs):**
```json
{
  "connectivity_path": "/orgs/default/projects/project-quality/vpcs/test-pod-sync-e8b8a7ca_m404i",
  "enabled": true,
  "relax_scale_validation": true,
  "size": "SMALL",
  "error_log_level": "INFO",
  "resource_type": "LBService",
  "id": "default",
  "display_name": "default",
  "tags": [
    {
      "scope": "nsx-op/cluster",
      "tag": "f06fd228-8088-4439-a9e6-26c90a829c57"
    },
    {
      "scope": "nsx-op/version",
      "tag": "1.0.0"
    },
    {
      "scope": "nsx-op/namespace",
      "tag": "test-pod-sync-e8b8a7ca"
    },
    {
      "scope": "nsx-op/namespace_uid",
      "tag": "df28714f-bbd0-4ac5-bfaa-13716c242ac0"
    },
    {
      "scope": "nsx-op/created_for",
      "tag": "SLB"
    }
  ],
  "path": "/orgs/default/projects/project-quality/vpcs/test-pod-sync-e8b8a7ca_m404i/vpc-lbs/default",
  "relative_path": "default",
  "parent_path": "/orgs/default/projects/project-quality/vpcs/test-pod-sync-e8b8a7ca_m404i",
  "remote_path": "",
  "unique_id": "6670eea2-84dc-45fc-852b-259cfffb578c",
  "realization_id": "6670eea2-84dc-45fc-852b-259cfffb578c",
  "owner_id": "42495ba4-8c0b-49c9-b645-84cc39c2df30",
  "marked_for_delete": false,
  "overridden": false,
  "_system_owned": false,
  "_protection": "NOT_PROTECTED",
  "_create_time": 1760688875898,
  "_create_user": "wcp-cluster-user-f06fd228-8088-4439-a9e6-26c90a829c57-d34133d7-0fdf-4c9d-abcf-df83bd050a59",
  "_last_modified_time": 1760688875898,
  "_last_modified_user": "wcp-cluster-user-f06fd228-8088-4439-a9e6-26c90a829c57-d34133d7-0fdf-4c9d-abcf-df83bd050a59",
  "_revision": 0
}
```
<a id="166-policy-api-v1-orgs-default-projects-project-quality-vpcs-update-ns-8eb115ed-baxdx-attachments-default"></a>
### 166. /policy/api/v1/orgs/default/projects/project-quality/vpcs/update-ns-8eb115ed_baxdx/attachments/default

**HTTP Methods:** GET

**Explanation:**
VPC (Virtual Private Cloud) management within a project. Manages isolated network environments for workloads.

---

<a id="167-policy-api-v1-orgs-default-projects-project-quality-vpcs-subnet-e2e-1f11082b-56qvy-attachments-default"></a>
### 167. /policy/api/v1/orgs/default/projects/project-quality/vpcs/subnet-e2e-1f11082b_56qvy/attachments/default

**HTTP Methods:** GET

**Explanation:**
VPC (Virtual Private Cloud) management within a project. Manages isolated network environments for workloads.

---

<a id="168-policy-api-v1-orgs-default-projects-project-quality-vpcs-testvpc-3658f2b5-ip-address-allocations-j7n9u"></a>
### 168. /policy/api/v1/orgs/default/projects/project-quality/vpcs/testvpc-3658f2b5/ip-address-allocations/j7n9u

**HTTP Methods:** DELETE, GET, PATCH

**Explanation:**
VPC (Virtual Private Cloud) management within a project. Manages isolated network environments for workloads.

---


**Sample Response Body (GET, from logs):**
```json
{
  "ip_address_type": "IPV4",
  "ip_address_block_visibility": "EXTERNAL",
  "allocation_ip": "192.168.0.8",
  "allocation_ips": "192.168.0.8",
  "resource_type": "VpcIpAddressAllocation",
  "id": "j7n9u",
  "display_name": "j7n9u",
  "tags": [
    {
      "scope": "ncp/version",
      "tag": "1.2.0"
    },
    {
      "scope": "ncp/cluster",
      "tag": "f06fd228-8088-4439-a9e6-26c90a829c57"
    },
    {
      "scope": "ncp/service_uid",
      "tag": "64af7175-c755-4315-9cf7-28c21bd6fc0a"
    },
    {
      "scope": "ncp/created_for",
      "tag": "l4_service"
    }
  ],
  "path": "/orgs/default/projects/project-quality/vpcs/testvpc-3658f2b5/ip-address-allocations/j7n9u",
  "relative_path": "j7n9u",
  "parent_path": "/orgs/default/projects/project-quality/vpcs/testvpc-3658f2b5",
  "remote_path": "",
  "unique_id": "c59cd10c-ca64-4ab8-97d9-5219edb1a98b",
  "realization_id": "c59cd10c-ca64-4ab8-97d9-5219edb1a98b",
  "owner_id": "42495ba4-8c0b-49c9-b645-84cc39c2df30",
  "marked_for_delete": false,
  "overridden": false,
  "_system_owned": false,
  "_protection": "NOT_PROTECTED",
  "_create_time": 1760690632462,
  "_create_user": "wcp-cluster-user-f06fd228-8088-4439-a9e6-26c90a829c57-d34133d7-0fdf-4c9d-abcf-df83bd050a59",
  "_last_modified_time": 1760690632462,
  "_last_modified_user": "wcp-cluster-user-f06fd228-8088-4439-a9e6-26c90a829c57-d34133d7-0fdf-4c9d-abcf-df83bd050a59",
  "_revision": 0
}
```
<a id="169-policy-api-v1-orgs-default-projects-project-quality-vpcs-shared-vpc-ns-0-3bc799ba-nwr40-vpc-lbs-default"></a>
### 169. /policy/api/v1/orgs/default/projects/project-quality/vpcs/shared-vpc-ns-0-3bc799ba_nwr40/vpc-lbs/default

**HTTP Methods:** GET

**Explanation:**
VPC (Virtual Private Cloud) management within a project. Manages isolated network environments for workloads.

---


**Sample Response Body (GET, from logs):**
```json
{
  "connectivity_path": "/orgs/default/projects/project-quality/vpcs/shared-vpc-ns-0-3bc799ba_nwr40",
  "enabled": true,
  "relax_scale_validation": true,
  "size": "SMALL",
  "error_log_level": "INFO",
  "resource_type": "LBService",
  "id": "default",
  "display_name": "default",
  "tags": [
    {
      "scope": "nsx-op/cluster",
      "tag": "f06fd228-8088-4439-a9e6-26c90a829c57"
    },
    {
      "scope": "nsx-op/version",
      "tag": "1.0.0"
    },
    {
      "scope": "nsx-op/namespace",
      "tag": "shared-vpc-ns-0-3bc799ba"
    },
    {
      "scope": "nsx-op/namespace_uid",
      "tag": "a8e6a49f-ab6b-4bc5-85d0-85b2a87434c6"
    },
    {
      "scope": "nsx-op/created_for",
      "tag": "SLB"
    }
  ],
  "path": "/orgs/default/projects/project-quality/vpcs/shared-vpc-ns-0-3bc799ba_nwr40/vpc-lbs/default",
  "relative_path": "default",
  "parent_path": "/orgs/default/projects/project-quality/vpcs/shared-vpc-ns-0-3bc799ba_nwr40",
  "remote_path": "",
  "unique_id": "fd649d15-fb1b-437e-b910-9e9464cf8736",
  "realization_id": "fd649d15-fb1b-437e-b910-9e9464cf8736",
  "owner_id": "42495ba4-8c0b-49c9-b645-84cc39c2df30",
  "marked_for_delete": false,
  "overridden": false,
  "_system_owned": false,
  "_protection": "NOT_PROTECTED",
  "_create_time": 1760689419139,
  "_create_user": "wcp-cluster-user-f06fd228-8088-4439-a9e6-26c90a829c57-d34133d7-0fdf-4c9d-abcf-df83bd050a59",
  "_last_modified_time": 1760689419139,
  "_last_modified_user": "wcp-cluster-user-f06fd228-8088-4439-a9e6-26c90a829c57-d34133d7-0fdf-4c9d-abcf-df83bd050a59",
  "_revision": 0
}
```
<a id="170-policy-api-v1-orgs-default-projects-project-quality-vpcs-staticroute-eb4f3a68-rxtge-attachments-default"></a>
### 170. /policy/api/v1/orgs/default/projects/project-quality/vpcs/staticroute-eb4f3a68_rxtge/attachments/default

**HTTP Methods:** GET

**Explanation:**
VPC (Virtual Private Cloud) management within a project. Manages isolated network environments for workloads.

---

<a id="171-policy-api-v1-orgs-default-projects-project-quality-vpcs-test-netpol-sync-c2cf40cd-65gvf-vpc-lbs-default"></a>
### 171. /policy/api/v1/orgs/default/projects/project-quality/vpcs/test-netpol-sync-c2cf40cd_65gvf/vpc-lbs/default

**HTTP Methods:** GET

**Explanation:**
VPC (Virtual Private Cloud) management within a project. Manages isolated network environments for workloads.

---


**Sample Response Body (GET, from logs):**
```json
{
  "connectivity_path": "/orgs/default/projects/project-quality/vpcs/test-netpol-sync-c2cf40cd_65gvf",
  "enabled": true,
  "relax_scale_validation": true,
  "size": "SMALL",
  "error_log_level": "INFO",
  "resource_type": "LBService",
  "id": "default",
  "display_name": "default",
  "tags": [
    {
      "scope": "nsx-op/cluster",
      "tag": "f06fd228-8088-4439-a9e6-26c90a829c57"
    },
    {
      "scope": "nsx-op/version",
      "tag": "1.0.0"
    },
    {
      "scope": "nsx-op/namespace",
      "tag": "test-netpol-sync-c2cf40cd"
    },
    {
      "scope": "nsx-op/namespace_uid",
      "tag": "035266c9-c300-485d-8f18-c9c250782d50"
    },
    {
      "scope": "nsx-op/created_for",
      "tag": "SLB"
    }
  ],
  "path": "/orgs/default/projects/project-quality/vpcs/test-netpol-sync-c2cf40cd_65gvf/vpc-lbs/default",
  "relative_path": "default",
  "parent_path": "/orgs/default/projects/project-quality/vpcs/test-netpol-sync-c2cf40cd_65gvf",
  "remote_path": "",
  "unique_id": "75a95159-c704-40fc-a444-1a6f07bb49de",
  "realization_id": "75a95159-c704-40fc-a444-1a6f07bb49de",
  "owner_id": "42495ba4-8c0b-49c9-b645-84cc39c2df30",
  "marked_for_delete": false,
  "overridden": false,
  "_system_owned": false,
  "_protection": "NOT_PROTECTED",
  "_create_time": 1760688993831,
  "_create_user": "wcp-cluster-user-f06fd228-8088-4439-a9e6-26c90a829c57-d34133d7-0fdf-4c9d-abcf-df83bd050a59",
  "_last_modified_time": 1760688993831,
  "_last_modified_user": "wcp-cluster-user-f06fd228-8088-4439-a9e6-26c90a829c57-d34133d7-0fdf-4c9d-abcf-df83bd050a59",
  "_revision": 0
}
```
<a id="172-policy-api-v1-orgs-default-projects-project-quality-vpcs-customized-ns-99beca1e-yleom-attachments-default"></a>
### 172. /policy/api/v1/orgs/default/projects/project-quality/vpcs/customized-ns-99beca1e_yleom/attachments/default

**HTTP Methods:** GET

**Explanation:**
VPC (Virtual Private Cloud) management within a project. Manages isolated network environments for workloads.

---

<a id="173-policy-api-v1-orgs-default-projects-project-quality-vpcs-test-ingress-sync-73e76bf1-rbp33-vpc-lbs-default"></a>
### 173. /policy/api/v1/orgs/default/projects/project-quality/vpcs/test-ingress-sync-73e76bf1_rbp33/vpc-lbs/default

**HTTP Methods:** GET

**Explanation:**
VPC (Virtual Private Cloud) management within a project. Manages isolated network environments for workloads.

---


**Sample Response Body (GET, from logs):**
```json
{
  "connectivity_path": "/orgs/default/projects/project-quality/vpcs/test-ingress-sync-73e76bf1_rbp33",
  "enabled": true,
  "relax_scale_validation": true,
  "size": "SMALL",
  "error_log_level": "INFO",
  "resource_type": "LBService",
  "id": "default",
  "display_name": "default",
  "tags": [
    {
      "scope": "nsx-op/cluster",
      "tag": "f06fd228-8088-4439-a9e6-26c90a829c57"
    },
    {
      "scope": "nsx-op/version",
      "tag": "1.0.0"
    },
    {
      "scope": "nsx-op/namespace",
      "tag": "test-ingress-sync-73e76bf1"
    },
    {
      "scope": "nsx-op/namespace_uid",
      "tag": "d9efcae1-642a-478c-9bb0-c5af498af932"
    },
    {
      "scope": "nsx-op/created_for",
      "tag": "SLB"
    }
  ],
  "path": "/orgs/default/projects/project-quality/vpcs/test-ingress-sync-73e76bf1_rbp33/vpc-lbs/default",
  "relative_path": "default",
  "parent_path": "/orgs/default/projects/project-quality/vpcs/test-ingress-sync-73e76bf1_rbp33",
  "remote_path": "",
  "unique_id": "86d3c5af-ad31-4ccd-8044-a3fbe8ed4dab",
  "realization_id": "86d3c5af-ad31-4ccd-8044-a3fbe8ed4dab",
  "owner_id": "42495ba4-8c0b-49c9-b645-84cc39c2df30",
  "marked_for_delete": false,
  "overridden": false,
  "_system_owned": false,
  "_protection": "NOT_PROTECTED",
  "_create_time": 1760689039186,
  "_create_user": "wcp-cluster-user-f06fd228-8088-4439-a9e6-26c90a829c57-d34133d7-0fdf-4c9d-abcf-df83bd050a59",
  "_last_modified_time": 1760689039186,
  "_last_modified_user": "wcp-cluster-user-f06fd228-8088-4439-a9e6-26c90a829c57-d34133d7-0fdf-4c9d-abcf-df83bd050a59",
  "_revision": 0
}
```
<a id="174-policy-api-v1-orgs-default-projects-project-quality-vpcs-test-pod-sync-e8b8a7ca-m404i-attachments-default"></a>
### 174. /policy/api/v1/orgs/default/projects/project-quality/vpcs/test-pod-sync-e8b8a7ca_m404i/attachments/default

**HTTP Methods:** GET

**Explanation:**
VPC (Virtual Private Cloud) management within a project. Manages isolated network environments for workloads.

---

<a id="175-policy-api-v1-orgs-default-projects-project-quality-vpcs-test-service-sync-f1d17bff-5230b-vpc-lbs-default"></a>
### 175. /policy/api/v1/orgs/default/projects/project-quality/vpcs/test-service-sync-f1d17bff_5230b/vpc-lbs/default

**HTTP Methods:** GET

**Explanation:**
VPC (Virtual Private Cloud) management within a project. Manages isolated network environments for workloads.

---


**Sample Response Body (GET, from logs):**
```json
{
  "connectivity_path": "/orgs/default/projects/project-quality/vpcs/test-service-sync-f1d17bff_5230b",
  "enabled": true,
  "relax_scale_validation": true,
  "size": "SMALL",
  "error_log_level": "INFO",
  "resource_type": "LBService",
  "id": "default",
  "display_name": "default",
  "tags": [
    {
      "scope": "nsx-op/cluster",
      "tag": "f06fd228-8088-4439-a9e6-26c90a829c57"
    },
    {
      "scope": "nsx-op/version",
      "tag": "1.0.0"
    },
    {
      "scope": "nsx-op/namespace",
      "tag": "test-service-sync-f1d17bff"
    },
    {
      "scope": "nsx-op/namespace_uid",
      "tag": "ac12dc97-c401-4639-b832-c2c7e909b276"
    },
    {
      "scope": "nsx-op/created_for",
      "tag": "SLB"
    }
  ],
  "path": "/orgs/default/projects/project-quality/vpcs/test-service-sync-f1d17bff_5230b/vpc-lbs/default",
  "relative_path": "default",
  "parent_path": "/orgs/default/projects/project-quality/vpcs/test-service-sync-f1d17bff_5230b",
  "remote_path": "",
  "unique_id": "a0456e8b-26d9-44e5-aeed-e340e177c2c9",
  "realization_id": "a0456e8b-26d9-44e5-aeed-e340e177c2c9",
  "owner_id": "42495ba4-8c0b-49c9-b645-84cc39c2df30",
  "marked_for_delete": false,
  "overridden": false,
  "_system_owned": false,
  "_protection": "NOT_PROTECTED",
  "_create_time": 1760688948130,
  "_create_user": "wcp-cluster-user-f06fd228-8088-4439-a9e6-26c90a829c57-d34133d7-0fdf-4c9d-abcf-df83bd050a59",
  "_last_modified_time": 1760688948130,
  "_last_modified_user": "wcp-cluster-user-f06fd228-8088-4439-a9e6-26c90a829c57-d34133d7-0fdf-4c9d-abcf-df83bd050a59",
  "_revision": 0
}
```
<a id="176-policy-api-v1-orgs-default-projects-project-quality-vpcs-networkinfo-default-efa7e691-1fkak-vpc-lbs-default"></a>
### 176. /policy/api/v1/orgs/default/projects/project-quality/vpcs/networkinfo-default-efa7e691_1fkak/vpc-lbs/default

**HTTP Methods:** GET

**Explanation:**
VPC (Virtual Private Cloud) management within a project. Manages isolated network environments for workloads.

---


**Sample Response Body (GET, from logs):**
```json
{
  "connectivity_path": "/orgs/default/projects/project-quality/vpcs/networkinfo-default-efa7e691_1fkak",
  "enabled": true,
  "relax_scale_validation": true,
  "size": "SMALL",
  "error_log_level": "INFO",
  "resource_type": "LBService",
  "id": "default",
  "display_name": "default",
  "tags": [
    {
      "scope": "nsx-op/cluster",
      "tag": "f06fd228-8088-4439-a9e6-26c90a829c57"
    },
    {
      "scope": "nsx-op/version",
      "tag": "1.0.0"
    },
    {
      "scope": "nsx-op/namespace",
      "tag": "networkinfo-default-efa7e691"
    },
    {
      "scope": "nsx-op/namespace_uid",
      "tag": "c8142be3-459f-4678-9a2d-04b6f67a194c"
    },
    {
      "scope": "nsx-op/created_for",
      "tag": "SLB"
    }
  ],
  "path": "/orgs/default/projects/project-quality/vpcs/networkinfo-default-efa7e691_1fkak/vpc-lbs/default",
  "relative_path": "default",
  "parent_path": "/orgs/default/projects/project-quality/vpcs/networkinfo-default-efa7e691_1fkak",
  "remote_path": "",
  "unique_id": "ca199584-b8a8-41dd-9e51-a0cdfb468f58",
  "realization_id": "ca199584-b8a8-41dd-9e51-a0cdfb468f58",
  "owner_id": "42495ba4-8c0b-49c9-b645-84cc39c2df30",
  "marked_for_delete": false,
  "overridden": false,
  "_system_owned": false,
  "_protection": "NOT_PROTECTED",
  "_create_time": 1760689407083,
  "_create_user": "wcp-cluster-user-f06fd228-8088-4439-a9e6-26c90a829c57-d34133d7-0fdf-4c9d-abcf-df83bd050a59",
  "_last_modified_time": 1760689407083,
  "_last_modified_user": "wcp-cluster-user-f06fd228-8088-4439-a9e6-26c90a829c57-d34133d7-0fdf-4c9d-abcf-df83bd050a59",
  "_revision": 0
}
```
<a id="177-policy-api-v1-orgs-default-projects-project-quality-vpcs-shared-vpc-ns-0-3bc799ba-nwr40-attachments-default"></a>
### 177. /policy/api/v1/orgs/default/projects/project-quality/vpcs/shared-vpc-ns-0-3bc799ba_nwr40/attachments/default

**HTTP Methods:** GET

**Explanation:**
VPC (Virtual Private Cloud) management within a project. Manages isolated network environments for workloads.

---

<a id="178-policy-api-v1-orgs-default-projects-project-quality-vpcs-test-namespace-sync-49fbe5bd-p9u70-vpc-lbs-default"></a>
### 178. /policy/api/v1/orgs/default/projects/project-quality/vpcs/test-namespace-sync-49fbe5bd_p9u70/vpc-lbs/default

**HTTP Methods:** GET

**Explanation:**
VPC (Virtual Private Cloud) management within a project. Manages isolated network environments for workloads.

---


**Sample Response Body (GET, from logs):**
```json
{
  "connectivity_path": "/orgs/default/projects/project-quality/vpcs/test-namespace-sync-49fbe5bd_p9u70",
  "enabled": true,
  "relax_scale_validation": true,
  "size": "SMALL",
  "error_log_level": "INFO",
  "resource_type": "LBService",
  "id": "default",
  "display_name": "default",
  "tags": [
    {
      "scope": "nsx-op/cluster",
      "tag": "f06fd228-8088-4439-a9e6-26c90a829c57"
    },
    {
      "scope": "nsx-op/version",
      "tag": "1.0.0"
    },
    {
      "scope": "nsx-op/namespace",
      "tag": "test-namespace-sync-49fbe5bd"
    },
    {
      "scope": "nsx-op/namespace_uid",
      "tag": "d52c0046-42a3-46fe-aa2d-58dbd58785fa"
    },
    {
      "scope": "nsx-op/created_for",
      "tag": "SLB"
    }
  ],
  "path": "/orgs/default/projects/project-quality/vpcs/test-namespace-sync-49fbe5bd_p9u70/vpc-lbs/default",
  "relative_path": "default",
  "parent_path": "/orgs/default/projects/project-quality/vpcs/test-namespace-sync-49fbe5bd_p9u70",
  "remote_path": "",
  "unique_id": "df8396ef-765d-4f7d-9c21-1467e9073714",
  "realization_id": "df8396ef-765d-4f7d-9c21-1467e9073714",
  "owner_id": "42495ba4-8c0b-49c9-b645-84cc39c2df30",
  "marked_for_delete": false,
  "overridden": false,
  "_system_owned": false,
  "_protection": "NOT_PROTECTED",
  "_create_time": 1760688845860,
  "_create_user": "wcp-cluster-user-f06fd228-8088-4439-a9e6-26c90a829c57-d34133d7-0fdf-4c9d-abcf-df83bd050a59",
  "_last_modified_time": 1760688845860,
  "_last_modified_user": "wcp-cluster-user-f06fd228-8088-4439-a9e6-26c90a829c57-d34133d7-0fdf-4c9d-abcf-df83bd050a59",
  "_revision": 0
}
```
<a id="179-policy-api-v1-orgs-default-projects-project-quality-vpcs-kube-system-fyr99-subnets-vm-default-637336f2-fyr99"></a>
### 179. /policy/api/v1/orgs/default/projects/project-quality/vpcs/kube-system_fyr99/subnets/vm-default-637336f2_fyr99

**HTTP Methods:** GET, PATCH

**Explanation:**
VPC subnet management within a project. Defines IP address ranges and network segments for VPC workloads.

**Request Body (PATCH):**
```json
{
  "_create_time": 1760503453832,
  "_create_user": "wcp-cluster-user-f06fd228-8088-4439-a9e6-26c90a829c57-d34133d7-0fdf-4c9d-abcf-df83bd050a59",
  "_last_modified_time": 1760686254207,
  "_last_modified_user": "wcp-cluster-user-f06fd228-8088-4439-a9e6-26c90a829c57-d34133d7-0fdf-4c9d-abcf-df83bd050a59",
  "_protection": "NOT_PROTECTED",
  "_revision": 12,
  "_system_owned": false,
  "access_mode": "Private",
  "advanced_config": {
    "connectivity_state": "CONNECTED",
    "enable_vlan_extension": false,
    "gateway_addresses": [
      "172.26.0.1/28"
    ],
    "static_ip_allocation": {
      "enabled": true
    }
  },
  "display_name": "vm-default-637336f2_fyr99",
  "id": "vm-default-637336f2_fyr99",
  "ip_addresses": [
    "172.26.0.0/28"
  ],
  "ip_blocks": [
    "/orgs/default/projects/project-quality/infra/ip-blocks/kube-system_fyr99-172_26_0_0_16"
  ],
  "ipv4_subnet_size": 16,
  "marked_for_delete": false,
  "overridden": false,
  "owner_id": "42495ba4-8c0b-49c9-b645-84cc39c2df30",
  "parent_path": "/orgs/default/projects/project-quality/vpcs/kube-system_fyr99",
  "path": "/orgs/default/projects/project-quality/vpcs/kube-system_fyr99/subnets/vm-default-637336f2_fyr99",
  "realization_id": "b79fb62e-54fb-49b6-a5d3-6f3377078b23",
  "relative_path": "vm-default-637336f2_fyr99",
  "remote_path": "",
  "resource_type": "VpcSubnet",
  "subnet_dhcp_config": {
    "mode": "DHCP_DEACTIVATED"
  },
  "tags": [
    {
      "scope": "nsx-op/cluster",
      "tag": "f06fd228-8088-4439-a9e6-26c90a829c57"
    },
    {
      "scope": "nsx-op/version",
      "tag": "1.0.0"
    },
    {
      "scope": "nsx-op/subnetset_name",
      "tag": "vm-default"
    },
    {
      "scope": "nsx-op/subnetset_uid",
      "tag": "797e7995-2a40-4b39-8547-7f3074debf7a"
    },
    {
      "scope": "nsx/managed-by",
      "tag": "nsx-op"
    },
    {
      "scope": "nsx-op/vm_namespace_uid",
      "tag": "1a552110-0336-484e-b9f3-c968449b5013"
    },
    {
      "scope": "nsx-op/vm_namespace",
      "tag": "kube-system"
    },
    {
      "scope": "iaas.vmware.com/contains-service-images",
      "tag": ""
    },
    {
      "scope": "kubernetes.io/metadata.name",
      "tag": "kube-system"
    },
    {
      "scope": "pod-security.kubernetes.io/enforce",
      "tag": "privileged"
    }
  ],
  "unique_id": "b79fb62e-54fb-49b6-a5d3-6f3377078b23"
}
```

---

<a id="180-policy-api-v1-orgs-default-projects-project-quality-vpcs-precreated-target-ns-3c7c1821-v5ml5-vpc-lbs-default"></a>
### 180. /policy/api/v1/orgs/default/projects/project-quality/vpcs/precreated-target-ns-3c7c1821_v5ml5/vpc-lbs/default

**HTTP Methods:** GET

**Explanation:**
VPC (Virtual Private Cloud) management within a project. Manages isolated network environments for workloads.

---


**Sample Response Body (GET, from logs):**
```json
{
  "connectivity_path": "/orgs/default/projects/project-quality/vpcs/precreated-target-ns-3c7c1821_v5ml5",
  "enabled": true,
  "relax_scale_validation": true,
  "size": "SMALL",
  "error_log_level": "INFO",
  "resource_type": "LBService",
  "id": "default",
  "display_name": "default",
  "tags": [
    {
      "scope": "nsx-op/cluster",
      "tag": "f06fd228-8088-4439-a9e6-26c90a829c57"
    },
    {
      "scope": "nsx-op/version",
      "tag": "1.0.0"
    },
    {
      "scope": "nsx-op/namespace",
      "tag": "precreated-target-ns-3c7c1821"
    },
    {
      "scope": "nsx-op/namespace_uid",
      "tag": "a4d76189-c002-4514-9616-5265c71b7b8b"
    },
    {
      "scope": "nsx-op/created_for",
      "tag": "SLB"
    }
  ],
  "path": "/orgs/default/projects/project-quality/vpcs/precreated-target-ns-3c7c1821_v5ml5/vpc-lbs/default",
  "relative_path": "default",
  "parent_path": "/orgs/default/projects/project-quality/vpcs/precreated-target-ns-3c7c1821_v5ml5",
  "remote_path": "",
  "unique_id": "8fd6d783-9984-4970-85e2-ef229a8a5686",
  "realization_id": "8fd6d783-9984-4970-85e2-ef229a8a5686",
  "owner_id": "42495ba4-8c0b-49c9-b645-84cc39c2df30",
  "marked_for_delete": false,
  "overridden": false,
  "_system_owned": false,
  "_protection": "NOT_PROTECTED",
  "_create_time": 1760690350571,
  "_create_user": "wcp-cluster-user-f06fd228-8088-4439-a9e6-26c90a829c57-d34133d7-0fdf-4c9d-abcf-df83bd050a59",
  "_last_modified_time": 1760690350571,
  "_last_modified_user": "wcp-cluster-user-f06fd228-8088-4439-a9e6-26c90a829c57-d34133d7-0fdf-4c9d-abcf-df83bd050a59",
  "_revision": 0
}
```
<a id="181-policy-api-v1-orgs-default-projects-project-quality-vpcs-subnet-e2e-1f11082b-56qvy-subnets-subnet-cidr-56qvy"></a>
### 181. /policy/api/v1/orgs/default/projects/project-quality/vpcs/subnet-e2e-1f11082b_56qvy/subnets/subnet-cidr_56qvy

**HTTP Methods:** DELETE, GET, PATCH

**Explanation:**
VPC subnet management within a project. Defines IP address ranges and network segments for VPC workloads.

**Request Body (PATCH):**
```json
{
  "access_mode": "Private",
  "advanced_config": {
    "connectivity_state": "CONNECTED",
    "static_ip_allocation": {
      "enabled": true
    }
  },
  "display_name": "subnet-cidr_56qvy",
  "id": "subnet-cidr_56qvy",
  "ipv4_subnet_size": 16,
  "subnet_dhcp_config": {
    "mode": "DHCP_DEACTIVATED"
  },
  "tags": [
    {
      "scope": "nsx-op/cluster",
      "tag": "f06fd228-8088-4439-a9e6-26c90a829c57"
    },
    {
      "scope": "nsx-op/version",
      "tag": "1.0.0"
    },
    {
      "scope": "nsx-op/subnet_name",
      "tag": "subnet-cidr"
    },
    {
      "scope": "nsx-op/subnet_uid",
      "tag": "94fee768-fc4b-4d60-b77d-31bfe29e65c5"
    },
    {
      "scope": "nsx/managed-by",
      "tag": "nsx-op"
    },
    {
      "scope": "nsx-op/vm_namespace_uid",
      "tag": "f629b82e-5ea2-4298-b1cf-3bafcea373fa"
    },
    {
      "scope": "nsx-op/vm_namespace",
      "tag": "subnet-e2e-1f11082b"
    },
    {
      "scope": "kubernetes.io/metadata.name",
      "tag": "subnet-e2e-1f11082b"
    }
  ]
}
```

---

<a id="182-policy-api-v1-orgs-default-projects-project-quality-vpcs-subnet-e2e-1f11082b-56qvy-subnets-subnet-dhcp-56qvy"></a>
### 182. /policy/api/v1/orgs/default/projects/project-quality/vpcs/subnet-e2e-1f11082b_56qvy/subnets/subnet-dhcp_56qvy

**HTTP Methods:** DELETE, GET, PATCH

**Explanation:**
VPC subnet management within a project. Defines IP address ranges and network segments for VPC workloads.

**Request Body (PATCH):**
```json
{
  "access_mode": "Private",
  "advanced_config": {
    "connectivity_state": "CONNECTED",
    "static_ip_allocation": {
      "enabled": false
    }
  },
  "display_name": "subnet-dhcp_56qvy",
  "id": "subnet-dhcp_56qvy",
  "ipv4_subnet_size": 32,
  "subnet_dhcp_config": {
    "mode": "DHCP_SERVER"
  },
  "tags": [
    {
      "scope": "nsx-op/cluster",
      "tag": "f06fd228-8088-4439-a9e6-26c90a829c57"
    },
    {
      "scope": "nsx-op/version",
      "tag": "1.0.0"
    },
    {
      "scope": "nsx-op/subnet_name",
      "tag": "subnet-dhcp"
    },
    {
      "scope": "nsx-op/subnet_uid",
      "tag": "ad224e98-8ba0-4397-b3e6-424a100ff601"
    },
    {
      "scope": "nsx/managed-by",
      "tag": "nsx-op"
    },
    {
      "scope": "nsx-op/vm_namespace_uid",
      "tag": "f629b82e-5ea2-4298-b1cf-3bafcea373fa"
    },
    {
      "scope": "nsx-op/vm_namespace",
      "tag": "subnet-e2e-1f11082b"
    },
    {
      "scope": "kubernetes.io/metadata.name",
      "tag": "subnet-e2e-1f11082b"
    }
  ]
}
```

---

<a id="183-policy-api-v1-orgs-default-projects-project-quality-vpcs-test-create-vm-basic-f449d9bf-3ehn6-vpc-lbs-default"></a>
### 183. /policy/api/v1/orgs/default/projects/project-quality/vpcs/test-create-vm-basic-f449d9bf_3ehn6/vpc-lbs/default

**HTTP Methods:** GET

**Explanation:**
VPC (Virtual Private Cloud) management within a project. Manages isolated network environments for workloads.

---


**Sample Response Body (GET, from logs):**
```json
{
  "connectivity_path": "/orgs/default/projects/project-quality/vpcs/test-create-vm-basic-f449d9bf_3ehn6",
  "enabled": true,
  "relax_scale_validation": true,
  "size": "SMALL",
  "error_log_level": "INFO",
  "resource_type": "LBService",
  "id": "default",
  "display_name": "default",
  "tags": [
    {
      "scope": "nsx-op/cluster",
      "tag": "f06fd228-8088-4439-a9e6-26c90a829c57"
    },
    {
      "scope": "nsx-op/version",
      "tag": "1.0.0"
    },
    {
      "scope": "nsx-op/namespace",
      "tag": "test-create-vm-basic-f449d9bf"
    },
    {
      "scope": "nsx-op/namespace_uid",
      "tag": "1d6f2e6e-f228-4ddc-87b3-b99608fd4766"
    },
    {
      "scope": "nsx-op/created_for",
      "tag": "SLB"
    }
  ],
  "path": "/orgs/default/projects/project-quality/vpcs/test-create-vm-basic-f449d9bf_3ehn6/vpc-lbs/default",
  "relative_path": "default",
  "parent_path": "/orgs/default/projects/project-quality/vpcs/test-create-vm-basic-f449d9bf_3ehn6",
  "remote_path": "",
  "unique_id": "c0d31d85-9af0-41cf-9382-8b00d4a1ec56",
  "realization_id": "c0d31d85-9af0-41cf-9382-8b00d4a1ec56",
  "owner_id": "42495ba4-8c0b-49c9-b645-84cc39c2df30",
  "marked_for_delete": false,
  "overridden": false,
  "_system_owned": false,
  "_protection": "NOT_PROTECTED",
  "_create_time": 1760690449217,
  "_create_user": "wcp-cluster-user-f06fd228-8088-4439-a9e6-26c90a829c57-d34133d7-0fdf-4c9d-abcf-df83bd050a59",
  "_last_modified_time": 1760690449217,
  "_last_modified_user": "wcp-cluster-user-f06fd228-8088-4439-a9e6-26c90a829c57-d34133d7-0fdf-4c9d-abcf-df83bd050a59",
  "_revision": 0
}
```
<a id="184-policy-api-v1-orgs-default-projects-project-quality-vpcs-test-lb-50fedbb3-mv836-ip-address-allocations-39r0c"></a>
### 184. /policy/api/v1/orgs/default/projects/project-quality/vpcs/test-lb-50fedbb3_mv836/ip-address-allocations/39r0c

**HTTP Methods:** DELETE, GET, PATCH

**Explanation:**
VPC (Virtual Private Cloud) management within a project. Manages isolated network environments for workloads.

---


**Sample Response Body (GET, from logs):**
```json
{
  "ip_address_type": "IPV4",
  "ip_address_block_visibility": "EXTERNAL",
  "allocation_ip": "192.168.0.9",
  "allocation_ips": "192.168.0.9",
  "resource_type": "VpcIpAddressAllocation",
  "id": "39r0c",
  "display_name": "39r0c",
  "tags": [
    {
      "scope": "ncp/version",
      "tag": "1.2.0"
    },
    {
      "scope": "ncp/cluster",
      "tag": "f06fd228-8088-4439-a9e6-26c90a829c57"
    },
    {
      "scope": "ncp/service_uid",
      "tag": "f8572ed6-448c-4830-8e1d-5c00326ab97f"
    },
    {
      "scope": "ncp/created_for",
      "tag": "l4_service"
    }
  ],
  "path": "/orgs/default/projects/project-quality/vpcs/test-lb-50fedbb3_mv836/ip-address-allocations/39r0c",
  "relative_path": "39r0c",
  "parent_path": "/orgs/default/projects/project-quality/vpcs/test-lb-50fedbb3_mv836",
  "remote_path": "",
  "unique_id": "a8d33590-096c-423e-a013-f7a949f6f5e5",
  "realization_id": "a8d33590-096c-423e-a013-f7a949f6f5e5",
  "owner_id": "42495ba4-8c0b-49c9-b645-84cc39c2df30",
  "marked_for_delete": false,
  "overridden": false,
  "_system_owned": false,
  "_protection": "NOT_PROTECTED",
  "_create_time": 1760689212275,
  "_create_user": "wcp-cluster-user-f06fd228-8088-4439-a9e6-26c90a829c57-d34133d7-0fdf-4c9d-abcf-df83bd050a59",
  "_last_modified_time": 1760689212275,
  "_last_modified_user": "wcp-cluster-user-f06fd228-8088-4439-a9e6-26c90a829c57-d34133d7-0fdf-4c9d-abcf-df83bd050a59",
  "_revision": 0
}
```
<a id="185-policy-api-v1-orgs-default-projects-project-quality-vpcs-test-lb-50fedbb3-mv836-ip-address-allocations-cnml1"></a>
### 185. /policy/api/v1/orgs/default/projects/project-quality/vpcs/test-lb-50fedbb3_mv836/ip-address-allocations/cnml1

**HTTP Methods:** DELETE, GET, PATCH

**Explanation:**
VPC (Virtual Private Cloud) management within a project. Manages isolated network environments for workloads.

---


**Sample Response Body (GET, from logs):**
```json
{
  "ip_address_type": "IPV4",
  "ip_address_block_visibility": "EXTERNAL",
  "allocation_ip": "192.168.0.12",
  "allocation_ips": "192.168.0.12",
  "resource_type": "VpcIpAddressAllocation",
  "id": "cnml1",
  "display_name": "cnml1",
  "tags": [
    {
      "scope": "ncp/version",
      "tag": "1.2.0"
    },
    {
      "scope": "ncp/cluster",
      "tag": "f06fd228-8088-4439-a9e6-26c90a829c57"
    },
    {
      "scope": "ncp/service_uid",
      "tag": "75a666bb-cb7a-45dd-a6a6-6d0f0e7d685e"
    },
    {
      "scope": "ncp/created_for",
      "tag": "l4_service"
    }
  ],
  "path": "/orgs/default/projects/project-quality/vpcs/test-lb-50fedbb3_mv836/ip-address-allocations/cnml1",
  "relative_path": "cnml1",
  "parent_path": "/orgs/default/projects/project-quality/vpcs/test-lb-50fedbb3_mv836",
  "remote_path": "",
  "unique_id": "ebb1e486-e931-426a-a56b-33c6754b7f8a",
  "realization_id": "ebb1e486-e931-426a-a56b-33c6754b7f8a",
  "owner_id": "42495ba4-8c0b-49c9-b645-84cc39c2df30",
  "marked_for_delete": false,
  "overridden": false,
  "_system_owned": false,
  "_protection": "NOT_PROTECTED",
  "_create_time": 1760689287138,
  "_create_user": "wcp-cluster-user-f06fd228-8088-4439-a9e6-26c90a829c57-d34133d7-0fdf-4c9d-abcf-df83bd050a59",
  "_last_modified_time": 1760689287138,
  "_last_modified_user": "wcp-cluster-user-f06fd228-8088-4439-a9e6-26c90a829c57-d34133d7-0fdf-4c9d-abcf-df83bd050a59",
  "_revision": 0
}
```
<a id="186-policy-api-v1-orgs-default-projects-project-quality-vpcs-test-lb-50fedbb3-mv836-ip-address-allocations-i3q14"></a>
### 186. /policy/api/v1/orgs/default/projects/project-quality/vpcs/test-lb-50fedbb3_mv836/ip-address-allocations/i3q14

**HTTP Methods:** DELETE, GET, PATCH

**Explanation:**
VPC (Virtual Private Cloud) management within a project. Manages isolated network environments for workloads.

---


**Sample Response Body (GET, from logs):**
```json
{
  "ip_address_type": "IPV4",
  "ip_address_block_visibility": "EXTERNAL",
  "allocation_ip": "192.168.0.10",
  "allocation_ips": "192.168.0.10",
  "resource_type": "VpcIpAddressAllocation",
  "id": "i3q14",
  "display_name": "i3q14",
  "tags": [
    {
      "scope": "ncp/version",
      "tag": "1.2.0"
    },
    {
      "scope": "ncp/cluster",
      "tag": "f06fd228-8088-4439-a9e6-26c90a829c57"
    },
    {
      "scope": "ncp/service_uid",
      "tag": "413462da-ad49-4afb-b755-88770ab32637"
    },
    {
      "scope": "ncp/created_for",
      "tag": "l4_service"
    }
  ],
  "path": "/orgs/default/projects/project-quality/vpcs/test-lb-50fedbb3_mv836/ip-address-allocations/i3q14",
  "relative_path": "i3q14",
  "parent_path": "/orgs/default/projects/project-quality/vpcs/test-lb-50fedbb3_mv836",
  "remote_path": "",
  "unique_id": "03ab976a-6168-4c7f-b0d2-f0b133f21c50",
  "realization_id": "03ab976a-6168-4c7f-b0d2-f0b133f21c50",
  "owner_id": "42495ba4-8c0b-49c9-b645-84cc39c2df30",
  "marked_for_delete": false,
  "overridden": false,
  "_system_owned": false,
  "_protection": "NOT_PROTECTED",
  "_create_time": 1760689221275,
  "_create_user": "wcp-cluster-user-f06fd228-8088-4439-a9e6-26c90a829c57-d34133d7-0fdf-4c9d-abcf-df83bd050a59",
  "_last_modified_time": 1760689221275,
  "_last_modified_user": "wcp-cluster-user-f06fd228-8088-4439-a9e6-26c90a829c57-d34133d7-0fdf-4c9d-abcf-df83bd050a59",
  "_revision": 0
}
```
<a id="187-policy-api-v1-orgs-default-projects-project-quality-vpcs-test-lb-50fedbb3-mv836-ip-address-allocations-o2zx3"></a>
### 187. /policy/api/v1/orgs/default/projects/project-quality/vpcs/test-lb-50fedbb3_mv836/ip-address-allocations/o2zx3

**HTTP Methods:** DELETE, GET, PATCH

**Explanation:**
VPC (Virtual Private Cloud) management within a project. Manages isolated network environments for workloads.

---


**Sample Response Body (GET, from logs):**
```json
{
  "ip_address_type": "IPV4",
  "ip_address_block_visibility": "EXTERNAL",
  "allocation_ip": "192.168.0.11",
  "allocation_ips": "192.168.0.11",
  "resource_type": "VpcIpAddressAllocation",
  "id": "o2zx3",
  "display_name": "o2zx3",
  "tags": [
    {
      "scope": "ncp/version",
      "tag": "1.2.0"
    },
    {
      "scope": "ncp/cluster",
      "tag": "f06fd228-8088-4439-a9e6-26c90a829c57"
    },
    {
      "scope": "ncp/project",
      "tag": "test-lb-50fedbb3"
    },
    {
      "scope": "ncp/project_uid",
      "tag": "2506fba2-2bca-42a9-9fb0-35aa09b1d33c"
    },
    {
      "scope": "ncp/created_for",
      "tag": "l7_per_namespace"
    }
  ],
  "path": "/orgs/default/projects/project-quality/vpcs/test-lb-50fedbb3_mv836/ip-address-allocations/o2zx3",
  "relative_path": "o2zx3",
  "parent_path": "/orgs/default/projects/project-quality/vpcs/test-lb-50fedbb3_mv836",
  "remote_path": "",
  "unique_id": "b3448c34-3eb7-4006-8e38-a8674fd7629a",
  "realization_id": "b3448c34-3eb7-4006-8e38-a8674fd7629a",
  "owner_id": "42495ba4-8c0b-49c9-b645-84cc39c2df30",
  "marked_for_delete": false,
  "overridden": false,
  "_system_owned": false,
  "_protection": "NOT_PROTECTED",
  "_create_time": 1760689255833,
  "_create_user": "wcp-cluster-user-f06fd228-8088-4439-a9e6-26c90a829c57-d34133d7-0fdf-4c9d-abcf-df83bd050a59",
  "_last_modified_time": 1760689255833,
  "_last_modified_user": "wcp-cluster-user-f06fd228-8088-4439-a9e6-26c90a829c57-d34133d7-0fdf-4c9d-abcf-df83bd050a59",
  "_revision": 0
}
```
<a id="188-policy-api-v1-orgs-default-projects-project-quality-vpcs-test-netpol-sync-c2cf40cd-65gvf-attachments-default"></a>
### 188. /policy/api/v1/orgs/default/projects/project-quality/vpcs/test-netpol-sync-c2cf40cd_65gvf/attachments/default

**HTTP Methods:** GET

**Explanation:**
VPC (Virtual Private Cloud) management within a project. Manages isolated network environments for workloads.

---

<a id="189-policy-api-v1-orgs-default-projects-project-quality-vpcs-testvpc-3658f2b5-subnets-pod-default-ec7c1039-d5d7u"></a>
### 189. /policy/api/v1/orgs/default/projects/project-quality/vpcs/testvpc-3658f2b5/subnets/pod-default-ec7c1039_d5d7u

**HTTP Methods:** DELETE, GET, PATCH

**Explanation:**
VPC subnet management within a project. Defines IP address ranges and network segments for VPC workloads.

**Request Body (PATCH):**
```json
{
  "access_mode": "Private_TGW",
  "advanced_config": {
    "static_ip_allocation": {
      "enabled": true
    }
  },
  "display_name": "pod-default-ec7c1039_d5d7u",
  "id": "pod-default-ec7c1039_d5d7u",
  "ipv4_subnet_size": 16,
  "subnet_dhcp_config": {
    "mode": "DHCP_DEACTIVATED"
  },
  "tags": [
    {
      "scope": "nsx-op/cluster",
      "tag": "f06fd228-8088-4439-a9e6-26c90a829c57"
    },
    {
      "scope": "nsx-op/version",
      "tag": "1.0.0"
    },
    {
      "scope": "nsx-op/subnetset_name",
      "tag": "pod-default"
    },
    {
      "scope": "nsx-op/subnetset_uid",
      "tag": "455d7685-2efd-406d-ad9d-05f82b3a508f"
    },
    {
      "scope": "nsx/managed-by",
      "tag": "nsx-op"
    },
    {
      "scope": "nsx-op/namespace_uid",
      "tag": "87995f00-857e-41a2-8687-41656a792cf7"
    },
    {
      "scope": "nsx-op/namespace",
      "tag": "test-prevpc-8f1a464f"
    },
    {
      "scope": "kubernetes.io/metadata.name",
      "tag": "test-prevpc-8f1a464f"
    },
    {
      "scope": "vSphereClusterID",
      "tag": "f06fd228-8088-4439-a9e6-26c90a829c57"
    }
  ]
}
```

---

<a id="190-policy-api-v1-orgs-default-projects-project-quality-vpcs-testvpc-7ab2d8aa-subnets-pod-default-e0268dd8-5583h"></a>
### 190. /policy/api/v1/orgs/default/projects/project-quality/vpcs/testvpc-7ab2d8aa/subnets/pod-default-e0268dd8_5583h

**HTTP Methods:** DELETE, GET, PATCH

**Explanation:**
VPC subnet management within a project. Defines IP address ranges and network segments for VPC workloads.

**Request Body (PATCH):**
```json
{
  "access_mode": "Private_TGW",
  "advanced_config": {
    "static_ip_allocation": {
      "enabled": true
    }
  },
  "display_name": "pod-default-e0268dd8_5583h",
  "id": "pod-default-e0268dd8_5583h",
  "ipv4_subnet_size": 16,
  "subnet_dhcp_config": {
    "mode": "DHCP_DEACTIVATED"
  },
  "tags": [
    {
      "scope": "nsx-op/cluster",
      "tag": "f06fd228-8088-4439-a9e6-26c90a829c57"
    },
    {
      "scope": "nsx-op/version",
      "tag": "1.0.0"
    },
    {
      "scope": "nsx-op/subnetset_name",
      "tag": "pod-default"
    },
    {
      "scope": "nsx-op/subnetset_uid",
      "tag": "36bfaa4d-6a5c-433f-9e05-dbee678d4d4c"
    },
    {
      "scope": "nsx/managed-by",
      "tag": "nsx-op"
    },
    {
      "scope": "nsx-op/namespace_uid",
      "tag": "a0a91583-c678-4a6d-8e23-f699d12140c4"
    },
    {
      "scope": "nsx-op/namespace",
      "tag": "test-prevpc-9f16bff1"
    },
    {
      "scope": "kubernetes.io/metadata.name",
      "tag": "test-prevpc-9f16bff1"
    },
    {
      "scope": "vSphereClusterID",
      "tag": "f06fd228-8088-4439-a9e6-26c90a829c57"
    }
  ]
}
```

---

<a id="191-policy-api-v1-orgs-default-projects-project-quality-vpcs-precreated-subnet-ns1-a72a2a9d-8m6zu-vpc-lbs-default"></a>
### 191. /policy/api/v1/orgs/default/projects/project-quality/vpcs/precreated-subnet-ns1-a72a2a9d_8m6zu/vpc-lbs/default

**HTTP Methods:** GET

**Explanation:**
VPC (Virtual Private Cloud) management within a project. Manages isolated network environments for workloads.

---


**Sample Response Body (GET, from logs):**
```json
{
  "connectivity_path": "/orgs/default/projects/project-quality/vpcs/precreated-subnet-ns1-a72a2a9d_8m6zu",
  "enabled": true,
  "relax_scale_validation": true,
  "size": "SMALL",
  "error_log_level": "INFO",
  "resource_type": "LBService",
  "id": "default",
  "display_name": "default",
  "tags": [
    {
      "scope": "nsx-op/cluster",
      "tag": "f06fd228-8088-4439-a9e6-26c90a829c57"
    },
    {
      "scope": "nsx-op/version",
      "tag": "1.0.0"
    },
    {
      "scope": "nsx-op/namespace",
      "tag": "precreated-subnet-ns1-a72a2a9d"
    },
    {
      "scope": "nsx-op/namespace_uid",
      "tag": "fb0c2f0a-e4cf-4742-b860-68261f4ac40b"
    },
    {
      "scope": "nsx-op/created_for",
      "tag": "SLB"
    }
  ],
  "path": "/orgs/default/projects/project-quality/vpcs/precreated-subnet-ns1-a72a2a9d_8m6zu/vpc-lbs/default",
  "relative_path": "default",
  "parent_path": "/orgs/default/projects/project-quality/vpcs/precreated-subnet-ns1-a72a2a9d_8m6zu",
  "remote_path": "",
  "unique_id": "6fba1679-f919-4e38-a3c2-5136d8ba7bb5",
  "realization_id": "6fba1679-f919-4e38-a3c2-5136d8ba7bb5",
  "owner_id": "42495ba4-8c0b-49c9-b645-84cc39c2df30",
  "marked_for_delete": false,
  "overridden": false,
  "_system_owned": false,
  "_protection": "NOT_PROTECTED",
  "_create_time": 1760690305463,
  "_create_user": "wcp-cluster-user-f06fd228-8088-4439-a9e6-26c90a829c57-d34133d7-0fdf-4c9d-abcf-df83bd050a59",
  "_last_modified_time": 1760690305463,
  "_last_modified_user": "wcp-cluster-user-f06fd228-8088-4439-a9e6-26c90a829c57-d34133d7-0fdf-4c9d-abcf-df83bd050a59",
  "_revision": 0
}
```
<a id="192-policy-api-v1-orgs-default-projects-project-quality-vpcs-precreated-subnet-ns2-42ff4c1a-tpi2w-vpc-lbs-default"></a>
### 192. /policy/api/v1/orgs/default/projects/project-quality/vpcs/precreated-subnet-ns2-42ff4c1a_tpi2w/vpc-lbs/default

**HTTP Methods:** GET

**Explanation:**
VPC (Virtual Private Cloud) management within a project. Manages isolated network environments for workloads.

---


**Sample Response Body (GET, from logs):**
```json
{
  "connectivity_path": "/orgs/default/projects/project-quality/vpcs/precreated-subnet-ns2-42ff4c1a_tpi2w",
  "enabled": true,
  "relax_scale_validation": true,
  "size": "SMALL",
  "error_log_level": "INFO",
  "resource_type": "LBService",
  "id": "default",
  "display_name": "default",
  "tags": [
    {
      "scope": "nsx-op/cluster",
      "tag": "f06fd228-8088-4439-a9e6-26c90a829c57"
    },
    {
      "scope": "nsx-op/version",
      "tag": "1.0.0"
    },
    {
      "scope": "nsx-op/namespace",
      "tag": "precreated-subnet-ns2-42ff4c1a"
    },
    {
      "scope": "nsx-op/namespace_uid",
      "tag": "b887cb00-e542-4424-9df8-15408df0ab92"
    },
    {
      "scope": "nsx-op/created_for",
      "tag": "SLB"
    }
  ],
  "path": "/orgs/default/projects/project-quality/vpcs/precreated-subnet-ns2-42ff4c1a_tpi2w/vpc-lbs/default",
  "relative_path": "default",
  "parent_path": "/orgs/default/projects/project-quality/vpcs/precreated-subnet-ns2-42ff4c1a_tpi2w",
  "remote_path": "",
  "unique_id": "ce413b40-e994-4664-bdd2-9fc743dab9aa",
  "realization_id": "ce413b40-e994-4664-bdd2-9fc743dab9aa",
  "owner_id": "42495ba4-8c0b-49c9-b645-84cc39c2df30",
  "marked_for_delete": false,
  "overridden": false,
  "_system_owned": false,
  "_protection": "NOT_PROTECTED",
  "_create_time": 1760690327533,
  "_create_user": "wcp-cluster-user-f06fd228-8088-4439-a9e6-26c90a829c57-d34133d7-0fdf-4c9d-abcf-df83bd050a59",
  "_last_modified_time": 1760690327533,
  "_last_modified_user": "wcp-cluster-user-f06fd228-8088-4439-a9e6-26c90a829c57-d34133d7-0fdf-4c9d-abcf-df83bd050a59",
  "_revision": 0
}
```
<a id="193-policy-api-v1-orgs-default-projects-project-quality-vpcs-subnet-e2e-1f11082b-56qvy-subnets-subnet-no-ip-56qvy"></a>
### 193. /policy/api/v1/orgs/default/projects/project-quality/vpcs/subnet-e2e-1f11082b_56qvy/subnets/subnet-no-ip_56qvy

**HTTP Methods:** DELETE, GET, PATCH

**Explanation:**
VPC subnet management within a project. Defines IP address ranges and network segments for VPC workloads.

**Request Body (PATCH):**
```json
{
  "access_mode": "Private",
  "advanced_config": {
    "connectivity_state": "CONNECTED",
    "static_ip_allocation": {
      "enabled": false
    }
  },
  "display_name": "subnet-no-ip_56qvy",
  "id": "subnet-no-ip_56qvy",
  "ipv4_subnet_size": 32,
  "subnet_dhcp_config": {
    "mode": "DHCP_DEACTIVATED"
  },
  "tags": [
    {
      "scope": "nsx-op/cluster",
      "tag": "f06fd228-8088-4439-a9e6-26c90a829c57"
    },
    {
      "scope": "nsx-op/version",
      "tag": "1.0.0"
    },
    {
      "scope": "nsx-op/subnet_name",
      "tag": "subnet-no-ip"
    },
    {
      "scope": "nsx-op/subnet_uid",
      "tag": "903545cb-d0e3-4163-9612-3fb017427d47"
    },
    {
      "scope": "nsx/managed-by",
      "tag": "nsx-op"
    },
    {
      "scope": "nsx-op/vm_namespace_uid",
      "tag": "f629b82e-5ea2-4298-b1cf-3bafcea373fa"
    },
    {
      "scope": "nsx-op/vm_namespace",
      "tag": "subnet-e2e-1f11082b"
    },
    {
      "scope": "kubernetes.io/metadata.name",
      "tag": "subnet-e2e-1f11082b"
    }
  ]
}
```

---

<a id="194-policy-api-v1-orgs-default-projects-project-quality-vpcs-test-ingress-sync-73e76bf1-rbp33-attachments-default"></a>
### 194. /policy/api/v1/orgs/default/projects/project-quality/vpcs/test-ingress-sync-73e76bf1_rbp33/attachments/default

**HTTP Methods:** GET

**Explanation:**
VPC (Virtual Private Cloud) management within a project. Manages isolated network environments for workloads.

---

<a id="195-policy-api-v1-orgs-default-projects-project-quality-vpcs-test-service-sync-f1d17bff-5230b-attachments-default"></a>
### 195. /policy/api/v1/orgs/default/projects/project-quality/vpcs/test-service-sync-f1d17bff_5230b/attachments/default

**HTTP Methods:** GET

**Explanation:**
VPC (Virtual Private Cloud) management within a project. Manages isolated network environments for workloads.

---

<a id="196-policy-api-v1-orgs-default-projects-project-quality-vpcs-web-da775e6f-6o7ts-subnets-pod-default-a734dd59-6o7ts"></a>
### 196. /policy/api/v1/orgs/default/projects/project-quality/vpcs/web-da775e6f_6o7ts/subnets/pod-default-a734dd59_6o7ts

**HTTP Methods:** DELETE, GET, PATCH

**Explanation:**
VPC subnet management within a project. Defines IP address ranges and network segments for VPC workloads.

**Request Body (PATCH):**
```json
{
  "access_mode": "Private_TGW",
  "advanced_config": {
    "static_ip_allocation": {
      "enabled": true
    }
  },
  "display_name": "pod-default-a734dd59_6o7ts",
  "id": "pod-default-a734dd59_6o7ts",
  "ipv4_subnet_size": 16,
  "subnet_dhcp_config": {
    "mode": "DHCP_DEACTIVATED"
  },
  "tags": [
    {
      "scope": "nsx-op/cluster",
      "tag": "f06fd228-8088-4439-a9e6-26c90a829c57"
    },
    {
      "scope": "nsx-op/version",
      "tag": "1.0.0"
    },
    {
      "scope": "nsx-op/subnetset_name",
      "tag": "pod-default"
    },
    {
      "scope": "nsx-op/subnetset_uid",
      "tag": "ad5433b7-334c-4aa4-8457-40f8b9fba137"
    },
    {
      "scope": "nsx/managed-by",
      "tag": "nsx-op"
    },
    {
      "scope": "nsx-op/namespace_uid",
      "tag": "d114a0e0-d12c-41ac-9435-213fd199fa7b"
    },
    {
      "scope": "nsx-op/namespace",
      "tag": "web-da775e6f"
    },
    {
      "scope": "kubernetes.io/metadata.name",
      "tag": "web-da775e6f"
    },
    {
      "scope": "vSphereClusterID",
      "tag": "f06fd228-8088-4439-a9e6-26c90a829c57"
    }
  ]
}
```

---

<a id="197-policy-api-v1-orgs-default-projects-project-quality-vpcs-networkinfo-default-efa7e691-1fkak-attachments-default"></a>
### 197. /policy/api/v1/orgs/default/projects/project-quality/vpcs/networkinfo-default-efa7e691_1fkak/attachments/default

**HTTP Methods:** GET

**Explanation:**
VPC (Virtual Private Cloud) management within a project. Manages isolated network environments for workloads.

---

<a id="198-policy-api-v1-orgs-default-projects-project-quality-vpcs-test-namespace-sync-49fbe5bd-p9u70-attachments-default"></a>
### 198. /policy/api/v1/orgs/default/projects/project-quality/vpcs/test-namespace-sync-49fbe5bd_p9u70/attachments/default

**HTTP Methods:** GET

**Explanation:**
VPC (Virtual Private Cloud) management within a project. Manages isolated network environments for workloads.

---

<a id="199-policy-api-v1-orgs-default-projects-project-quality-vpcs-precreated-target-ns-3c7c1821-v5ml5-attachments-default"></a>
### 199. /policy/api/v1/orgs/default/projects/project-quality/vpcs/precreated-target-ns-3c7c1821_v5ml5/attachments/default

**HTTP Methods:** GET

**Explanation:**
VPC (Virtual Private Cloud) management within a project. Manages isolated network environments for workloads.

---

<a id="200-policy-api-v1-orgs-default-projects-project-quality-vpcs-test-create-vm-basic-f449d9bf-3ehn6-attachments-default"></a>
### 200. /policy/api/v1/orgs/default/projects/project-quality/vpcs/test-create-vm-basic-f449d9bf_3ehn6/attachments/default

**HTTP Methods:** GET

**Explanation:**
VPC (Virtual Private Cloud) management within a project. Manages isolated network environments for workloads.

---

<a id="201-policy-api-v1-orgs-default-projects-project-quality-vpcs-test-security-policy-web-a2b779b4-f6e79-vpc-lbs-default"></a>
### 201. /policy/api/v1/orgs/default/projects/project-quality/vpcs/test-security-policy-web-a2b779b4_f6e79/vpc-lbs/default

**HTTP Methods:** GET

**Explanation:**
VPC (Virtual Private Cloud) management within a project. Manages isolated network environments for workloads.

---


**Sample Response Body (GET, from logs):**
```json
{
  "connectivity_path": "/orgs/default/projects/project-quality/vpcs/test-security-policy-web-a2b779b4_f6e79",
  "enabled": true,
  "relax_scale_validation": true,
  "size": "SMALL",
  "error_log_level": "INFO",
  "resource_type": "LBService",
  "id": "default",
  "display_name": "default",
  "tags": [
    {
      "scope": "nsx-op/cluster",
      "tag": "f06fd228-8088-4439-a9e6-26c90a829c57"
    },
    {
      "scope": "nsx-op/version",
      "tag": "1.0.0"
    },
    {
      "scope": "nsx-op/namespace",
      "tag": "test-security-policy-web-a2b779b4"
    },
    {
      "scope": "nsx-op/namespace_uid",
      "tag": "57bca641-76c0-4368-a354-37acdffaed83"
    },
    {
      "scope": "nsx-op/created_for",
      "tag": "SLB"
    }
  ],
  "path": "/orgs/default/projects/project-quality/vpcs/test-security-policy-web-a2b779b4_f6e79/vpc-lbs/default",
  "relative_path": "default",
  "parent_path": "/orgs/default/projects/project-quality/vpcs/test-security-policy-web-a2b779b4_f6e79",
  "remote_path": "",
  "unique_id": "33fb754c-46e4-40e3-b89e-cd13c27f2ef3",
  "realization_id": "33fb754c-46e4-40e3-b89e-cd13c27f2ef3",
  "owner_id": "42495ba4-8c0b-49c9-b645-84cc39c2df30",
  "marked_for_delete": false,
  "overridden": false,
  "_system_owned": false,
  "_protection": "NOT_PROTECTED",
  "_create_time": 1760689975768,
  "_create_user": "wcp-cluster-user-f06fd228-8088-4439-a9e6-26c90a829c57-d34133d7-0fdf-4c9d-abcf-df83bd050a59",
  "_last_modified_time": 1760689975768,
  "_last_modified_user": "wcp-cluster-user-f06fd228-8088-4439-a9e6-26c90a829c57-d34133d7-0fdf-4c9d-abcf-df83bd050a59",
  "_revision": 0
}
```
<a id="202-policy-api-v1-orgs-default-projects-project-quality-vpcs-client-91c3f484-qzuxu-subnets-pod-default-075e5037-qzuxu"></a>
### 202. /policy/api/v1/orgs/default/projects/project-quality/vpcs/client-91c3f484_qzuxu/subnets/pod-default-075e5037_qzuxu

**HTTP Methods:** DELETE, GET, PATCH

**Explanation:**
VPC subnet management within a project. Defines IP address ranges and network segments for VPC workloads.

**Request Body (PATCH):**
```json
{
  "access_mode": "Private_TGW",
  "advanced_config": {
    "static_ip_allocation": {
      "enabled": true
    }
  },
  "display_name": "pod-default-075e5037_qzuxu",
  "id": "pod-default-075e5037_qzuxu",
  "ipv4_subnet_size": 16,
  "subnet_dhcp_config": {
    "mode": "DHCP_DEACTIVATED"
  },
  "tags": [
    {
      "scope": "nsx-op/cluster",
      "tag": "f06fd228-8088-4439-a9e6-26c90a829c57"
    },
    {
      "scope": "nsx-op/version",
      "tag": "1.0.0"
    },
    {
      "scope": "nsx-op/subnetset_name",
      "tag": "pod-default"
    },
    {
      "scope": "nsx-op/subnetset_uid",
      "tag": "1ce079e6-3d4a-4d90-bfbf-3a9fe53497dd"
    },
    {
      "scope": "nsx/managed-by",
      "tag": "nsx-op"
    },
    {
      "scope": "nsx-op/namespace_uid",
      "tag": "e19581fd-dbb5-4b0c-b896-e4fcff60f0ed"
    },
    {
      "scope": "nsx-op/namespace",
      "tag": "client-91c3f484"
    },
    {
      "scope": "kubernetes.io/metadata.name",
      "tag": "client-91c3f484"
    },
    {
      "scope": "vSphereClusterID",
      "tag": "f06fd228-8088-4439-a9e6-26c90a829c57"
    }
  ]
}
```

---

<a id="203-policy-api-v1-orgs-default-projects-project-quality-vpcs-precreated-subnet-ns1-a72a2a9d-8m6zu-attachments-default"></a>
### 203. /policy/api/v1/orgs/default/projects/project-quality/vpcs/precreated-subnet-ns1-a72a2a9d_8m6zu/attachments/default

**HTTP Methods:** GET

**Explanation:**
VPC (Virtual Private Cloud) management within a project. Manages isolated network environments for workloads.

---

<a id="204-policy-api-v1-orgs-default-projects-project-quality-vpcs-precreated-subnet-ns2-42ff4c1a-tpi2w-attachments-default"></a>
### 204. /policy/api/v1/orgs/default/projects/project-quality/vpcs/precreated-subnet-ns2-42ff4c1a_tpi2w/attachments/default

**HTTP Methods:** GET

**Explanation:**
VPC (Virtual Private Cloud) management within a project. Manages isolated network environments for workloads.

---

<a id="205-policy-api-v1-orgs-default-projects-project-quality-vpcs-subnet-e2e-1f11082b-56qvy-subnets-subnet-dhcp-cidr-56qvy"></a>
### 205. /policy/api/v1/orgs/default/projects/project-quality/vpcs/subnet-e2e-1f11082b_56qvy/subnets/subnet-dhcp-cidr_56qvy

**HTTP Methods:** DELETE, GET, PATCH

**Explanation:**
VPC subnet management within a project. Defines IP address ranges and network segments for VPC workloads.

**Request Body (PATCH):**
```json
{
  "access_mode": "Private",
  "advanced_config": {
    "connectivity_state": "CONNECTED",
    "static_ip_allocation": {
      "enabled": false
    }
  },
  "display_name": "subnet-dhcp-cidr_56qvy",
  "id": "subnet-dhcp-cidr_56qvy",
  "ipv4_subnet_size": 32,
  "subnet_dhcp_config": {
    "mode": "DHCP_SERVER"
  },
  "tags": [
    {
      "scope": "nsx-op/cluster",
      "tag": "f06fd228-8088-4439-a9e6-26c90a829c57"
    },
    {
      "scope": "nsx-op/version",
      "tag": "1.0.0"
    },
    {
      "scope": "nsx-op/subnet_name",
      "tag": "subnet-dhcp-cidr"
    },
    {
      "scope": "nsx-op/subnet_uid",
      "tag": "72cf030b-2443-486a-afb0-1183069efd26"
    },
    {
      "scope": "nsx/managed-by",
      "tag": "nsx-op"
    },
    {
      "scope": "nsx-op/vm_namespace_uid",
      "tag": "f629b82e-5ea2-4298-b1cf-3bafcea373fa"
    },
    {
      "scope": "nsx-op/vm_namespace",
      "tag": "subnet-e2e-1f11082b"
    },
    {
      "scope": "kubernetes.io/metadata.name",
      "tag": "subnet-e2e-1f11082b"
    }
  ]
}
```

---

<a id="206-policy-api-v1-orgs-default-projects-project-quality-vpcs-subnet-e2e-1f11082b-56qvy-subnets-subnet-only-dhcp-56qvy"></a>
### 206. /policy/api/v1/orgs/default/projects/project-quality/vpcs/subnet-e2e-1f11082b_56qvy/subnets/subnet-only-dhcp_56qvy

**HTTP Methods:** DELETE, GET, PATCH

**Explanation:**
VPC subnet management within a project. Defines IP address ranges and network segments for VPC workloads.

**Request Body (PATCH):**
```json
{
  "access_mode": "Private",
  "advanced_config": {
    "connectivity_state": "CONNECTED",
    "static_ip_allocation": {
      "enabled": false
    }
  },
  "display_name": "subnet-only-dhcp_56qvy",
  "id": "subnet-only-dhcp_56qvy",
  "ipv4_subnet_size": 32,
  "subnet_dhcp_config": {
    "mode": "DHCP_SERVER"
  },
  "tags": [
    {
      "scope": "nsx-op/cluster",
      "tag": "f06fd228-8088-4439-a9e6-26c90a829c57"
    },
    {
      "scope": "nsx-op/version",
      "tag": "1.0.0"
    },
    {
      "scope": "nsx-op/subnet_name",
      "tag": "subnet-only-dhcp"
    },
    {
      "scope": "nsx-op/subnet_uid",
      "tag": "b19690c5-7787-47da-a1ac-daa80a8855fb"
    },
    {
      "scope": "nsx/managed-by",
      "tag": "nsx-op"
    },
    {
      "scope": "nsx-op/vm_namespace_uid",
      "tag": "f629b82e-5ea2-4298-b1cf-3bafcea373fa"
    },
    {
      "scope": "nsx-op/vm_namespace",
      "tag": "subnet-e2e-1f11082b"
    },
    {
      "scope": "kubernetes.io/metadata.name",
      "tag": "subnet-e2e-1f11082b"
    }
  ]
}
```

---

<a id="207-policy-api-v1-orgs-default-projects-project-quality-vpcs-test-ipaddress-allocation-40d5699d-2p2tu-vpc-lbs-default"></a>
### 207. /policy/api/v1/orgs/default/projects/project-quality/vpcs/test-ipaddress-allocation-40d5699d_2p2tu/vpc-lbs/default

**HTTP Methods:** GET

**Explanation:**
VPC (Virtual Private Cloud) management within a project. Manages isolated network environments for workloads.

---


**Sample Response Body (GET, from logs):**
```json
{
  "connectivity_path": "/orgs/default/projects/project-quality/vpcs/test-ipaddress-allocation-40d5699d_2p2tu",
  "enabled": true,
  "relax_scale_validation": true,
  "size": "SMALL",
  "error_log_level": "INFO",
  "resource_type": "LBService",
  "id": "default",
  "display_name": "default",
  "tags": [
    {
      "scope": "nsx-op/cluster",
      "tag": "f06fd228-8088-4439-a9e6-26c90a829c57"
    },
    {
      "scope": "nsx-op/version",
      "tag": "1.0.0"
    },
    {
      "scope": "nsx-op/namespace",
      "tag": "test-ipaddress-allocation-40d5699d"
    },
    {
      "scope": "nsx-op/namespace_uid",
      "tag": "bf9c62cf-7653-43fd-9177-7319f8b4fe95"
    },
    {
      "scope": "nsx-op/created_for",
      "tag": "SLB"
    }
  ],
  "path": "/orgs/default/projects/project-quality/vpcs/test-ipaddress-allocation-40d5699d_2p2tu/vpc-lbs/default",
  "relative_path": "default",
  "parent_path": "/orgs/default/projects/project-quality/vpcs/test-ipaddress-allocation-40d5699d_2p2tu",
  "remote_path": "",
  "unique_id": "e65168a9-0c43-4d98-b78f-4b16ecd6d598",
  "realization_id": "e65168a9-0c43-4d98-b78f-4b16ecd6d598",
  "owner_id": "42495ba4-8c0b-49c9-b645-84cc39c2df30",
  "marked_for_delete": false,
  "overridden": false,
  "_system_owned": false,
  "_protection": "NOT_PROTECTED",
  "_create_time": 1760689085578,
  "_create_user": "wcp-cluster-user-f06fd228-8088-4439-a9e6-26c90a829c57-d34133d7-0fdf-4c9d-abcf-df83bd050a59",
  "_last_modified_time": 1760689085578,
  "_last_modified_user": "wcp-cluster-user-f06fd228-8088-4439-a9e6-26c90a829c57-d34133d7-0fdf-4c9d-abcf-df83bd050a59",
  "_revision": 0
}
```
<a id="208-policy-api-v1-orgs-default-projects-project-quality-vpcs-test-lb-50fedbb3-mv836-subnets-pod-default-3cc5e9c8-mv836"></a>
### 208. /policy/api/v1/orgs/default/projects/project-quality/vpcs/test-lb-50fedbb3_mv836/subnets/pod-default-3cc5e9c8_mv836

**HTTP Methods:** DELETE, GET, PATCH

**Explanation:**
VPC subnet management within a project. Defines IP address ranges and network segments for VPC workloads.

**Request Body (PATCH):**
```json
{
  "access_mode": "Private_TGW",
  "advanced_config": {
    "static_ip_allocation": {
      "enabled": true
    }
  },
  "display_name": "pod-default-3cc5e9c8_mv836",
  "id": "pod-default-3cc5e9c8_mv836",
  "ipv4_subnet_size": 16,
  "subnet_dhcp_config": {
    "mode": "DHCP_DEACTIVATED"
  },
  "tags": [
    {
      "scope": "nsx-op/cluster",
      "tag": "f06fd228-8088-4439-a9e6-26c90a829c57"
    },
    {
      "scope": "nsx-op/version",
      "tag": "1.0.0"
    },
    {
      "scope": "nsx-op/subnetset_name",
      "tag": "pod-default"
    },
    {
      "scope": "nsx-op/subnetset_uid",
      "tag": "87e18b5a-4305-4a1b-862f-702f3ac0a0f4"
    },
    {
      "scope": "nsx/managed-by",
      "tag": "nsx-op"
    },
    {
      "scope": "nsx-op/namespace_uid",
      "tag": "2506fba2-2bca-42a9-9fb0-35aa09b1d33c"
    },
    {
      "scope": "nsx-op/namespace",
      "tag": "test-lb-50fedbb3"
    },
    {
      "scope": "kubernetes.io/metadata.name",
      "tag": "test-lb-50fedbb3"
    },
    {
      "scope": "vSphereClusterID",
      "tag": "f06fd228-8088-4439-a9e6-26c90a829c57"
    }
  ]
}
```

---

<a id="209-policy-api-v1-orgs-default-projects-project-quality-vpcs-test-security-policy-basic-72ecfa65-ib6li-vpc-lbs-default"></a>
### 209. /policy/api/v1/orgs/default/projects/project-quality/vpcs/test-security-policy-basic-72ecfa65_ib6li/vpc-lbs/default

**HTTP Methods:** GET

**Explanation:**
VPC (Virtual Private Cloud) management within a project. Manages isolated network environments for workloads.

---


**Sample Response Body (GET, from logs):**
```json
{
  "connectivity_path": "/orgs/default/projects/project-quality/vpcs/test-security-policy-basic-72ecfa65_ib6li",
  "enabled": true,
  "relax_scale_validation": true,
  "size": "SMALL",
  "error_log_level": "INFO",
  "resource_type": "LBService",
  "id": "default",
  "display_name": "default",
  "tags": [
    {
      "scope": "nsx-op/cluster",
      "tag": "f06fd228-8088-4439-a9e6-26c90a829c57"
    },
    {
      "scope": "nsx-op/version",
      "tag": "1.0.0"
    },
    {
      "scope": "nsx-op/namespace",
      "tag": "test-security-policy-basic-72ecfa65"
    },
    {
      "scope": "nsx-op/namespace_uid",
      "tag": "a022f7f8-ff5d-4e79-964f-8782d0683f3a"
    },
    {
      "scope": "nsx-op/created_for",
      "tag": "SLB"
    }
  ],
  "path": "/orgs/default/projects/project-quality/vpcs/test-security-policy-basic-72ecfa65_ib6li/vpc-lbs/default",
  "relative_path": "default",
  "parent_path": "/orgs/default/projects/project-quality/vpcs/test-security-policy-basic-72ecfa65_ib6li",
  "remote_path": "",
  "unique_id": "1068c26b-38cf-46bd-9946-6646f82baa02",
  "realization_id": "1068c26b-38cf-46bd-9946-6646f82baa02",
  "owner_id": "42495ba4-8c0b-49c9-b645-84cc39c2df30",
  "marked_for_delete": false,
  "overridden": false,
  "_system_owned": false,
  "_protection": "NOT_PROTECTED",
  "_create_time": 1760689462889,
  "_create_user": "wcp-cluster-user-f06fd228-8088-4439-a9e6-26c90a829c57-d34133d7-0fdf-4c9d-abcf-df83bd050a59",
  "_last_modified_time": 1760689462889,
  "_last_modified_user": "wcp-cluster-user-f06fd228-8088-4439-a9e6-26c90a829c57-d34133d7-0fdf-4c9d-abcf-df83bd050a59",
  "_revision": 0
}
```
<a id="210-policy-api-v1-orgs-default-projects-project-quality-vpcs-target-ns-56446c91-6zdip-subnets-vm-default-eb532fd0-c6gls"></a>
### 210. /policy/api/v1/orgs/default/projects/project-quality/vpcs/target-ns-56446c91_6zdip/subnets/vm-default-eb532fd0_c6gls

**HTTP Methods:** DELETE, GET, PATCH

**Explanation:**
VPC subnet management within a project. Defines IP address ranges and network segments for VPC workloads.

**Request Body (PATCH):**
```json
{
  "access_mode": "Private",
  "advanced_config": {
    "static_ip_allocation": {
      "enabled": true
    }
  },
  "display_name": "vm-default-eb532fd0_c6gls",
  "id": "vm-default-eb532fd0_c6gls",
  "ipv4_subnet_size": 32,
  "subnet_dhcp_config": {
    "mode": "DHCP_DEACTIVATED"
  },
  "tags": [
    {
      "scope": "nsx-op/cluster",
      "tag": "f06fd228-8088-4439-a9e6-26c90a829c57"
    },
    {
      "scope": "nsx-op/version",
      "tag": "1.0.0"
    },
    {
      "scope": "nsx-op/subnetset_name",
      "tag": "vm-default"
    },
    {
      "scope": "nsx-op/subnetset_uid",
      "tag": "06da1bb0-aca2-4875-b521-b1ba476722a2"
    },
    {
      "scope": "nsx/managed-by",
      "tag": "nsx-op"
    },
    {
      "scope": "nsx-op/vm_namespace_uid",
      "tag": "b8c362f7-3bda-4a5b-8cad-cd7a79b4f372"
    },
    {
      "scope": "nsx-op/vm_namespace",
      "tag": "subnet-e2e-shared-05b500ba"
    },
    {
      "scope": "kubernetes.io/metadata.name",
      "tag": "subnet-e2e-shared-05b500ba"
    }
  ]
}
```

---

<a id="211-policy-api-v1-orgs-default-projects-project-quality-vpcs-test-lb-50fedbb3-mv836-vpc-lb-pools-tea-svc-80-mv836-scsoh"></a>
### 211. /policy/api/v1/orgs/default/projects/project-quality/vpcs/test-lb-50fedbb3_mv836/vpc-lb-pools/tea-svc_80_mv836_scsoh

**HTTP Methods:** DELETE, GET, PATCH

**Explanation:**
VPC (Virtual Private Cloud) management within a project. Manages isolated network environments for workloads.

---


**Sample Response Body (GET, from logs):**
```json
{
  "algorithm": "ROUND_ROBIN",
  "snat_translation": {
    "type": "LBSnatAutoMap"
  },
  "min_active_members": 1,
  "resource_type": "LBPool",
  "id": "tea-svc_80_mv836_scsoh",
  "display_name": "tea-svc_80",
  "tags": [
    {
      "scope": "ncp/version",
      "tag": "1.2.0"
    },
    {
      "scope": "ncp/cluster",
      "tag": "f06fd228-8088-4439-a9e6-26c90a829c57"
    },
    {
      "scope": "ncp/project",
      "tag": "test-lb-50fedbb3"
    },
    {
      "scope": "external_id",
      "tag": "f8572ed6-448c-4830-8e1d-5c00326ab97f"
    },
    {
      "scope": "ncp/service",
      "tag": "tea-svc"
    },
    {
      "scope": "ncp/service_port",
      "tag": "80"
    },
    {
      "scope": "ncp/service_uid",
      "tag": "f8572ed6-448c-4830-8e1d-5c00326ab97f"
    },
    {
      "scope": "ncp/created_for",
      "tag": "SLB"
    },
    {
      "scope": "ncp/service_port_protocol",
      "tag": "UDP"
    }
  ],
  "path": "/orgs/default/projects/project-quality/vpcs/test-lb-50fedbb3_mv836/vpc-lb-pools/tea-svc_80_mv836_scsoh",
  "relative_path": "tea-svc_80_mv836_scsoh",
  "parent_path": "/orgs/default/projects/project-quality/vpcs/test-lb-50fedbb3_mv836",
  "remote_path": "",
  "unique_id": "33a60fff-84d2-40a0-8b88-066c81f05c73",
  "realization_id": "33a60fff-84d2-40a0-8b88-066c81f05c73",
  "owner_id": "42495ba4-8c0b-49c9-b645-84cc39c2df30",
  "marked_for_delete": false,
  "overridden": false,
  "_system_owned": false,
  "_protection": "NOT_PROTECTED",
  "_create_time": 1760689216999,
  "_create_user": "wcp-cluster-user-f06fd228-8088-4439-a9e6-26c90a829c57-d34133d7-0fdf-4c9d-abcf-df83bd050a59",
  "_last_modified_time": 1760689216999,
  "_last_modified_user": "wcp-cluster-user-f06fd228-8088-4439-a9e6-26c90a829c57-d34133d7-0fdf-4c9d-abcf-df83bd050a59",
  "_revision": 0
}
```
<a id="212-policy-api-v1-orgs-default-projects-project-quality-vpcs-test-lb-50fedbb3-mv836-vpc-lb-pools-tea-svc-80-mv836-xirvk"></a>
### 212. /policy/api/v1/orgs/default/projects/project-quality/vpcs/test-lb-50fedbb3_mv836/vpc-lb-pools/tea-svc_80_mv836_xirvk

**HTTP Methods:** DELETE, GET, PATCH

**Explanation:**
VPC (Virtual Private Cloud) management within a project. Manages isolated network environments for workloads.

---


**Sample Response Body (GET, from logs):**
```json
{
  "algorithm": "ROUND_ROBIN",
  "snat_translation": {
    "type": "LBSnatAutoMap"
  },
  "min_active_members": 1,
  "resource_type": "LBPool",
  "id": "tea-svc_80_mv836_xirvk",
  "display_name": "tea-svc_80",
  "tags": [
    {
      "scope": "ncp/version",
      "tag": "1.2.0"
    },
    {
      "scope": "ncp/cluster",
      "tag": "f06fd228-8088-4439-a9e6-26c90a829c57"
    },
    {
      "scope": "ncp/project",
      "tag": "test-lb-50fedbb3"
    },
    {
      "scope": "external_id",
      "tag": "f8572ed6-448c-4830-8e1d-5c00326ab97f"
    },
    {
      "scope": "ncp/service",
      "tag": "tea-svc"
    },
    {
      "scope": "ncp/service_port",
      "tag": "80"
    },
    {
      "scope": "ncp/service_uid",
      "tag": "f8572ed6-448c-4830-8e1d-5c00326ab97f"
    },
    {
      "scope": "ncp/created_for",
      "tag": "SLB"
    },
    {
      "scope": "ncp/service_port_protocol",
      "tag": "TCP"
    }
  ],
  "path": "/orgs/default/projects/project-quality/vpcs/test-lb-50fedbb3_mv836/vpc-lb-pools/tea-svc_80_mv836_xirvk",
  "relative_path": "tea-svc_80_mv836_xirvk",
  "parent_path": "/orgs/default/projects/project-quality/vpcs/test-lb-50fedbb3_mv836",
  "remote_path": "",
  "unique_id": "58ad97de-1cc4-4c41-94d3-cc3f4a56d5db",
  "realization_id": "58ad97de-1cc4-4c41-94d3-cc3f4a56d5db",
  "owner_id": "42495ba4-8c0b-49c9-b645-84cc39c2df30",
  "marked_for_delete": false,
  "overridden": false,
  "_system_owned": false,
  "_protection": "NOT_PROTECTED",
  "_create_time": 1760689212354,
  "_create_user": "wcp-cluster-user-f06fd228-8088-4439-a9e6-26c90a829c57-d34133d7-0fdf-4c9d-abcf-df83bd050a59",
  "_last_modified_time": 1760689212354,
  "_last_modified_user": "wcp-cluster-user-f06fd228-8088-4439-a9e6-26c90a829c57-d34133d7-0fdf-4c9d-abcf-df83bd050a59",
  "_revision": 0
}
```
<a id="213-policy-api-v1-orgs-default-projects-project-quality-vpcs-test-pod-1dd9a577-fu9t5-subnets-pod-default-5cf92338-fu9t5"></a>
### 213. /policy/api/v1/orgs/default/projects/project-quality/vpcs/test-pod-1dd9a577_fu9t5/subnets/pod-default-5cf92338_fu9t5

**HTTP Methods:** DELETE, GET, PATCH

**Explanation:**
VPC subnet management within a project. Defines IP address ranges and network segments for VPC workloads.

**Request Body (PATCH):**
```json
{
  "access_mode": "Private_TGW",
  "advanced_config": {
    "static_ip_allocation": {
      "enabled": true
    }
  },
  "display_name": "pod-default-5cf92338_fu9t5",
  "id": "pod-default-5cf92338_fu9t5",
  "ipv4_subnet_size": 16,
  "subnet_dhcp_config": {
    "mode": "DHCP_DEACTIVATED"
  },
  "tags": [
    {
      "scope": "nsx-op/cluster",
      "tag": "f06fd228-8088-4439-a9e6-26c90a829c57"
    },
    {
      "scope": "nsx-op/version",
      "tag": "1.0.0"
    },
    {
      "scope": "nsx-op/subnetset_name",
      "tag": "pod-default"
    },
    {
      "scope": "nsx-op/subnetset_uid",
      "tag": "d63ae866-6011-423b-aa7e-3dbd6292a9d6"
    },
    {
      "scope": "nsx/managed-by",
      "tag": "nsx-op"
    },
    {
      "scope": "nsx-op/namespace_uid",
      "tag": "6c0816d9-ed05-4f26-91d1-b87dae8e9c1b"
    },
    {
      "scope": "nsx-op/namespace",
      "tag": "test-pod-1dd9a577"
    },
    {
      "scope": "kubernetes.io/metadata.name",
      "tag": "test-pod-1dd9a577"
    },
    {
      "scope": "vSphereClusterID",
      "tag": "f06fd228-8088-4439-a9e6-26c90a829c57"
    }
  ]
}
```

---

<a id="214-policy-api-v1-orgs-default-projects-project-quality-vpcs-test-security-policy-client-3a06d660-qiyvu-vpc-lbs-default"></a>
### 214. /policy/api/v1/orgs/default/projects/project-quality/vpcs/test-security-policy-client-3a06d660_qiyvu/vpc-lbs/default

**HTTP Methods:** GET

**Explanation:**
VPC (Virtual Private Cloud) management within a project. Manages isolated network environments for workloads.

---


**Sample Response Body (GET, from logs):**
```json
{
  "connectivity_path": "/orgs/default/projects/project-quality/vpcs/test-security-policy-client-3a06d660_qiyvu",
  "enabled": true,
  "relax_scale_validation": true,
  "size": "SMALL",
  "error_log_level": "INFO",
  "resource_type": "LBService",
  "id": "default",
  "display_name": "default",
  "tags": [
    {
      "scope": "nsx-op/cluster",
      "tag": "f06fd228-8088-4439-a9e6-26c90a829c57"
    },
    {
      "scope": "nsx-op/version",
      "tag": "1.0.0"
    },
    {
      "scope": "nsx-op/namespace",
      "tag": "test-security-policy-client-3a06d660"
    },
    {
      "scope": "nsx-op/namespace_uid",
      "tag": "a84abf99-2aca-4594-854f-381bc44d868b"
    },
    {
      "scope": "nsx-op/created_for",
      "tag": "SLB"
    }
  ],
  "path": "/orgs/default/projects/project-quality/vpcs/test-security-policy-client-3a06d660_qiyvu/vpc-lbs/default",
  "relative_path": "default",
  "parent_path": "/orgs/default/projects/project-quality/vpcs/test-security-policy-client-3a06d660_qiyvu",
  "remote_path": "",
  "unique_id": "53a7adac-600c-43ad-af9b-a138adffe2db",
  "realization_id": "53a7adac-600c-43ad-af9b-a138adffe2db",
  "owner_id": "42495ba4-8c0b-49c9-b645-84cc39c2df30",
  "marked_for_delete": false,
  "overridden": false,
  "_system_owned": false,
  "_protection": "NOT_PROTECTED",
  "_create_time": 1760689975342,
  "_create_user": "wcp-cluster-user-f06fd228-8088-4439-a9e6-26c90a829c57-d34133d7-0fdf-4c9d-abcf-df83bd050a59",
  "_last_modified_time": 1760689975342,
  "_last_modified_user": "wcp-cluster-user-f06fd228-8088-4439-a9e6-26c90a829c57-d34133d7-0fdf-4c9d-abcf-df83bd050a59",
  "_revision": 0
}
```
<a id="215-policy-api-v1-orgs-default-projects-project-quality-vpcs-subnet-e2e-1f11082b-56qvy-subnets-subnet-only-no-dhcp-56qvy"></a>
### 215. /policy/api/v1/orgs/default/projects/project-quality/vpcs/subnet-e2e-1f11082b_56qvy/subnets/subnet-only-no-dhcp_56qvy

**HTTP Methods:** DELETE, GET, PATCH

**Explanation:**
VPC subnet management within a project. Defines IP address ranges and network segments for VPC workloads.

**Request Body (PATCH):**
```json
{
  "access_mode": "Private",
  "advanced_config": {
    "connectivity_state": "CONNECTED",
    "static_ip_allocation": {
      "enabled": true
    }
  },
  "display_name": "subnet-only-no-dhcp_56qvy",
  "id": "subnet-only-no-dhcp_56qvy",
  "ipv4_subnet_size": 32,
  "subnet_dhcp_config": {
    "mode": "DHCP_DEACTIVATED"
  },
  "tags": [
    {
      "scope": "nsx-op/cluster",
      "tag": "f06fd228-8088-4439-a9e6-26c90a829c57"
    },
    {
      "scope": "nsx-op/version",
      "tag": "1.0.0"
    },
    {
      "scope": "nsx-op/subnet_name",
      "tag": "subnet-only-no-dhcp"
    },
    {
      "scope": "nsx-op/subnet_uid",
      "tag": "749dacef-2d50-4e13-b4e8-0f332e243af2"
    },
    {
      "scope": "nsx/managed-by",
      "tag": "nsx-op"
    },
    {
      "scope": "nsx-op/vm_namespace_uid",
      "tag": "f629b82e-5ea2-4298-b1cf-3bafcea373fa"
    },
    {
      "scope": "nsx-op/vm_namespace",
      "tag": "subnet-e2e-1f11082b"
    },
    {
      "scope": "kubernetes.io/metadata.name",
      "tag": "subnet-e2e-1f11082b"
    }
  ]
}
```

---

<a id="216-policy-api-v1-orgs-default-projects-project-quality-vpcs-test-security-policy-web-a2b779b4-f6e79-attachments-default"></a>
### 216. /policy/api/v1/orgs/default/projects/project-quality/vpcs/test-security-policy-web-a2b779b4_f6e79/attachments/default

**HTTP Methods:** GET

**Explanation:**
VPC (Virtual Private Cloud) management within a project. Manages isolated network environments for workloads.

---

<a id="217-policy-api-v1-orgs-default-projects-project-quality-vpcs-subnet-e2e-1f11082b-56qvy-subnets-pod-default-6a81803a-56qvy"></a>
### 217. /policy/api/v1/orgs/default/projects/project-quality/vpcs/subnet-e2e-1f11082b_56qvy/subnets/pod-default-6a81803a_56qvy

**HTTP Methods:** DELETE, GET, PATCH

**Explanation:**
VPC subnet management within a project. Defines IP address ranges and network segments for VPC workloads.

**Request Body (PATCH):**
```json
{
  "access_mode": "Private_TGW",
  "advanced_config": {
    "static_ip_allocation": {
      "enabled": true
    }
  },
  "display_name": "pod-default-6a81803a_56qvy",
  "id": "pod-default-6a81803a_56qvy",
  "ipv4_subnet_size": 32,
  "subnet_dhcp_config": {
    "mode": "DHCP_DEACTIVATED"
  },
  "tags": [
    {
      "scope": "nsx-op/cluster",
      "tag": "f06fd228-8088-4439-a9e6-26c90a829c57"
    },
    {
      "scope": "nsx-op/version",
      "tag": "1.0.0"
    },
    {
      "scope": "nsx-op/subnetset_name",
      "tag": "pod-default"
    },
    {
      "scope": "nsx-op/subnetset_uid",
      "tag": "773fe14b-1212-4183-9695-1fac65bb571a"
    },
    {
      "scope": "nsx/managed-by",
      "tag": "nsx-op"
    },
    {
      "scope": "nsx-op/namespace_uid",
      "tag": "f629b82e-5ea2-4298-b1cf-3bafcea373fa"
    },
    {
      "scope": "nsx-op/namespace",
      "tag": "subnet-e2e-1f11082b"
    },
    {
      "scope": "kubernetes.io/metadata.name",
      "tag": "subnet-e2e-1f11082b"
    }
  ]
}
```

---

<a id="218-policy-api-v1-orgs-default-projects-project-quality-vpcs-subnet-e2e-1f11082b-56qvy-subnets-subnet-dhcp-modify-1-56qvy"></a>
### 218. /policy/api/v1/orgs/default/projects/project-quality/vpcs/subnet-e2e-1f11082b_56qvy/subnets/subnet-dhcp-modify-1_56qvy

**HTTP Methods:** DELETE, GET, PATCH

**Explanation:**
VPC subnet management within a project. Defines IP address ranges and network segments for VPC workloads.

**Request Body (PATCH):**
```json
{
  "access_mode": "Private",
  "advanced_config": {
    "connectivity_state": "CONNECTED",
    "static_ip_allocation": {
      "enabled": false
    }
  },
  "display_name": "subnet-dhcp-modify-1_56qvy",
  "id": "subnet-dhcp-modify-1_56qvy",
  "ipv4_subnet_size": 32,
  "subnet_dhcp_config": {
    "mode": "DHCP_DEACTIVATED"
  },
  "tags": [
    {
      "scope": "nsx-op/cluster",
      "tag": "f06fd228-8088-4439-a9e6-26c90a829c57"
    },
    {
      "scope": "nsx-op/version",
      "tag": "1.0.0"
    },
    {
      "scope": "nsx-op/subnet_name",
      "tag": "subnet-dhcp-modify-1"
    },
    {
      "scope": "nsx-op/subnet_uid",
      "tag": "11c06417-8ce0-44a4-93d1-4b352c098bcd"
    },
    {
      "scope": "nsx/managed-by",
      "tag": "nsx-op"
    },
    {
      "scope": "nsx-op/vm_namespace_uid",
      "tag": "f629b82e-5ea2-4298-b1cf-3bafcea373fa"
    },
    {
      "scope": "nsx-op/vm_namespace",
      "tag": "subnet-e2e-1f11082b"
    },
    {
      "scope": "kubernetes.io/metadata.name",
      "tag": "subnet-e2e-1f11082b"
    }
  ]
}
```

---

<a id="219-policy-api-v1-orgs-default-projects-project-quality-vpcs-test-ipaddress-allocation-40d5699d-2p2tu-attachments-default"></a>
### 219. /policy/api/v1/orgs/default/projects/project-quality/vpcs/test-ipaddress-allocation-40d5699d_2p2tu/attachments/default

**HTTP Methods:** GET

**Explanation:**
VPC (Virtual Private Cloud) management within a project. Manages isolated network environments for workloads.

---

<a id="220-policy-api-v1-orgs-default-projects-project-quality-vpcs-test-ingress-sync-73e76bf1-rbp33-ip-address-allocations-9ca2y"></a>
### 220. /policy/api/v1/orgs/default/projects/project-quality/vpcs/test-ingress-sync-73e76bf1_rbp33/ip-address-allocations/9ca2y

**HTTP Methods:** DELETE, GET, PATCH

**Explanation:**
VPC (Virtual Private Cloud) management within a project. Manages isolated network environments for workloads.

---


**Sample Response Body (GET, from logs):**
```json
{
  "ip_address_type": "IPV4",
  "ip_address_block_visibility": "EXTERNAL",
  "allocation_ip": "192.168.0.8",
  "allocation_ips": "192.168.0.8",
  "resource_type": "VpcIpAddressAllocation",
  "id": "9ca2y",
  "display_name": "9ca2y",
  "tags": [
    {
      "scope": "ncp/version",
      "tag": "1.2.0"
    },
    {
      "scope": "ncp/cluster",
      "tag": "f06fd228-8088-4439-a9e6-26c90a829c57"
    },
    {
      "scope": "ncp/project",
      "tag": "test-ingress-sync-73e76bf1"
    },
    {
      "scope": "ncp/project_uid",
      "tag": "d9efcae1-642a-478c-9bb0-c5af498af932"
    },
    {
      "scope": "ncp/created_for",
      "tag": "l7_per_namespace"
    }
  ],
  "path": "/orgs/default/projects/project-quality/vpcs/test-ingress-sync-73e76bf1_rbp33/ip-address-allocations/9ca2y",
  "relative_path": "9ca2y",
  "parent_path": "/orgs/default/projects/project-quality/vpcs/test-ingress-sync-73e76bf1_rbp33",
  "remote_path": "",
  "unique_id": "7d97d4c6-c870-4af9-acec-f27cec95a42b",
  "realization_id": "7d97d4c6-c870-4af9-acec-f27cec95a42b",
  "owner_id": "42495ba4-8c0b-49c9-b645-84cc39c2df30",
  "marked_for_delete": false,
  "overridden": false,
  "_system_owned": false,
  "_protection": "NOT_PROTECTED",
  "_create_time": 1760689048583,
  "_create_user": "wcp-cluster-user-f06fd228-8088-4439-a9e6-26c90a829c57-d34133d7-0fdf-4c9d-abcf-df83bd050a59",
  "_last_modified_time": 1760689048583,
  "_last_modified_user": "wcp-cluster-user-f06fd228-8088-4439-a9e6-26c90a829c57-d34133d7-0fdf-4c9d-abcf-df83bd050a59",
  "_revision": 0
}
```
<a id="221-policy-api-v1-orgs-default-projects-project-quality-vpcs-test-lb-50fedbb3-mv836-ip-address-allocations-coffee-ip-mv836"></a>
### 221. /policy/api/v1/orgs/default/projects/project-quality/vpcs/test-lb-50fedbb3_mv836/ip-address-allocations/coffee-ip_mv836

**HTTP Methods:** DELETE, GET, PATCH

**Explanation:**
VPC (Virtual Private Cloud) management within a project. Manages isolated network environments for workloads.

**Request Body (PATCH):**
```json
{
  "allocation_size": 32,
  "display_name": "coffee-ip",
  "id": "coffee-ip_mv836",
  "ip_address_block_visibility": "EXTERNAL",
  "tags": [
    {
      "scope": "nsx-op/cluster",
      "tag": "f06fd228-8088-4439-a9e6-26c90a829c57"
    },
    {
      "scope": "nsx-op/version",
      "tag": "1.0.0"
    },
    {
      "scope": "nsx-op/namespace",
      "tag": "test-lb-50fedbb3"
    },
    {
      "scope": "nsx-op/ipaddressallocation_name",
      "tag": "coffee-ip"
    },
    {
      "scope": "nsx-op/ipaddressallocation_uid",
      "tag": "d29cb6d4-df81-4483-90ba-7fad27aca17b"
    },
    {
      "scope": "nsx-op/namespace_uid",
      "tag": "2506fba2-2bca-42a9-9fb0-35aa09b1d33c"
    }
  ]
}
```

---

<a id="222-policy-api-v1-orgs-default-projects-project-quality-vpcs-test-lb-50fedbb3-mv836-vpc-lb-pools-coffee-svc-80-mv836-eyftl"></a>
### 222. /policy/api/v1/orgs/default/projects/project-quality/vpcs/test-lb-50fedbb3_mv836/vpc-lb-pools/coffee-svc_80_mv836_eyftl

**HTTP Methods:** DELETE, GET, PATCH

**Explanation:**
VPC (Virtual Private Cloud) management within a project. Manages isolated network environments for workloads.

---


**Sample Response Body (GET, from logs):**
```json
{
  "algorithm": "ROUND_ROBIN",
  "members": [
    {
      "display_name": "coffee-svc.coffee",
      "ip_address": "10.246.0.21",
      "port": "80",
      "admin_state": "ENABLED",
      "backup_member": false,
      "weight": 1
    }
  ],
  "snat_translation": {
    "type": "LBSnatAutoMap"
  },
  "min_active_members": 1,
  "resource_type": "LBPool",
  "id": "coffee-svc_80_mv836_eyftl",
  "display_name": "coffee-svc_80",
  "tags": [
    {
      "scope": "ncp/version",
      "tag": "1.2.0"
    },
    {
      "scope": "ncp/cluster",
      "tag": "f06fd228-8088-4439-a9e6-26c90a829c57"
    },
    {
      "scope": "ncp/project",
      "tag": "test-lb-50fedbb3"
    },
    {
      "scope": "external_id",
      "tag": "75a666bb-cb7a-45dd-a6a6-6d0f0e7d685e"
    },
    {
      "scope": "ncp/service",
      "tag": "coffee-svc"
    },
    {
      "scope": "ncp/service_port",
      "tag": "80"
    },
    {
      "scope": "ncp/service_uid",
      "tag": "75a666bb-cb7a-45dd-a6a6-6d0f0e7d685e"
    },
    {
      "scope": "ncp/created_for",
      "tag": "SLB"
    },
    {
      "scope": "ncp/service_port_protocol",
      "tag": "TCP"
    }
  ],
  "path": "/orgs/default/projects/project-quality/vpcs/test-lb-50fedbb3_mv836/vpc-lb-pools/coffee-svc_80_mv836_eyftl",
  "relative_path": "coffee-svc_80_mv836_eyftl",
  "parent_path": "/orgs/default/projects/project-quality/vpcs/test-lb-50fedbb3_mv836",
  "remote_path": "",
  "unique_id": "db7b5ab8-0951-4223-8191-5f9e832c969d",
  "realization_id": "db7b5ab8-0951-4223-8191-5f9e832c969d",
  "owner_id": "42495ba4-8c0b-49c9-b645-84cc39c2df30",
  "marked_for_delete": false,
  "overridden": false,
  "_system_owned": false,
  "_protection": "NOT_PROTECTED",
  "_create_time": 1760689287316,
  "_create_user": "wcp-cluster-user-f06fd228-8088-4439-a9e6-26c90a829c57-d34133d7-0fdf-4c9d-abcf-df83bd050a59",
  "_last_modified_time": 1760689287316,
  "_last_modified_user": "wcp-cluster-user-f06fd228-8088-4439-a9e6-26c90a829c57-d34133d7-0fdf-4c9d-abcf-df83bd050a59",
  "_revision": 0
}
```
<a id="223-policy-api-v1-orgs-default-projects-project-quality-vpcs-test-security-policy-basic-72ecfa65-ib6li-attachments-default"></a>
### 223. /policy/api/v1/orgs/default/projects/project-quality/vpcs/test-security-policy-basic-72ecfa65_ib6li/attachments/default

**HTTP Methods:** GET

**Explanation:**
VPC (Virtual Private Cloud) management within a project. Manages isolated network environments for workloads.

---

<a id="224-policy-api-v1-orgs-default-projects-project-quality-vpcs-test-lb-50fedbb3-mv836-vpc-lb-pools-default-svc-80-mv836-iszzt"></a>
### 224. /policy/api/v1/orgs/default/projects/project-quality/vpcs/test-lb-50fedbb3_mv836/vpc-lb-pools/default-svc_80_mv836_iszzt

**HTTP Methods:** DELETE, GET, PATCH

**Explanation:**
VPC (Virtual Private Cloud) management within a project. Manages isolated network environments for workloads.

---


**Sample Response Body (GET, from logs):**
```json
{
  "algorithm": "ROUND_ROBIN",
  "snat_translation": {
    "type": "LBSnatAutoMap"
  },
  "min_active_members": 1,
  "resource_type": "LBPool",
  "id": "default-svc_80_mv836_iszzt",
  "display_name": "default-svc_80",
  "tags": [
    {
      "scope": "ncp/version",
      "tag": "1.2.0"
    },
    {
      "scope": "ncp/cluster",
      "tag": "f06fd228-8088-4439-a9e6-26c90a829c57"
    },
    {
      "scope": "ncp/project",
      "tag": "test-lb-50fedbb3"
    },
    {
      "scope": "external_id",
      "tag": "413462da-ad49-4afb-b755-88770ab32637"
    },
    {
      "scope": "ncp/service",
      "tag": "default-svc"
    },
    {
      "scope": "ncp/service_port",
      "tag": "80"
    },
    {
      "scope": "ncp/service_uid",
      "tag": "413462da-ad49-4afb-b755-88770ab32637"
    },
    {
      "scope": "ncp/created_for",
      "tag": "SLB"
    },
    {
      "scope": "ncp/service_port_protocol",
      "tag": "TCP"
    }
  ],
  "path": "/orgs/default/projects/project-quality/vpcs/test-lb-50fedbb3_mv836/vpc-lb-pools/default-svc_80_mv836_iszzt",
  "relative_path": "default-svc_80_mv836_iszzt",
  "parent_path": "/orgs/default/projects/project-quality/vpcs/test-lb-50fedbb3_mv836",
  "remote_path": "",
  "unique_id": "c7c4dacf-9ae2-4a50-91d0-e7cb5298dc64",
  "realization_id": "c7c4dacf-9ae2-4a50-91d0-e7cb5298dc64",
  "owner_id": "42495ba4-8c0b-49c9-b645-84cc39c2df30",
  "marked_for_delete": false,
  "overridden": false,
  "_system_owned": false,
  "_protection": "NOT_PROTECTED",
  "_create_time": 1760689221336,
  "_create_user": "wcp-cluster-user-f06fd228-8088-4439-a9e6-26c90a829c57-d34133d7-0fdf-4c9d-abcf-df83bd050a59",
  "_last_modified_time": 1760689221336,
  "_last_modified_user": "wcp-cluster-user-f06fd228-8088-4439-a9e6-26c90a829c57-d34133d7-0fdf-4c9d-abcf-df83bd050a59",
  "_revision": 0
}
```
<a id="225-policy-api-v1-orgs-default-projects-project-quality-vpcs-test-lb-50fedbb3-mv836-vpc-lb-pools-default-svc-80-mv836-rmigv"></a>
### 225. /policy/api/v1/orgs/default/projects/project-quality/vpcs/test-lb-50fedbb3_mv836/vpc-lb-pools/default-svc_80_mv836_rmigv

**HTTP Methods:** DELETE, GET, PATCH

**Explanation:**
VPC (Virtual Private Cloud) management within a project. Manages isolated network environments for workloads.

---


**Sample Response Body (GET, from logs):**
```json
{
  "algorithm": "ROUND_ROBIN",
  "snat_translation": {
    "type": "LBSnatAutoMap"
  },
  "min_active_members": 1,
  "resource_type": "LBPool",
  "id": "default-svc_80_mv836_rmigv",
  "display_name": "default-svc_80",
  "tags": [
    {
      "scope": "ncp/version",
      "tag": "1.2.0"
    },
    {
      "scope": "ncp/cluster",
      "tag": "f06fd228-8088-4439-a9e6-26c90a829c57"
    },
    {
      "scope": "ncp/project",
      "tag": "test-lb-50fedbb3"
    },
    {
      "scope": "external_id",
      "tag": "413462da-ad49-4afb-b755-88770ab32637"
    },
    {
      "scope": "ncp/service",
      "tag": "default-svc"
    },
    {
      "scope": "ncp/service_port",
      "tag": "80"
    },
    {
      "scope": "ncp/service_uid",
      "tag": "413462da-ad49-4afb-b755-88770ab32637"
    },
    {
      "scope": "ncp/created_for",
      "tag": "SLB"
    },
    {
      "scope": "ncp/service_port_protocol",
      "tag": "UDP"
    }
  ],
  "path": "/orgs/default/projects/project-quality/vpcs/test-lb-50fedbb3_mv836/vpc-lb-pools/default-svc_80_mv836_rmigv",
  "relative_path": "default-svc_80_mv836_rmigv",
  "parent_path": "/orgs/default/projects/project-quality/vpcs/test-lb-50fedbb3_mv836",
  "remote_path": "",
  "unique_id": "8210c6e4-f0b0-4b4b-8e76-b76cabe51f35",
  "realization_id": "8210c6e4-f0b0-4b4b-8e76-b76cabe51f35",
  "owner_id": "42495ba4-8c0b-49c9-b645-84cc39c2df30",
  "marked_for_delete": false,
  "overridden": false,
  "_system_owned": false,
  "_protection": "NOT_PROTECTED",
  "_create_time": 1760689223749,
  "_create_user": "wcp-cluster-user-f06fd228-8088-4439-a9e6-26c90a829c57-d34133d7-0fdf-4c9d-abcf-df83bd050a59",
  "_last_modified_time": 1760689223749,
  "_last_modified_user": "wcp-cluster-user-f06fd228-8088-4439-a9e6-26c90a829c57-d34133d7-0fdf-4c9d-abcf-df83bd050a59",
  "_revision": 0
}
```
<a id="226-policy-api-v1-orgs-default-projects-project-quality-vpcs-test-security-policy-add-delete-0e034260-aruoj-vpc-lbs-default"></a>
### 226. /policy/api/v1/orgs/default/projects/project-quality/vpcs/test-security-policy-add-delete-0e034260_aruoj/vpc-lbs/default

**HTTP Methods:** GET

**Explanation:**
VPC (Virtual Private Cloud) management within a project. Manages isolated network environments for workloads.

---


**Sample Response Body (GET, from logs):**
```json
{
  "connectivity_path": "/orgs/default/projects/project-quality/vpcs/test-security-policy-add-delete-0e034260_aruoj",
  "enabled": true,
  "relax_scale_validation": true,
  "size": "SMALL",
  "error_log_level": "INFO",
  "resource_type": "LBService",
  "id": "default",
  "display_name": "default",
  "tags": [
    {
      "scope": "nsx-op/cluster",
      "tag": "f06fd228-8088-4439-a9e6-26c90a829c57"
    },
    {
      "scope": "nsx-op/version",
      "tag": "1.0.0"
    },
    {
      "scope": "nsx-op/namespace",
      "tag": "test-security-policy-add-delete-0e034260"
    },
    {
      "scope": "nsx-op/namespace_uid",
      "tag": "ccfa2571-0d62-46e3-b588-89af3e040cda"
    },
    {
      "scope": "nsx-op/created_for",
      "tag": "SLB"
    }
  ],
  "path": "/orgs/default/projects/project-quality/vpcs/test-security-policy-add-delete-0e034260_aruoj/vpc-lbs/default",
  "relative_path": "default",
  "parent_path": "/orgs/default/projects/project-quality/vpcs/test-security-policy-add-delete-0e034260_aruoj",
  "remote_path": "",
  "unique_id": "f039dc3b-e918-4faf-be27-659e328bd69e",
  "realization_id": "f039dc3b-e918-4faf-be27-659e328bd69e",
  "owner_id": "42495ba4-8c0b-49c9-b645-84cc39c2df30",
  "marked_for_delete": false,
  "overridden": false,
  "_system_owned": false,
  "_protection": "NOT_PROTECTED",
  "_create_time": 1760689672512,
  "_create_user": "wcp-cluster-user-f06fd228-8088-4439-a9e6-26c90a829c57-d34133d7-0fdf-4c9d-abcf-df83bd050a59",
  "_last_modified_time": 1760689672512,
  "_last_modified_user": "wcp-cluster-user-f06fd228-8088-4439-a9e6-26c90a829c57-d34133d7-0fdf-4c9d-abcf-df83bd050a59",
  "_revision": 0
}
```
<a id="227-policy-api-v1-orgs-default-projects-project-quality-vpcs-test-security-policy-client-3a06d660-qiyvu-attachments-default"></a>
### 227. /policy/api/v1/orgs/default/projects/project-quality/vpcs/test-security-policy-client-3a06d660_qiyvu/attachments/default

**HTTP Methods:** GET

**Explanation:**
VPC (Virtual Private Cloud) management within a project. Manages isolated network environments for workloads.

---

<a id="228-policy-api-v1-orgs-default-projects-project-quality-vpcs-test-create-vm-basic-f449d9bf-3ehn6-subnets-public-subnet-3ehn6"></a>
### 228. /policy/api/v1/orgs/default/projects/project-quality/vpcs/test-create-vm-basic-f449d9bf_3ehn6/subnets/public-subnet_3ehn6

**HTTP Methods:** DELETE, GET, PATCH

**Explanation:**
VPC subnet management within a project. Defines IP address ranges and network segments for VPC workloads.

**Request Body (PATCH):**
```json
{
  "access_mode": "Public",
  "advanced_config": {
    "connectivity_state": "CONNECTED",
    "static_ip_allocation": {
      "enabled": true
    }
  },
  "display_name": "public-subnet_3ehn6",
  "id": "public-subnet_3ehn6",
  "ipv4_subnet_size": 16,
  "subnet_dhcp_config": {
    "mode": "DHCP_DEACTIVATED"
  },
  "tags": [
    {
      "scope": "nsx-op/cluster",
      "tag": "f06fd228-8088-4439-a9e6-26c90a829c57"
    },
    {
      "scope": "nsx-op/version",
      "tag": "1.0.0"
    },
    {
      "scope": "nsx-op/subnet_name",
      "tag": "public-subnet"
    },
    {
      "scope": "nsx-op/subnet_uid",
      "tag": "9d0090bd-9f6e-4115-850b-07b3e7d1f636"
    },
    {
      "scope": "nsx/managed-by",
      "tag": "nsx-op"
    },
    {
      "scope": "nsx-op/vm_namespace_uid",
      "tag": "1d6f2e6e-f228-4ddc-87b3-b99608fd4766"
    },
    {
      "scope": "nsx-op/vm_namespace",
      "tag": "test-create-vm-basic-f449d9bf"
    },
    {
      "scope": "kubernetes.io/metadata.name",
      "tag": "test-create-vm-basic-f449d9bf"
    },
    {
      "scope": "vSphereClusterID",
      "tag": "f06fd228-8088-4439-a9e6-26c90a829c57"
    }
  ]
}
```

---

<a id="229-policy-api-v1-orgs-default-projects-project-quality-vpcs-test-pod-sync-e8b8a7ca-m404i-subnets-pod-default-0dd88421-m404i"></a>
### 229. /policy/api/v1/orgs/default/projects/project-quality/vpcs/test-pod-sync-e8b8a7ca_m404i/subnets/pod-default-0dd88421_m404i

**HTTP Methods:** DELETE, GET, PATCH

**Explanation:**
VPC subnet management within a project. Defines IP address ranges and network segments for VPC workloads.

**Request Body (PATCH):**
```json
{
  "access_mode": "Private_TGW",
  "advanced_config": {
    "static_ip_allocation": {
      "enabled": true
    }
  },
  "display_name": "pod-default-0dd88421_m404i",
  "id": "pod-default-0dd88421_m404i",
  "ipv4_subnet_size": 16,
  "subnet_dhcp_config": {
    "mode": "DHCP_DEACTIVATED"
  },
  "tags": [
    {
      "scope": "nsx-op/cluster",
      "tag": "f06fd228-8088-4439-a9e6-26c90a829c57"
    },
    {
      "scope": "nsx-op/version",
      "tag": "1.0.0"
    },
    {
      "scope": "nsx-op/subnetset_name",
      "tag": "pod-default"
    },
    {
      "scope": "nsx-op/subnetset_uid",
      "tag": "119d0146-c8ff-4c75-b284-38be788c0816"
    },
    {
      "scope": "nsx/managed-by",
      "tag": "nsx-op"
    },
    {
      "scope": "nsx-op/namespace_uid",
      "tag": "df28714f-bbd0-4ac5-bfaa-13716c242ac0"
    },
    {
      "scope": "nsx-op/namespace",
      "tag": "test-pod-sync-e8b8a7ca"
    },
    {
      "scope": "kubernetes.io/metadata.name",
      "tag": "test-pod-sync-e8b8a7ca"
    },
    {
      "scope": "vSphereClusterID",
      "tag": "f06fd228-8088-4439-a9e6-26c90a829c57"
    }
  ]
}
```

---

<a id="230-policy-api-v1-orgs-default-projects-project-quality-vpcs-precreated-subnet-ns1-a72a2a9d-8m6zu-subnets-normal-subnet-8m6zu"></a>
### 230. /policy/api/v1/orgs/default/projects/project-quality/vpcs/precreated-subnet-ns1-a72a2a9d_8m6zu/subnets/normal-subnet_8m6zu

**HTTP Methods:** DELETE, GET, PATCH

**Explanation:**
VPC subnet management within a project. Defines IP address ranges and network segments for VPC workloads.

**Request Body (PATCH):**
```json
{
  "access_mode": "Private",
  "advanced_config": {
    "connectivity_state": "CONNECTED",
    "static_ip_allocation": {
      "enabled": true
    }
  },
  "display_name": "normal-subnet_8m6zu",
  "id": "normal-subnet_8m6zu",
  "ipv4_subnet_size": 16,
  "subnet_dhcp_config": {
    "mode": "DHCP_DEACTIVATED"
  },
  "tags": [
    {
      "scope": "nsx-op/cluster",
      "tag": "f06fd228-8088-4439-a9e6-26c90a829c57"
    },
    {
      "scope": "nsx-op/version",
      "tag": "1.0.0"
    },
    {
      "scope": "nsx-op/subnet_name",
      "tag": "normal-subnet"
    },
    {
      "scope": "nsx-op/subnet_uid",
      "tag": "f2f051b4-3cae-4961-8b37-181e0e301faf"
    },
    {
      "scope": "nsx/managed-by",
      "tag": "nsx-op"
    },
    {
      "scope": "nsx-op/vm_namespace_uid",
      "tag": "fb0c2f0a-e4cf-4742-b860-68261f4ac40b"
    },
    {
      "scope": "nsx-op/vm_namespace",
      "tag": "precreated-subnet-ns1-a72a2a9d"
    },
    {
      "scope": "kubernetes.io/metadata.name",
      "tag": "precreated-subnet-ns1-a72a2a9d"
    },
    {
      "scope": "vSphereClusterID",
      "tag": "f06fd228-8088-4439-a9e6-26c90a829c57"
    }
  ]
}
```

---

<a id="231-policy-api-v1-orgs-default-projects-project-quality-vpcs-test-lb-50fedbb3-mv836-vpc-lb-virtual-servers-tea-svc-80-tcp-39r0c"></a>
### 231. /policy/api/v1/orgs/default/projects/project-quality/vpcs/test-lb-50fedbb3_mv836/vpc-lb-virtual-servers/tea-svc_80_TCP_39r0c

**HTTP Methods:** DELETE, GET, PATCH

**Explanation:**
VPC (Virtual Private Cloud) management within a project. Manages isolated network environments for workloads.

---


**Sample Response Body (GET, from logs):**
```json
{
  "enabled": true,
  "ip_address": "192.168.0.9",
  "ports": [
    "80"
  ],
  "access_log_enabled": false,
  "lb_persistence_profile_path": "",
  "lb_service_path": "/orgs/default/projects/project-quality/vpcs/test-lb-50fedbb3_mv836/vpc-lbs/default",
  "pool_path": "/orgs/default/projects/project-quality/vpcs/test-lb-50fedbb3_mv836/vpc-lb-pools/tea-svc_80_mv836_xirvk",
  "application_profile_path": "/infra/lb-app-profiles/ncp_f06fd228-8088-4439-a9e6-26c90a829c57_LBFastTcpProfile",
  "log_significant_event_only": false,
  "resource_type": "LBVirtualServer",
  "id": "tea-svc_80_TCP_39r0c",
  "display_name": "tea-svc_80_TCP",
  "tags": [
    {
      "scope": "ncp/version",
      "tag": "1.2.0"
    },
    {
      "scope": "ncp/cluster",
      "tag": "f06fd228-8088-4439-a9e6-26c90a829c57"
    },
    {
      "scope": "ncp/service_uid",
      "tag": "f8572ed6-448c-4830-8e1d-5c00326ab97f"
    },
    {
      "scope": "ncp/lb_vs_type",
      "tag": "layer_4"
    },
    {
      "scope": "ncp/created_for",
      "tag": "SLB"
    },
    {
      "scope": "external_id",
      "tag": "f8572ed6-448c-4830-8e1d-5c00326ab97f"
    },
    {
      "scope": "ncp/service_port_protocol",
      "tag": "TCP"
    }
  ],
  "path": "/orgs/default/projects/project-quality/vpcs/test-lb-50fedbb3_mv836/vpc-lb-virtual-servers/tea-svc_80_TCP_39r0c",
  "relative_path": "tea-svc_80_TCP_39r0c",
  "parent_path": "/orgs/default/projects/project-quality/vpcs/test-lb-50fedbb3_mv836",
  "remote_path": "",
  "unique_id": "9553b76d-86eb-40ad-a047-77afcd574dd2",
  "realization_id": "9553b76d-86eb-40ad-a047-77afcd574dd2",
  "owner_id": "42495ba4-8c0b-49c9-b645-84cc39c2df30",
  "marked_for_delete": false,
  "overridden": false,
  "_system_owned": false,
  "_protection": "NOT_PROTECTED",
  "_create_time": 1760689215007,
  "_create_user": "wcp-cluster-user-f06fd228-8088-4439-a9e6-26c90a829c57-d34133d7-0fdf-4c9d-abcf-df83bd050a59",
  "_last_modified_time": 1760689215007,
  "_last_modified_user": "wcp-cluster-user-f06fd228-8088-4439-a9e6-26c90a829c57-d34133d7-0fdf-4c9d-abcf-df83bd050a59",
  "_revision": 0
}
```
<a id="232-policy-api-v1-orgs-default-projects-project-quality-vpcs-test-lb-50fedbb3-mv836-vpc-lb-virtual-servers-tea-svc-80-udp-39r0c"></a>
### 232. /policy/api/v1/orgs/default/projects/project-quality/vpcs/test-lb-50fedbb3_mv836/vpc-lb-virtual-servers/tea-svc_80_UDP_39r0c

**HTTP Methods:** DELETE, GET, PATCH

**Explanation:**
VPC (Virtual Private Cloud) management within a project. Manages isolated network environments for workloads.

---


**Sample Response Body (GET, from logs):**
```json
{
  "enabled": true,
  "ip_address": "192.168.0.9",
  "ports": [
    "80"
  ],
  "access_log_enabled": false,
  "lb_persistence_profile_path": "",
  "lb_service_path": "/orgs/default/projects/project-quality/vpcs/test-lb-50fedbb3_mv836/vpc-lbs/default",
  "pool_path": "/orgs/default/projects/project-quality/vpcs/test-lb-50fedbb3_mv836/vpc-lb-pools/tea-svc_80_mv836_scsoh",
  "application_profile_path": "/infra/lb-app-profiles/ncp_f06fd228-8088-4439-a9e6-26c90a829c57_LBFastUdpProfile",
  "log_significant_event_only": false,
  "resource_type": "LBVirtualServer",
  "id": "tea-svc_80_UDP_39r0c",
  "display_name": "tea-svc_80_UDP",
  "tags": [
    {
      "scope": "ncp/version",
      "tag": "1.2.0"
    },
    {
      "scope": "ncp/cluster",
      "tag": "f06fd228-8088-4439-a9e6-26c90a829c57"
    },
    {
      "scope": "ncp/service_uid",
      "tag": "f8572ed6-448c-4830-8e1d-5c00326ab97f"
    },
    {
      "scope": "ncp/lb_vs_type",
      "tag": "layer_4"
    },
    {
      "scope": "ncp/created_for",
      "tag": "SLB"
    },
    {
      "scope": "external_id",
      "tag": "f8572ed6-448c-4830-8e1d-5c00326ab97f"
    },
    {
      "scope": "ncp/service_port_protocol",
      "tag": "UDP"
    }
  ],
  "path": "/orgs/default/projects/project-quality/vpcs/test-lb-50fedbb3_mv836/vpc-lb-virtual-servers/tea-svc_80_UDP_39r0c",
  "relative_path": "tea-svc_80_UDP_39r0c",
  "parent_path": "/orgs/default/projects/project-quality/vpcs/test-lb-50fedbb3_mv836",
  "remote_path": "",
  "unique_id": "9446c002-010f-42b1-906f-c0cde9fe2331",
  "realization_id": "9446c002-010f-42b1-906f-c0cde9fe2331",
  "owner_id": "42495ba4-8c0b-49c9-b645-84cc39c2df30",
  "marked_for_delete": false,
  "overridden": false,
  "_system_owned": false,
  "_protection": "NOT_PROTECTED",
  "_create_time": 1760689218718,
  "_create_user": "wcp-cluster-user-f06fd228-8088-4439-a9e6-26c90a829c57-d34133d7-0fdf-4c9d-abcf-df83bd050a59",
  "_last_modified_time": 1760689218718,
  "_last_modified_user": "wcp-cluster-user-f06fd228-8088-4439-a9e6-26c90a829c57-d34133d7-0fdf-4c9d-abcf-df83bd050a59",
  "_revision": 0
}
```
<a id="233-policy-api-v1-orgs-default-projects-project-quality-vpcs-test-security-policy-add-delete-0e034260-aruoj-attachments-default"></a>
### 233. /policy/api/v1/orgs/default/projects/project-quality/vpcs/test-security-policy-add-delete-0e034260_aruoj/attachments/default

**HTTP Methods:** GET

**Explanation:**
VPC (Virtual Private Cloud) management within a project. Manages isolated network environments for workloads.

---

<a id="234-policy-api-v1-orgs-default-projects-project-quality-vpcs-testvpc-3658f2b5-vpc-lb-pools-prevpc-loadbalancer-8080-d5d7u-icdrq"></a>
### 234. /policy/api/v1/orgs/default/projects/project-quality/vpcs/testvpc-3658f2b5/vpc-lb-pools/prevpc-loadbalancer_8080_d5d7u_icdrq

**HTTP Methods:** DELETE, GET, PATCH

**Explanation:**
VPC (Virtual Private Cloud) management within a project. Manages isolated network environments for workloads.

---


**Sample Response Body (GET, from logs):**
```json
{
  "algorithm": "ROUND_ROBIN",
  "snat_translation": {
    "type": "LBSnatAutoMap"
  },
  "min_active_members": 1,
  "resource_type": "LBPool",
  "id": "prevpc-loadbalancer_8080_d5d7u_icdrq",
  "display_name": "prevpc-loadbalancer_8080",
  "tags": [
    {
      "scope": "ncp/version",
      "tag": "1.2.0"
    },
    {
      "scope": "ncp/cluster",
      "tag": "f06fd228-8088-4439-a9e6-26c90a829c57"
    },
    {
      "scope": "ncp/project",
      "tag": "test-prevpc-8f1a464f"
    },
    {
      "scope": "external_id",
      "tag": "64af7175-c755-4315-9cf7-28c21bd6fc0a"
    },
    {
      "scope": "ncp/service",
      "tag": "prevpc-loadbalancer"
    },
    {
      "scope": "ncp/service_port",
      "tag": "8080"
    },
    {
      "scope": "ncp/service_uid",
      "tag": "64af7175-c755-4315-9cf7-28c21bd6fc0a"
    },
    {
      "scope": "ncp/created_for",
      "tag": "SLB"
    },
    {
      "scope": "ncp/service_port_protocol",
      "tag": "TCP"
    }
  ],
  "path": "/orgs/default/projects/project-quality/vpcs/testvpc-3658f2b5/vpc-lb-pools/prevpc-loadbalancer_8080_d5d7u_icdrq",
  "relative_path": "prevpc-loadbalancer_8080_d5d7u_icdrq",
  "parent_path": "/orgs/default/projects/project-quality/vpcs/testvpc-3658f2b5",
  "remote_path": "",
  "unique_id": "5aa49152-59f8-4027-84dc-5d824be9fc73",
  "realization_id": "5aa49152-59f8-4027-84dc-5d824be9fc73",
  "owner_id": "42495ba4-8c0b-49c9-b645-84cc39c2df30",
  "marked_for_delete": false,
  "overridden": false,
  "_system_owned": false,
  "_protection": "NOT_PROTECTED",
  "_create_time": 1760690632559,
  "_create_user": "wcp-cluster-user-f06fd228-8088-4439-a9e6-26c90a829c57-d34133d7-0fdf-4c9d-abcf-df83bd050a59",
  "_last_modified_time": 1760690632559,
  "_last_modified_user": "wcp-cluster-user-f06fd228-8088-4439-a9e6-26c90a829c57-d34133d7-0fdf-4c9d-abcf-df83bd050a59",
  "_revision": 0
}
```
<a id="235-policy-api-v1-orgs-default-projects-project-quality-vpcs-subnet-e2e-1f11082b-56qvy-subnets-user-subnetset-dhcp-c85186d8-56qvy"></a>
### 235. /policy/api/v1/orgs/default/projects/project-quality/vpcs/subnet-e2e-1f11082b_56qvy/subnets/user-subnetset-dhcp-c85186d8_56qvy

**HTTP Methods:** DELETE, GET, PATCH

**Explanation:**
VPC subnet management within a project. Defines IP address ranges and network segments for VPC workloads.

**Request Body (PATCH):**
```json
{
  "access_mode": "Private_TGW",
  "advanced_config": {
    "static_ip_allocation": {
      "enabled": false
    }
  },
  "display_name": "user-subnetset-dhcp-c85186d8_56qvy",
  "id": "user-subnetset-dhcp-c85186d8_56qvy",
  "ipv4_subnet_size": 32,
  "subnet_dhcp_config": {
    "mode": "DHCP_SERVER"
  },
  "tags": [
    {
      "scope": "nsx-op/cluster",
      "tag": "f06fd228-8088-4439-a9e6-26c90a829c57"
    },
    {
      "scope": "nsx-op/version",
      "tag": "1.0.0"
    },
    {
      "scope": "nsx-op/subnetset_name",
      "tag": "user-subnetset-dhcp"
    },
    {
      "scope": "nsx-op/subnetset_uid",
      "tag": "aae60193-400f-4d7c-a2e1-f778fbcd9b83"
    },
    {
      "scope": "nsx/managed-by",
      "tag": "nsx-op"
    },
    {
      "scope": "nsx-op/vm_namespace_uid",
      "tag": "f629b82e-5ea2-4298-b1cf-3bafcea373fa"
    },
    {
      "scope": "nsx-op/vm_namespace",
      "tag": "subnet-e2e-1f11082b"
    },
    {
      "scope": "kubernetes.io/metadata.name",
      "tag": "subnet-e2e-1f11082b"
    }
  ]
}
```

---

<a id="236-policy-api-v1-orgs-default-projects-project-quality-vpcs-test-security-policy-match-expression-ff1dafa9-bgm74-vpc-lbs-default"></a>
### 236. /policy/api/v1/orgs/default/projects/project-quality/vpcs/test-security-policy-match-expression-ff1dafa9_bgm74/vpc-lbs/default

**HTTP Methods:** GET

**Explanation:**
VPC (Virtual Private Cloud) management within a project. Manages isolated network environments for workloads.

---


**Sample Response Body (GET, from logs):**
```json
{
  "connectivity_path": "/orgs/default/projects/project-quality/vpcs/test-security-policy-match-expression-ff1dafa9_bgm74",
  "enabled": true,
  "relax_scale_validation": true,
  "size": "SMALL",
  "error_log_level": "INFO",
  "resource_type": "LBService",
  "id": "default",
  "display_name": "default",
  "tags": [
    {
      "scope": "nsx-op/cluster",
      "tag": "f06fd228-8088-4439-a9e6-26c90a829c57"
    },
    {
      "scope": "nsx-op/version",
      "tag": "1.0.0"
    },
    {
      "scope": "nsx-op/namespace",
      "tag": "test-security-policy-match-expression-ff1dafa9"
    },
    {
      "scope": "nsx-op/namespace_uid",
      "tag": "3de47ade-81f0-4df6-b8fe-4bd50341d1b1"
    },
    {
      "scope": "nsx-op/created_for",
      "tag": "SLB"
    }
  ],
  "path": "/orgs/default/projects/project-quality/vpcs/test-security-policy-match-expression-ff1dafa9_bgm74/vpc-lbs/default",
  "relative_path": "default",
  "parent_path": "/orgs/default/projects/project-quality/vpcs/test-security-policy-match-expression-ff1dafa9_bgm74",
  "remote_path": "",
  "unique_id": "7ba32582-abf7-4595-91c4-1a582904a61d",
  "realization_id": "7ba32582-abf7-4595-91c4-1a582904a61d",
  "owner_id": "42495ba4-8c0b-49c9-b645-84cc39c2df30",
  "marked_for_delete": false,
  "overridden": false,
  "_system_owned": false,
  "_protection": "NOT_PROTECTED",
  "_create_time": 1760689706304,
  "_create_user": "wcp-cluster-user-f06fd228-8088-4439-a9e6-26c90a829c57-d34133d7-0fdf-4c9d-abcf-df83bd050a59",
  "_last_modified_time": 1760689706304,
  "_last_modified_user": "wcp-cluster-user-f06fd228-8088-4439-a9e6-26c90a829c57-d34133d7-0fdf-4c9d-abcf-df83bd050a59",
  "_revision": 0
}
```
<a id="237-policy-api-v1-orgs-default-projects-project-quality-vpcs-precreated-target-ns-3c7c1821-v5ml5-subnets-shared-subnet-892e2-v5ml5"></a>
### 237. /policy/api/v1/orgs/default/projects/project-quality/vpcs/precreated-target-ns-3c7c1821_v5ml5/subnets/shared-subnet-892e2_v5ml5

**HTTP Methods:** DELETE, GET, PATCH

**Explanation:**
VPC subnet management within a project. Defines IP address ranges and network segments for VPC workloads.

**Request Body (PATCH):**
```json
{
  "access_mode": "Private",
  "advanced_config": {
    "connectivity_state": "CONNECTED",
    "static_ip_allocation": {
      "enabled": true
    }
  },
  "display_name": "shared-subnet-892e2_v5ml5",
  "id": "shared-subnet-892e2_v5ml5",
  "ipv4_subnet_size": 16,
  "subnet_dhcp_config": {
    "mode": "DHCP_DEACTIVATED"
  },
  "tags": [
    {
      "scope": "nsx-op/cluster",
      "tag": "f06fd228-8088-4439-a9e6-26c90a829c57"
    },
    {
      "scope": "nsx-op/version",
      "tag": "1.0.0"
    },
    {
      "scope": "nsx-op/subnet_name",
      "tag": "shared-subnet-892e2"
    },
    {
      "scope": "nsx-op/subnet_uid",
      "tag": "cd1e1684-19aa-48f5-9f8a-a29dbc6f5f14"
    },
    {
      "scope": "nsx/managed-by",
      "tag": "nsx-op"
    },
    {
      "scope": "nsx-op/vm_namespace_uid",
      "tag": "a4d76189-c002-4514-9616-5265c71b7b8b"
    },
    {
      "scope": "nsx-op/vm_namespace",
      "tag": "precreated-target-ns-3c7c1821"
    },
    {
      "scope": "kubernetes.io/metadata.name",
      "tag": "precreated-target-ns-3c7c1821"
    },
    {
      "scope": "vSphereClusterID",
      "tag": "f06fd228-8088-4439-a9e6-26c90a829c57"
    }
  ]
}
```

---

<a id="238-policy-api-v1-orgs-default-projects-project-quality-vpcs-test-ipaddress-allocation-40d5699d-2p2tu-ip-address-allocations-p5j45"></a>
### 238. /policy/api/v1/orgs/default/projects/project-quality/vpcs/test-ipaddress-allocation-40d5699d_2p2tu/ip-address-allocations/p5j45

**HTTP Methods:** DELETE, GET, PATCH

**Explanation:**
VPC (Virtual Private Cloud) management within a project. Manages isolated network environments for workloads.

---


**Sample Response Body (GET, from logs):**
```json
{
  "ip_address_type": "IPV4",
  "ip_address_block_visibility": "EXTERNAL",
  "allocation_ip": "192.168.0.8",
  "allocation_ips": "192.168.0.8",
  "resource_type": "VpcIpAddressAllocation",
  "id": "p5j45",
  "display_name": "p5j45",
  "tags": [
    {
      "scope": "ncp/version",
      "tag": "1.2.0"
    },
    {
      "scope": "ncp/cluster",
      "tag": "f06fd228-8088-4439-a9e6-26c90a829c57"
    },
    {
      "scope": "ncp/service_uid",
      "tag": "55c7492b-a285-4cba-9d71-bb6305d8c977"
    },
    {
      "scope": "ncp/created_for",
      "tag": "l4_service"
    }
  ],
  "path": "/orgs/default/projects/project-quality/vpcs/test-ipaddress-allocation-40d5699d_2p2tu/ip-address-allocations/p5j45",
  "relative_path": "p5j45",
  "parent_path": "/orgs/default/projects/project-quality/vpcs/test-ipaddress-allocation-40d5699d_2p2tu",
  "remote_path": "",
  "unique_id": "cdb54123-15b3-4dfa-9cc5-312de6a7aadd",
  "realization_id": "cdb54123-15b3-4dfa-9cc5-312de6a7aadd",
  "owner_id": "42495ba4-8c0b-49c9-b645-84cc39c2df30",
  "marked_for_delete": false,
  "overridden": false,
  "_system_owned": false,
  "_protection": "NOT_PROTECTED",
  "_create_time": 1760689104732,
  "_create_user": "wcp-cluster-user-f06fd228-8088-4439-a9e6-26c90a829c57-d34133d7-0fdf-4c9d-abcf-df83bd050a59",
  "_last_modified_time": 1760689104732,
  "_last_modified_user": "wcp-cluster-user-f06fd228-8088-4439-a9e6-26c90a829c57-d34133d7-0fdf-4c9d-abcf-df83bd050a59",
  "_revision": 0
}
```
<a id="239-policy-api-v1-orgs-default-projects-project-quality-vpcs-test-lb-50fedbb3-mv836-vpc-lb-virtual-servers-coffee-svc-80-tcp-cnml1"></a>
### 239. /policy/api/v1/orgs/default/projects/project-quality/vpcs/test-lb-50fedbb3_mv836/vpc-lb-virtual-servers/coffee-svc_80_TCP_cnml1

**HTTP Methods:** DELETE, GET, PATCH

**Explanation:**
VPC (Virtual Private Cloud) management within a project. Manages isolated network environments for workloads.

---


**Sample Response Body (GET, from logs):**
```json
{
  "enabled": true,
  "ip_address": "192.168.0.12",
  "ports": [
    "80"
  ],
  "access_log_enabled": false,
  "lb_persistence_profile_path": "",
  "lb_service_path": "/orgs/default/projects/project-quality/vpcs/test-lb-50fedbb3_mv836/vpc-lbs/default",
  "pool_path": "/orgs/default/projects/project-quality/vpcs/test-lb-50fedbb3_mv836/vpc-lb-pools/coffee-svc_80_mv836_eyftl",
  "application_profile_path": "/infra/lb-app-profiles/ncp_f06fd228-8088-4439-a9e6-26c90a829c57_LBFastTcpProfile",
  "log_significant_event_only": false,
  "resource_type": "LBVirtualServer",
  "id": "coffee-svc_80_TCP_cnml1",
  "display_name": "coffee-svc_80_TCP",
  "tags": [
    {
      "scope": "ncp/version",
      "tag": "1.2.0"
    },
    {
      "scope": "ncp/cluster",
      "tag": "f06fd228-8088-4439-a9e6-26c90a829c57"
    },
    {
      "scope": "ncp/service_uid",
      "tag": "75a666bb-cb7a-45dd-a6a6-6d0f0e7d685e"
    },
    {
      "scope": "ncp/lb_vs_type",
      "tag": "layer_4"
    },
    {
      "scope": "ncp/created_for",
      "tag": "SLB"
    },
    {
      "scope": "external_id",
      "tag": "75a666bb-cb7a-45dd-a6a6-6d0f0e7d685e"
    },
    {
      "scope": "ncp/service_port_protocol",
      "tag": "TCP"
    }
  ],
  "path": "/orgs/default/projects/project-quality/vpcs/test-lb-50fedbb3_mv836/vpc-lb-virtual-servers/coffee-svc_80_TCP_cnml1",
  "relative_path": "coffee-svc_80_TCP_cnml1",
  "parent_path": "/orgs/default/projects/project-quality/vpcs/test-lb-50fedbb3_mv836",
  "remote_path": "",
  "unique_id": "e0125ced-c8fc-4ad4-a4c7-439c42aee614",
  "realization_id": "e0125ced-c8fc-4ad4-a4c7-439c42aee614",
  "owner_id": "42495ba4-8c0b-49c9-b645-84cc39c2df30",
  "marked_for_delete": false,
  "overridden": false,
  "_system_owned": false,
  "_protection": "NOT_PROTECTED",
  "_create_time": 1760689288275,
  "_create_user": "wcp-cluster-user-f06fd228-8088-4439-a9e6-26c90a829c57-d34133d7-0fdf-4c9d-abcf-df83bd050a59",
  "_last_modified_time": 1760689288275,
  "_last_modified_user": "wcp-cluster-user-f06fd228-8088-4439-a9e6-26c90a829c57-d34133d7-0fdf-4c9d-abcf-df83bd050a59",
  "_revision": 0
}
```
<a id="240-policy-api-v1-orgs-default-projects-project-quality-vpcs-web-da775e6f-6o7ts-security-policies-named-port-policy-with-pod-d3qx0"></a>
### 240. /policy/api/v1/orgs/default/projects/project-quality/vpcs/web-da775e6f_6o7ts/security-policies/named-port-policy-with-pod_d3qx0

**HTTP Methods:** DELETE, GET

**Explanation:**
VPC (Virtual Private Cloud) management within a project. Manages isolated network environments for workloads.

---

<a id="241-policy-api-v1-orgs-default-projects-project-quality-vpcs-subnet-e2e-1f11082b-56qvy-subnets-user-subnetset-static-948a4c45-56qvy"></a>
### 241. /policy/api/v1/orgs/default/projects/project-quality/vpcs/subnet-e2e-1f11082b_56qvy/subnets/user-subnetset-static-948a4c45_56qvy

**HTTP Methods:** DELETE, GET, PATCH

**Explanation:**
VPC subnet management within a project. Defines IP address ranges and network segments for VPC workloads.

**Request Body (PATCH):**
```json
{
  "access_mode": "Private",
  "advanced_config": {
    "static_ip_allocation": {
      "enabled": true
    }
  },
  "display_name": "user-subnetset-static-948a4c45_56qvy",
  "id": "user-subnetset-static-948a4c45_56qvy",
  "ipv4_subnet_size": 32,
  "subnet_dhcp_config": {
    "mode": "DHCP_DEACTIVATED"
  },
  "tags": [
    {
      "scope": "nsx-op/cluster",
      "tag": "f06fd228-8088-4439-a9e6-26c90a829c57"
    },
    {
      "scope": "nsx-op/version",
      "tag": "1.0.0"
    },
    {
      "scope": "nsx-op/subnetset_name",
      "tag": "user-subnetset-static"
    },
    {
      "scope": "nsx-op/subnetset_uid",
      "tag": "8a69d8ac-a5a1-4d05-9c50-dd8092018b34"
    },
    {
      "scope": "nsx/managed-by",
      "tag": "nsx-op"
    },
    {
      "scope": "nsx-op/vm_namespace_uid",
      "tag": "f629b82e-5ea2-4298-b1cf-3bafcea373fa"
    },
    {
      "scope": "nsx-op/vm_namespace",
      "tag": "subnet-e2e-1f11082b"
    },
    {
      "scope": "kubernetes.io/metadata.name",
      "tag": "subnet-e2e-1f11082b"
    }
  ]
}
```

---

<a id="242-policy-api-v1-orgs-default-projects-project-quality-vpcs-test-lb-50fedbb3-mv836-vpc-lb-virtual-servers-default-svc-80-tcp-i3q14"></a>
### 242. /policy/api/v1/orgs/default/projects/project-quality/vpcs/test-lb-50fedbb3_mv836/vpc-lb-virtual-servers/default-svc_80_TCP_i3q14

**HTTP Methods:** DELETE, GET, PATCH

**Explanation:**
VPC (Virtual Private Cloud) management within a project. Manages isolated network environments for workloads.

---


**Sample Response Body (GET, from logs):**
```json
{
  "enabled": true,
  "ip_address": "192.168.0.10",
  "ports": [
    "80"
  ],
  "access_log_enabled": false,
  "lb_persistence_profile_path": "",
  "lb_service_path": "/orgs/default/projects/project-quality/vpcs/test-lb-50fedbb3_mv836/vpc-lbs/default",
  "pool_path": "/orgs/default/projects/project-quality/vpcs/test-lb-50fedbb3_mv836/vpc-lb-pools/default-svc_80_mv836_iszzt",
  "application_profile_path": "/infra/lb-app-profiles/ncp_f06fd228-8088-4439-a9e6-26c90a829c57_LBFastTcpProfile",
  "log_significant_event_only": false,
  "resource_type": "LBVirtualServer",
  "id": "default-svc_80_TCP_i3q14",
  "display_name": "default-svc_80_TCP",
  "tags": [
    {
      "scope": "ncp/version",
      "tag": "1.2.0"
    },
    {
      "scope": "ncp/cluster",
      "tag": "f06fd228-8088-4439-a9e6-26c90a829c57"
    },
    {
      "scope": "ncp/service_uid",
      "tag": "413462da-ad49-4afb-b755-88770ab32637"
    },
    {
      "scope": "ncp/lb_vs_type",
      "tag": "layer_4"
    },
    {
      "scope": "ncp/created_for",
      "tag": "SLB"
    },
    {
      "scope": "external_id",
      "tag": "413462da-ad49-4afb-b755-88770ab32637"
    },
    {
      "scope": "ncp/service_port_protocol",
      "tag": "TCP"
    }
  ],
  "path": "/orgs/default/projects/project-quality/vpcs/test-lb-50fedbb3_mv836/vpc-lb-virtual-servers/default-svc_80_TCP_i3q14",
  "relative_path": "default-svc_80_TCP_i3q14",
  "parent_path": "/orgs/default/projects/project-quality/vpcs/test-lb-50fedbb3_mv836",
  "remote_path": "",
  "unique_id": "2a5c2ce0-af50-4154-bd39-c109448b3409",
  "realization_id": "2a5c2ce0-af50-4154-bd39-c109448b3409",
  "owner_id": "42495ba4-8c0b-49c9-b645-84cc39c2df30",
  "marked_for_delete": false,
  "overridden": false,
  "_system_owned": false,
  "_protection": "NOT_PROTECTED",
  "_create_time": 1760689222554,
  "_create_user": "wcp-cluster-user-f06fd228-8088-4439-a9e6-26c90a829c57-d34133d7-0fdf-4c9d-abcf-df83bd050a59",
  "_last_modified_time": 1760689222554,
  "_last_modified_user": "wcp-cluster-user-f06fd228-8088-4439-a9e6-26c90a829c57-d34133d7-0fdf-4c9d-abcf-df83bd050a59",
  "_revision": 0
}
```
<a id="243-policy-api-v1-orgs-default-projects-project-quality-vpcs-test-lb-50fedbb3-mv836-vpc-lb-virtual-servers-default-svc-80-udp-i3q14"></a>
### 243. /policy/api/v1/orgs/default/projects/project-quality/vpcs/test-lb-50fedbb3_mv836/vpc-lb-virtual-servers/default-svc_80_UDP_i3q14

**HTTP Methods:** DELETE, GET, PATCH

**Explanation:**
VPC (Virtual Private Cloud) management within a project. Manages isolated network environments for workloads.

---


**Sample Response Body (GET, from logs):**
```json
{
  "enabled": true,
  "ip_address": "192.168.0.10",
  "ports": [
    "80"
  ],
  "access_log_enabled": false,
  "lb_persistence_profile_path": "",
  "lb_service_path": "/orgs/default/projects/project-quality/vpcs/test-lb-50fedbb3_mv836/vpc-lbs/default",
  "pool_path": "/orgs/default/projects/project-quality/vpcs/test-lb-50fedbb3_mv836/vpc-lb-pools/default-svc_80_mv836_rmigv",
  "application_profile_path": "/infra/lb-app-profiles/ncp_f06fd228-8088-4439-a9e6-26c90a829c57_LBFastUdpProfile",
  "log_significant_event_only": false,
  "resource_type": "LBVirtualServer",
  "id": "default-svc_80_UDP_i3q14",
  "display_name": "default-svc_80_UDP",
  "tags": [
    {
      "scope": "ncp/version",
      "tag": "1.2.0"
    },
    {
      "scope": "ncp/cluster",
      "tag": "f06fd228-8088-4439-a9e6-26c90a829c57"
    },
    {
      "scope": "ncp/service_uid",
      "tag": "413462da-ad49-4afb-b755-88770ab32637"
    },
    {
      "scope": "ncp/lb_vs_type",
      "tag": "layer_4"
    },
    {
      "scope": "ncp/created_for",
      "tag": "SLB"
    },
    {
      "scope": "external_id",
      "tag": "413462da-ad49-4afb-b755-88770ab32637"
    },
    {
      "scope": "ncp/service_port_protocol",
      "tag": "UDP"
    }
  ],
  "path": "/orgs/default/projects/project-quality/vpcs/test-lb-50fedbb3_mv836/vpc-lb-virtual-servers/default-svc_80_UDP_i3q14",
  "relative_path": "default-svc_80_UDP_i3q14",
  "parent_path": "/orgs/default/projects/project-quality/vpcs/test-lb-50fedbb3_mv836",
  "remote_path": "",
  "unique_id": "4772218a-252e-4e2d-829d-46f4ff5ef549",
  "realization_id": "4772218a-252e-4e2d-829d-46f4ff5ef549",
  "owner_id": "42495ba4-8c0b-49c9-b645-84cc39c2df30",
  "marked_for_delete": false,
  "overridden": false,
  "_system_owned": false,
  "_protection": "NOT_PROTECTED",
  "_create_time": 1760689224807,
  "_create_user": "wcp-cluster-user-f06fd228-8088-4439-a9e6-26c90a829c57-d34133d7-0fdf-4c9d-abcf-df83bd050a59",
  "_last_modified_time": 1760689224807,
  "_last_modified_user": "wcp-cluster-user-f06fd228-8088-4439-a9e6-26c90a829c57-d34133d7-0fdf-4c9d-abcf-df83bd050a59",
  "_revision": 0
}
```
<a id="244-policy-api-v1-orgs-default-projects-project-quality-vpcs-precreated-target-ns-3c7c1821-v5ml5-subnets-shared-subnet-2-421d2-v5ml5"></a>
### 244. /policy/api/v1/orgs/default/projects/project-quality/vpcs/precreated-target-ns-3c7c1821_v5ml5/subnets/shared-subnet-2-421d2_v5ml5

**HTTP Methods:** DELETE, GET, PATCH

**Explanation:**
VPC subnet management within a project. Defines IP address ranges and network segments for VPC workloads.

**Request Body (PATCH):**
```json
{
  "access_mode": "Private",
  "advanced_config": {
    "connectivity_state": "CONNECTED",
    "static_ip_allocation": {
      "enabled": true
    }
  },
  "display_name": "shared-subnet-2-421d2_v5ml5",
  "id": "shared-subnet-2-421d2_v5ml5",
  "ipv4_subnet_size": 16,
  "subnet_dhcp_config": {
    "mode": "DHCP_DEACTIVATED"
  },
  "tags": [
    {
      "scope": "nsx-op/cluster",
      "tag": "f06fd228-8088-4439-a9e6-26c90a829c57"
    },
    {
      "scope": "nsx-op/version",
      "tag": "1.0.0"
    },
    {
      "scope": "nsx-op/subnet_name",
      "tag": "shared-subnet-2-421d2"
    },
    {
      "scope": "nsx-op/subnet_uid",
      "tag": "c352d81e-e34d-4a06-bcea-92ec6d09700b"
    },
    {
      "scope": "nsx/managed-by",
      "tag": "nsx-op"
    },
    {
      "scope": "nsx-op/vm_namespace_uid",
      "tag": "a4d76189-c002-4514-9616-5265c71b7b8b"
    },
    {
      "scope": "nsx-op/vm_namespace",
      "tag": "precreated-target-ns-3c7c1821"
    },
    {
      "scope": "kubernetes.io/metadata.name",
      "tag": "precreated-target-ns-3c7c1821"
    },
    {
      "scope": "vSphereClusterID",
      "tag": "f06fd228-8088-4439-a9e6-26c90a829c57"
    }
  ]
}
```

---

<a id="245-policy-api-v1-orgs-default-projects-project-quality-vpcs-test-security-policy-match-expression-ff1dafa9-bgm74-attachments-default"></a>
### 245. /policy/api/v1/orgs/default/projects/project-quality/vpcs/test-security-policy-match-expression-ff1dafa9_bgm74/attachments/default

**HTTP Methods:** GET

**Explanation:**
VPC (Virtual Private Cloud) management within a project. Manages isolated network environments for workloads.

---

<a id="246-policy-api-v1-orgs-default-projects-project-quality-vpcs-staticroute-eb4f3a68-rxtge-static-routes-guestcluster-staticroute-2-rxtge"></a>
### 246. /policy/api/v1/orgs/default/projects/project-quality/vpcs/staticroute-eb4f3a68_rxtge/static-routes/guestcluster-staticroute-2_rxtge

**HTTP Methods:** DELETE, GET, PATCH

**Explanation:**
VPC (Virtual Private Cloud) management within a project. Manages isolated network environments for workloads.

**Request Body (PATCH):**
```json
{
  "display_name": "guestcluster-staticroute-2",
  "id": "guestcluster-staticroute-2_rxtge",
  "network": "10.246.0.0/27",
  "next_hops": [
    {
      "admin_distance": 1,
      "ip_address": "192.168.0.1"
    }
  ],
  "tags": [
    {
      "scope": "nsx-op/cluster",
      "tag": "f06fd228-8088-4439-a9e6-26c90a829c57"
    },
    {
      "scope": "nsx-op/version",
      "tag": "1.0.0"
    },
    {
      "scope": "nsx-op/namespace",
      "tag": "staticroute-eb4f3a68"
    },
    {
      "scope": "nsx-op/static_route_name",
      "tag": "guestcluster-staticroute-2"
    },
    {
      "scope": "nsx-op/static_route_uid",
      "tag": "0ca322b9-3256-428d-9ca9-819bd0252888"
    },
    {
      "scope": "nsx-op/namespace_uid",
      "tag": "d379ee54-20b6-4fa3-b6f9-413d233226b6"
    }
  ]
}
```

---

<a id="247-policy-api-v1-orgs-default-projects-project-quality-vpcs-test-lb-50fedbb3-mv836-vpc-lb-virtual-servers-test-lb-50fedbb3-mv836-http"></a>
### 247. /policy/api/v1/orgs/default/projects/project-quality/vpcs/test-lb-50fedbb3_mv836/vpc-lb-virtual-servers/test-lb-50fedbb3_mv836_http

**HTTP Methods:** DELETE, GET, PATCH

**Explanation:**
VPC (Virtual Private Cloud) management within a project. Manages isolated network environments for workloads.

---


**Sample Response Body (GET, from logs):**
```json
{
  "enabled": true,
  "ip_address": "192.168.0.11",
  "ports": [
    "80"
  ],
  "access_log_enabled": false,
  "lb_persistence_profile_path": "",
  "lb_service_path": "/orgs/default/projects/project-quality/vpcs/test-lb-50fedbb3_mv836/vpc-lbs/default",
  "pool_path": "",
  "application_profile_path": "/infra/lb-app-profiles/ncp_f06fd228-8088-4439-a9e6-26c90a829c57_LBHttpProfile",
  "log_significant_event_only": false,
  "resource_type": "LBVirtualServer",
  "id": "test-lb-50fedbb3_mv836_http",
  "display_name": "test-lb-50fedbb3_http",
  "tags": [
    {
      "scope": "ncp/version",
      "tag": "1.2.0"
    },
    {
      "scope": "ncp/cluster",
      "tag": "f06fd228-8088-4439-a9e6-26c90a829c57"
    },
    {
      "scope": "ncp/lb_vs_type",
      "tag": "http"
    },
    {
      "scope": "ncp/created_for",
      "tag": "SLB"
    },
    {
      "scope": "external_id",
      "tag": "2506fba2-2bca-42a9-9fb0-35aa09b1d33c"
    },
    {
      "scope": "ncp/project",
      "tag": "test-lb-50fedbb3"
    },
    {
      "scope": "ncp/project_uid",
      "tag": "2506fba2-2bca-42a9-9fb0-35aa09b1d33c"
    }
  ],
  "path": "/orgs/default/projects/project-quality/vpcs/test-lb-50fedbb3_mv836/vpc-lb-virtual-servers/test-lb-50fedbb3_mv836_http",
  "relative_path": "test-lb-50fedbb3_mv836_http",
  "parent_path": "/orgs/default/projects/project-quality/vpcs/test-lb-50fedbb3_mv836",
  "remote_path": "",
  "unique_id": "df86678f-1cd5-47cc-8fe7-bd2cede4a201",
  "realization_id": "df86678f-1cd5-47cc-8fe7-bd2cede4a201",
  "owner_id": "42495ba4-8c0b-49c9-b645-84cc39c2df30",
  "marked_for_delete": false,
  "overridden": false,
  "_system_owned": false,
  "_protection": "NOT_PROTECTED",
  "_create_time": 1760689256034,
  "_create_user": "wcp-cluster-user-f06fd228-8088-4439-a9e6-26c90a829c57-d34133d7-0fdf-4c9d-abcf-df83bd050a59",
  "_last_modified_time": 1760689256034,
  "_last_modified_user": "wcp-cluster-user-f06fd228-8088-4439-a9e6-26c90a829c57-d34133d7-0fdf-4c9d-abcf-df83bd050a59",
  "_revision": 0
}
```
<a id="248-policy-api-v1-orgs-default-projects-project-quality-vpcs-testvpc-3658f2b5-vpc-lb-virtual-servers-prevpc-loadbalancer-8080-tcp-j7n9u"></a>
### 248. /policy/api/v1/orgs/default/projects/project-quality/vpcs/testvpc-3658f2b5/vpc-lb-virtual-servers/prevpc-loadbalancer_8080_TCP_j7n9u

**HTTP Methods:** DELETE, GET, PATCH

**Explanation:**
VPC (Virtual Private Cloud) management within a project. Manages isolated network environments for workloads.

---


**Sample Response Body (GET, from logs):**
```json
{
  "enabled": true,
  "ip_address": "192.168.0.8",
  "ports": [
    "8080"
  ],
  "access_log_enabled": false,
  "lb_persistence_profile_path": "",
  "lb_service_path": "/orgs/default/projects/project-quality/vpcs/testvpc-3658f2b5/vpc-lbs/default",
  "pool_path": "/orgs/default/projects/project-quality/vpcs/testvpc-3658f2b5/vpc-lb-pools/prevpc-loadbalancer_8080_d5d7u_icdrq",
  "application_profile_path": "/infra/lb-app-profiles/ncp_f06fd228-8088-4439-a9e6-26c90a829c57_LBFastTcpProfile",
  "log_significant_event_only": false,
  "resource_type": "LBVirtualServer",
  "id": "prevpc-loadbalancer_8080_TCP_j7n9u",
  "display_name": "prevpc-loadbalancer_8080_TCP",
  "tags": [
    {
      "scope": "ncp/version",
      "tag": "1.2.0"
    },
    {
      "scope": "ncp/cluster",
      "tag": "f06fd228-8088-4439-a9e6-26c90a829c57"
    },
    {
      "scope": "ncp/service_uid",
      "tag": "64af7175-c755-4315-9cf7-28c21bd6fc0a"
    },
    {
      "scope": "ncp/lb_vs_type",
      "tag": "layer_4"
    },
    {
      "scope": "ncp/created_for",
      "tag": "SLB"
    },
    {
      "scope": "external_id",
      "tag": "64af7175-c755-4315-9cf7-28c21bd6fc0a"
    },
    {
      "scope": "ncp/service_port_protocol",
      "tag": "TCP"
    }
  ],
  "path": "/orgs/default/projects/project-quality/vpcs/testvpc-3658f2b5/vpc-lb-virtual-servers/prevpc-loadbalancer_8080_TCP_j7n9u",
  "relative_path": "prevpc-loadbalancer_8080_TCP_j7n9u",
  "parent_path": "/orgs/default/projects/project-quality/vpcs/testvpc-3658f2b5",
  "remote_path": "",
  "unique_id": "fb003ea5-74c9-4a1e-8c28-920ce2c9d2ae",
  "realization_id": "fb003ea5-74c9-4a1e-8c28-920ce2c9d2ae",
  "owner_id": "42495ba4-8c0b-49c9-b645-84cc39c2df30",
  "marked_for_delete": false,
  "overridden": false,
  "_system_owned": false,
  "_protection": "NOT_PROTECTED",
  "_create_time": 1760690633816,
  "_create_user": "wcp-cluster-user-f06fd228-8088-4439-a9e6-26c90a829c57-d34133d7-0fdf-4c9d-abcf-df83bd050a59",
  "_last_modified_time": 1760690633816,
  "_last_modified_user": "wcp-cluster-user-f06fd228-8088-4439-a9e6-26c90a829c57-d34133d7-0fdf-4c9d-abcf-df83bd050a59",
  "_revision": 0
}
```
<a id="249-policy-api-v1-orgs-default-projects-project-quality-vpcs-staticroute-eb4f3a68-rxtge-ip-address-allocations-staticroute-ipalloc-rxtge"></a>
### 249. /policy/api/v1/orgs/default/projects/project-quality/vpcs/staticroute-eb4f3a68_rxtge/ip-address-allocations/staticroute-ipalloc_rxtge

**HTTP Methods:** DELETE, GET, PATCH

**Explanation:**
VPC (Virtual Private Cloud) management within a project. Manages isolated network environments for workloads.

**Request Body (PATCH):**
```json
{
  "allocation_size": 32,
  "display_name": "staticroute-ipalloc",
  "id": "staticroute-ipalloc_rxtge",
  "ip_address_block_visibility": "PRIVATE_TGW",
  "tags": [
    {
      "scope": "nsx-op/cluster",
      "tag": "f06fd228-8088-4439-a9e6-26c90a829c57"
    },
    {
      "scope": "nsx-op/version",
      "tag": "1.0.0"
    },
    {
      "scope": "nsx-op/namespace",
      "tag": "staticroute-eb4f3a68"
    },
    {
      "scope": "nsx-op/ipaddressallocation_name",
      "tag": "staticroute-ipalloc"
    },
    {
      "scope": "nsx-op/ipaddressallocation_uid",
      "tag": "9197b0de-2f10-4255-a239-da5d69f73b5d"
    },
    {
      "scope": "nsx-op/namespace_uid",
      "tag": "d379ee54-20b6-4fa3-b6f9-413d233226b6"
    }
  ]
}
```

---

<a id="250-policy-api-v1-orgs-default-projects-project-quality-vpcs-test-ipaddress-allocation-40d5699d-2p2tu-vpc-lb-pools-tea-svc-80-2p2tu-cusgz"></a>
### 250. /policy/api/v1/orgs/default/projects/project-quality/vpcs/test-ipaddress-allocation-40d5699d_2p2tu/vpc-lb-pools/tea-svc_80_2p2tu_cusgz

**HTTP Methods:** DELETE, GET, PATCH

**Explanation:**
VPC (Virtual Private Cloud) management within a project. Manages isolated network environments for workloads.

---


**Sample Response Body (GET, from logs):**
```json
{
  "algorithm": "ROUND_ROBIN",
  "snat_translation": {
    "type": "LBSnatAutoMap"
  },
  "min_active_members": 1,
  "resource_type": "LBPool",
  "id": "tea-svc_80_2p2tu_cusgz",
  "display_name": "tea-svc_80",
  "tags": [
    {
      "scope": "ncp/version",
      "tag": "1.2.0"
    },
    {
      "scope": "ncp/cluster",
      "tag": "f06fd228-8088-4439-a9e6-26c90a829c57"
    },
    {
      "scope": "ncp/project",
      "tag": "test-ipaddress-allocation-40d5699d"
    },
    {
      "scope": "external_id",
      "tag": "55c7492b-a285-4cba-9d71-bb6305d8c977"
    },
    {
      "scope": "ncp/service",
      "tag": "tea-svc"
    },
    {
      "scope": "ncp/service_port",
      "tag": "80"
    },
    {
      "scope": "ncp/service_uid",
      "tag": "55c7492b-a285-4cba-9d71-bb6305d8c977"
    },
    {
      "scope": "ncp/created_for",
      "tag": "SLB"
    },
    {
      "scope": "ncp/service_port_protocol",
      "tag": "TCP"
    }
  ],
  "path": "/orgs/default/projects/project-quality/vpcs/test-ipaddress-allocation-40d5699d_2p2tu/vpc-lb-pools/tea-svc_80_2p2tu_cusgz",
  "relative_path": "tea-svc_80_2p2tu_cusgz",
  "parent_path": "/orgs/default/projects/project-quality/vpcs/test-ipaddress-allocation-40d5699d_2p2tu",
  "remote_path": "",
  "unique_id": "154ae23d-a41d-4c71-b719-d874d5502a73",
  "realization_id": "154ae23d-a41d-4c71-b719-d874d5502a73",
  "owner_id": "42495ba4-8c0b-49c9-b645-84cc39c2df30",
  "marked_for_delete": false,
  "overridden": false,
  "_system_owned": false,
  "_protection": "NOT_PROTECTED",
  "_create_time": 1760689104834,
  "_create_user": "wcp-cluster-user-f06fd228-8088-4439-a9e6-26c90a829c57-d34133d7-0fdf-4c9d-abcf-df83bd050a59",
  "_last_modified_time": 1760689104834,
  "_last_modified_user": "wcp-cluster-user-f06fd228-8088-4439-a9e6-26c90a829c57-d34133d7-0fdf-4c9d-abcf-df83bd050a59",
  "_revision": 0
}
```
<a id="251-policy-api-v1-orgs-default-projects-project-quality-vpcs-test-security-policy-basic-72ecfa65-ib6li-subnets-pod-default-db03dc29-ib6li"></a>
### 251. /policy/api/v1/orgs/default/projects/project-quality/vpcs/test-security-policy-basic-72ecfa65_ib6li/subnets/pod-default-db03dc29_ib6li

**HTTP Methods:** DELETE, GET, PATCH

**Explanation:**
VPC subnet management within a project. Defines IP address ranges and network segments for VPC workloads.

**Request Body (PATCH):**
```json
{
  "access_mode": "Private_TGW",
  "advanced_config": {
    "static_ip_allocation": {
      "enabled": true
    }
  },
  "display_name": "pod-default-db03dc29_ib6li",
  "id": "pod-default-db03dc29_ib6li",
  "ipv4_subnet_size": 16,
  "subnet_dhcp_config": {
    "mode": "DHCP_DEACTIVATED"
  },
  "tags": [
    {
      "scope": "nsx-op/cluster",
      "tag": "f06fd228-8088-4439-a9e6-26c90a829c57"
    },
    {
      "scope": "nsx-op/version",
      "tag": "1.0.0"
    },
    {
      "scope": "nsx-op/subnetset_name",
      "tag": "pod-default"
    },
    {
      "scope": "nsx-op/subnetset_uid",
      "tag": "09c59213-fe9c-44c7-8d24-b6de3f3e49d1"
    },
    {
      "scope": "nsx/managed-by",
      "tag": "nsx-op"
    },
    {
      "scope": "nsx-op/namespace_uid",
      "tag": "a022f7f8-ff5d-4e79-964f-8782d0683f3a"
    },
    {
      "scope": "nsx-op/namespace",
      "tag": "test-security-policy-basic-72ecfa65"
    },
    {
      "scope": "kubernetes.io/metadata.name",
      "tag": "test-security-policy-basic-72ecfa65"
    },
    {
      "scope": "vSphereClusterID",
      "tag": "f06fd228-8088-4439-a9e6-26c90a829c57"
    }
  ]
}
```

---

<a id="252-policy-api-v1-orgs-default-projects-project-quality-vpcs-test-ipaddress-allocation-40d5699d-2p2tu-ip-address-allocations-ipalloc-vip-2p2tu"></a>
### 252. /policy/api/v1/orgs/default/projects/project-quality/vpcs/test-ipaddress-allocation-40d5699d_2p2tu/ip-address-allocations/ipalloc-vip_2p2tu

**HTTP Methods:** DELETE, GET, PATCH

**Explanation:**
VPC (Virtual Private Cloud) management within a project. Manages isolated network environments for workloads.

**Request Body (PATCH):**
```json
{
  "allocation_size": 32,
  "display_name": "ipalloc-vip",
  "id": "ipalloc-vip_2p2tu",
  "ip_address_block_visibility": "EXTERNAL",
  "tags": [
    {
      "scope": "nsx-op/cluster",
      "tag": "f06fd228-8088-4439-a9e6-26c90a829c57"
    },
    {
      "scope": "nsx-op/version",
      "tag": "1.0.0"
    },
    {
      "scope": "nsx-op/namespace",
      "tag": "test-ipaddress-allocation-40d5699d"
    },
    {
      "scope": "nsx-op/ipaddressallocation_name",
      "tag": "ipalloc-vip"
    },
    {
      "scope": "nsx-op/ipaddressallocation_uid",
      "tag": "0c1ebd4f-e722-4bc1-a70a-bdefa4069d23"
    },
    {
      "scope": "nsx-op/namespace_uid",
      "tag": "bf9c62cf-7653-43fd-9177-7319f8b4fe95"
    }
  ]
}
```

---

<a id="253-policy-api-v1-orgs-default-projects-project-quality-vpcs-test-ingress-sync-73e76bf1-rbp33-vpc-lb-pools-test-service-da1e3736-80-rbp33-xmlel"></a>
### 253. /policy/api/v1/orgs/default/projects/project-quality/vpcs/test-ingress-sync-73e76bf1_rbp33/vpc-lb-pools/test-service-da1e3736_80_rbp33_xmlel

**HTTP Methods:** DELETE, GET, PATCH

**Explanation:**
VPC (Virtual Private Cloud) management within a project. Manages isolated network environments for workloads.

---


**Sample Response Body (GET, from logs):**
```json
{
  "algorithm": "ROUND_ROBIN",
  "snat_translation": {
    "type": "LBSnatAutoMap"
  },
  "tcp_multiplexing_enabled": false,
  "tcp_multiplexing_number": 6,
  "min_active_members": 1,
  "resource_type": "LBPool",
  "id": "test-service-da1e3736_80_rbp33_xmlel",
  "display_name": "test-service-da1e3736_80",
  "tags": [
    {
      "scope": "ncp/version",
      "tag": "1.2.0"
    },
    {
      "scope": "ncp/cluster",
      "tag": "f06fd228-8088-4439-a9e6-26c90a829c57"
    },
    {
      "scope": "ncp/project",
      "tag": "test-ingress-sync-73e76bf1"
    },
    {
      "scope": "ncp/service",
      "tag": "test-service-da1e3736"
    },
    {
      "scope": "ncp/service_port",
      "tag": "80"
    },
    {
      "scope": "ncp/created_for",
      "tag": "SLB"
    }
  ],
  "path": "/orgs/default/projects/project-quality/vpcs/test-ingress-sync-73e76bf1_rbp33/vpc-lb-pools/test-service-da1e3736_80_rbp33_xmlel",
  "relative_path": "test-service-da1e3736_80_rbp33_xmlel",
  "parent_path": "/orgs/default/projects/project-quality/vpcs/test-ingress-sync-73e76bf1_rbp33",
  "remote_path": "",
  "unique_id": "830bf42b-778a-4ca5-825b-ef518bd4c470",
  "realization_id": "830bf42b-778a-4ca5-825b-ef518bd4c470",
  "owner_id": "42495ba4-8c0b-49c9-b645-84cc39c2df30",
  "marked_for_delete": false,
  "overridden": false,
  "_system_owned": false,
  "_protection": "NOT_PROTECTED",
  "_create_time": 1760689052455,
  "_create_user": "wcp-cluster-user-f06fd228-8088-4439-a9e6-26c90a829c57-d34133d7-0fdf-4c9d-abcf-df83bd050a59",
  "_last_modified_time": 1760689052455,
  "_last_modified_user": "wcp-cluster-user-f06fd228-8088-4439-a9e6-26c90a829c57-d34133d7-0fdf-4c9d-abcf-df83bd050a59",
  "_revision": 0
}
```
<a id="254-policy-api-v1-orgs-default-projects-project-quality-vpcs-test-security-policy-basic-72ecfa65-ib6li-security-policies-isolate-policy-1-f3sgl"></a>
### 254. /policy/api/v1/orgs/default/projects/project-quality/vpcs/test-security-policy-basic-72ecfa65_ib6li/security-policies/isolate-policy-1_f3sgl

**HTTP Methods:** DELETE, GET

**Explanation:**
VPC (Virtual Private Cloud) management within a project. Manages isolated network environments for workloads.

---

<a id="255-policy-api-v1-orgs-default-projects-project-quality-vpcs-test-ipaddress-allocation-40d5699d-2p2tu-vpc-lb-virtual-servers-tea-svc-80-tcp-p5j45"></a>
### 255. /policy/api/v1/orgs/default/projects/project-quality/vpcs/test-ipaddress-allocation-40d5699d_2p2tu/vpc-lb-virtual-servers/tea-svc_80_TCP_p5j45

**HTTP Methods:** DELETE, GET, PATCH

**Explanation:**
VPC (Virtual Private Cloud) management within a project. Manages isolated network environments for workloads.

---


**Sample Response Body (GET, from logs):**
```json
{
  "enabled": true,
  "ip_address": "192.168.0.8",
  "ports": [
    "80"
  ],
  "access_log_enabled": false,
  "lb_persistence_profile_path": "",
  "lb_service_path": "/orgs/default/projects/project-quality/vpcs/test-ipaddress-allocation-40d5699d_2p2tu/vpc-lbs/default",
  "pool_path": "/orgs/default/projects/project-quality/vpcs/test-ipaddress-allocation-40d5699d_2p2tu/vpc-lb-pools/tea-svc_80_2p2tu_cusgz",
  "application_profile_path": "/infra/lb-app-profiles/ncp_f06fd228-8088-4439-a9e6-26c90a829c57_LBFastTcpProfile",
  "log_significant_event_only": false,
  "resource_type": "LBVirtualServer",
  "id": "tea-svc_80_TCP_p5j45",
  "display_name": "tea-svc_80_TCP",
  "tags": [
    {
      "scope": "ncp/version",
      "tag": "1.2.0"
    },
    {
      "scope": "ncp/cluster",
      "tag": "f06fd228-8088-4439-a9e6-26c90a829c57"
    },
    {
      "scope": "ncp/service_uid",
      "tag": "55c7492b-a285-4cba-9d71-bb6305d8c977"
    },
    {
      "scope": "ncp/lb_vs_type",
      "tag": "layer_4"
    },
    {
      "scope": "ncp/created_for",
      "tag": "SLB"
    },
    {
      "scope": "external_id",
      "tag": "55c7492b-a285-4cba-9d71-bb6305d8c977"
    },
    {
      "scope": "ncp/service_port_protocol",
      "tag": "TCP"
    }
  ],
  "path": "/orgs/default/projects/project-quality/vpcs/test-ipaddress-allocation-40d5699d_2p2tu/vpc-lb-virtual-servers/tea-svc_80_TCP_p5j45",
  "relative_path": "tea-svc_80_TCP_p5j45",
  "parent_path": "/orgs/default/projects/project-quality/vpcs/test-ipaddress-allocation-40d5699d_2p2tu",
  "remote_path": "",
  "unique_id": "f703995b-dbf1-4d61-b2ba-5980b070edfe",
  "realization_id": "f703995b-dbf1-4d61-b2ba-5980b070edfe",
  "owner_id": "42495ba4-8c0b-49c9-b645-84cc39c2df30",
  "marked_for_delete": false,
  "overridden": false,
  "_system_owned": false,
  "_protection": "NOT_PROTECTED",
  "_create_time": 1760689105825,
  "_create_user": "wcp-cluster-user-f06fd228-8088-4439-a9e6-26c90a829c57-d34133d7-0fdf-4c9d-abcf-df83bd050a59",
  "_last_modified_time": 1760689105825,
  "_last_modified_user": "wcp-cluster-user-f06fd228-8088-4439-a9e6-26c90a829c57-d34133d7-0fdf-4c9d-abcf-df83bd050a59",
  "_revision": 0
}
```
<a id="256-policy-api-v1-orgs-default-projects-project-quality-vpcs-test-lb-50fedbb3-mv836-vpc-lb-virtual-servers-test-lb-50fedbb3-mv836-https-terminated"></a>
### 256. /policy/api/v1/orgs/default/projects/project-quality/vpcs/test-lb-50fedbb3_mv836/vpc-lb-virtual-servers/test-lb-50fedbb3_mv836_https_terminated

**HTTP Methods:** DELETE, GET, PATCH

**Explanation:**
VPC (Virtual Private Cloud) management within a project. Manages isolated network environments for workloads.

---


**Sample Response Body (GET, from logs):**
```json
{
  "enabled": true,
  "ip_address": "192.168.0.11",
  "ports": [
    "443"
  ],
  "access_log_enabled": false,
  "lb_persistence_profile_path": "",
  "lb_service_path": "/orgs/default/projects/project-quality/vpcs/test-lb-50fedbb3_mv836/vpc-lbs/default",
  "pool_path": "",
  "application_profile_path": "/infra/lb-app-profiles/ncp_f06fd228-8088-4439-a9e6-26c90a829c57_LBHttpProfile",
  "log_significant_event_only": false,
  "resource_type": "LBVirtualServer",
  "id": "test-lb-50fedbb3_mv836_https_terminated",
  "display_name": "test-lb-50fedbb3_https_terminated",
  "tags": [
    {
      "scope": "ncp/version",
      "tag": "1.2.0"
    },
    {
      "scope": "ncp/cluster",
      "tag": "f06fd228-8088-4439-a9e6-26c90a829c57"
    },
    {
      "scope": "ncp/lb_vs_type",
      "tag": "https_terminated"
    },
    {
      "scope": "ncp/created_for",
      "tag": "SLB"
    },
    {
      "scope": "external_id",
      "tag": "2506fba2-2bca-42a9-9fb0-35aa09b1d33c"
    },
    {
      "scope": "ncp/project",
      "tag": "test-lb-50fedbb3"
    },
    {
      "scope": "ncp/project_uid",
      "tag": "2506fba2-2bca-42a9-9fb0-35aa09b1d33c"
    }
  ],
  "path": "/orgs/default/projects/project-quality/vpcs/test-lb-50fedbb3_mv836/vpc-lb-virtual-servers/test-lb-50fedbb3_mv836_https_terminated",
  "relative_path": "test-lb-50fedbb3_mv836_https_terminated",
  "parent_path": "/orgs/default/projects/project-quality/vpcs/test-lb-50fedbb3_mv836",
  "remote_path": "",
  "unique_id": "09fbb75b-92a6-4398-bcbb-c379cb153e2f",
  "realization_id": "09fbb75b-92a6-4398-bcbb-c379cb153e2f",
  "owner_id": "42495ba4-8c0b-49c9-b645-84cc39c2df30",
  "marked_for_delete": false,
  "overridden": false,
  "_system_owned": false,
  "_protection": "NOT_PROTECTED",
  "_create_time": 1760689260229,
  "_create_user": "wcp-cluster-user-f06fd228-8088-4439-a9e6-26c90a829c57-d34133d7-0fdf-4c9d-abcf-df83bd050a59",
  "_last_modified_time": 1760689260229,
  "_last_modified_user": "wcp-cluster-user-f06fd228-8088-4439-a9e6-26c90a829c57-d34133d7-0fdf-4c9d-abcf-df83bd050a59",
  "_revision": 0
}
```
<a id="257-policy-api-v1-orgs-default-projects-project-quality-vpcs-test-security-policy-add-delete-0e034260-aruoj-security-policies-isolate-policy-1-6nt7g"></a>
### 257. /policy/api/v1/orgs/default/projects/project-quality/vpcs/test-security-policy-add-delete-0e034260_aruoj/security-policies/isolate-policy-1_6nt7g

**HTTP Methods:** DELETE, GET

**Explanation:**
VPC (Virtual Private Cloud) management within a project. Manages isolated network environments for workloads.

---

<a id="258-policy-api-v1-orgs-default-projects-project-quality-vpcs-test-security-policy-match-expression-ff1dafa9-bgm74-subnets-pod-default-1289f64d-bgm74"></a>
### 258. /policy/api/v1/orgs/default/projects/project-quality/vpcs/test-security-policy-match-expression-ff1dafa9_bgm74/subnets/pod-default-1289f64d_bgm74

**HTTP Methods:** DELETE, GET, PATCH

**Explanation:**
VPC subnet management within a project. Defines IP address ranges and network segments for VPC workloads.

**Request Body (PATCH):**
```json
{
  "access_mode": "Private_TGW",
  "advanced_config": {
    "static_ip_allocation": {
      "enabled": true
    }
  },
  "display_name": "pod-default-1289f64d_bgm74",
  "id": "pod-default-1289f64d_bgm74",
  "ipv4_subnet_size": 16,
  "subnet_dhcp_config": {
    "mode": "DHCP_DEACTIVATED"
  },
  "tags": [
    {
      "scope": "nsx-op/cluster",
      "tag": "f06fd228-8088-4439-a9e6-26c90a829c57"
    },
    {
      "scope": "nsx-op/version",
      "tag": "1.0.0"
    },
    {
      "scope": "nsx-op/subnetset_name",
      "tag": "pod-default"
    },
    {
      "scope": "nsx-op/subnetset_uid",
      "tag": "8e00ffa8-98d5-4b7b-9b50-7ce1b5943722"
    },
    {
      "scope": "nsx/managed-by",
      "tag": "nsx-op"
    },
    {
      "scope": "nsx-op/namespace_uid",
      "tag": "3de47ade-81f0-4df6-b8fe-4bd50341d1b1"
    },
    {
      "scope": "nsx-op/namespace",
      "tag": "test-security-policy-match-expression-ff1dafa9"
    },
    {
      "scope": "kubernetes.io/metadata.name",
      "tag": "test-security-policy-match-expression-ff1dafa9"
    },
    {
      "scope": "vSphereClusterID",
      "tag": "f06fd228-8088-4439-a9e6-26c90a829c57"
    }
  ]
}
```

---

<a id="259-policy-api-v1-orgs-default-projects-project-quality-vpcs-test-netpol-sync-c2cf40cd-65gvf-security-policies-test-network-policy-b6db586a-allow-qgq7e"></a>
### 259. /policy/api/v1/orgs/default/projects/project-quality/vpcs/test-netpol-sync-c2cf40cd_65gvf/security-policies/test-network-policy-b6db586a-allow_qgq7e

**HTTP Methods:** DELETE, GET

**Explanation:**
VPC (Virtual Private Cloud) management within a project. Manages isolated network environments for workloads.

---

<a id="260-policy-api-v1-orgs-default-projects-project-quality-vpcs-test-ipaddress-allocation-40d5699d-2p2tu-ip-address-allocations-guestcluster-workers-a-2p2tu"></a>
### 260. /policy/api/v1/orgs/default/projects/project-quality/vpcs/test-ipaddress-allocation-40d5699d_2p2tu/ip-address-allocations/guestcluster-workers-a_2p2tu

**HTTP Methods:** DELETE, GET, PATCH

**Explanation:**
VPC (Virtual Private Cloud) management within a project. Manages isolated network environments for workloads.

**Request Body (PATCH):**
```json
{
  "allocation_size": 32,
  "display_name": "guestcluster-workers-a",
  "id": "guestcluster-workers-a_2p2tu",
  "ip_address_block_visibility": "PRIVATE",
  "tags": [
    {
      "scope": "nsx-op/cluster",
      "tag": "f06fd228-8088-4439-a9e6-26c90a829c57"
    },
    {
      "scope": "nsx-op/version",
      "tag": "1.0.0"
    },
    {
      "scope": "nsx-op/namespace",
      "tag": "test-ipaddress-allocation-40d5699d"
    },
    {
      "scope": "nsx-op/ipaddressallocation_name",
      "tag": "guestcluster-workers-a"
    },
    {
      "scope": "nsx-op/ipaddressallocation_uid",
      "tag": "147745a4-1e8a-4b17-ab15-f4c9c2cdb8e1"
    },
    {
      "scope": "nsx-op/namespace_uid",
      "tag": "bf9c62cf-7653-43fd-9177-7319f8b4fe95"
    }
  ]
}
```

---

<a id="261-policy-api-v1-orgs-default-projects-project-quality-vpcs-test-ipaddress-allocation-40d5699d-2p2tu-ip-address-allocations-guestcluster-workers-b-2p2tu"></a>
### 261. /policy/api/v1/orgs/default/projects/project-quality/vpcs/test-ipaddress-allocation-40d5699d_2p2tu/ip-address-allocations/guestcluster-workers-b_2p2tu

**HTTP Methods:** DELETE, GET, PATCH

**Explanation:**
VPC (Virtual Private Cloud) management within a project. Manages isolated network environments for workloads.

**Request Body (PATCH):**
```json
{
  "allocation_size": 32,
  "display_name": "guestcluster-workers-b",
  "id": "guestcluster-workers-b_2p2tu",
  "ip_address_block_visibility": "EXTERNAL",
  "tags": [
    {
      "scope": "nsx-op/cluster",
      "tag": "f06fd228-8088-4439-a9e6-26c90a829c57"
    },
    {
      "scope": "nsx-op/version",
      "tag": "1.0.0"
    },
    {
      "scope": "nsx-op/namespace",
      "tag": "test-ipaddress-allocation-40d5699d"
    },
    {
      "scope": "nsx-op/ipaddressallocation_name",
      "tag": "guestcluster-workers-b"
    },
    {
      "scope": "nsx-op/ipaddressallocation_uid",
      "tag": "268950df-f233-4a67-954a-4f652e27afda"
    },
    {
      "scope": "nsx-op/namespace_uid",
      "tag": "bf9c62cf-7653-43fd-9177-7319f8b4fe95"
    }
  ]
}
```

---

<a id="262-policy-api-v1-orgs-default-projects-project-quality-vpcs-test-ipaddress-allocation-40d5699d-2p2tu-ip-address-allocations-guestcluster-workers-c-2p2tu"></a>
### 262. /policy/api/v1/orgs/default/projects/project-quality/vpcs/test-ipaddress-allocation-40d5699d_2p2tu/ip-address-allocations/guestcluster-workers-c_2p2tu

**HTTP Methods:** DELETE, GET, PATCH

**Explanation:**
VPC (Virtual Private Cloud) management within a project. Manages isolated network environments for workloads.

**Request Body (PATCH):**
```json
{
  "allocation_size": 256,
  "display_name": "guestcluster-workers-c",
  "id": "guestcluster-workers-c_2p2tu",
  "ip_address_block_visibility": "PRIVATE_TGW",
  "tags": [
    {
      "scope": "nsx-op/cluster",
      "tag": "f06fd228-8088-4439-a9e6-26c90a829c57"
    },
    {
      "scope": "nsx-op/version",
      "tag": "1.0.0"
    },
    {
      "scope": "nsx-op/namespace",
      "tag": "test-ipaddress-allocation-40d5699d"
    },
    {
      "scope": "nsx-op/ipaddressallocation_name",
      "tag": "guestcluster-workers-c"
    },
    {
      "scope": "nsx-op/ipaddressallocation_uid",
      "tag": "cd774b8d-b2df-4a7d-96e8-154a8dfe2a77"
    },
    {
      "scope": "nsx-op/namespace_uid",
      "tag": "bf9c62cf-7653-43fd-9177-7319f8b4fe95"
    }
  ]
}
```

---

<a id="263-policy-api-v1-orgs-default-projects-project-quality-vpcs-test-ingress-sync-73e76bf1-rbp33-vpc-lb-virtual-servers-test-ingress-sync-73e76bf1-rbp33-http"></a>
### 263. /policy/api/v1/orgs/default/projects/project-quality/vpcs/test-ingress-sync-73e76bf1_rbp33/vpc-lb-virtual-servers/test-ingress-sync-73e76bf1_rbp33_http

**HTTP Methods:** DELETE, GET, PATCH

**Explanation:**
VPC (Virtual Private Cloud) management within a project. Manages isolated network environments for workloads.

---


**Sample Response Body (GET, from logs):**
```json
{
  "enabled": true,
  "ip_address": "192.168.0.8",
  "ports": [
    "80"
  ],
  "access_log_enabled": false,
  "lb_persistence_profile_path": "",
  "lb_service_path": "/orgs/default/projects/project-quality/vpcs/test-ingress-sync-73e76bf1_rbp33/vpc-lbs/default",
  "pool_path": "",
  "application_profile_path": "/infra/lb-app-profiles/ncp_f06fd228-8088-4439-a9e6-26c90a829c57_LBHttpProfile",
  "log_significant_event_only": false,
  "resource_type": "LBVirtualServer",
  "id": "test-ingress-sync-73e76bf1_rbp33_http",
  "display_name": "test-ingress-sync-73e76bf1_http",
  "tags": [
    {
      "scope": "ncp/version",
      "tag": "1.2.0"
    },
    {
      "scope": "ncp/cluster",
      "tag": "f06fd228-8088-4439-a9e6-26c90a829c57"
    },
    {
      "scope": "ncp/lb_vs_type",
      "tag": "http"
    },
    {
      "scope": "ncp/created_for",
      "tag": "SLB"
    },
    {
      "scope": "external_id",
      "tag": "d9efcae1-642a-478c-9bb0-c5af498af932"
    },
    {
      "scope": "ncp/project",
      "tag": "test-ingress-sync-73e76bf1"
    },
    {
      "scope": "ncp/project_uid",
      "tag": "d9efcae1-642a-478c-9bb0-c5af498af932"
    }
  ],
  "path": "/orgs/default/projects/project-quality/vpcs/test-ingress-sync-73e76bf1_rbp33/vpc-lb-virtual-servers/test-ingress-sync-73e76bf1_rbp33_http",
  "relative_path": "test-ingress-sync-73e76bf1_rbp33_http",
  "parent_path": "/orgs/default/projects/project-quality/vpcs/test-ingress-sync-73e76bf1_rbp33",
  "remote_path": "",
  "unique_id": "7c21b452-8ecf-4950-b1ad-8fbb47464532",
  "realization_id": "7c21b452-8ecf-4950-b1ad-8fbb47464532",
  "owner_id": "42495ba4-8c0b-49c9-b645-84cc39c2df30",
  "marked_for_delete": false,
  "overridden": false,
  "_system_owned": false,
  "_protection": "NOT_PROTECTED",
  "_create_time": 1760689048720,
  "_create_user": "wcp-cluster-user-f06fd228-8088-4439-a9e6-26c90a829c57-d34133d7-0fdf-4c9d-abcf-df83bd050a59",
  "_last_modified_time": 1760689048720,
  "_last_modified_user": "wcp-cluster-user-f06fd228-8088-4439-a9e6-26c90a829c57-d34133d7-0fdf-4c9d-abcf-df83bd050a59",
  "_revision": 0
}
```
<a id="264-policy-api-v1-orgs-default-projects-project-quality-vpcs-test-security-policy-web-a2b779b4-f6e79-security-policies-named-port-policy-without-pod-ncmij"></a>
### 264. /policy/api/v1/orgs/default/projects/project-quality/vpcs/test-security-policy-web-a2b779b4_f6e79/security-policies/named-port-policy-without-pod_ncmij

**HTTP Methods:** DELETE, GET

**Explanation:**
VPC (Virtual Private Cloud) management within a project. Manages isolated network environments for workloads.

---

<a id="265-policy-api-v1-orgs-default-projects-project-quality-vpcs-test-netpol-sync-c2cf40cd-65gvf-security-policies-test-network-policy-b6db586a-isolation-qgq7e"></a>
### 265. /policy/api/v1/orgs/default/projects/project-quality/vpcs/test-netpol-sync-c2cf40cd_65gvf/security-policies/test-network-policy-b6db586a-isolation_qgq7e

**HTTP Methods:** DELETE, GET

**Explanation:**
VPC (Virtual Private Cloud) management within a project. Manages isolated network environments for workloads.

---

<a id="266-policy-api-v1-orgs-default-projects-project-quality-vpcs-test-security-policy-match-expression-ff1dafa9-bgm74-security-policies-expression-policy-1-jo4yz"></a>
### 266. /policy/api/v1/orgs/default/projects/project-quality/vpcs/test-security-policy-match-expression-ff1dafa9_bgm74/security-policies/expression-policy-1_jo4yz

**HTTP Methods:** DELETE, GET

**Explanation:**
VPC (Virtual Private Cloud) management within a project. Manages isolated network environments for workloads.

---

<a id="267-policy-api-v1-orgs-default-projects-project-quality-vpcs-test-ingress-sync-73e76bf1-rbp33-vpc-lb-virtual-servers-test-ingress-sync-73e76bf1-rbp33-https-terminated"></a>
### 267. /policy/api/v1/orgs/default/projects/project-quality/vpcs/test-ingress-sync-73e76bf1_rbp33/vpc-lb-virtual-servers/test-ingress-sync-73e76bf1_rbp33_https_terminated

**HTTP Methods:** DELETE, GET, PATCH

**Explanation:**
VPC (Virtual Private Cloud) management within a project. Manages isolated network environments for workloads.

---


**Sample Response Body (GET, from logs):**
```json
{
  "enabled": true,
  "ip_address": "192.168.0.8",
  "ports": [
    "443"
  ],
  "access_log_enabled": false,
  "lb_persistence_profile_path": "",
  "lb_service_path": "/orgs/default/projects/project-quality/vpcs/test-ingress-sync-73e76bf1_rbp33/vpc-lbs/default",
  "pool_path": "",
  "application_profile_path": "/infra/lb-app-profiles/ncp_f06fd228-8088-4439-a9e6-26c90a829c57_LBHttpProfile",
  "log_significant_event_only": false,
  "resource_type": "LBVirtualServer",
  "id": "test-ingress-sync-73e76bf1_rbp33_https_terminated",
  "display_name": "test-ingress-sync-73e76bf1_https_terminated",
  "tags": [
    {
      "scope": "ncp/version",
      "tag": "1.2.0"
    },
    {
      "scope": "ncp/cluster",
      "tag": "f06fd228-8088-4439-a9e6-26c90a829c57"
    },
    {
      "scope": "ncp/lb_vs_type",
      "tag": "https_terminated"
    },
    {
      "scope": "ncp/created_for",
      "tag": "SLB"
    },
    {
      "scope": "external_id",
      "tag": "d9efcae1-642a-478c-9bb0-c5af498af932"
    },
    {
      "scope": "ncp/project",
      "tag": "test-ingress-sync-73e76bf1"
    },
    {
      "scope": "ncp/project_uid",
      "tag": "d9efcae1-642a-478c-9bb0-c5af498af932"
    }
  ],
  "path": "/orgs/default/projects/project-quality/vpcs/test-ingress-sync-73e76bf1_rbp33/vpc-lb-virtual-servers/test-ingress-sync-73e76bf1_rbp33_https_terminated",
  "relative_path": "test-ingress-sync-73e76bf1_rbp33_https_terminated",
  "parent_path": "/orgs/default/projects/project-quality/vpcs/test-ingress-sync-73e76bf1_rbp33",
  "remote_path": "",
  "unique_id": "76824f84-251a-4d12-9dd8-be9b246c053c",
  "realization_id": "76824f84-251a-4d12-9dd8-be9b246c053c",
  "owner_id": "42495ba4-8c0b-49c9-b645-84cc39c2df30",
  "marked_for_delete": false,
  "overridden": false,
  "_system_owned": false,
  "_protection": "NOT_PROTECTED",
  "_create_time": 1760689050806,
  "_create_user": "wcp-cluster-user-f06fd228-8088-4439-a9e6-26c90a829c57-d34133d7-0fdf-4c9d-abcf-df83bd050a59",
  "_last_modified_time": 1760689050806,
  "_last_modified_user": "wcp-cluster-user-f06fd228-8088-4439-a9e6-26c90a829c57-d34133d7-0fdf-4c9d-abcf-df83bd050a59",
  "_revision": 0
}
```
<a id="268-policy-api-v1-orgs-default-projects-project-quality-vpcs-testvpc-3658f2b5-nat-default-nat-rules"></a>
### 268. /policy/api/v1/orgs/default/projects/project-quality/vpcs/testvpc-3658f2b5/nat/DEFAULT/nat-rules

**HTTP Methods:** GET

**Explanation:**
VPC (Virtual Private Cloud) management within a project. Manages isolated network environments for workloads.

---

<a id="269-policy-api-v1-orgs-default-projects-project-quality-vpcs-testvpc-7ab2d8aa-nat-default-nat-rules"></a>
### 269. /policy/api/v1/orgs/default/projects/project-quality/vpcs/testvpc-7ab2d8aa/nat/DEFAULT/nat-rules

**HTTP Methods:** GET

**Explanation:**
VPC (Virtual Private Cloud) management within a project. Manages isolated network environments for workloads.

---

<a id="270-policy-api-v1-orgs-default-projects-project-quality-vpcs-kube-system-fyr99-nat-default-nat-rules"></a>
### 270. /policy/api/v1/orgs/default/projects/project-quality/vpcs/kube-system_fyr99/nat/DEFAULT/nat-rules

**HTTP Methods:** GET

**Explanation:**
VPC (Virtual Private Cloud) management within a project. Manages isolated network environments for workloads.

---

<a id="271-policy-api-v1-orgs-default-projects-project-quality-vpcs-web-da775e6f-6o7ts-nat-default-nat-rules"></a>
### 271. /policy/api/v1/orgs/default/projects/project-quality/vpcs/web-da775e6f_6o7ts/nat/DEFAULT/nat-rules

**HTTP Methods:** GET

**Explanation:**
VPC (Virtual Private Cloud) management within a project. Manages isolated network environments for workloads.

---

<a id="272-policy-api-v1-orgs-default-projects-project-quality-vpcs-client-91c3f484-qzuxu-nat-default-nat-rules"></a>
### 272. /policy/api/v1/orgs/default/projects/project-quality/vpcs/client-91c3f484_qzuxu/nat/DEFAULT/nat-rules

**HTTP Methods:** GET

**Explanation:**
VPC (Virtual Private Cloud) management within a project. Manages isolated network environments for workloads.

---

<a id="273-policy-api-v1-orgs-default-projects-project-quality-vpcs-test-lb-50fedbb3-mv836-nat-default-nat-rules"></a>
### 273. /policy/api/v1/orgs/default/projects/project-quality/vpcs/test-lb-50fedbb3_mv836/nat/DEFAULT/nat-rules

**HTTP Methods:** GET

**Explanation:**
VPC (Virtual Private Cloud) management within a project. Manages isolated network environments for workloads.

---

<a id="274-policy-api-v1-orgs-default-projects-project-quality-vpcs-test-pod-1dd9a577-fu9t5-nat-default-nat-rules"></a>
### 274. /policy/api/v1/orgs/default/projects/project-quality/vpcs/test-pod-1dd9a577_fu9t5/nat/DEFAULT/nat-rules

**HTTP Methods:** GET

**Explanation:**
VPC (Virtual Private Cloud) management within a project. Manages isolated network environments for workloads.

---

<a id="275-policy-api-v1-orgs-default-projects-project-quality-vpcs-target-ns-56446c91-6zdip-nat-default-nat-rules"></a>
### 275. /policy/api/v1/orgs/default/projects/project-quality/vpcs/target-ns-56446c91_6zdip/nat/DEFAULT/nat-rules

**HTTP Methods:** GET

**Explanation:**
VPC (Virtual Private Cloud) management within a project. Manages isolated network environments for workloads.

---

<a id="276-policy-api-v1-orgs-default-projects-project-quality-vpcs-update-ns-8eb115ed-baxdx-nat-default-nat-rules"></a>
### 276. /policy/api/v1/orgs/default/projects/project-quality/vpcs/update-ns-8eb115ed_baxdx/nat/DEFAULT/nat-rules

**HTTP Methods:** GET

**Explanation:**
VPC (Virtual Private Cloud) management within a project. Manages isolated network environments for workloads.

---

<a id="277-policy-api-v1-orgs-default-projects-project-quality-vpcs-subnet-e2e-1f11082b-56qvy-nat-default-nat-rules"></a>
### 277. /policy/api/v1/orgs/default/projects/project-quality/vpcs/subnet-e2e-1f11082b_56qvy/nat/DEFAULT/nat-rules

**HTTP Methods:** GET

**Explanation:**
VPC (Virtual Private Cloud) management within a project. Manages isolated network environments for workloads.

---

<a id="278-policy-api-v1-orgs-default-projects-project-quality-vpcs-staticroute-eb4f3a68-rxtge-nat-default-nat-rules"></a>
### 278. /policy/api/v1/orgs/default/projects/project-quality/vpcs/staticroute-eb4f3a68_rxtge/nat/DEFAULT/nat-rules

**HTTP Methods:** GET

**Explanation:**
VPC (Virtual Private Cloud) management within a project. Manages isolated network environments for workloads.

---

<a id="279-policy-api-v1-orgs-default-projects-project-quality-vpcs-customized-ns-99beca1e-yleom-nat-default-nat-rules"></a>
### 279. /policy/api/v1/orgs/default/projects/project-quality/vpcs/customized-ns-99beca1e_yleom/nat/DEFAULT/nat-rules

**HTTP Methods:** GET

**Explanation:**
VPC (Virtual Private Cloud) management within a project. Manages isolated network environments for workloads.

---

<a id="280-policy-api-v1-orgs-default-projects-project-quality-vpcs-test-pod-sync-e8b8a7ca-m404i-nat-default-nat-rules"></a>
### 280. /policy/api/v1/orgs/default/projects/project-quality/vpcs/test-pod-sync-e8b8a7ca_m404i/nat/DEFAULT/nat-rules

**HTTP Methods:** GET

**Explanation:**
VPC (Virtual Private Cloud) management within a project. Manages isolated network environments for workloads.

---

<a id="281-policy-api-v1-orgs-default-projects-project-quality-vpcs-shared-vpc-ns-0-3bc799ba-nwr40-nat-default-nat-rules"></a>
### 281. /policy/api/v1/orgs/default/projects/project-quality/vpcs/shared-vpc-ns-0-3bc799ba_nwr40/nat/DEFAULT/nat-rules

**HTTP Methods:** GET

**Explanation:**
VPC (Virtual Private Cloud) management within a project. Manages isolated network environments for workloads.

---

<a id="282-policy-api-v1-orgs-default-projects-project-quality-vpcs-test-netpol-sync-c2cf40cd-65gvf-nat-default-nat-rules"></a>
### 282. /policy/api/v1/orgs/default/projects/project-quality/vpcs/test-netpol-sync-c2cf40cd_65gvf/nat/DEFAULT/nat-rules

**HTTP Methods:** GET

**Explanation:**
VPC (Virtual Private Cloud) management within a project. Manages isolated network environments for workloads.

---

<a id="283-policy-api-v1-orgs-default-projects-project-quality-vpcs-test-ingress-sync-73e76bf1-rbp33-nat-default-nat-rules"></a>
### 283. /policy/api/v1/orgs/default/projects/project-quality/vpcs/test-ingress-sync-73e76bf1_rbp33/nat/DEFAULT/nat-rules

**HTTP Methods:** GET

**Explanation:**
VPC (Virtual Private Cloud) management within a project. Manages isolated network environments for workloads.

---

<a id="284-policy-api-v1-orgs-default-projects-project-quality-vpcs-test-service-sync-f1d17bff-5230b-nat-default-nat-rules"></a>
### 284. /policy/api/v1/orgs/default/projects/project-quality/vpcs/test-service-sync-f1d17bff_5230b/nat/DEFAULT/nat-rules

**HTTP Methods:** GET

**Explanation:**
VPC (Virtual Private Cloud) management within a project. Manages isolated network environments for workloads.

---

<a id="285-policy-api-v1-orgs-default-projects-project-quality-vpcs-networkinfo-default-efa7e691-1fkak-nat-default-nat-rules"></a>
### 285. /policy/api/v1/orgs/default/projects/project-quality/vpcs/networkinfo-default-efa7e691_1fkak/nat/DEFAULT/nat-rules

**HTTP Methods:** GET

**Explanation:**
VPC (Virtual Private Cloud) management within a project. Manages isolated network environments for workloads.

---

<a id="286-policy-api-v1-orgs-default-projects-project-quality-vpcs-test-namespace-sync-49fbe5bd-p9u70-nat-default-nat-rules"></a>
### 286. /policy/api/v1/orgs/default/projects/project-quality/vpcs/test-namespace-sync-49fbe5bd_p9u70/nat/DEFAULT/nat-rules

**HTTP Methods:** GET

**Explanation:**
VPC (Virtual Private Cloud) management within a project. Manages isolated network environments for workloads.

---

<a id="287-policy-api-v1-orgs-default-projects-project-quality-vpcs-precreated-target-ns-3c7c1821-v5ml5-nat-default-nat-rules"></a>
### 287. /policy/api/v1/orgs/default/projects/project-quality/vpcs/precreated-target-ns-3c7c1821_v5ml5/nat/DEFAULT/nat-rules

**HTTP Methods:** GET

**Explanation:**
VPC (Virtual Private Cloud) management within a project. Manages isolated network environments for workloads.

---

<a id="288-policy-api-v1-orgs-default-projects-project-quality-vpcs-test-create-vm-basic-f449d9bf-3ehn6-nat-default-nat-rules"></a>
### 288. /policy/api/v1/orgs/default/projects/project-quality/vpcs/test-create-vm-basic-f449d9bf_3ehn6/nat/DEFAULT/nat-rules

**HTTP Methods:** GET

**Explanation:**
VPC (Virtual Private Cloud) management within a project. Manages isolated network environments for workloads.

---

<a id="289-policy-api-v1-orgs-default-projects-project-quality-vpcs-kube-system-fyr99-subnets-vm-default-637336f2-fyr99-status"></a>
### 289. /policy/api/v1/orgs/default/projects/project-quality/vpcs/kube-system_fyr99/subnets/vm-default-637336f2_fyr99/status

**HTTP Methods:** GET

**Explanation:**
VPC subnet management within a project. Defines IP address ranges and network segments for VPC workloads.

---

<a id="290-policy-api-v1-orgs-default-projects-project-quality-vpcs-precreated-subnet-ns1-a72a2a9d-8m6zu-nat-default-nat-rules"></a>
### 290. /policy/api/v1/orgs/default/projects/project-quality/vpcs/precreated-subnet-ns1-a72a2a9d_8m6zu/nat/DEFAULT/nat-rules

**HTTP Methods:** GET

**Explanation:**
VPC (Virtual Private Cloud) management within a project. Manages isolated network environments for workloads.

---

<a id="291-policy-api-v1-orgs-default-projects-project-quality-vpcs-precreated-subnet-ns2-42ff4c1a-tpi2w-nat-default-nat-rules"></a>
### 291. /policy/api/v1/orgs/default/projects/project-quality/vpcs/precreated-subnet-ns2-42ff4c1a_tpi2w/nat/DEFAULT/nat-rules

**HTTP Methods:** GET

**Explanation:**
VPC (Virtual Private Cloud) management within a project. Manages isolated network environments for workloads.

---

<a id="292-policy-api-v1-orgs-default-projects-project-quality-vpcs-subnet-e2e-1f11082b-56qvy-subnets-subnet-cidr-56qvy-status"></a>
### 292. /policy/api/v1/orgs/default/projects/project-quality/vpcs/subnet-e2e-1f11082b_56qvy/subnets/subnet-cidr_56qvy/status

**HTTP Methods:** GET

**Explanation:**
VPC subnet management within a project. Defines IP address ranges and network segments for VPC workloads.

---

<a id="293-policy-api-v1-orgs-default-projects-project-quality-vpcs-subnet-e2e-1f11082b-56qvy-subnets-subnet-dhcp-56qvy-status"></a>
### 293. /policy/api/v1/orgs/default/projects/project-quality/vpcs/subnet-e2e-1f11082b_56qvy/subnets/subnet-dhcp_56qvy/status

**HTTP Methods:** GET

**Explanation:**
VPC subnet management within a project. Defines IP address ranges and network segments for VPC workloads.

---

<a id="294-policy-api-v1-orgs-default-projects-project-quality-vpcs-testvpc-3658f2b5-subnets-pod-default-ec7c1039-d5d7u-status"></a>
### 294. /policy/api/v1/orgs/default/projects/project-quality/vpcs/testvpc-3658f2b5/subnets/pod-default-ec7c1039_d5d7u/status

**HTTP Methods:** GET

**Explanation:**
VPC subnet management within a project. Defines IP address ranges and network segments for VPC workloads.

---

<a id="295-policy-api-v1-orgs-default-projects-project-quality-vpcs-testvpc-7ab2d8aa-subnets-pod-default-e0268dd8-5583h-status"></a>
### 295. /policy/api/v1/orgs/default/projects/project-quality/vpcs/testvpc-7ab2d8aa/subnets/pod-default-e0268dd8_5583h/status

**HTTP Methods:** GET

**Explanation:**
VPC subnet management within a project. Defines IP address ranges and network segments for VPC workloads.

---

<a id="296-policy-api-v1-orgs-default-projects-project-quality-vpcs-subnet-e2e-1f11082b-56qvy-subnets-subnet-no-ip-56qvy-status"></a>
### 296. /policy/api/v1/orgs/default/projects/project-quality/vpcs/subnet-e2e-1f11082b_56qvy/subnets/subnet-no-ip_56qvy/status

**HTTP Methods:** GET

**Explanation:**
VPC subnet management within a project. Defines IP address ranges and network segments for VPC workloads.

---

<a id="297-policy-api-v1-orgs-default-projects-project-quality-vpcs-web-da775e6f-6o7ts-subnets-pod-default-a734dd59-6o7ts-status"></a>
### 297. /policy/api/v1/orgs/default/projects/project-quality/vpcs/web-da775e6f_6o7ts/subnets/pod-default-a734dd59_6o7ts/status

**HTTP Methods:** GET

**Explanation:**
VPC subnet management within a project. Defines IP address ranges and network segments for VPC workloads.

---

<a id="298-policy-api-v1-orgs-default-projects-project-quality-vpcs-test-security-policy-web-a2b779b4-f6e79-nat-default-nat-rules"></a>
### 298. /policy/api/v1/orgs/default/projects/project-quality/vpcs/test-security-policy-web-a2b779b4_f6e79/nat/DEFAULT/nat-rules

**HTTP Methods:** GET

**Explanation:**
VPC (Virtual Private Cloud) management within a project. Manages isolated network environments for workloads.

---

<a id="299-policy-api-v1-orgs-default-projects-project-quality-vpcs-test-ipaddress-allocation-40d5699d-2p2tu-nat-default-nat-rules"></a>
### 299. /policy/api/v1/orgs/default/projects/project-quality/vpcs/test-ipaddress-allocation-40d5699d_2p2tu/nat/DEFAULT/nat-rules

**HTTP Methods:** GET

**Explanation:**
VPC (Virtual Private Cloud) management within a project. Manages isolated network environments for workloads.

---

<a id="300-policy-api-v1-orgs-default-projects-project-quality-vpcs-client-91c3f484-qzuxu-subnets-pod-default-075e5037-qzuxu-status"></a>
### 300. /policy/api/v1/orgs/default/projects/project-quality/vpcs/client-91c3f484_qzuxu/subnets/pod-default-075e5037_qzuxu/status

**HTTP Methods:** GET

**Explanation:**
VPC subnet management within a project. Defines IP address ranges and network segments for VPC workloads.

---

<a id="301-policy-api-v1-orgs-default-projects-project-quality-vpcs-subnet-e2e-1f11082b-56qvy-subnets-subnet-dhcp-cidr-56qvy-status"></a>
### 301. /policy/api/v1/orgs/default/projects/project-quality/vpcs/subnet-e2e-1f11082b_56qvy/subnets/subnet-dhcp-cidr_56qvy/status

**HTTP Methods:** GET

**Explanation:**
VPC subnet management within a project. Defines IP address ranges and network segments for VPC workloads.

---

<a id="302-policy-api-v1-orgs-default-projects-project-quality-vpcs-subnet-e2e-1f11082b-56qvy-subnets-subnet-only-dhcp-56qvy-status"></a>
### 302. /policy/api/v1/orgs/default/projects/project-quality/vpcs/subnet-e2e-1f11082b_56qvy/subnets/subnet-only-dhcp_56qvy/status

**HTTP Methods:** GET

**Explanation:**
VPC subnet management within a project. Defines IP address ranges and network segments for VPC workloads.

---

<a id="303-policy-api-v1-orgs-default-projects-project-quality-vpcs-test-security-policy-basic-72ecfa65-ib6li-nat-default-nat-rules"></a>
### 303. /policy/api/v1/orgs/default/projects/project-quality/vpcs/test-security-policy-basic-72ecfa65_ib6li/nat/DEFAULT/nat-rules

**HTTP Methods:** GET

**Explanation:**
VPC (Virtual Private Cloud) management within a project. Manages isolated network environments for workloads.

---

<a id="304-policy-api-v1-orgs-default-projects-project-quality-vpcs-test-lb-50fedbb3-mv836-subnets-pod-default-3cc5e9c8-mv836-status"></a>
### 304. /policy/api/v1/orgs/default/projects/project-quality/vpcs/test-lb-50fedbb3_mv836/subnets/pod-default-3cc5e9c8_mv836/status

**HTTP Methods:** GET

**Explanation:**
VPC subnet management within a project. Defines IP address ranges and network segments for VPC workloads.

---

<a id="305-policy-api-v1-orgs-default-projects-project-quality-vpcs-test-security-policy-client-3a06d660-qiyvu-nat-default-nat-rules"></a>
### 305. /policy/api/v1/orgs/default/projects/project-quality/vpcs/test-security-policy-client-3a06d660_qiyvu/nat/DEFAULT/nat-rules

**HTTP Methods:** GET

**Explanation:**
VPC (Virtual Private Cloud) management within a project. Manages isolated network environments for workloads.

---

<a id="306-policy-api-v1-orgs-default-projects-project-quality-vpcs-target-ns-56446c91-6zdip-subnets-vm-default-eb532fd0-c6gls-status"></a>
### 306. /policy/api/v1/orgs/default/projects/project-quality/vpcs/target-ns-56446c91_6zdip/subnets/vm-default-eb532fd0_c6gls/status

**HTTP Methods:** GET

**Explanation:**
VPC subnet management within a project. Defines IP address ranges and network segments for VPC workloads.

---

<a id="307-policy-api-v1-orgs-default-projects-project-quality-vpcs-test-pod-1dd9a577-fu9t5-subnets-pod-default-5cf92338-fu9t5-status"></a>
### 307. /policy/api/v1/orgs/default/projects/project-quality/vpcs/test-pod-1dd9a577_fu9t5/subnets/pod-default-5cf92338_fu9t5/status

**HTTP Methods:** GET

**Explanation:**
VPC subnet management within a project. Defines IP address ranges and network segments for VPC workloads.

---

<a id="308-policy-api-v1-orgs-default-projects-project-quality-vpcs-vmware-system-supervisor-services-vpc-kzc7e-nat-default-nat-rules"></a>
### 308. /policy/api/v1/orgs/default/projects/project-quality/vpcs/vmware-system-supervisor-services-vpc_kzc7e/nat/DEFAULT/nat-rules

**HTTP Methods:** GET

**Explanation:**
VPC (Virtual Private Cloud) management within a project. Manages isolated network environments for workloads.

---

<a id="309-policy-api-v1-orgs-default-projects-project-quality-vpcs-subnet-e2e-1f11082b-56qvy-subnets-subnet-only-no-dhcp-56qvy-status"></a>
### 309. /policy/api/v1/orgs/default/projects/project-quality/vpcs/subnet-e2e-1f11082b_56qvy/subnets/subnet-only-no-dhcp_56qvy/status

**HTTP Methods:** GET

**Explanation:**
VPC subnet management within a project. Defines IP address ranges and network segments for VPC workloads.

---

<a id="310-policy-api-v1-orgs-default-projects-project-quality-vpcs-subnet-e2e-1f11082b-56qvy-subnets-pod-default-6a81803a-56qvy-status"></a>
### 310. /policy/api/v1/orgs/default/projects/project-quality/vpcs/subnet-e2e-1f11082b_56qvy/subnets/pod-default-6a81803a_56qvy/status

**HTTP Methods:** GET

**Explanation:**
VPC subnet management within a project. Defines IP address ranges and network segments for VPC workloads.

---

<a id="311-policy-api-v1-orgs-default-projects-project-quality-vpcs-subnet-e2e-1f11082b-56qvy-subnets-subnet-dhcp-modify-1-56qvy-status"></a>
### 311. /policy/api/v1/orgs/default/projects/project-quality/vpcs/subnet-e2e-1f11082b_56qvy/subnets/subnet-dhcp-modify-1_56qvy/status

**HTTP Methods:** GET

**Explanation:**
VPC subnet management within a project. Defines IP address ranges and network segments for VPC workloads.

---

<a id="312-policy-api-v1-orgs-default-projects-project-quality-vpcs-test-security-policy-add-delete-0e034260-aruoj-nat-default-nat-rules"></a>
### 312. /policy/api/v1/orgs/default/projects/project-quality/vpcs/test-security-policy-add-delete-0e034260_aruoj/nat/DEFAULT/nat-rules

**HTTP Methods:** GET

**Explanation:**
VPC (Virtual Private Cloud) management within a project. Manages isolated network environments for workloads.

---

<a id="313-policy-api-v1-orgs-default-projects-project-quality-vpcs-test-create-vm-basic-f449d9bf-3ehn6-subnets-public-subnet-3ehn6-status"></a>
### 313. /policy/api/v1/orgs/default/projects/project-quality/vpcs/test-create-vm-basic-f449d9bf_3ehn6/subnets/public-subnet_3ehn6/status

**HTTP Methods:** GET

**Explanation:**
VPC subnet management within a project. Defines IP address ranges and network segments for VPC workloads.

---

<a id="314-policy-api-v1-orgs-default-projects-project-quality-vpcs-test-pod-sync-e8b8a7ca-m404i-subnets-pod-default-0dd88421-m404i-status"></a>
### 314. /policy/api/v1/orgs/default/projects/project-quality/vpcs/test-pod-sync-e8b8a7ca_m404i/subnets/pod-default-0dd88421_m404i/status

**HTTP Methods:** GET

**Explanation:**
VPC subnet management within a project. Defines IP address ranges and network segments for VPC workloads.

---

<a id="315-policy-api-v1-orgs-default-projects-project-quality-vpcs-precreated-subnet-ns1-a72a2a9d-8m6zu-subnets-normal-subnet-8m6zu-status"></a>
### 315. /policy/api/v1/orgs/default/projects/project-quality/vpcs/precreated-subnet-ns1-a72a2a9d_8m6zu/subnets/normal-subnet_8m6zu/status

**HTTP Methods:** GET

**Explanation:**
VPC subnet management within a project. Defines IP address ranges and network segments for VPC workloads.

---

<a id="316-policy-api-v1-orgs-default-projects-project-quality-vpcs-test-security-policy-match-expression-ff1dafa9-bgm74-nat-default-nat-rules"></a>
### 316. /policy/api/v1/orgs/default/projects/project-quality/vpcs/test-security-policy-match-expression-ff1dafa9_bgm74/nat/DEFAULT/nat-rules

**HTTP Methods:** GET

**Explanation:**
VPC (Virtual Private Cloud) management within a project. Manages isolated network environments for workloads.

---

<a id="317-policy-api-v1-orgs-default-projects-project-quality-vpcs-kube-system-fyr99-subnets-vm-default-637336f2-fyr99-dynamic-ip-reservations"></a>
### 317. /policy/api/v1/orgs/default/projects/project-quality/vpcs/kube-system_fyr99/subnets/vm-default-637336f2_fyr99/dynamic-ip-reservations

**HTTP Methods:** GET

**Explanation:**
VPC subnet management within a project. Defines IP address ranges and network segments for VPC workloads.

---

<a id="318-policy-api-v1-orgs-default-projects-project-quality-vpcs-subnet-e2e-1f11082b-56qvy-subnets-user-subnetset-dhcp-c85186d8-56qvy-status"></a>
### 318. /policy/api/v1/orgs/default/projects/project-quality/vpcs/subnet-e2e-1f11082b_56qvy/subnets/user-subnetset-dhcp-c85186d8_56qvy/status

**HTTP Methods:** GET

**Explanation:**
VPC subnet management within a project. Defines IP address ranges and network segments for VPC workloads.

---

<a id="319-policy-api-v1-orgs-default-projects-project-quality-vpcs-precreated-target-ns-3c7c1821-v5ml5-subnets-shared-subnet-892e2-v5ml5-status"></a>
### 319. /policy/api/v1/orgs/default/projects/project-quality/vpcs/precreated-target-ns-3c7c1821_v5ml5/subnets/shared-subnet-892e2_v5ml5/status

**HTTP Methods:** GET

**Explanation:**
VPC subnet management within a project. Defines IP address ranges and network segments for VPC workloads.

---

<a id="320-policy-api-v1-orgs-default-projects-project-quality-vpcs-subnet-e2e-1f11082b-56qvy-subnets-user-subnetset-static-948a4c45-56qvy-status"></a>
### 320. /policy/api/v1/orgs/default/projects/project-quality/vpcs/subnet-e2e-1f11082b_56qvy/subnets/user-subnetset-static-948a4c45_56qvy/status

**HTTP Methods:** GET

**Explanation:**
VPC subnet management within a project. Defines IP address ranges and network segments for VPC workloads.

---

<a id="321-policy-api-v1-orgs-default-projects-project-quality-vpcs-precreated-target-ns-3c7c1821-v5ml5-subnets-shared-subnet-2-421d2-v5ml5-status"></a>
### 321. /policy/api/v1/orgs/default/projects/project-quality/vpcs/precreated-target-ns-3c7c1821_v5ml5/subnets/shared-subnet-2-421d2_v5ml5/status

**HTTP Methods:** GET

**Explanation:**
VPC subnet management within a project. Defines IP address ranges and network segments for VPC workloads.

---

<a id="322-policy-api-v1-orgs-default-projects-project-quality-vpcs-test-security-policy-basic-72ecfa65-ib6li-subnets-pod-default-db03dc29-ib6li-status"></a>
### 322. /policy/api/v1/orgs/default/projects/project-quality/vpcs/test-security-policy-basic-72ecfa65_ib6li/subnets/pod-default-db03dc29_ib6li/status

**HTTP Methods:** GET

**Explanation:**
VPC subnet management within a project. Defines IP address ranges and network segments for VPC workloads.

---

<a id="323-policy-api-v1-orgs-default-projects-project-quality-vpcs-test-security-policy-match-expression-ff1dafa9-bgm74-subnets-pod-default-1289f64d-bgm74-status"></a>
### 323. /policy/api/v1/orgs/default/projects/project-quality/vpcs/test-security-policy-match-expression-ff1dafa9_bgm74/subnets/pod-default-1289f64d_bgm74/status

**HTTP Methods:** GET

**Explanation:**
VPC subnet management within a project. Defines IP address ranges and network segments for VPC workloads.

---

<a id="324-policy-api-v1-orgs-default-projects-project-quality-vpcs-test-lb-50fedbb3-mv836-subnets-pod-default-3cc5e9c8-mv836-ports-tea-mv836"></a>
### 324. /policy/api/v1/orgs/default/projects/project-quality/vpcs/test-lb-50fedbb3_mv836/subnets/pod-default-3cc5e9c8_mv836/ports/tea_mv836

**HTTP Methods:** DELETE, GET, PATCH

**Explanation:**
VPC subnet management within a project. Defines IP address ranges and network segments for VPC workloads.

**Request Body (PATCH):**
```json
{
  "attachment": {
    "allocate_addresses": "BOTH",
    "app_id": "a646f548-25f7-4baa-b1a8-7dc89ed47af0",
    "context_id": "80cedc6a-fa1c-4a55-b574-b23c89536d95",
    "id": "6854a882-dbf3-58b6-a636-74f8e4fbfa4a",
    "traffic_tag": 0,
    "type": "INDEPENDENT"
  },
  "display_name": "tea",
  "id": "tea_mv836",
  "parent_path": "/orgs/default/projects/project-quality/vpcs/test-lb-50fedbb3_mv836/subnets/pod-default-3cc5e9c8_mv836",
  "path": "/orgs/default/projects/project-quality/vpcs/test-lb-50fedbb3_mv836/subnets/pod-default-3cc5e9c8_mv836/ports/tea_mv836",
  "tags": [
    {
      "scope": "nsx-op/cluster",
      "tag": "f06fd228-8088-4439-a9e6-26c90a829c57"
    },
    {
      "scope": "nsx-op/version",
      "tag": "1.0.0"
    },
    {
      "scope": "nsx-op/namespace",
      "tag": "test-lb-50fedbb3"
    },
    {
      "scope": "nsx-op/pod_name",
      "tag": "tea"
    },
    {
      "scope": "nsx-op/pod_uid",
      "tag": "a646f548-25f7-4baa-b1a8-7dc89ed47af0"
    },
    {
      "scope": "nsx-op/namespace_uid",
      "tag": "2506fba2-2bca-42a9-9fb0-35aa09b1d33c"
    },
    {
      "scope": "app",
      "tag": "tea"
    },
    {
      "scope": "nsx-op-e2e",
      "tag": "tea"
    }
  ]
}
```

---

<a id="325-policy-api-v1-orgs-default-projects-project-quality-vpcs-client-91c3f484-qzuxu-subnets-pod-default-075e5037-qzuxu-ports-client-qzuxu"></a>
### 325. /policy/api/v1/orgs/default/projects/project-quality/vpcs/client-91c3f484_qzuxu/subnets/pod-default-075e5037_qzuxu/ports/client_qzuxu

**HTTP Methods:** DELETE, GET, PATCH

**Explanation:**
VPC subnet management within a project. Defines IP address ranges and network segments for VPC workloads.

**Request Body (PATCH):**
```json
{
  "attachment": {
    "allocate_addresses": "BOTH",
    "app_id": "f727dcc9-a668-431d-acae-9461c08ff943",
    "context_id": "56cd0d00-c51c-4381-bd8b-64a2a3ac9ab0",
    "id": "e858cd7e-9f1c-5919-8d42-931b510107bb",
    "traffic_tag": 0,
    "type": "INDEPENDENT"
  },
  "display_name": "client",
  "id": "client_qzuxu",
  "parent_path": "/orgs/default/projects/project-quality/vpcs/client-91c3f484_qzuxu/subnets/pod-default-075e5037_qzuxu",
  "path": "/orgs/default/projects/project-quality/vpcs/client-91c3f484_qzuxu/subnets/pod-default-075e5037_qzuxu/ports/client_qzuxu",
  "tags": [
    {
      "scope": "nsx-op/cluster",
      "tag": "f06fd228-8088-4439-a9e6-26c90a829c57"
    },
    {
      "scope": "nsx-op/version",
      "tag": "1.0.0"
    },
    {
      "scope": "nsx-op/namespace",
      "tag": "client-91c3f484"
    },
    {
      "scope": "nsx-op/pod_name",
      "tag": "client"
    },
    {
      "scope": "nsx-op/pod_uid",
      "tag": "f727dcc9-a668-431d-acae-9461c08ff943"
    },
    {
      "scope": "nsx-op/namespace_uid",
      "tag": "e19581fd-dbb5-4b0c-b896-e4fcff60f0ed"
    },
    {
      "scope": "role",
      "tag": "client"
    }
  ]
}
```

---

<a id="326-policy-api-v1-orgs-default-projects-project-quality-vpcs-subnet-e2e-1f11082b-56qvy-subnets-subnet-dhcp-56qvy-dhcp-server-config-stats"></a>
### 326. /policy/api/v1/orgs/default/projects/project-quality/vpcs/subnet-e2e-1f11082b_56qvy/subnets/subnet-dhcp_56qvy/dhcp-server-config/stats

**HTTP Methods:** GET

**Explanation:**
VPC subnet management within a project. Defines IP address ranges and network segments for VPC workloads.

---

<a id="327-policy-api-v1-orgs-default-projects-project-quality-vpcs-test-lb-50fedbb3-mv836-subnets-pod-default-3cc5e9c8-mv836-ports-coffee-mv836"></a>
### 327. /policy/api/v1/orgs/default/projects/project-quality/vpcs/test-lb-50fedbb3_mv836/subnets/pod-default-3cc5e9c8_mv836/ports/coffee_mv836

**HTTP Methods:** DELETE, GET, PATCH

**Explanation:**
VPC subnet management within a project. Defines IP address ranges and network segments for VPC workloads.

**Request Body (PATCH):**
```json
{
  "attachment": {
    "allocate_addresses": "BOTH",
    "app_id": "476b1f1d-9cdc-4184-869c-83a00aa04553",
    "context_id": "80cedc6a-fa1c-4a55-b574-b23c89536d95",
    "id": "2faea8c9-f6dd-516f-9242-38d88496f1b6",
    "traffic_tag": 0,
    "type": "INDEPENDENT"
  },
  "display_name": "coffee",
  "id": "coffee_mv836",
  "parent_path": "/orgs/default/projects/project-quality/vpcs/test-lb-50fedbb3_mv836/subnets/pod-default-3cc5e9c8_mv836",
  "path": "/orgs/default/projects/project-quality/vpcs/test-lb-50fedbb3_mv836/subnets/pod-default-3cc5e9c8_mv836/ports/coffee_mv836",
  "tags": [
    {
      "scope": "nsx-op/cluster",
      "tag": "f06fd228-8088-4439-a9e6-26c90a829c57"
    },
    {
      "scope": "nsx-op/version",
      "tag": "1.0.0"
    },
    {
      "scope": "nsx-op/namespace",
      "tag": "test-lb-50fedbb3"
    },
    {
      "scope": "nsx-op/pod_name",
      "tag": "coffee"
    },
    {
      "scope": "nsx-op/pod_uid",
      "tag": "476b1f1d-9cdc-4184-869c-83a00aa04553"
    },
    {
      "scope": "nsx-op/namespace_uid",
      "tag": "2506fba2-2bca-42a9-9fb0-35aa09b1d33c"
    },
    {
      "scope": "app",
      "tag": "coffee"
    },
    {
      "scope": "nsx-op-e2e",
      "tag": "coffee"
    }
  ]
}
```

---

<a id="328-policy-api-v1-orgs-default-projects-project-quality-vpcs-testvpc-7ab2d8aa-subnets-pod-default-e0268dd8-5583h-ports-prevpc-podvm-5583h"></a>
### 328. /policy/api/v1/orgs/default/projects/project-quality/vpcs/testvpc-7ab2d8aa/subnets/pod-default-e0268dd8_5583h/ports/prevpc-podvm_5583h

**HTTP Methods:** DELETE, GET, PATCH

**Explanation:**
VPC subnet management within a project. Defines IP address ranges and network segments for VPC workloads.

**Request Body (PATCH):**
```json
{
  "attachment": {
    "allocate_addresses": "BOTH",
    "app_id": "69267151-c3c9-4022-8a75-c4cded1dfb15",
    "context_id": "56cd0d00-c51c-4381-bd8b-64a2a3ac9ab0",
    "id": "3d5a12a9-afa8-53f6-a56d-0f4bac683d13",
    "traffic_tag": 0,
    "type": "INDEPENDENT"
  },
  "display_name": "prevpc-podvm",
  "id": "prevpc-podvm_5583h",
  "parent_path": "/orgs/default/projects/project-quality/vpcs/testvpc-7ab2d8aa/subnets/pod-default-e0268dd8_5583h",
  "path": "/orgs/default/projects/project-quality/vpcs/testvpc-7ab2d8aa/subnets/pod-default-e0268dd8_5583h/ports/prevpc-podvm_5583h",
  "tags": [
    {
      "scope": "nsx-op/cluster",
      "tag": "f06fd228-8088-4439-a9e6-26c90a829c57"
    },
    {
      "scope": "nsx-op/version",
      "tag": "1.0.0"
    },
    {
      "scope": "nsx-op/namespace",
      "tag": "test-prevpc-9f16bff1"
    },
    {
      "scope": "nsx-op/pod_name",
      "tag": "prevpc-podvm"
    },
    {
      "scope": "nsx-op/pod_uid",
      "tag": "69267151-c3c9-4022-8a75-c4cded1dfb15"
    },
    {
      "scope": "nsx-op/namespace_uid",
      "tag": "a0a91583-c678-4a6d-8e23-f699d12140c4"
    },
    {
      "scope": "app",
      "tag": "prevpc-podvm"
    },
    {
      "scope": "nsx-op-e2e",
      "tag": "prevpc-podvm"
    }
  ]
}
```

---

<a id="329-policy-api-v1-orgs-default-projects-project-quality-vpcs-test-lb-50fedbb3-mv836-subnets-pod-default-3cc5e9c8-mv836-ports-default-mv836"></a>
### 329. /policy/api/v1/orgs/default/projects/project-quality/vpcs/test-lb-50fedbb3_mv836/subnets/pod-default-3cc5e9c8_mv836/ports/default_mv836

**HTTP Methods:** DELETE, GET, PATCH

**Explanation:**
VPC subnet management within a project. Defines IP address ranges and network segments for VPC workloads.

**Request Body (PATCH):**
```json
{
  "attachment": {
    "allocate_addresses": "BOTH",
    "app_id": "fcf92e19-f055-498e-9732-0bdee388318c",
    "context_id": "56cd0d00-c51c-4381-bd8b-64a2a3ac9ab0",
    "id": "09f4d815-b68a-5f16-8b6f-9013fe42f38a",
    "traffic_tag": 0,
    "type": "INDEPENDENT"
  },
  "display_name": "default",
  "id": "default_mv836",
  "parent_path": "/orgs/default/projects/project-quality/vpcs/test-lb-50fedbb3_mv836/subnets/pod-default-3cc5e9c8_mv836",
  "path": "/orgs/default/projects/project-quality/vpcs/test-lb-50fedbb3_mv836/subnets/pod-default-3cc5e9c8_mv836/ports/default_mv836",
  "tags": [
    {
      "scope": "nsx-op/cluster",
      "tag": "f06fd228-8088-4439-a9e6-26c90a829c57"
    },
    {
      "scope": "nsx-op/version",
      "tag": "1.0.0"
    },
    {
      "scope": "nsx-op/namespace",
      "tag": "test-lb-50fedbb3"
    },
    {
      "scope": "nsx-op/pod_name",
      "tag": "default"
    },
    {
      "scope": "nsx-op/pod_uid",
      "tag": "fcf92e19-f055-498e-9732-0bdee388318c"
    },
    {
      "scope": "nsx-op/namespace_uid",
      "tag": "2506fba2-2bca-42a9-9fb0-35aa09b1d33c"
    },
    {
      "scope": "app",
      "tag": "default"
    },
    {
      "scope": "nsx-op-e2e",
      "tag": "default"
    }
  ]
}
```

---

<a id="330-policy-api-v1-orgs-default-projects-project-quality-vpcs-subnet-e2e-1f11082b-56qvy-subnets-subnet-cidr-56qvy-ports-port-with-ip-1-56qvy"></a>
### 330. /policy/api/v1/orgs/default/projects/project-quality/vpcs/subnet-e2e-1f11082b_56qvy/subnets/subnet-cidr_56qvy/ports/port-with-ip-1_56qvy

**HTTP Methods:** DELETE, GET, PATCH

**Explanation:**
VPC subnet management within a project. Defines IP address ranges and network segments for VPC workloads.

**Request Body (PATCH):**
```json
{
  "address_bindings": [
    {
      "ip_address": "172.26.0.132"
    }
  ],
  "attachment": {
    "allocate_addresses": "BOTH",
    "id": "531ae000-2df2-5bd2-bebd-0efdb0ca25f9",
    "traffic_tag": 0,
    "type": "INDEPENDENT"
  },
  "display_name": "port-with-ip-1",
  "id": "port-with-ip-1_56qvy",
  "parent_path": "/orgs/default/projects/project-quality/vpcs/subnet-e2e-1f11082b_56qvy/subnets/subnet-cidr_56qvy",
  "path": "/orgs/default/projects/project-quality/vpcs/subnet-e2e-1f11082b_56qvy/subnets/subnet-cidr_56qvy/ports/port-with-ip-1_56qvy",
  "tags": [
    {
      "scope": "nsx-op/cluster",
      "tag": "f06fd228-8088-4439-a9e6-26c90a829c57"
    },
    {
      "scope": "nsx-op/version",
      "tag": "1.0.0"
    },
    {
      "scope": "nsx-op/vm_namespace",
      "tag": "subnet-e2e-1f11082b"
    },
    {
      "scope": "nsx-op/vm_namespace_uid",
      "tag": "f629b82e-5ea2-4298-b1cf-3bafcea373fa"
    },
    {
      "scope": "nsx-op/subnetport_name",
      "tag": "port-with-ip-1"
    },
    {
      "scope": "nsx-op/subnetport_uid",
      "tag": "ae28d216-5476-4b8c-b033-2344c567c297"
    }
  ]
}
```

---

<a id="331-policy-api-v1-orgs-default-projects-project-quality-vpcs-subnet-e2e-1f11082b-56qvy-subnets-subnet-cidr-56qvy-ports-port-with-ip-2-56qvy"></a>
### 331. /policy/api/v1/orgs/default/projects/project-quality/vpcs/subnet-e2e-1f11082b_56qvy/subnets/subnet-cidr_56qvy/ports/port-with-ip-2_56qvy

**HTTP Methods:** DELETE, GET, PATCH

**Explanation:**
VPC subnet management within a project. Defines IP address ranges and network segments for VPC workloads.

**Request Body (PATCH):**
```json
{
  "address_bindings": [
    {
      "ip_address": "172.26.0.133",
      "mac_address": "ff:50:56:00:00:00"
    }
  ],
  "attachment": {
    "allocate_addresses": "IP_POOL",
    "id": "ff125813-d987-5297-a922-bcdd7de869e5",
    "traffic_tag": 0,
    "type": "INDEPENDENT"
  },
  "display_name": "port-with-ip-2",
  "id": "port-with-ip-2_56qvy",
  "parent_path": "/orgs/default/projects/project-quality/vpcs/subnet-e2e-1f11082b_56qvy/subnets/subnet-cidr_56qvy",
  "path": "/orgs/default/projects/project-quality/vpcs/subnet-e2e-1f11082b_56qvy/subnets/subnet-cidr_56qvy/ports/port-with-ip-2_56qvy",
  "tags": [
    {
      "scope": "nsx-op/cluster",
      "tag": "f06fd228-8088-4439-a9e6-26c90a829c57"
    },
    {
      "scope": "nsx-op/version",
      "tag": "1.0.0"
    },
    {
      "scope": "nsx-op/vm_namespace",
      "tag": "subnet-e2e-1f11082b"
    },
    {
      "scope": "nsx-op/vm_namespace_uid",
      "tag": "f629b82e-5ea2-4298-b1cf-3bafcea373fa"
    },
    {
      "scope": "nsx-op/subnetport_name",
      "tag": "port-with-ip-2"
    },
    {
      "scope": "nsx-op/subnetport_uid",
      "tag": "486497aa-83fc-4b10-98e8-0e9dff4a46d1"
    }
  ]
}
```

---

<a id="332-policy-api-v1-orgs-default-projects-project-quality-vpcs-subnet-e2e-1f11082b-56qvy-subnets-subnet-cidr-56qvy-ports-port-with-ip-3-56qvy"></a>
### 332. /policy/api/v1/orgs/default/projects/project-quality/vpcs/subnet-e2e-1f11082b_56qvy/subnets/subnet-cidr_56qvy/ports/port-with-ip-3_56qvy

**HTTP Methods:** DELETE, PATCH

**Explanation:**
VPC subnet management within a project. Defines IP address ranges and network segments for VPC workloads.

**Request Body (PATCH):**
```json
{
  "address_bindings": [
    {
      "ip_address": "164.249.93.47"
    }
  ],
  "attachment": {
    "allocate_addresses": "BOTH",
    "id": "0ae2ef9d-7a01-5b9d-9928-4860214db399",
    "traffic_tag": 0,
    "type": "INDEPENDENT"
  },
  "display_name": "port-with-ip-3",
  "id": "port-with-ip-3_56qvy",
  "parent_path": "/orgs/default/projects/project-quality/vpcs/subnet-e2e-1f11082b_56qvy/subnets/subnet-cidr_56qvy",
  "path": "/orgs/default/projects/project-quality/vpcs/subnet-e2e-1f11082b_56qvy/subnets/subnet-cidr_56qvy/ports/port-with-ip-3_56qvy",
  "tags": [
    {
      "scope": "nsx-op/cluster",
      "tag": "f06fd228-8088-4439-a9e6-26c90a829c57"
    },
    {
      "scope": "nsx-op/version",
      "tag": "1.0.0"
    },
    {
      "scope": "nsx-op/vm_namespace",
      "tag": "subnet-e2e-1f11082b"
    },
    {
      "scope": "nsx-op/vm_namespace_uid",
      "tag": "f629b82e-5ea2-4298-b1cf-3bafcea373fa"
    },
    {
      "scope": "nsx-op/subnetport_name",
      "tag": "port-with-ip-3"
    },
    {
      "scope": "nsx-op/subnetport_uid",
      "tag": "3247c8bd-b8a1-470e-826c-2bfede071194"
    }
  ]
}
```

---

<a id="333-policy-api-v1-orgs-default-projects-project-quality-vpcs-subnet-e2e-1f11082b-56qvy-subnets-subnet-cidr-56qvy-ip-pools-static-ipv4-default"></a>
### 333. /policy/api/v1/orgs/default/projects/project-quality/vpcs/subnet-e2e-1f11082b_56qvy/subnets/subnet-cidr_56qvy/ip-pools/static-ipv4-default

**HTTP Methods:** GET

**Explanation:**
VPC subnet management within a project. Defines IP address ranges and network segments for VPC workloads.

---

<a id="334-policy-api-v1-orgs-default-projects-project-quality-vpcs-testvpc-3658f2b5-subnets-pod-default-ec7c1039-d5d7u-ip-pools-static-ipv4-default"></a>
### 334. /policy/api/v1/orgs/default/projects/project-quality/vpcs/testvpc-3658f2b5/subnets/pod-default-ec7c1039_d5d7u/ip-pools/static-ipv4-default

**HTTP Methods:** GET

**Explanation:**
VPC subnet management within a project. Defines IP address ranges and network segments for VPC workloads.

---

<a id="335-policy-api-v1-orgs-default-projects-project-quality-vpcs-testvpc-7ab2d8aa-subnets-pod-default-e0268dd8-5583h-ip-pools-static-ipv4-default"></a>
### 335. /policy/api/v1/orgs/default/projects/project-quality/vpcs/testvpc-7ab2d8aa/subnets/pod-default-e0268dd8_5583h/ip-pools/static-ipv4-default

**HTTP Methods:** GET

**Explanation:**
VPC subnet management within a project. Defines IP address ranges and network segments for VPC workloads.

---

<a id="336-policy-api-v1-orgs-default-projects-project-quality-vpcs-testvpc-3658f2b5-subnets-pod-default-ec7c1039-d5d7u-ports-prevpc-client-pod-d5d7u"></a>
### 336. /policy/api/v1/orgs/default/projects/project-quality/vpcs/testvpc-3658f2b5/subnets/pod-default-ec7c1039_d5d7u/ports/prevpc-client-pod_d5d7u

**HTTP Methods:** DELETE, GET, PATCH

**Explanation:**
VPC subnet management within a project. Defines IP address ranges and network segments for VPC workloads.

**Request Body (PATCH):**
```json
{
  "attachment": {
    "allocate_addresses": "BOTH",
    "app_id": "1290466a-4910-4900-ab21-892aec1f51ed",
    "context_id": "80cedc6a-fa1c-4a55-b574-b23c89536d95",
    "id": "f5068e47-09ab-501d-88c4-5ef3c2046fd5",
    "traffic_tag": 0,
    "type": "INDEPENDENT"
  },
  "display_name": "prevpc-client-pod",
  "id": "prevpc-client-pod_d5d7u",
  "parent_path": "/orgs/default/projects/project-quality/vpcs/testvpc-3658f2b5/subnets/pod-default-ec7c1039_d5d7u",
  "path": "/orgs/default/projects/project-quality/vpcs/testvpc-3658f2b5/subnets/pod-default-ec7c1039_d5d7u/ports/prevpc-client-pod_d5d7u",
  "tags": [
    {
      "scope": "nsx-op/cluster",
      "tag": "f06fd228-8088-4439-a9e6-26c90a829c57"
    },
    {
      "scope": "nsx-op/version",
      "tag": "1.0.0"
    },
    {
      "scope": "nsx-op/namespace",
      "tag": "test-prevpc-8f1a464f"
    },
    {
      "scope": "nsx-op/pod_name",
      "tag": "prevpc-client-pod"
    },
    {
      "scope": "nsx-op/pod_uid",
      "tag": "1290466a-4910-4900-ab21-892aec1f51ed"
    },
    {
      "scope": "nsx-op/namespace_uid",
      "tag": "87995f00-857e-41a2-8687-41656a792cf7"
    },
    {
      "scope": "app",
      "tag": "prevpc-client-pod"
    },
    {
      "scope": "nsx-op-e2e",
      "tag": "prevpc-client-pod"
    }
  ]
}
```

---

<a id="337-policy-api-v1-orgs-default-projects-project-quality-vpcs-testvpc-3658f2b5-subnets-pod-default-ec7c1039-d5d7u-ports-prevpc-service-pod-d5d7u"></a>
### 337. /policy/api/v1/orgs/default/projects/project-quality/vpcs/testvpc-3658f2b5/subnets/pod-default-ec7c1039_d5d7u/ports/prevpc-service-pod_d5d7u

**HTTP Methods:** DELETE, GET, PATCH

**Explanation:**
VPC subnet management within a project. Defines IP address ranges and network segments for VPC workloads.

**Request Body (PATCH):**
```json
{
  "attachment": {
    "allocate_addresses": "BOTH",
    "app_id": "4610957b-33d9-4e57-8c58-ea7cf48b0090",
    "context_id": "56cd0d00-c51c-4381-bd8b-64a2a3ac9ab0",
    "id": "ce1cae3e-0aaa-5984-be2a-0b65404b99b8",
    "traffic_tag": 0,
    "type": "INDEPENDENT"
  },
  "display_name": "prevpc-service-pod",
  "id": "prevpc-service-pod_d5d7u",
  "parent_path": "/orgs/default/projects/project-quality/vpcs/testvpc-3658f2b5/subnets/pod-default-ec7c1039_d5d7u",
  "path": "/orgs/default/projects/project-quality/vpcs/testvpc-3658f2b5/subnets/pod-default-ec7c1039_d5d7u/ports/prevpc-service-pod_d5d7u",
  "tags": [
    {
      "scope": "nsx-op/cluster",
      "tag": "f06fd228-8088-4439-a9e6-26c90a829c57"
    },
    {
      "scope": "nsx-op/version",
      "tag": "1.0.0"
    },
    {
      "scope": "nsx-op/namespace",
      "tag": "test-prevpc-8f1a464f"
    },
    {
      "scope": "nsx-op/pod_name",
      "tag": "prevpc-service-pod"
    },
    {
      "scope": "nsx-op/pod_uid",
      "tag": "4610957b-33d9-4e57-8c58-ea7cf48b0090"
    },
    {
      "scope": "nsx-op/namespace_uid",
      "tag": "87995f00-857e-41a2-8687-41656a792cf7"
    },
    {
      "scope": "app",
      "tag": "prevpc-service-pod"
    },
    {
      "scope": "nsx-op-e2e",
      "tag": "prevpc-service-pod"
    },
    {
      "scope": "prevpc-test",
      "tag": "prevpc-loadbalancer"
    }
  ]
}
```

---

<a id="338-policy-api-v1-orgs-default-projects-project-quality-vpcs-web-da775e6f-6o7ts-subnets-pod-default-a734dd59-6o7ts-ip-pools-static-ipv4-default"></a>
### 338. /policy/api/v1/orgs/default/projects/project-quality/vpcs/web-da775e6f_6o7ts/subnets/pod-default-a734dd59_6o7ts/ip-pools/static-ipv4-default

**HTTP Methods:** GET

**Explanation:**
VPC subnet management within a project. Defines IP address ranges and network segments for VPC workloads.

---

<a id="339-policy-api-v1-orgs-default-projects-project-quality-vpcs-client-91c3f484-qzuxu-subnets-pod-default-075e5037-qzuxu-ip-pools-static-ipv4-default"></a>
### 339. /policy/api/v1/orgs/default/projects/project-quality/vpcs/client-91c3f484_qzuxu/subnets/pod-default-075e5037_qzuxu/ip-pools/static-ipv4-default

**HTTP Methods:** GET

**Explanation:**
VPC subnet management within a project. Defines IP address ranges and network segments for VPC workloads.

---

<a id="340-policy-api-v1-orgs-default-projects-project-quality-vpcs-subnet-e2e-1f11082b-56qvy-subnets-subnet-no-ip-56qvy-ports-port-in-no-ip-subnet-56qvy"></a>
### 340. /policy/api/v1/orgs/default/projects/project-quality/vpcs/subnet-e2e-1f11082b_56qvy/subnets/subnet-no-ip_56qvy/ports/port-in-no-ip-subnet_56qvy

**HTTP Methods:** DELETE, GET, PATCH

**Explanation:**
VPC subnet management within a project. Defines IP address ranges and network segments for VPC workloads.

**Request Body (PATCH):**
```json
{
  "attachment": {
    "allocate_addresses": "NONE",
    "id": "08b2df9b-94b3-5906-96ec-2e0d293076ca",
    "traffic_tag": 0,
    "type": "INDEPENDENT"
  },
  "display_name": "port-in-no-ip-subnet",
  "id": "port-in-no-ip-subnet_56qvy",
  "parent_path": "/orgs/default/projects/project-quality/vpcs/subnet-e2e-1f11082b_56qvy/subnets/subnet-no-ip_56qvy",
  "path": "/orgs/default/projects/project-quality/vpcs/subnet-e2e-1f11082b_56qvy/subnets/subnet-no-ip_56qvy/ports/port-in-no-ip-subnet_56qvy",
  "tags": [
    {
      "scope": "nsx-op/cluster",
      "tag": "f06fd228-8088-4439-a9e6-26c90a829c57"
    },
    {
      "scope": "nsx-op/version",
      "tag": "1.0.0"
    },
    {
      "scope": "nsx-op/vm_namespace",
      "tag": "subnet-e2e-1f11082b"
    },
    {
      "scope": "nsx-op/vm_namespace_uid",
      "tag": "f629b82e-5ea2-4298-b1cf-3bafcea373fa"
    },
    {
      "scope": "nsx-op/subnetport_name",
      "tag": "port-in-no-ip-subnet"
    },
    {
      "scope": "nsx-op/subnetport_uid",
      "tag": "82a71c00-8a36-484b-ba65-c2cdfee8164b"
    }
  ]
}
```

---

<a id="341-policy-api-v1-orgs-default-projects-project-quality-vpcs-target-ns-56446c91-6zdip-subnets-vm-default-eb532fd0-c6gls-ports-port-e2e-test-3-c6gls"></a>
### 341. /policy/api/v1/orgs/default/projects/project-quality/vpcs/target-ns-56446c91_6zdip/subnets/vm-default-eb532fd0_c6gls/ports/port-e2e-test-3_c6gls

**HTTP Methods:** DELETE, GET, PATCH

**Explanation:**
VPC subnet management within a project. Defines IP address ranges and network segments for VPC workloads.

**Request Body (PATCH):**
```json
{
  "attachment": {
    "allocate_addresses": "BOTH",
    "id": "612df564-f7f5-51b0-8838-7a57c327362f",
    "traffic_tag": 0,
    "type": "INDEPENDENT"
  },
  "display_name": "port-e2e-test-3",
  "id": "port-e2e-test-3_c6gls",
  "parent_path": "/orgs/default/projects/project-quality/vpcs/target-ns-56446c91_6zdip/subnets/vm-default-eb532fd0_c6gls",
  "path": "/orgs/default/projects/project-quality/vpcs/target-ns-56446c91_6zdip/subnets/vm-default-eb532fd0_c6gls/ports/port-e2e-test-3_c6gls",
  "tags": [
    {
      "scope": "nsx-op/cluster",
      "tag": "f06fd228-8088-4439-a9e6-26c90a829c57"
    },
    {
      "scope": "nsx-op/version",
      "tag": "1.0.0"
    },
    {
      "scope": "nsx-op/vm_namespace",
      "tag": "subnet-e2e-shared-05b500ba"
    },
    {
      "scope": "nsx-op/vm_namespace_uid",
      "tag": "b8c362f7-3bda-4a5b-8cad-cd7a79b4f372"
    },
    {
      "scope": "nsx-op/subnetport_name",
      "tag": "port-e2e-test-3"
    },
    {
      "scope": "nsx-op/subnetport_uid",
      "tag": "ae26d2bb-d32d-436c-a7fc-487ab7199258"
    }
  ]
}
```

---

<a id="342-policy-api-v1-orgs-default-projects-project-quality-vpcs-test-lb-50fedbb3-mv836-subnets-pod-default-3cc5e9c8-mv836-ip-pools-static-ipv4-default"></a>
### 342. /policy/api/v1/orgs/default/projects/project-quality/vpcs/test-lb-50fedbb3_mv836/subnets/pod-default-3cc5e9c8_mv836/ip-pools/static-ipv4-default

**HTTP Methods:** GET

**Explanation:**
VPC subnet management within a project. Defines IP address ranges and network segments for VPC workloads.

---

<a id="343-policy-api-v1-orgs-default-projects-project-quality-vpcs-target-ns-56446c91-6zdip-subnets-vm-default-eb532fd0-c6gls-ip-pools-static-ipv4-default"></a>
### 343. /policy/api/v1/orgs/default/projects/project-quality/vpcs/target-ns-56446c91_6zdip/subnets/vm-default-eb532fd0_c6gls/ip-pools/static-ipv4-default

**HTTP Methods:** GET

**Explanation:**
VPC subnet management within a project. Defines IP address ranges and network segments for VPC workloads.

---

<a id="344-policy-api-v1-orgs-default-projects-project-quality-vpcs-test-pod-1dd9a577-fu9t5-subnets-pod-default-5cf92338-fu9t5-ip-pools-static-ipv4-default"></a>
### 344. /policy/api/v1/orgs/default/projects/project-quality/vpcs/test-pod-1dd9a577_fu9t5/subnets/pod-default-5cf92338_fu9t5/ip-pools/static-ipv4-default

**HTTP Methods:** GET

**Explanation:**
VPC subnet management within a project. Defines IP address ranges and network segments for VPC workloads.

---

<a id="345-policy-api-v1-orgs-default-projects-project-quality-vpcs-subnet-e2e-1f11082b-56qvy-subnets-pod-default-6a81803a-56qvy-ports-port-e2e-test-1-56qvy"></a>
### 345. /policy/api/v1/orgs/default/projects/project-quality/vpcs/subnet-e2e-1f11082b_56qvy/subnets/pod-default-6a81803a_56qvy/ports/port-e2e-test-1_56qvy

**HTTP Methods:** DELETE, GET, PATCH

**Explanation:**
VPC subnet management within a project. Defines IP address ranges and network segments for VPC workloads.

**Request Body (PATCH):**
```json
{
  "attachment": {
    "allocate_addresses": "BOTH",
    "id": "43883720-0d8c-5c38-84bf-eb0561318d2f",
    "traffic_tag": 0,
    "type": "INDEPENDENT"
  },
  "display_name": "port-e2e-test-1",
  "id": "port-e2e-test-1_56qvy",
  "parent_path": "/orgs/default/projects/project-quality/vpcs/subnet-e2e-1f11082b_56qvy/subnets/pod-default-6a81803a_56qvy",
  "path": "/orgs/default/projects/project-quality/vpcs/subnet-e2e-1f11082b_56qvy/subnets/pod-default-6a81803a_56qvy/ports/port-e2e-test-1_56qvy",
  "tags": [
    {
      "scope": "nsx-op/cluster",
      "tag": "f06fd228-8088-4439-a9e6-26c90a829c57"
    },
    {
      "scope": "nsx-op/version",
      "tag": "1.0.0"
    },
    {
      "scope": "nsx-op/vm_namespace",
      "tag": "subnet-e2e-1f11082b"
    },
    {
      "scope": "nsx-op/vm_namespace_uid",
      "tag": "f629b82e-5ea2-4298-b1cf-3bafcea373fa"
    },
    {
      "scope": "nsx-op/subnetport_name",
      "tag": "port-e2e-test-1"
    },
    {
      "scope": "nsx-op/subnetport_uid",
      "tag": "31c9ac43-db10-418f-aca8-baf8d8e50e0a"
    }
  ]
}
```

---

<a id="346-policy-api-v1-orgs-default-projects-project-quality-vpcs-subnet-e2e-1f11082b-56qvy-subnets-pod-default-6a81803a-56qvy-ip-pools-static-ipv4-default"></a>
### 346. /policy/api/v1/orgs/default/projects/project-quality/vpcs/subnet-e2e-1f11082b_56qvy/subnets/pod-default-6a81803a_56qvy/ip-pools/static-ipv4-default

**HTTP Methods:** GET

**Explanation:**
VPC subnet management within a project. Defines IP address ranges and network segments for VPC workloads.

---

<a id="347-policy-api-v1-orgs-default-projects-project-quality-vpcs-test-create-vm-basic-f449d9bf-3ehn6-subnets-public-subnet-3ehn6-ip-pools-static-ipv4-default"></a>
### 347. /policy/api/v1/orgs/default/projects/project-quality/vpcs/test-create-vm-basic-f449d9bf_3ehn6/subnets/public-subnet_3ehn6/ip-pools/static-ipv4-default

**HTTP Methods:** GET

**Explanation:**
VPC subnet management within a project. Defines IP address ranges and network segments for VPC workloads.

---

<a id="348-policy-api-v1-orgs-default-projects-project-quality-vpcs-test-pod-sync-e8b8a7ca-m404i-subnets-pod-default-0dd88421-m404i-ip-pools-static-ipv4-default"></a>
### 348. /policy/api/v1/orgs/default/projects/project-quality/vpcs/test-pod-sync-e8b8a7ca_m404i/subnets/pod-default-0dd88421_m404i/ip-pools/static-ipv4-default

**HTTP Methods:** GET

**Explanation:**
VPC subnet management within a project. Defines IP address ranges and network segments for VPC workloads.

---

<a id="349-policy-api-v1-orgs-default-projects-project-quality-vpcs-subnet-e2e-1f11082b-56qvy-subnets-user-subnetset-dhcp-c85186d8-56qvy-dhcp-server-config-stats"></a>
### 349. /policy/api/v1/orgs/default/projects/project-quality/vpcs/subnet-e2e-1f11082b_56qvy/subnets/user-subnetset-dhcp-c85186d8_56qvy/dhcp-server-config/stats

**HTTP Methods:** GET

**Explanation:**
VPC subnet management within a project. Defines IP address ranges and network segments for VPC workloads.

---

<a id="350-policy-api-v1-orgs-default-projects-project-quality-vpcs-test-pod-sync-e8b8a7ca-m404i-subnets-pod-default-0dd88421-m404i-ports-test-pod-32c0f6bc-m404i"></a>
### 350. /policy/api/v1/orgs/default/projects/project-quality/vpcs/test-pod-sync-e8b8a7ca_m404i/subnets/pod-default-0dd88421_m404i/ports/test-pod-32c0f6bc_m404i

**HTTP Methods:** DELETE, GET, PATCH

**Explanation:**
VPC subnet management within a project. Defines IP address ranges and network segments for VPC workloads.

**Request Body (PATCH):**
```json
{
  "attachment": {
    "allocate_addresses": "BOTH",
    "app_id": "a35c0731-4635-4a5b-93dc-a2bbb9567cde",
    "context_id": "56cd0d00-c51c-4381-bd8b-64a2a3ac9ab0",
    "id": "8be67176-1710-5d16-8260-a5015b7df6d0",
    "traffic_tag": 0,
    "type": "INDEPENDENT"
  },
  "display_name": "test-pod-32c0f6bc",
  "id": "test-pod-32c0f6bc_m404i",
  "parent_path": "/orgs/default/projects/project-quality/vpcs/test-pod-sync-e8b8a7ca_m404i/subnets/pod-default-0dd88421_m404i",
  "path": "/orgs/default/projects/project-quality/vpcs/test-pod-sync-e8b8a7ca_m404i/subnets/pod-default-0dd88421_m404i/ports/test-pod-32c0f6bc_m404i",
  "tags": [
    {
      "scope": "nsx-op/cluster",
      "tag": "f06fd228-8088-4439-a9e6-26c90a829c57"
    },
    {
      "scope": "nsx-op/version",
      "tag": "1.0.0"
    },
    {
      "scope": "nsx-op/namespace",
      "tag": "test-pod-sync-e8b8a7ca"
    },
    {
      "scope": "nsx-op/pod_name",
      "tag": "test-pod-32c0f6bc"
    },
    {
      "scope": "nsx-op/pod_uid",
      "tag": "a35c0731-4635-4a5b-93dc-a2bbb9567cde"
    },
    {
      "scope": "nsx-op/namespace_uid",
      "tag": "df28714f-bbd0-4ac5-bfaa-13716c242ac0"
    },
    {
      "scope": "app",
      "tag": "test-pod-32c0f6bc"
    },
    {
      "scope": "nsx-op-e2e",
      "tag": "test-pod-32c0f6bc"
    }
  ]
}
```

---

<a id="351-policy-api-v1-orgs-default-projects-project-quality-vpcs-test-pod-1dd9a577-fu9t5-subnets-pod-default-5cf92338-fu9t5-ports-test-source-pod-f9ba0670-fu9t5"></a>
### 351. /policy/api/v1/orgs/default/projects/project-quality/vpcs/test-pod-1dd9a577_fu9t5/subnets/pod-default-5cf92338_fu9t5/ports/test-source-pod-f9ba0670_fu9t5

**HTTP Methods:** DELETE, GET, PATCH

**Explanation:**
VPC subnet management within a project. Defines IP address ranges and network segments for VPC workloads.

**Request Body (PATCH):**
```json
{
  "attachment": {
    "allocate_addresses": "BOTH",
    "app_id": "c9acc384-0f2a-4542-9495-ed60c5b8fc3a",
    "context_id": "56cd0d00-c51c-4381-bd8b-64a2a3ac9ab0",
    "id": "0f667210-9517-584c-938b-90dc141c9d24",
    "traffic_tag": 0,
    "type": "INDEPENDENT"
  },
  "display_name": "test-source-pod-f9ba0670",
  "id": "test-source-pod-f9ba0670_fu9t5",
  "parent_path": "/orgs/default/projects/project-quality/vpcs/test-pod-1dd9a577_fu9t5/subnets/pod-default-5cf92338_fu9t5",
  "path": "/orgs/default/projects/project-quality/vpcs/test-pod-1dd9a577_fu9t5/subnets/pod-default-5cf92338_fu9t5/ports/test-source-pod-f9ba0670_fu9t5",
  "tags": [
    {
      "scope": "nsx-op/cluster",
      "tag": "f06fd228-8088-4439-a9e6-26c90a829c57"
    },
    {
      "scope": "nsx-op/version",
      "tag": "1.0.0"
    },
    {
      "scope": "nsx-op/namespace",
      "tag": "test-pod-1dd9a577"
    },
    {
      "scope": "nsx-op/pod_name",
      "tag": "test-source-pod-f9ba0670"
    },
    {
      "scope": "nsx-op/pod_uid",
      "tag": "c9acc384-0f2a-4542-9495-ed60c5b8fc3a"
    },
    {
      "scope": "nsx-op/namespace_uid",
      "tag": "6c0816d9-ed05-4f26-91d1-b87dae8e9c1b"
    },
    {
      "scope": "app",
      "tag": "test-source-pod-f9ba0670"
    },
    {
      "scope": "nsx-op-e2e",
      "tag": "test-source-pod-f9ba0670"
    }
  ]
}
```

---

<a id="352-policy-api-v1-orgs-default-projects-project-quality-vpcs-web-da775e6f-6o7ts-subnets-pod-default-a734dd59-6o7ts-ports-tcp-deployment-56bcbfc896-s7rng-6o7ts"></a>
### 352. /policy/api/v1/orgs/default/projects/project-quality/vpcs/web-da775e6f_6o7ts/subnets/pod-default-a734dd59_6o7ts/ports/tcp-deployment-56bcbfc896-s7rng_6o7ts

**HTTP Methods:** DELETE, GET, PATCH

**Explanation:**
VPC subnet management within a project. Defines IP address ranges and network segments for VPC workloads.

**Request Body (PATCH):**
```json
{
  "attachment": {
    "allocate_addresses": "BOTH",
    "app_id": "4b3969fe-5aa6-40b3-ae51-ec6309c60dab",
    "context_id": "56cd0d00-c51c-4381-bd8b-64a2a3ac9ab0",
    "id": "6434a7ee-f72e-58c5-93f3-49f4fcc49eb1",
    "traffic_tag": 0,
    "type": "INDEPENDENT"
  },
  "display_name": "tcp-deployment-56bcbfc896-s7rng",
  "id": "tcp-deployment-56bcbfc896-s7rng_6o7ts",
  "parent_path": "/orgs/default/projects/project-quality/vpcs/web-da775e6f_6o7ts/subnets/pod-default-a734dd59_6o7ts",
  "path": "/orgs/default/projects/project-quality/vpcs/web-da775e6f_6o7ts/subnets/pod-default-a734dd59_6o7ts/ports/tcp-deployment-56bcbfc896-s7rng_6o7ts",
  "tags": [
    {
      "scope": "nsx-op/cluster",
      "tag": "f06fd228-8088-4439-a9e6-26c90a829c57"
    },
    {
      "scope": "nsx-op/version",
      "tag": "1.0.0"
    },
    {
      "scope": "nsx-op/namespace",
      "tag": "web-da775e6f"
    },
    {
      "scope": "nsx-op/pod_name",
      "tag": "tcp-deployment-56bcbfc896-s7rng"
    },
    {
      "scope": "nsx-op/pod_uid",
      "tag": "4b3969fe-5aa6-40b3-ae51-ec6309c60dab"
    },
    {
      "scope": "nsx-op/namespace_uid",
      "tag": "d114a0e0-d12c-41ac-9435-213fd199fa7b"
    },
    {
      "scope": "deployment",
      "tag": "tcp-deployment"
    },
    {
      "scope": "pod-template-hash",
      "tag": "56bcbfc896"
    },
    {
      "scope": "role",
      "tag": "web"
    }
  ]
}
```

---

<a id="353-policy-api-v1-orgs-default-projects-project-quality-vpcs-web-da775e6f-6o7ts-subnets-pod-default-a734dd59-6o7ts-ports-tcp-deployment-56bcbfc896-xs2hs-6o7ts"></a>
### 353. /policy/api/v1/orgs/default/projects/project-quality/vpcs/web-da775e6f_6o7ts/subnets/pod-default-a734dd59_6o7ts/ports/tcp-deployment-56bcbfc896-xs2hs_6o7ts

**HTTP Methods:** DELETE, GET, PATCH

**Explanation:**
VPC subnet management within a project. Defines IP address ranges and network segments for VPC workloads.

**Request Body (PATCH):**
```json
{
  "attachment": {
    "allocate_addresses": "BOTH",
    "app_id": "684bd69e-6e81-41d3-a072-81bfe404c6a3",
    "context_id": "80cedc6a-fa1c-4a55-b574-b23c89536d95",
    "id": "55334ac6-a8c4-507d-b43d-5f7a386eaf9b",
    "traffic_tag": 0,
    "type": "INDEPENDENT"
  },
  "display_name": "tcp-deployment-56bcbfc896-xs2hs",
  "id": "tcp-deployment-56bcbfc896-xs2hs_6o7ts",
  "parent_path": "/orgs/default/projects/project-quality/vpcs/web-da775e6f_6o7ts/subnets/pod-default-a734dd59_6o7ts",
  "path": "/orgs/default/projects/project-quality/vpcs/web-da775e6f_6o7ts/subnets/pod-default-a734dd59_6o7ts/ports/tcp-deployment-56bcbfc896-xs2hs_6o7ts",
  "tags": [
    {
      "scope": "nsx-op/cluster",
      "tag": "f06fd228-8088-4439-a9e6-26c90a829c57"
    },
    {
      "scope": "nsx-op/version",
      "tag": "1.0.0"
    },
    {
      "scope": "nsx-op/namespace",
      "tag": "web-da775e6f"
    },
    {
      "scope": "nsx-op/pod_name",
      "tag": "tcp-deployment-56bcbfc896-xs2hs"
    },
    {
      "scope": "nsx-op/pod_uid",
      "tag": "684bd69e-6e81-41d3-a072-81bfe404c6a3"
    },
    {
      "scope": "nsx-op/namespace_uid",
      "tag": "d114a0e0-d12c-41ac-9435-213fd199fa7b"
    },
    {
      "scope": "deployment",
      "tag": "tcp-deployment"
    },
    {
      "scope": "pod-template-hash",
      "tag": "56bcbfc896"
    },
    {
      "scope": "role",
      "tag": "web"
    }
  ]
}
```

---

<a id="354-policy-api-v1-orgs-default-projects-project-quality-vpcs-subnet-e2e-1f11082b-56qvy-subnets-user-subnetset-static-948a4c45-56qvy-ip-pools-static-ipv4-default"></a>
### 354. /policy/api/v1/orgs/default/projects/project-quality/vpcs/subnet-e2e-1f11082b_56qvy/subnets/user-subnetset-static-948a4c45_56qvy/ip-pools/static-ipv4-default

**HTTP Methods:** GET

**Explanation:**
VPC subnet management within a project. Defines IP address ranges and network segments for VPC workloads.

---

<a id="355-policy-api-v1-orgs-default-projects-project-quality-vpcs-subnet-e2e-1f11082b-56qvy-subnets-user-subnetset-dhcp-c85186d8-56qvy-ports-port-in-dhcp-subnetset-56qvy"></a>
### 355. /policy/api/v1/orgs/default/projects/project-quality/vpcs/subnet-e2e-1f11082b_56qvy/subnets/user-subnetset-dhcp-c85186d8_56qvy/ports/port-in-dhcp-subnetset_56qvy

**HTTP Methods:** DELETE, GET, PATCH

**Explanation:**
VPC subnet management within a project. Defines IP address ranges and network segments for VPC workloads.

**Request Body (PATCH):**
```json
{
  "attachment": {
    "allocate_addresses": "NONE",
    "id": "4a2e0a06-2f8a-51d1-a7f6-47eba03e65d7",
    "traffic_tag": 0,
    "type": "INDEPENDENT"
  },
  "display_name": "port-in-dhcp-subnetset",
  "id": "port-in-dhcp-subnetset_56qvy",
  "parent_path": "/orgs/default/projects/project-quality/vpcs/subnet-e2e-1f11082b_56qvy/subnets/user-subnetset-dhcp-c85186d8_56qvy",
  "path": "/orgs/default/projects/project-quality/vpcs/subnet-e2e-1f11082b_56qvy/subnets/user-subnetset-dhcp-c85186d8_56qvy/ports/port-in-dhcp-subnetset_56qvy",
  "tags": [
    {
      "scope": "nsx-op/cluster",
      "tag": "f06fd228-8088-4439-a9e6-26c90a829c57"
    },
    {
      "scope": "nsx-op/version",
      "tag": "1.0.0"
    },
    {
      "scope": "nsx-op/vm_namespace",
      "tag": "subnet-e2e-1f11082b"
    },
    {
      "scope": "nsx-op/vm_namespace_uid",
      "tag": "f629b82e-5ea2-4298-b1cf-3bafcea373fa"
    },
    {
      "scope": "nsx-op/subnetport_name",
      "tag": "port-in-dhcp-subnetset"
    },
    {
      "scope": "nsx-op/subnetport_uid",
      "tag": "8a982112-7237-41b7-8637-9dbb954d9985"
    }
  ]
}
```

---

<a id="356-policy-api-v1-orgs-default-projects-project-quality-vpcs-test-create-vm-basic-f449d9bf-3ehn6-subnets-public-subnet-3ehn6-ports-public-vm-public-subnet-eth0-3ehn6"></a>
### 356. /policy/api/v1/orgs/default/projects/project-quality/vpcs/test-create-vm-basic-f449d9bf_3ehn6/subnets/public-subnet_3ehn6/ports/public-vm-public-subnet-eth0_3ehn6

**HTTP Methods:** DELETE, GET, PATCH

**Explanation:**
VPC subnet management within a project. Defines IP address ranges and network segments for VPC workloads.

**Request Body (PATCH):**
```json
{
  "attachment": {
    "allocate_addresses": "BOTH",
    "id": "f826912f-33a6-5acf-90b5-353362b9f5ce",
    "traffic_tag": 0,
    "type": "INDEPENDENT"
  },
  "display_name": "public-vm-public-subnet-eth0",
  "id": "public-vm-public-subnet-eth0_3ehn6",
  "parent_path": "/orgs/default/projects/project-quality/vpcs/test-create-vm-basic-f449d9bf_3ehn6/subnets/public-subnet_3ehn6",
  "path": "/orgs/default/projects/project-quality/vpcs/test-create-vm-basic-f449d9bf_3ehn6/subnets/public-subnet_3ehn6/ports/public-vm-public-subnet-eth0_3ehn6",
  "tags": [
    {
      "scope": "nsx-op/cluster",
      "tag": "f06fd228-8088-4439-a9e6-26c90a829c57"
    },
    {
      "scope": "nsx-op/version",
      "tag": "1.0.0"
    },
    {
      "scope": "nsx-op/vm_namespace",
      "tag": "test-create-vm-basic-f449d9bf"
    },
    {
      "scope": "nsx-op/vm_namespace_uid",
      "tag": "1d6f2e6e-f228-4ddc-87b3-b99608fd4766"
    },
    {
      "scope": "nsx-op/subnetport_name",
      "tag": "public-vm-public-subnet-eth0"
    },
    {
      "scope": "nsx-op/subnetport_uid",
      "tag": "0df89cec-26f2-47f8-9c52-afe070792e15"
    }
  ]
}
```

---

<a id="357-policy-api-v1-orgs-default-projects-project-quality-vpcs-test-security-policy-basic-72ecfa65-ib6li-subnets-pod-default-db03dc29-ib6li-ip-pools-static-ipv4-default"></a>
### 357. /policy/api/v1/orgs/default/projects/project-quality/vpcs/test-security-policy-basic-72ecfa65_ib6li/subnets/pod-default-db03dc29_ib6li/ip-pools/static-ipv4-default

**HTTP Methods:** GET

**Explanation:**
VPC subnet management within a project. Defines IP address ranges and network segments for VPC workloads.

---

<a id="358-policy-api-v1-orgs-default-projects-project-quality-vpcs-test-security-policy-match-expression-ff1dafa9-bgm74-subnets-pod-default-1289f64d-bgm74-ports-pod-a-bgm74"></a>
### 358. /policy/api/v1/orgs/default/projects/project-quality/vpcs/test-security-policy-match-expression-ff1dafa9_bgm74/subnets/pod-default-1289f64d_bgm74/ports/pod-a_bgm74

**HTTP Methods:** DELETE, GET, PATCH

**Explanation:**
VPC subnet management within a project. Defines IP address ranges and network segments for VPC workloads.

**Request Body (PATCH):**
```json
{
  "attachment": {
    "allocate_addresses": "BOTH",
    "app_id": "42f90b69-2ffa-4412-ab5c-b135e591627e",
    "context_id": "56cd0d00-c51c-4381-bd8b-64a2a3ac9ab0",
    "id": "b8564daf-7fd4-516b-ab8c-985dc05ac8ea",
    "traffic_tag": 0,
    "type": "INDEPENDENT"
  },
  "display_name": "pod-a",
  "id": "pod-a_bgm74",
  "parent_path": "/orgs/default/projects/project-quality/vpcs/test-security-policy-match-expression-ff1dafa9_bgm74/subnets/pod-default-1289f64d_bgm74",
  "path": "/orgs/default/projects/project-quality/vpcs/test-security-policy-match-expression-ff1dafa9_bgm74/subnets/pod-default-1289f64d_bgm74/ports/pod-a_bgm74",
  "tags": [
    {
      "scope": "nsx-op/cluster",
      "tag": "f06fd228-8088-4439-a9e6-26c90a829c57"
    },
    {
      "scope": "nsx-op/version",
      "tag": "1.0.0"
    },
    {
      "scope": "nsx-op/namespace",
      "tag": "test-security-policy-match-expression-ff1dafa9"
    },
    {
      "scope": "nsx-op/pod_name",
      "tag": "pod-a"
    },
    {
      "scope": "nsx-op/pod_uid",
      "tag": "42f90b69-2ffa-4412-ab5c-b135e591627e"
    },
    {
      "scope": "nsx-op/namespace_uid",
      "tag": "3de47ade-81f0-4df6-b8fe-4bd50341d1b1"
    }
  ]
}
```

---

<a id="359-policy-api-v1-orgs-default-projects-project-quality-vpcs-subnet-e2e-1f11082b-56qvy-subnets-user-subnetset-static-948a4c45-56qvy-ports-port-in-static-subnetset-56qvy"></a>
### 359. /policy/api/v1/orgs/default/projects/project-quality/vpcs/subnet-e2e-1f11082b_56qvy/subnets/user-subnetset-static-948a4c45_56qvy/ports/port-in-static-subnetset_56qvy

**HTTP Methods:** DELETE, GET, PATCH

**Explanation:**
VPC subnet management within a project. Defines IP address ranges and network segments for VPC workloads.

**Request Body (PATCH):**
```json
{
  "attachment": {
    "allocate_addresses": "BOTH",
    "id": "7d99122b-1cf1-566e-955a-3f7124ad2e40",
    "traffic_tag": 0,
    "type": "INDEPENDENT"
  },
  "display_name": "port-in-static-subnetset",
  "id": "port-in-static-subnetset_56qvy",
  "parent_path": "/orgs/default/projects/project-quality/vpcs/subnet-e2e-1f11082b_56qvy/subnets/user-subnetset-static-948a4c45_56qvy",
  "path": "/orgs/default/projects/project-quality/vpcs/subnet-e2e-1f11082b_56qvy/subnets/user-subnetset-static-948a4c45_56qvy/ports/port-in-static-subnetset_56qvy",
  "tags": [
    {
      "scope": "nsx-op/cluster",
      "tag": "f06fd228-8088-4439-a9e6-26c90a829c57"
    },
    {
      "scope": "nsx-op/version",
      "tag": "1.0.0"
    },
    {
      "scope": "nsx-op/vm_namespace",
      "tag": "subnet-e2e-1f11082b"
    },
    {
      "scope": "nsx-op/vm_namespace_uid",
      "tag": "f629b82e-5ea2-4298-b1cf-3bafcea373fa"
    },
    {
      "scope": "nsx-op/subnetport_name",
      "tag": "port-in-static-subnetset"
    },
    {
      "scope": "nsx-op/subnetport_uid",
      "tag": "31918f7a-0eb2-46a5-9aa0-132f14016588"
    }
  ]
}
```

---

<a id="360-policy-api-v1-orgs-default-projects-project-quality-vpcs-test-security-policy-match-expression-ff1dafa9-bgm74-subnets-pod-default-1289f64d-bgm74-ports-client-a-bgm74"></a>
### 360. /policy/api/v1/orgs/default/projects/project-quality/vpcs/test-security-policy-match-expression-ff1dafa9_bgm74/subnets/pod-default-1289f64d_bgm74/ports/client-a_bgm74

**HTTP Methods:** DELETE, GET, PATCH

**Explanation:**
VPC subnet management within a project. Defines IP address ranges and network segments for VPC workloads.

**Request Body (PATCH):**
```json
{
  "attachment": {
    "allocate_addresses": "BOTH",
    "app_id": "51ec593c-19e9-4553-8753-f67fecad1a0e",
    "context_id": "56cd0d00-c51c-4381-bd8b-64a2a3ac9ab0",
    "id": "6614a2e3-0d89-501f-843f-c56f01f58469",
    "traffic_tag": 0,
    "type": "INDEPENDENT"
  },
  "display_name": "client-a",
  "id": "client-a_bgm74",
  "parent_path": "/orgs/default/projects/project-quality/vpcs/test-security-policy-match-expression-ff1dafa9_bgm74/subnets/pod-default-1289f64d_bgm74",
  "path": "/orgs/default/projects/project-quality/vpcs/test-security-policy-match-expression-ff1dafa9_bgm74/subnets/pod-default-1289f64d_bgm74/ports/client-a_bgm74",
  "tags": [
    {
      "scope": "nsx-op/cluster",
      "tag": "f06fd228-8088-4439-a9e6-26c90a829c57"
    },
    {
      "scope": "nsx-op/version",
      "tag": "1.0.0"
    },
    {
      "scope": "nsx-op/namespace",
      "tag": "test-security-policy-match-expression-ff1dafa9"
    },
    {
      "scope": "nsx-op/pod_name",
      "tag": "client-a"
    },
    {
      "scope": "nsx-op/pod_uid",
      "tag": "51ec593c-19e9-4553-8753-f67fecad1a0e"
    },
    {
      "scope": "nsx-op/namespace_uid",
      "tag": "3de47ade-81f0-4df6-b8fe-4bd50341d1b1"
    },
    {
      "scope": "k1",
      "tag": "a1"
    },
    {
      "scope": "k2",
      "tag": "b1"
    },
    {
      "scope": "user",
      "tag": "internal"
    }
  ]
}
```

---

<a id="361-policy-api-v1-orgs-default-projects-project-quality-vpcs-test-security-policy-match-expression-ff1dafa9-bgm74-subnets-pod-default-1289f64d-bgm74-ports-client-b-bgm74"></a>
### 361. /policy/api/v1/orgs/default/projects/project-quality/vpcs/test-security-policy-match-expression-ff1dafa9_bgm74/subnets/pod-default-1289f64d_bgm74/ports/client-b_bgm74

**HTTP Methods:** DELETE, GET, PATCH

**Explanation:**
VPC subnet management within a project. Defines IP address ranges and network segments for VPC workloads.

**Request Body (PATCH):**
```json
{
  "attachment": {
    "allocate_addresses": "BOTH",
    "app_id": "1d7deb66-2f96-428f-90fa-4962eb4322e4",
    "context_id": "80cedc6a-fa1c-4a55-b574-b23c89536d95",
    "id": "4b1fa53a-7881-50b5-b452-0e9f281215d8",
    "traffic_tag": 0,
    "type": "INDEPENDENT"
  },
  "display_name": "client-b",
  "id": "client-b_bgm74",
  "parent_path": "/orgs/default/projects/project-quality/vpcs/test-security-policy-match-expression-ff1dafa9_bgm74/subnets/pod-default-1289f64d_bgm74",
  "path": "/orgs/default/projects/project-quality/vpcs/test-security-policy-match-expression-ff1dafa9_bgm74/subnets/pod-default-1289f64d_bgm74/ports/client-b_bgm74",
  "tags": [
    {
      "scope": "nsx-op/cluster",
      "tag": "f06fd228-8088-4439-a9e6-26c90a829c57"
    },
    {
      "scope": "nsx-op/version",
      "tag": "1.0.0"
    },
    {
      "scope": "nsx-op/namespace",
      "tag": "test-security-policy-match-expression-ff1dafa9"
    },
    {
      "scope": "nsx-op/pod_name",
      "tag": "client-b"
    },
    {
      "scope": "nsx-op/pod_uid",
      "tag": "1d7deb66-2f96-428f-90fa-4962eb4322e4"
    },
    {
      "scope": "nsx-op/namespace_uid",
      "tag": "3de47ade-81f0-4df6-b8fe-4bd50341d1b1"
    },
    {
      "scope": "k1",
      "tag": "a1"
    },
    {
      "scope": "k2",
      "tag": "b4"
    },
    {
      "scope": "user",
      "tag": "internal"
    }
  ]
}
```

---

<a id="362-policy-api-v1-orgs-default-projects-project-quality-vpcs-subnet-e2e-1f11082b-56qvy-subnets-subnet-dhcp-56qvy-ports-port-in-dhcp-subnet-with-address-bindings-vc-macpool-56qvy"></a>
### 362. /policy/api/v1/orgs/default/projects/project-quality/vpcs/subnet-e2e-1f11082b_56qvy/subnets/subnet-dhcp_56qvy/ports/port-in-dhcp-subnet-with-address-bindings-vc-macpool_56qvy

**HTTP Methods:** DELETE, GET, PATCH

**Explanation:**
VPC subnet management within a project. Defines IP address ranges and network segments for VPC workloads.

**Request Body (PATCH):**
```json
{
  "address_bindings": [
    {
      "ip_address": "172.26.0.164",
      "mac_address": "00:50:56:ba:d6:7a"
    }
  ],
  "attachment": {
    "allocate_addresses": "NONE",
    "id": "fb491594-3a97-5620-8072-90cfa0b0c63b",
    "traffic_tag": 0,
    "type": "INDEPENDENT"
  },
  "display_name": "port-in-dhcp-subnet-with-address-bindings-vc-macpool",
  "id": "port-in-dhcp-subnet-with-address-bindings-vc-macpool_56qvy",
  "parent_path": "/orgs/default/projects/project-quality/vpcs/subnet-e2e-1f11082b_56qvy/subnets/subnet-dhcp_56qvy",
  "path": "/orgs/default/projects/project-quality/vpcs/subnet-e2e-1f11082b_56qvy/subnets/subnet-dhcp_56qvy/ports/port-in-dhcp-subnet-with-address-bindings-vc-macpool_56qvy",
  "tags": [
    {
      "scope": "nsx-op/cluster",
      "tag": "f06fd228-8088-4439-a9e6-26c90a829c57"
    },
    {
      "scope": "nsx-op/version",
      "tag": "1.0.0"
    },
    {
      "scope": "nsx-op/vm_namespace",
      "tag": "subnet-e2e-1f11082b"
    },
    {
      "scope": "nsx-op/vm_namespace_uid",
      "tag": "f629b82e-5ea2-4298-b1cf-3bafcea373fa"
    },
    {
      "scope": "nsx-op/subnetport_name",
      "tag": "port-in-dhcp-subnet-with-address-bindings-vc-macpool"
    },
    {
      "scope": "nsx-op/subnetport_uid",
      "tag": "49e6c2e6-7722-4e43-a918-5a5543c8a16c"
    }
  ]
}
```

---

<a id="363-policy-api-v1-orgs-default-projects-project-quality-vpcs-test-security-policy-match-expression-ff1dafa9-bgm74-subnets-pod-default-1289f64d-bgm74-ip-pools-static-ipv4-default"></a>
### 363. /policy/api/v1/orgs/default/projects/project-quality/vpcs/test-security-policy-match-expression-ff1dafa9_bgm74/subnets/pod-default-1289f64d_bgm74/ip-pools/static-ipv4-default

**HTTP Methods:** GET

**Explanation:**
VPC subnet management within a project. Defines IP address ranges and network segments for VPC workloads.

---

<a id="364-policy-api-v1-orgs-default-projects-project-quality-vpcs-subnet-e2e-1f11082b-56qvy-subnets-subnet-dhcp-56qvy-ports-port-in-dhcp-subnet-with-address-bindings-nsx-macpool-56qvy"></a>
### 364. /policy/api/v1/orgs/default/projects/project-quality/vpcs/subnet-e2e-1f11082b_56qvy/subnets/subnet-dhcp_56qvy/ports/port-in-dhcp-subnet-with-address-bindings-nsx-macpool_56qvy

**HTTP Methods:** DELETE, GET, PATCH

**Explanation:**
VPC subnet management within a project. Defines IP address ranges and network segments for VPC workloads.

**Request Body (PATCH):**
```json
{
  "address_bindings": [
    {
      "ip_address": "172.26.0.173",
      "mac_address": "04:50:56:ba:d6:7a"
    }
  ],
  "attachment": {
    "allocate_addresses": "NONE",
    "id": "aae040ed-abc1-5e48-8bd2-e3f3ef0b794f",
    "traffic_tag": 0,
    "type": "INDEPENDENT"
  },
  "display_name": "port-in-dhcp-subnet-with-address-bindings-nsx-macpool",
  "id": "port-in-dhcp-subnet-with-address-bindings-nsx-macpool_56qvy",
  "parent_path": "/orgs/default/projects/project-quality/vpcs/subnet-e2e-1f11082b_56qvy/subnets/subnet-dhcp_56qvy",
  "path": "/orgs/default/projects/project-quality/vpcs/subnet-e2e-1f11082b_56qvy/subnets/subnet-dhcp_56qvy/ports/port-in-dhcp-subnet-with-address-bindings-nsx-macpool_56qvy",
  "tags": [
    {
      "scope": "nsx-op/cluster",
      "tag": "f06fd228-8088-4439-a9e6-26c90a829c57"
    },
    {
      "scope": "nsx-op/version",
      "tag": "1.0.0"
    },
    {
      "scope": "nsx-op/vm_namespace",
      "tag": "subnet-e2e-1f11082b"
    },
    {
      "scope": "nsx-op/vm_namespace_uid",
      "tag": "f629b82e-5ea2-4298-b1cf-3bafcea373fa"
    },
    {
      "scope": "nsx-op/subnetport_name",
      "tag": "port-in-dhcp-subnet-with-address-bindings-nsx-macpool"
    },
    {
      "scope": "nsx-op/subnetport_uid",
      "tag": "99891b06-06d6-4996-9d03-5da2e0b5f00c"
    }
  ]
}
```

---

<a id="365-policy-api-v1-orgs-default-projects-project-quality-vpcs-test-security-policy-basic-72ecfa65-ib6li-subnets-pod-default-db03dc29-ib6li-ports-server-client-68f86f99bc-2xkkv-ib6li"></a>
### 365. /policy/api/v1/orgs/default/projects/project-quality/vpcs/test-security-policy-basic-72ecfa65_ib6li/subnets/pod-default-db03dc29_ib6li/ports/server-client-68f86f99bc-2xkkv_ib6li

**HTTP Methods:** DELETE, GET, PATCH

**Explanation:**
VPC subnet management within a project. Defines IP address ranges and network segments for VPC workloads.

**Request Body (PATCH):**
```json
{
  "attachment": {
    "allocate_addresses": "BOTH",
    "app_id": "d86ac536-156e-4150-a3a3-6343932c48e8",
    "context_id": "80cedc6a-fa1c-4a55-b574-b23c89536d95",
    "id": "cd423b05-7157-5863-b32d-2ff08c51f445",
    "traffic_tag": 0,
    "type": "INDEPENDENT"
  },
  "display_name": "server-client-68f86f99bc-2xkkv",
  "id": "server-client-68f86f99bc-2xkkv_ib6li",
  "parent_path": "/orgs/default/projects/project-quality/vpcs/test-security-policy-basic-72ecfa65_ib6li/subnets/pod-default-db03dc29_ib6li",
  "path": "/orgs/default/projects/project-quality/vpcs/test-security-policy-basic-72ecfa65_ib6li/subnets/pod-default-db03dc29_ib6li/ports/server-client-68f86f99bc-2xkkv_ib6li",
  "tags": [
    {
      "scope": "nsx-op/cluster",
      "tag": "f06fd228-8088-4439-a9e6-26c90a829c57"
    },
    {
      "scope": "nsx-op/version",
      "tag": "1.0.0"
    },
    {
      "scope": "nsx-op/namespace",
      "tag": "test-security-policy-basic-72ecfa65"
    },
    {
      "scope": "nsx-op/pod_name",
      "tag": "server-client-68f86f99bc-2xkkv"
    },
    {
      "scope": "nsx-op/pod_uid",
      "tag": "d86ac536-156e-4150-a3a3-6343932c48e8"
    },
    {
      "scope": "nsx-op/namespace_uid",
      "tag": "a022f7f8-ff5d-4e79-964f-8782d0683f3a"
    },
    {
      "scope": "deployment",
      "tag": "server-client"
    },
    {
      "scope": "nsx-op-e2e",
      "tag": "server-client"
    },
    {
      "scope": "pod-template-hash",
      "tag": "68f86f99bc"
    }
  ]
}
```

---

<a id="366-policy-api-v1-orgs-default-projects-project-quality-vpcs-test-security-policy-basic-72ecfa65-ib6li-subnets-pod-default-db03dc29-ib6li-ports-server-client-68f86f99bc-c2xvr-ib6li"></a>
### 366. /policy/api/v1/orgs/default/projects/project-quality/vpcs/test-security-policy-basic-72ecfa65_ib6li/subnets/pod-default-db03dc29_ib6li/ports/server-client-68f86f99bc-c2xvr_ib6li

**HTTP Methods:** DELETE, GET, PATCH

**Explanation:**
VPC subnet management within a project. Defines IP address ranges and network segments for VPC workloads.

**Request Body (PATCH):**
```json
{
  "attachment": {
    "allocate_addresses": "BOTH",
    "app_id": "8fc3e173-b887-437c-83b0-011233d47329",
    "context_id": "56cd0d00-c51c-4381-bd8b-64a2a3ac9ab0",
    "id": "61da48ab-f7a1-52c7-9adf-50d8de922d84",
    "traffic_tag": 0,
    "type": "INDEPENDENT"
  },
  "display_name": "server-client-68f86f99bc-c2xvr",
  "id": "server-client-68f86f99bc-c2xvr_ib6li",
  "parent_path": "/orgs/default/projects/project-quality/vpcs/test-security-policy-basic-72ecfa65_ib6li/subnets/pod-default-db03dc29_ib6li",
  "path": "/orgs/default/projects/project-quality/vpcs/test-security-policy-basic-72ecfa65_ib6li/subnets/pod-default-db03dc29_ib6li/ports/server-client-68f86f99bc-c2xvr_ib6li",
  "tags": [
    {
      "scope": "nsx-op/cluster",
      "tag": "f06fd228-8088-4439-a9e6-26c90a829c57"
    },
    {
      "scope": "nsx-op/version",
      "tag": "1.0.0"
    },
    {
      "scope": "nsx-op/namespace",
      "tag": "test-security-policy-basic-72ecfa65"
    },
    {
      "scope": "nsx-op/pod_name",
      "tag": "server-client-68f86f99bc-c2xvr"
    },
    {
      "scope": "nsx-op/pod_uid",
      "tag": "8fc3e173-b887-437c-83b0-011233d47329"
    },
    {
      "scope": "nsx-op/namespace_uid",
      "tag": "a022f7f8-ff5d-4e79-964f-8782d0683f3a"
    },
    {
      "scope": "deployment",
      "tag": "server-client"
    },
    {
      "scope": "nsx-op-e2e",
      "tag": "server-client"
    },
    {
      "scope": "pod-template-hash",
      "tag": "68f86f99bc"
    }
  ]
}
```

---

<a id="367-policy-api-v1-orgs-default-projects-project-quality-vpcs-testvpc-3658f2b5-subnets-pod-default-ec7c1039-d5d7u-ports-vmware-system-image-280f8fa0-3f96-4aaf-bf38-390fbf5915ae-d5d7u"></a>
### 367. /policy/api/v1/orgs/default/projects/project-quality/vpcs/testvpc-3658f2b5/subnets/pod-default-ec7c1039_d5d7u/ports/vmware-system-image-280f8fa0-3f96-4aaf-bf38-390fbf5915ae_d5d7u

**HTTP Methods:** DELETE, GET, PATCH

**Explanation:**
VPC subnet management within a project. Defines IP address ranges and network segments for VPC workloads.

**Request Body (PATCH):**
```json
{
  "attachment": {
    "allocate_addresses": "BOTH",
    "id": "f54cd6e9-2303-58ef-b80a-1e939f32089f",
    "traffic_tag": 0,
    "type": "INDEPENDENT"
  },
  "display_name": "vmware-system-image-280f8fa0-3f96-4aaf-bf38-390fbf5915ae",
  "id": "vmware-system-image-280f8fa0-3f96-4aaf-bf38-390fbf5915ae_d5d7u",
  "parent_path": "/orgs/default/projects/project-quality/vpcs/testvpc-3658f2b5/subnets/pod-default-ec7c1039_d5d7u",
  "path": "/orgs/default/projects/project-quality/vpcs/testvpc-3658f2b5/subnets/pod-default-ec7c1039_d5d7u/ports/vmware-system-image-280f8fa0-3f96-4aaf-bf38-390fbf5915ae_d5d7u",
  "tags": [
    {
      "scope": "nsx-op/cluster",
      "tag": "f06fd228-8088-4439-a9e6-26c90a829c57"
    },
    {
      "scope": "nsx-op/version",
      "tag": "1.0.0"
    },
    {
      "scope": "nsx-op/namespace",
      "tag": "test-prevpc-8f1a464f"
    },
    {
      "scope": "nsx-op/subnetport_name",
      "tag": "vmware-system-image-280f8fa0-3f96-4aaf-bf38-390fbf5915ae"
    },
    {
      "scope": "nsx-op/subnetport_uid",
      "tag": "2c1cd1e3-2e38-499e-a876-6c5e35d46e6b"
    },
    {
      "scope": "nsx-op/namespace_uid",
      "tag": "87995f00-857e-41a2-8687-41656a792cf7"
    },
    {
      "scope": "iaas.vmware.com/image-fetcher",
      "tag": "true"
    }
  ]
}
```

---

<a id="368-policy-api-v1-orgs-default-projects-project-quality-vpcs-testvpc-7ab2d8aa-subnets-pod-default-e0268dd8-5583h-ports-vmware-system-image-1a52a8a8-37d8-4ae2-b433-4a96be950051-5583h"></a>
### 368. /policy/api/v1/orgs/default/projects/project-quality/vpcs/testvpc-7ab2d8aa/subnets/pod-default-e0268dd8_5583h/ports/vmware-system-image-1a52a8a8-37d8-4ae2-b433-4a96be950051_5583h

**HTTP Methods:** DELETE, GET, PATCH

**Explanation:**
VPC subnet management within a project. Defines IP address ranges and network segments for VPC workloads.

**Request Body (PATCH):**
```json
{
  "attachment": {
    "allocate_addresses": "BOTH",
    "id": "e70d2316-b674-5021-b6cb-bf6783dc56d7",
    "traffic_tag": 0,
    "type": "INDEPENDENT"
  },
  "display_name": "vmware-system-image-1a52a8a8-37d8-4ae2-b433-4a96be950051",
  "id": "vmware-system-image-1a52a8a8-37d8-4ae2-b433-4a96be950051_5583h",
  "parent_path": "/orgs/default/projects/project-quality/vpcs/testvpc-7ab2d8aa/subnets/pod-default-e0268dd8_5583h",
  "path": "/orgs/default/projects/project-quality/vpcs/testvpc-7ab2d8aa/subnets/pod-default-e0268dd8_5583h/ports/vmware-system-image-1a52a8a8-37d8-4ae2-b433-4a96be950051_5583h",
  "tags": [
    {
      "scope": "nsx-op/cluster",
      "tag": "f06fd228-8088-4439-a9e6-26c90a829c57"
    },
    {
      "scope": "nsx-op/version",
      "tag": "1.0.0"
    },
    {
      "scope": "nsx-op/namespace",
      "tag": "test-prevpc-9f16bff1"
    },
    {
      "scope": "nsx-op/subnetport_name",
      "tag": "vmware-system-image-1a52a8a8-37d8-4ae2-b433-4a96be950051"
    },
    {
      "scope": "nsx-op/subnetport_uid",
      "tag": "a3052b27-01ae-471f-ab3a-bd339dd18297"
    },
    {
      "scope": "nsx-op/namespace_uid",
      "tag": "a0a91583-c678-4a6d-8e23-f699d12140c4"
    },
    {
      "scope": "iaas.vmware.com/image-fetcher",
      "tag": "true"
    }
  ]
}
```

---

<a id="369-policy-api-v1-orgs-default-projects-project-quality-vpcs-web-da775e6f-6o7ts-subnets-pod-default-a734dd59-6o7ts-ports-vmware-system-image-67d253b4-2743-45dd-86ca-a5de1909fc68-6o7ts"></a>
### 369. /policy/api/v1/orgs/default/projects/project-quality/vpcs/web-da775e6f_6o7ts/subnets/pod-default-a734dd59_6o7ts/ports/vmware-system-image-67d253b4-2743-45dd-86ca-a5de1909fc68_6o7ts

**HTTP Methods:** DELETE, GET, PATCH

**Explanation:**
VPC subnet management within a project. Defines IP address ranges and network segments for VPC workloads.

**Request Body (PATCH):**
```json
{
  "attachment": {
    "allocate_addresses": "BOTH",
    "id": "5f61bff0-eb40-56c6-a14e-94c55f7c96f9",
    "traffic_tag": 0,
    "type": "INDEPENDENT"
  },
  "display_name": "vmware-system-image-67d253b4-2743-45dd-86ca-a5de1909fc68",
  "id": "vmware-system-image-67d253b4-2743-45dd-86ca-a5de1909fc68_6o7ts",
  "parent_path": "/orgs/default/projects/project-quality/vpcs/web-da775e6f_6o7ts/subnets/pod-default-a734dd59_6o7ts",
  "path": "/orgs/default/projects/project-quality/vpcs/web-da775e6f_6o7ts/subnets/pod-default-a734dd59_6o7ts/ports/vmware-system-image-67d253b4-2743-45dd-86ca-a5de1909fc68_6o7ts",
  "tags": [
    {
      "scope": "nsx-op/cluster",
      "tag": "f06fd228-8088-4439-a9e6-26c90a829c57"
    },
    {
      "scope": "nsx-op/version",
      "tag": "1.0.0"
    },
    {
      "scope": "nsx-op/namespace",
      "tag": "web-da775e6f"
    },
    {
      "scope": "nsx-op/subnetport_name",
      "tag": "vmware-system-image-67d253b4-2743-45dd-86ca-a5de1909fc68"
    },
    {
      "scope": "nsx-op/subnetport_uid",
      "tag": "1f42e2ec-64e0-495f-ada2-352f73773599"
    },
    {
      "scope": "nsx-op/namespace_uid",
      "tag": "d114a0e0-d12c-41ac-9435-213fd199fa7b"
    },
    {
      "scope": "iaas.vmware.com/image-fetcher",
      "tag": "true"
    }
  ]
}
```

---

<a id="370-policy-api-v1-orgs-default-projects-project-quality-vpcs-web-da775e6f-6o7ts-subnets-pod-default-a734dd59-6o7ts-ports-vmware-system-image-b3305f6d-fd0d-4c43-9b16-78dc0b9f7ce2-6o7ts"></a>
### 370. /policy/api/v1/orgs/default/projects/project-quality/vpcs/web-da775e6f_6o7ts/subnets/pod-default-a734dd59_6o7ts/ports/vmware-system-image-b3305f6d-fd0d-4c43-9b16-78dc0b9f7ce2_6o7ts

**HTTP Methods:** DELETE, GET, PATCH

**Explanation:**
VPC subnet management within a project. Defines IP address ranges and network segments for VPC workloads.

**Request Body (PATCH):**
```json
{
  "attachment": {
    "allocate_addresses": "BOTH",
    "id": "9598392a-81c0-530c-a78f-0bf40ff66f8a",
    "traffic_tag": 0,
    "type": "INDEPENDENT"
  },
  "display_name": "vmware-system-image-b3305f6d-fd0d-4c43-9b16-78dc0b9f7ce2",
  "id": "vmware-system-image-b3305f6d-fd0d-4c43-9b16-78dc0b9f7ce2_6o7ts",
  "parent_path": "/orgs/default/projects/project-quality/vpcs/web-da775e6f_6o7ts/subnets/pod-default-a734dd59_6o7ts",
  "path": "/orgs/default/projects/project-quality/vpcs/web-da775e6f_6o7ts/subnets/pod-default-a734dd59_6o7ts/ports/vmware-system-image-b3305f6d-fd0d-4c43-9b16-78dc0b9f7ce2_6o7ts",
  "tags": [
    {
      "scope": "nsx-op/cluster",
      "tag": "f06fd228-8088-4439-a9e6-26c90a829c57"
    },
    {
      "scope": "nsx-op/version",
      "tag": "1.0.0"
    },
    {
      "scope": "nsx-op/namespace",
      "tag": "web-da775e6f"
    },
    {
      "scope": "nsx-op/subnetport_name",
      "tag": "vmware-system-image-b3305f6d-fd0d-4c43-9b16-78dc0b9f7ce2"
    },
    {
      "scope": "nsx-op/subnetport_uid",
      "tag": "3240bbdd-1b8b-4e3c-a805-52c8124c8e3a"
    },
    {
      "scope": "nsx-op/namespace_uid",
      "tag": "d114a0e0-d12c-41ac-9435-213fd199fa7b"
    },
    {
      "scope": "iaas.vmware.com/image-fetcher",
      "tag": "true"
    }
  ]
}
```

---

<a id="371-policy-api-v1-orgs-default-projects-project-quality-vpcs-client-91c3f484-qzuxu-subnets-pod-default-075e5037-qzuxu-ports-vmware-system-image-b16a63d0-2b48-4e25-9222-ed24d7a5c67c-qzuxu"></a>
### 371. /policy/api/v1/orgs/default/projects/project-quality/vpcs/client-91c3f484_qzuxu/subnets/pod-default-075e5037_qzuxu/ports/vmware-system-image-b16a63d0-2b48-4e25-9222-ed24d7a5c67c_qzuxu

**HTTP Methods:** DELETE, GET, PATCH

**Explanation:**
VPC subnet management within a project. Defines IP address ranges and network segments for VPC workloads.

**Request Body (PATCH):**
```json
{
  "attachment": {
    "allocate_addresses": "BOTH",
    "id": "4c8710ba-c165-5f51-a603-b9e7756c3d5d",
    "traffic_tag": 0,
    "type": "INDEPENDENT"
  },
  "display_name": "vmware-system-image-b16a63d0-2b48-4e25-9222-ed24d7a5c67c",
  "id": "vmware-system-image-b16a63d0-2b48-4e25-9222-ed24d7a5c67c_qzuxu",
  "parent_path": "/orgs/default/projects/project-quality/vpcs/client-91c3f484_qzuxu/subnets/pod-default-075e5037_qzuxu",
  "path": "/orgs/default/projects/project-quality/vpcs/client-91c3f484_qzuxu/subnets/pod-default-075e5037_qzuxu/ports/vmware-system-image-b16a63d0-2b48-4e25-9222-ed24d7a5c67c_qzuxu",
  "tags": [
    {
      "scope": "nsx-op/cluster",
      "tag": "f06fd228-8088-4439-a9e6-26c90a829c57"
    },
    {
      "scope": "nsx-op/version",
      "tag": "1.0.0"
    },
    {
      "scope": "nsx-op/namespace",
      "tag": "client-91c3f484"
    },
    {
      "scope": "nsx-op/subnetport_name",
      "tag": "vmware-system-image-b16a63d0-2b48-4e25-9222-ed24d7a5c67c"
    },
    {
      "scope": "nsx-op/subnetport_uid",
      "tag": "4f7989e0-9a21-4841-97db-98a59fbf8f81"
    },
    {
      "scope": "nsx-op/namespace_uid",
      "tag": "e19581fd-dbb5-4b0c-b896-e4fcff60f0ed"
    },
    {
      "scope": "iaas.vmware.com/image-fetcher",
      "tag": "true"
    }
  ]
}
```

---

<a id="372-policy-api-v1-orgs-default-projects-project-quality-vpcs-test-lb-50fedbb3-mv836-subnets-pod-default-3cc5e9c8-mv836-ports-vmware-system-image-90dc9354-d875-41fe-b545-01332c956b5a-mv836"></a>
### 372. /policy/api/v1/orgs/default/projects/project-quality/vpcs/test-lb-50fedbb3_mv836/subnets/pod-default-3cc5e9c8_mv836/ports/vmware-system-image-90dc9354-d875-41fe-b545-01332c956b5a_mv836

**HTTP Methods:** DELETE, GET, PATCH

**Explanation:**
VPC subnet management within a project. Defines IP address ranges and network segments for VPC workloads.

**Request Body (PATCH):**
```json
{
  "attachment": {
    "allocate_addresses": "BOTH",
    "id": "8db2c96d-8828-5dda-9b00-88fc085dff66",
    "traffic_tag": 0,
    "type": "INDEPENDENT"
  },
  "display_name": "vmware-system-image-90dc9354-d875-41fe-b545-01332c956b5a",
  "id": "vmware-system-image-90dc9354-d875-41fe-b545-01332c956b5a_mv836",
  "parent_path": "/orgs/default/projects/project-quality/vpcs/test-lb-50fedbb3_mv836/subnets/pod-default-3cc5e9c8_mv836",
  "path": "/orgs/default/projects/project-quality/vpcs/test-lb-50fedbb3_mv836/subnets/pod-default-3cc5e9c8_mv836/ports/vmware-system-image-90dc9354-d875-41fe-b545-01332c956b5a_mv836",
  "tags": [
    {
      "scope": "nsx-op/cluster",
      "tag": "f06fd228-8088-4439-a9e6-26c90a829c57"
    },
    {
      "scope": "nsx-op/version",
      "tag": "1.0.0"
    },
    {
      "scope": "nsx-op/namespace",
      "tag": "test-lb-50fedbb3"
    },
    {
      "scope": "nsx-op/subnetport_name",
      "tag": "vmware-system-image-90dc9354-d875-41fe-b545-01332c956b5a"
    },
    {
      "scope": "nsx-op/subnetport_uid",
      "tag": "d833ed51-86a3-458d-8f26-0df449ba3c6a"
    },
    {
      "scope": "nsx-op/namespace_uid",
      "tag": "2506fba2-2bca-42a9-9fb0-35aa09b1d33c"
    },
    {
      "scope": "iaas.vmware.com/image-fetcher",
      "tag": "true"
    }
  ]
}
```

---

<a id="373-policy-api-v1-orgs-default-projects-project-quality-vpcs-test-pod-1dd9a577-fu9t5-subnets-pod-default-5cf92338-fu9t5-ports-vmware-system-image-cd289a18-4ce4-4dff-a025-39f9d0636310-fu9t5"></a>
### 373. /policy/api/v1/orgs/default/projects/project-quality/vpcs/test-pod-1dd9a577_fu9t5/subnets/pod-default-5cf92338_fu9t5/ports/vmware-system-image-cd289a18-4ce4-4dff-a025-39f9d0636310_fu9t5

**HTTP Methods:** DELETE, GET, PATCH

**Explanation:**
VPC subnet management within a project. Defines IP address ranges and network segments for VPC workloads.

**Request Body (PATCH):**
```json
{
  "attachment": {
    "allocate_addresses": "BOTH",
    "id": "537ab3ae-08d5-51e0-9517-75f0112d73b4",
    "traffic_tag": 0,
    "type": "INDEPENDENT"
  },
  "display_name": "vmware-system-image-cd289a18-4ce4-4dff-a025-39f9d0636310",
  "id": "vmware-system-image-cd289a18-4ce4-4dff-a025-39f9d0636310_fu9t5",
  "parent_path": "/orgs/default/projects/project-quality/vpcs/test-pod-1dd9a577_fu9t5/subnets/pod-default-5cf92338_fu9t5",
  "path": "/orgs/default/projects/project-quality/vpcs/test-pod-1dd9a577_fu9t5/subnets/pod-default-5cf92338_fu9t5/ports/vmware-system-image-cd289a18-4ce4-4dff-a025-39f9d0636310_fu9t5",
  "tags": [
    {
      "scope": "nsx-op/cluster",
      "tag": "f06fd228-8088-4439-a9e6-26c90a829c57"
    },
    {
      "scope": "nsx-op/version",
      "tag": "1.0.0"
    },
    {
      "scope": "nsx-op/namespace",
      "tag": "test-pod-1dd9a577"
    },
    {
      "scope": "nsx-op/subnetport_name",
      "tag": "vmware-system-image-cd289a18-4ce4-4dff-a025-39f9d0636310"
    },
    {
      "scope": "nsx-op/subnetport_uid",
      "tag": "808619ef-7b02-4be0-9222-5a3584fa807e"
    },
    {
      "scope": "nsx-op/namespace_uid",
      "tag": "6c0816d9-ed05-4f26-91d1-b87dae8e9c1b"
    },
    {
      "scope": "iaas.vmware.com/image-fetcher",
      "tag": "true"
    }
  ]
}
```

---

<a id="374-policy-api-v1-orgs-default-projects-project-quality-vpcs-test-pod-sync-e8b8a7ca-m404i-subnets-pod-default-0dd88421-m404i-ports-vmware-system-image-38f4d4f7-1fae-4270-9eb3-e8e9f2c5f08a-m404i"></a>
### 374. /policy/api/v1/orgs/default/projects/project-quality/vpcs/test-pod-sync-e8b8a7ca_m404i/subnets/pod-default-0dd88421_m404i/ports/vmware-system-image-38f4d4f7-1fae-4270-9eb3-e8e9f2c5f08a_m404i

**HTTP Methods:** DELETE, GET, PATCH

**Explanation:**
VPC subnet management within a project. Defines IP address ranges and network segments for VPC workloads.

**Request Body (PATCH):**
```json
{
  "attachment": {
    "allocate_addresses": "BOTH",
    "id": "fdcbdac2-41d9-5c1a-85ff-36b57382bcc0",
    "traffic_tag": 0,
    "type": "INDEPENDENT"
  },
  "display_name": "vmware-system-image-38f4d4f7-1fae-4270-9eb3-e8e9f2c5f08a",
  "id": "vmware-system-image-38f4d4f7-1fae-4270-9eb3-e8e9f2c5f08a_m404i",
  "parent_path": "/orgs/default/projects/project-quality/vpcs/test-pod-sync-e8b8a7ca_m404i/subnets/pod-default-0dd88421_m404i",
  "path": "/orgs/default/projects/project-quality/vpcs/test-pod-sync-e8b8a7ca_m404i/subnets/pod-default-0dd88421_m404i/ports/vmware-system-image-38f4d4f7-1fae-4270-9eb3-e8e9f2c5f08a_m404i",
  "tags": [
    {
      "scope": "nsx-op/cluster",
      "tag": "f06fd228-8088-4439-a9e6-26c90a829c57"
    },
    {
      "scope": "nsx-op/version",
      "tag": "1.0.0"
    },
    {
      "scope": "nsx-op/namespace",
      "tag": "test-pod-sync-e8b8a7ca"
    },
    {
      "scope": "nsx-op/subnetport_name",
      "tag": "vmware-system-image-38f4d4f7-1fae-4270-9eb3-e8e9f2c5f08a"
    },
    {
      "scope": "nsx-op/subnetport_uid",
      "tag": "ba150f50-b029-4d25-8c3e-3bda86c63268"
    },
    {
      "scope": "nsx-op/namespace_uid",
      "tag": "df28714f-bbd0-4ac5-bfaa-13716c242ac0"
    },
    {
      "scope": "iaas.vmware.com/image-fetcher",
      "tag": "true"
    }
  ]
}
```

---

<a id="375-policy-api-v1-orgs-default-projects-project-quality-vpcs-test-security-policy-basic-72ecfa65-ib6li-subnets-pod-default-db03dc29-ib6li-ports-vmware-system-image-7f80e1f0-a3f7-4d67-87e3-16162d5cdcc8-ib6li"></a>
### 375. /policy/api/v1/orgs/default/projects/project-quality/vpcs/test-security-policy-basic-72ecfa65_ib6li/subnets/pod-default-db03dc29_ib6li/ports/vmware-system-image-7f80e1f0-a3f7-4d67-87e3-16162d5cdcc8_ib6li

**HTTP Methods:** DELETE, GET, PATCH

**Explanation:**
VPC subnet management within a project. Defines IP address ranges and network segments for VPC workloads.

**Request Body (PATCH):**
```json
{
  "attachment": {
    "allocate_addresses": "BOTH",
    "id": "97bfb18b-ddd0-5001-95de-c90df2b3c120",
    "traffic_tag": 0,
    "type": "INDEPENDENT"
  },
  "display_name": "vmware-system-image-7f80e1f0-a3f7-4d67-87e3-16162d5cdcc8",
  "id": "vmware-system-image-7f80e1f0-a3f7-4d67-87e3-16162d5cdcc8_ib6li",
  "parent_path": "/orgs/default/projects/project-quality/vpcs/test-security-policy-basic-72ecfa65_ib6li/subnets/pod-default-db03dc29_ib6li",
  "path": "/orgs/default/projects/project-quality/vpcs/test-security-policy-basic-72ecfa65_ib6li/subnets/pod-default-db03dc29_ib6li/ports/vmware-system-image-7f80e1f0-a3f7-4d67-87e3-16162d5cdcc8_ib6li",
  "tags": [
    {
      "scope": "nsx-op/cluster",
      "tag": "f06fd228-8088-4439-a9e6-26c90a829c57"
    },
    {
      "scope": "nsx-op/version",
      "tag": "1.0.0"
    },
    {
      "scope": "nsx-op/namespace",
      "tag": "test-security-policy-basic-72ecfa65"
    },
    {
      "scope": "nsx-op/subnetport_name",
      "tag": "vmware-system-image-7f80e1f0-a3f7-4d67-87e3-16162d5cdcc8"
    },
    {
      "scope": "nsx-op/subnetport_uid",
      "tag": "9c962f72-65a3-4f54-a406-91c8e384b2bb"
    },
    {
      "scope": "nsx-op/namespace_uid",
      "tag": "a022f7f8-ff5d-4e79-964f-8782d0683f3a"
    },
    {
      "scope": "iaas.vmware.com/image-fetcher",
      "tag": "true"
    }
  ]
}
```

---

<a id="376-policy-api-v1-orgs-default-projects-project-quality-vpcs-test-security-policy-match-expression-ff1dafa9-bgm74-subnets-pod-default-1289f64d-bgm74-ports-vmware-system-image-78efc28d-50fb-4bf5-8eb3-5ff538be370c-bgm74"></a>
### 376. /policy/api/v1/orgs/default/projects/project-quality/vpcs/test-security-policy-match-expression-ff1dafa9_bgm74/subnets/pod-default-1289f64d_bgm74/ports/vmware-system-image-78efc28d-50fb-4bf5-8eb3-5ff538be370c_bgm74

**HTTP Methods:** DELETE, GET, PATCH

**Explanation:**
VPC subnet management within a project. Defines IP address ranges and network segments for VPC workloads.

**Request Body (PATCH):**
```json
{
  "attachment": {
    "allocate_addresses": "BOTH",
    "id": "700a91a6-9e72-5be3-a71b-124a12e12492",
    "traffic_tag": 0,
    "type": "INDEPENDENT"
  },
  "display_name": "vmware-system-image-78efc28d-50fb-4bf5-8eb3-5ff538be370c",
  "id": "vmware-system-image-78efc28d-50fb-4bf5-8eb3-5ff538be370c_bgm74",
  "parent_path": "/orgs/default/projects/project-quality/vpcs/test-security-policy-match-expression-ff1dafa9_bgm74/subnets/pod-default-1289f64d_bgm74",
  "path": "/orgs/default/projects/project-quality/vpcs/test-security-policy-match-expression-ff1dafa9_bgm74/subnets/pod-default-1289f64d_bgm74/ports/vmware-system-image-78efc28d-50fb-4bf5-8eb3-5ff538be370c_bgm74",
  "tags": [
    {
      "scope": "nsx-op/cluster",
      "tag": "f06fd228-8088-4439-a9e6-26c90a829c57"
    },
    {
      "scope": "nsx-op/version",
      "tag": "1.0.0"
    },
    {
      "scope": "nsx-op/namespace",
      "tag": "test-security-policy-match-expression-ff1dafa9"
    },
    {
      "scope": "nsx-op/subnetport_name",
      "tag": "vmware-system-image-78efc28d-50fb-4bf5-8eb3-5ff538be370c"
    },
    {
      "scope": "nsx-op/subnetport_uid",
      "tag": "9b503a1d-5456-4e45-b19b-6b25972d330d"
    },
    {
      "scope": "nsx-op/namespace_uid",
      "tag": "3de47ade-81f0-4df6-b8fe-4bd50341d1b1"
    },
    {
      "scope": "iaas.vmware.com/image-fetcher",
      "tag": "true"
    }
  ]
}
```

---

<a id="377-policy-api-v1-orgs-default-projects-project-quality-vpcs-test-security-policy-match-expression-ff1dafa9-bgm74-subnets-pod-default-1289f64d-bgm74-ports-vmware-system-image-849fb668-f3ab-48bc-846b-38c485bd8f1f-bgm74"></a>
### 377. /policy/api/v1/orgs/default/projects/project-quality/vpcs/test-security-policy-match-expression-ff1dafa9_bgm74/subnets/pod-default-1289f64d_bgm74/ports/vmware-system-image-849fb668-f3ab-48bc-846b-38c485bd8f1f_bgm74

**HTTP Methods:** DELETE, GET, PATCH

**Explanation:**
VPC subnet management within a project. Defines IP address ranges and network segments for VPC workloads.

**Request Body (PATCH):**
```json
{
  "attachment": {
    "allocate_addresses": "BOTH",
    "id": "f8b14ded-0d43-5db7-9d13-f144aa7007b6",
    "traffic_tag": 0,
    "type": "INDEPENDENT"
  },
  "display_name": "vmware-system-image-849fb668-f3ab-48bc-846b-38c485bd8f1f",
  "id": "vmware-system-image-849fb668-f3ab-48bc-846b-38c485bd8f1f_bgm74",
  "parent_path": "/orgs/default/projects/project-quality/vpcs/test-security-policy-match-expression-ff1dafa9_bgm74/subnets/pod-default-1289f64d_bgm74",
  "path": "/orgs/default/projects/project-quality/vpcs/test-security-policy-match-expression-ff1dafa9_bgm74/subnets/pod-default-1289f64d_bgm74/ports/vmware-system-image-849fb668-f3ab-48bc-846b-38c485bd8f1f_bgm74",
  "tags": [
    {
      "scope": "nsx-op/cluster",
      "tag": "f06fd228-8088-4439-a9e6-26c90a829c57"
    },
    {
      "scope": "nsx-op/version",
      "tag": "1.0.0"
    },
    {
      "scope": "nsx-op/namespace",
      "tag": "test-security-policy-match-expression-ff1dafa9"
    },
    {
      "scope": "nsx-op/subnetport_name",
      "tag": "vmware-system-image-849fb668-f3ab-48bc-846b-38c485bd8f1f"
    },
    {
      "scope": "nsx-op/subnetport_uid",
      "tag": "03870928-da2e-425f-b0cc-79d18481a2a8"
    },
    {
      "scope": "nsx-op/namespace_uid",
      "tag": "3de47ade-81f0-4df6-b8fe-4bd50341d1b1"
    },
    {
      "scope": "iaas.vmware.com/image-fetcher",
      "tag": "true"
    }
  ]
}
```

---

<a id="378-policy-api-v1-orgs-default-projects-project-quality-vpcs-test-security-policy-match-expression-ff1dafa9-bgm74-subnets-pod-default-1289f64d-bgm74-ports-vmware-system-image-92b67ea7-200d-4a00-92d3-c6974f97422f-bgm74"></a>
### 378. /policy/api/v1/orgs/default/projects/project-quality/vpcs/test-security-policy-match-expression-ff1dafa9_bgm74/subnets/pod-default-1289f64d_bgm74/ports/vmware-system-image-92b67ea7-200d-4a00-92d3-c6974f97422f_bgm74

**HTTP Methods:** DELETE, GET, PATCH

**Explanation:**
VPC subnet management within a project. Defines IP address ranges and network segments for VPC workloads.

**Request Body (PATCH):**
```json
{
  "attachment": {
    "allocate_addresses": "BOTH",
    "id": "69cc9754-5d31-50c9-bb37-e69d885c7bf4",
    "traffic_tag": 0,
    "type": "INDEPENDENT"
  },
  "display_name": "vmware-system-image-92b67ea7-200d-4a00-92d3-c6974f97422f",
  "id": "vmware-system-image-92b67ea7-200d-4a00-92d3-c6974f97422f_bgm74",
  "parent_path": "/orgs/default/projects/project-quality/vpcs/test-security-policy-match-expression-ff1dafa9_bgm74/subnets/pod-default-1289f64d_bgm74",
  "path": "/orgs/default/projects/project-quality/vpcs/test-security-policy-match-expression-ff1dafa9_bgm74/subnets/pod-default-1289f64d_bgm74/ports/vmware-system-image-92b67ea7-200d-4a00-92d3-c6974f97422f_bgm74",
  "tags": [
    {
      "scope": "nsx-op/cluster",
      "tag": "f06fd228-8088-4439-a9e6-26c90a829c57"
    },
    {
      "scope": "nsx-op/version",
      "tag": "1.0.0"
    },
    {
      "scope": "nsx-op/namespace",
      "tag": "test-security-policy-match-expression-ff1dafa9"
    },
    {
      "scope": "nsx-op/subnetport_name",
      "tag": "vmware-system-image-92b67ea7-200d-4a00-92d3-c6974f97422f"
    },
    {
      "scope": "nsx-op/subnetport_uid",
      "tag": "5d5196c5-79c9-4930-8b9f-7075f890174d"
    },
    {
      "scope": "nsx-op/namespace_uid",
      "tag": "3de47ade-81f0-4df6-b8fe-4bd50341d1b1"
    },
    {
      "scope": "iaas.vmware.com/image-fetcher",
      "tag": "true"
    }
  ]
}
```

---

<a id="379-policy-api-v1-orgs-default-projects-project-quality-vpcs-test-lb-50fedbb3-mv836-subnets-pod-default-3cc5e9c8-mv836-ports-tea-mv836-state"></a>
### 379. /policy/api/v1/orgs/default/projects/project-quality/vpcs/test-lb-50fedbb3_mv836/subnets/pod-default-3cc5e9c8_mv836/ports/tea_mv836/state

**HTTP Methods:** GET

**Explanation:**
VPC subnet management within a project. Defines IP address ranges and network segments for VPC workloads.

---

<a id="380-policy-api-v1-orgs-default-projects-project-quality-vpcs-client-91c3f484-qzuxu-subnets-pod-default-075e5037-qzuxu-ports-client-qzuxu-state"></a>
### 380. /policy/api/v1/orgs/default/projects/project-quality/vpcs/client-91c3f484_qzuxu/subnets/pod-default-075e5037_qzuxu/ports/client_qzuxu/state

**HTTP Methods:** GET

**Explanation:**
VPC subnet management within a project. Defines IP address ranges and network segments for VPC workloads.

---

<a id="381-policy-api-v1-orgs-default-projects-project-quality-vpcs-test-lb-50fedbb3-mv836-subnets-pod-default-3cc5e9c8-mv836-ports-coffee-mv836-state"></a>
### 381. /policy/api/v1/orgs/default/projects/project-quality/vpcs/test-lb-50fedbb3_mv836/subnets/pod-default-3cc5e9c8_mv836/ports/coffee_mv836/state

**HTTP Methods:** GET

**Explanation:**
VPC subnet management within a project. Defines IP address ranges and network segments for VPC workloads.

---

<a id="382-policy-api-v1-orgs-default-projects-project-quality-vpcs-testvpc-7ab2d8aa-subnets-pod-default-e0268dd8-5583h-ports-prevpc-podvm-5583h-state"></a>
### 382. /policy/api/v1/orgs/default/projects/project-quality/vpcs/testvpc-7ab2d8aa/subnets/pod-default-e0268dd8_5583h/ports/prevpc-podvm_5583h/state

**HTTP Methods:** GET

**Explanation:**
VPC subnet management within a project. Defines IP address ranges and network segments for VPC workloads.

---

<a id="383-policy-api-v1-orgs-default-projects-project-quality-vpcs-test-lb-50fedbb3-mv836-subnets-pod-default-3cc5e9c8-mv836-ports-default-mv836-state"></a>
### 383. /policy/api/v1/orgs/default/projects/project-quality/vpcs/test-lb-50fedbb3_mv836/subnets/pod-default-3cc5e9c8_mv836/ports/default_mv836/state

**HTTP Methods:** GET

**Explanation:**
VPC subnet management within a project. Defines IP address ranges and network segments for VPC workloads.

---

<a id="384-policy-api-v1-orgs-default-projects-project-quality-vpcs-subnet-e2e-1f11082b-56qvy-subnets-subnet-cidr-56qvy-ports-port-with-ip-1-56qvy-state"></a>
### 384. /policy/api/v1/orgs/default/projects/project-quality/vpcs/subnet-e2e-1f11082b_56qvy/subnets/subnet-cidr_56qvy/ports/port-with-ip-1_56qvy/state

**HTTP Methods:** GET

**Explanation:**
VPC subnet management within a project. Defines IP address ranges and network segments for VPC workloads.

---

<a id="385-policy-api-v1-orgs-default-projects-project-quality-vpcs-subnet-e2e-1f11082b-56qvy-subnets-subnet-cidr-56qvy-ports-port-with-ip-2-56qvy-state"></a>
### 385. /policy/api/v1/orgs/default/projects/project-quality/vpcs/subnet-e2e-1f11082b_56qvy/subnets/subnet-cidr_56qvy/ports/port-with-ip-2_56qvy/state

**HTTP Methods:** GET

**Explanation:**
VPC subnet management within a project. Defines IP address ranges and network segments for VPC workloads.

---

<a id="386-policy-api-v1-orgs-default-projects-project-quality-vpcs-testvpc-3658f2b5-subnets-pod-default-ec7c1039-d5d7u-ports-prevpc-client-pod-d5d7u-state"></a>
### 386. /policy/api/v1/orgs/default/projects/project-quality/vpcs/testvpc-3658f2b5/subnets/pod-default-ec7c1039_d5d7u/ports/prevpc-client-pod_d5d7u/state

**HTTP Methods:** GET

**Explanation:**
VPC subnet management within a project. Defines IP address ranges and network segments for VPC workloads.

---

<a id="387-policy-api-v1-orgs-default-projects-project-quality-vpcs-testvpc-3658f2b5-subnets-pod-default-ec7c1039-d5d7u-ports-prevpc-service-pod-d5d7u-state"></a>
### 387. /policy/api/v1/orgs/default/projects/project-quality/vpcs/testvpc-3658f2b5/subnets/pod-default-ec7c1039_d5d7u/ports/prevpc-service-pod_d5d7u/state

**HTTP Methods:** GET

**Explanation:**
VPC subnet management within a project. Defines IP address ranges and network segments for VPC workloads.

---

<a id="388-policy-api-v1-orgs-default-projects-project-quality-vpcs-subnet-e2e-1f11082b-56qvy-subnets-subnet-no-ip-56qvy-ports-port-in-no-ip-subnet-56qvy-state"></a>
### 388. /policy/api/v1/orgs/default/projects/project-quality/vpcs/subnet-e2e-1f11082b_56qvy/subnets/subnet-no-ip_56qvy/ports/port-in-no-ip-subnet_56qvy/state

**HTTP Methods:** GET

**Explanation:**
VPC subnet management within a project. Defines IP address ranges and network segments for VPC workloads.

---

<a id="389-policy-api-v1-orgs-default-projects-project-quality-vpcs-target-ns-56446c91-6zdip-subnets-vm-default-eb532fd0-c6gls-ports-port-e2e-test-3-c6gls-state"></a>
### 389. /policy/api/v1/orgs/default/projects/project-quality/vpcs/target-ns-56446c91_6zdip/subnets/vm-default-eb532fd0_c6gls/ports/port-e2e-test-3_c6gls/state

**HTTP Methods:** GET

**Explanation:**
VPC subnet management within a project. Defines IP address ranges and network segments for VPC workloads.

---

<a id="390-policy-api-v1-orgs-default-projects-project-quality-vpcs-subnet-e2e-1f11082b-56qvy-subnets-pod-default-6a81803a-56qvy-ports-port-e2e-test-1-56qvy-state"></a>
### 390. /policy/api/v1/orgs/default/projects/project-quality/vpcs/subnet-e2e-1f11082b_56qvy/subnets/pod-default-6a81803a_56qvy/ports/port-e2e-test-1_56qvy/state

**HTTP Methods:** GET

**Explanation:**
VPC subnet management within a project. Defines IP address ranges and network segments for VPC workloads.

---

<a id="391-policy-api-v1-orgs-default-projects-project-quality-vpcs-test-pod-sync-e8b8a7ca-m404i-subnets-pod-default-0dd88421-m404i-ports-test-pod-32c0f6bc-m404i-state"></a>
### 391. /policy/api/v1/orgs/default/projects/project-quality/vpcs/test-pod-sync-e8b8a7ca_m404i/subnets/pod-default-0dd88421_m404i/ports/test-pod-32c0f6bc_m404i/state

**HTTP Methods:** GET

**Explanation:**
VPC subnet management within a project. Defines IP address ranges and network segments for VPC workloads.

---

<a id="392-policy-api-v1-orgs-default-projects-project-quality-vpcs-test-pod-1dd9a577-fu9t5-subnets-pod-default-5cf92338-fu9t5-ports-test-source-pod-f9ba0670-fu9t5-state"></a>
### 392. /policy/api/v1/orgs/default/projects/project-quality/vpcs/test-pod-1dd9a577_fu9t5/subnets/pod-default-5cf92338_fu9t5/ports/test-source-pod-f9ba0670_fu9t5/state

**HTTP Methods:** GET

**Explanation:**
VPC subnet management within a project. Defines IP address ranges and network segments for VPC workloads.

---

<a id="393-policy-api-v1-orgs-default-projects-project-quality-vpcs-web-da775e6f-6o7ts-subnets-pod-default-a734dd59-6o7ts-ports-tcp-deployment-56bcbfc896-s7rng-6o7ts-state"></a>
### 393. /policy/api/v1/orgs/default/projects/project-quality/vpcs/web-da775e6f_6o7ts/subnets/pod-default-a734dd59_6o7ts/ports/tcp-deployment-56bcbfc896-s7rng_6o7ts/state

**HTTP Methods:** GET

**Explanation:**
VPC subnet management within a project. Defines IP address ranges and network segments for VPC workloads.

---

<a id="394-policy-api-v1-orgs-default-projects-project-quality-vpcs-web-da775e6f-6o7ts-subnets-pod-default-a734dd59-6o7ts-ports-tcp-deployment-56bcbfc896-xs2hs-6o7ts-state"></a>
### 394. /policy/api/v1/orgs/default/projects/project-quality/vpcs/web-da775e6f_6o7ts/subnets/pod-default-a734dd59_6o7ts/ports/tcp-deployment-56bcbfc896-xs2hs_6o7ts/state

**HTTP Methods:** GET

**Explanation:**
VPC subnet management within a project. Defines IP address ranges and network segments for VPC workloads.

---

<a id="395-policy-api-v1-orgs-default-projects-project-quality-vpcs-subnet-e2e-1f11082b-56qvy-subnets-user-subnetset-dhcp-c85186d8-56qvy-ports-port-in-dhcp-subnetset-56qvy-state"></a>
### 395. /policy/api/v1/orgs/default/projects/project-quality/vpcs/subnet-e2e-1f11082b_56qvy/subnets/user-subnetset-dhcp-c85186d8_56qvy/ports/port-in-dhcp-subnetset_56qvy/state

**HTTP Methods:** GET

**Explanation:**
VPC subnet management within a project. Defines IP address ranges and network segments for VPC workloads.

---

<a id="396-policy-api-v1-orgs-default-projects-project-quality-vpcs-test-create-vm-basic-f449d9bf-3ehn6-subnets-public-subnet-3ehn6-ports-public-vm-public-subnet-eth0-3ehn6-state"></a>
### 396. /policy/api/v1/orgs/default/projects/project-quality/vpcs/test-create-vm-basic-f449d9bf_3ehn6/subnets/public-subnet_3ehn6/ports/public-vm-public-subnet-eth0_3ehn6/state

**HTTP Methods:** GET

**Explanation:**
VPC subnet management within a project. Defines IP address ranges and network segments for VPC workloads.

---

<a id="397-policy-api-v1-orgs-default-projects-project-quality-vpcs-test-security-policy-match-expression-ff1dafa9-bgm74-subnets-pod-default-1289f64d-bgm74-ports-pod-a-bgm74-state"></a>
### 397. /policy/api/v1/orgs/default/projects/project-quality/vpcs/test-security-policy-match-expression-ff1dafa9_bgm74/subnets/pod-default-1289f64d_bgm74/ports/pod-a_bgm74/state

**HTTP Methods:** GET

**Explanation:**
VPC subnet management within a project. Defines IP address ranges and network segments for VPC workloads.

---

<a id="398-policy-api-v1-orgs-default-projects-project-quality-vpcs-subnet-e2e-1f11082b-56qvy-subnets-user-subnetset-static-948a4c45-56qvy-ports-port-in-static-subnetset-56qvy-state"></a>
### 398. /policy/api/v1/orgs/default/projects/project-quality/vpcs/subnet-e2e-1f11082b_56qvy/subnets/user-subnetset-static-948a4c45_56qvy/ports/port-in-static-subnetset_56qvy/state

**HTTP Methods:** GET

**Explanation:**
VPC subnet management within a project. Defines IP address ranges and network segments for VPC workloads.

---

<a id="399-policy-api-v1-orgs-default-projects-project-quality-vpcs-test-security-policy-match-expression-ff1dafa9-bgm74-subnets-pod-default-1289f64d-bgm74-ports-client-a-bgm74-state"></a>
### 399. /policy/api/v1/orgs/default/projects/project-quality/vpcs/test-security-policy-match-expression-ff1dafa9_bgm74/subnets/pod-default-1289f64d_bgm74/ports/client-a_bgm74/state

**HTTP Methods:** GET

**Explanation:**
VPC subnet management within a project. Defines IP address ranges and network segments for VPC workloads.

---

<a id="400-policy-api-v1-orgs-default-projects-project-quality-vpcs-test-security-policy-match-expression-ff1dafa9-bgm74-subnets-pod-default-1289f64d-bgm74-ports-client-b-bgm74-state"></a>
### 400. /policy/api/v1/orgs/default/projects/project-quality/vpcs/test-security-policy-match-expression-ff1dafa9_bgm74/subnets/pod-default-1289f64d_bgm74/ports/client-b_bgm74/state

**HTTP Methods:** GET

**Explanation:**
VPC subnet management within a project. Defines IP address ranges and network segments for VPC workloads.

---

<a id="401-policy-api-v1-orgs-default-projects-project-quality-vpcs-subnet-e2e-1f11082b-56qvy-subnets-subnet-dhcp-56qvy-ports-port-in-dhcp-subnet-with-address-bindings-vc-macpool-56qvy-state"></a>
### 401. /policy/api/v1/orgs/default/projects/project-quality/vpcs/subnet-e2e-1f11082b_56qvy/subnets/subnet-dhcp_56qvy/ports/port-in-dhcp-subnet-with-address-bindings-vc-macpool_56qvy/state

**HTTP Methods:** GET

**Explanation:**
VPC subnet management within a project. Defines IP address ranges and network segments for VPC workloads.

---

<a id="402-policy-api-v1-orgs-default-projects-project-quality-vpcs-subnet-e2e-1f11082b-56qvy-subnets-subnet-dhcp-56qvy-ports-port-in-dhcp-subnet-with-address-bindings-nsx-macpool-56qvy-state"></a>
### 402. /policy/api/v1/orgs/default/projects/project-quality/vpcs/subnet-e2e-1f11082b_56qvy/subnets/subnet-dhcp_56qvy/ports/port-in-dhcp-subnet-with-address-bindings-nsx-macpool_56qvy/state

**HTTP Methods:** GET

**Explanation:**
VPC subnet management within a project. Defines IP address ranges and network segments for VPC workloads.

---

<a id="403-policy-api-v1-orgs-default-projects-project-quality-vpcs-test-security-policy-basic-72ecfa65-ib6li-subnets-pod-default-db03dc29-ib6li-ports-server-client-68f86f99bc-2xkkv-ib6li-state"></a>
### 403. /policy/api/v1/orgs/default/projects/project-quality/vpcs/test-security-policy-basic-72ecfa65_ib6li/subnets/pod-default-db03dc29_ib6li/ports/server-client-68f86f99bc-2xkkv_ib6li/state

**HTTP Methods:** GET

**Explanation:**
VPC subnet management within a project. Defines IP address ranges and network segments for VPC workloads.

---

<a id="404-policy-api-v1-orgs-default-projects-project-quality-vpcs-test-security-policy-basic-72ecfa65-ib6li-subnets-pod-default-db03dc29-ib6li-ports-server-client-68f86f99bc-c2xvr-ib6li-state"></a>
### 404. /policy/api/v1/orgs/default/projects/project-quality/vpcs/test-security-policy-basic-72ecfa65_ib6li/subnets/pod-default-db03dc29_ib6li/ports/server-client-68f86f99bc-c2xvr_ib6li/state

**HTTP Methods:** GET

**Explanation:**
VPC subnet management within a project. Defines IP address ranges and network segments for VPC workloads.

---

<a id="405-policy-api-v1-orgs-default-projects-project-quality-vpcs-testvpc-3658f2b5-subnets-pod-default-ec7c1039-d5d7u-ports-vmware-system-image-280f8fa0-3f96-4aaf-bf38-390fbf5915ae-d5d7u-state"></a>
### 405. /policy/api/v1/orgs/default/projects/project-quality/vpcs/testvpc-3658f2b5/subnets/pod-default-ec7c1039_d5d7u/ports/vmware-system-image-280f8fa0-3f96-4aaf-bf38-390fbf5915ae_d5d7u/state

**HTTP Methods:** GET

**Explanation:**
VPC subnet management within a project. Defines IP address ranges and network segments for VPC workloads.

---

<a id="406-policy-api-v1-orgs-default-projects-project-quality-vpcs-testvpc-7ab2d8aa-subnets-pod-default-e0268dd8-5583h-ports-vmware-system-image-1a52a8a8-37d8-4ae2-b433-4a96be950051-5583h-state"></a>
### 406. /policy/api/v1/orgs/default/projects/project-quality/vpcs/testvpc-7ab2d8aa/subnets/pod-default-e0268dd8_5583h/ports/vmware-system-image-1a52a8a8-37d8-4ae2-b433-4a96be950051_5583h/state

**HTTP Methods:** GET

**Explanation:**
VPC subnet management within a project. Defines IP address ranges and network segments for VPC workloads.

---

<a id="407-policy-api-v1-orgs-default-projects-project-quality-vpcs-web-da775e6f-6o7ts-subnets-pod-default-a734dd59-6o7ts-ports-vmware-system-image-67d253b4-2743-45dd-86ca-a5de1909fc68-6o7ts-state"></a>
### 407. /policy/api/v1/orgs/default/projects/project-quality/vpcs/web-da775e6f_6o7ts/subnets/pod-default-a734dd59_6o7ts/ports/vmware-system-image-67d253b4-2743-45dd-86ca-a5de1909fc68_6o7ts/state

**HTTP Methods:** GET

**Explanation:**
VPC subnet management within a project. Defines IP address ranges and network segments for VPC workloads.

---

<a id="408-policy-api-v1-orgs-default-projects-project-quality-vpcs-web-da775e6f-6o7ts-subnets-pod-default-a734dd59-6o7ts-ports-vmware-system-image-b3305f6d-fd0d-4c43-9b16-78dc0b9f7ce2-6o7ts-state"></a>
### 408. /policy/api/v1/orgs/default/projects/project-quality/vpcs/web-da775e6f_6o7ts/subnets/pod-default-a734dd59_6o7ts/ports/vmware-system-image-b3305f6d-fd0d-4c43-9b16-78dc0b9f7ce2_6o7ts/state

**HTTP Methods:** GET

**Explanation:**
VPC subnet management within a project. Defines IP address ranges and network segments for VPC workloads.

---

<a id="409-policy-api-v1-orgs-default-projects-project-quality-vpcs-client-91c3f484-qzuxu-subnets-pod-default-075e5037-qzuxu-ports-vmware-system-image-b16a63d0-2b48-4e25-9222-ed24d7a5c67c-qzuxu-state"></a>
### 409. /policy/api/v1/orgs/default/projects/project-quality/vpcs/client-91c3f484_qzuxu/subnets/pod-default-075e5037_qzuxu/ports/vmware-system-image-b16a63d0-2b48-4e25-9222-ed24d7a5c67c_qzuxu/state

**HTTP Methods:** GET

**Explanation:**
VPC subnet management within a project. Defines IP address ranges and network segments for VPC workloads.

---

<a id="410-policy-api-v1-orgs-default-projects-project-quality-vpcs-test-lb-50fedbb3-mv836-subnets-pod-default-3cc5e9c8-mv836-ports-vmware-system-image-90dc9354-d875-41fe-b545-01332c956b5a-mv836-state"></a>
### 410. /policy/api/v1/orgs/default/projects/project-quality/vpcs/test-lb-50fedbb3_mv836/subnets/pod-default-3cc5e9c8_mv836/ports/vmware-system-image-90dc9354-d875-41fe-b545-01332c956b5a_mv836/state

**HTTP Methods:** GET

**Explanation:**
VPC subnet management within a project. Defines IP address ranges and network segments for VPC workloads.

---

<a id="411-policy-api-v1-orgs-default-projects-project-quality-vpcs-test-pod-1dd9a577-fu9t5-subnets-pod-default-5cf92338-fu9t5-ports-vmware-system-image-cd289a18-4ce4-4dff-a025-39f9d0636310-fu9t5-state"></a>
### 411. /policy/api/v1/orgs/default/projects/project-quality/vpcs/test-pod-1dd9a577_fu9t5/subnets/pod-default-5cf92338_fu9t5/ports/vmware-system-image-cd289a18-4ce4-4dff-a025-39f9d0636310_fu9t5/state

**HTTP Methods:** GET

**Explanation:**
VPC subnet management within a project. Defines IP address ranges and network segments for VPC workloads.

---

<a id="412-policy-api-v1-orgs-default-projects-project-quality-vpcs-test-pod-sync-e8b8a7ca-m404i-subnets-pod-default-0dd88421-m404i-ports-vmware-system-image-38f4d4f7-1fae-4270-9eb3-e8e9f2c5f08a-m404i-state"></a>
### 412. /policy/api/v1/orgs/default/projects/project-quality/vpcs/test-pod-sync-e8b8a7ca_m404i/subnets/pod-default-0dd88421_m404i/ports/vmware-system-image-38f4d4f7-1fae-4270-9eb3-e8e9f2c5f08a_m404i/state

**HTTP Methods:** GET

**Explanation:**
VPC subnet management within a project. Defines IP address ranges and network segments for VPC workloads.

---

<a id="413-policy-api-v1-orgs-default-projects-project-quality-vpcs-test-security-policy-basic-72ecfa65-ib6li-subnets-pod-default-db03dc29-ib6li-ports-vmware-system-image-7f80e1f0-a3f7-4d67-87e3-16162d5cdcc8-ib6li-state"></a>
### 413. /policy/api/v1/orgs/default/projects/project-quality/vpcs/test-security-policy-basic-72ecfa65_ib6li/subnets/pod-default-db03dc29_ib6li/ports/vmware-system-image-7f80e1f0-a3f7-4d67-87e3-16162d5cdcc8_ib6li/state

**HTTP Methods:** GET

**Explanation:**
VPC subnet management within a project. Defines IP address ranges and network segments for VPC workloads.

---

<a id="414-policy-api-v1-orgs-default-projects-project-quality-vpcs-test-security-policy-match-expression-ff1dafa9-bgm74-subnets-pod-default-1289f64d-bgm74-ports-vmware-system-image-78efc28d-50fb-4bf5-8eb3-5ff538be370c-bgm74-state"></a>
### 414. /policy/api/v1/orgs/default/projects/project-quality/vpcs/test-security-policy-match-expression-ff1dafa9_bgm74/subnets/pod-default-1289f64d_bgm74/ports/vmware-system-image-78efc28d-50fb-4bf5-8eb3-5ff538be370c_bgm74/state

**HTTP Methods:** GET

**Explanation:**
VPC subnet management within a project. Defines IP address ranges and network segments for VPC workloads.

---

<a id="415-policy-api-v1-orgs-default-projects-project-quality-vpcs-test-security-policy-match-expression-ff1dafa9-bgm74-subnets-pod-default-1289f64d-bgm74-ports-vmware-system-image-849fb668-f3ab-48bc-846b-38c485bd8f1f-bgm74-state"></a>
### 415. /policy/api/v1/orgs/default/projects/project-quality/vpcs/test-security-policy-match-expression-ff1dafa9_bgm74/subnets/pod-default-1289f64d_bgm74/ports/vmware-system-image-849fb668-f3ab-48bc-846b-38c485bd8f1f_bgm74/state

**HTTP Methods:** GET

**Explanation:**
VPC subnet management within a project. Defines IP address ranges and network segments for VPC workloads.

---

<a id="416-policy-api-v1-orgs-default-projects-project-quality-vpcs-test-security-policy-match-expression-ff1dafa9-bgm74-subnets-pod-default-1289f64d-bgm74-ports-vmware-system-image-92b67ea7-200d-4a00-92d3-c6974f97422f-bgm74-state"></a>
### 416. /policy/api/v1/orgs/default/projects/project-quality/vpcs/test-security-policy-match-expression-ff1dafa9_bgm74/subnets/pod-default-1289f64d_bgm74/ports/vmware-system-image-92b67ea7-200d-4a00-92d3-c6974f97422f_bgm74/state

**HTTP Methods:** GET

**Explanation:**
VPC subnet management within a project. Defines IP address ranges and network segments for VPC workloads.

---
