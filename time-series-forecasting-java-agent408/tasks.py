"""Time Series Forecasting Tasks"""

from crewai import Task
from agents import data_analyzer, forecasting_specialist, anomaly_detector, validation_engineer, reporting_specialist


def create_tasks(data_description: str, forecast_horizon: int = 30):
    analyze = Task(
        description=f"Analyze time series data: {data_description}\nIdentify patterns and trends",
        agent=data_analyzer,
        expected_output="Data analysis with trend, seasonality, and pattern identification"
    )

    detect_anomalies = Task(
        description="Detect anomalies in the time series",
        agent=anomaly_detector,
        expected_output="Anomaly detection report",
        context=[analyze]
    )

    forecast = Task(
        description=f"Generate {forecast_horizon}-period forecast",
        agent=forecasting_specialist,
        expected_output="Forecasted values with confidence intervals",
        context=[analyze, detect_anomalies]
    )

    validate = Task(
        description="Validate forecast model performance",
        agent=validation_engineer,
        expected_output="Model validation metrics and accuracy assessment",
        context=[forecast]
    )

    report = Task(
        description="Create comprehensive forecasting report",
        agent=reporting_specialist,
        expected_output="Executive summary with forecast and recommendations",
        context=[analyze, detect_anomalies, forecast, validate]
    )

    return [analyze, detect_anomalies, forecast, validate, report]
