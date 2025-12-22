"""
Custom Tools for AI Trends Pipeline
"""

from crewai_tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field
from langchain_openai import ChatOpenAI
import os
import requests


class TrendMonitorInput(BaseModel):
    timeframe: str = Field(..., description="Time period to monitor")
    sources: list[str] = Field(default_factory=lambda: ["arxiv", "news", "github"], description="Sources to monitor")


class TrendMonitorTool(BaseTool):
    name: str = "AI Trend Monitor"
    description: str = "Monitors AI trends from research papers, news, and industry sources"
    args_schema: Type[BaseModel] = TrendMonitorInput

    def _run(self, timeframe: str, sources: list[str] = None) -> str:
        try:
            llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.3)
            serper_key = os.getenv("SERPER_API_KEY")

            if serper_key:
                results = []
                for source in sources or ["arxiv", "news", "github"]:
                    url = "https://google.serper.dev/search"
                    payload = {"q": f"AI trends {source} {timeframe}", "num": 10}
                    headers = {"X-API-KEY": serper_key, "Content-Type": "application/json"}
                    response = requests.post(url, json=payload, headers=headers)
                    if response.status_code == 200:
                        results.append(response.json())

                prompt = f"Analyze these AI trends: {results}\nIdentify top emerging trends."
                return llm.invoke(prompt).content

            prompt = f"Based on general knowledge, what are the top AI trends in {timeframe}?"
            return llm.invoke(prompt).content
        except Exception as e:
            return f"Error monitoring trends: {str(e)}"


class DataAnalysisTool(BaseTool):
    name: str = "Trend Data Analyzer"
    description: str = "Analyzes trend data for growth patterns and significance"
    args_schema: Type[BaseModel] = BaseModel

    def _run(self, trend_data: str = "") -> str:
        try:
            llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.2)
            prompt = f"""Analyze these trends: {trend_data}
            Provide:
            - Growth metrics
            - Adoption indicators
            - Impact scores
            - Rankings"""
            return llm.invoke(prompt).content
        except Exception as e:
            return f"Error analyzing data: {str(e)}"


class ReportGeneratorTool(BaseTool):
    name: str = "Trend Report Generator"
    description: str = "Generates comprehensive trend reports"
    args_schema: Type[BaseModel] = BaseModel

    def _run(self, analysis: str = "") -> str:
        try:
            llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.3)
            prompt = f"""Create executive trend report from: {analysis}
            Include:
            - Executive summary
            - Top trends ranked
            - Strategic recommendations
            - Action items"""
            return llm.invoke(prompt).content
        except Exception as e:
            return f"Error generating report: {str(e)}"
