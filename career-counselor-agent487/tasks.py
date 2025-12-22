"""
CrewAI Tasks for Career Counselor - Agent 487
"""

from crewai import Task


def create_career_guidance_task(agent, career_situation):
    """
    Task for career advisor to provide career path guidance
    """
    return Task(
        description=f"""Provide comprehensive career guidance and planning:

        Career Situation: {career_situation}

        Your task:
        1. Assess current career situation:
           - Current role, industry, experience level
           - Skills, strengths, and competencies
           - Interests, values, and priorities
           - Career goals and aspirations
           - Challenges and constraints

        2. Explore career options:
           - Potential career paths aligned with profile
           - Industry trends and job market outlook
           - Growth potential and advancement opportunities
           - Salary ranges and compensation expectations
           - Work-life balance considerations
           - Required skills and qualifications

        3. Provide career development guidance:
           - Skills to develop or acquire
           - Education/certifications needed
           - Experience to gain
           - Timeline for transition (if applicable)
           - Steps to advance in current path

        4. Address specific situations:
           - Career change/pivot strategies
           - Returning to workforce
           - Moving up vs moving laterally
           - Industry transitions
           - Geographic considerations

        5. Create action plan:
           - Short-term goals (3-6 months)
           - Medium-term goals (1-2 years)
           - Long-term vision (3-5 years)
           - Milestones and checkpoints
           - Resources and support needed

        Provide realistic, personalized career guidance.""",
        agent=agent,
        expected_output="""Comprehensive career guidance including:
        - Career situation assessment
        - 3-5 recommended career paths with details
        - Skills gap analysis
        - Industry and market insights
        - Education/certification recommendations
        - Career development roadmap
        - Action plan with timeline
        - Resources and next steps
        - Potential challenges and solutions
        - Success metrics"""
    )


def create_resume_interview_task(agent, job_application_needs):
    """
    Task for resume/interview coach to prepare application materials
    """
    return Task(
        description=f"""Develop resume, cover letter, and interview preparation:

        Job Application Needs: {job_application_needs}

        Your task:
        1. Resume optimization:
           - Format selection (chronological/functional/combination)
           - Achievement-focused bullet points
           - Quantified accomplishments
           - ATS optimization (keywords)
           - Tailoring for target role
           - Professional summary
           - Skills section optimization
           - Addressing gaps or transitions

        2. Cover letter guidance:
           - Compelling opening
           - Value proposition
           - Company research integration
           - Specific examples
           - Call to action
           - Professional tone

        3. Interview preparation:
           - Common interview questions
           - Behavioral interview (STAR method)
           - Company research checklist
           - Questions to ask interviewer
           - Dress code guidance
           - Virtual interview tips (if applicable)
           - Follow-up strategy

        4. Salary negotiation:
           - Market research for role
           - Negotiation strategies
           - Total compensation considerations
           - When and how to negotiate
           - Handling offer discussions

        5. Application strategy:
           - How to apply (online, referral, direct)
           - Follow-up timing
           - Tracking applications
           - Multiple interview rounds

        Provide actionable, specific guidance.""",
        agent=agent,
        expected_output="""Complete application package including:
        - Resume template/structure
        - Achievement bullet point examples
        - ATS optimization keywords
        - Cover letter template
        - 15-20 interview questions with answer frameworks
        - STAR method examples
        - Company research template
        - Salary negotiation guide
        - Application tracking template
        - Follow-up email templates
        - Interview preparation checklist"""
    )


def create_job_search_strategy_task(agent, search_parameters):
    """
    Task for job search strategist to create search and networking plan
    """
    return Task(
        description=f"""Design comprehensive job search and networking strategy:

        Search Parameters: {search_parameters}

        Your task:
        1. Job search strategy:
           - Target companies identification
           - Job boards and resources to use
           - Application volume targets
           - Timeline and daily/weekly activities
           - Passive vs active search approach
           - Tracking and organization system

        2. LinkedIn optimization:
           - Profile headline optimization
           - About section compelling story
           - Experience descriptions (achievement-focused)
           - Skills and endorsements strategy
           - Recommendations approach
           - Content sharing plan
           - Profile photo and banner

        3. Networking plan:
           - Identify networking opportunities
           - Informational interview strategy
           - Networking events (virtual/in-person)
           - Alumni network utilization
           - Professional associations
           - Networking scripts and templates
           - Relationship maintenance plan

        4. Personal branding:
           - Professional value proposition
           - Online presence audit
           - Thought leadership opportunities
           - Portfolio/website (if applicable)
           - Social media guidelines
           - Elevator pitch development

        5. Job search tactics:
           - Hidden job market access
           - Referral strategies
           - Recruiter relationships
           - Company direct applications
           - Startup vs corporate strategies
           - Remote work opportunities

        6. Momentum and motivation:
           - Weekly activity goals
           - Accountability measures
           - Dealing with rejection
           - Celebrating small wins
           - When to adjust strategy

        Create actionable, sustainable job search plan.""",
        agent=agent,
        expected_output="""Complete job search strategy including:
        - Target company list (20-30 companies)
        - Job search resources by industry
        - Weekly activity plan
        - LinkedIn profile optimization guide
        - Networking action plan
        - Informational interview templates
        - Personal brand statement
        - Elevator pitch (30/60/90 second versions)
        - Email templates (networking, follow-up)
        - Application tracking system
        - 30/60/90 day search milestones
        - Motivation and accountability plan"""
    )


def create_all_tasks(agents, career_request):
    """
    Create all tasks for the career counseling crew

    Args:
        agents: Dictionary of created agents
        career_request: Can be dict with 'career_situation', 'application_needs', 'search_parameters'
                       or string for general career inquiry
    """
    # Handle both dict and string inputs
    if isinstance(career_request, dict):
        career = career_request.get('career_situation', 'Career exploration and planning')
        application = career_request.get('application_needs', 'Resume and interview preparation')
        search = career_request.get('search_parameters', 'Job search strategy')
    else:
        career = application = search = career_request

    return [
        create_career_guidance_task(agents['career_advisor'], career),
        create_resume_interview_task(agents['resume_interview_coach'], application),
        create_job_search_strategy_task(agents['job_search_strategist'], search)
    ]
