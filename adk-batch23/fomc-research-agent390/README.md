# FOMC Research Agent - CrewAI Implementation

Federal Open Market Committee meeting analysis and economic research using CrewAI multi-agent system.

## Overview

An intelligent FOMC (Federal Open Market Committee) analysis platform powered by CrewAI with five specialized agents that collaborate to provide comprehensive monetary policy research, economic analysis, and market impact assessments.

### Agents

1. **FOMC Document Research Analyst**
   - Role: Research and analyze FOMC meeting materials
   - Capabilities: Statement analysis, minutes review, economic projections interpretation
   - Tools: Web search, website scraping
   - Output: Comprehensive FOMC document summary

2. **Economic Data Analyst**
   - Role: Analyze economic indicators
   - Capabilities: Inflation analysis, employment data, GDP assessment, financial conditions
   - Tools: Web search for economic data
   - Output: Economic context analysis

3. **Monetary Policy Interpretation Specialist**
   - Role: Interpret Fed policy stance and forward guidance
   - Capabilities: Policy position assessment, forward guidance interpretation, risk analysis
   - Tools: None (focuses on interpretation)
   - Output: Detailed policy interpretation

4. **Financial Market Impact Analyst**
   - Role: Assess market implications of FOMC decisions
   - Capabilities: Market reaction analysis, asset class implications, investment strategy
   - Tools: Web search for market data
   - Output: Market impact assessment

5. **Economic Research Report Writer**
   - Role: Synthesize analysis into research reports
   - Capabilities: Report structuring, synthesis, actionable insights
   - Tools: None (focuses on writing)
   - Output: Comprehensive research report

## Features

- **Comprehensive FOMC analysis**: Statements, minutes, projections, press conferences
- **Economic context**: Inflation, employment, GDP, financial conditions
- **Policy interpretation**: Stance, forward guidance, dual mandate, risks
- **Market impact**: Equities, bonds, currencies, investment implications
- **Professional reports**: Structured research reports in Markdown
- **Flexible focus**: Comprehensive, policy, markets, or economic outlook
- **Current data**: Real-time web search for latest information

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

Choose analysis options:
1. Select meeting (latest or specific date)
2. Choose analysis focus
3. Review comprehensive research report
4. Save to file

### Python API

```python
from main import analyze_fomc_meeting, save_report

# Analyze latest FOMC meeting
result = analyze_fomc_meeting(
    meeting_date="latest",
    analysis_focus="comprehensive"
)

# Analyze specific meeting
result = analyze_fomc_meeting(
    meeting_date="2024-12-18",
    analysis_focus="policy"
)

# Access components
print(result["fomc_research"])
print(result["economic_context"])
print(result["policy_interpretation"])
print(result["market_impact"])

# Save full report
save_report(result["full_report"], "fomc-analysis-dec2024.md")
```

## Analysis Workflow

### Phase 1: FOMC Document Research
**Agent**: FOMC Document Research Analyst

Researches and analyzes:
- **FOMC Statement**: Policy decision, economic assessment, forward guidance
- **Meeting Minutes**: Discussion points, projections, debates, risks
- **Economic Projections**: GDP, unemployment, inflation, interest rate dot plot
- **Press Conference**: Chair's key messages, Q&A highlights

### Phase 2: Economic Context Analysis
**Agent**: Economic Data Analyst

Evaluates key indicators:
- **Inflation**: CPI, Core CPI, PCE, wage growth
- **Employment**: Unemployment rate, job creation, participation, openings
- **Growth**: GDP, consumer spending, investment, trade
- **Financial Conditions**: Credit markets, banking, volatility, stress

### Phase 3: Policy Interpretation
**Agent**: Monetary Policy Interpretation Specialist

Interprets:
- **Policy Stance**: Accommodative/neutral/restrictive, hawkish/dovish
- **Forward Guidance**: Rate trajectory, conditions, timeline
- **Dual Mandate**: Price stability and maximum employment progress
- **Risks**: Inflation, growth, financial stability, external factors

### Phase 4: Market Impact Assessment
**Agent**: Financial Market Impact Analyst

Assesses:
- **Market Reaction**: Equities, bonds, dollar, commodities
- **Expectations**: Pre-meeting pricing, surprises, futures
- **Implications**: Sector impacts, duration risk, credit spreads
- **Investment Strategy**: Positioning, opportunities, risks

### Phase 5: Research Report Generation
**Agent**: Economic Research Report Writer

Creates structured report:
- Executive summary with key takeaways
- Meeting overview and policy decision
- Economic assessment and projections
- Monetary policy analysis and forward guidance
- Market implications and investment strategy
- Outlook and recommendations
- Appendix with data and context

## Analysis Focus Options

### Comprehensive (Default)
Complete analysis of all aspects:
- FOMC documents in depth
- Full economic context
- Detailed policy interpretation
- Comprehensive market analysis
- Balanced recommendations

### Policy Focus
Deep dive into monetary policy:
- Policy stance and changes
- Forward guidance details
- Historical policy context
- Policy transmission mechanisms
- Central bank communication

### Markets Focus
Emphasis on market implications:
- Detailed market reaction analysis
- Asset class recommendations
- Trading strategies
- Risk management
- Portfolio positioning

### Economic Outlook Focus
Economic trends and forecasts:
- Economic indicator deep dive
- Growth and inflation outlook
- Labor market analysis
- Recession/expansion signals
- Long-term trends

## FOMC Meeting Documents

### Statement
Published after each meeting (8 times/year):
- Interest rate decision
- Economic assessment
- Forward guidance
- Vote count and dissents

### Minutes
Published 3 weeks after meeting:
- Detailed discussion
- Staff economic outlook
- Policy deliberations
- Risk assessments
- Individual views

