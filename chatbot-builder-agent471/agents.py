from crewai import Agent
from tools import ChatbotDesignTools, ConversationFlowTools, IntegrationTools

class ChatbotBuilderAgents:
    def conversation_designer(self):
        return Agent(
            role='Conversation Designer',
            goal='Design engaging and natural conversation flows for chatbots',
            backstory="""You are an expert in conversation design and UX writing.
            You understand how to create chatbot dialogues that feel natural, helpful,
            and user-friendly. You excel at designing conversation paths, handling
            edge cases, and creating personality-driven responses.""",
            tools=[
                ChatbotDesignTools.analyze_user_intent,
                ChatbotDesignTools.generate_responses,
                ChatbotDesignTools.design_conversation_tree
            ],
            verbose=True,
            allow_delegation=False
        )

    def nlp_specialist(self):
        return Agent(
            role='NLP Specialist',
            goal='Implement natural language understanding and intent recognition',
            backstory="""You are a natural language processing expert who specializes
            in understanding user intent, entity extraction, and context management.
            You design systems that can accurately interpret user messages and
            handle variations in how people express themselves.""",
            tools=[
                ChatbotDesignTools.analyze_user_intent,
                ConversationFlowTools.extract_entities,
                ConversationFlowTools.classify_intent
            ],
            verbose=True,
            allow_delegation=False
        )

    def integration_specialist(self):
        return Agent(
            role='Integration Specialist',
            goal='Connect chatbot to external services and APIs',
            backstory="""You are an expert in integrating chatbots with various
            platforms, APIs, and services. You know how to connect chatbots to
            messaging platforms, databases, CRMs, and other business tools to
            create powerful automated workflows.""",
            tools=[
                IntegrationTools.setup_webhook,
                IntegrationTools.connect_api,
                IntegrationTools.configure_platform
            ],
            verbose=True,
            allow_delegation=False
        )

    def response_optimizer(self):
        return Agent(
            role='Response Optimizer',
            goal='Optimize chatbot responses for clarity, engagement, and effectiveness',
            backstory="""You are a chatbot optimization specialist who refines
            bot responses to be clear, engaging, and effective. You analyze
            conversation patterns, identify areas for improvement, and craft
            responses that drive user satisfaction and goal completion.""",
            tools=[
                ChatbotDesignTools.generate_responses,
                ConversationFlowTools.analyze_conversation_metrics
            ],
            verbose=True,
            allow_delegation=False
        )
