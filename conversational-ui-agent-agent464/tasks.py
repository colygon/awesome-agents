"""CrewAI Tasks for Conversational UI"""

from crewai import Task
from textwrap import dedent


class ConversationalUITasks:
    """Factory class for conversational UI tasks"""

    def classify_intent(self, agent, user_input: str) -> Task:
        return Task(
            description=dedent(f"""
                Classify user intent and extract entities from input:
                User Input: "{user_input}"

                Tasks:
                1. Identify primary intent
                2. Extract named entities
                3. Determine confidence level
                4. Identify any ambiguities
                5. Suggest clarifying questions if needed
            """),
            agent=agent,
            expected_output='Intent classification with entities and confidence scores'
        )

    def manage_dialog(self, agent, conversation_history: list) -> Task:
        return Task(
            description=dedent(f"""
                Manage dialog flow and context:
                History: {conversation_history}

                Responsibilities:
                1. Track dialog state
                2. Maintain conversation context
                3. Determine next action
                4. Handle topic switches
                5. Manage fallback strategies
            """),
            agent=agent,
            expected_output='Dialog state and recommended next action',
            context=[]
        )

    def generate_response(self, agent, user_persona: dict = None) -> Task:
        return Task(
            description=dedent(f"""
                Generate natural, helpful response:
                User Persona: {user_persona}

                Requirements:
                1. Create contextually appropriate response
                2. Match conversation tone
                3. Provide helpful information
                4. Include follow-up suggestions
                5. Maintain personality consistency
            """),
            agent=agent,
            expected_output='Natural language response with optional suggestions',
            context=[]
        )

    def design_personality(self, agent, brand_info: dict) -> Task:
        return Task(
            description=dedent(f"""
                Design conversational personality:
                Brand: {brand_info}

                Design:
                1. Define personality traits
                2. Establish tone guidelines
                3. Create response patterns
                4. Set boundaries and limitations
                5. Design error/fallback messaging
            """),
            agent=agent,
            expected_output='Comprehensive personality design guide',
            context=[]
        )
