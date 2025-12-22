#!/usr/bin/env python3
"""
Financial Advisor CrewAI Agent
Converts Google ADK Financial Advisor to CrewAI implementation

Provides educational content about finance and investments.
Includes risk analysis, strategy generation, and report generation.
"""

import os
from crewai import Agent, Task, Crew, Process
from crewai_tools import SerperDevTool
from langchain_openai import ChatOpenAI
import datetime
import json

# Initialize OpenAI LLM (replacing Gemini)
llm = ChatOpenAI(
    model="gpt-4o",
    temperature=0.7,
    api_key=os.getenv("OPENAI_API_KEY")
)

# Initialize search tool
search_tool = SerperDevTool()

# Define Agents

# 1. Data Analyst Agent
data_analyst = Agent(
    role="Financial Data Analyst",
    goal="Analyze financial data, market trends, and investment performance",
    backstory="""You are an expert financial data analyst with deep knowledge of
    market analysis, financial metrics, and investment performance evaluation.
    You analyze data to identify trends, patterns, and opportunities.""",
    verbose=True,
    allow_delegation=False,
    tools=[search_tool],
    llm=llm
)

# 2. Risk Assessor Agent
risk_assessor = Agent(
    role="Investment Risk Assessor",
    goal="Evaluate investment risks and provide risk management strategies",
    backstory="""You are a seasoned risk management specialist who evaluates
    investment risks, market volatility, and potential downside scenarios.
    You provide comprehensive risk assessments and mitigation strategies.""",
    verbose=True,
    allow_delegation=False,
    tools=[search_tool],
    llm=llm
)

# 3. Financial Advisor Agent
advisor = Agent(
    role="Senior Financial Advisor",
    goal="Provide educational investment guidance and strategic recommendations",
    backstory="""You are a senior financial advisor who educates clients about
    investment strategies, portfolio management, and financial planning.
    You synthesize data and risk analysis into clear, actionable recommendations.""",
    verbose=True,
    allow_delegation=False,
    tools=[search_tool],
    llm=llm
)

def analyze_investment(
    investment_type: str,
    amount: float,
    time_horizon: str,
    risk_tolerance: str
) -> dict:
    """
    Provide investment guidance and analysis

    Args:
        investment_type: Type of investment (stocks, bonds, ETFs, etc.)
        amount: Investment amount
        time_horizon: Investment time horizon (short/medium/long term)
        risk_tolerance: Risk tolerance (conservative/moderate/aggressive)

    Returns:
        dict with analysis, risk_assessment, recommendations, report
    """

    current_date = datetime.datetime.now().strftime("%Y-%m-%d")

    # Task 1: Data Analysis
    analysis_task = Task(
        description=f"""Analyze the following investment scenario:
        - Investment Type: {investment_type}
        - Amount: ${amount:,.2f}
        - Time Horizon: {time_horizon}
        - Risk Tolerance: {risk_tolerance}

        Conduct comprehensive research on:
        1. Current market conditions for {investment_type}
        2. Historical performance and trends
        3. Economic factors affecting this investment
        4. Industry outlook and forecasts

        Use web search to gather current market data and trends.
        Current date: {current_date}

        Provide a detailed data analysis report.""",
        agent=data_analyst,
        expected_output="Comprehensive financial data analysis with market trends and performance metrics"
    )

    # Task 2: Risk Assessment
    risk_task = Task(
        description=f"""Based on the data analysis, evaluate investment risks:
        - Investment Type: {investment_type}
        - Amount: ${amount:,.2f}
        - Time Horizon: {time_horizon}
        - Risk Tolerance: {risk_tolerance}

        Assess:
        1. Market risk and volatility
        2. Liquidity risk
        3. Interest rate risk
        4. Inflation risk
        5. Sector-specific risks

        Provide risk ratings (Low/Medium/High) and mitigation strategies.
        Ensure recommendations align with {risk_tolerance} risk tolerance.""",
        agent=risk_assessor,
        expected_output="Detailed risk assessment with ratings and mitigation strategies",
        context=[analysis_task]
    )

    # Task 3: Advisory Recommendations
    advisory_task = Task(
        description=f"""Create educational investment guidance report:
        - Investment Type: {investment_type}
        - Amount: ${amount:,.2f}
        - Time Horizon: {time_horizon}
        - Risk Tolerance: {risk_tolerance}

        Synthesize the data analysis and risk assessment to provide:
        1. Executive Summary
        2. Investment Strategy Recommendations
        3. Portfolio Diversification Suggestions
        4. Expected Returns and Scenarios (best/expected/worst case)
        5. Action Plan and Next Steps
        6. Important Disclaimers

        IMPORTANT: This is educational content only, not personalized financial advice.
        Include appropriate disclaimers about seeking professional advice.

        Format as a comprehensive, professional advisory report.""",
        agent=advisor,
        expected_output="Complete investment advisory report with educational recommendations and disclaimers",
        context=[analysis_task, risk_task]
    )

    # Create and run crew
    crew = Crew(
        agents=[data_analyst, risk_assessor, advisor],
        tasks=[analysis_task, risk_task, advisory_task],
        process=Process.sequential,
        verbose=True
    )

    result = crew.kickoff()

    return {
        "data_analysis": analysis_task.output.raw if hasattr(analysis_task, 'output') else "",
        "risk_assessment": risk_task.output.raw if hasattr(risk_task, 'output') else "",
        "advisory_report": str(result),
        "metadata": {
            "investment_type": investment_type,
            "amount": amount,
            "time_horizon": time_horizon,
            "risk_tolerance": risk_tolerance,
            "date": current_date
        }
    }

