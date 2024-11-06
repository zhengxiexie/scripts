#!/bin/bash

set -o errexit
set -o nounset
set -o pipefail

rm -fr /root/.kubectx /usr/local/bin/kubectx /usr/local/bin/kubens /root/.kube-ps1 /usr/local/bat/bat /usr/local/bat /usr/local/go /root/go /usr/local/fubectl.source
# zsh -c "$(curl -fsSL  https://raw.githubusercontent.com/zhengxiexie/scripts/main/installk8stool.sh)"

# Install kubectx and kube-ps1
echo "Installing kubectx and kube-ps1..."
git clone https://github.com/ahmetb/kubectx.git ~/.kubectx
ln -s ~/.kubectx/kubectx /usr/local/bin/kubectx
ln -s ~/.kubectx/kubens /usr/local/bin/kubens
git clone https://github.com/jonmosco/kube-ps1.git ~/.kube-ps1
echo 'source ~/.kube-ps1/kube-ps1.sh' >> ~/.zshrc
echo 'export FUBECTL_WATCH_CMD=viddy' >> ~/.zshrc

# Install https://raw.githubusercontent.com/ahmetb/kubectl-aliases/master/.kubectl_aliases
#wget https://raw.githubusercontent.com/ahmetb/kubectl-aliases/master/.kubectl_aliases
#echo '[ -f ~/.kubectl_aliases ] && source ~/.kubectl_aliases' >> ~/.zshrc

# Install golang
#wget https://go.dev/dl/go1.22.5.linux-amd64.tar.gz
wget https://artifactory.vcfd.broadcom.net/artifactory/golang-dist/go1.22.5.linux-amd64.tar.gz
tar -C /usr/local -xzf go1.22.5.linux-amd64.tar.gz
# shellcheck disable=SC2016
echo 'export PATH=$PATH:/usr/local/go/bin' >> ~/.zshrc
# shellcheck disable=SC2016
echo 'export PATH=$PATH:/root/go/bin' >> ~/.zshrc
export PATH=$PATH:/usr/local/go/bin
go install github.com/trzsz/trzsz-go/cmd/trz@latest
go install github.com/trzsz/trzsz-go/cmd/tsz@latest
go install github.com/trzsz/trzsz-go/cmd/trzsz@latest

# Install Bat
curl -o bat.zip -L https://github.com/sharkdp/bat/releases/download/v0.18.2/bat-v0.18.2-x86_64-unknown-linux-musl.tar.gz
tar -xvzf bat.zip
mv bat-v0.18.2-x86_64-unknown-linux-musl /usr/local/bat
mv /usr/local/bat/bat /usr/local/bin

# Install fzf
curl -o fzf.zip -L https://github.com/junegunn/fzf/releases/download/0.48.1/fzf-0.48.1-linux_amd64.tar.gz
tar -xvzf fzf.zip
mv fzf /usr/local/bin/fzf

# Install exa
curl -o exa.zip -L https://github.com/ogham/exa/releases/download/v0.10.1/exa-linux-x86_64-v0.10.1.zip
unzip exa.zip
mv bin/exa /usr/local/bin/exa
echo 'alias ls=exa' >> ~/.zshrc

# Install ripgrep
curl -o rip.zip -L https://github.com/BurntSushi/ripgrep/releases/download/14.1.0/ripgrep-14.1.0-x86_64-unknown-linux-musl.tar.gz
tar -xvzf rip.zip
mv ripgrep-14.1.0-x86_64-unknown-linux-musl/rg /usr/local/bin

# Install ranger
curl -o ranger.zip -L https://ranger.github.io/ranger-stable.tar.gz
tar -xvzf ranger.zip
cd ranger-*
sudo python setup.py install --optimize=1 --record=install_log.txt

# Install Viddy
wget -O viddy.tar.gz https://github.com/sachaos/viddy/releases/download/v0.4.0/viddy_Linux_x86_64.tar.gz && tar xvf viddy.tar.gz && mv viddy /usr/local/bin

# Install Popeye
echo "Installing Popeye..."
wget https://github.com/derailed/popeye/releases/download/v0.21.3/popeye_linux_amd64.tar.gz
tar -xzvf popeye_linux_amd64.tar.gz
mv popeye /usr/local/bin

# Install Stern
echo "Installing Stern..."
wget https://github.com/stern/stern/releases/download/v1.30.0/stern_1.30.0_linux_amd64.tar.gz
tar -xzvf stern_1.30.0_linux_amd64.tar.gz
mv stern /usr/local/bin

# Install k9s
echo "Installing k9s..."
wget https://github.com/derailed/k9s/releases/download/v0.32.5/k9s_Linux_amd64.tar.gz
tar -xzvf k9s_Linux_amd64.tar.gz
mv k9s /usr/local/bin

