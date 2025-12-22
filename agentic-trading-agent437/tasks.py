"""Agentic Trading - CrewAI Task Definitions"""
from crewai import Task

def create_market_analysis_task(agent, market_data: dict) -> Task:
    return Task(description=f"Analyze market: {market_data.get('symbol', '')}. Identify trends and signals.", expected_output="Market analysis report.", agent=agent)

def create_strategy_task(agent, analysis_output) -> Task:
    return Task(description=f"Develop trading strategy based on: {analysis_output}", expected_output="Trading strategy with backtest results.", agent=agent, context=[analysis_output] if isinstance(analysis_output, Task) else [])

def create_risk_management_task(agent, analysis_output, strategy_output) -> Task:
    return Task(description=f"Optimize risk for strategy. Analysis: {analysis_output}, Strategy: {strategy_output}", expected_output="Risk management plan with position sizing.", agent=agent, context=[analysis_output, strategy_output] if isinstance(analysis_output, Task) else [])
