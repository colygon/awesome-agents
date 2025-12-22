"""Tools for Time Series Forecasting"""

from crewai_tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field


class TimeSeriesAnalysisInput(BaseModel):
    data_description: str = Field(..., description="Description of time series data")


class TimeSeriesAnalysisTool(BaseTool):
    name: str = "Time Series Analysis Tool"
    description: str = "Analyzes time series for trends, seasonality, and patterns"
    args_schema: Type[BaseModel] = TimeSeriesAnalysisInput

    def _run(self, data_description: str) -> str:
        return f"Time series analysis for: {data_description}\nNote: Integrate with pandas, statsmodels for real analysis"


class ForecastingInput(BaseModel):
    method: str = Field(..., description="Forecasting method to use")


class ForecastingTool(BaseTool):
    name: str = "Forecasting Tool"
    description: str = "Generates forecasts using various methods"
    args_schema: Type[BaseModel] = ForecastingInput

    def _run(self, method: str) -> str:
        return f"Generating forecast using {method}\nNote: Integrate Prophet, ARIMA, or LSTM models"


class AnomalyDetectionInput(BaseModel):
    threshold: float = Field(default=3.0, description="Anomaly detection threshold")


class AnomalyDetectionTool(BaseTool):
    name: str = "Anomaly Detection Tool"
    description: str = "Detects anomalies in time series data"
    args_schema: Type[BaseModel] = AnomalyDetectionInput

    def _run(self, threshold: float = 3.0) -> str:
        return f"Detecting anomalies with threshold {threshold}\nNote: Use isolation forest or statistical methods"
