"""Tools for Customer Service"""

from crewai_tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field


class TicketAnalysisInput(BaseModel):
    message: str = Field(..., description="Customer message to analyze")


class TicketAnalysisTool(BaseTool):
    name: str = "Ticket Analysis Tool"
    description: str = "Analyzes customer tickets for category, priority, and intent"
    args_schema: Type[BaseModel] = TicketAnalysisInput

    def _run(self, message: str) -> str:
        categories = ['billing', 'technical', 'account', 'general']
        # Simple keyword matching
        category = 'general'
        if 'pay' in message.lower() or 'bill' in message.lower():
            category = 'billing'
        elif 'error' in message.lower() or 'not working' in message.lower():
            category = 'technical'
        return f"Category: {category}, Priority: Medium"


class KnowledgeBaseInput(BaseModel):
    query: str = Field(..., description="Search query for knowledge base")


class KnowledgeBaseTool(BaseTool):
    name: str = "Knowledge Base Tool"
    description: str = "Searches knowledge base for relevant articles"
    args_schema: Type[BaseModel] = KnowledgeBaseInput

    def _run(self, query: str) -> str:
        return f"KB search for: {query}\nNote: Integrate with actual knowledge base API"


class SentimentAnalysisInput(BaseModel):
    text: str = Field(..., description="Text to analyze sentiment")


class SentimentAnalysisTool(BaseTool):
    name: str = "Sentiment Analysis Tool"
    description: str = "Analyzes customer sentiment"
    args_schema: Type[BaseModel] = SentimentAnalysisInput

    def _run(self, text: str) -> str:
        negative_words = ['angry', 'frustrated', 'terrible', 'awful', 'worst']
        positive_words = ['great', 'thank', 'appreciate', 'love', 'excellent']

        sentiment = 'neutral'
        if any(word in text.lower() for word in negative_words):
            sentiment = 'negative'
        elif any(word in text.lower() for word in positive_words):
            sentiment = 'positive'

        return f"Sentiment: {sentiment}"
