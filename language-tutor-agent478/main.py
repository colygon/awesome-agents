#!/usr/bin/env python
from crewai import Crew, Process
from agents import LanguageTutorAgents
from tasks import LanguageTutorTasks
from dotenv import load_dotenv

load_dotenv()

def run_language_tutor():
    print("## Welcome to the Language Tutor Crew")
    print("-------------------------------------")

    language = input("Which language to learn? ")
    level = input("Current level? (beginner/intermediate/advanced): ")
    focus = input("Focus area? (grammar/conversation/vocabulary): ")

    lesson_topic = f"{language} - {focus} for {level} learners"

    agents = LanguageTutorAgents()
    tasks_manager = LanguageTutorTasks()

    instructor = agents.language_instructor()
    partner = agents.conversation_partner()
    guide = agents.cultural_guide()
    assessor = agents.progress_assessor()

    lesson_task = tasks_manager.teach_lesson(instructor, lesson_topic)
    practice_task = tasks_manager.practice_conversation(partner, "Daily conversation")
    culture_task = tasks_manager.teach_culture(guide, f"{language} customs")
    assess_task = tasks_manager.assess_level(assessor, f"{level} level work")

    crew = Crew(
        agents=[instructor, partner, guide, assessor],
        tasks=[lesson_task, practice_task, culture_task, assess_task],
        process=Process.sequential,
        verbose=True
    )

    result = crew.kickoff()
    print("\n## Language Tutor Results\n")
    print(result)
    return result

if __name__ == "__main__":
    run_language_tutor()