def save_report(content: str, filename: str):
    """Save advisory report to file"""
    if not filename.endswith('.md'):
        filename += '.md'

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
        f.write("\n\n---\n")
        f.write("**DISCLAIMER**: This report is for educational purposes only and does not constitute ")
        f.write("personalized financial advice. Please consult with a qualified financial advisor ")
        f.write("before making investment decisions.\n")

    print(f"\nReport saved to: {filename}")

if __name__ == "__main__":
    print("Financial Advisor CrewAI Agent")
    print("=" * 50)
    print("Educational Investment Guidance System")
    print("=" * 50)

    # Get investment parameters
    investment_type = input("\nInvestment type (e.g., stocks, bonds, ETFs, real estate): ").strip()
    if not investment_type:
        investment_type = "diversified ETF portfolio"

    try:
        amount = float(input("Investment amount ($): ").strip() or "10000")
    except ValueError:
        amount = 10000.0

    time_horizon = input("Time horizon (short/medium/long term): ").strip().lower()
    if time_horizon not in ['short', 'medium', 'long']:
        time_horizon = "long"

    risk_tolerance = input("Risk tolerance (conservative/moderate/aggressive): ").strip().lower()
    if risk_tolerance not in ['conservative', 'moderate', 'aggressive']:
        risk_tolerance = "moderate"

    print(f"\nAnalyzing investment scenario...")
    print(f"Type: {investment_type}")
    print(f"Amount: ${amount:,.2f}")
    print(f"Time Horizon: {time_horizon} term")
    print(f"Risk Tolerance: {risk_tolerance}")

    # Analyze investment
    result = analyze_investment(
        investment_type=investment_type,
        amount=amount,
        time_horizon=time_horizon,
        risk_tolerance=risk_tolerance
    )

    # Display result
    print("\n" + "=" * 50)
    print("INVESTMENT ADVISORY REPORT")
    print("=" * 50)
    print(result["advisory_report"])
    print("\n" + "=" * 50)
    print("DISCLAIMER: Educational purposes only. Consult a qualified financial advisor.")
    print("=" * 50)

    # Save option
    save = input("\n\nSave report to file? (y/n): ").strip().lower()
    if save == 'y':
        filename = input("Enter filename (without .md extension): ").strip()
        if filename:
            save_report(result["advisory_report"], filename)
