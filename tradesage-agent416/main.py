#!/usr/bin/env python
"""TradeSage AI - CrewAI Implementation"""

import sys
from crewai import Crew, Process
from agents import market_analyst, technical_analyst, risk_manager, strategy_developer, portfolio_advisor
from tasks import create_tasks


def main():
    print("TradeSage AI - Trading Analysis System")
    print("="*60)
    print("WARNING: This is for educational purposes only. Not financial advice.\n")

    ticker = input("Stock ticker (e.g., AAPL, TSLA): ").strip().upper()
    capital_input = input("Trading capital ($): ").strip()
    capital = float(capital_input) if capital_input else 10000.0

    tasks = create_tasks(ticker, capital)
    crew = Crew(
        agents=[market_analyst, technical_analyst, risk_manager, strategy_developer, portfolio_advisor],
        tasks=tasks,
        process=Process.sequential,
        verbose=True
    )

    print(f"\nAnalyzing {ticker}...")
    result = crew.kickoff()
    print("\n" + "="*60)
    print("ANALYSIS COMPLETE")
    print("="*60)
    print(result)


if __name__ == "__main__":
    main()
