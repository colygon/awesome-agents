# Marketing Agency CrewAI Agent

Converted from Google ADK Marketing Agency to CrewAI implementation with OpenAI.

## Overview

A comprehensive marketing campaign generator powered by CrewAI with three specialized agents that streamline product and website launches.

### Agents

1. **Marketing Analytics Specialist**
   - Role: Analyze market data and recommend domains
   - Tools: Web search for market research
   - Output: Market analysis with domain recommendations

2. **Marketing Strategy Director**
   - Role: Develop comprehensive marketing strategies
   - Tools: Web search for strategy insights
   - Output: Complete go-to-market strategy

3. **Creative Content Director**
   - Role: Generate marketing content and brand assets
   - Tools: Web search for creative inspiration
   - Output: Content package with messaging and brand guidelines

## Features

- **Domain recommendations**: 5-10 suggested domain names with availability analysis
- **Marketing strategy**: Go-to-market plan with timeline and KPIs
- **Content generation**: Website copy, email templates, social media posts
- **Brand guidelines**: Color palettes, typography, visual direction
- **Budget-aware**: Tailored recommendations based on budget constraints

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
1. Enter product/website name
2. Provide brief description
3. Define target audience
4. Select budget level (low/medium/high)
5. Review the campaign plan
6. Save to file

### Python API

```python
from main import create_launch_campaign, save_campaign

# Create campaign
result = create_launch_campaign(
    product_name="InnovateApp",
    product_description="A productivity app for remote teams",
    target_audience="Small to medium-sized businesses",
    budget="medium"
)

# Save campaign
save_campaign(result["content_package"], "innovateapp-campaign.md")
```

## Workflow

1. **Analysis Phase**: Analyst researches market and recommends domains
2. **Strategy Phase**: Strategist develops go-to-market plan
3. **Content Phase**: Content creator generates marketing materials

## Campaign Components

Generated campaigns include:

### Market Analysis
- Competitor landscape
- Target audience insights
- Domain name suggestions (5-10 options)
- Market positioning opportunities
- Key differentiators

### Marketing Strategy
- Go-to-market strategy
- Channel selection (social, email, content, paid ads)
- Campaign timeline and milestones
- Key Performance Indicators (KPIs)
- Budget allocation
- Launch phases (pre-launch, launch, post-launch)

### Content Package
- Brand messaging framework
  - Tagline options (5-7 variations)
  - Value proposition
  - Key messages
- Website content plan
  - Homepage copy outline
  - Key page structures
  - Call-to-action recommendations
- Marketing copy
  - Email campaign templates
  - Social media post ideas (10+)
  - Ad copy variations
- Brand asset recommendations
  - Color palette
  - Typography
  - Visual style direction
  - Logo concepts

## Migration from ADK

### Architecture

This agent system streamlines new website and product launches by:
- Identifying optimal DNS domains
- Generating website content
- Developing marketing strategies
- Designing brand assets

### Key Changes

| ADK Component | CrewAI Equivalent |
|---------------|-------------------|
| Gemini model | OpenAI GPT-4 |
| `google_search` tool | SerperDevTool |
| ADK multi-agent workflow | CrewAI sequential process |

### Agent Design

- **Analyst**: Market research and domain recommendations
- **Strategist**: Go-to-market strategy and planning
- **Content Creator**: Content generation and brand assets

## Example Scenarios

### SaaS Product Launch
```
Product: CloudSync Pro
Description: Enterprise file synchronization platform
Audience: IT departments in large corporations
Budget: High
```

### E-commerce Website
```
Product: EcoGoods Store
Description: Sustainable home products marketplace
Audience: Environmentally conscious consumers
Budget: Medium
```

### Mobile App Launch
```
Product: FitTrack
Description: AI-powered fitness tracking app
Audience: Health-conscious millennials
Budget: Low
```

## Use Cases

- New product launches
- Website redesigns and launches
- Rebranding campaigns
- Market expansion initiatives
- Startup go-to-market strategies

## Original ADK Agent

Based on: Marketing Agency from [adk-samples](https://github.com/colygon/adk-samples/tree/main/python/agents/marketing-agency)

## License

Apache License 2.0
