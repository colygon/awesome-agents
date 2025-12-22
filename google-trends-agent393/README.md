# Google Trends Agent - CrewAI Implementation

Upgraded from Google ADK to CrewAI framework.

## Overview

AI-powered trend analysis agent that collects Google Trends data, analyzes patterns, and generates comprehensive reports for business intelligence and market research.

## Architecture

### CrewAI Agents

1. **Data Collector**
   - Role: Trends Data Specialist
   - Collects trending topics and search data
   - Gathers historical trend information
   - Aggregates data from multiple sources

2. **Trend Analyzer**
   - Role: Market Intelligence Analyst
   - Analyzes trend patterns and trajectories
   - Identifies emerging trends vs declining topics
   - Performs comparative analysis across regions/time periods

3. **Report Writer**
   - Role: Business Intelligence Reporter
   - Synthesizes findings into actionable insights
   - Creates visualizations and trend summaries
   - Generates executive summaries and detailed reports

## Original ADK Features

- Real-time Google Trends data collection
- Multi-region trend comparison
- Historical trend analysis
- Topic clustering and categorization
- Sentiment analysis of trending topics
- Automated report generation

## CrewAI Implementation

### Tools Implemented

- **Trends API Tools**: Access Google Trends data
- **Data Analysis Tools**: Statistical analysis and pattern detection
- **Regional Comparison Tools**: Multi-location trend analysis
- **Report Generation Tools**: Create formatted reports
- **Visualization Tools**: Generate charts and graphs
- **Export Tools**: Save reports in multiple formats

### Workflow

1. Data Collector gathers trend data based on query parameters
2. Trend Analyzer performs pattern analysis and identifies insights
3. Report Writer compiles findings into comprehensive reports

## Setup

```bash
cd google-trends-agent393
pip install -r requirements.txt
cp .env.example .env
# Edit .env with your API keys
python main.py
```

## Usage

```python
from agents import run_trends_analysis

result = run_trends_analysis(
    keywords=["AI", "machine learning", "ChatGPT"],
    regions=["US", "GB", "JP"],
    timeframe="today 12-m"
)
print(result)
```

## Migration Notes

- ADK action-based data collection → CrewAI task-based workflow
- Integrated pytrends library for Google Trends API access
- Multi-agent architecture for scalable analysis
- Enhanced error handling and rate limiting
