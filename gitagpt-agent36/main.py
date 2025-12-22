"""
Gita GPT - Agent 36 CrewAI Upgrade
Main application orchestrating the spiritual text analysis crew
"""

import os
from dotenv import load_dotenv
from crewai import Crew, Process
from agents import create_all_agents
from tasks import create_all_tasks


# Load environment variables
load_dotenv()


def create_spiritual_crew(query):
    """
    Create and configure the spiritual text analysis crew
    """
    # Create the three agents
    agents = create_all_agents(model="gpt-4", temperature=0.7)

    # Create tasks for each agent
    tasks = create_all_tasks(agents, query)

    # Create the crew with sequential process
    crew = Crew(
        agents=list(agents.values()),
        tasks=tasks,
        process=Process.sequential,
        verbose=True
    )

    return crew


def analyze_spiritual_query(query):
    """
    Analyze a spiritual query using the crew of agents
    """
    print("\n" + "="*80)
    print("GITA GPT - AGENT 36 CREWAI ANALYSIS")
    print("="*80)
    print(f"\nQuery: {query}\n")
    print("="*80 + "\n")

    # Create and run the crew
    crew = create_spiritual_crew(query)
    result = crew.kickoff()

    print("\n" + "="*80)
    print("ANALYSIS COMPLETE")
    print("="*80 + "\n")

    return result


def interactive_mode():
    """
    Run the application in interactive mode
    """
    print("\n" + "="*80)
    print("Welcome to Gita GPT - Agent 36 CrewAI Edition")
    print("="*80)
    print("\nAsk questions about spiritual texts, life situations, or seek guidance.")
    print("The three-agent crew will provide deep insights and practical wisdom.\n")
    print("Type 'quit' or 'exit' to end the session.\n")
    print("="*80 + "\n")

    while True:
        try:
            query = input("\nYour question: ").strip()

            if not query:
                print("Please enter a question.")
                continue

            if query.lower() in ['quit', 'exit', 'q']:
                print("\nThank you for using Gita GPT. May wisdom guide your path.")
                break

            # Analyze the query
            result = analyze_spiritual_query(query)

            # Display the result
            print("\nFINAL WISDOM:\n")
            print(result)
            print("\n" + "="*80 + "\n")

        except KeyboardInterrupt:
            print("\n\nSession interrupted. Goodbye!")
            break
        except Exception as e:
            print(f"\nAn error occurred: {str(e)}")
            print("Please try again.\n")


def main():
    """
    Main entry point for the application
    """
    # Check for API key
    if not os.getenv("OPENAI_API_KEY"):
        print("Error: OPENAI_API_KEY not found in environment variables.")
        print("Please create a .env file with your OpenAI API key.")
        print("See .env.example for reference.")
        return

    # Run in interactive mode
    interactive_mode()


if __name__ == "__main__":
    main()
