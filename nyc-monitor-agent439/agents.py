"""
NYC Monitor - CrewAI Agent Definitions
Multi-Agent NYC Data Monitoring System

Agents for monitoring NYC data and events:
1. Data Collector - Collects data from NYC APIs and sources
2. Trend Analyzer - Analyzes trends and patterns
3. Alert Generator - Generates alerts and notifications
"""

from crewai import Agent
from textwrap import dedent

def create_data_collector() -> Agent:
    return Agent(role="Data Collector", goal="Collect data from NYC open data sources and APIs",
        backstory="Data integration expert with knowledge of NYC Open Data portal and APIs.", verbose=True, allow_delegation=False, memory=True)

def create_trend_analyzer() -> Agent:
    return Agent(role="Trend Analyzer", goal="Analyze trends and patterns in NYC data",
        backstory="Urban data analyst specializing in city metrics and trend identification.", verbose=True, allow_delegation=False, memory=True)

def create_alert_generator() -> Agent:
    return Agent(role="Alert Generator", goal="Generate actionable alerts from NYC data insights",
        backstory="Alert systems specialist who creates timely, relevant notifications.", verbose=True, allow_delegation=False, memory=True)
