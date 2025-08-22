#!/bin/bash

# Daily Configuration Backup Script
# Backs up important config files to iCloud Documents

# Set variables
BACKUP_DATE=$(date +%Y%m%d_%H%M%S)
ICLOUD_CONFIG_DIR="/Users/zhengxie/Library/Mobile Documents/com~apple~CloudDocs/config"
LOG_FILE="/Users/zhengxie/Library/Logs/config-backup.log"

# Function to log messages
log_message() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1" >> "$LOG_FILE"
}

# Start backup
log_message "Starting configuration backup"

# Create backup directory if it doesn't exist
if [ ! -d "$ICLOUD_CONFIG_DIR" ]; then
    mkdir -p "$ICLOUD_CONFIG_DIR"
    log_message "Created backup directory: $ICLOUD_CONFIG_DIR"
fi

# Backup files and directories
ITEMS_TO_BACKUP=(
    "$HOME/.ssh"
    "$HOME/.zshrc"
    "$HOME/.gitconfig"
    "$HOME/.liketheme"
)

# Perform backup
for item in "${ITEMS_TO_BACKUP[@]}"; do
    if [ -e "$item" ]; then
        # Get the base name of the item
        basename_item=$(basename "$item")
        
        # Remove existing backup first to avoid permission issues
        target_path="$ICLOUD_CONFIG_DIR/$basename_item"
        if [ -e "$target_path" ]; then
            rm -rf "$target_path"
        fi
        
        # Copy the item to iCloud
        if cp -r "$item" "$ICLOUD_CONFIG_DIR/"; then
            log_message "Successfully backed up: $item"
        else
            log_message "ERROR: Failed to backup: $item"
        fi
    else
        log_message "WARNING: Item not found: $item"
    fi
done

# Fix permissions for the backed up .ssh directory
if [ -d "$ICLOUD_CONFIG_DIR/.ssh" ]; then
    chmod 700 "$ICLOUD_CONFIG_DIR/.ssh"
    chmod 600 "$ICLOUD_CONFIG_DIR/.ssh/id_rsa" 2>/dev/null
    chmod 644 "$ICLOUD_CONFIG_DIR/.ssh/id_rsa.pub" 2>/dev/null
    chmod 600 "$ICLOUD_CONFIG_DIR/.ssh/config" 2>/dev/null
    log_message "Fixed permissions for .ssh directory"
fi

log_message "Configuration backup completed"
