"""Forkcast - CrewAI Task Definitions"""
from crewai import Task
from textwrap import dedent

def create_data_analysis_task(agent, data_context: dict) -> Task:
    return Task(
        description=f"Analyze historical data: {data_context.get('description', '')}. Identify trends, seasonality, and anomalies.",
        expected_output="Data analysis report with visualizations and statistical summaries.",
        agent=agent
    )

def create_forecast_modeling_task(agent, analysis_output) -> Task:
    return Task(
        description=f"Build forecast models based on analysis: {analysis_output}",
        expected_output="Predictive models with accuracy metrics and forecasts.",
        agent=agent,
        context=[analysis_output] if isinstance(analysis_output, Task) else []
    )

def create_insights_task(agent, analysis_output, forecast_output) -> Task:
    return Task(
        description=f"Interpret forecasts and generate insights. Analysis: {analysis_output}, Forecast: {forecast_output}",
        expected_output="Business insights report with recommendations and risk assessment.",
        agent=agent,
        context=[analysis_output, forecast_output] if isinstance(analysis_output, Task) else []
    )
