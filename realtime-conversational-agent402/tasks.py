"""
Realtime Conversational Agent CrewAI Tasks
Defines the workflow for managing realtime conversations
"""

from crewai import Task
from agents import (
    conversation_manager,
    intent_recognizer,
    response_generator,
    knowledge_retriever
)


def create_tasks(user_message: str, conversation_history: list = None):
    """
    Create tasks for conversational workflow

    Args:
        user_message: The current message from the user
        conversation_history: List of previous conversation turns

    Returns:
        List of Task objects
    """

    if conversation_history is None:
        conversation_history = []

    # Format conversation history for context
    history_text = "\n".join([
        f"{turn['role']}: {turn['content']}"
        for turn in conversation_history[-5:]  # Last 5 turns for context
    ])

    # Task 1: Recognize user intent and extract entities
    intent_task = Task(
        description=f"""Analyze the user's message to identify their intent and extract key entities.

        User Message: "{user_message}"

        Conversation History:
        {history_text if history_text else "No previous conversation"}

        Your analysis should include:
        1. Primary Intent: What is the user trying to accomplish?
           (e.g., asking_question, requesting_action, providing_feedback, greeting, etc.)
        2. Entities: Extract any important entities (names, dates, locations, topics, etc.)
        3. Emotional Tone: Detect the emotional tone (neutral, positive, negative, urgent, etc.)
        4. Clarity: Assess if the intent is clear or if clarification is needed
        5. Context Dependencies: Identify if the message depends on previous conversation context

        Provide a structured analysis that will help generate an appropriate response.""",
        agent=intent_recognizer,
        expected_output="""A structured analysis containing:
        - Primary intent (labeled clearly)
        - List of extracted entities with types
        - Emotional tone assessment
        - Clarity level (clear/ambiguous/unclear)
        - Context dependencies (if any)
        - Recommended action (answer directly, ask clarification, retrieve information, etc.)"""
    )

    # Task 2: Retrieve relevant knowledge (if needed)
    knowledge_task = Task(
        description="""Based on the intent analysis, determine if external knowledge or
        information retrieval is needed to address the user's message.

        If the user is asking a factual question, requesting specific information, or
        needs documentation/references:
        1. Formulate appropriate search queries
        2. Identify relevant knowledge sources
        3. Retrieve and summarize relevant information
        4. Note the credibility and recency of sources

        If no external knowledge is needed (e.g., greetings, simple clarifications),
        indicate that internal knowledge is sufficient.

        Provide organized, relevant information that can be used to craft a response.""",
        agent=knowledge_retriever,
        expected_output="""Either:
        - A summary of relevant information with sources (if retrieval needed)
        - Or a note that no external knowledge retrieval is required
        Include confidence level in the information retrieved.""",
        context=[intent_task]
    )

    # Task 3: Manage conversation flow and context
    conversation_task = Task(
        description="""Manage the conversation flow based on the intent analysis and
        available knowledge.

        Consider:
        1. Conversation History: How does this message relate to previous turns?
        2. Topic Continuity: Are we continuing a topic or starting a new one?
        3. Follow-up Needs: Will the user likely need follow-up questions or clarification?
        4. Conversation State: What state is the conversation in (opening, ongoing, closing)?

        Provide recommendations for:
        - Whether to ask clarifying questions
        - How to structure the response (direct answer, options, step-by-step, etc.)
        - What context to reference from conversation history
        - Whether to suggest related topics or next steps""",
        agent=conversation_manager,
        expected_output="""Conversation management recommendations including:
        - Conversation state assessment
        - Response structure recommendation
        - Context references to include
        - Clarification needs (if any)
        - Suggested follow-up topics
        - Overall conversation strategy""",
        context=[intent_task, knowledge_task]
    )

    # Task 4: Generate appropriate response
    response_task = Task(
        description=f"""Generate a natural, contextually appropriate response to the user.

        User Message: "{user_message}"

        Based on:
        - Intent analysis
        - Retrieved knowledge (if any)
        - Conversation management recommendations

        Your response should:
        1. Directly address the user's intent
        2. Use information from knowledge retrieval if applicable
        3. Maintain appropriate tone and style
        4. Reference conversation history when relevant
        5. Be clear, concise, and helpful
        6. Ask clarifying questions if needed
        7. Suggest next steps or related topics when appropriate

        Generate a response that feels natural and conversational while being informative
        and helpful. Adapt the length and complexity based on the user's query.""",
        agent=response_generator,
        expected_output="""A conversational response that:
        - Addresses the user's message appropriately
        - Incorporates relevant information
        - Maintains natural dialogue flow
        - Includes clarifying questions or follow-ups if needed
        - Is properly formatted for easy reading""",
        context=[intent_task, knowledge_task, conversation_task]
    )

    return [intent_task, knowledge_task, conversation_task, response_task]
