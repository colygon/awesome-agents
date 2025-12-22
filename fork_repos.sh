#!/bin/bash

# Script to fork all Streamlit app repositories
# This creates our own copies where we can make CrewAI upgrades

LOG_FILE="/tmp/fork_streamlit_repos.log"
ERROR_FILE="/tmp/fork_streamlit_repos_errors.log"

echo "Starting fork process at $(date)" > "$LOG_FILE"
echo "Errors log:" > "$ERROR_FILE"

# Read the analysis results and fork repos that need upgrading
if [ ! -f "./app_analysis_results.json" ]; then
    echo "Error: app_analysis_results.json not found!"
    echo "Please run: node analyze_streamlit_apps.js first"
    exit 1
fi

# Extract GitHub URLs from apps that need upgrading (not HAS_CREWAI, not ERROR)
urls=$(node -e "
const data = require('./app_analysis_results.json');
const needsUpgrade = data.filter(app =>
    app.classification !== 'HAS_CREWAI' &&
    app.classification !== 'ERROR'
);
needsUpgrade.forEach(app => console.log(app.github_url));
")

total=0
success=0
failed=0
skipped=0

for repo_url in $urls; do
    ((total++))

    # Extract owner/repo from URL
    repo_path=$(echo "$repo_url" | sed 's|https://github.com/||')

    echo "[$total] Checking: $repo_path" | tee -a "$LOG_FILE"

    # Check if we already forked it
    if gh repo view "colygon/$repo_path" &>/dev/null; then
        ((skipped++))
        echo "  ⊙ Already forked" | tee -a "$LOG_FILE"
    else
        # Fork the repository
        if gh repo fork "$repo_path" --clone=false 2>&1 | tee -a "$LOG_FILE"; then
            ((success++))
            echo "  ✓ Forked successfully" | tee -a "$LOG_FILE"
        else
            ((failed++))
            echo "  ✗ Failed: $repo_path" | tee -a "$ERROR_FILE"
        fi
    fi

    # Small delay to avoid rate limiting
    sleep 1
done

echo "" | tee -a "$LOG_FILE"
echo "================================" | tee -a "$LOG_FILE"
echo "Fork process completed at $(date)" | tee -a "$LOG_FILE"
echo "Total: $total | Success: $success | Skipped: $skipped | Failed: $failed" | tee -a "$LOG_FILE"
echo "================================" | tee -a "$LOG_FILE"
echo ""
echo "Check $LOG_FILE for full log"
echo "Check $ERROR_FILE for errors"
