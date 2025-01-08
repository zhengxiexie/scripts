#!/bin/bash

set -o errexit
set -o nounset
set -o pipefail

# sh -c "$(curl -fsSL  https://raw.githubusercontent.com/zhengxiexie/scripts/main/installzsh.sh)"
# Update package repositories

# Set a default package manager
cmd=""

mkdir -p /root/.local/bin
export PATH=$PATH:/root/.local/bin
rm -fr ~/autojump ~/.autojump/ ~/.zsh ~/.zshrc ~/.kube-ps1/ ~/oh-my-posh

echo "Updating package repositories..."
if [ -f /etc/os-release ]; then
    . /etc/os-release
    case "$ID" in
        photon)
          # Photon OS uses a different repository URL than other Linux distributions
            /usr/bin/sed -i \
              's|packages.vmware.com/photon|artifactory.vcfd.broadcom.net/artifactory/photon-remote|g' \
              /etc/yum.repos.d/*.repo
            cmd="tdnf"
            ;;
        ubuntu)
            cmd="apt"
            ;;
        centos)
            cmd="yum"
            ;;
        *)
            echo "Unsupported distribution: $ID"
            exit 1
            ;;
    esac
else
    echo "/etc/os-release not found. Cannot determine package manager."
    exit 1
fi

# Ensure cmd is not empty
if [ -z "$cmd" ]; then
    echo "Package manager command not set. Exiting."
    exit 1
fi

echo "Using $cmd for package management."
${cmd} update -y

echo "Installing required packages..."
case "$ID" in
    ubuntu)
        sudo apt install snapd
        snap install go --classic
        ${cmd} install -y wget gcc make  binutils rsync git zsh zip
        ;;
    photon)
        ${cmd} install -y wget gcc make  binutils rsync go git zsh zip unzip glibc-devel syslinux-devel linux-api-headers
        ;;
    centos)
        ${cmd} install -y wget gcc make  binutils rsync go git zsh zip unzip glibc-devel syslinux-devel linux-api-headers
        ;;
esac


# Install autojump
echo "Installing autojump..."
git clone https://github.com/wting/autojump.git
cd autojump || exit
./install.py
cd ..

# Install oh-my-posh
curl -s https://ohmyposh.dev/install.sh | bash -s
git clone https://github.com/JanDeDobbeleer/oh-my-posh

# Set zsh as the default shell
#echo "Setting zsh as the default shell..."
#chsh -s /bin/zsh

# Install zsh plugins
echo "Installing zsh plugins..."
mkdir .zsh
git clone https://github.com/zsh-users/zsh-autosuggestions.git .zsh/zsh-autosuggestions
git clone https://github.com/zsh-users/zsh-syntax-highlighting.git .zsh/zsh-syntax-highlightings
git clone https://github.com/zsh-users/zsh-history-substring-search .zsh/zsh-history-substring-search
git clone https://github.com/jeffreytse/zsh-vi-mode.git .zsh/.zsh-vi-mode

# shellcheck disable=SC2016
echo 'export PATH=$PATH:/root/bin' >> ~/.zshrc
echo 'export PATH=$PATH:/root/.local/bin' >> ~/.zshrc
echo 'eval "$(oh-my-posh init zsh  --config ~/oh-my-posh/themes/catppuccin.omp.json)"' >> ~/.zshrc
# shellcheck disable=SC1090
echo 'source ~/.zsh/zsh-autosuggestions/zsh-autosuggestions.zsh' >> ~/.zshrc
# shellcheck disable=SC1090
echo 'source ~/.zsh/zsh-syntax-highlightings/zsh-syntax-highlighting.zsh' >> ~/.zshrc
# shellcheck disable=SC1090
echo 'source ~/.zsh/zsh-history-substring-search/zsh-history-substring-search.zsh' >> ~/.zshrc
echo '[[ -s /root/.autojump/etc/profile.d/autojump.sh ]] && source /root/.autojump/etc/profile.d/autojump.sh' >> ~/.zshrc
echo 'autoload -U compinit && compinit -u' >> ~/.zshrc
echo 'source ~/.zsh/.zsh-vi-mode/zsh-vi-mode.plugin.zsh' >> ~/.zshrc