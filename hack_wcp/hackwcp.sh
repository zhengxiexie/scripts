#!/bin/bash

set -o errexit
set -o nounset
set -o pipefail

tdnf install -y python3
tdnf install -y python3-pip
git clone https://github.com/zhengxiexie/scripts.git
cd scripts
pip3 install --index-url=https://packages.vcfd.broadcom.net/artifactory/api/pypi/pypi-remote/simple/ -r requirements.txt

echo "enable wcp sleep"
echo "python3 /root/scripts/hack_wcp/hack_wcp.py nsx-operator 0"
echo "enable wcp non-sleep"
echo "python3 /root/scripts/hack_wcp/hack_wcp.py nsx-operator 1"
