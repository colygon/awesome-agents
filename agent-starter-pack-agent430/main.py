#!/usr/bin/env python
from crewai import Crew, Process
from agents import AgentStarterAgents
from tasks import AgentStarterTasks
from dotenv import load_dotenv

load_dotenv()

def run_agent_starter():
    print("## Welcome to Agent Starter Pack")
    print('-------------------------------')

    topic = input("Enter research topic or 'default': ")
    if topic.lower() == 'default':
        topic = "Artificial Intelligence trends in 2024"

    content_type = input("Enter content type or 'default': ")
    if content_type.lower() == 'default':
        content_type = "Blog post (800 words)"

    agents = AgentStarterAgents()
    tasks = AgentStarterTasks()

    researcher = agents.research_agent()
    writer = agents.writing_agent()
    analyst = agents.analysis_agent()
    coordinator = agents.coordinator_agent()

    research_task = tasks.research_topic(researcher, topic)
    write_task = tasks.create_content(writer, content_type)
    analyze_task = tasks.analyze_findings(analyst, "From research")
    deliver_task = tasks.deliver_project(coordinator)

    crew = Crew(
        agents=[researcher, writer, analyst, coordinator],
        tasks=[research_task, write_task, analyze_task, deliver_task],
        process=Process.sequential,
        verbose=True
    )

    result = crew.kickoff()

    print("\n\n########################")
    print("## Project Complete!")
    print("########################\n")
    print(result)

    return result

if __name__ == "__main__":
    run_agent_starter()
