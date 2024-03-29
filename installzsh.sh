#!/bin/bash

set -o errexit
set -o nounset
set -o pipefail

# sh -c "$(curl -fsSL  https://raw.githubusercontent.com/zhengxiexie/scripts/main/installzsh.sh)"
# Update package repositories

# Set a default package manager
cmd=""

echo "Updating package repositories..."
if [ -f /etc/os-release ]; then
    . /etc/os-release
    case "$ID" in
        photon)
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
${cmd} install -y wget gcc make  binutils rsync git zsh


# Install autojump
echo "Installing autojump..."
git clone https://github.com/wting/autojump.git
cd autojump || exit
./install.py
cd ..

# Install oh-my-posh
curl -s https://ohmyposh.dev/install.sh | bash -s
# shellcheck disable=SC2016
echo 'eval "$(oh-my-posh init zsh)"' >> ~/.zshrc

# Set zsh as the default shell
echo "Setting zsh as the default shell..."
chsh -s /bin/zsh

zsh