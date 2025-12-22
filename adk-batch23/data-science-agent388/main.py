#!/usr/bin/env python3
"""
Data Science Agent - CrewAI Implementation
End-to-end data science workflow using multi-agent system
"""

import os
import json
from crewai import Agent, Task, Crew, Process
from crewai_tools import SerperDevTool, FileReadTool, DirectoryReadTool
from langchain_openai import ChatOpenAI
import datetime

# Initialize OpenAI LLM
llm = ChatOpenAI(
    model="gpt-4o",
    temperature=0.7,
    api_key=os.getenv("OPENAI_API_KEY")
)

# Initialize tools
search_tool = SerperDevTool()
file_read_tool = FileReadTool()
directory_tool = DirectoryReadTool()

# Define Agents

# 1. Data Analyst
data_analyst = Agent(
    role="Senior Data Analyst",
    goal="Perform exploratory data analysis and identify insights",
    backstory="""You are an experienced data analyst who excels at understanding
    datasets, identifying patterns, and extracting meaningful insights. You have
    strong statistical knowledge and can detect anomalies, trends, and relationships
    in data. You ask the right questions and know which analyses to perform.""",
    verbose=True,
    allow_delegation=False,
    tools=[file_read_tool, directory_tool],
    llm=llm
)

# 2. Feature Engineer
feature_engineer = Agent(
    role="ML Feature Engineering Specialist",
    goal="Design and create effective features for machine learning models",
    backstory="""You are a feature engineering specialist who understands how to
    transform raw data into meaningful features for ML models. You know feature
    selection techniques, encoding methods, scaling approaches, and how to handle
    missing data. You create features that improve model performance.""",
    verbose=True,
    allow_delegation=False,
    tools=[file_read_tool],
    llm=llm
)

# 3. ML Engineer
ml_engineer = Agent(
    role="Machine Learning Engineer",
    goal="Build, train, and optimize machine learning models",
    backstory="""You are a machine learning engineer with expertise in various
    ML algorithms, model selection, hyperparameter tuning, and performance
    optimization. You understand trade-offs between different algorithms and
    can select the best approach for each problem. You focus on creating
    production-ready, maintainable models.""",
    verbose=True,
    allow_delegation=False,
    tools=[search_tool],
    llm=llm
)

# 4. Model Evaluator
model_evaluator = Agent(
    role="ML Model Evaluation Specialist",
    goal="Evaluate model performance and identify improvements",
    backstory="""You are a model evaluation specialist who thoroughly assesses
    ML model performance using appropriate metrics. You understand bias-variance
    tradeoff, overfitting, cross-validation, and statistical significance. You
    provide objective assessments and actionable recommendations for improvement.""",
    verbose=True,
    allow_delegation=False,
    llm=llm
)

# 5. Data Science Communicator
communicator = Agent(
    role="Data Science Communications Specialist",
    goal="Translate technical findings into clear business insights",
    backstory="""You are a data science communicator who excels at explaining
    complex technical concepts to non-technical stakeholders. You create clear
    visualizations, compelling narratives, and actionable recommendations. You
    bridge the gap between data science and business decision-making.""",
    verbose=True,
    allow_delegation=False,
    llm=llm
)

