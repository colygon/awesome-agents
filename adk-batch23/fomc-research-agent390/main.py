#!/usr/bin/env python3
"""
FOMC Research Agent - CrewAI Implementation
Federal Open Market Committee meeting analysis and economic research
"""

import os
import json
from crewai import Agent, Task, Crew, Process
from crewai_tools import SerperDevTool, ScrapeWebsiteTool
from langchain_openai import ChatOpenAI
import datetime

# Initialize OpenAI LLM
llm = ChatOpenAI(
    model="gpt-4o",
    temperature=0.5,  # Balanced for financial analysis
    api_key=os.getenv("OPENAI_API_KEY")
)

# Initialize tools
search_tool = SerperDevTool()
scrape_tool = ScrapeWebsiteTool()

# Define Agents

# 1. FOMC Document Researcher
fomc_researcher = Agent(
    role="FOMC Document Research Analyst",
    goal="Research and analyze FOMC meeting minutes, statements, and economic data",
    backstory="""You are an expert Federal Reserve analyst who specializes in
    analyzing FOMC (Federal Open Market Committee) meeting documents. You understand
    monetary policy, economic indicators, and Fed communications. You can identify
    key policy changes, economic assessments, and forward guidance in FOMC materials.""",
    verbose=True,
    allow_delegation=False,
    tools=[search_tool, scrape_tool],
    llm=llm
)

# 2. Economic Data Analyst
economic_analyst = Agent(
    role="Economic Data Analyst",
    goal="Analyze economic indicators and their implications for monetary policy",
    backstory="""You are a macroeconomic analyst with expertise in analyzing
    economic indicators like inflation, employment, GDP, and market data. You
    understand how these metrics influence Federal Reserve policy decisions and
    can contextualize economic trends within the Fed's dual mandate of price
    stability and maximum employment.""",
    verbose=True,
    allow_delegation=False,
    tools=[search_tool],
    llm=llm
)

# 3. Policy Interpretation Specialist
policy_analyst = Agent(
    role="Monetary Policy Interpretation Specialist",
    goal="Interpret FOMC decisions and forward guidance",
    backstory="""You are a monetary policy expert who excels at interpreting
    Federal Reserve communications, including statements, minutes, and speeches.
    You understand the nuances of Fed language, can identify policy shifts, and
    interpret forward guidance. You know the difference between hawkish and
    dovish signals and their market implications.""",
    verbose=True,
    allow_delegation=False,
    llm=llm
)

# 4. Market Impact Analyst
market_analyst = Agent(
    role="Financial Market Impact Analyst",
    goal="Assess market implications of FOMC decisions and communications",
    backstory="""You are a financial markets analyst who evaluates how FOMC
    decisions and communications affect financial markets, including equities,
    bonds, currencies, and commodities. You understand market expectations,
    surprise factors, and how policy changes flow through to asset prices.""",
    verbose=True,
    allow_delegation=False,
    tools=[search_tool],
    llm=llm
)

# 5. Research Report Writer
report_writer = Agent(
    role="Economic Research Report Writer",
    goal="Synthesize FOMC analysis into comprehensive research reports",
    backstory="""You are an experienced economic research writer who creates
    clear, comprehensive reports on Federal Reserve policy. You synthesize
    complex economic and policy information into accessible analysis for
    investors, policymakers, and researchers. You excel at structured reporting
    and actionable insights.""",
    verbose=True,
    allow_delegation=False,
    llm=llm
)

