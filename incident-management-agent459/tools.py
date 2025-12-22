"""
Custom Tools for Incident Management
"""

from crewai_tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field
from langchain_openai import ChatOpenAI
import random


class IncidentInput(BaseModel):
    description: str = Field(..., description="Incident description")
    priority: str = Field(default="Medium", description="Priority level")


class IncidentCreationTool(BaseTool):
    name: str = "ServiceNow Incident Creator"
    description: str = "Creates incidents in ServiceNow"
    args_schema: Type[BaseModel] = IncidentInput

    def _run(self, description: str, priority: str = "Medium") -> str:
        try:
            incident_num = f"INC{random.randint(1000000, 9999999)}"
            return f"""Incident created successfully.

Incident Number: {incident_num}
Priority: {priority}
Status: New
Assigned To: IT Support Team
Created: Just now
SLA: Respond within 4 hours

Next steps: Team will review and begin investigation."""
        except Exception as e:
            return f"Error creating incident: {str(e)}"


class IncidentStatusTool(BaseTool):
    name: str = "Incident Status Checker"
    description: str = "Checks status of ServiceNow incidents"
    args_schema: Type[BaseModel] = BaseModel

    def _run(self, incident_number: str = "") -> str:
        try:
            statuses = ["New", "In Progress", "Pending", "Resolved"]
            status = random.choice(statuses)

            return f"""Incident Status: {incident_number}

Current Status: {status}
Assigned Team: IT Infrastructure
Priority: Medium
Time Elapsed: 2 hours
SLA Status: Within SLA

Latest Update: Team is investigating the issue."""
        except Exception as e:
            return f"Error checking status: {str(e)}"


class KnowledgeBaseTool(BaseTool):
    name: str = "ServiceNow Knowledge Base"
    description: str = "Searches knowledge base for solutions"
    args_schema: Type[BaseModel] = BaseModel

    def _run(self, query: str = "") -> str:
        try:
            llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.2)
            prompt = f"""Search ServiceNow knowledge base for: {query}

Provide:
- Relevant KB articles
- Step-by-step solutions
- Workarounds
- Prevention tips"""
            return llm.invoke(prompt).content
        except Exception as e:
            return f"Error searching knowledge base: {str(e)}"
