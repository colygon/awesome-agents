#!/usr/bin/env python
from crewai import Crew, Process
from agents import TradeSageAgents
from tasks import TradeSageTasks
import os
from dotenv import load_dotenv

load_dotenv()

def run_tradesage():
    """
    Run the TradeSage MVP system
    """
    print("## Welcome to TradeSage MVP")
    print("---------------------------")

    symbol = input("Enter symbol to analyze (e.g., AAPL): ").upper()
    timeframe = input("Enter timeframe (e.g., 1D, 4H): ")

    # Initialize agents and tasks
    agents = TradeSageAgents()
    tasks = TradeSageTasks()

    # Create agents
    market_agent = agents.market_analysis_agent()
    technical_agent = agents.technical_analyst_agent()
    sentiment_agent = agents.sentiment_analyst_agent()
    strategy_agent = agents.strategy_designer_agent()
    backtest_agent = agents.backtest_agent()

    # Create tasks
    market_task = tasks.analyze_market_task(market_agent, symbol, timeframe)
    signals_task = tasks.generate_signals_task(technical_agent, symbol, "RSI,MACD,MA")
    sentiment_task = tasks.analyze_sentiment_task(sentiment_agent, symbol)
    strategy_task = tasks.design_strategy_task(strategy_agent, f"{symbol} swing trading")
    backtest_task = tasks.backtest_strategy_task(backtest_agent, "{{strategy_output}}", symbol, "1Y")

    # Create crew
    crew = Crew(
        agents=[market_agent, technical_agent, sentiment_agent, strategy_agent, backtest_agent],
        tasks=[market_task, signals_task, sentiment_task, strategy_task, backtest_task],
        process=Process.sequential,
        verbose=True
    )

    # Execute
    result = crew.kickoff()

    print("\n\n########################")
    print("## TradeSage Result")
    print("########################\n")
    print(result)

    return result

if __name__ == "__main__":
    run_tradesage()