def analyze_fomc_meeting(
    meeting_date: str = None,
    analysis_focus: str = "comprehensive"
) -> dict:
    """
    Analyze FOMC meeting and provide comprehensive research report

    Args:
        meeting_date: Date of FOMC meeting (YYYY-MM-DD) or "latest"
        analysis_focus: Focus area (comprehensive, policy, markets, economic_outlook)

    Returns:
        dict with FOMC analysis and report
    """

    if meeting_date is None or meeting_date == "latest":
        meeting_date = "latest available"

    current_date = datetime.datetime.now().strftime("%Y-%m-%d")

    # Task 1: Research FOMC Documents
    research_task = Task(
        description=f"""Research FOMC meeting materials for: {meeting_date}

        Find and analyze:
        1. **FOMC Statement**
           - Policy decision (interest rate changes)
           - Economic assessment
           - Forward guidance
           - Vote count and dissents

        2. **Meeting Minutes** (if available)
           - Discussion points
           - Economic projections
           - Policy debates
           - Risk assessments

        3. **Economic Projections** (if available)
           - GDP forecasts
           - Unemployment projections
           - Inflation expectations
           - Interest rate dot plot

        4. **Chair's Press Conference** (if available)
           - Key messages
           - Q&A highlights
           - Policy clarifications

        Use web search to find official Federal Reserve sources.
        Current date: {current_date}

        Provide comprehensive summary of FOMC materials.""",
        agent=fomc_researcher,
        expected_output="Comprehensive summary of FOMC meeting documents and key points"
    )

    # Task 2: Economic Context Analysis
    economic_task = Task(
        description=f"""Analyze economic context surrounding FOMC meeting: {meeting_date}

        Evaluate key economic indicators:

        1. **Inflation Metrics**
           - CPI and Core CPI trends
           - PCE and Core PCE (Fed's preferred measure)
           - Inflation expectations
           - Wage growth

        2. **Employment Data**
           - Unemployment rate
           - Job creation trends
           - Labor force participation
           - Job openings and quits

        3. **Economic Growth**
           - GDP growth rate
           - Consumer spending
           - Business investment
           - Trade balance

        4. **Financial Conditions**
           - Credit markets
           - Banking sector health
           - Market volatility
           - Financial stress indicators

        Use web search for recent economic data.

        Provide economic context analysis.""",
        agent=economic_analyst,
        expected_output="Economic context analysis with key indicators",
        context=[research_task]
    )

    # Task 3: Policy Interpretation
    policy_task = Task(
        description=f"""Interpret FOMC policy stance and forward guidance:

        Based on FOMC materials and economic context, analyze:

        1. **Policy Stance**
           - Current policy position (accommodative, neutral, restrictive)
           - Changes from previous meeting
           - Hawkish vs dovish signals
           - Policy path implications

        2. **Forward Guidance**
           - Interest rate trajectory signals
           - Conditions for policy changes
           - Balance sheet policy (QT/QE)
           - Timeline and pace expectations

        3. **Dual Mandate Assessment**
           - Progress on price stability
           - Maximum employment status
           - Trade-offs being considered
           - Risk balance

        4. **Policy Risks**
           - Upside inflation risks
           - Downside growth risks
           - Financial stability concerns
           - External factors (global economy, geopolitics)

        Provide detailed policy interpretation.""",
        agent=policy_analyst,
        expected_output="Detailed monetary policy interpretation and forward guidance analysis",
        context=[research_task, economic_task]
    )

    # Task 4: Market Impact Assessment
    market_task = Task(
        description=f"""Assess market implications of FOMC decision:

        Analyze market impact and outlook:

        1. **Immediate Market Reaction**
           - Equity market response
           - Bond yields and curve
           - Dollar exchange rate
           - Gold and commodities

        2. **Market Expectations**
           - Pre-meeting expectations
           - Surprise elements
           - Market pricing of future rates
           - Fed funds futures

        3. **Sector and Asset Implications**
           - Interest-sensitive sectors (financials, real estate)
           - Growth vs value stocks
           - Duration risk in bonds
           - Credit spreads

        4. **Investment Implications**
           - Portfolio positioning recommendations
           - Risk management considerations
           - Opportunities and risks
           - Time horizon considerations

        Use web search for market data and reactions.

        Provide market impact assessment.""",
        agent=market_analyst,
        expected_output="Comprehensive market impact assessment and investment implications",
        context=[research_task, policy_task]
    )

    # Task 5: Comprehensive Research Report
    report_task = Task(
        description=f"""Create comprehensive FOMC research report:

        Synthesize all analysis into structured research report:

        ## Executive Summary
        - Key takeaways (3-5 bullets)
        - Policy decision and rationale
        - Market implications
        - Outlook and recommendations

        ## FOMC Meeting Overview
        - Meeting date and context
        - Policy decision details
        - Vote and dissents
        - Key statement language changes

        ## Economic Assessment
        - Fed's view of economy
        - Key economic indicators
        - Economic projections (if available)
        - Comparison to previous meeting

        ## Monetary Policy Analysis
        - Current policy stance
        - Forward guidance interpretation
        - Expected policy path
        - Risk assessment

        ## Market Implications
        - Market reaction summary
        - Asset class implications
        - Investment strategy considerations
        - Risk factors to monitor

        ## Outlook and Recommendations
        - Near-term policy expectations
        - Key data points to watch
        - Potential scenarios
        - Strategic recommendations

        ## Appendix
        - Economic data summary
        - Historical context
        - Glossary of key terms

        Format as professional research report in Markdown.
        Focus: {analysis_focus}""",
        agent=report_writer,
        expected_output="Complete FOMC research report in Markdown format",
        context=[research_task, economic_task, policy_task, market_task]
    )

    # Create and run crew
    crew = Crew(
        agents=[fomc_researcher, economic_analyst, policy_analyst, market_analyst, report_writer],
        tasks=[research_task, economic_task, policy_task, market_task, report_task],
        process=Process.sequential,
        verbose=True
    )

    result = crew.kickoff()

    return {
        "fomc_research": research_task.output.raw if hasattr(research_task, 'output') else "",
        "economic_context": economic_task.output.raw if hasattr(economic_task, 'output') else "",
        "policy_interpretation": policy_task.output.raw if hasattr(policy_task, 'output') else "",
        "market_impact": market_task.output.raw if hasattr(market_task, 'output') else "",
        "full_report": str(result),
        "metadata": {
            "meeting_date": meeting_date,
            "analysis_focus": analysis_focus,
            "report_date": current_date
        }
    }

