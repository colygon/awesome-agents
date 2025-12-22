#!/bin/bash

# Single App Upgrade Script
# Usage: ./upgrade_single_app.sh <app_id> <app_name> <github_url> <repo_name>

APP_ID=$1
APP_NAME=$2
GITHUB_URL=$3
REPO_NAME=$4
TARGET_DIR="${REPO_NAME}-agent${APP_ID}"

echo "============================================"
echo "Processing: $APP_NAME (agent$APP_ID)"
echo "GitHub: $GITHUB_URL"
echo "Target: $TARGET_DIR"
echo "============================================"

# Step 1: Fork repository
echo "Step 1: Forking repository..."
gh repo fork "$GITHUB_URL" --clone=false 2>&1 | tee /tmp/fork_output.txt
FORK_STATUS=$?

# Extract the fork URL from the output
FORK_URL=$(grep -o "colygon/[^ ]*" /tmp/fork_output.txt | head -1 | sed 's/colygon\//https:\/\/github.com\/colygon\//')

if [ -z "$FORK_URL" ]; then
    # Try alternative fork URL construction
    FORK_URL="https://github.com/colygon/$(basename $GITHUB_URL)"
fi

echo "Fork URL: $FORK_URL"

# Step 2: Clone repository
echo "Step 2: Cloning repository to $TARGET_DIR..."
if [ -d "$TARGET_DIR" ]; then
    echo "Directory $TARGET_DIR already exists, skipping clone"
else
    git clone "$FORK_URL" "$TARGET_DIR"
    CLONE_STATUS=$?
    if [ $CLONE_STATUS -ne 0 ]; then
        echo "ERROR: Failed to clone repository"
        exit 1
    fi
fi

echo "Successfully prepared $APP_NAME for upgrade"
echo "Next: Analyze codebase and implement CrewAI upgrade"
