#!/usr/bin/env python
"""Edu.AI Brazil - CrewAI Implementation"""

import sys
from crewai import Crew, Process
from agents import brazil_curriculum_specialist, portuguese_content_creator, enem_prep_specialist, inclusive_education_advisor, assessment_creator_br
from tasks import create_tasks


def main():
    print("Edu.AI Brazil - Sistema Educacional Brasileiro")
    print("="*60)

    subject = input("Disciplina: ").strip() or "Matemática"
    level = input("Nível (Infantil/Fundamental/Médio): ").strip() or "Ensino Fundamental"

    course_info = {
        'subject': subject,
        'level': level
    }

    tasks = create_tasks(course_info)
    crew = Crew(
        agents=[brazil_curriculum_specialist, portuguese_content_creator, enem_prep_specialist, inclusive_education_advisor, assessment_creator_br],
        tasks=tasks,
        process=Process.sequential,
        verbose=True
    )

    print(f"\nCriando conteúdo para {subject}...")
    result = crew.kickoff()
    print("\n" + "="*60)
    print("CONTEÚDO CRIADO")
    print("="*60)
    print(result)


if __name__ == "__main__":
    main()
