#!/bin/bash

# Batch 6 Upgrade Helper Script
# This script helps fork, clone, and prepare repos for CrewAI upgrade

set -e

# Function to fork a repo
fork_repo() {
    local github_url=$1
    local repo_name=$(echo $github_url | sed 's/.*\///')

    echo "Forking $github_url..."
    gh repo fork $github_url --clone=false --fork-name $repo_name --org colygon || true
    echo "https://github.com/colygon/$repo_name"
}

# Function to clone a repo
clone_repo() {
    local repo_name=$1
    local target_dir=$2

    echo "Cloning colygon/$repo_name to $target_dir..."
    if [ -d "$target_dir" ]; then
        echo "Directory $target_dir already exists, skipping clone"
    else
        git clone "https://github.com/colygon/$repo_name.git" "$target_dir"
    fi
}

# Function to update results JSON
update_results() {
    local app_id=$1
    local field=$2
    local value=$3
    local results_file="/Users/colinlowenberg/crew/BATCH_6_RESULTS.json"

    # Use jq to update the results file
    jq --arg id "$app_id" --arg field "$field" --arg value "$value" \
        '(.apps[] | select(.id == ($id | tonumber)) | .[$field]) = $value' \
        "$results_file" > "${results_file}.tmp" && mv "${results_file}.tmp" "$results_file"
}

# Export functions for use in subshells
export -f fork_repo
export -f clone_repo
export -f update_results

# Main execution
case "${1:-}" in
    fork)
        fork_repo "$2"
        ;;
    clone)
        clone_repo "$2" "$3"
        ;;
    update)
        update_results "$2" "$3" "$4"
        ;;
    *)
        echo "Usage: $0 {fork|clone|update} [args...]"
        echo "  fork <github_url>"
        echo "  clone <repo_name> <target_dir>"
        echo "  update <app_id> <field> <value>"
        exit 1
        ;;
esac
