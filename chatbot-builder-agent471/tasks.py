from crewai import Task
from textwrap import dedent

class ChatbotBuilderTasks:
    def design_conversation_flow(self, agent, chatbot_config):
        return Task(
            description=dedent(f"""
                Design a comprehensive conversation flow for the chatbot with the following specifications:

                Chatbot Configuration:
                {chatbot_config}

                Your tasks:
                1. Identify main conversation paths and user intents
                2. Design conversation tree with branches for different scenarios
                3. Create fallback responses for unrecognized intents
                4. Define context management strategy
                5. Design welcome and goodbye messages
                6. Plan for common edge cases and error handling

                Provide a detailed conversation flow diagram and script.
            """),
            agent=agent,
            expected_output="Detailed conversation flow design with dialogue trees, intent mapping, and sample responses"
        )

    def implement_nlp_logic(self, agent, chatbot_config):
        return Task(
            description=dedent(f"""
                Implement natural language processing logic for the chatbot:

                Chatbot Configuration:
                {chatbot_config}

                Your tasks:
                1. Define all possible user intents
                2. Create training phrases for each intent
                3. Set up entity extraction for key information
                4. Implement context tracking across conversation turns
                5. Design intent classification logic
                6. Handle variations and synonyms in user input

                Provide intent definitions, entity schemas, and NLP configuration.
            """),
            agent=agent,
            expected_output="Complete NLP implementation with intent definitions, entity schemas, training data, and classification logic"
        )

    def setup_integrations(self, agent, integration_requirements):
        return Task(
            description=dedent(f"""
                Set up all necessary integrations for the chatbot:

                Integration Requirements:
                {integration_requirements}

                Your tasks:
                1. Configure platform integrations (Slack, WhatsApp, web, etc.)
                2. Set up API connections for external services
                3. Configure webhooks for event handling
                4. Implement authentication and security
                5. Set up data persistence and logging
                6. Test all integration endpoints

                Provide integration configuration and setup documentation.
            """),
            agent=agent,
            expected_output="Complete integration setup with configuration files, API connections, and deployment instructions"
        )

    def optimize_responses(self, agent, conversation_data):
        return Task(
            description=dedent(f"""
                Optimize chatbot responses based on conversation data:

                Conversation Data:
                {conversation_data}

                Your tasks:
                1. Analyze conversation metrics and user feedback
                2. Identify responses that need improvement
                3. Rewrite responses for clarity and engagement
                4. Add personality and brand voice to responses
                5. Optimize for different user segments
                6. Create A/B test variations for key responses

                Provide optimized response scripts and improvement recommendations.
            """),
            agent=agent,
            expected_output="Optimized response scripts with improvements, personalization strategies, and A/B test recommendations"
        )

    def generate_chatbot_documentation(self, agent, chatbot_details):
        return Task(
            description=dedent(f"""
                Create comprehensive documentation for the chatbot:

                Chatbot Details:
                {chatbot_details}

                Your tasks:
                1. Document all conversation flows and intents
                2. Create user guide for chatbot interactions
                3. Write deployment and maintenance guide
                4. Document integration setup and configuration
                5. Create troubleshooting guide
                6. Provide analytics and monitoring recommendations

                Provide complete chatbot documentation.
            """),
            agent=agent,
            expected_output="Comprehensive chatbot documentation including user guides, technical documentation, and maintenance procedures"
        )
