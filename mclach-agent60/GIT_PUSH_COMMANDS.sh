#!/bin/bash
# Git commands to initialize repository and push to crewai-upgrade branch
# Execute these commands to complete the git setup

echo "McLachApp CrewAI Upgrade - Git Setup Commands"
echo "=============================================="
echo ""

# Navigate to project directory
echo "Step 1: Navigate to project directory"
echo "cd /Users/colinlowenberg/crew/mclach-agent60"
echo ""

# Initialize git repository
echo "Step 2: Initialize git repository"
echo "git init"
echo ""

# Add all files
echo "Step 3: Add all files to git"
echo "git add ."
echo ""

# Create initial commit
echo "Step 4: Create initial commit"
cat << 'EOF'
git commit -m "Initial commit: McLachApp CrewAI upgrade by Agent 60

Implemented intelligent sports analytics platform with CrewAI multi-agent system.

Key Features:
- Three specialized AI agents: Data Analyst, Performance Evaluator, Strategy Advisor
- Multi-agent workflows for player, team, and match analysis
- CrewAI orchestration with sequential and collaborative processing
- Comprehensive documentation (CREWAI_UPGRADE.md)
- Complete configuration system with environment variables
- Utility functions for data processing and validation
- Example tests and interactive application

Technical Specifications:
- crewai>=0.86.0
- langchain-openai>=0.3.0
- Python 3.8+
- 18 files, 2500+ lines of code

Generated with Claude Code

Co-Authored-By: Claude Sonnet 4.5 <noreply@anthropic.com>"
EOF
echo ""

# Create and switch to crewai-upgrade branch
echo "Step 5: Create and switch to crewai-upgrade branch"
echo "git checkout -b crewai-upgrade"
echo ""

# Add remote (you need to replace with actual repository URL)
echo "Step 6: Add remote repository"
echo "git remote add origin <YOUR-REPOSITORY-URL>"
echo "# Replace <YOUR-REPOSITORY-URL> with actual repository URL"
echo ""

# Push to remote
echo "Step 7: Push to remote repository"
echo "git push -u origin crewai-upgrade"
echo ""

echo "=============================================="
echo "Note: Make sure to replace <YOUR-REPOSITORY-URL> with your actual repository URL"
echo "Example: git remote add origin https://github.com/yourusername/mclach-agent60.git"
