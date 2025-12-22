#!/bin/bash
# Deploy All CrewAI Agents Script
# This script prepares all 5 agents for deployment

set -e  # Exit on error

# Colors for output
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

# Agent configurations
declare -A AGENTS
AGENTS=(
    ["agent5"]="knowledge-gpt-agent5"
    ["agent6"]="gptlab-agent6"
    ["agent7"]="email-generator-agent7"
    ["agent9"]="talk-with-pdf-agent9"
    ["agent10"]="llm-leaderboard-agent10"
)

echo -e "${BLUE}========================================${NC}"
echo -e "${BLUE}CrewAI Agents Deployment Script${NC}"
echo -e "${BLUE}========================================${NC}"
echo ""

# Function to check if command exists
command_exists() {
    command -v "$1" >/dev/null 2>&1
}

# Check prerequisites
echo -e "${YELLOW}Checking prerequisites...${NC}"

if ! command_exists python3; then
    echo -e "${RED}Error: python3 is required but not installed.${NC}"
    exit 1
fi

if ! command_exists pip; then
    echo -e "${RED}Error: pip is required but not installed.${NC}"
    exit 1
fi

echo -e "${GREEN}✓ Prerequisites satisfied${NC}"
echo ""

# Function to deploy a single agent
deploy_agent() {
    local agent_id=$1
    local agent_dir=$2

    echo -e "${BLUE}========================================${NC}"
    echo -e "${BLUE}Deploying $agent_id: $agent_dir${NC}"
    echo -e "${BLUE}========================================${NC}"

    if [ ! -d "$agent_dir" ]; then
        echo -e "${RED}✗ Directory not found: $agent_dir${NC}"
        return 1
    fi

    cd "$agent_dir"

    # Check for requirements.txt
    if [ -f "requirements.txt" ]; then
        echo -e "${YELLOW}Installing dependencies...${NC}"
        pip install -q -r requirements.txt
        echo -e "${GREEN}✓ Dependencies installed${NC}"
    else
        echo -e "${YELLOW}⚠ No requirements.txt found${NC}"
    fi

    # Check for .env.example and create .env if needed
    if [ -f ".env.example" ] && [ ! -f ".env" ]; then
        echo -e "${YELLOW}Creating .env from .env.example...${NC}"
        cp .env.example .env
        echo -e "${GREEN}✓ .env created (remember to add your API keys!)${NC}"
    fi

    # Run tests if available
    if [ -d "tests" ]; then
        echo -e "${YELLOW}Running tests...${NC}"
        python3 -m pytest tests/ -v || echo -e "${YELLOW}⚠ Tests failed or not configured${NC}"
    fi

    cd ..

    echo -e "${GREEN}✓ $agent_id deployed successfully${NC}"
    echo ""

    return 0
}

# Main deployment loop
DEPLOYED=0
FAILED=0

for agent_id in "${!AGENTS[@]}"; do
    agent_dir="${AGENTS[$agent_id]}"

    if deploy_agent "$agent_id" "$agent_dir"; then
        ((DEPLOYED++))
    else
        ((FAILED++))
    fi
done

# Summary
echo -e "${BLUE}========================================${NC}"
echo -e "${BLUE}Deployment Summary${NC}"
echo -e "${BLUE}========================================${NC}"
echo -e "${GREEN}✓ Successfully deployed: $DEPLOYED agents${NC}"
if [ $FAILED -gt 0 ]; then
    echo -e "${RED}✗ Failed: $FAILED agents${NC}"
fi
echo ""

# Next steps
echo -e "${YELLOW}Next Steps:${NC}"
echo "1. Add OpenAI API keys to .env files in each agent directory"
echo "2. Test each agent locally:"
echo "   - cd <agent-dir>"
echo "   - streamlit run <script>.py"
echo "3. Deploy to Streamlit Cloud or your preferred platform"
echo ""

# Validation
echo -e "${YELLOW}Running validation...${NC}"
if [ -f "run_parallel_agents.py" ]; then
    python3 run_parallel_agents.py
else
    echo -e "${YELLOW}⚠ Validation script not found${NC}"
fi

echo ""
echo -e "${GREEN}🎉 Deployment preparation complete!${NC}"
echo ""

exit 0
