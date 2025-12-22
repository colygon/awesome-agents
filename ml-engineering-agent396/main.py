"""
ML Engineering Pipeline - CrewAI Implementation
Main execution script for MLOps workflows
"""

import os
from dotenv import load_dotenv
from crewai import Crew, Process
from agents import MLEngineeringAgents
from tasks import MLEngineeringTasks

# Load environment variables
load_dotenv()


def run_ml_engineering_pipeline(
    model_requirements: str,
    data_info: str,
    training_config: str,
    performance_requirements: str,
    deployment_config: str,
    monitoring_requirements: str
):
    """
    Execute the ML engineering pipeline

    Args:
        model_requirements: Model requirements and constraints
        data_info: Information about available data
        training_config: Training configuration
        performance_requirements: Required model performance
        deployment_config: Deployment configuration
        monitoring_requirements: Monitoring requirements

    Returns:
        Crew execution result
    """
    # Initialize agents
    agents = MLEngineeringAgents()
    feature_engineer = agents.feature_engineer_agent()
    model_trainer = agents.model_trainer_agent()
    deployment_engineer = agents.deployment_engineer_agent()

    # Initialize tasks
    tasks = MLEngineeringTasks()
    feature_task = tasks.feature_engineering_task(feature_engineer, model_requirements, data_info)
    training_task = tasks.model_training_task(model_trainer, training_config, performance_requirements)
    deployment_task = tasks.deployment_task(deployment_engineer, deployment_config, monitoring_requirements)

    # Create crew
    crew = Crew(
        agents=[feature_engineer, model_trainer, deployment_engineer],
        tasks=[feature_task, training_task, deployment_task],
        process=Process.sequential,
        verbose=True
    )

    # Execute pipeline
    print("\n" + "="*80)
    print("ML ENGINEERING PIPELINE - CREWAI")
    print("="*80)
    print("\nMLOps Workflow: Feature Engineering → Model Training → Deployment")
    print("\nStarting ML engineering pipeline...\n")

    result = crew.kickoff()

    print("\n" + "="*80)
    print("PIPELINE EXECUTION COMPLETE")
    print("="*80)

    return result


def main():
    """Main execution with example configuration"""

    # Example configuration - Fraud Detection System
    model_requirements = """
    Business Problem: Real-time credit card fraud detection
    Model Type: Binary Classification (Fraud vs. Legitimate)
    Performance Requirements:
    - Recall >= 85% (must catch most fraud)
    - Precision >= 70% (minimize false alarms)
    - Latency < 100ms (real-time requirement)
    - Interpretability: High (for dispute resolution)

    Constraints:
    - Handle extreme class imbalance (~0.1% fraud rate)
    - Must work with missing/incomplete data
    - Need to explain predictions for compliance
    - Support 10,000+ transactions per second
    """

    data_info = """
    Data Sources:
    1. Transaction Database:
       - Transaction amount, merchant, location, time
       - Card details (masked), customer ID
       - Historical transaction data (90 days)

    2. Customer Profile:
       - Account age, credit limit, average spending
       - Geographic home location
       - Device fingerprints

    3. External Data:
       - Merchant category codes
       - Geographic risk scores
       - Time-based risk patterns

    Available Features:
    - Numerical: amount, time_since_last_transaction, avg_amount_30d
    - Categorical: merchant_category, country, card_type
    - Temporal: hour_of_day, day_of_week, is_weekend
    - Aggregated: transaction_count_24h, total_spend_7d

    Data Volume: 100M transactions/month, 0.1% fraud rate
    """

    training_config = """
    Platform: AWS SageMaker
    Compute: ml.p3.2xlarge (GPU) for training
    Framework: XGBoost + LightGBM ensemble

    Training Strategy:
    - Use 6 months historical data
    - Stratified train/val/test split (70/15/15)
    - SMOTE for class balancing
    - 5-fold cross-validation
    - Hyperparameter tuning with Optuna (100 trials)

    Experiment Tracking: MLflow
    Model Registry: MLflow Model Registry
    Version Control: Git + DVC for data
    """

    performance_requirements = """
    Primary Metric: F1-Score (balance precision and recall)
    Minimum Thresholds:
    - Recall >= 85% (catch fraud)
    - Precision >= 70% (reduce false positives)
    - ROC-AUC >= 0.95
    - PR-AUC >= 0.80 (for imbalanced data)

    Latency: P95 < 100ms for inference
    Throughput: 10,000+ predictions/second

    Validation Requirements:
    - Temporal validation (test on future data)
    - Fairness across customer segments
    - Robustness to adversarial examples
    - Calibrated probability outputs
    """

    deployment_config = """
    Platform: AWS (EKS + SageMaker)
    Architecture: Microservices

    Serving:
    - REST API (FastAPI) for real-time predictions
    - Batch inference for daily risk scoring
    - Feature store: AWS Feature Store

    Deployment Strategy: Canary (5% → 25% → 100%)
    Infrastructure:
    - Kubernetes cluster (3 nodes, auto-scaling)
    - GPU inference for high throughput
    - Redis cache for feature serving
    - Load balancer with health checks

    Security:
    - API authentication (JWT tokens)
    - Encryption at rest and in transit
    - PCI-DSS compliance
    - Audit logging
    """

    monitoring_requirements = """
    Performance Monitoring:
    - Latency (p50, p95, p99) - Alert if p95 > 150ms
    - Throughput - Alert if < 8,000 req/s
    - Error rate - Alert if > 0.1%
    - Resource utilization - Alert if CPU/GPU > 80%

    Model Quality Monitoring:
    - Prediction distribution drift - Daily checks
    - Feature drift detection - Alert on significant shift
    - Model performance metrics - Weekly evaluation
    - False positive rate - Alert if > 30%
    - False negative rate - Alert if > 15%

    Business Metrics:
    - Fraud detection rate
    - False alarm rate
    - Average resolution time
    - Customer satisfaction impact

    Alerting:
    - PagerDuty for critical alerts
    - Slack for warnings
    - Email for daily summaries

    SLO: 99.9% uptime, <100ms p95 latency
    """

    # Run pipeline
    result = run_ml_engineering_pipeline(
        model_requirements=model_requirements,
        data_info=data_info,
        training_config=training_config,
        performance_requirements=performance_requirements,
        deployment_config=deployment_config,
        monitoring_requirements=monitoring_requirements
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
