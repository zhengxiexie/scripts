#!/bin/bash

set -o errexit
set -o nounset
set -o pipefail

tdnf install -y python3
tdnf install -y python3-pip
git clone https://github.com/zhengxiexie/scripts.git
cd scripts
pip3 install -r requirements.txt

echo "enable wcp sleep"
echo "python3 main.py 0"
echo "enable wcp non-sleep"
echo "python3 main.py 1"
