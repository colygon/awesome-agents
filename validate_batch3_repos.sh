#!/bin/bash
# Validation script for Batch 3 repositories
# This script checks which repositories exist and are accessible

echo "=== Batch 3 Repository Validation ==="
echo "Started: $(date)"
echo ""

repos=(
  "1cy1c3/friendtech_dashboard"
  "zusegd/umamusume_virgo_cup_dashboard"
  "arup-group/social-data"
  "mito-ds/mito-for-streamlit-demo"
  "data-science-at-swast/handover_poc"
  "aydinarda/tge_case-web-page"
  "hamagistral/de-zoomcamp-ui"
  "dataprofessor/hugchat"
  "koenleemans/paa"
  "steamship-packages/langchain-production-starter"
  "frog-land/chat2vis"
  "thomashacker/weaviate-magic-chat-demo"
  "e-johnstonn/docsummarizer"
  "singhjaspreetb/summerization-llm"
  "intelligenzaartificiale/ia-italia-chatbotv2"
)

valid_repos=()
invalid_repos=()

for repo in "${repos[@]}"; do
  echo -n "Checking $repo ... "
  if gh repo view "$repo" &>/dev/null; then
    echo "✅ EXISTS"
    valid_repos+=("$repo")
  else
    echo "❌ NOT FOUND"
    invalid_repos+=("$repo")
  fi
done

echo ""
echo "=== Summary ==="
echo "Valid repositories: ${#valid_repos[@]}"
echo "Invalid repositories: ${#invalid_repos[@]}"
echo ""

if [ ${#valid_repos[@]} -gt 0 ]; then
  echo "Valid repos:"
  for repo in "${valid_repos[@]}"; do
    echo "  - $repo"
  done
  echo ""
fi

if [ ${#invalid_repos[@]} -gt 0 ]; then
  echo "Invalid repos:"
  for repo in "${invalid_repos[@]}"; do
    echo "  - $repo"
  done
fi

echo ""
echo "Completed: $(date)"
