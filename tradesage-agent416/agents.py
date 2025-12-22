"""
TradeSage AI CrewAI Agents
Multi-agent trading and investment analysis system
"""

from crewai import Agent
from tools import MarketDataTool, TechnicalAnalysisTool, RiskAssessmentTool

market_analyst = Agent(
    role="Market Research Analyst",
    goal="Analyze market trends, news, and fundamental factors",
    backstory="""You are an expert market analyst with deep understanding of financial
    markets, economic indicators, and company fundamentals. You excel at analyzing
    market trends, identifying opportunities, and assessing macroeconomic factors.""",
    verbose=True,
    allow_delegation=False,
    tools=[MarketDataTool()]
)

technical_analyst = Agent(
    role="Technical Analysis Specialist",
    goal="Perform technical analysis using charts, indicators, and patterns",
    backstory="""You are a technical analysis expert skilled in chart patterns, technical
    indicators, support/resistance levels, and trading signals. You can identify trends,
    reversals, and entry/exit points.""",
    verbose=True,
    allow_delegation=False,
    tools=[TechnicalAnalysisTool()]
)

risk_manager = Agent(
    role="Risk Management Specialist",
    goal="Assess and manage trading risks",
    backstory="""You are a risk management expert who evaluates position sizing, stop
    losses, risk-reward ratios, and portfolio diversification. You ensure prudent
    risk management in trading strategies.""",
    verbose=True,
    allow_delegation=False,
    tools=[RiskAssessmentTool()]
)

strategy_developer = Agent(
    role="Trading Strategy Developer",
    goal="Develop and optimize trading strategies",
    backstory="""You are a trading strategy expert who combines fundamental and technical
    analysis to create robust trading strategies. You understand different trading styles
    and can optimize strategies for various market conditions.""",
    verbose=True,
    allow_delegation=False
)

portfolio_advisor = Agent(
    role="Portfolio Advisory Specialist",
    goal="Provide portfolio recommendations and allocation advice",
    backstory="""You are a portfolio management expert who creates balanced, diversified
    investment portfolios aligned with risk tolerance and goals. You understand asset
    allocation, rebalancing, and long-term wealth building.""",
    verbose=True,
    allow_delegation=False
)
