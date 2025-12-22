"""
McLachApp - Sports Analytics with CrewAI
Version 2.0.0-crewai

Intelligent sports analytics platform powered by multi-agent AI systems.
"""

__version__ = "2.0.0-crewai"
__author__ = "Agent 60"
__description__ = "Sports Analytics with CrewAI Multi-Agent System"

from agents import SportsAnalyticsAgents
from tasks import SportsAnalyticsTasks
from crew import (
    SportsAnalyticsCrew,
    run_player_analysis,
    run_team_analysis,
    run_player_comparison,
    run_match_analysis
)

__all__ = [
    "SportsAnalyticsAgents",
    "SportsAnalyticsTasks",
    "SportsAnalyticsCrew",
    "run_player_analysis",
    "run_team_analysis",
    "run_player_comparison",
    "run_match_analysis",
]
