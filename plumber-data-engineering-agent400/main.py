#!/usr/bin/env python
from crewai import Crew, Process
from agents import DataEngineeringAgents
from tasks import DataEngineeringTasks
from dotenv import load_dotenv
import os
import sys

load_dotenv()

def build_data_pipeline(
    source_systems: str,
    target_system: str,
    requirements: str,
    technology: str = "Python/SQL"
):
    """
    Build a complete data pipeline from design to implementation.

    Args:
        source_systems: Source data systems (databases, APIs, files)
        target_system: Target data warehouse or database
        requirements: Pipeline requirements and business logic
        technology: Technology stack to use
    """
    print(f"\n{'='*60}")
    print(f"Data Pipeline Development")
    print(f"Source: {source_systems}")
    print(f"Target: {target_system}")
    print(f"Technology: {technology}")
    print(f"{'='*60}\n")

    # Initialize agents and tasks
    agents = DataEngineeringAgents()
    tasks = DataEngineeringTasks()

    # Create agents
    data_architect = agents.data_architect()
    etl_engineer = agents.etl_engineer()
    data_quality_engineer = agents.data_quality_engineer()
    pipeline_optimizer = agents.pipeline_optimizer()
    data_engineering_lead = agents.data_engineering_lead()

    # Create tasks
    design_task = tasks.design_data_pipeline(
        agent=data_architect,
        source_systems=source_systems,
        target_system=target_system,
        requirements=requirements
    )

    implementation_task = tasks.implement_etl_process(
        agent=etl_engineer,
        pipeline_design="Use the pipeline design",
        technology=technology
    )

    quality_task = tasks.validate_data_quality(
        agent=data_quality_engineer,
        dataset="Validate the pipeline output",
        quality_rules="Standard data quality rules"
    )

    optimization_task = tasks.optimize_pipeline_performance(
        agent=pipeline_optimizer,
        pipeline_metrics="Analyze pipeline performance",
        bottlenecks="Identify and resolve bottlenecks"
    )

    documentation_task = tasks.create_pipeline_documentation(
        agent=data_engineering_lead,
        pipeline_design="Use pipeline design",
        etl_code="Use ETL implementation",
        quality_checks="Use quality validation"
    )

    # Create crew
    crew = Crew(
        agents=[
            data_architect,
            etl_engineer,
            data_quality_engineer,
            pipeline_optimizer,
            data_engineering_lead
        ],
        tasks=[
            design_task,
            implementation_task,
            quality_task,
            optimization_task,
            documentation_task
        ],
        process=Process.sequential,
        verbose=True
    )

    # Execute
    result = crew.kickoff()

    print(f"\n{'='*60}")
    print("Data Pipeline Development Complete!")
    print(f"{'='*60}\n")
    print(result)

    # Save pipeline documentation
    output_file = f"pipeline_{source_systems.replace(' ', '_').lower()}_to_{target_system.replace(' ', '_').lower()}.txt"
    with open(output_file, 'w') as f:
        f.write(str(result))
    print(f"\nPipeline documentation saved to: {output_file}")

    return result

def optimize_existing_pipeline(pipeline_name: str):
    """
    Optimize an existing data pipeline.
    """
    print(f"\n{'='*60}")
    print(f"Optimizing Pipeline: {pipeline_name}")
    print(f"{'='*60}\n")

    agents = DataEngineeringAgents()
    tasks = DataEngineeringTasks()

    pipeline_optimizer = agents.pipeline_optimizer()
    data_engineering_lead = agents.data_engineering_lead()

    optimization_task = tasks.optimize_pipeline_performance(
        agent=pipeline_optimizer,
        pipeline_metrics=f"Current metrics for {pipeline_name}",
        bottlenecks="Identified performance issues"
    )

    documentation_task = tasks.create_pipeline_documentation(
        agent=data_engineering_lead,
        pipeline_design=f"Optimized design for {pipeline_name}",
        etl_code="Optimized implementation",
        quality_checks="Quality validation results"
    )

    crew = Crew(
        agents=[pipeline_optimizer, data_engineering_lead],
        tasks=[optimization_task, documentation_task],
        process=Process.sequential,
        verbose=True
    )

    result = crew.kickoff()

    print(f"\n{'='*60}")
    print("Pipeline Optimization Complete!")
    print(f"{'='*60}\n")
    print(result)

    return result

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage:")
        print("  New pipeline:  python main.py new <source> <target> '<requirements>' [technology]")
        print("  Optimize:      python main.py optimize <pipeline_name>")
        print("\nExamples:")
        print("  python main.py new 'MySQL Database' 'Snowflake' 'Daily customer data sync' 'Python/dbt'")
        print("  python main.py optimize 'customer_data_pipeline'")
        print("\nTechnology options: Python/SQL, Spark/Scala, dbt, Airflow, Prefect")
        sys.exit(1)

    command = sys.argv[1]

    if command == "new":
        if len(sys.argv) < 5:
            print("Error: Source, target, and requirements needed")
            print("Usage: python main.py new <source> <target> '<requirements>' [technology]")
            sys.exit(1)

        source = sys.argv[2]
        target = sys.argv[3]
        requirements = sys.argv[4]
        technology = sys.argv[5] if len(sys.argv) > 5 else "Python/SQL"

        build_data_pipeline(source, target, requirements, technology)

    elif command == "optimize":
        if len(sys.argv) < 3:
            print("Error: Pipeline name required")
            print("Usage: python main.py optimize <pipeline_name>")
            sys.exit(1)

        pipeline_name = sys.argv[2]
        optimize_existing_pipeline(pipeline_name)

    else:
        print(f"Unknown command: {command}")
        print("Use 'new' to create a pipeline or 'optimize' to optimize existing")
        sys.exit(1)
