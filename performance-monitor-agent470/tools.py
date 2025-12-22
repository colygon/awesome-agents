"""Custom Tools for Performance Monitor"""

from crewai_tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field


class MetricsCollectorInput(BaseModel):
    metric_name: str = Field(..., description="Metric to collect")
    timeframe: str = Field(default="1h", description="Collection timeframe")


class MetricsCollectorTool(BaseTool):
    name: str = "Metrics Collector"
    description: str = "Collects system and application performance metrics"
    args_schema: Type[BaseModel] = MetricsCollectorInput

    def _run(self, metric_name: str, timeframe: str = "1h") -> str:
        return f"Metrics for {metric_name} ({timeframe}):\\nAvg: 45.2%\\nMax: 78.5%\\nMin: 12.3%\\nP95: 65.1%"


class AnomalyDetectorInput(BaseModel):
    metric_data: str = Field(..., description="Metric data to analyze")


class AnomalyDetectorTool(BaseTool):
    name: str = "Anomaly Detector"
    description: str = "Detects anomalies in performance metrics using statistical analysis"
    args_schema: Type[BaseModel] = AnomalyDetectorInput

    def _run(self, metric_data: str) -> str:
        return "Anomaly Detection Results:\\nAnomalies detected: 3\\nSeverity: MEDIUM\\nPattern: Sudden spike at 14:23 UTC"
