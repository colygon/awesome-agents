"""
Pet Care Assistant - Agent 485 CrewAI Integration
Main orchestration file for comprehensive pet care multi-agent system
"""

import os
from dotenv import load_dotenv
from crewai import Crew, Process
from agents import create_all_agents
from tasks import create_all_tasks

# Load environment variables
load_dotenv()


def create_pet_care_crew(pet_care_request):
    """
    Create and configure the pet care crew
    """
    # Create the three specialized agents
    agents = create_all_agents(model="gpt-4", temperature=0.7)

    # Create tasks for each agent
    tasks = create_all_tasks(agents, pet_care_request)

    # Create the crew with sequential process
    crew = Crew(
        agents=list(agents.values()),
        tasks=tasks,
        process=Process.sequential,
        verbose=True
    )

    return crew


def get_pet_care_advice(pet_care_request):
    """
    Get comprehensive pet care guidance using the CrewAI multi-agent system

    Args:
        pet_care_request: Dictionary or string with pet info and care questions

    Returns:
        Complete pet care package with health guidance, training plan, and care routine
    """
    print("\n" + "="*80)
    print("PET CARE ASSISTANT - AGENT 485 CREWAI SYSTEM")
    print("="*80)
    print(f"\nPet Care Request: {pet_care_request}\n")
    print("="*80 + "\n")

    # Create and run the crew
    crew = create_pet_care_crew(pet_care_request)
    result = crew.kickoff()

    print("\n" + "="*80)
    print("PET CARE GUIDANCE COMPLETE")
    print("="*80 + "\n")

    return result


if __name__ == "__main__":
    # Example usage
    if not os.getenv("OPENAI_API_KEY"):
        print("Error: OPENAI_API_KEY not found in environment variables.")
        print("Please create a .env file with your OpenAI API key.")
    else:
        # Test with sample pet care request
        sample_request = {
            "pet_info": {
                "species": "dog",
                "breed": "Golden Retriever",
                "age": "8 months",
                "weight": "45 lbs",
                "name": "Max"
            },

            "health": """Max seems to have itchy skin and is scratching a lot, especially
                        behind his ears. Also wondering about the best food for his age and
                        how much exercise he needs. He's very energetic!""",

            "behavior": """Max jumps on guests when they arrive and pulls on the leash during
                          walks. Also working on basic commands - he knows 'sit' but struggles
                          with 'stay' and recall. Sometimes gets overly excited and mouthy.""",

            "care_routine": """Both my partner and I work full-time. Need help creating a
                              daily routine including feeding schedule, exercise, training time,
                              and managing his energy. Also planning a road trip next month -
                              need travel tips."""
        }

        result = get_pet_care_advice(sample_request)
        print("\nPet Care Guidance:")
        print(result)
