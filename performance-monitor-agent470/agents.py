"""
CrewAI Agents for Performance Monitor
Specialized agents for system and application performance monitoring
"""

from crewai import Agent
import os


class PerformanceMonitorAgents:
    """Factory class for creating performance monitoring agents"""

    def __init__(self):
        self.openai_api_key = os.getenv('OPENAI_API_KEY')

    def metrics_collector(self) -> Agent:
        """Metrics Collection Agent"""
        return Agent(
            role='Performance Metrics Collector',
            goal='Collect, aggregate, and organize system and application performance metrics',
            backstory='You are an observability expert specializing in metrics collection and time-series data analysis.',
            verbose=True,
            allow_delegation=False,
            tools=[],
            llm='gpt-4o'
        )

    def bottleneck_analyzer(self) -> Agent:
        """Bottleneck Analysis Agent"""
        return Agent(
            role='Performance Bottleneck Analyst',
            goal='Identify performance bottlenecks, slow queries, and resource constraints',
            backstory='You excel at performance profiling and identifying system bottlenecks through data analysis.',
            verbose=True,
            allow_delegation=False,
            tools=[],
            llm='gpt-4o'
        )

    def trend_forecaster(self) -> Agent:
        """Trend Forecasting Agent"""
        return Agent(
            role='Performance Trend Forecaster',
            goal='Analyze performance trends and predict future capacity needs',
            backstory='You specialize in capacity planning and predictive analytics for system performance.',
            verbose=True,
            allow_delegation=False,
            tools=[],
            llm='gpt-4o'
        )

    def alert_manager(self) -> Agent:
        """Alert Management Agent"""
        return Agent(
            role='Performance Alert Manager',
            goal='Configure intelligent alerts, detect anomalies, and manage incident response',
            backstory='You are skilled at setting up monitoring alerts that balance sensitivity with reducing noise.',
            verbose=True,
            allow_delegation=False,
            tools=[],
            llm='gpt-4o'
        )
