# Code Review Assistant - CrewAI Edition

## Overview
Multi-agent system for comprehensive code review including quality analysis, security assessment, performance optimization, and style checking.

## Features
- Code quality and maintainability analysis
- Security vulnerability detection
- Performance bottleneck identification
- Style and convention enforcement

## Agents
1. **Code Analyzer** - Quality and best practices review
2. **Security Reviewer** - Vulnerability assessment
3. **Performance Reviewer** - Optimization opportunities
4. **Style Checker** - Convention and formatting compliance

## Setup
```bash
pip install -r requirements.txt
cp .env.example .env
```

## Usage
```python
from main import review_code
result = review_code("app.py", "Python", "PEP 8")
```

**Version:** 1.0.0 | **CrewAI:** 0.86.0+
