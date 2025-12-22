"""
Custom Tools for Job Interview Preparation
Provides resume analysis, company research, and question generation
"""

from crewai_tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field
import os
import requests
from langchain_community.document_loaders import PyPDFLoader, Docx2txtLoader
from langchain_openai import ChatOpenAI


class ResumeAnalysisInput(BaseModel):
    """Input schema for ResumeAnalysisTool"""
    resume_path: str = Field(..., description="Path to the resume file (PDF or DOCX)")


class ResumeAnalysisTool(BaseTool):
    name: str = "Resume Analysis Tool"
    description: str = """Analyzes resumes in PDF or DOCX format. Extracts skills, experience,
    education, achievements, and provides insights on strengths and areas for improvement.
    Returns structured analysis of the candidate's background."""
    args_schema: Type[BaseModel] = ResumeAnalysisInput

    def _run(self, resume_path: str) -> str:
        """
        Analyze a resume file and extract key information

        Args:
            resume_path: Path to the resume file

        Returns:
            Structured analysis of the resume
        """
        try:
            # Load resume based on file type
            if resume_path.lower().endswith('.pdf'):
                loader = PyPDFLoader(resume_path)
                pages = loader.load()
                resume_text = "\n\n".join([page.page_content for page in pages])
            elif resume_path.lower().endswith('.docx'):
                loader = Docx2txtLoader(resume_path)
                resume_text = loader.load()[0].page_content
            else:
                # Try to read as text file
                with open(resume_path, 'r', encoding='utf-8') as f:
                    resume_text = f.read()

            # Use LLM to extract structured information
            llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

            prompt = f"""Analyze this resume and provide a comprehensive breakdown:

1. Contact Information (name, email, phone, LinkedIn)
2. Professional Summary/Objective
3. Key Skills (categorized: technical, soft skills, tools/technologies)
4. Work Experience (for each role: company, title, dates, key achievements with metrics)
5. Education (degrees, institutions, dates, relevant coursework)
6. Certifications and Additional Qualifications
7. Projects (if mentioned)
8. Strengths (top 5 strengths for job interviews)
9. Potential Gaps or Areas to Address
10. Unique Selling Points

Resume content:
{resume_text}

Provide a well-structured analysis with clear sections."""

            response = llm.invoke(prompt)
            return response.content

        except Exception as e:
            return f"Error analyzing resume: {str(e)}"


class CompanyResearchInput(BaseModel):
    """Input schema for CompanyResearchTool"""
    company_name: str = Field(..., description="Name of the company to research")


