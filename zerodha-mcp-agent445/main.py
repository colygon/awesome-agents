#!/usr/bin/env python
from crewai import Crew, Process
from agents import ZerodhaMCPAgents
from tasks import ZerodhaMCPTasks
import os
from dotenv import load_dotenv

load_dotenv()

def run_zerodha_mcp():
    """
    Run the Zerodha MCP integration system
    """
    print("## Welcome to the Zerodha MCP Integration")
    print("------------------------------------------")

    print("\nSelect operation:")
    print("1. Fetch market data")
    print("2. Execute order")
    print("3. Analyze portfolio")
    print("4. Check risk")

    choice = input("Enter choice (1-4): ")

    # Initialize agents and tasks
    agents = ZerodhaMCPAgents()
    tasks = ZerodhaMCPTasks()

    # Create agents
    market_agent = agents.market_data_agent()
    order_agent = agents.order_management_agent()
    portfolio_agent = agents.portfolio_agent()
    risk_agent = agents.risk_management_agent()
    mcp_agent = agents.mcp_integration_agent()

    # Create tasks based on choice
    if choice == '1':
        symbols = input("Enter symbols (comma-separated): ")
        task_list = [
            tasks.fetch_market_data_task(market_agent, symbols),
            tasks.integrate_mcp_task(mcp_agent, f"market_data:{symbols}")
        ]
        agent_list = [market_agent, mcp_agent]
    elif choice == '2':
        order_details = input("Enter order details (symbol quantity price): ")
        task_list = [
            tasks.execute_order_task(order_agent, order_details),
            tasks.manage_risk_task(risk_agent, order_details)
        ]
        agent_list = [order_agent, risk_agent]
    elif choice == '3':
        task_list = [
            tasks.analyze_portfolio_task(portfolio_agent),
            tasks.manage_risk_task(risk_agent, "current_positions")
        ]
        agent_list = [portfolio_agent, risk_agent]
    else:
        task_list = [
            tasks.manage_risk_task(risk_agent, "all_positions")
        ]
        agent_list = [risk_agent]

    # Create crew
    crew = Crew(
        agents=agent_list,
        tasks=task_list,
        process=Process.sequential,
        verbose=True
    )

    # Execute
    result = crew.kickoff()

    print("\n\n########################")
    print("## Zerodha MCP Result")
    print("########################\n")
    print(result)

    return result

if __name__ == "__main__":
    run_zerodha_mcp()
