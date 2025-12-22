#!/usr/bin/env python
from crewai import Crew, Process
from agents import ChatbotBuilderAgents
from tasks import ChatbotBuilderTasks
from dotenv import load_dotenv

load_dotenv()

def run_chatbot_builder():
    """
    Run the Chatbot Builder crew to design and implement a chatbot
    """
    print("## Welcome to the Chatbot Builder Crew")
    print("--------------------------------------")

    # Get user input for chatbot requirements
    chatbot_purpose = input("What is the main purpose of your chatbot? (e.g., customer support, lead generation): ")
    platform = input("Which platform(s) will the chatbot be deployed on? (e.g., website, Slack, WhatsApp): ")
    key_features = input("What key features should the chatbot have? (e.g., appointment booking, FAQ): ")

    chatbot_config = f"""
    Purpose: {chatbot_purpose}
    Platform(s): {platform}
    Key Features: {key_features}
    """

    integration_requirements = f"""
    Platforms: {platform}
    Required Integrations: CRM, Analytics, Database
    """

    conversation_data = """
    Sample conversation scenarios and user feedback
    """

    # Initialize agents
    agents = ChatbotBuilderAgents()
    tasks_manager = ChatbotBuilderTasks()

    # Create agents
    conversation_designer = agents.conversation_designer()
    nlp_specialist = agents.nlp_specialist()
    integration_specialist = agents.integration_specialist()
    response_optimizer = agents.response_optimizer()

    # Create tasks
    design_task = tasks_manager.design_conversation_flow(
        conversation_designer,
        chatbot_config
    )

    nlp_task = tasks_manager.implement_nlp_logic(
        nlp_specialist,
        chatbot_config
    )

    integration_task = tasks_manager.setup_integrations(
        integration_specialist,
        integration_requirements
    )

    optimization_task = tasks_manager.optimize_responses(
        response_optimizer,
        conversation_data
    )

    documentation_task = tasks_manager.generate_chatbot_documentation(
        conversation_designer,
        chatbot_config
    )

    # Create and run crew
    crew = Crew(
        agents=[
            conversation_designer,
            nlp_specialist,
            integration_specialist,
            response_optimizer
        ],
        tasks=[
            design_task,
            nlp_task,
            integration_task,
            optimization_task,
            documentation_task
        ],
        process=Process.sequential,
        verbose=True
    )

    result = crew.kickoff()

    print("\n\n########################")
    print("## Chatbot Builder Results")
    print("########################\n")
    print(result)

    return result


if __name__ == "__main__":
    run_chatbot_builder()
