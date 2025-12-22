"""
Weather Advisor - Agent 484 CrewAI Integration
Main orchestration file for weather analysis and activity planning multi-agent system
"""

import os
from dotenv import load_dotenv
from crewai import Crew, Process
from agents import create_all_agents
from tasks import create_all_tasks

# Load environment variables
load_dotenv()


def create_weather_advisory_crew(weather_request):
    """
    Create and configure the weather advisory crew
    """
    # Create the three specialized agents
    agents = create_all_agents(model="gpt-4", temperature=0.7)

    # Create tasks for each agent
    tasks = create_all_tasks(agents, weather_request)

    # Create the crew with sequential process
    crew = Crew(
        agents=list(agents.values()),
        tasks=tasks,
        process=Process.sequential,
        verbose=True
    )

    return crew


def get_weather_advice(weather_request):
    """
    Get comprehensive weather advisory using the CrewAI multi-agent system

    Args:
        weather_request: Dictionary or string with location, date, and planned activities

    Returns:
        Complete weather advisory with forecast, activity recommendations, and preparation guide
    """
    print("\n" + "="*80)
    print("WEATHER ADVISOR - AGENT 484 CREWAI SYSTEM")
    print("="*80)
    print(f"\nWeather Request: {weather_request}\n")
    print("="*80 + "\n")

    # Create and run the crew
    crew = create_weather_advisory_crew(weather_request)
    result = crew.kickoff()

    print("\n" + "="*80)
    print("WEATHER ADVISORY COMPLETE")
    print("="*80 + "\n")

    return result


if __name__ == "__main__":
    # Example usage
    if not os.getenv("OPENAI_API_KEY"):
        print("Error: OPENAI_API_KEY not found in environment variables.")
        print("Please create a .env file with your OpenAI API key.")
    else:
        # Test with sample weather request
        sample_request = {
            "location": "Seattle, WA",
            "date": "This Saturday",
            "activity": """Planning an outdoor wedding ceremony and reception.
                         Ceremony at 4 PM, reception until 9 PM. 80 guests.
                         Venue has partial covered area but ceremony is outdoors.""",
            "concerns": [
                "Rain probability",
                "Temperature for guest comfort",
                "Wind (affects decorations)",
                "Backup plan timing"
            ]
        }

        result = get_weather_advice(sample_request)
        print("\nWeather Advisory:")
        print(result)
