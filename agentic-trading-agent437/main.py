"""Agentic Trading - CrewAI Multi-Agent Trading System"""
import os, sys
from datetime import datetime
from dotenv import load_dotenv
from crewai import Crew, Process
from agents import create_market_analyst, create_strategy_developer, create_risk_manager
from tasks import create_market_analysis_task, create_strategy_task, create_risk_management_task

def load_environment():
    load_dotenv()
    if not os.getenv('OPENAI_API_KEY'):
        print("ERROR: OPENAI_API_KEY not found.")
        sys.exit(1)

def run_trading_system(market_data: dict):
    analyst = create_market_analyst()
    developer = create_strategy_developer()
    manager = create_risk_manager()

    analysis_task = create_market_analysis_task(analyst, market_data)
    strategy_task = create_strategy_task(developer, analysis_task)
    risk_task = create_risk_management_task(manager, analysis_task, strategy_task)

    crew = Crew(agents=[analyst, developer, manager], tasks=[analysis_task, strategy_task, risk_task], process=Process.sequential, verbose=True)
    return {'result': crew.kickoff(), 'timestamp': datetime.now().isoformat()}

def main():
    load_environment()
    result = run_trading_system({'symbol': 'BTC/USD', 'timeframe': '1h'})
    print(f"\n\nTRADING RESULTS\n{result['result']}")

if __name__ == "__main__":
    main()
