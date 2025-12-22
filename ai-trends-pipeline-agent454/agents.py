"""
AI Trends Pipeline CrewAI Agents
"""

from crewai import Agent
from tools import TrendMonitorTool, DataAnalysisTool, ReportGeneratorTool

trend_monitor = Agent(
    role="AI Trends Monitor",
    goal="Monitor and identify emerging AI trends from multiple sources",
    backstory="""Expert in AI research monitoring with access to papers, news, and social media.
    You track breakthroughs, emerging techniques, and industry developments.""",
    verbose=True,
    allow_delegation=False,
    tools=[TrendMonitorTool()]
)

data_analyst = Agent(
    role="Trend Data Analyst",
    goal="Analyze trend data to identify patterns and significance",
    backstory="""Data scientist specializing in trend analysis. You quantify trends,
    identify growth patterns, and assess impact and adoption rates.""",
    verbose=True,
    allow_delegation=False,
    tools=[DataAnalysisTool()]
)

report_generator = Agent(
    role="Trends Report Generator",
    goal="Create comprehensive trend reports with actionable insights",
    backstory="""Strategic analyst who synthesizes trend data into executive-ready reports
    with predictions and recommendations.""",
    verbose=True,
    allow_delegation=False,
    tools=[ReportGeneratorTool()]
)
