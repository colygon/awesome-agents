"""
Custom Tools for Email Management
"""

from crewai_tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field
from langchain_openai import ChatOpenAI


class EmailClassifierInput(BaseModel):
    email_content: str = Field(..., description="Email content to classify")


class EmailClassifierTool(BaseTool):
    name: str = "Email Classifier"
    description: str = "Classifies emails by type, priority, and action needed"
    args_schema: Type[BaseModel] = EmailClassifierInput

    def _run(self, email_content: str) -> str:
        try:
            llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.2)
            prompt = f"""Classify this email:

{email_content}

Provide:
- Type: inquiry/request/notification/marketing/etc
- Priority: urgent/high/normal/low
- Action: reply/forward/archive/delete
- Sentiment: positive/neutral/negative
- Response time: immediate/today/this week/none"""
            return llm.invoke(prompt).content
        except Exception as e:
            return f"Error classifying email: {str(e)}"


class DraftGeneratorInput(BaseModel):
    email_content: str = Field(..., description="Original email")
    tone: str = Field(default="professional", description="Response tone")


class DraftGeneratorTool(BaseTool):
    name: str = "Email Draft Generator"
    description: str = "Generates professional email responses"
    args_schema: Type[BaseModel] = DraftGeneratorInput

    def _run(self, email_content: str, tone: str = "professional") -> str:
        try:
            llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.5)
            prompt = f"""Draft a {tone} email response to:

{email_content}

Provide:
- Subject line
- Full response
- Key points addressed
- Call to action (if needed)"""
            return llm.invoke(prompt).content
        except Exception as e:
            return f"Error generating draft: {str(e)}"


class PriorityAnalyzerTool(BaseTool):
    name: str = "Email Priority Analyzer"
    description: str = "Analyzes email priority and urgency"
    args_schema: Type[BaseModel] = EmailClassifierInput

    def _run(self, email_content: str) -> str:
        try:
            llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.2)
            prompt = f"""Analyze priority of:

{email_content}

Consider:
- Time sensitivity
- Sender importance
- Impact of delay
- Dependencies

Provide priority score (1-10) and justification."""
            return llm.invoke(prompt).content
        except Exception as e:
            return f"Error analyzing priority: {str(e)}"
