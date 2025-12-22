"""
Budget Tracker - Agent 482 CrewAI Integration
Main orchestration file for personal finance management multi-agent system
"""

import os
from dotenv import load_dotenv
from crewai import Crew, Process
from agents import create_all_agents
from tasks import create_all_tasks

# Load environment variables
load_dotenv()


def create_budget_tracking_crew(financial_data):
    """
    Create and configure the budget tracking crew
    """
    # Create the three specialized agents
    agents = create_all_agents(model="gpt-4", temperature=0.7)

    # Create tasks for each agent
    tasks = create_all_tasks(agents, financial_data)

    # Create the crew with sequential process
    crew = Crew(
        agents=list(agents.values()),
        tasks=tasks,
        process=Process.sequential,
        verbose=True
    )

    return crew


def analyze_budget(financial_data):
    """
    Analyze finances and create budget using the CrewAI multi-agent system

    Args:
        financial_data: Dictionary or string with income, expenses, and goals

    Returns:
        Comprehensive financial analysis, budget plan, and savings strategies
    """
    print("\n" + "="*80)
    print("BUDGET TRACKER - AGENT 482 CREWAI SYSTEM")
    print("="*80)
    print(f"\nFinancial Data: {financial_data}\n")
    print("="*80 + "\n")

    # Create and run the crew
    crew = create_budget_tracking_crew(financial_data)
    result = crew.kickoff()

    print("\n" + "="*80)
    print("BUDGET ANALYSIS COMPLETE")
    print("="*80 + "\n")

    return result


if __name__ == "__main__":
    # Example usage
    if not os.getenv("OPENAI_API_KEY"):
        print("Error: OPENAI_API_KEY not found in environment variables.")
        print("Please create a .env file with your OpenAI API key.")
    else:
        # Test with sample financial data
        sample_data = {
            "monthly_income": 5000,
            "expenses": {
                "rent": 1500,
                "utilities": 200,
                "groceries": 400,
                "dining_out": 300,
                "transportation": 350,
                "car_insurance": 150,
                "health_insurance": 250,
                "phone": 80,
                "internet": 60,
                "streaming_services": 45,
                "gym": 50,
                "entertainment": 150,
                "clothing": 100,
                "miscellaneous": 200
            },
            "debt": {
                "credit_card": 200,
                "student_loan": 300
            },
            "current_savings": 2000,
            "financial_goals": [
                "Build 6-month emergency fund ($15,000)",
                "Save for vacation ($3,000)",
                "Pay off credit card debt"
            ]
        }

        result = analyze_budget(sample_data)
        print("\nBudget Analysis:")
        print(result)
