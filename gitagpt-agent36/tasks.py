"""
Tasks for the Spiritual Text Analysis Crew
Agent 36 - CrewAI Upgrade
"""

from crewai import Task


def create_text_analysis_task(agent, query):
    """
    Task for the Text Analyst agent to analyze relevant spiritual texts
    """
    return Task(
        description=f"""Analyze the following spiritual query or situation and identify
        relevant teachings from the Bhagavad Gita and other spiritual texts:

        Query: {query}

        Your task:
        1. Identify the most relevant verses or teachings from the Bhagavad Gita
        2. Explain the literal meaning of these verses
        3. Extract the core spiritual principles being taught
        4. Note any symbolic or metaphorical meanings
        5. Explain how these teachings address the query

        Provide a thorough analysis that will help others understand the spiritual wisdom.""",
        agent=agent,
        expected_output="""A detailed analysis including:
        - Relevant verse references (chapter and verse numbers)
        - Literal translations
        - Core spiritual principles
        - Symbolic interpretations
        - Connection to the query"""
    )


def create_context_task(agent, query):
    """
    Task for the Context Provider agent to provide historical and philosophical context
    """
    return Task(
        description=f"""Provide comprehensive context for the spiritual teachings related to:

        Query: {query}

        Your task:
        1. Explain the historical context of relevant Bhagavad Gita passages
        2. Describe the philosophical schools that interpret these teachings
        3. Connect to broader Vedic and Hindu philosophical traditions
        4. Explain the cultural significance of these teachings in ancient India
        5. Compare with similar teachings in other wisdom traditions if relevant

        Help deepen understanding through rich contextual knowledge.""",
        agent=agent,
        expected_output="""A comprehensive contextual analysis including:
        - Historical background
        - Philosophical interpretations across different schools
        - Cultural significance
        - Connections to broader traditions
        - Comparative insights"""
    )


def create_practical_guidance_task(agent, query):
    """
    Task for the Practical Guide agent to provide modern, actionable guidance
    """
    return Task(
        description=f"""Translate the ancient spiritual wisdom into practical, modern guidance for:

        Query: {query}

        Your task:
        1. Synthesize the insights from the textual analysis and context
        2. Explain how these teachings apply to modern life situations
        3. Provide concrete, actionable steps or practices
        4. Offer examples of how to implement this wisdom
        5. Address potential challenges in applying these teachings today

        Make the ancient wisdom accessible and immediately useful for someone living in the modern world.""",
        agent=agent,
        expected_output="""Practical guidance including:
        - Clear modern interpretation of the teachings
        - 3-5 specific actionable steps or practices
        - Real-world examples
        - How to overcome implementation challenges
        - Summary of key takeaways"""
    )


def create_all_tasks(agents, query):
    """
    Create all tasks for the crew with the given query
    """
    return [
        create_text_analysis_task(agents['text_analyst'], query),
        create_context_task(agents['context_provider'], query),
        create_practical_guidance_task(agents['practical_guide'], query)
    ]
