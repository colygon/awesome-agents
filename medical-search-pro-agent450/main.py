#!/usr/bin/env python
from crewai import Crew, Process
from agents import MedicalSearchAgents
from tasks import MedicalSearchTasks
import os
from dotenv import load_dotenv

load_dotenv()

def run_medical_search():
    """
    Run the Medical Search Pro system
    """
    print("## Welcome to Medical Search Pro")
    print("---------------------------------")
    print("\nDISCLAIMER: This is for informational purposes only.")
    print("Always consult healthcare professionals for medical advice.\n")

    print("Select search type:")
    print("1. Research medical condition")
    print("2. Find clinical trials")
    print("3. Drug information")
    print("4. General medical search")

    choice = input("\nEnter choice (1-4): ")

    # Initialize agents and tasks
    agents = MedicalSearchAgents()
    tasks = MedicalSearchTasks()

    # Create agents
    literature_agent = agents.literature_researcher_agent()
    trial_agent = agents.clinical_trial_specialist_agent()
    drug_agent = agents.drug_information_agent()
    synthesizer = agents.medical_synthesizer_agent()
    evaluator = agents.evidence_evaluator_agent()

    # Create tasks based on choice
    if choice == '1':
        condition = input("Enter medical condition: ")
        task_list = [
            tasks.search_literature_task(literature_agent, condition, "pathophysiology and treatment"),
            tasks.synthesize_evidence_task(synthesizer, "{{literature_output}}"),
            tasks.evaluate_evidence_task(evaluator, "{{synthesis_output}}")
        ]
        agent_list = [literature_agent, synthesizer, evaluator]
    elif choice == '2':
        condition = input("Enter condition: ")
        intervention = input("Enter intervention/treatment: ")
        task_list = [
            tasks.find_clinical_trials_task(trial_agent, condition, intervention),
            tasks.synthesize_evidence_task(synthesizer, "{{trials_output}}")
        ]
        agent_list = [trial_agent, synthesizer]
    elif choice == '3':
        drug_name = input("Enter drug name: ")
        task_list = [
            tasks.research_drug_task(drug_agent, drug_name),
            tasks.search_literature_task(literature_agent, drug_name, "efficacy and safety")
        ]
        agent_list = [drug_agent, literature_agent]
    else:
        query = input("Enter medical search query: ")
        task_list = [
            tasks.search_literature_task(literature_agent, query, "general"),
            tasks.synthesize_evidence_task(synthesizer, "{{literature_output}}")
        ]
        agent_list = [literature_agent, synthesizer]

    # Create crew
    crew = Crew(
        agents=agent_list,
        tasks=task_list,
        process=Process.sequential,
        verbose=True
    )

    # Execute
    result = crew.kickoff()

    print("\n\n########################")
    print("## Medical Search Results")
    print("########################\n")
    print(result)
    print("\n\nDISCLAIMER: This information is for educational purposes only.")
    print("Consult qualified healthcare professionals for medical advice.")

    return result

if __name__ == "__main__":
    run_medical_search()
