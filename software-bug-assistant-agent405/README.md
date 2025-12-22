# Software Bug Assistant Agent - CrewAI Implementation

Upgraded from Google ADK to CrewAI framework.

## Overview

AI-powered debugging assistant that helps developers identify, analyze, and fix software bugs through automated code analysis, solution research, and fix recommendations.

## Architecture

### CrewAI Agents

1. **Bug Analyzer**
   - Role: Software Debugging Specialist
   - Analyzes bug reports and error messages
   - Reproduces and categorizes bugs
   - Identifies root causes and affected components

2. **Solution Finder**
   - Role: Technical Solutions Researcher
   - Searches knowledge bases and documentation
   - Finds similar issues and solutions
   - Identifies relevant code patterns and fixes

3. **Fix Recommender**
   - Role: Code Fix Architect
   - Recommends specific code changes
   - Provides implementation guidance
   - Creates test cases for verification

## Original ADK Features

- Automated bug triage and categorization
- Stack trace analysis
- Code pattern matching
- Solution knowledge base search
- Fix suggestion generation
- Integration with issue tracking systems
- Regression detection

## CrewAI Implementation

### Tools Implemented

- **Bug Analysis Tools**: Parse error messages and stack traces
- **Code Search Tools**: Search codebase for related issues
- **Documentation Tools**: Search internal and external docs
- **Solution Database Tools**: Query known bug fixes
- **Code Generation Tools**: Generate fix suggestions
- **Testing Tools**: Create test cases
- **Integration Tools**: Update issue trackers

### Workflow

1. Bug Analyzer categorizes and analyzes the bug report
2. Solution Finder researches solutions and similar issues
3. Fix Recommender provides specific code fixes and testing guidance

## Setup

```bash
cd software-bug-assistant-agent405
pip install -r requirements.txt
cp .env.example .env
# Edit .env with your API keys
python main.py
```

## Usage

```python
from agents import run_bug_analysis

result = run_bug_analysis(
    bug_report="NullPointerException in UserService.updateProfile()",
    stack_trace="...",
    code_context="..."
)
print(result)
```

## Migration Notes

- ADK debugging workflow → CrewAI multi-agent analysis
- Enhanced code context understanding
- Integration with code search and documentation tools
- Automated test case generation
