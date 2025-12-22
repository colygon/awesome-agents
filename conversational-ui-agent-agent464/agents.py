"""
CrewAI Agents for Conversational UI
Specialized agents for building conversational interfaces
"""

from crewai import Agent
import os


class ConversationalUIAgents:
    """Factory class for creating conversational UI agents"""

    def __init__(self):
        self.openai_api_key = os.getenv('OPENAI_API_KEY')

    def intent_classifier(self) -> Agent:
        """Intent Classification Agent"""
        return Agent(
            role='Intent Classification Specialist',
            goal='Accurately classify user intents and extract entities from conversational input',
            backstory='You are an NLP expert specializing in intent recognition and entity extraction for conversational AI systems.',
            verbose=True,
            allow_delegation=False,
            tools=[],
            llm='gpt-4o'
        )

    def dialog_manager(self) -> Agent:
        """Dialog Management Agent"""
        return Agent(
            role='Dialog Management Specialist',
            goal='Manage conversation flow, context, and state to create natural, coherent interactions',
            backstory='You excel at dialog state tracking and managing multi-turn conversations with context awareness.',
            verbose=True,
            allow_delegation=False,
            tools=[],
            llm='gpt-4o'
        )

    def response_generator(self) -> Agent:
        """Response Generation Agent"""
        return Agent(
            role='Response Generation Specialist',
            goal='Generate natural, contextually appropriate responses that engage users effectively',
            backstory='You are a conversational AI specialist who creates human-like, helpful responses tailored to user needs.',
            verbose=True,
            allow_delegation=False,
            tools=[],
            llm='gpt-4o'
        )

    def personality_designer(self) -> Agent:
        """Personality Design Agent"""
        return Agent(
            role='Conversational Personality Designer',
            goal='Design and maintain consistent conversational personality and tone across interactions',
            backstory='You specialize in creating engaging, brand-aligned conversational personalities that users connect with.',
            verbose=True,
            allow_delegation=False,
            tools=[],
            llm='gpt-4o'
        )
