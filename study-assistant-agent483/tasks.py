"""
CrewAI Tasks for Study Assistant - Agent 483
"""

from crewai import Task


def create_content_explanation_task(agent, learning_request):
    """
    Task for content explainer to teach concepts
    """
    return Task(
        description=f"""Explain the academic topic in a clear, comprehensive way:

        Learning Request: {learning_request}

        Your task:
        1. Break down the topic into core concepts
        2. Explain each concept clearly using:
           - Simple language (avoid jargon, or define when necessary)
           - Concrete examples and real-world applications
           - Analogies to familiar concepts
           - Visual descriptions (when helpful)
           - Step-by-step reasoning
        3. Build from fundamentals to advanced concepts
        4. Address common misconceptions
        5. Provide practice problems or thought exercises
        6. Suggest related topics to explore
        7. Check for understanding with review questions

        Make the explanation engaging and accessible.""",
        agent=agent,
        expected_output="""A comprehensive explanation including:
        - Clear breakdown of core concepts
        - Multiple examples and analogies
        - Step-by-step explanations
        - Common misconceptions addressed
        - Practice problems (3-5)
        - Review questions for self-assessment
        - Related topics for further study
        - Summary of key takeaways"""
    )


def create_study_plan_task(agent, study_needs):
    """
    Task for study planner to create learning schedule
    """
    return Task(
        description=f"""Create an effective study plan based on learning needs:

        Study Needs: {study_needs}

        Your task:
        1. Assess the scope of material to cover
        2. Identify time available and constraints
        3. Create a realistic study schedule including:
           - Daily/weekly study sessions
           - Subject rotation and interleaving
           - Spaced repetition schedule for review
           - Active recall practice sessions
           - Rest and break periods
        4. Prioritize topics by:
           - Difficulty level
           - Importance (exam weight, prerequisites)
           - Current understanding
        5. Incorporate evidence-based techniques:
           - Pomodoro sessions (25 min focus, 5 min break)
           - Active recall over passive reading
           - Spaced repetition intervals
        6. Build in flexibility for adjustments
        7. Include progress checkpoints

        Design a sustainable, effective study plan.""",
        agent=agent,
        expected_output="""A detailed study plan including:
        - Week-by-week study schedule
        - Daily session breakdown (topics and duration)
        - Study technique recommendations
        - Prioritized topic list
        - Spaced repetition schedule
        - Progress checkpoints and milestones
        - Adjustment strategies
        - Tips for maintaining motivation"""
    )


def create_test_prep_task(agent, exam_details):
    """
    Task for test prep coach to prepare for exams
    """
    return Task(
        description=f"""Develop a comprehensive test preparation strategy:

        Exam Details: {exam_details}

        Your task:
        1. Analyze exam format and requirements
        2. Identify key topics likely to be tested
        3. Create practice materials:
           - Sample questions (multiple choice, short answer, essay)
           - Practice problems with solutions
           - Mock exam sections
           - Time-limited practice sets
        4. Develop test-taking strategies:
           - Time management techniques
           - Question prioritization
           - Answer elimination methods
           - Anxiety management
        5. Create a final review plan:
           - Last-week intensive review schedule
           - High-yield topics to focus on
           - Quick reference materials
        6. Provide confidence-building exercises
        7. Include day-before and day-of exam tips

        Prepare students for exam success.""",
        agent=agent,
        expected_output="""A complete test prep package including:
        - Exam analysis and topic breakdown
        - 10-20 practice questions with answers
        - Test-taking strategy guide
        - Time management plan for exam
        - Final week review schedule
        - Quick reference sheet/formula list
        - Anxiety management techniques
        - Day-of-exam checklist
        - Confidence-building tips"""
    )


def create_all_tasks(agents, study_request):
    """
    Create all tasks for the study assistant crew

    Args:
        agents: Dictionary of created agents
        study_request: Can be dict with 'topic', 'schedule_needs', 'exam_details'
                      or string for general study help
    """
    # Handle both dict and string inputs
    if isinstance(study_request, dict):
        topic = study_request.get('topic', 'General study assistance')
        schedule = study_request.get('schedule_needs', topic)
        exam = study_request.get('exam_details', topic)
    else:
        topic = schedule = exam = study_request

    return [
        create_content_explanation_task(agents['content_explainer'], topic),
        create_study_plan_task(agents['study_planner'], schedule),
        create_test_prep_task(agents['test_prep_coach'], exam)
    ]
