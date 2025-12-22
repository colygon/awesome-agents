"""
AI Trends Pipeline CrewAI Tasks
"""

from crewai import Task
from agents import trend_monitor, data_analyst, report_generator

def create_tasks(timeframe: str = "last 30 days", focus_areas: list = None):
    monitor_task = Task(
        description=f"""Monitor AI trends from {timeframe}.
        Focus areas: {focus_areas or ['all AI domains']}

        Identify:
        - Emerging techniques and models
        - Research breakthroughs
        - Industry applications
        - Open source releases
        - Funding and acquisitions""",
        agent=trend_monitor,
        expected_output="List of trending AI topics with sources and descriptions"
    )

    analyze_task = Task(
        description="""Analyze identified trends for:
        - Growth rate and momentum
        - Adoption indicators
        - Impact potential
        - Market readiness
        - Competitive landscape""",
        agent=data_analyst,
        expected_output="Quantified trend analysis with metrics and rankings",
        context=[monitor_task]
    )

    report_task = Task(
        description="""Create executive trend report with:
        - Top 10 trends ranked by impact
        - Growth trajectories
        - Strategic recommendations
        - Investment opportunities
        - Risk assessments""",
        agent=report_generator,
        expected_output="Comprehensive trends report with actionable insights",
        context=[monitor_task, analyze_task]
    )

    return [monitor_task, analyze_task, report_task]
