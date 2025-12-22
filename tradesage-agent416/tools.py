"""TradeSage AI Custom Tools"""

from crewai_tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field
from langchain_openai import ChatOpenAI


class MarketDataInput(BaseModel):
    ticker: str = Field(..., description="Stock ticker symbol")


class MarketDataTool(BaseTool):
    name: str = "Market Data Tool"
    description: str = "Fetches market data and fundamentals"
    args_schema: Type[BaseModel] = MarketDataInput

    def _run(self, ticker: str) -> str:
        try:
            llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.3)
            prompt = f"""Provide market analysis for {ticker}:
            1. Company overview
            2. Recent news and events
            3. Sector analysis
            4. Fundamental metrics (P/E, revenue growth, etc.)
            5. Market sentiment"""
            response = llm.invoke(prompt)
            return response.content
        except Exception as e:
            return f"Error: {str(e)}"


class TechnicalAnalysisInput(BaseModel):
    ticker: str = Field(..., description="Stock ticker")


class TechnicalAnalysisTool(BaseTool):
    name: str = "Technical Analysis Tool"
    description: str = "Performs technical analysis"
    args_schema: Type[BaseModel] = TechnicalAnalysisInput

    def _run(self, ticker: str) -> str:
        try:
            llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.3)
            prompt = f"""Technical analysis for {ticker}:
            1. Trend direction
            2. Key support/resistance levels
            3. Indicator signals (RSI, MACD, Moving Averages)
            4. Chart patterns
            5. Trading signals"""
            response = llm.invoke(prompt)
            return response.content
        except Exception as e:
            return f"Error: {str(e)}"


class RiskInput(BaseModel):
    ticker: str = Field(..., description="Ticker")
    capital: float = Field(..., description="Trading capital")


class RiskAssessmentTool(BaseTool):
    name: str = "Risk Assessment Tool"
    description: str = "Assesses trading risk"
    args_schema: Type[BaseModel] = RiskInput

    def _run(self, ticker: str, capital: float) -> str:
        try:
            llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.2)
            prompt = f"""Risk assessment for {ticker} with ${capital} capital:
            1. Position sizing (2% rule)
            2. Stop loss recommendation
            3. Risk-reward ratio
            4. Volatility analysis
            5. Risk factors"""
            response = llm.invoke(prompt)
            return response.content
        except Exception as e:
            return f"Error: {str(e)}"
