# Documentation Generator - CrewAI Edition

## Overview
Multi-agent system for generating comprehensive technical documentation including code docs, API references, tutorials, and README files.

## Features
- Automated docstring generation
- API documentation (OpenAPI/Swagger)
- Step-by-step tutorials
- Professional README files

## Agents
1. **Code Documenter** - Generates code-level documentation
2. **API Documenter** - Creates API reference docs
3. **Tutorial Writer** - Writes getting started guides
4. **README Generator** - Creates comprehensive README files

## Setup
```bash
pip install -r requirements.txt
cp .env.example .env
```

## Usage
```python
from main import generate_documentation
result = generate_documentation(source_files, project_info, api_spec)
```

**Version:** 1.0.0 | **CrewAI:** 0.86.0+
