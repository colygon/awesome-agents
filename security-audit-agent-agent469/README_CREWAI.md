# Security Audit Agent - CrewAI Edition

## Overview
Multi-agent system for comprehensive security auditing including vulnerability scanning, dependency auditing, configuration review, and compliance checking.

## Features
- OWASP Top 10 vulnerability scanning
- Dependency vulnerability assessment
- Security configuration review
- Compliance verification (GDPR, SOC 2, HIPAA)

## Agents
1. **Vulnerability Scanner** - Identifies security vulnerabilities
2. **Dependency Auditor** - Audits package dependencies
3. **Configuration Reviewer** - Reviews security settings
4. **Compliance Checker** - Verifies regulatory compliance

## Setup
```bash
pip install -r requirements.txt
cp .env.example .env
```

## Usage
```python
from main import perform_security_audit
result = perform_security_audit(target, deps, configs, standards)
```

**Version:** 1.0.0 | **CrewAI:** 0.86.0+
