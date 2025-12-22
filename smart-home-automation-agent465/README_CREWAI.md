# Smart Home Automation - CrewAI Edition

## Overview
Multi-agent system for orchestrating smart home devices, creating automation routines, optimizing energy usage, and monitoring security.

## Features
- Multi-protocol device coordination
- Intelligent automation design
- Energy consumption optimization
- Security monitoring and alerts

## Agents
1. **Device Coordinator** - Manages device connections and state
2. **Automation Designer** - Creates intelligent routines
3. **Energy Optimizer** - Optimizes power consumption
4. **Security Monitor** - Monitors and responds to security events

## Setup
```bash
pip install -r requirements.txt
cp .env.example .env
```

## Usage
```python
from main import setup_smart_home
result = setup_smart_home(devices, preferences, security_config)
```

**Version:** 1.0.0 | **CrewAI:** 0.86.0+
