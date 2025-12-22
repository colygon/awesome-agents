"""
Custom Tools for Job Finder
"""

from crewai_tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field
from langchain_openai import ChatOpenAI
import os
import requests


class JobSearchInput(BaseModel):
    job_title: str = Field(..., description="Job title to search for")
    location: str = Field(..., description="Location for job search")
    remote: bool = Field(default=True, description="Include remote jobs")


class JobSearchTool(BaseTool):
    name: str = "Job Board Search"
    description: str = "Searches job boards for relevant opportunities"
    args_schema: Type[BaseModel] = JobSearchInput

    def _run(self, job_title: str, location: str, remote: bool = True) -> str:
        try:
            serper_key = os.getenv("SERPER_API_KEY")
            if serper_key:
                url = "https://google.serper.dev/search"
                query = f"{job_title} jobs {location} {'remote' if remote else ''}"
                payload = {"q": query, "num": 20}
                headers = {"X-API-KEY": serper_key, "Content-Type": "application/json"}
                response = requests.post(url, json=payload, headers=headers)
                if response.status_code == 200:
                    return str(response.json())

            llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.3)
            prompt = f"List typical {job_title} job opportunities in {location}"
            return llm.invoke(prompt).content
        except Exception as e:
            return f"Error searching jobs: {str(e)}"


class ResumeMatchTool(BaseTool):
    name: str = "Resume Job Matcher"
    description: str = "Matches candidate skills to job requirements"
    args_schema: Type[BaseModel] = BaseModel

    def _run(self, candidate_skills: str = "", job_description: str = "") -> str:
        try:
            llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.2)
            prompt = f"""Match candidate skills to job:

Candidate: {candidate_skills}
Job: {job_description}

Provide:
- Match percentage
- Matching skills
- Skill gaps
- Recommendations"""
            return llm.invoke(prompt).content
        except Exception as e:
            return f"Error matching resume: {str(e)}"


class CompanyResearchTool(BaseTool):
    name: str = "Company Researcher"
    description: str = "Researches companies for culture and fit"
    args_schema: Type[BaseModel] = BaseModel

    def _run(self, company_name: str = "") -> str:
        try:
            llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.3)
            prompt = f"""Research {company_name}:
- Company overview
- Culture and values
- Interview process
- Employee reviews
- Growth trajectory"""
            return llm.invoke(prompt).content
        except Exception as e:
            return f"Error researching company: {str(e)}"
