"""Agentic Trading - CrewAI Tools"""
from crewai_tools import tool

@tool("Technical Indicator Calculator")
def calculate_indicator(indicator: str, data: list) -> dict:
    return {"values": [], "signal": "neutral"}

@tool("Backtest Engine")
def run_backtest(strategy: dict, historical_data: list) -> dict:
    return {"sharpe_ratio": 1.5, "max_drawdown": -0.15, "total_return": 0.25}
