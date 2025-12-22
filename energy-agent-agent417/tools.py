"""Energy Agent AI Tools"""

from crewai_tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field
from langchain_openai import ChatOpenAI


class EnergyDataInput(BaseModel):
    property_type: str = Field(..., description="Property type")
    size: str = Field(..., description="Property size")


class EnergyDataTool(BaseTool):
    name: str = "Energy Data Tool"
    description: str = "Provides energy consumption data and benchmarks"
    args_schema: Type[BaseModel] = EnergyDataInput

    def _run(self, property_type: str, size: str) -> str:
        try:
            llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.2)
            prompt = f"""Provide energy benchmarks for {property_type} ({size}):
            1. Typical annual consumption (kWh)
            2. Breakdown by end use (HVAC, lighting, appliances)
            3. Cost estimates
            4. Comparison with efficient buildings"""
            response = llm.invoke(prompt)
            return response.content
        except Exception as e:
            return f"Error: {str(e)}"


class ConsumptionInput(BaseModel):
    usage_data: str = Field(..., description="Energy usage data")


class ConsumptionAnalysisTool(BaseTool):
    name: str = "Consumption Analysis Tool"
    description: str = "Analyzes energy consumption patterns"
    args_schema: Type[BaseModel] = ConsumptionInput

    def _run(self, usage_data: str) -> str:
        try:
            llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.3)
            prompt = f"""Analyze energy consumption: {usage_data}
            Identify:
            1. Peak usage periods
            2. Baseload consumption
            3. Anomalies or waste
            4. Seasonal patterns
            5. Optimization opportunities"""
            response = llm.invoke(prompt)
            return response.content
        except Exception as e:
            return f"Error: {str(e)}"


class RecommendationInput(BaseModel):
    audit_findings: str = Field(..., description="Audit findings")


class RecommendationTool(BaseTool):
    name: str = "Recommendation Tool"
    description: str = "Generates energy recommendations"
    args_schema: Type[BaseModel] = RecommendationInput

    def _run(self, audit_findings: str) -> str:
        try:
            llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.4)
            prompt = f"""Based on findings: {audit_findings}
            Recommend:
            1. Quick wins (low cost, high impact)
            2. Medium-term projects
            3. Long-term investments
            4. Behavioral changes
            5. Technology upgrades"""
            response = llm.invoke(prompt)
            return response.content
        except Exception as e:
            return f"Error: {str(e)}"