### Economic Projections
Published quarterly (4 times/year):
- GDP growth forecasts
- Unemployment projections
- Inflation expectations
- Fed funds rate dot plot
- Longer-run estimates

### Press Conference
After every meeting (8 times/year):
- Chair's opening statement
- Q&A with reporters
- Policy clarifications
- Additional context

## Key Economic Indicators

### Inflation Metrics
- **CPI**: Consumer Price Index (headline and core)
- **PCE**: Personal Consumption Expenditures (Fed's preferred)
- **PPI**: Producer Price Index
- **Wage Growth**: Average hourly earnings
- **Inflation Expectations**: Survey and market-based

### Employment Data
- **Unemployment Rate**: U-3 official rate
- **Payrolls**: Monthly job creation
- **Participation Rate**: Labor force percentage
- **JOLTS**: Job openings and quits
- **Claims**: Initial jobless claims

### Growth Indicators
- **GDP**: Quarterly growth rate
- **Retail Sales**: Consumer spending
- **Industrial Production**: Manufacturing output
- **Housing**: Starts, sales, prices
- **ISM**: Manufacturing and services PMIs

### Financial Conditions
- **Yield Curve**: Treasury yields across maturities
- **Credit Spreads**: Corporate bond spreads
- **Equity Markets**: S&P 500, volatility (VIX)
- **Dollar Index**: DXY currency strength
- **Financial Stress**: Fed stress index

## Fed's Dual Mandate

The Federal Reserve has two main objectives:

### 1. Price Stability
- Target: 2% inflation (PCE measure)
- Current focus: Bringing inflation down from elevated levels
- Tools: Interest rate adjustments, balance sheet policy

### 2. Maximum Employment
- Target: Full employment (sustainable maximum)
- Assessment: Unemployment rate, participation, wage growth
- Balance: Avoiding overheating while supporting job creation

## Policy Tools

### Interest Rates
- **Fed Funds Rate**: Overnight lending rate
- **Discount Rate**: Direct Fed lending rate
- **IORB**: Interest on reserve balances

### Balance Sheet
- **QE**: Quantitative easing (asset purchases)
- **QT**: Quantitative tightening (runoff)
- **Composition**: Treasuries, MBS holdings

### Forward Guidance
- Communication about future policy path
- Conditional vs calendar-based
- Dots plot for rate expectations

## Market Implications

### Asset Classes

#### Equities
- Interest rates affect discount rates
- Sector rotation (growth vs value)
- Earnings impact through economy

#### Fixed Income
- Rate changes affect bond prices
- Yield curve shape and inversion
- Credit spreads and risk appetite

#### Currencies
- Dollar strength from rate differentials
- Carry trade implications
- Emerging market spillovers

#### Commodities
- Gold as inflation hedge
- Oil sensitive to growth outlook
- Real assets in inflationary environment

## Migration from ADK

### Key Changes

| ADK Component | CrewAI Equivalent |
|---------------|-------------------|
| FOMC scraper | FOMC Document Research Analyst |
| Economic analyzer | Economic Data Analyst |
| Policy interpreter | Monetary Policy Interpretation Specialist |
| Market assessor | Financial Market Impact Analyst |
| Report generator | Economic Research Report Writer |
| Gemini model | OpenAI GPT-4 |
| Custom scrapers | SerperDevTool, ScrapeWebsiteTool |

### Architecture Differences

- **ADK**: Sequential document processing
- **CrewAI**: Multi-agent collaborative analysis
- **LLM**: Migrated from Google Gemini to OpenAI GPT-4
- **Data Sources**: Web search for real-time information

## Best Practices

### For Analysts
1. Read full FOMC statement and minutes
2. Compare to previous meeting language
3. Track dot plot changes over time
4. Monitor economic data between meetings
5. Follow Fed official speeches

### For Investors
1. Focus on forward guidance changes
2. Watch for policy surprises
3. Consider market expectations vs reality
4. Diversify based on policy uncertainty
5. Adjust duration and risk accordingly

### For Researchers
1. Build historical FOMC database
2. Analyze language patterns over time
3. Correlate policy with economic outcomes
4. Study market reactions systematically
5. Track forecast accuracy

## Historical Context

### Recent FOMC History
- **2020-2021**: Pandemic response, near-zero rates, massive QE
- **2022**: Aggressive tightening, fastest rate hikes since 1980s
- **2023**: Continued tightening, then pause
- **2024**: Data-dependent approach, potential pivot

### Policy Regimes
- **Accommodative**: Supporting growth, low rates
- **Neutral**: Balanced stance, neutral rate
- **Restrictive**: Slowing economy, high rates

## Limitations

- Analysis based on publicly available information
- Cannot access proprietary Fed models or internal discussions
- Market predictions are uncertain
- Economic data subject to revisions
- Real-time data may not be complete

## Future Enhancements

- Historical FOMC database integration
- Automated data collection from FRED API
- Sentiment analysis of Fed communications
- Comparison to market expectations (Bloomberg, CME)
- Natural language processing for statement changes
- Backtesting of policy predictions
- Integration with portfolio management systems
- Real-time alerts for FOMC announcements

## Resources

### Official Sources
- Federal Reserve Board (federalreserve.gov)
- FOMC meeting calendar and statements
- Economic projections (SEP)
- Fed speeches and testimonies
- FRED economic data

### Research Tools
- Bloomberg Terminal
- CME FedWatch Tool
- Treasury yield data
- Economic calendars
- Academic research on Fed policy

## Original ADK Agent

Based on: Google Agent Development Kit (ADK) FOMC Research sample

## License

Apache License 2.0
