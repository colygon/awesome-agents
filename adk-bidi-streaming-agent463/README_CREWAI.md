# Bidirectional Streaming Agent - CrewAI Edition

## Overview
Multi-agent system for managing bidirectional streaming connections with real-time message processing and state coordination.

## Features
- WebSocket/gRPC stream management
- Real-time message processing
- State synchronization
- Flow control and backpressure
- Automatic reconnection

## Agents
1. **Stream Manager** - Connection lifecycle and flow control
2. **Message Processor** - Real-time message validation and transformation
3. **State Coordinator** - State management and synchronization

## Setup
```bash
pip install -r requirements.txt
cp .env.example .env
```

## Usage
```python
from main import setup_bidi_streaming
result = setup_bidi_streaming(config, schema)
```

**Version:** 1.0.0 | **CrewAI:** 0.86.0+