def save_report(content: str, filename: str):
    """Save FOMC research report to file"""
    if not filename.endswith('.md'):
        filename += '.md'

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"\nReport saved to: {filename}")

if __name__ == "__main__":
    print("FOMC Research Agent - CrewAI")
    print("=" * 60)
    print("Federal Open Market Committee Analysis")
    print("=" * 60)

    # Get analysis parameters
    print("\nFOMC Meeting Analysis Options:")
    print("1. Latest FOMC meeting")
    print("2. Specific meeting date")

    choice = input("\nSelect option (1-2) [1]: ").strip()

    if choice == "2":
        meeting_date = input("Enter FOMC meeting date (YYYY-MM-DD): ").strip()
    else:
        meeting_date = "latest"

    print("\nAnalysis Focus:")
    print("1. Comprehensive (all aspects)")
    print("2. Policy focus (monetary policy details)")
    print("3. Markets focus (market implications)")
    print("4. Economic outlook focus")

    focus_choice = input("\nSelect focus (1-4) [1]: ").strip()
    focus_map = {
        "1": "comprehensive",
        "2": "policy",
        "3": "markets",
        "4": "economic_outlook"
    }
    analysis_focus = focus_map.get(focus_choice, "comprehensive")

    print(f"\nAnalyzing FOMC meeting: {meeting_date}")
    print(f"Analysis focus: {analysis_focus}")
    print("\nThis may take several minutes...\n")

    # Run analysis
    result = analyze_fomc_meeting(meeting_date, analysis_focus)

    # Display report
    print("\n" + "=" * 60)
    print("FOMC RESEARCH REPORT")
    print("=" * 60)
    print(result["full_report"])

    # Save option
    save = input("\n\nSave report to file? (y/n): ").strip().lower()
    if save == 'y':
        filename = input("Enter filename (without .md extension): ").strip()
        if not filename:
            filename = f"fomc-report-{datetime.datetime.now().strftime('%Y%m%d')}"
        save_report(result["full_report"], filename)
