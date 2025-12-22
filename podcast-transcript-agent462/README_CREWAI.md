# Podcast Transcript Analyzer - CrewAI Edition

## Overview

Multi-agent system for processing, analyzing, and optimizing podcast transcripts. Generates complete episode packages including summaries, timestamps, quotes, and SEO-optimized metadata.

## Features

- **Transcript Cleaning** - Remove filler words, fix punctuation, format speakers
- **Content Analysis** - Identify themes, topics, and key insights
- **Multi-Level Summaries** - One-liner, brief, standard, and detailed summaries
- **Chapter Markers** - Timestamps and navigation aids
- **Quote Extraction** - Memorable soundbites for promotion
- **SEO Optimization** - Search-optimized titles, descriptions, and show notes

## Agents

1. **Transcript Processor** - Cleans and formats raw transcripts
2. **Content Analyzer** - Identifies themes and insights
3. **Summarizer** - Creates multi-level summaries
4. **Timestamp Generator** - Creates chapter markers
5. **Quote Extractor** - Finds shareable soundbites
6. **SEO Optimizer** - Optimizes for search and discovery

## Setup

```bash
cd podcast-transcript-agent462
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
# Add your OpenAI API key to .env
```

## Usage

```python
from main import analyze_podcast_transcript

result = analyze_podcast_transcript(
    transcript_text=your_transcript,
    episode_info={'title': 'Episode Title', 'guest': 'Guest Name'},
    speakers=['Host', 'Guest'],
    target_keywords=['keyword1', 'keyword2']
)
```

## Output Package

- Cleaned transcript
- Content analysis with themes
- Four-tier summaries
- Chapter markers with timestamps
- Top 10 memorable quotes
- SEO-optimized metadata
- Platform-specific content

---

**Version:** 1.0.0 | **CrewAI:** 0.86.0+ | **Python:** 3.10+
