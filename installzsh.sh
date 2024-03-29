#!/bin/bash


set -o xtrace
set -o errexit
set -o nounset
set -o pipefail

# sh -c "$(curl -fsSL  https://raw.githubusercontent.com/zhengxiexie/scripts/main/installzsh.sh)"
# Update package repositories
echo "Updating package repositories..."
if [ -f /etc/os-release ]; then
    . /etc/os-release
    if [ "$ID" = "photon" ]; then
      cmd="tdnf"
    elif [ "$ID" = "ubuntu" ]; then
      cmd="apt"
    elif [ "$ID" = "centos" ]; then
      cmd="yum"
    fi
fi

$cmd update

# Install required packages
echo "Installing required packages..."
$cmd install -y wget gcc make python binutils rsync git zsh fzf autojump

# Install autojump
echo "Installing autojump..."
git clone https://github.com/wting/autojump.git
cd autojump || exit
./install.py or ./uninstall.py
cd ..

# Install oh-my-zsh
echo "Installing oh-my-zsh..."
wget https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh
sh install.sh --unattended

# Set zsh as the default shell
echo "Setting zsh as the default shell..."
chsh -s /bin/zsh

# Install zsh plugins
echo "Installing zsh plugins..."
git clone https://github.com/zsh-users/zsh-syntax-highlighting.git "${ZSH_CUSTOM:-~/.oh-my-zsh/custom}"/plugins/zsh-syntax-highlighting
git clone https://github.com/zsh-users/zsh-autosuggestions "${ZSH_CUSTOM:-~/.oh-my-zsh/custom}"/plugins/zsh-autosuggestions
git clone https://github.com/zsh-users/zsh-history-substring-search "${ZSH_CUSTOM:-~/.oh-my-zsh/custom}"/plugins/zsh-history-substring-search

# Configure zsh theme and plugins
echo "Configuring zsh theme and plugins..."
sed -i 's/plugins=(\(.*\))/plugins=(\1 git zsh-syntax-highlighting zsh-autosuggestions autojump colored-man-pages cp vi-mode zsh-history-substring-search)/' ~/.zshrc
# eval "$(oh-my-posh init zsh)" to ~/.zshrc
# shellcheck disable=SC2016
echo 'eval "$(oh-my-posh init zsh)"' >> ~/.zshrc

# Source the modified zshrc file
echo "Sourcing the modified zshrc file..."
# shellcheck disable=SC1090
zsh && source ~/.zshrc