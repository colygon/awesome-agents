#!/usr/bin/env python
from crewai import Crew, Process
from agents import MongooseMigrationAgents
from tasks import MongooseMigrationTasks
import os
from dotenv import load_dotenv

load_dotenv()

def run_mongoose_migration():
    """
    Run the Mongoose Migration system
    """
    print("## Welcome to the Mongoose Migration System")
    print("--------------------------------------------")

    print("\nEnter old schema (or 'default' for sample):")
    old_schema = input()
    if old_schema.lower() == 'default':
        old_schema = '{"name": "User", "fields": {"name": "String", "email": "String"}}'

    print("\nEnter new schema (or 'default' for sample):")
    new_schema = input()
    if new_schema.lower() == 'default':
        new_schema = '{"name": "User", "fields": {"name": "String", "email": "String", "age": "Number"}}'

    # Initialize agents and tasks
    agents = MongooseMigrationAgents()
    tasks = MongooseMigrationTasks()

    # Create agents
    analyst_agent = agents.schema_analyst_agent()
    engineer_agent = agents.migration_engineer_agent()
    transformer_agent = agents.data_transformer_agent()
    validator_agent = agents.validation_agent()

    # Create tasks
    analysis_task = tasks.analyze_schema_task(analyst_agent, old_schema, new_schema)
    generation_task = tasks.generate_migration_task(engineer_agent, "{{analysis_output}}")
    transformation_task = tasks.transform_data_task(transformer_agent, "{{generation_output}}", "sample_data")
    validation_task = tasks.validate_migration_task(validator_agent, "{{generation_output}}", "test_data")

    # Create crew
    crew = Crew(
        agents=[analyst_agent, engineer_agent, transformer_agent, validator_agent],
        tasks=[analysis_task, generation_task, transformation_task, validation_task],
        process=Process.sequential,
        verbose=True
    )

    # Execute
    result = crew.kickoff()

    print("\n\n########################")
    print("## Migration Result")
    print("########################\n")
    print(result)

    return result

if __name__ == "__main__":
    run_mongoose_migration()
