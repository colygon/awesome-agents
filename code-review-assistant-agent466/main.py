"""Code Review Assistant - CrewAI Implementation"""

import os
from dotenv import load_dotenv
from crewai import Crew, Process
from agents import CodeReviewAgents
from tasks import CodeReviewTasks

load_dotenv()


def review_code(code_file: str, language: str, style_guide: str = "PEP 8") -> str:
    """Perform comprehensive code review"""

    agents = CodeReviewAgents()
    tasks_factory = CodeReviewTasks()

    code_analyzer = agents.code_analyzer()
    security_reviewer = agents.security_reviewer()
    performance_reviewer = agents.performance_reviewer()
    style_checker = agents.style_checker()

    quality_task = tasks_factory.analyze_code_quality(code_analyzer, code_file, language)
    security_task = tasks_factory.review_security(security_reviewer, code_file)
    performance_task = tasks_factory.review_performance(performance_reviewer, code_file)
    style_task = tasks_factory.check_style(style_checker, code_file, style_guide)

    synthesis_task = tasks_factory.synthesize_review(code_analyzer, code_file)
    synthesis_task.context = [quality_task, security_task, performance_task, style_task]

    crew = Crew(
        agents=[code_analyzer, security_reviewer, performance_reviewer, style_checker],
        tasks=[quality_task, security_task, performance_task, style_task, synthesis_task],
        process=Process.sequential,
        verbose=True
    )

    return crew.kickoff()


def main():
    result = review_code("app.py", "Python", "PEP 8")
    print(result)


if __name__ == "__main__":
    main()
