"""
Data Engineering Pipeline - CrewAI Implementation
Main execution script for data engineering operations
"""

import os
from dotenv import load_dotenv
from crewai import Crew, Process
from agents import DataEngineeringAgents
from tasks import DataEngineeringTasks

# Load environment variables
load_dotenv()


def run_data_engineering_pipeline(
    data_source: str,
    data_format: str,
    transformation_requirements: str,
    quality_rules: str
):
    """
    Execute the data engineering pipeline

    Args:
        data_source: Source identifier (database, API, file path, etc.)
        data_format: Data format (CSV, JSON, Parquet, etc.)
        transformation_requirements: Transformation rules and requirements
        quality_rules: Data quality validation rules

    Returns:
        Crew execution result
    """
    # Initialize agents
    agents = DataEngineeringAgents()
    ingestion_agent = agents.data_ingestion_agent()
    transformation_agent = agents.data_transformation_agent()
    quality_agent = agents.data_quality_agent()

    # Initialize tasks
    tasks = DataEngineeringTasks()
    ingest_task = tasks.ingest_data_task(ingestion_agent, data_source, data_format)
    transform_task = tasks.transform_data_task(transformation_agent, transformation_requirements)
    validate_task = tasks.validate_quality_task(quality_agent, quality_rules)

    # Create crew
    crew = Crew(
        agents=[ingestion_agent, transformation_agent, quality_agent],
        tasks=[ingest_task, transform_task, validate_task],
        process=Process.sequential,
        verbose=True
    )

    # Execute pipeline
    print("\n" + "="*80)
    print("DATA ENGINEERING PIPELINE - CREWAI")
    print("="*80)
    print(f"\nData Source: {data_source}")
    print(f"Data Format: {data_format}")
    print("\nStarting pipeline execution...\n")

    result = crew.kickoff()

    print("\n" + "="*80)
    print("PIPELINE EXECUTION COMPLETE")
    print("="*80)

    return result


def main():
    """Main execution with example configuration"""

    # Example configuration
    data_source = "s3://data-lake/customer-transactions/2025-12-21/"
    data_format = "Parquet"

    transformation_requirements = """
    1. Remove duplicate transactions based on transaction_id
    2. Convert all timestamps to UTC
    3. Normalize currency values to USD
    4. Calculate customer lifetime value (CLV)
    5. Categorize transactions by product type
    6. Create aggregated daily/weekly/monthly views
    7. Enrich with customer demographic data from CRM system
    8. Handle null values: impute missing amounts with 0, remove records with null customer_id
    """

    quality_rules = """
    1. Completeness: transaction_id, customer_id, amount, timestamp must be 100% populated
    2. Accuracy: amount must be > 0 and < $1,000,000
    3. Validity: timestamp must be within last 90 days
    4. Consistency: customer_id must exist in customer dimension table
    5. Uniqueness: No duplicate transaction_ids allowed
    6. Threshold: Total quality score must be >= 95%
    7. Anomaly: Flag transactions > 3 standard deviations from mean
    """

    # Run pipeline
    result = run_data_engineering_pipeline(
        data_source=data_source,
        data_format=data_format,
        transformation_requirements=transformation_requirements,
        quality_rules=quality_rules
    )

    print("\n" + "="*80)
    print("FINAL RESULT")
    print("="*80)
    print(result)


if __name__ == "__main__":
    # Check for OpenAI API key
    if not os.getenv("OPENAI_API_KEY"):
        print("Error: OPENAI_API_KEY not found in environment variables")
        print("Please create a .env file with your OpenAI API key")
        print("\nExample .env file:")
        print("OPENAI_API_KEY=sk-your-key-here")
        exit(1)

    main()
