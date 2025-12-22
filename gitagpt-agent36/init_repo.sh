#!/bin/bash

# Initialize git repository and push to crewai-upgrade branch
# Run this script to complete the setup

cd /Users/colinlowenberg/crew/gitagpt-agent36

# Initialize git repository
git init

# Add all files
git add .

# Create initial commit
git commit -m "Initial commit: Gita GPT Agent 36 CrewAI upgrade

- Added 3 specialized agents: Text Analyst, Context Provider, Practical Guide
- Implemented CrewAI orchestration with sequential processing
- Added sample Bhagavad Gita verses database
- Created comprehensive documentation in CREWAI_UPGRADE.md
- Dependencies: crewai>=0.86.0, langchain-openai>=0.3.0

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude Sonnet 4.5 <noreply@anthropic.com>"

# Create and checkout crewai-upgrade branch
git checkout -b crewai-upgrade

echo "Repository initialized successfully!"
echo "To push to remote, run:"
echo "  git remote add origin <your-remote-url>"
echo "  git push -u origin crewai-upgrade"
