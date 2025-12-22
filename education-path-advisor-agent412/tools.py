"""
Custom Tools for Education Path Advisory
Provides student analysis, career research, and education system navigation
"""

from crewai_tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field
import os
import requests
from langchain_openai import ChatOpenAI


class StudentProfileInput(BaseModel):
    """Input schema for StudentProfileAnalyzer"""
    profile_data: str = Field(..., description="Student profile information as text")


class StudentProfileAnalyzer(BaseTool):
    name: str = "Student Profile Analyzer"
    description: str = """Analyzes student academic performance, interests, and background
    to identify strengths, aptitudes, and potential career alignments. Returns comprehensive
    profile assessment."""
    args_schema: Type[BaseModel] = StudentProfileInput

    def _run(self, profile_data: str) -> str:
        """
        Analyze student profile and identify strengths and aptitudes

        Args:
            profile_data: Student information text

        Returns:
            Detailed profile analysis
        """
        try:
            llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.3)

            prompt = f"""Analyze this Indian student's profile and provide comprehensive assessment:

Student Information:
{profile_data}

Provide detailed analysis:

1. ACADEMIC STRENGTHS:
   - Subject-wise performance analysis
   - Strongest areas and why
   - Academic patterns and trends

2. APTITUDE INDICATORS:
   - Analytical aptitude (Science, Maths, Engineering)
   - Creative aptitude (Design, Arts, Media)
   - Social aptitude (Teaching, Social Work, HR)
   - Technical aptitude (IT, Programming, Electronics)
   - Business aptitude (Commerce, Management, Entrepreneurship)

3. INTEREST ALIGNMENT:
   - How interests match with academic performance
   - Genuine passions vs casual interests
   - Extracurricular activities significance

4. LEARNING STYLE:
   - Visual, Auditory, Kinesthetic preferences
   - Self-study vs guided learning
   - Theory vs practical orientation

5. COMPETITIVE READINESS:
   - Readiness for competitive exams (JEE, NEET, etc.)
   - Discipline and consistency level
   - Pressure handling capability

6. UNIQUE STRENGTHS:
   - Special talents or achievements
   - Differentiating factors
   - Leadership or initiative examples

7. DEVELOPMENT AREAS:
   - Subjects/skills needing improvement
   - Gaps to address
   - Recommended focus areas

Consider Indian education context, board systems, and competitive landscape.
Be specific and actionable."""

            response = llm.invoke(prompt)
            return response.content

        except Exception as e:
            return f"Error analyzing student profile: {str(e)}"


class CareerResearchInput(BaseModel):
    """Input schema for CareerPathResearcher"""
    student_summary: str = Field(..., description="Summary of student strengths and interests")
    grade_level: str = Field(..., description="Current grade level")


class CareerPathResearcher(BaseTool):
    name: str = "Career Path Researcher"
    description: str = """Researches career options in the Indian job market. Identifies
    careers aligned with student profile, provides salary ranges, growth prospects, and
    educational requirements. Returns comprehensive career options report."""
    args_schema: Type[BaseModel] = CareerResearchInput

    def _run(self, student_summary: str, grade_level: str) -> str:
        """
        Research suitable career paths for Indian students

        Args:
            student_summary: Student profile summary
            grade_level: Current grade

        Returns:
            Detailed career options report
        """
        try:
            serper_api_key = os.getenv("SERPER_API_KEY")

            # Use LLM to generate comprehensive career options
            llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.4)

            prompt = f"""Research and recommend suitable careers for an Indian student.

Student Profile Summary:
{student_summary}

Current Grade: {grade_level}

Provide 10-12 diverse career options covering:

For EACH career option, provide:

1. CAREER TITLE and Brief Description
2. WHY SUITABLE for this student (specific alignment with profile)
3. EDUCATIONAL PATH:
   - Required stream (Science/Commerce/Arts)
   - Undergraduate degree(s)
   - Postgraduate (if needed)
   - Professional certifications
4. ENTRANCE EXAMS (if applicable):
   - JEE, NEET, CLAT, CAT, GATE, etc.
5. TOP INSTITUTIONS in India:
   - 3-5 premier institutions
6. SALARY RANGE in India:
   - Entry level (0-3 years): ₹X - ₹Y lakhs/year
   - Mid-level (5-10 years): ₹X - ₹Y lakhs/year
   - Senior level (10+ years): ₹X - ₹Y lakhs/year
7. JOB MARKET & GROWTH:
   - Current demand in India (2025)
   - Future prospects (next 5-10 years)
   - Emerging opportunities
8. KEY SKILLS REQUIRED:
   - Technical skills
   - Soft skills
9. PROS and CONS:
   - 3-4 pros
   - 3-4 cons
10. TYPICAL JOB ROLES

Include mix of:
- Traditional careers (Engineering, Medicine, Law, etc.)
- Emerging careers (AI/ML, Data Science, Cybersecurity, etc.)
- Creative careers (Design, Media, Arts)
- Business careers (Management, Finance, Entrepreneurship)
- Service careers (Civil Services, Teaching, Social Work)

Be specific to Indian context with accurate salary figures (in lakhs per annum).
Consider current job market trends in India."""

            response = llm.invoke(prompt)
            return response.content

        except Exception as e:
            return f"Error researching careers: {str(e)}"


