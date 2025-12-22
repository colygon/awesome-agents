# Financial Advisor CrewAI Agent

Converted from Google ADK Financial Advisor to CrewAI implementation with OpenAI.

## Overview

An educational investment guidance system powered by CrewAI with three specialized agents that provide comprehensive financial analysis and recommendations.

### Agents

1. **Financial Data Analyst**
   - Role: Analyze financial data, market trends, and investment performance
   - Tools: Web search for current market data
   - Output: Comprehensive data analysis with market trends

2. **Investment Risk Assessor**
   - Role: Evaluate investment risks and provide risk management strategies
   - Tools: Web search for risk factors and market volatility
   - Output: Detailed risk assessment with ratings and mitigation strategies

3. **Senior Financial Advisor**
   - Role: Provide educational investment guidance
   - Tools: Web search for investment strategies
   - Output: Complete advisory report with recommendations

## Features

- **Multi-agent workflow**: Sequential process from analysis to recommendations
- **Risk assessment**: Comprehensive evaluation of investment risks
- **Market analysis**: Current market conditions and trends
- **Educational content**: Investment strategies and portfolio guidance
- **Professional reports**: Formatted advisory reports with disclaimers

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
1. Enter investment type (stocks, bonds, ETFs, etc.)
2. Enter investment amount
3. Select time horizon (short/medium/long term)
4. Select risk tolerance (conservative/moderate/aggressive)
5. Review the advisory report
6. Save to file

### Python API

```python
from main import analyze_investment, save_report

# Analyze investment
result = analyze_investment(
    investment_type="diversified ETF portfolio",
    amount=50000.0,
    time_horizon="long",
    risk_tolerance="moderate"
)

# Save report
save_report(result["advisory_report"], "investment-analysis.md")
```

## Workflow

1. **Data Analysis Phase**: Analyst researches market conditions and trends
2. **Risk Assessment Phase**: Risk assessor evaluates investment risks
3. **Advisory Phase**: Advisor synthesizes information into recommendations

## Report Components

Generated reports include:
1. Executive Summary
2. Market Data Analysis
3. Risk Assessment with Ratings
4. Investment Strategy Recommendations
5. Portfolio Diversification Suggestions
6. Expected Returns Scenarios (best/expected/worst case)
7. Action Plan and Next Steps
8. Important Disclaimers

## Migration from ADK

### Architecture

This agent system provides educational content to assist human financial advisors, following the ADK pattern of:
- Risk analysis
- Strategy generation
- Summarization
- Report generation

### Key Changes

| ADK Component | CrewAI Equivalent |
|---------------|-------------------|
| Gemini model | OpenAI GPT-4 |
| `google_search` tool | SerperDevTool |
| ADK multi-agent workflow | CrewAI sequential process |

### Agent Design

- **Data Analyst**: Gathers and analyzes market data
- **Risk Assessor**: Evaluates risks and provides mitigation strategies
- **Financial Advisor**: Synthesizes information into actionable guidance

## Important Disclaimers

This system provides **educational content only** and does not constitute personalized financial advice. Users should:
- Consult with qualified financial advisors
- Conduct their own due diligence
- Consider their personal financial situation
- Understand investment risks

## Example Scenarios

### Conservative Investor
```
Investment: Government bonds
Amount: $25,000
Time Horizon: Short term
Risk Tolerance: Conservative
```

### Moderate Investor
```
Investment: Diversified ETF portfolio
Amount: $50,000
Time Horizon: Medium term
Risk Tolerance: Moderate
```

### Aggressive Investor
```
Investment: Growth stocks
Amount: $100,000
Time Horizon: Long term
Risk Tolerance: Aggressive
```

## Original ADK Agent

Based on: Financial Advisor from [adk-samples](https://github.com/colygon/adk-samples/tree/main/python/agents/financial-advisor)

## License

Apache License 2.0
