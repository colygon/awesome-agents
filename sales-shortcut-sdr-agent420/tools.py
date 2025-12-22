"""SalesShortcut SDR Tools"""

from crewai_tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field
from langchain_openai import ChatOpenAI
import os
import requests


class LeadResearchInput(BaseModel):
    company_name: str = Field(..., description="Company name to research")
    industry: str = Field(..., description="Industry")


class LeadResearchTool(BaseTool):
    name: str = "Lead Research Tool"
    description: str = "Researches companies and prospects for sales outreach"
    args_schema: Type[BaseModel] = LeadResearchInput

    def _run(self, company_name: str, industry: str) -> str:
        try:
            serper_api_key = os.getenv("SERPER_API_KEY")

            if serper_api_key:
                url = "https://google.serper.dev/search"
                headers = {"X-API-KEY": serper_api_key, "Content-Type": "application/json"}
                queries = [
                    f"{company_name} company news recent",
                    f"{company_name} leadership team executives",
                    f"{industry} challenges pain points"
                ]

                results = []
                for query in queries:
                    response = requests.post(url, json={"q": query, "num": 5}, headers=headers)
                    if response.status_code == 200:
                        for item in response.json().get("organic", []):
                            results.append(f"{item.get('title')}: {item.get('snippet')}")

                return "\n".join(results)

            # Fallback
            llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.3)
            prompt = f"""Research {company_name} in {industry}:
            1. Company overview
            2. Recent news and initiatives
            3. Potential pain points
            4. Key decision makers (typical titles)
            5. Buying signals"""
            response = llm.invoke(prompt)
            return response.content
        except Exception as e:
            return f"Error: {str(e)}"


class EmailGenInput(BaseModel):
    prospect_info: str = Field(..., description="Prospect information")
    value_prop: str = Field(..., description="Value proposition")


class EmailGeneratorTool(BaseTool):
    name: str = "Email Generator Tool"
    description: str = "Generates personalized sales emails"
    args_schema: Type[BaseModel] = EmailGenInput

    def _run(self, prospect_info: str, value_prop: str) -> str:
        try:
            llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.6)
            prompt = f"""Write personalized sales email:

            Prospect: {prospect_info}
            Value: {value_prop}

            Create:
            1. 3 subject line options
            2. Personalized opening (reference research)
            3. Pain point identification
            4. Brief value prop (1-2 sentences)
            5. Clear CTA

            Keep under 125 words. No fluff."""
            response = llm.invoke(prompt)
            return response.content
        except Exception as e:
            return f"Error: {str(e)}"


class SequenceInput(BaseModel):
    campaign_goal: str = Field(..., description="Campaign goal")
    duration: int = Field(default=21, description="Sequence duration in days")


class OutreachSequenceTool(BaseTool):
    name: str = "Outreach Sequence Tool"
    description: str = "Designs multi-touch outreach sequences"
    args_schema: Type[BaseModel] = SequenceInput

    def _run(self, campaign_goal: str, duration: int = 21) -> str:
        try:
            llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.4)
            prompt = f"""Design {duration}-day outreach sequence for: {campaign_goal}

            Create sequence with:
            1. 6-8 touchpoints
            2. Mix of channels (email, LinkedIn, phone)
            3. Increasing value in each touch
            4. Timing between touches
            5. Goal for each touchpoint"""
            response = llm.invoke(prompt)
            return response.content
        except Exception as e:
            return f"Error: {str(e)}"
