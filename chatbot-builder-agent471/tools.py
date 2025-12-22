from crewai_tools import tool
import json
from typing import Dict, List, Any

class ChatbotDesignTools:
    @tool("Analyze User Intent")
    def analyze_user_intent(message: str) -> str:
        """
        Analyzes user message to identify intent and confidence.
        Useful for understanding what users are trying to achieve.
        """
        # Simulated intent analysis
        common_intents = {
            "greeting": ["hello", "hi", "hey", "good morning"],
            "help": ["help", "assist", "support", "problem"],
            "question": ["what", "how", "why", "when", "where"],
            "feedback": ["like", "dislike", "love", "hate", "good", "bad"],
            "goodbye": ["bye", "goodbye", "see you", "later"]
        }

        message_lower = message.lower()
        detected_intents = []

        for intent, keywords in common_intents.items():
            if any(keyword in message_lower for keyword in keywords):
                detected_intents.append(intent)

        return json.dumps({
            "message": message,
            "detected_intents": detected_intents if detected_intents else ["unknown"],
            "confidence": 0.85 if detected_intents else 0.3
        }, indent=2)

    @tool("Generate Responses")
    def generate_responses(intent: str) -> str:
        """
        Generates appropriate chatbot responses for a given intent.
        Useful for creating response variations.
        """
        response_templates = {
            "greeting": [
                "Hello! How can I help you today?",
                "Hi there! What can I do for you?",
                "Welcome! I'm here to assist you."
            ],
            "help": [
                "I'd be happy to help! What do you need assistance with?",
                "I'm here to support you. Can you tell me more about your issue?",
                "Let me help you with that. Please provide more details."
            ],
            "unknown": [
                "I'm not sure I understand. Could you rephrase that?",
                "I didn't quite catch that. Can you provide more details?",
                "That's interesting! Can you tell me more?"
            ],
            "goodbye": [
                "Goodbye! Have a great day!",
                "See you later! Feel free to come back anytime.",
                "Take care! I'm always here if you need help."
            ]
        }

        responses = response_templates.get(intent, response_templates["unknown"])

        return json.dumps({
            "intent": intent,
            "response_variations": responses,
            "count": len(responses)
        }, indent=2)

    @tool("Design Conversation Tree")
    def design_conversation_tree(use_case: str) -> str:
        """
        Designs a conversation tree structure for a specific use case.
        Useful for mapping out conversation flows.
        """
        tree_template = {
            "root": {
                "node": "Welcome",
                "message": "Hello! How can I help you today?",
                "children": [
                    {
                        "node": "Product Inquiry",
                        "message": "What would you like to know about our products?",
                        "children": [
                            {"node": "Pricing", "message": "Our pricing starts at..."},
                            {"node": "Features", "message": "Here are the key features..."},
                            {"node": "Availability", "message": "Let me check availability..."}
                        ]
                    },
                    {
                        "node": "Support Request",
                        "message": "I'll help you with your issue. Can you describe the problem?",
                        "children": [
                            {"node": "Technical Issue", "message": "Let me troubleshoot..."},
                            {"node": "Account Issue", "message": "I can help with your account..."},
                            {"node": "Billing Issue", "message": "Let me connect you to billing..."}
                        ]
                    },
                    {
                        "node": "General Question",
                        "message": "Sure, what would you like to know?",
                        "children": []
                    }
                ]
            }
        }

        return json.dumps({
            "use_case": use_case,
            "conversation_tree": tree_template,
            "total_nodes": 10
        }, indent=2)


class ConversationFlowTools:
    @tool("Extract Entities")
    def extract_entities(message: str) -> str:
        """
        Extracts entities like dates, numbers, names from user messages.
        Useful for capturing structured information.
        """
        import re

        entities = {
            "numbers": re.findall(r'\b\d+\b', message),
            "emails": re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', message),
            "dates": re.findall(r'\b\d{1,2}/\d{1,2}/\d{2,4}\b', message),
            "phone_numbers": re.findall(r'\b\d{3}[-.]?\d{3}[-.]?\d{4}\b', message)
        }

        return json.dumps({
            "message": message,
            "extracted_entities": entities,
            "entity_count": sum(len(v) for v in entities.values())
        }, indent=2)

    @tool("Classify Intent")
    def classify_intent(message: str) -> str:
        """
        Classifies user message into predefined intent categories.
        Useful for routing conversations.
        """
        intent_keywords = {
            "booking": ["book", "reserve", "schedule", "appointment"],
            "cancellation": ["cancel", "refund", "return"],
            "information": ["tell", "what", "how", "when", "where"],
            "complaint": ["problem", "issue", "not working", "broken"],
            "praise": ["great", "excellent", "love", "amazing"]
        }

        message_lower = message.lower()
        classified_intent = "general"
        confidence = 0.5

        for intent, keywords in intent_keywords.items():
            if any(keyword in message_lower for keyword in keywords):
                classified_intent = intent
                confidence = 0.85
                break

        return json.dumps({
            "message": message,
            "intent": classified_intent,
            "confidence": confidence
        }, indent=2)

    @tool("Analyze Conversation Metrics")
    def analyze_conversation_metrics(conversation_id: str) -> str:
        """
        Analyzes metrics for a conversation to identify optimization opportunities.
        Useful for improving chatbot performance.
        """
        metrics = {
            "conversation_id": conversation_id,
            "total_messages": 12,
            "avg_response_time": "1.2s",
            "user_satisfaction": 4.2,
            "goal_completion": True,
            "intents_detected": ["greeting", "question", "question", "confirmation", "goodbye"],
            "fallback_rate": 0.08,
            "conversation_duration": "4m 32s"
        }

        return json.dumps(metrics, indent=2)


class IntegrationTools:
    @tool("Setup Webhook")
    def setup_webhook(platform: str) -> str:
        """
        Sets up webhook configuration for a messaging platform.
        Useful for receiving messages from external platforms.
        """
        webhook_config = {
            "platform": platform,
            "webhook_url": f"https://api.chatbot.example.com/webhook/{platform}",
            "events": ["message.received", "message.sent", "user.joined"],
            "authentication": "bearer_token",
            "status": "configured"
        }

        return json.dumps(webhook_config, indent=2)

    @tool("Connect API")
    def connect_api(api_name: str) -> str:
        """
        Establishes connection to an external API service.
        Useful for integrating third-party services.
        """
        api_config = {
            "api_name": api_name,
            "endpoint": f"https://api.{api_name.lower()}.com/v1",
            "authentication": "api_key",
            "rate_limit": "1000 requests/hour",
            "status": "connected",
            "available_methods": ["GET", "POST", "PUT", "DELETE"]
        }

        return json.dumps(api_config, indent=2)

    @tool("Configure Platform")
    def configure_platform(platform_name: str) -> str:
        """
        Configures chatbot for deployment on a specific platform.
        Useful for multi-platform chatbot deployment.
        """
        platform_config = {
            "platform": platform_name,
            "supported_features": ["text", "images", "buttons", "quick_replies"],
            "max_message_length": 2000,
            "deployment_url": f"https://{platform_name.lower()}.chatbot.example.com",
            "status": "ready"
        }

        return json.dumps(platform_config, indent=2)
