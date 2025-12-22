"""
Time Series Forecasting Java - CrewAI Implementation
Original: Java ADK, Migrated to Python CrewAI
"""

from crewai import Agent
from tools import TimeSeriesAnalysisTool, ForecastingTool, AnomalyDetectionTool

# Data Analyzer Agent
data_analyzer = Agent(
    role="Time Series Data Analyst",
    goal="Analyze time series data patterns, trends, and seasonality",
    backstory="""You are a data analyst specializing in time series analysis.
    You understand trends, seasonality, cycles, and noise. You can identify patterns
    in temporal data and prepare it for forecasting.""",
    verbose=True,
    allow_delegation=False,
    tools=[TimeSeriesAnalysisTool()]
)

# Forecasting Specialist Agent
forecasting_specialist = Agent(
    role="Forecasting Model Specialist",
    goal="Build and optimize time series forecasting models",
    backstory="""You are an expert in forecasting methods including ARIMA, Prophet,
    LSTM, and exponential smoothing. You select appropriate models based on data
    characteristics and requirements.""",
    verbose=True,
    allow_delegation=False,
    tools=[ForecastingTool()]
)

# Anomaly Detector Agent
anomaly_detector = Agent(
    role="Anomaly Detection Specialist",
    goal="Identify anomalies and outliers in time series data",
    backstory="""You detect unusual patterns, outliers, and anomalies in temporal data.
    You distinguish between natural variation and genuine anomalies.""",
    verbose=True,
    allow_delegation=False,
    tools=[AnomalyDetectionTool()]
)

# Validation Engineer Agent
validation_engineer = Agent(
    role="Model Validation Engineer",
    goal="Validate forecast accuracy and model performance",
    backstory="""You evaluate forecasting models using metrics like MAE, RMSE, and MAPE.
    You perform cross-validation and backtesting to ensure model reliability.""",
    verbose=True,
    allow_delegation=False
)

# Reporting Specialist Agent
reporting_specialist = Agent(
    role="Forecasting Report Specialist",
    goal="Create comprehensive forecasting reports with visualizations",
    backstory="""You create clear, actionable forecasting reports with insights,
    confidence intervals, and recommendations for decision-makers.""",
    verbose=True,
    allow_delegation=False
)
