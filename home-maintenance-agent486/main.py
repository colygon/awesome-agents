"""
Home Maintenance - Agent 486 CrewAI Integration
Main orchestration file for home repair, maintenance, and improvement multi-agent system
"""

import os
from dotenv import load_dotenv
from crewai import Crew, Process
from agents import create_all_agents
from tasks import create_all_tasks

# Load environment variables
load_dotenv()


def create_home_maintenance_crew(home_request):
    """
    Create and configure the home maintenance crew
    """
    # Create the three specialized agents
    agents = create_all_agents(model="gpt-4", temperature=0.7)

    # Create tasks for each agent
    tasks = create_all_tasks(agents, home_request)

    # Create the crew with sequential process
    crew = Crew(
        agents=list(agents.values()),
        tasks=tasks,
        process=Process.sequential,
        verbose=True
    )

    return crew


def get_home_maintenance_help(home_request):
    """
    Get comprehensive home maintenance guidance using the CrewAI multi-agent system

    Args:
        home_request: Dictionary or string with home issue, maintenance needs, or project plans

    Returns:
        Complete home care package with repair guidance, maintenance schedule, and project plan
    """
    print("\n" + "="*80)
    print("HOME MAINTENANCE - AGENT 486 CREWAI SYSTEM")
    print("="*80)
    print(f"\nHome Request: {home_request}\n")
    print("="*80 + "\n")

    # Create and run the crew
    crew = create_home_maintenance_crew(home_request)
    result = crew.kickoff()

    print("\n" + "="*80)
    print("HOME MAINTENANCE GUIDANCE COMPLETE")
    print("="*80 + "\n")

    return result


if __name__ == "__main__":
    # Example usage
    if not os.getenv("OPENAI_API_KEY"):
        print("Error: OPENAI_API_KEY not found in environment variables.")
        print("Please create a .env file with your OpenAI API key.")
    else:
        # Test with sample home maintenance request
        sample_request = {
            "home_info": {
                "type": "Single-family home",
                "age": "15 years",
                "size": "2,200 sq ft",
                "location": "Pacific Northwest",
                "features": "2 bathrooms, forced air heating, central AC, wood deck"
            },

            "repair": """The master bathroom toilet keeps running after flushing.
                        Also, there's a slow leak under the kitchen sink that's causing
                        the cabinet to warp. Upstairs bedroom outlet doesn't work.""",

            "maintenance": """Need help creating a year-round maintenance schedule.
                             Haven't been keeping up with regular tasks and want to get
                             organized. Especially concerned about HVAC and preventing
                             issues before they become expensive.""",

            "improvement": """Planning to remodel the guest bathroom - want to replace
                             old tub with walk-in shower, new vanity, and update flooring.
                             Budget around $8,000-$12,000. Not sure what I can DIY vs
                             hire out. Also considering deck refinishing this summer."""
        }

        result = get_home_maintenance_help(sample_request)
        print("\nHome Maintenance Plan:")
        print(result)
