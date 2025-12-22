"""
Data Science Workflow - CrewAI Implementation
Main execution script for analytics and modeling operations
"""

import os
from dotenv import load_dotenv
from crewai import Crew, Process
from agents import DataScienceAgents
from tasks import DataScienceTasks

# Load environment variables
load_dotenv()


def run_data_science_workflow(
    dataset_description: str,
    analysis_objectives: str,
    problem_type: str,
    model_requirements: str,
    business_context: str
):
    """
    Execute the data science workflow

    Args:
        dataset_description: Description of the dataset
        analysis_objectives: What to analyze and discover
        problem_type: Type of ML problem (regression/classification/clustering)
        model_requirements: Model requirements and constraints
        business_context: Business context for insights generation

    Returns:
        Crew execution result
    """
    # Initialize agents
    agents = DataScienceAgents()
    analyst = agents.data_analyst_agent()
    model_builder = agents.model_builder_agent()
    insights_generator = agents.insights_generator_agent()

    # Initialize tasks
    tasks = DataScienceTasks()
    eda_task = tasks.exploratory_analysis_task(analyst, dataset_description, analysis_objectives)
    modeling_task = tasks.model_building_task(model_builder, problem_type, model_requirements)
    insights_task = tasks.insights_generation_task(insights_generator, business_context)

    # Create crew
    crew = Crew(
        agents=[analyst, model_builder, insights_generator],
        tasks=[eda_task, modeling_task, insights_task],
        process=Process.sequential,
        verbose=True
    )

    # Execute workflow
    print("\n" + "="*80)
    print("DATA SCIENCE WORKFLOW - CREWAI")
    print("="*80)
    print(f"\nDataset: {dataset_description}")
    print(f"Problem Type: {problem_type}")
    print("\nStarting data science workflow...\n")

    result = crew.kickoff()

    print("\n" + "="*80)
    print("WORKFLOW EXECUTION COMPLETE")
    print("="*80)

    return result


def main():
    """Main execution with example configuration"""

    # Example configuration - Customer Churn Prediction
    dataset_description = """
    Customer Churn Dataset
    - 10,000 customer records
    - 20 features including demographics, usage patterns, service subscriptions
    - Target: Churn (binary - Yes/No)
    - Features: tenure, monthly_charges, total_charges, contract_type, payment_method,
                internet_service, phone_service, streaming_services, customer_service_calls
    - Time period: Last 12 months
    """

    analysis_objectives = """
    1. Understand customer churn patterns and key drivers
    2. Identify high-risk customer segments
    3. Analyze relationship between service usage and churn
    4. Examine impact of contract types and payment methods
    5. Discover actionable insights for retention strategies
    """

    problem_type = "Binary Classification (Churn Prediction)"

    model_requirements = """
    1. Primary metric: F1-score (balance precision and recall)
    2. Minimum recall: 75% (must catch most churners)
    3. Model interpretability is important for business stakeholders
    4. Handle class imbalance (churn rate ~20%)
    5. Feature importance needed for retention strategy
    6. Production deployment target: Model must be explainable
    """

    business_context = """
    Business Problem:
    - Current churn rate: 20% annually
    - Customer acquisition cost: $500
    - Average customer lifetime value: $2,000
    - Goal: Reduce churn by 5 percentage points (from 20% to 15%)
    - Budget for retention programs: $1M annually

    Decision Requirements:
    - Identify top 3 factors driving churn
    - Recommend targeted retention strategies
    - Prioritize high-value customers for retention
    - Estimate ROI of retention programs
    - Define early warning indicators

    Stakeholders:
    - Marketing team (retention campaigns)
    - Customer success team (intervention strategies)
    - Product team (service improvements)
    - Executive leadership (strategic decisions)
    """

    # Run workflow
    result = run_data_science_workflow(
        dataset_description=dataset_description,
        analysis_objectives=analysis_objectives,
        problem_type=problem_type,
        model_requirements=model_requirements,
        business_context=business_context
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
