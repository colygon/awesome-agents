"""Custom Tools for Conversational UI"""

from crewai_tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field


class IntentRecognizerInput(BaseModel):
    text: str = Field(..., description="User input text")


class IntentRecognizerTool(BaseTool):
    name: str = "Intent Recognizer"
    description: str = "Classifies user intent from natural language input"
    args_schema: Type[BaseModel] = IntentRecognizerInput

    def _run(self, text: str) -> str:
        return f"Intent: information_query\\nConfidence: 0.89\\nEntities: ['product', 'price']"


class ContextTrackerInput(BaseModel):
    conversation_id: str = Field(..., description="Conversation identifier")


class ContextTrackerTool(BaseTool):
    name: str = "Context Tracker"
    description: str = "Tracks and retrieves conversation context and history"
    args_schema: Type[BaseModel] = ContextTrackerInput

    def _run(self, conversation_id: str) -> str:
        return f"Context for {conversation_id}:\\nTurns: 5\\nTopic: product_inquiry\\nEntities: ['laptop', '$1200']"
