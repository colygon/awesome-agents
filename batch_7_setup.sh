#!/bin/bash

# Batch 7 Repository Setup Script
# This script forks and clones all repositories for batch 7

set -e

CREW_DIR="/Users/colinlowenberg/crew"
cd "$CREW_DIR"

echo "Starting Batch 7 repository setup..."

# Array of apps with format: "id|github_url|folder_name|repo_name"
declare -a apps=(
    "224|https://github.com/stavrostheocharis/streamlit-apps-showcase|tokencraft-agent224|streamlit-apps-showcase"
    "195|https://github.com/martin1998215/locasx|quest2query-agent195|locasx"
    "171|https://github.com/sean1832/sumgpt|sumgpt-agent171|sumgpt"
    "145|https://github.com/czubert/sersitivis|sersitivis-agent145|sersitivis"
    "93|https://github.com/langchain-ai/streamlit-agent|mrkl-agent93|streamlit-agent"
    "83|https://github.com/chrieke/prettymapp|prettymapp-agent83|prettymapp"
    "223|https://github.com/laxman001/snowdq|snowdq-agent223|snowdq"
    "194|https://github.com/basil-chatha/taxgpt|taxgpt-agent194|taxgpt"
    "84|https://github.com/jkanner/streamlit-dataview|gwquickview-agent84|streamlit-dataview"
    "253|https://github.com/nurinsalsabl/pmpjnotarisjatim|pmpjatim-agent253|pmpjnotarisjatim"
    "144|https://github.com/mydgd/snowflake-table-catalog|snowflake-catalog-agent144|snowflake-table-catalog"
    "222|https://github.com/jumitti/tfinder|tfinder-agent222|tfinder"
    "228|https://github.com/semantha/kate1|kate-agent228|kate1"
    "170|https://github.com/iamontheinet/snowpark-python-anaconda|snowpark-agent170|snowpark-python-anaconda"
    "143|https://github.com/voltackle67/smartprep-q1|smartprep-agent143|smartprep-q1"
    "117|https://github.com/panditpranav/svm_covid_tracking|covid19-agent117|svm_covid_tracking"
    "193|https://github.com/maxwellknowles/catalyst|aspasia-agent193|catalyst"
    "86|https://github.com/kinshukk/gitagpt|gitagpt-agent86|gitagpt"
    "169|https://github.com/streamlit/release-demos|streamlit128-agent169|release-demos"
    "142|https://github.com/snowflake-labs/sfquickstart-data-clean-room|dcr-agent142|sfquickstart-data-clean-room"
)

success_count=0
fail_count=0
declare -a failed_apps=()

for app in "${apps[@]}"; do
    IFS='|' read -r id github_url folder_name repo_name <<< "$app"

    echo ""
    echo "========================================="
    echo "Processing app $id: $folder_name"
    echo "========================================="

    # Skip if directory already exists
    if [ -d "$folder_name" ]; then
        echo "Directory $folder_name already exists, skipping..."
        ((success_count++))
        continue
    fi

    # Fork the repository
    echo "Forking $github_url..."
    if gh repo fork "$github_url" --clone=false --fork-name "$repo_name" --org colygon 2>/dev/null; then
        echo "Fork successful"
    else
        echo "Fork may already exist or failed, continuing..."
    fi

    # Clone the forked repository
    echo "Cloning to $folder_name..."
    if git clone "https://github.com/colygon/$repo_name.git" "$folder_name"; then
        cd "$folder_name"

        # Set up upstream remote
        git remote add upstream "$github_url" 2>/dev/null || true

        cd "$CREW_DIR"
        echo "Successfully set up $folder_name"
        ((success_count++))
    else
        echo "Failed to clone $folder_name"
        failed_apps+=("$id: $folder_name")
        ((fail_count++))
    fi
done

echo ""
echo "========================================="
echo "Batch 7 Setup Complete"
echo "========================================="
echo "Successful: $success_count"
echo "Failed: $fail_count"

if [ ${#failed_apps[@]} -gt 0 ]; then
    echo ""
    echo "Failed apps:"
    for failed in "${failed_apps[@]}"; do
        echo "  - $failed"
    done
fi
