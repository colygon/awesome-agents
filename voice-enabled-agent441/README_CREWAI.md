# Voice-Enabled Agent - CrewAI Implementation

## Overview
A multi-agent system for voice interaction, speech recognition, natural language understanding, and voice synthesis.

## Agents

### 1. Speech Recognition Specialist
- Converts voice input to text transcription
- Handles audio quality assessment
- Supports multiple accents and dialects

### 2. Natural Language Understanding Specialist
- Analyzes transcribed text for intent
- Extracts entities and parameters
- Classifies command types

### 3. Voice Synthesis Specialist
- Generates natural-sounding speech responses
- Applies appropriate prosody and emotion
- Creates context-aware voice output

### 4. Conversation Manager
- Manages multi-turn conversations
- Maintains conversation context
- Orchestrates dialogue flow

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Configure environment:
```bash
cp .env.example .env
# Edit .env with your API keys
```

3. Run the system:
```bash
python main.py
```

## Features
- Speech-to-text transcription
- Natural language understanding
- Intent recognition and extraction
- Text-to-speech synthesis
- Conversation management
- Multi-turn dialogue support

## Integration Points
- Google Speech-to-Text
- Azure Speech Services
- OpenAI Whisper
- ElevenLabs TTS
- Amazon Polly

## Use Cases
- Voice assistants
- Voice command systems
- Interactive voice response (IVR)
- Voice-controlled applications
- Accessibility features
