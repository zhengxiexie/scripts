#!/bin/bash

# Check if build number argument is provided
if [ $# -eq 0 ]; then
    echo "Please provide a build number as an argument."
    exit 1
fi

BUILD_NUMBER=$1

# Extract version number from BUILD_NUMBER
VERSION=$(echo $BUILD_NUMBER | sed 's/sb-//')

# Download tar files
echo "Downloading tar files..."
curl "http://build-squid.vcfd.broadcom.net/build/mts/release/$BUILD_NUMBER/publish/nsx-container/Kubernetes/nsx-ncp-photon-4.2.0.$VERSION.tar" -O
curl "http://build-squid.vcfd.broadcom.net/build/mts/release/$BUILD_NUMBER/publish/nsx-container/Kubernetes/nsx-operator-4.2.0.$VERSION.tar" -O

# Import images
echo "Importing images..."
sudo ctr --debug --namespace k8s.io images import "nsx-ncp-photon-4.2.0.$VERSION.tar"
sudo ctr --debug --namespace k8s.io images import "nsx-operator-4.2.0.$VERSION.tar"

# Check imported images
echo "Checking imported images..."
crictl images | grep "$VERSION"

# Label current node
echo "Labeling current node..."
NODE_NAME=$(hostname)
kubectl label nodes $NODE_NAME node-role.kubernetes.io/control-plane=replace --overwrite

# Edit deployment
echo "Editing deployment..."
kubectl get deployment nsx-ncp -n vmware-system-nsx -o yaml | \
sed "s|replicas: 2|replicas: 1|" | \
sed 's|node-role.kubernetes.io/control-plane: ""|node-role.kubernetes.io/control-plane: "replace"|g' | \
sed "s|image: localhost:5000/vmware/nsx-ncp-photon:[^ ]*|image: registry.local/4.2.0.$VERSION/nsx-ncp-photon:latest|g" | \
sed "s|image: localhost:5000/vmware/nsx-operator:[^ ]*|image: registry.local/4.2.0.$VERSION/nsx-operator:latest|g" | \
head -n -18 | \
kubectl apply -f -

echo "Script completed successfully."