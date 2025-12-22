"""
Custom Tools for Realtime Conversational Agent
Provides conversation management, context memory, and response generation capabilities
"""

from crewai_tools import BaseTool
from typing import Type, Dict, List, Any
from pydantic import BaseModel, Field
import json
from datetime import datetime


class ConversationManagerInput(BaseModel):
    """Input schema for ConversationManagerTool"""
    action: str = Field(..., description="Action to perform: 'store', 'retrieve', or 'analyze'")
    data: Dict[str, Any] = Field(default={}, description="Data for the action")


class ConversationManagerTool(BaseTool):
    name: str = "Conversation Manager Tool"
    description: str = """Manages conversation state, history, and flow. Can store conversation
    turns, retrieve conversation history, and analyze conversation patterns. Use 'store' to
    save a conversation turn, 'retrieve' to get history, or 'analyze' to understand patterns."""
    args_schema: Type[BaseModel] = ConversationManagerInput

    def __init__(self):
        super().__init__()
        self.conversation_store = []  # In-memory storage for demo

    def _run(self, action: str, data: Dict[str, Any] = None) -> str:
        """
        Manage conversation data

        Args:
            action: The action to perform (store/retrieve/analyze)
            data: Data for the action

        Returns:
            Result of the operation
        """
        try:
            if data is None:
                data = {}

            if action == "store":
                # Store a conversation turn
                turn = {
                    "timestamp": datetime.now().isoformat(),
                    "role": data.get("role", "user"),
                    "content": data.get("content", ""),
                    "intent": data.get("intent"),
                    "entities": data.get("entities", [])
                }
                self.conversation_store.append(turn)
                return f"Stored conversation turn: {turn['role']} - {turn['content'][:50]}..."

            elif action == "retrieve":
                # Retrieve conversation history
                limit = data.get("limit", 10)
                history = self.conversation_store[-limit:]
                return json.dumps(history, indent=2)

            elif action == "analyze":
                # Analyze conversation patterns
                if not self.conversation_store:
                    return "No conversation history to analyze"

                total_turns = len(self.conversation_store)
                user_turns = sum(1 for t in self.conversation_store if t["role"] == "user")
                assistant_turns = total_turns - user_turns

                intents = [t.get("intent") for t in self.conversation_store if t.get("intent")]
                unique_intents = set(intents)

                analysis = f"""Conversation Analysis:
- Total turns: {total_turns}
- User messages: {user_turns}
- Assistant responses: {assistant_turns}
- Unique intents identified: {len(unique_intents)}
- Most recent intents: {intents[-5:] if intents else 'None'}
- Average turn length: {sum(len(t['content']) for t in self.conversation_store) / total_turns:.1f} characters"""

                return analysis

            else:
                return f"Unknown action: {action}. Use 'store', 'retrieve', or 'analyze'"

        except Exception as e:
            return f"Error in conversation management: {str(e)}"


class ContextMemoryInput(BaseModel):
    """Input schema for ContextMemoryTool"""
    key: str = Field(..., description="Key to store or retrieve")
    value: str = Field(default="", description="Value to store (for 'set' operation)")
    operation: str = Field(default="get", description="Operation: 'get' or 'set'")


class ContextMemoryTool(BaseTool):
    name: str = "Context Memory Tool"
    description: str = """Stores and retrieves contextual information during conversations.
    Use this to remember user preferences, facts mentioned, or ongoing topics. Operations:
    'set' to store information, 'get' to retrieve it."""
    args_schema: Type[BaseModel] = ContextMemoryInput

    def __init__(self):
        super().__init__()
        self.memory_store = {}

    def _run(self, key: str, value: str = "", operation: str = "get") -> str:
        """
        Manage context memory

        Args:
            key: The key for the memory item
            value: The value to store (for 'set' operation)
            operation: 'get' or 'set'

        Returns:
            Result of the operation
        """
        try:
            if operation == "set":
                self.memory_store[key] = {
                    "value": value,
                    "timestamp": datetime.now().isoformat()
                }
                return f"Stored '{key}': {value[:100]}..."

            elif operation == "get":
                if key in self.memory_store:
                    item = self.memory_store[key]
                    return f"{item['value']}"
                else:
                    return f"No memory found for key '{key}'"

            else:
                return f"Unknown operation: {operation}. Use 'get' or 'set'"

        except Exception as e:
            return f"Error in context memory: {str(e)}"


class ResponseGeneratorInput(BaseModel):
    """Input schema for ResponseGeneratorTool"""
    intent: str = Field(..., description="The identified user intent")
    context: str = Field(..., description="Relevant context for the response")
    style: str = Field(default="conversational", description="Response style: conversational, formal, concise, detailed")


class ResponseGeneratorTool(BaseTool):
    name: str = "Response Generator Tool"
    description: str = """Generates contextually appropriate responses based on user intent
    and conversation context. Can adapt style and tone. Provides natural, engaging responses."""
    args_schema: Type[BaseModel] = ResponseGeneratorInput

    def _run(self, intent: str, context: str, style: str = "conversational") -> str:
        """
        Generate a response template/guidelines

        Args:
            intent: The user's intent
            context: Relevant context
            style: Desired response style

        Returns:
            Response guidelines or template
        """
        try:
            style_guidelines = {
                "conversational": "Use friendly, natural language. Ask follow-up questions. Be engaging.",
                "formal": "Use professional language. Be precise and structured. Avoid casual phrases.",
                "concise": "Keep responses brief and to the point. Use bullet points if listing items.",
                "detailed": "Provide comprehensive explanations. Include examples and context."
            }

            intent_templates = {
                "asking_question": "Provide a clear answer. Offer to elaborate if needed.",
                "requesting_action": "Confirm understanding, then explain the action steps.",
                "providing_feedback": "Acknowledge the feedback. Thank the user.",
                "greeting": "Respond warmly. Ask how you can help.",
                "farewell": "Provide a friendly closing. Offer future assistance.",
                "clarification": "Ask specific questions to understand better.",
                "complaint": "Show empathy. Offer solutions or next steps."
            }

            guidelines = f"""Response Generation Guidelines:

Intent: {intent}
Style: {style}

Style Guide: {style_guidelines.get(style, style_guidelines['conversational'])}

Intent-Specific Guide: {intent_templates.get(intent, 'Address the user need directly and helpfully.')}

Context to incorporate: {context[:200]}...

Key principles:
1. Be helpful and address the user's need
2. Maintain conversation flow
3. Use appropriate tone
4. Provide clear, actionable information
5. Ask clarifying questions if needed"""

            return guidelines

        except Exception as e:
            return f"Error generating response guidelines: {str(e)}"
