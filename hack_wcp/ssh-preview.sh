#!/bin/bash

# Enhanced SSH Hosts Preview Script with fzf support
# Shows SSH hosts with their descriptions and enables interactive selection

SSH_CONFIG="${HOME}/.ssh/config"

# Check if fzf is installed
if command -v fzf >/dev/null 2>&1; then
    USE_FZF=true
else
    USE_FZF=false
fi

# Function to parse SSH config and extract hosts with descriptions
parse_ssh_hosts() {
    awk '
        /^# Description:/ {
            # Store the description
            sub(/^# Description: /, "")
            desc = $0
            next
        }
        /^Host / && !/^Host \*/ {
            # Extract host name
            host = $0
            sub(/^Host /, "", host)
            # Handle hosts with spaces or special characters
            gsub(/\(.*\)/, "", host)  # Remove content in parentheses for display
            
            if (desc != "") {
                printf "%-40s │ %s\n", host, desc
                desc = ""
            } else {
                printf "%-40s │ (No description)\n", host
            }
        }
    ' "$SSH_CONFIG"
}

# Function to show hosts without fzf
show_hosts_plain() {
    echo "╭────────────────────────────────────────────────────────────────────────────╮"
    echo "│                         SSH Hosts Configuration                            │"
    echo "├────────────────────────────────────────────────────────────────────────────┤"
    
    parse_ssh_hosts | while IFS= read -r line; do
        printf "│ %-75s │\n" "$line"
    done
    
    echo "╰────────────────────────────────────────────────────────────────────────────╯"
    echo ""
    echo "💡 Tip: Install 'fzf' for interactive host selection: brew install fzf"
    echo "   Then use: ssh-preview (or sp) to interactively select and connect"
}

# Function to show hosts with fzf and connect
show_hosts_fzf() {
    local selected
    selected=$(parse_ssh_hosts | fzf \
        --header="Select SSH Host (ESC to cancel)" \
        --preview-window=hidden \
        --height=20 \
        --border=rounded \
        --prompt="SSH to > " \
        --pointer="▶" \
        --marker="✓" \
        --ansi)
    
    if [[ -n "$selected" ]]; then
        # Extract the hostname from the selected line
        hostname=$(echo "$selected" | cut -d'│' -f1 | xargs)
        echo "🔗 Connecting to: $hostname"
        echo "─────────────────────────────────────"
        tssh "$hostname"
    else
        echo "❌ No host selected"
    fi
}

# Main execution
main() {
    case "$1" in
        --list|-l)
            show_hosts_plain
            ;;
        --help|-h)
            echo "SSH Preview - Interactive SSH host selector with descriptions"
            echo ""
            echo "Usage:"
            echo "  ssh-preview [options]"
            echo ""
            echo "Options:"
            echo "  (no options)  Interactive mode with fzf (if installed)"
            echo "  --list, -l    List all hosts with descriptions"
            echo "  --help, -h    Show this help message"
            echo ""
            echo "Examples:"
            echo "  ssh-preview       # Interactive selection"
            echo "  ssh-preview -l    # List all hosts"
            ;;
        *)
            if $USE_FZF; then
                show_hosts_fzf
            else
                show_hosts_plain
                echo ""
                echo "💡 For interactive selection, install fzf: brew install fzf"
            fi
            ;;
    esac
}

main "$@"
