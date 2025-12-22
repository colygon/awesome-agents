"""TradeSage AI CrewAI Tasks"""

from crewai import Task
from agents import market_analyst, technical_analyst, risk_manager, strategy_developer, portfolio_advisor


def create_tasks(ticker: str, capital: float):
    """Create trading analysis tasks"""

    analyze_market_task = Task(
        description=f"""Analyze market conditions for {ticker}.
        Research fundamentals, news, sector trends, and economic factors.
        Provide market outlook and key insights.""",
        agent=market_analyst,
        expected_output="Market analysis report with trends and outlook"
    )

    technical_analysis_task = Task(
        description=f"""Perform technical analysis on {ticker}.
        Analyze price charts, indicators (RSI, MACD, MA), support/resistance,
        and identify trading signals.""",
        agent=technical_analyst,
        expected_output="Technical analysis with entry/exit signals",
        context=[analyze_market_task]
    )

    assess_risk_task = Task(
        description=f"""Assess trading risks for {ticker}.
        Calculate position size for ${capital} capital, recommend stop loss,
        evaluate risk-reward ratio, and identify risk factors.""",
        agent=risk_manager,
        expected_output="Risk assessment with position sizing recommendations",
        context=[analyze_market_task, technical_analysis_task]
    )

    develop_strategy_task = Task(
        description=f"""Develop trading strategy for {ticker}.
        Combine fundamental and technical analysis, define entry/exit rules,
        timeframe, and strategy rationale.""",
        agent=strategy_developer,
        expected_output="Complete trading strategy with rules",
        context=[analyze_market_task, technical_analysis_task, assess_risk_task]
    )

    portfolio_advice_task = Task(
        description=f"""Provide portfolio advice for {ticker} with ${capital} capital.
        Recommend allocation, diversification, and portfolio construction.""",
        agent=portfolio_advisor,
        expected_output="Portfolio recommendations",
        context=[analyze_market_task, technical_analysis_task, assess_risk_task, develop_strategy_task]
    )

    return [analyze_market_task, technical_analysis_task, assess_risk_task, develop_strategy_task, portfolio_advice_task]
