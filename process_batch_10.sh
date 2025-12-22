#!/bin/bash

# Batch 10 Processing Script
# This script systematically processes each app in batch 10

# Results tracking
RESULTS_FILE="/Users/colinlowenberg/crew/BATCH_10_RESULTS.json"

# Initialize results
cat > "$RESULTS_FILE" << 'EOF'
{
  "batch_number": 10,
  "total_apps": 20,
  "processed": 0,
  "successful": 0,
  "failed": 0,
  "skipped": 0,
  "apps": []
}
EOF

# Function to add app result
add_result() {
    local id=$1
    local title=$2
    local status=$3
    local message=$4
    local directory=$5

    python3 << PYTHON
import json
import sys

results_file = "$RESULTS_FILE"
with open(results_file, 'r') as f:
    data = json.load(f)

data['apps'].append({
    'id': $id,
    'title': "$title",
    'status': "$status",
    'message': "$message",
    'directory': "$directory"
})

data['processed'] += 1
if [ "$status" = "success" ]; then
    data['successful'] += 1
elif [ "$status" = "failed" ]; then
    data['failed'] += 1
elif [ "$status" = "skipped" ]; then
    data['skipped'] += 1
fi

with open(results_file, 'w') as f:
    json.dump(data, f, indent=2)
PYTHON
}

echo "Starting Batch 10 processing..."

# App 133: State of LLM Apps 2023 - llm-report
add_result 133 "State of LLM Apps 2023" "failed" "Repository not accessible (404)" ""

# App 109: McLachApp - ALREADY COMPLETED
add_result 109 "McLachApp" "success" "Already completed" "mclach-agent60"

# App 230: Streamlit cheat sheet - ALREADY COMPLETED
add_result 230 "Streamlit cheat sheet" "success" "Already completed" "cheatsheet-agent19"

# App 274: Industry Agents - crewAI-examples (SKIP)
add_result 274 "Industry Agents" "skipped" "Already a CrewAI example repository" ""

# App 272: Recruitment Crew - crewAI-examples (SKIP)
add_result 272 "Recruitment Crew" "skipped" "Already a CrewAI example repository" ""

echo "Batch 10 initial processing complete. Check $RESULTS_FILE for details."
