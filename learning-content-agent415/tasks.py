"""
Learning Content System CrewAI Tasks
"""

from crewai import Task
from agents import (
    curriculum_designer,
    content_creator,
    assessment_designer,
    learning_experience_designer,
    quality_reviewer
)


def create_tasks(course_info: dict):
    """Create tasks for learning content creation"""

    subject = course_info.get('subject', 'General')
    level = course_info.get('level', 'Intermediate')
    duration = course_info.get('duration', '4 weeks')

    design_curriculum_task = Task(
        description=f"""Design curriculum for {subject} course at {level} level.

        Duration: {duration}
        Target audience: {course_info.get('audience', 'General learners')}

        Create:
        1. Course overview and learning objectives
        2. Module breakdown with topics
        3. Learning progression and prerequisites
        4. Estimated time per module
        5. Assessment strategy""",
        agent=curriculum_designer,
        expected_output="Complete curriculum design with modules and objectives"
    )

    create_content_task = Task(
        description=f"""Create learning content for {subject} course.

        For each module, develop:
        1. Introduction and context
        2. Core concepts with explanations
        3. Examples and case studies
        4. Practice activities
        5. Summary and key takeaways""",
        agent=content_creator,
        expected_output="Detailed learning content for all modules",
        context=[design_curriculum_task]
    )

    design_assessments_task = Task(
        description=f"""Design assessments for {subject} course.

        Create:
        1. Formative assessments (quizzes, checks)
        2. Summative assessments (exams, projects)
        3. Rubrics and grading criteria
        4. Answer keys and feedback templates""",
        agent=assessment_designer,
        expected_output="Complete assessment package",
        context=[design_curriculum_task, create_content_task]
    )

    design_activities_task = Task(
        description=f"""Design learning activities for {subject} course.

        Create:
        1. Interactive exercises
        2. Discussion prompts
        3. Collaborative projects
        4. Real-world applications""",
        agent=learning_experience_designer,
        expected_output="Engaging learning activities",
        context=[design_curriculum_task, create_content_task]
    )

    review_quality_task = Task(
        description=f"""Review quality of {subject} course content.

        Check:
        1. Alignment with objectives
        2. Content accuracy and clarity
        3. Assessment validity
        4. Accessibility and inclusivity
        5. Overall course coherence""",
        agent=quality_reviewer,
        expected_output="Quality review report with recommendations",
        context=[design_curriculum_task, create_content_task, design_assessments_task, design_activities_task]
    )

    return [design_curriculum_task, create_content_task, design_assessments_task, design_activities_task, review_quality_task]