class CompanyResearchTool(BaseTool):
    name: str = "Company Research Tool"
    description: str = """Researches companies to gather information about their culture,
    values, recent news, products, and interview processes. Useful for interview preparation."""
    args_schema: Type[BaseModel] = CompanyResearchInput

    def _run(self, company_name: str) -> str:
        """
        Research a company for interview preparation

        Args:
            company_name: Name of the company

        Returns:
            Comprehensive company research
        """
        try:
            serper_api_key = os.getenv("SERPER_API_KEY")

            if serper_api_key:
                # Use Serper API for company research
                url = "https://google.serper.dev/search"
                headers = {
                    "X-API-KEY": serper_api_key,
                    "Content-Type": "application/json"
                }

                # Multiple searches for comprehensive research
                searches = [
                    f"{company_name} company culture values mission",
                    f"{company_name} recent news 2025",
                    f"{company_name} interview process experience",
                    f"{company_name} products services technology stack"
                ]

                all_results = []
                for query in searches:
                    payload = {"q": query, "num": 5}
                    response = requests.post(url, json=payload, headers=headers)

                    if response.status_code == 200:
                        results = response.json()
                        all_results.append(f"\n### {query}\n")
                        for item in results.get("organic", []):
                            all_results.append(
                                f"**{item.get('title')}**\n"
                                f"Link: {item.get('link')}\n"
                                f"{item.get('snippet')}\n"
                            )

                if all_results:
                    # Use LLM to synthesize research
                    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
                    research_text = "\n".join(all_results)

                    prompt = f"""Based on this research about {company_name}, create a comprehensive interview preparation guide:

1. Company Overview (mission, vision, values)
2. Recent News and Developments (last 6 months)
3. Products/Services and Technology
4. Company Culture and Work Environment
5. Interview Process (what to expect)
6. Key Talking Points (why you'd be a good fit)
7. Thoughtful Questions to Ask Interviewers (8-10 questions)

Research data:
{research_text[:8000]}

Provide actionable insights for interview preparation."""

                    response = llm.invoke(prompt)
                    return response.content

            # Fallback: Provide research guidance
            return f"""Company Research Guide for {company_name}:

Research these areas before your interview:

1. Company Website:
   - About Us / Mission / Values
   - Products and Services
   - Recent blog posts or news
   - Leadership team

2. News and Media:
   - Google News: "{company_name} news"
   - Recent press releases
   - Industry articles and analysis

3. Employee Insights:
   - Glassdoor reviews
   - LinkedIn employee posts
   - Company culture information

4. Social Media:
   - LinkedIn company page
   - Twitter/X updates
   - YouTube channel

5. Financial Information (if public):
   - Recent earnings reports
   - Growth trajectory
   - Market position

6. Interview Process:
   - Glassdoor interview reviews
   - Search: "{company_name} interview experience"

Questions to Prepare:
- Why do you want to work at {company_name}?
- What do you know about our products/services?
- How do your values align with our company culture?

Note: Set SERPER_API_KEY for automated research."""

        except Exception as e:
            return f"Error researching company: {str(e)}"


class QuestionGeneratorInput(BaseModel):
    """Input schema for QuestionGeneratorTool"""
    job_title: str = Field(..., description="Job title/role")
    experience_level: str = Field(default="mid-level", description="Experience level: entry, mid-level, or senior")


class QuestionGeneratorTool(BaseTool):
    name: str = "Interview Question Generator"
    description: str = """Generates relevant interview questions for specific job roles.
    Creates behavioral, technical, and situational questions tailored to the position."""
    args_schema: Type[BaseModel] = QuestionGeneratorInput

    def _run(self, job_title: str, experience_level: str = "mid-level") -> str:
        """
        Generate interview questions for a specific role

        Args:
            job_title: The job title/role
            experience_level: Experience level (entry, mid-level, senior)

        Returns:
            Comprehensive list of interview questions
        """
        try:
            llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.7)

            prompt = f"""Generate comprehensive interview questions for a {experience_level} {job_title} position.

Create questions in these categories:

1. BEHAVIORAL QUESTIONS (12-15 questions):
   - Use STAR method scenarios
   - Cover: leadership, teamwork, conflict resolution, problem-solving, adaptability
   - Examples: "Tell me about a time when...", "Describe a situation where..."

2. TECHNICAL QUESTIONS (12-15 questions):
   - Role-specific technical skills
   - Tools, technologies, and methodologies
   - Appropriate for {experience_level} level

3. ROLE-SPECIFIC QUESTIONS (8-10 questions):
   - Day-to-day responsibilities
   - Domain knowledge
   - Industry-specific challenges

4. CULTURE FIT QUESTIONS (6-8 questions):
   - Work style and preferences
   - Values alignment
   - Team dynamics

5. SITUATIONAL/PROBLEM-SOLVING (6-8 questions):
   - Hypothetical scenarios
   - Decision-making process
   - Critical thinking

Ensure questions are:
- Relevant to {experience_level} level expectations
- Mix of common and challenging questions
- Cover various competency areas
- Appropriate difficulty

Provide questions in a clear, numbered format within each category."""

            response = llm.invoke(prompt)
            return response.content

        except Exception as e:
            return f"Error generating questions: {str(e)}"
