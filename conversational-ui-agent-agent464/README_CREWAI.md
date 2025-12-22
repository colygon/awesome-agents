# Conversational UI Agent - CrewAI Edition

## Overview
Multi-agent system for building intelligent conversational interfaces with intent classification, dialog management, and personality design.

## Features
- Intent classification and entity extraction
- Context-aware dialog management
- Natural language response generation
- Consistent personality design

## Agents
1. **Intent Classifier** - Recognizes user intents and extracts entities
2. **Dialog Manager** - Manages conversation flow and state
3. **Response Generator** - Creates natural, helpful responses
4. **Personality Designer** - Designs conversational personality

## Setup
```bash
pip install -r requirements.txt
cp .env.example .env
```

## Usage
```python
from main import create_conversational_ui
result = create_conversational_ui(user_input, brand_info)
```

**Version:** 1.0.0 | **CrewAI:** 0.86.0+
