"""
Job Interview Agent CrewAI Tasks
Defines the workflow for comprehensive interview preparation
"""

from crewai import Task
from agents import (
    resume_analyzer,
    company_researcher,
    question_generator,
    answer_coach,
    mock_interviewer
)


def create_tasks(resume_path: str, job_title: str, company_name: str):
    """
    Create tasks for interview preparation workflow

    Args:
        resume_path: Path to the candidate's resume
        job_title: Target job title/role
        company_name: Name of the company

    Returns:
        List of Task objects
    """

    # Task 1: Analyze Resume
    analyze_resume_task = Task(
        description=f"""Analyze the resume at {resume_path} for the {job_title} role.

        Extract and analyze:
        1. Key skills and technical competencies
        2. Work experience and achievements
        3. Education and certifications
        4. Projects and notable accomplishments
        5. Strengths that align with {job_title} requirements
        6. Potential gaps or areas to address in interview
        7. Unique selling points

        Provide specific examples and quantifiable achievements that can be highlighted
        during the interview.""",
        agent=resume_analyzer,
        expected_output="""Comprehensive resume analysis including:
        - List of key skills and competencies
        - Summary of work experience with achievements
        - Strengths for the target role
        - Areas to address or improve
        - Talking points for the interview"""
    )

    # Task 2: Research Company
    research_company_task = Task(
        description=f"""Research {company_name} to prepare for the interview.

        Gather information about:
        1. Company mission, vision, and values
        2. Recent news, product launches, or milestones
        3. Company culture and work environment
        4. Interview process and what they look for in candidates
        5. Key competitors and market position
        6. Technologies or methodologies they use
        7. Growth trajectory and future plans

        Identify specific talking points about why the candidate would be a good fit
        and thoughtful questions the candidate can ask interviewers.""",
        agent=company_researcher,
        expected_output="""Detailed company research report including:
        - Company overview and values
        - Recent news and developments
        - Culture and work environment insights
        - Interview process expectations
        - 5-10 thoughtful questions to ask interviewers
        - Key points about company fit"""
    )

    # Task 3: Generate Interview Questions
    generate_questions_task = Task(
        description=f"""Generate comprehensive interview questions for {job_title} at {company_name}.

        Create questions in these categories:
        1. Behavioral Questions (10-15 questions using STAR method scenarios)
        2. Technical Questions (10-15 questions based on required skills)
        3. Role-Specific Questions (8-10 questions about job responsibilities)
        4. Company Culture Fit Questions (5-8 questions)
        5. Situational/Problem-Solving Questions (5-8 scenarios)

        Ensure questions are:
        - Relevant to the specific role and seniority level
        - Aligned with company values and culture
        - Mix of common and challenging questions
        - Cover various competency areas""",
        agent=question_generator,
        expected_output="""Categorized list of interview questions:
        - Behavioral questions (STAR format)
        - Technical questions
        - Role-specific questions
        - Culture fit questions
        - Situational questions
        Total: 40-50 questions across all categories""",
        context=[analyze_resume_task, research_company_task]
    )

    # Task 4: Provide Model Answers
    provide_answers_task = Task(
        description=f"""Create model answers and coaching guidance for the interview questions.

        For each category of questions:
        1. Provide 3-5 detailed model answers using the STAR method for behavioral questions
        2. Provide structured technical answer frameworks
        3. Give tips on how to personalize answers based on the candidate's background
        4. Include dos and don'ts for each question type
        5. Suggest ways to incorporate company research into answers
        6. Provide body language and delivery tips

        Ensure answers:
        - Demonstrate relevant skills from the resume
        - Align with company values
        - Are authentic and adaptable
        - Showcase impact and results""",
        agent=answer_coach,
        expected_output="""Interview answer guide including:
        - 3-5 model STAR answers for behavioral questions
        - Technical answer frameworks and examples
        - Tips for personalizing answers
        - Communication and delivery guidance
        - Company-specific talking points to incorporate""",
        context=[analyze_resume_task, research_company_task, generate_questions_task]
    )

    # Task 5: Conduct Mock Interview
    mock_interview_task = Task(
        description=f"""Conduct a comprehensive mock interview preparation session for {job_title} at {company_name}.

        Provide guidance on:
        1. Interview structure and flow (what to expect)
        2. Opening strong - introducing yourself effectively
        3. Handling difficult questions or gaps in experience
        4. Asking thoughtful questions to interviewers
        5. Closing the interview professionally
        6. Follow-up best practices

        Create a practice plan:
        - Prioritized list of questions to practice
        - Suggested practice schedule
        - Key areas to focus on
        - Confidence-building exercises
        - Final preparation checklist

        Include specific feedback areas to monitor during practice.""",
        agent=mock_interviewer,
        expected_output="""Mock interview preparation guide:
        - Interview flow and structure overview
        - Opening and closing strategies
        - Difficult question handling techniques
        - Practice plan with prioritized questions
        - Preparation checklist
        - Confidence-building tips""",
        context=[
            analyze_resume_task,
            research_company_task,
            generate_questions_task,
            provide_answers_task
        ]
    )

    return [
        analyze_resume_task,
        research_company_task,
        generate_questions_task,
        provide_answers_task,
        mock_interview_task
    ]
