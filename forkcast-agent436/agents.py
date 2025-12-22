"""
Forkcast - CrewAI Agent Definitions
Multi-Agent Forecasting and Prediction System

Agents for data forecasting and trend analysis:
1. Data Analyst - Analyzes historical data and trends
2. Forecast Modeler - Builds predictive models
3. Insights Interpreter - Interprets results and generates insights
"""

from crewai import Agent
from textwrap import dedent


def create_data_analyst() -> Agent:
    return Agent(
        role="Data Analyst",
        goal="Analyze historical data to identify patterns and trends",
        backstory=dedent("""
            You are an expert data analyst with deep knowledge of statistical analysis,
            time series data, and trend identification. You excel at cleaning, transforming,
            and analyzing data to uncover meaningful patterns.
        """),
        verbose=True,
        allow_delegation=False,
        memory=True
    )


def create_forecast_modeler() -> Agent:
    return Agent(
        role="Forecast Modeler",
        goal="Build accurate predictive models for forecasting",
        backstory=dedent("""
            You are a machine learning expert specialized in forecasting models including
            ARIMA, Prophet, LSTM, and ensemble methods. You create robust models that
            deliver accurate predictions.
        """),
        verbose=True,
        allow_delegation=False,
        memory=True
    )


def create_insights_interpreter() -> Agent:
    return Agent(
        role="Insights Interpreter",
        goal="Interpret forecast results and generate actionable business insights",
        backstory=dedent("""
            You are a business analyst who translates technical forecasts into clear,
            actionable insights for stakeholders. You understand uncertainty quantification
            and risk assessment.
        """),
        verbose=True,
        allow_delegation=False,
        memory=True
    )
