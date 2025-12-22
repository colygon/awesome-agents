# Software Bug Assistant - CrewAI Edition

## Overview

AI-powered bug detection and resolution system with specialized agents for analysis, solution design, testing, and documentation.

## Agents

1. **Bug Detective** - Identifies and categorizes bugs
2. **Code Analyzer** - Analyzes root causes
3. **Solution Architect** - Designs fixes
4. **Test Engineer** - Creates test cases
5. **Documentation Specialist** - Documents resolutions

## Installation

```bash
cd software-bug-assistant-agent405
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
# Add OPENAI_API_KEY
```

## Usage

```bash
python main.py "NullPointerException in user authentication"
```

---

**Migration Date:** December 2025
