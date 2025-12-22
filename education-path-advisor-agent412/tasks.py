"""
Education Path Advisor CrewAI Tasks
Defines the workflow for personalized education guidance
"""

from crewai import Task
from agents import (
    student_analyst,
    career_researcher,
    education_expert,
    stream_advisor,
    roadmap_creator
)


def create_tasks(student_info: dict):
    """
    Create tasks for education path advisory workflow

    Args:
        student_info: Dictionary containing:
            - name: Student name
            - grade: Current grade (e.g., "10th", "12th")
            - board: Education board (CBSE, ICSE, State)
            - subjects: Current subjects
            - marks: Academic performance
            - interests: Areas of interest
            - budget: Family budget for education
            - location: City/state

    Returns:
        List of Task objects
    """

    grade = student_info.get('grade', '10th')
    name = student_info.get('name', 'Student')
    interests = student_info.get('interests', '')
    marks = student_info.get('marks', '')

    # Task 1: Analyze Student Profile
    analyze_profile_task = Task(
        description=f"""Analyze the student profile for {name} (Grade {grade}).

        Student Information:
        - Current Grade: {grade}
        - Board: {student_info.get('board', 'Not specified')}
        - Current Subjects: {student_info.get('subjects', 'Not specified')}
        - Academic Performance: {marks}
        - Interests: {interests}
        - Extracurricular Activities: {student_info.get('activities', 'Not specified')}
        - Location: {student_info.get('location', 'India')}
        - Budget: {student_info.get('budget', 'Not specified')}

        Provide comprehensive analysis:
        1. Academic Strengths (subjects/areas where student excels)
        2. Interest Areas (based on stated interests and activities)
        3. Learning Style and Aptitude
        4. Potential Career Aptitudes (analytical, creative, social, technical, etc.)
        5. Gaps or Areas Needing Development
        6. Unique Strengths or Talents

        Consider the Indian education context and competitive landscape.""",
        agent=student_analyst,
        expected_output="""Detailed student profile analysis including:
        - Academic strengths and performance assessment
        - Interest and aptitude mapping
        - Career aptitude indicators
        - Development areas
        - Unique selling points"""
    )

    # Task 2: Research Career Options
    research_careers_task = Task(
        description=f"""Research and identify suitable career paths for {name} based on the profile analysis.

        Focus on:
        1. Careers aligned with interests: {interests}
        2. Careers matching academic strengths
        3. High-growth careers in India (2025 and beyond)
        4. Traditional and emerging career options
        5. Realistic options based on academic performance
        6. Careers considering location and budget constraints

        For each career path (recommend 8-12 options), provide:
        - Career title and description
        - Why it's suitable for this student
        - Required qualifications and educational path
        - Typical salary range in India (entry to senior level)
        - Growth prospects and job market demand
        - Key skills required
        - Pros and cons

        Include diverse options across sectors (IT, Engineering, Medicine, Commerce,
        Arts, Humanities, Social Sciences, Design, Media, etc.).""",
        agent=career_researcher,
        expected_output="""Comprehensive career options report with 8-12 careers including:
        - Career description and suitability
        - Educational requirements
        - Salary ranges and growth prospects
        - Required skills
        - Pros and cons for each option""",
        context=[analyze_profile_task]
    )

    # Task 3: Recommend Academic Streams and Institutions
    recommend_education_task = Task(
        description=f"""Recommend academic streams and educational institutions for {name} (Grade {grade}).

        Based on career options identified, provide:

        1. Stream Recommendations (if Grade 10th):
           - Science (PCM/PCB/PCMB) with reasons
           - Commerce (with/without Maths) with reasons
           - Arts/Humanities with subject combinations
           - Vocational/Skill-based programs
           - Recommended subject combinations for each stream

        2. Education Pathways:
           - Undergraduate programs required for shortlisted careers
           - Entrance exams needed (JEE, NEET, CLAT, CUET, etc.)
           - Top institutions (IITs, NITs, IIMs, Medical colleges, etc.)
           - Alternative quality institutions (state universities, private colleges)
           - Distance/Online education options if relevant

        3. Entrance Exam Details:
           - Exam pattern and syllabus
           - Difficulty level and competition
           - Recommended preparation timeline
           - Coaching requirements (optional vs necessary)

        4. Financial Considerations:
           - Fee structures (government vs private)
           - Scholarship opportunities
           - Education loans
           - Options within budget: {student_info.get('budget', 'Not specified')}

        Provide specific institution names, exam dates (general timeline), and
        realistic admission chances based on current performance.""",
        agent=education_expert,
        expected_output="""Educational pathway guide including:
        - Stream recommendations with subject combinations
        - Required undergraduate programs
        - Entrance exams with preparation details
        - Top 10-15 institutions (tier-wise)
        - Fee structures and financial options
        - Admission timeline and requirements""",
        context=[analyze_profile_task, research_careers_task]
    )

    # Task 4: Advise on Stream Selection (if applicable)
    if grade.lower() in ['10th', '10']:
        stream_selection_task = Task(
            description=f"""Provide detailed stream selection advice for {name} after 10th standard.

            Create a comprehensive comparison:

            1. Science Stream:
               - PCM (Physics, Chemistry, Maths): Career options, difficulty, coaching needs
               - PCB (Physics, Chemistry, Biology): Medical/life sciences paths
               - PCMB: Flexibility and workload considerations
               - Who should choose and why

            2. Commerce Stream:
               - With Maths: CA, Economics, Business Analytics paths
               - Without Maths: BBA, Law, Humanities combinations
               - Who should choose and why

            3. Arts/Humanities:
               - Subject combinations (Psychology, Sociology, Political Science, etc.)
               - Career paths (Law, Journalism, Design, Social Work, Civil Services)
               - Who should choose and why

            4. Vocational/Skill Courses:
               - ITI courses, Polytechnic, Skill development programs
               - When to consider

            Based on {name}'s profile:
            - Primary recommendation with strong justification
            - Alternative option
            - Subject combination suggestions
            - Schools/colleges to target in {student_info.get('location', 'your area')}

            Address common concerns and misconceptions about each stream.""",
            agent=stream_advisor,
            expected_output="""Stream selection guide with:
            - Detailed comparison of all streams
            - Primary recommendation with justification
            - Subject combination suggestions
            - School/college recommendations
            - Common misconceptions addressed""",
            context=[analyze_profile_task, research_careers_task, recommend_education_task]
        )
        tasks_list = [analyze_profile_task, research_careers_task, recommend_education_task, stream_selection_task]
    else:
        tasks_list = [analyze_profile_task, research_careers_task, recommend_education_task]

    # Task 5: Create Actionable Roadmap
    create_roadmap_task = Task(
        description=f"""Create a detailed, actionable educational roadmap for {name}.

        Develop a comprehensive plan with:

        1. Immediate Actions (Next 3 months):
           - Subject focus areas
           - Study schedule recommendations
           - Entrance exam registration (if applicable)
           - Coaching institute enrollment (if needed)
           - Skill development activities

        2. Short-term Goals (6-12 months):
           - Academic milestones (board exams, entrance exams)
           - Preparation timeline for competitive exams
           - Application deadlines for colleges
           - Recommended online courses or certifications
           - Extracurricular activities to pursue

        3. Medium-term Goals (1-3 years):
           - Undergraduate program completion
           - Internship opportunities
           - Skill enhancement
           - Networking and professional development

        4. Long-term Goals (3-5 years):
           - Career entry points
           - Higher education (if needed)
           - Professional certifications
           - Career progression milestones

        5. Resources and Support:
           - Recommended books and study materials
           - Online resources and platforms
           - Coaching institutes (with locations and fee ranges)
           - Scholarship application timelines
           - Mentorship opportunities

        6. Backup Plans:
           - Alternative career paths
           - What if entrance exams don't go well
           - Lateral entry options

        Create a timeline chart with specific months/years and milestones.
        Make it realistic, actionable, and tailored to {name}'s profile.""",
        agent=roadmap_creator,
        expected_output="""Comprehensive educational roadmap including:
        - Immediate actions (3 months)
        - Short-term goals (6-12 months) with timeline
        - Medium-term goals (1-3 years)
        - Long-term goals (3-5 years)
        - Resources and study materials
        - Backup plans and alternatives
        - Milestone chart with deadlines""",
        context=tasks_list
    )

    tasks_list.append(create_roadmap_task)
    return tasks_list