def run_data_science_project(
    problem_statement: str,
    data_description: str,
    target_variable: str = None,
    project_type: str = "classification"
) -> dict:
    """
    Execute a complete data science project workflow

    Args:
        problem_statement: Description of the business problem
        data_description: Description of available data
        target_variable: Target variable to predict (if applicable)
        project_type: Type of project (classification, regression, clustering, etc.)

    Returns:
        dict with project outputs
    """

    current_date = datetime.datetime.now().strftime("%Y-%m-%d")
    target_info = f"\nTarget Variable: {target_variable}" if target_variable else ""

    # Task 1: Exploratory Data Analysis
    eda_task = Task(
        description=f"""Perform comprehensive exploratory data analysis:

        Problem: {problem_statement}
        Data: {data_description}{target_info}
        Project Type: {project_type}

        Your analysis should include:
        1. **Data Understanding**
           - Dataset structure and size
           - Variable types and distributions
           - Missing values analysis
           - Data quality assessment

        2. **Statistical Analysis**
           - Descriptive statistics
           - Correlation analysis
           - Distribution analysis
           - Outlier detection

        3. **Key Insights**
           - Patterns and trends
           - Relationships between variables
           - Potential data issues
           - Initial hypotheses

        4. **Recommendations**
           - Data cleaning needs
           - Feature engineering opportunities
           - Modeling approach suggestions

        Provide comprehensive EDA report.""",
        agent=data_analyst,
        expected_output="Comprehensive exploratory data analysis report"
    )

    # Task 2: Feature Engineering
    feature_task = Task(
        description=f"""Design feature engineering strategy:

        Based on the EDA findings, create a feature engineering plan for:
        Problem: {problem_statement}
        Project Type: {project_type}

        Your plan should include:
        1. **Feature Creation**
           - New features to derive
           - Interaction terms
           - Polynomial features (if applicable)
           - Domain-specific features

        2. **Feature Transformation**
           - Encoding categorical variables
           - Scaling/normalization methods
           - Handling skewed distributions
           - Date/time feature extraction

        3. **Feature Selection**
           - Importance ranking approach
           - Dimensionality reduction (if needed)
           - Multicollinearity handling

        4. **Data Preprocessing**
           - Missing value imputation strategy
           - Outlier handling approach
           - Train/test split strategy

        Provide detailed feature engineering plan with code examples.""",
        agent=feature_engineer,
        expected_output="Detailed feature engineering plan with implementation guidance",
        context=[eda_task]
    )

    # Task 3: Model Development
    model_task = Task(
        description=f"""Develop machine learning model strategy:

        Problem: {problem_statement}
        Type: {project_type}{target_info}

        Based on EDA and feature engineering plan, develop:

        1. **Model Selection**
           - Recommend 3-5 candidate algorithms
           - Justify selections based on problem characteristics
           - Consider interpretability vs performance tradeoffs

        2. **Training Strategy**
           - Cross-validation approach
           - Train/validation/test split
           - Evaluation metrics to use
           - Baseline model for comparison

        3. **Hyperparameter Tuning**
           - Key hyperparameters to tune
           - Search strategy (grid, random, bayesian)
           - Tuning approach

        4. **Implementation Plan**
           - Training pipeline
           - Model serialization
           - Reproducibility considerations

        Use web search for current best practices.
        Date: {current_date}

        Provide comprehensive model development plan with code examples.""",
        agent=ml_engineer,
        expected_output="Complete model development strategy with implementation details",
        context=[eda_task, feature_task]
    )

    # Task 4: Model Evaluation
    evaluation_task = Task(
        description=f"""Design model evaluation framework:

        Project Type: {project_type}
        Problem: {problem_statement}

        Create comprehensive evaluation plan:

        1. **Evaluation Metrics**
           - Primary metrics for {project_type}
           - Secondary metrics
           - Business metrics
           - Metric interpretation guidelines

        2. **Validation Strategy**
           - Cross-validation results interpretation
           - Overfitting/underfitting detection
           - Learning curves analysis
           - Error analysis approach

        3. **Model Comparison**
           - Framework for comparing models
           - Statistical significance testing
           - Performance vs complexity tradeoffs

        4. **Deployment Readiness**
           - Production performance expectations
           - Monitoring recommendations
           - Model maintenance plan

        Provide detailed evaluation framework.""",
        agent=model_evaluator,
        expected_output="Comprehensive model evaluation framework",
        context=[model_task]
    )

    # Task 5: Business Communication
    communication_task = Task(
        description=f"""Create business-focused project summary:

        Problem: {problem_statement}
        Project Type: {project_type}

        Synthesize all findings into executive summary for stakeholders:

        1. **Executive Summary**
           - Business problem and impact
           - Approach overview
           - Key findings
           - Recommended solution

        2. **Data Insights**
           - Most important patterns discovered
           - Business implications
           - Data quality considerations

        3. **Model Performance**
           - Expected accuracy/performance in business terms
           - Confidence intervals
           - Limitations and risks

        4. **Implementation Roadmap**
           - Recommended next steps
           - Timeline estimate
           - Resource requirements
           - Success metrics

        5. **Business Impact**
           - Expected ROI or value
           - Key performance indicators
           - Success criteria

        Format as clear, non-technical Markdown report suitable for executives.""",
        agent=communicator,
        expected_output="Executive-level project summary in Markdown",
        context=[eda_task, feature_task, model_task, evaluation_task]
    )

    # Create and run crew
    crew = Crew(
        agents=[data_analyst, feature_engineer, ml_engineer, model_evaluator, communicator],
        tasks=[eda_task, feature_task, model_task, evaluation_task, communication_task],
        process=Process.sequential,
        verbose=True
    )

    result = crew.kickoff()

    return {
        "eda_report": eda_task.output.raw if hasattr(eda_task, 'output') else "",
        "feature_engineering": feature_task.output.raw if hasattr(feature_task, 'output') else "",
        "model_strategy": model_task.output.raw if hasattr(model_task, 'output') else "",
        "evaluation_framework": evaluation_task.output.raw if hasattr(evaluation_task, 'output') else "",
        "executive_summary": str(result),
        "metadata": {
            "problem": problem_statement,
            "project_type": project_type,
            "target": target_variable,
            "date": current_date
        }
    }

