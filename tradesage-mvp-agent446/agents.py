from crewai import Agent
from tools import (
    market_analyzer,
    technical_indicator_tool,
    sentiment_analyzer,
    strategy_generator,
    backtest_engine
)

class TradeSageAgents:
    def market_analysis_agent(self):
        return Agent(
            role='Market Analysis Expert',
            goal='Analyze market conditions and identify trading opportunities',
            backstory="""You are a seasoned market analyst with expertise in
            technical and fundamental analysis. You identify trends, support/resistance
            levels, and market conditions that present trading opportunities.""",
            tools=[market_analyzer, technical_indicator_tool],
            verbose=True,
            allow_delegation=True
        )

    def technical_analyst_agent(self):
        return Agent(
            role='Technical Analysis Specialist',
            goal='Apply technical indicators and chart patterns for trade signals',
            backstory="""You are an expert in technical analysis who uses indicators,
            chart patterns, and price action to generate trade signals. You understand
            RSI, MACD, moving averages, and various chart patterns.""",
            tools=[technical_indicator_tool, market_analyzer],
            verbose=True,
            allow_delegation=False
        )

    def sentiment_analyst_agent(self):
        return Agent(
            role='Market Sentiment Analyst',
            goal='Analyze market sentiment from news and social media',
            backstory="""You are a sentiment analysis expert who gauges market
            mood from news, social media, and market data. You identify bullish
            or bearish sentiment that can impact trading decisions.""",
            tools=[sentiment_analyzer],
            verbose=True,
            allow_delegation=False
        )

    def strategy_designer_agent(self):
        return Agent(
            role='Trading Strategy Designer',
            goal='Design and optimize trading strategies',
            backstory="""You are a quantitative trader who designs algorithmic
            trading strategies. You combine technical indicators, risk management,
            and market conditions to create robust trading systems.""",
            tools=[strategy_generator, technical_indicator_tool],
            verbose=True,
            allow_delegation=True
        )

    def backtest_agent(self):
        return Agent(
            role='Backtesting Specialist',
            goal='Test and validate trading strategies on historical data',
            backstory="""You are an expert in backtesting trading strategies.
            You test strategies on historical data, calculate performance metrics,
            and identify strategy strengths and weaknesses.""",
            tools=[backtest_engine, market_analyzer],
            verbose=True,
            allow_delegation=False
        )
