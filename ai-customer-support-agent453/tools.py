"""
Custom Tools for AI Customer Support
Provides knowledge base search, ticket analysis, and sentiment analysis
"""

from crewai_tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field
import os
from langchain_openai import ChatOpenAI


class KnowledgeBaseInput(BaseModel):
    """Input schema for KnowledgeBaseTool"""
    query: str = Field(..., description="Search query for knowledge base")
    category: str = Field(default="all", description="Category to search within")


class KnowledgeBaseTool(BaseTool):
    name: str = "Knowledge Base Search"
    description: str = """Searches the company knowledge base for solutions, articles,
    and documentation. Returns relevant information to help resolve customer issues.
    Includes FAQs, troubleshooting guides, product documentation, and known issues."""
    args_schema: Type[BaseModel] = KnowledgeBaseInput

    def _run(self, query: str, category: str = "all") -> str:
        """
        Search knowledge base for information

        Args:
            query: Search query
            category: Optional category filter

        Returns:
            Relevant knowledge base articles
        """
        try:
            llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.2)

            prompt = f"""Search the knowledge base for information about: {query}

{f"Focus on category: {category}" if category != "all" else ""}

Provide relevant information including:

1. DIRECT ANSWER
   - Quick solution or answer to the query
   - Key points to address the issue

2. DETAILED EXPLANATION
   - Step-by-step instructions if applicable
   - Background information
   - Technical details

3. RELATED ARTICLES
   - Similar issues or questions
   - Related features or topics
   - Prerequisites or dependencies

4. TROUBLESHOOTING TIPS
   - Common causes
   - Diagnostic steps
   - Solutions and workarounds

5. ADDITIONAL RESOURCES
   - Documentation links
   - Video tutorials
   - Community discussions

Provide accurate, helpful information based on best practices for customer support."""

            response = llm.invoke(prompt)
            return response.content

        except Exception as e:
            return f"Error searching knowledge base: {str(e)}"


class TicketAnalysisInput(BaseModel):
    """Input schema for TicketAnalysisTool"""
    ticket_description: str = Field(..., description="Description of the support ticket")
    customer_history: str = Field(default="", description="Optional customer interaction history")


class TicketAnalysisTool(BaseTool):
    name: str = "Support Ticket Analyzer"
    description: str = """Analyzes support tickets to identify issue type, priority,
    root cause, and resolution strategy. Considers customer history and patterns.
    Returns structured analysis to guide support response."""
    args_schema: Type[BaseModel] = TicketAnalysisInput

    def _run(self, ticket_description: str, customer_history: str = "") -> str:
        """
        Analyze a support ticket

        Args:
            ticket_description: The ticket content
            customer_history: Optional history of customer interactions

        Returns:
            Structured ticket analysis
        """
        try:
            llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.2)

            prompt = f"""Analyze this customer support ticket:

Ticket: {ticket_description}

{f"Customer History: {customer_history}" if customer_history else ""}

Provide comprehensive analysis:

1. ISSUE CLASSIFICATION
   - Primary issue type
   - Secondary issues (if any)
   - Severity level
   - Urgency level

2. ROOT CAUSE ANALYSIS
   - Likely root cause
   - Contributing factors
   - Whether this is a known issue

3. CUSTOMER CONTEXT
   - Customer emotional state
   - Impact on customer's business/use case
   - Customer expertise level
   - Previous similar issues

4. RESOLUTION STRATEGY
   - Recommended approach
   - Estimated resolution time
   - Resources needed
   - Escalation criteria

5. PRIORITY ASSESSMENT
   - Priority level (P1-P4)
   - Justification for priority
   - SLA considerations

6. NEXT ACTIONS
   - Immediate actions required
   - Information needed from customer
   - Internal team involvement
   - Communication plan

Provide structured, actionable analysis."""

            response = llm.invoke(prompt)
            return response.content

        except Exception as e:
            return f"Error analyzing ticket: {str(e)}"


class SentimentAnalysisInput(BaseModel):
    """Input schema for SentimentAnalysisTool"""
    customer_message: str = Field(..., description="Customer message to analyze")


class SentimentAnalysisTool(BaseTool):
    name: str = "Customer Sentiment Analyzer"
    description: str = """Analyzes customer sentiment and emotional state from messages.
    Identifies frustration, urgency, satisfaction, confusion, etc. Helps tailor response
    tone and prioritize cases appropriately."""
    args_schema: Type[BaseModel] = SentimentAnalysisInput

    def _run(self, customer_message: str) -> str:
        """
        Analyze customer sentiment

        Args:
            customer_message: The customer's message

        Returns:
            Sentiment analysis results
        """
        try:
            llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.2)

            prompt = f"""Analyze the sentiment and emotional state in this customer message:

"{customer_message}"

Provide detailed sentiment analysis:

1. OVERALL SENTIMENT
   - Primary sentiment (positive/neutral/negative)
   - Sentiment score (1-10, where 1=very negative, 10=very positive)
   - Confidence level

2. EMOTIONAL INDICATORS
   - Detected emotions (frustration, confusion, anger, satisfaction, etc.)
   - Intensity of emotions
   - Emotional triggers mentioned

3. URGENCY LEVEL
   - Perceived urgency (low/medium/high/critical)
   - Indicators of urgency
   - Time sensitivity

4. CUSTOMER STATE
   - Level of frustration or patience
   - Understanding of their issue
   - Expectations expressed
   - Tone (professional, casual, aggressive, polite)

5. RESPONSE RECOMMENDATIONS
   - Appropriate tone to use in response
   - Key points to address first
   - Phrases to use or avoid
   - Whether immediate escalation is needed

6. RED FLAGS
   - Churn risk indicators
   - Legal or compliance concerns
   - Threats to reputation
   - Safety or security issues

Provide nuanced, actionable analysis."""

            response = llm.invoke(prompt)
            return response.content

        except Exception as e:
            return f"Error analyzing sentiment: {str(e)}"