# Install ketall
echo "Installing ketall..."
curl -Lo ketall.gz https://github.com/corneliusweig/ketall/releases/download/v1.3.8/ketall-amd64-linux.tar.gz
tar -xzvf ketall.gz
mv ketall-amd64-linux /usr/local/bin/ketall

# Install kubeshark
echo "Installing kubeshark..."
curl -Lo kubeshark https://github.com/kubeshark/kubeshark/releases/download/v52.3.74/kubeshark_linux_amd64
chmod 755 kubeshark
mv kubeshark /usr/local/bin/

# Install fubectl
#echo "Downloading fubectl.source..."
#curl -LO https://rawgit.com/kubermatic/fubectl/master/fubectl.source
#mv fubectl.source /usr/local/
#sed -i 's/complete -o default -F __start_kubectl k/compdef default __start_kubectl k/' /usr/local/fubectl.source
#echo "[ -f /usr/local/fubectl.source ] && source /usr/local/fubectl.source" >> ~/.zshrc

# Install atuin
echo "Downloading atuin..."
curl --proto '=https' --tlsv1.2 -LsSf https://setup.atuin.sh | sh
mv /root/.atuin/bin/atuin /usr/local/bin
atuin init zsh
sed -i 's/enter_accept = true/enter_accept = false/' ~/.config/atuin/config.toml
sed -i 's/# style = "auto"/style = "compact"/' ~/.config/atuin/config.toml
cat <<EOF >> ~/.zshrc
export ATUIN_NOBIND="true"
eval "$(atuin init zsh)"
bindkey '^r' atuin-search
# bind to the up key, which depends on terminal mode
bindkey '^[[A' atuin-up-search
bindkey '^[OA' atuin-up-search
EOF

# Configure k9s plugin
echo "Configuring k9s plugin..."
mkdir -p ~/.config/k9s/
touch ~/.config/k9s/plugin.yml
cat <<EOF > ~/.config/k9s/plugin.yml
plugin:
  # See https://k9scli.io/topics/plugins/
  dive:
    shortCut: d
    confirm: false
    description: "Dive image"
    scopes:
      - containers
    command: dive
    background: false
    args:
      - \$COL-IMA
  debug:
    shortCut: Shift-D
    description: Add debug container
    scopes:
      - containers
    command: bash
    background: false
    confirm: true
    args:
      - -c
      - "kubectl debug -it -n=\$NAMESPACE \$POD --target=\$NAME --image=harbor-repo.vmware.com/nsx_ujo/netshoot:latest -- /bin/bash"
  watch-events:
    shortCut: Shift-E
    confirm: false
    description: Get Events
    scopes:
    - all
    command: sh
    background: false
    args:
    - -c
    - "watch -n 5 kubectl get events --context \$CONTEXT --namespace \$NAMESPACE --field-selector involvedObject.name=\$NAME"
  get-all-namespace:
    shortCut: g
    confirm: false
    description: get-all
    scopes:
    - namespaces
    command: sh
    background: false
    args:
    - -c
    - "kubectl get all --context \$CONTEXT -A | less"
  raw-logs-follow:
    shortCut: Ctrl-L
    description: logs -f
    scopes:
    - po
    command: kubectl
    background: false
    args:
    - logs
    - -f
    - \$NAME
    - -n
    - \$NAMESPACE
    - --context
    - \$CONTEXT
    - --kubeconfig
    - \$KUBECONFIG
  log-less:
    shortCut: Shift-L
    description: "logs|less"
    scopes:
    - po
    command: bash
    background: false
    args:
    - -c
    - '"$@" | less'
    - dummy-arg
    - kubectl
    - logs
    - \$NAME
    - -n
    - \$NAMESPACE
    - --context
    - \$CONTEXT
    - --kubeconfig
    - \$KUBECONFIG
  log-less-container:
    shortCut: Shift-L
    description: "logs|less"
    scopes:
    - containers
    command: bash
    background: false
    args:
    - -c
    - '"$@" | less'
    - dummy-arg
    - kubectl
    - logs
    - -c
    - \$NAME
    - \$POD
    - -n
    - \$NAMESPACE
    - --context
    - \$CONTEXT
    - --kubeconfig
    - \$KUBECONFIG
  raw-logs-follow-container:
    shortCut: Ctrl-L
    description: "logs|less"
    scopes:
    - containers
    command: bash
    background: false
    args:
    shortCut: Ctrl-L
    description: logs -f
    scopes:
    - containers
    command: kubectl
    background: false
    args:
    - logs
    - -f
    - -c
    - \$NAME
    - \$POD
    - -n
    - \$NAMESPACE
    - --context
    - \$CONTEXT
    - --kubeconfig
    - \$KUBECONFIG
EOF

echo "Installation completed successfully!"

zsh && source ~/.zshrc