class EducationSystemInput(BaseModel):
    """Input schema for IndianEducationSystemTool"""
    career_field: str = Field(..., description="Career field or stream to research")
    budget: str = Field(default="moderate", description="Budget category: low, moderate, or high")


class IndianEducationSystemTool(BaseTool):
    name: str = "Indian Education System Navigator"
    description: str = """Provides information about Indian educational institutions,
    entrance exams, admission processes, and scholarships for specific career paths.
    Returns detailed education pathway information."""
    args_schema: Type[BaseModel] = EducationSystemInput

    def _run(self, career_field: str, budget: str = "moderate") -> str:
        """
        Research Indian education system for specific career field

        Args:
            career_field: Career field or stream
            budget: Budget category

        Returns:
            Education pathway information
        """
        try:
            llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.2)

            prompt = f"""Provide comprehensive information about educational pathways in India for {career_field}.

Budget Category: {budget}

Provide detailed information on:

1. STREAM REQUIREMENTS:
   - Required stream after 10th (Science/Commerce/Arts)
   - Specific subject combinations needed
   - Optional vs mandatory subjects

2. ENTRANCE EXAMS:
   For each relevant exam:
   - Exam name and conducting body
   - Exam pattern (MCQ/subjective, sections, marking)
   - Syllabus overview
   - Difficulty level and competition statistics
   - Exam dates (general timeline in academic year)
   - Preparation time needed (months)
   - Coaching necessary or optional
   - Top coaching institutes in India

3. PREMIER INSTITUTIONS (Tier 1):
   List top 10-15 institutions with:
   - Institution name and location
   - Cutoff scores/ranks (approximate)
   - Fee structure (per year)
   - Placement statistics (average package)
   - Reputation and ranking

4. GOOD ALTERNATIVES (Tier 2):
   List 10-15 quality institutions:
   - Government colleges/universities
   - Reputable private institutions
   - State universities
   - Fee ranges
   - Placement prospects

5. BUDGET-FRIENDLY OPTIONS:
   Considering {budget} budget:
   - Government institutions (low fees)
   - State quota advantages
   - Distance/Online programs
   - Part-time options

6. SCHOLARSHIPS:
   - National scholarships (NSP, Merit-based)
   - Minority scholarships
   - State government scholarships
   - Institution-specific scholarships
   - Private scholarships
   - Eligibility criteria

7. ADMISSION PROCESS:
   - Timeline (application to admission)
   - Required documents
   - Counseling process
   - Seat allotment rounds
   - Important deadlines

8. FINANCIAL PLANNING:
   - Total cost estimate (4 years undergraduate)
   - Education loan options
   - Bank schemes for students
   - Collateral requirements

Provide specific, actionable information relevant to Indian students in 2025.
Use accurate fee ranges and realistic admission statistics."""

            response = llm.invoke(prompt)
            return response.content

        except Exception as e:
            return f"Error researching education system: {str(e)}"
