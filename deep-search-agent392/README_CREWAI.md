# Deep Search Agent - CrewAI Implementation

A comprehensive deep search system powered by CrewAI that performs multi-layered research, fact-checking, and synthesis to deliver thorough, verified information on any topic.

## Overview

This CrewAI implementation provides deep, multi-source research capabilities with fact verification and comprehensive reporting. The system uses a team of specialized agents to search, analyze, verify, and synthesize information.

## Agents

1. **Search Strategy Expert**: Designs comprehensive search strategies and query formulations
2. **Information Analyst**: Executes searches, collects data, and performs initial analysis
3. **Fact Verification Specialist**: Cross-references claims and verifies information accuracy
4. **Research Synthesis Expert**: Compiles findings into comprehensive, well-structured reports

## Features

- Multi-angle search strategy development
- Comprehensive web search across multiple sources
- Information extraction and pattern recognition
- Fact verification and cross-referencing
- Source credibility assessment
- Comprehensive report generation with citations
- Organized findings by theme and relevance

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Configure environment variables:
```bash
cp .env.example .env
# Edit .env with your API keys
```

3. Required API keys:
- OpenAI API key (or Google Gemini)
- Google Custom Search API key
- Google Search Engine ID

## Usage

Run the deep search agent:

```bash
python main.py
```

Or use programmatically:

```python
from main import run_deep_search

result = run_deep_search("Your research query here")
print(result)
```

## Workflow

1. **Strategy Planning**: Develops comprehensive search strategy
2. **Information Gathering**: Executes searches across multiple sources
3. **Analysis**: Extracts insights and organizes findings
4. **Fact Verification**: Verifies key claims through cross-referencing
5. **Synthesis**: Compiles comprehensive research report

## Output

The system produces a comprehensive research report including:
- Executive summary
- Main findings organized by theme
- Key facts and data points
- Multiple perspectives
- Verification status of claims
- Source credibility assessment
- Information gaps and limitations
- Conclusions and recommendations

## Customization

Modify the following files to customize behavior:
- `agents.py`: Adjust agent roles and capabilities
- `tasks.py`: Modify research workflow and output requirements
- `tools.py`: Add custom search or analysis tools
- `main.py`: Change the orchestration logic

## Example Use Cases

- Academic research
- Market research
- Competitive intelligence
- Fact-checking articles or claims
- Due diligence research
- Literature reviews
- Investigative journalism

## Notes

- Requires valid API keys for full functionality
- Search depth can be adjusted in tasks.py
- Fact verification requires multiple reliable sources
- Report format can be customized in synthesis task
