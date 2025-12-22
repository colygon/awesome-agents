"""
Custom tools for Career Counselor - Agent 487
(Tools for career research, resume optimization, and job search)
"""

from crewai_tools import tool


@tool("Career Path Explorer")
def explore_career_paths(interests: str, skills: str, industry: str = "any") -> str:
    """
    Explore potential career paths based on interests and skills.

    Args:
        interests: Areas of interest
        skills: Current skills and strengths
        industry: Target industry (optional)

    Returns:
        Career path recommendations with details
    """
    # Placeholder implementation
    # In production, integrate with O*NET, BLS data, or career databases
    return f"""
    Career paths for interests: {interests}, skills: {skills}, industry: {industry}

    This tool would provide:
    - 5-10 matching career paths
    - Job descriptions and responsibilities
    - Required qualifications and skills
    - Salary ranges by experience level
    - Job outlook and growth projections
    - Work environment and lifestyle
    - Career advancement paths

    Data sources:
    - O*NET (Occupational Information Network)
    - Bureau of Labor Statistics
    - LinkedIn Career Insights
    - Glassdoor salary data
    - Industry reports

    Career categories:
    - Technical (engineering, IT, data science)
    - Business (marketing, sales, operations)
    - Creative (design, content, media)
    - Healthcare
    - Education
    - Finance
    """


@tool("Resume ATS Optimizer")
def optimize_for_ats(resume_text: str, job_description: str) -> str:
    """
    Analyze resume for ATS compatibility and keyword matching.

    Args:
        resume_text: Current resume content
        job_description: Target job description

    Returns:
        ATS optimization recommendations
    """
    # Placeholder implementation
    return f"""
    ATS optimization for resume vs job description:

    This tool would analyze:
    - Keyword matching (skills, tools, technologies)
    - Format compatibility (headers, sections, fonts)
    - Missing required qualifications
    - Suggested additions
    - Readability score

    ATS-friendly practices:
    - Use standard section headers
    - Avoid images, graphics, tables
    - Use simple, clean formatting
    - Include relevant keywords naturally
    - List skills explicitly
    - Use industry-standard job titles

    Common ATS systems:
    - Workday
    - Taleo
    - Greenhouse
    - iCIMS
    - Lever
    """


@tool("Salary Research Tool")
def research_salary(job_title: str, location: str, experience_level: str) -> str:
    """
    Research salary ranges for specific role, location, and experience.

    Args:
        job_title: Job title or role
        location: City, state, or region
        experience_level: entry, mid, senior, executive

    Returns:
        Salary data and compensation insights
    """
    # Placeholder implementation
    return f"""
    Salary research for {job_title} in {location} ({experience_level} level):

    This tool would provide:
    - Salary range (25th, 50th, 75th percentile)
    - Total compensation (base + bonus + equity)
    - Regional cost of living adjustments
    - Industry variations
    - Company size impact
    - Benefits benchmarks

    Data sources:
    - Glassdoor salary database
    - levels.fyi (tech roles)
    - PayScale
    - LinkedIn Salary Insights
    - Bureau of Labor Statistics
    - Salary.com

    Considerations:
    - Remote work impact
    - Industry differences
    - Company stage (startup vs enterprise)
    - Education and certifications
    """


@tool("Interview Question Database")
def get_interview_questions(job_type: str, company_type: str, difficulty: str = "all") -> str:
    """
    Get relevant interview questions for job type and company.

    Args:
        job_type: Type of role (engineering, marketing, sales, etc.)
        company_type: startup, tech, corporate, nonprofit, etc.
        difficulty: behavioral, technical, case, situational, or "all"

    Returns:
        Interview questions with answer frameworks
    """
    # Placeholder implementation
    return f"""
    Interview questions for {job_type} at {company_type} ({difficulty}):

    This tool would provide:
    - Common behavioral questions
    - Technical/role-specific questions
    - Company culture fit questions
    - Case study or problem-solving questions
    - STAR method answer frameworks
    - Red flags in answers to avoid

    Question categories:
    - Behavioral: "Tell me about a time when..."
    - Technical: Role-specific skills assessment
    - Situational: "What would you do if..."
    - Cultural: Values and team fit
    - Motivational: "Why this role/company?"

    Resources:
    - Glassdoor interview reviews
    - LeetCode (technical roles)
    - Case interview prep (consulting)
    - Industry-specific forums
    """


@tool("LinkedIn Profile Analyzer")
def analyze_linkedin_profile(profile_summary: str, target_role: str) -> str:
    """
    Analyze LinkedIn profile and provide optimization recommendations.

    Args:
        profile_summary: Current LinkedIn profile content
        target_role: Role being targeted

    Returns:
        LinkedIn optimization recommendations
    """
    # Placeholder implementation
    return f"""
    LinkedIn profile analysis for targeting: {target_role}

    This tool would analyze:
    - Headline effectiveness
    - About section engagement
    - Experience descriptions (achievement focus)
    - Skills and endorsements relevance
    - Recommendations count and quality
    - Profile completeness score
    - Keywords for searchability

    Optimization tips:
    - Headline: Role + Value proposition (not just job title)
    - About: Story-driven, results-focused
    - Experience: Achievement bullets with metrics
    - Skills: Top 3 match target role
    - Recommendations: 3-5 from diverse sources
    - Custom URL
    - Featured section with portfolio

    LinkedIn best practices:
    - Professional photo (headshot)
    - Banner image (branded or professional)
    - Open to work (if actively searching)
    - Creator mode (for content sharing)
    - Engagement (comment, share, post)
    """


# Export tools list for easy import
career_counselor_tools = [
    explore_career_paths,
    optimize_for_ats,
    research_salary,
    get_interview_questions,
    analyze_linkedin_profile
]
