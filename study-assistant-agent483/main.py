"""
Study Assistant - Agent 483 CrewAI Integration
Main orchestration file for academic learning multi-agent system
"""

import os
from dotenv import load_dotenv
from crewai import Crew, Process
from agents import create_all_agents
from tasks import create_all_tasks

# Load environment variables
load_dotenv()


def create_study_assistance_crew(study_request):
    """
    Create and configure the study assistance crew
    """
    # Create the three specialized agents
    agents = create_all_agents(model="gpt-4", temperature=0.7)

    # Create tasks for each agent
    tasks = create_all_tasks(agents, study_request)

    # Create the crew with sequential process
    crew = Crew(
        agents=list(agents.values()),
        tasks=tasks,
        process=Process.sequential,
        verbose=True
    )

    return crew


def get_study_help(study_request):
    """
    Get comprehensive study assistance using the CrewAI multi-agent system

    Args:
        study_request: Dictionary or string with learning topic, study needs, and exam details

    Returns:
        Complete study package with explanations, study plan, and test prep
    """
    print("\n" + "="*80)
    print("STUDY ASSISTANT - AGENT 483 CREWAI SYSTEM")
    print("="*80)
    print(f"\nStudy Request: {study_request}\n")
    print("="*80 + "\n")

    # Create and run the crew
    crew = create_study_assistance_crew(study_request)
    result = crew.kickoff()

    print("\n" + "="*80)
    print("STUDY ASSISTANCE COMPLETE")
    print("="*80 + "\n")

    return result


if __name__ == "__main__":
    # Example usage
    if not os.getenv("OPENAI_API_KEY"):
        print("Error: OPENAI_API_KEY not found in environment variables.")
        print("Please create a .env file with your OpenAI API key.")
    else:
        # Test with sample study request
        sample_request = {
            "topic": """Photosynthesis - I need to understand the light-dependent and
                       light-independent reactions, including the role of chlorophyll,
                       ATP production, and the Calvin cycle.""",

            "schedule_needs": """I have a biology exam in 2 weeks. I can study 1-2 hours
                                per day on weekdays and 3-4 hours on weekends. I also need
                                to cover cellular respiration and genetics.""",

            "exam_details": """The exam is 90 minutes with 40 multiple choice questions,
                             5 short answer questions, and 1 essay. Heavy emphasis on
                             photosynthesis and cellular respiration. Professor likes to
                             test on comparing/contrasting processes."""
        }

        result = get_study_help(sample_request)
        print("\nStudy Package:")
        print(result)
