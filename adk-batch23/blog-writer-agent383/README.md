# Blog Writer CrewAI Agent

Converted from Google ADK Blog Writer to CrewAI implementation with OpenAI.

## Overview

An automated blog writing system powered by CrewAI with three specialized agents:

### Agents

1. **Technical Content Strategist (Researcher)**
   - Role: Research topics and create comprehensive outlines
   - Converted from: ADK `robust_blog_planner`
   - Tools: Web search for gathering information
   - Output: Detailed blog post outline in Markdown

2. **Expert Technical Writer**
   - Role: Write high-quality technical blog posts
   - Converted from: ADK `robust_blog_writer`
   - Tools: Web search for examples and context
   - Output: Complete blog post draft

3. **Professional Technical Editor**
   - Role: Polish and refine blog posts
   - Converted from: ADK `blog_editor`
   - Tools: None (focuses on editing)
   - Output: Publication-ready blog post

## Features

- **Multi-agent workflow**: Sequential process from research to final polish
- **Web search integration**: Agents can search for current information
- **Codebase analysis**: Optional analysis of code projects for technical posts
- **Markdown output**: Clean, formatted blog posts ready for publication
- **Interactive CLI**: User-friendly interface for creating blog posts

## Installation

```bash
# Install dependencies
pip install -r requirements.txt

# Set up environment variables
cp .env.example .env
# Edit .env and add your API keys
```

## Configuration

Required API keys:
- `OPENAI_API_KEY`: OpenAI API key for GPT-4
- `SERPER_API_KEY`: Serper API key for web search

## Usage

### Command Line

```bash
python main.py
```

Follow the prompts to:
1. Enter your blog post topic
2. Optionally provide a codebase path to analyze
3. Review the generated blog post
4. Save to file

### Python API

```python
from main import create_blog_post, save_blog_post

# Create blog post
result = create_blog_post(
    topic="Introduction to Machine Learning",
    codebase_path="/path/to/code"  # Optional
)

# Save to file
save_blog_post(result["final_post"], "my-blog-post.md")
```

## Workflow

1. **Research Phase**: Strategist researches topic and creates outline
2. **Writing Phase**: Writer creates comprehensive blog post from outline
3. **Editing Phase**: Editor polishes and refines the final content

## Migration from ADK

### Key Changes

| ADK Component | CrewAI Equivalent |
|---------------|-------------------|
| `robust_blog_planner` | Technical Content Strategist agent |
| `robust_blog_writer` | Expert Technical Writer agent |
| `blog_editor` | Professional Technical Editor agent |
| `social_media_writer` | Not implemented (can be added) |
| Gemini model | OpenAI GPT-4 |
| `google_search` tool | SerperDevTool |
| `analyze_codebase` tool | Simple file analysis function |
| `save_blog_post_to_file` tool | `save_blog_post()` function |

### Architecture Differences

- **ADK**: Uses LoopAgent with validation checkers
- **CrewAI**: Sequential process with task context

## Example Output

The system produces blog posts with:
- Engaging title and introduction
- Well-structured body with code examples
- Technical depth appropriate for audience
- Clear conclusion and call to action
- Proper Markdown formatting

## Original ADK Agent

Based on: [blog-writer](https://github.com/colygon/adk-samples/tree/main/python/agents/blog-writer)

## License

Apache License 2.0
