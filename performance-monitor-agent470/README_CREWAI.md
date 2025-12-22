# Performance Monitor - CrewAI Edition

## Overview
Multi-agent system for comprehensive performance monitoring including metrics collection, bottleneck analysis, trend forecasting, and intelligent alerting.

## Features
- Real-time metrics collection
- Bottleneck identification
- Capacity planning and forecasting
- Intelligent anomaly detection and alerts

## Agents
1. **Metrics Collector** - Gathers performance data
2. **Bottleneck Analyzer** - Identifies performance issues
3. **Trend Forecaster** - Predicts capacity needs
4. **Alert Manager** - Configures intelligent alerts

## Setup
```bash
pip install -r requirements.txt
cp .env.example .env
```

## Usage
```python
from main import setup_performance_monitoring
result = setup_performance_monitoring(system_config, alert_config)
```

**Version:** 1.0.0 | **CrewAI:** 0.86.0+
