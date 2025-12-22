"""
Customer Service Agent - Main Entry Point
CrewAI implementation of Google ADK customer service agent
"""

import os
from dotenv import load_dotenv
from crewai import Crew, Process
from agents import create_customer_service_agents
from tasks import create_customer_service_tasks

# Load environment variables
load_dotenv()


def run_customer_service(customer_message: str,
                        customer_id: str = "123",
                        customer_name: str = "Alex",
                        location: str = "Las Vegas, NV"):
    """
    Run the customer service crew to handle a customer request.

    Args:
        customer_message: The customer's support request or message
        customer_id: Customer ID for context and cart access
        customer_name: Customer name for personalization
        location: Customer location for climate-specific recommendations

    Returns:
        The final customer response with all actions taken
    """

    # Create agents
    ticket_analyzer, solution_researcher, response_generator = create_customer_service_agents()

    # Create tasks
    tasks = create_customer_service_tasks(
        customer_message=customer_message,
        customer_id=customer_id,
        customer_name=customer_name,
        location=location
    )

    # Create crew
    crew = Crew(
        agents=[ticket_analyzer, solution_researcher, response_generator],
        tasks=tasks,
        process=Process.sequential,
        verbose=True
    )

    # Execute
    try:
        result = crew.kickoff()
        return result
    except Exception as e:
        return f"Error processing customer request: {str(e)}"


def main():
    """
    Main function with example customer service interaction.
    """
    print("=== Cymbal Home & Garden Customer Service ===\n")

    # Example customer request
    customer_request = """Hi there! I just bought some plants labeled 'sun loving annuals'
    for my backyard. I totally spaced on picking up potting soil, so I'm placing an order
    for pickup now. The problem is, I'm not sure if the potting soil and fertilizer I picked
    out are the right ones for these plants. Can you help?"""

    print(f"Customer Request:\n{customer_request}\n")
    print("Processing with Customer Service Crew...\n")

    result = run_customer_service(
        customer_message=customer_request,
        customer_id="123",
        customer_name="Alex",
        location="Las Vegas, NV"
    )

    print("\n=== Customer Service Response ===")
    print(result)


if __name__ == "__main__":
    main()
