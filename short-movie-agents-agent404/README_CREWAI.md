# Short Movie Agents - CrewAI Edition

## Overview

Complete short film development system with AI agents for story, screenplay, characters, storyboards, and director's vision.

## Agents

1. **Story Developer** - Creates compelling film concepts
2. **Character Developer** - Develops rich, believable characters
3. **Screenwriter** - Writes properly formatted screenplays
4. **Storyboard Artist** - Visualizes scenes with detailed shot descriptions
5. **Director** - Provides creative vision and directorial guidance

## Installation

```bash
cd short-movie-agents-agent404
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
# Add your OPENAI_API_KEY to .env
```

## Usage

Interactive:
```bash
python main.py
```

Command line:
```bash
python main.py "A lonely astronaut discovers an alien artifact" sci-fi 12
```

## Output

Complete film package including:
- Story concept and structure
- Character profiles
- Full screenplay (properly formatted)
- Visual storyboard descriptions
- Director's vision statement

---

**Migration Date:** December 2025
**CrewAI Version:** 0.86.0+