def save_project_output(content: str, filename: str):
    """Save project output to file"""
    if not filename.endswith('.md'):
        filename += '.md'

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"\nProject summary saved to: {filename}")

if __name__ == "__main__":
    print("Data Science Agent - CrewAI")
    print("=" * 60)

    # Get project details
    print("\nDefine your data science project:")

    problem = input("\nEnter problem statement: ").strip()
    if not problem:
        problem = "Predict customer churn to improve retention strategies"

    data_desc = input("Describe available data: ").strip()
    if not data_desc:
        data_desc = "Customer transaction history, demographics, support interactions, and engagement metrics over 2 years"

    project_type = input("Project type (classification/regression/clustering) [classification]: ").strip().lower()
    if project_type not in ["classification", "regression", "clustering"]:
        project_type = "classification"

    target = input("Target variable (optional): ").strip() or None

    print(f"\nProblem: {problem}")
    print(f"Data: {data_desc}")
    print(f"Type: {project_type}")
    if target:
        print(f"Target: {target}")
    print("\nRunning data science workflow...\n")

    # Run project
    result = run_data_science_project(problem, data_desc, target, project_type)

    # Display results
    print("\n" + "=" * 60)
    print("DATA SCIENCE PROJECT COMPLETE")
    print("=" * 60)

    print("\n--- Exploratory Data Analysis ---")
    print(result["eda_report"][:1000] + "..." if len(result["eda_report"]) > 1000 else result["eda_report"])

    print("\n--- Feature Engineering ---")
    print(result["feature_engineering"][:1000] + "..." if len(result["feature_engineering"]) > 1000 else result["feature_engineering"])

    print("\n--- Model Strategy ---")
    print(result["model_strategy"][:1000] + "..." if len(result["model_strategy"]) > 1000 else result["model_strategy"])

    print("\n--- Evaluation Framework ---")
    print(result["evaluation_framework"][:1000] + "..." if len(result["evaluation_framework"]) > 1000 else result["evaluation_framework"])

    print("\n--- Executive Summary ---")
    print(result["executive_summary"])

    # Save option
    save = input("\n\nSave project summary to file? (y/n): ").strip().lower()
    if save == 'y':
        filename = input("Enter filename (without .md extension): ").strip()
        if filename:
            save_project_output(result["executive_summary"], filename)
