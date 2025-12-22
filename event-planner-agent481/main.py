"""
Event Planner - Agent 481 CrewAI Integration
Main orchestration file for event planning multi-agent system
"""

import os
from dotenv import load_dotenv
from crewai import Crew, Process
from agents import create_all_agents
from tasks import create_all_tasks

# Load environment variables
load_dotenv()


def create_event_planning_crew(event_details):
    """
    Create and configure the event planning crew
    """
    # Create the three specialized agents
    agents = create_all_agents(model="gpt-4", temperature=0.7)

    # Create tasks for each agent
    tasks = create_all_tasks(agents, event_details)

    # Create the crew with sequential process
    crew = Crew(
        agents=list(agents.values()),
        tasks=tasks,
        process=Process.sequential,
        verbose=True
    )

    return crew


def plan_event(event_details):
    """
    Plan an event using the CrewAI multi-agent system

    Args:
        event_details: Dictionary or string describing event requirements

    Returns:
        Comprehensive event plan including venue, schedule, and budget
    """
    print("\n" + "="*80)
    print("EVENT PLANNER - AGENT 481 CREWAI SYSTEM")
    print("="*80)
    print(f"\nEvent Details: {event_details}\n")
    print("="*80 + "\n")

    # Create and run the crew
    crew = create_event_planning_crew(event_details)
    result = crew.kickoff()

    print("\n" + "="*80)
    print("EVENT PLANNING COMPLETE")
    print("="*80 + "\n")

    return result


if __name__ == "__main__":
    # Example usage
    if not os.getenv("OPENAI_API_KEY"):
        print("Error: OPENAI_API_KEY not found in environment variables.")
        print("Please create a .env file with your OpenAI API key.")
    else:
        # Test with sample event
        sample_event = {
            "type": "Corporate Team Building Event",
            "guest_count": 50,
            "date": "June 15, 2024",
            "duration": "4 hours",
            "location": "San Francisco Bay Area",
            "budget": "$8,000 - $12,000",
            "requirements": [
                "Indoor venue with outdoor access",
                "AV equipment for presentations",
                "Catering for lunch",
                "Space for team activities",
                "Parking for 50 cars"
            ],
            "special_requests": "Team building activities and networking opportunities"
        }

        result = plan_event(sample_event)
        print("\nEvent Plan:")
        print(result)
