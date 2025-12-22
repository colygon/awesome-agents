"""LineBot ADK - CrewAI Task Definitions"""

from crewai import Task
from textwrap import dedent


def create_conversation_design_task(agent, bot_purpose: str) -> Task:
    return Task(
        description=dedent(f"""
            Design conversation flows for a LINE bot with the following purpose:
            {bot_purpose}

            Create comprehensive conversation designs including:
            1. User intents and expected inputs
            2. Bot responses and dialogue flows
            3. Error handling and fallback strategies
            4. Rich menu structure and quick replies
            5. Personality and tone guidelines
        """),
        expected_output="Detailed conversation flow document with user journeys, sample dialogues, and interaction patterns.",
        agent=agent
    )


def create_bot_development_task(agent, conversation_design_output, bot_purpose: str) -> Task:
    return Task(
        description=dedent(f"""
            Implement LINE bot functionality based on conversation design:
            {conversation_design_output}

            Purpose: {bot_purpose}

            Provide complete implementation including:
            1. Webhook handler code
            2. Message processing logic
            3. Rich menu and Flex Message templates
            4. Database schema and models
            5. Configuration and deployment setup
        """),
        expected_output="Complete bot implementation code with all necessary files and configurations.",
        agent=agent,
        context=[conversation_design_output] if isinstance(conversation_design_output, Task) else []
    )


def create_ux_optimization_task(agent, conversation_design_output, bot_development_output) -> Task:
    return Task(
        description=dedent(f"""
            Optimize user experience for the LINE bot:

            Conversation Design: {conversation_design_output}
            Implementation: {bot_development_output}

            Provide UX optimization recommendations:
            1. Usability improvements
            2. Engagement enhancement strategies
            3. Analytics and metrics to track
            4. A/B testing opportunities
            5. Accessibility considerations
        """),
        expected_output="UX optimization report with specific recommendations and implementation guidance.",
        agent=agent,
        context=[conversation_design_output, bot_development_output] if isinstance(conversation_design_output, Task) else []
    )
