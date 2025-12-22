"""
Agentic Trading - CrewAI Agent Definitions
Multi-Agent Trading System

Agents for algorithmic trading:
1. Market Analyst - Analyzes market trends and conditions
2. Strategy Developer - Develops and backtests trading strategies
3. Risk Manager - Manages risk and portfolio optimization
"""

from crewai import Agent
from textwrap import dedent

def create_market_analyst() -> Agent:
    return Agent(role="Market Analyst", goal="Analyze market trends and conditions",
        backstory="Expert in technical and fundamental analysis with deep market knowledge.", verbose=True, allow_delegation=False, memory=True)

def create_strategy_developer() -> Agent:
    return Agent(role="Strategy Developer", goal="Develop and backtest trading strategies",
        backstory="Quantitative analyst expert in algorithmic trading and backtesting.", verbose=True, allow_delegation=False, memory=True)

def create_risk_manager() -> Agent:
    return Agent(role="Risk Manager", goal="Manage risk and optimize portfolio",
        backstory="Risk management specialist focused on portfolio optimization and capital preservation.", verbose=True, allow_delegation=False, memory=True)
