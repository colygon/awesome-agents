"""Conversational UI Agent - CrewAI Implementation"""

import os
from dotenv import load_dotenv
from crewai import Crew, Process
from agents import ConversationalUIAgents
from tasks import ConversationalUITasks

load_dotenv()


def create_conversational_ui(user_input: str, brand_info: dict, conversation_history: list = None) -> str:
    """Create conversational UI response"""

    agents = ConversationalUIAgents()
    tasks_factory = ConversationalUITasks()

    intent_classifier = agents.intent_classifier()
    dialog_manager = agents.dialog_manager()
    response_generator = agents.response_generator()
    personality_designer = agents.personality_designer()

    intent_task = tasks_factory.classify_intent(intent_classifier, user_input)
    dialog_task = tasks_factory.manage_dialog(dialog_manager, conversation_history or [])
    dialog_task.context = [intent_task]

    response_task = tasks_factory.generate_response(response_generator)
    response_task.context = [intent_task, dialog_task]

    personality_task = tasks_factory.design_personality(personality_designer, brand_info)

    crew = Crew(
        agents=[intent_classifier, dialog_manager, response_generator, personality_designer],
        tasks=[intent_task, dialog_task, response_task, personality_task],
        process=Process.sequential,
        verbose=True
    )

    return crew.kickoff()


def main():
    user_input = "I'm looking for a laptop under $1200 for video editing"
    brand_info = {'name': 'TechStore', 'tone': 'helpful and knowledgeable'}
    result = create_conversational_ui(user_input, brand_info)
    print(result)


if __name__ == "__main__":
    main()
