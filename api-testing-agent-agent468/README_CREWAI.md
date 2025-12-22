# API Testing Agent - CrewAI Edition

## Overview
Multi-agent system for comprehensive API testing including functional, performance, and integration testing.

## Features
- Test suite design
- Endpoint validation
- Performance and load testing
- Integration workflow testing

## Agents
1. **Test Designer** - Creates comprehensive test suites
2. **Endpoint Validator** - Validates API contracts
3. **Performance Tester** - Tests load and performance
4. **Integration Tester** - Tests end-to-end workflows

## Setup
```bash
pip install -r requirements.txt
cp .env.example .env
```

## Usage
```python
from main import test_api
result = test_api(api_spec, endpoints, load_config, workflow)
```

**Version:** 1.0.0 | **CrewAI:** 0.86.0+
