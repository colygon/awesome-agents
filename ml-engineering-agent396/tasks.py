"""
ML Engineering Tasks
CrewAI task definitions for MLOps workflows
"""

from crewai import Task
from textwrap import dedent


class MLEngineeringTasks:
    """Task definitions for ML engineering workflow"""

    def feature_engineering_task(self, agent, model_requirements, data_info):
        """
        Task for designing and implementing feature engineering pipeline

        Args:
            agent: Feature engineering specialist agent
            model_requirements: Model requirements and constraints
            data_info: Information about available data sources
        """
        return Task(
            description=dedent(f"""
                Design and implement a production-ready feature engineering pipeline:

                Model Requirements: {model_requirements}
                Data Information: {data_info}

                Your responsibilities:

                1. Feature Discovery and Design:
                   - Identify raw features from data sources
                   - Design derived features based on domain knowledge
                   - Create interaction features
                   - Design temporal features (lags, rolling windows, seasonality)
                   - Identify features for different model types

                2. Feature Transformation Pipeline:
                   - Numerical features:
                     * Scaling (StandardScaler, MinMaxScaler, RobustScaler)
                     * Log/power transformations for skewed distributions
                     * Binning and discretization
                   - Categorical features:
                     * One-hot encoding for low cardinality
                     * Label encoding for ordinal features
                     * Target encoding for high cardinality
                     * Embeddings for very high cardinality
                   - Text features:
                     * TF-IDF vectorization
                     * Word embeddings (Word2Vec, GloVe)
                     * Sentence embeddings (BERT, Sentence Transformers)
                   - Datetime features:
                     * Extract hour, day, month, year, day_of_week
                     * Create cyclical encodings (sin/cos for hour, month)
                     * Calculate time since last event
                     * Identify holidays and special dates

                3. Feature Selection:
                   - Remove low-variance features
                   - Correlation analysis (remove highly correlated features)
                   - Statistical tests (ANOVA, chi-square)
                   - Model-based selection (Random Forest importance, L1 regularization)
                   - Recursive feature elimination
                   - Domain-based selection

                4. Feature Pipeline Implementation:
                   - Create scikit-learn Pipeline or ColumnTransformer
                   - Implement custom transformers for complex features
                   - Ensure pipeline is fit on training data only
                   - Handle missing values (imputation strategies)
                   - Prevent data leakage (no target information in features)

                5. Feature Store Integration:
                   - Design feature definitions and metadata
                   - Implement online/offline feature consistency
                   - Create feature serving layer
                   - Set up feature versioning
                   - Document feature lineage

                6. Feature Validation:
                   - Validate feature distributions
                   - Check for data leakage
                   - Test feature pipeline on sample data
                   - Verify reproducibility
                   - Document feature importance and rationale

                7. Production Readiness:
                   - Optimize feature computation performance
                   - Handle edge cases (null values, outliers, new categories)
                   - Create feature monitoring plan
                   - Document feature engineering logic
                   - Provide feature usage examples

                Provide a comprehensive feature engineering report and pipeline specification.
            """),
            expected_output=dedent("""
                A comprehensive feature engineering report containing:
                - Feature catalog (list of all features with descriptions)
                - Feature types breakdown (numerical, categorical, text, temporal)
                - Feature transformation specifications:
                  * Encoding methods used
                  * Scaling methods applied
                  * Derived feature formulas
                - Feature selection results:
                  * Number of features before/after selection
                  * Selection method and criteria
                  * Removed features with justification
                - Feature pipeline architecture:
                  * Pipeline diagram/flow
                  * scikit-learn Pipeline code structure
                  * Custom transformer descriptions
                - Feature validation results:
                  * Distribution checks
                  * Leakage prevention verification
                  * Null value handling strategy
                - Feature importance (preliminary analysis)
                - Production considerations:
                  * Performance optimization notes
                  * Edge case handling
                  * Online/offline consistency plan
                - Feature documentation:
                  * Feature definitions
                  * Business logic rationale
                  * Usage guidelines
            """),
            agent=agent
        )

    def model_training_task(self, agent, training_config, performance_requirements):
        """
        Task for training and optimizing ML models

        Args:
            agent: Model trainer agent
            training_config: Training configuration and hyperparameters
            performance_requirements: Required model performance metrics
        """
        return Task(
            description=dedent(f"""
                Train, optimize, and validate production ML models:

                Training Configuration: {training_config}
                Performance Requirements: {performance_requirements}

                Your responsibilities:

                1. Experiment Setup:
                   - Configure experiment tracking (MLflow, W&B)
                   - Version control data and code
                   - Set up reproducible random seeds
                   - Create experiment naming convention
                   - Log hyperparameters and metadata

                2. Data Preparation:
                   - Split data (train/validation/test)
                   - Implement stratified splitting for classification
                   - Handle class imbalance (SMOTE, class weights, sampling)
                   - Create cross-validation folds
                   - Prepare feature matrices and target vectors

                3. Baseline Model Training:
                   - Train simple baseline (mean/median/mode predictor)
                   - Train linear baseline (Logistic/Linear Regression)
                   - Establish baseline metrics
                   - Document baseline performance

                4. Advanced Model Training:
                   - Train tree-based models (Random Forest, XGBoost, LightGBM, CatBoost)
                   - Train neural networks if appropriate
                   - Implement ensemble methods (stacking, blending)
                   - Log all training runs to experiment tracker

                5. Hyperparameter Optimization:
                   - Define hyperparameter search space
                   - Implement search strategy:
                     * Grid Search for small spaces
                     * Random Search for larger spaces
                     * Bayesian Optimization (Optuna, Hyperopt) for complex spaces
                   - Use cross-validation for evaluation
                   - Track best parameters and performance
                   - Analyze hyperparameter importance

                6. Model Evaluation:
                   - Calculate comprehensive metrics:
                     * Classification: Accuracy, Precision, Recall, F1, ROC-AUC, PR-AUC
                     * Regression: RMSE, MAE, R², MAPE, quantile losses
                   - Generate evaluation plots:
                     * ROC and Precision-Recall curves
                     * Confusion matrix
                     * Residual plots (regression)
                     * Learning curves (training/validation)
                     * Feature importance plots
                   - Perform error analysis:
                     * Identify misclassified examples
                     * Analyze error patterns
                     * Check for systematic biases

                7. Model Validation:
                   - Validate on held-out test set
                   - Test temporal stability (if time-series)
                   - Check model calibration
                   - Verify fairness across groups
                   - Test robustness to input perturbations
                   - Analyze prediction confidence

                8. Model Selection:
                   - Compare all models on validation metrics
                   - Consider performance vs. complexity trade-off
                   - Evaluate inference latency
                   - Assess interpretability needs
                   - Select final model with justification

                9. Model Documentation:
                   - Create model card (intended use, limitations, performance)
                   - Document training process and decisions
                   - Save model artifacts (weights, pipeline, configs)
                   - Generate training report

                Provide comprehensive training report with model selection recommendation.
            """),
            expected_output=dedent("""
                A comprehensive model training report containing:
                - Experiment tracking summary (run IDs, timestamps)
                - Data preparation details:
                  * Train/val/test split sizes
                  * Class distribution
                  * Feature dimensions
                - Baseline model results
                - Advanced model comparison table:
                  * Model name
                  * Hyperparameters
                  * Training time
                  * Validation metrics
                  * Test metrics
                - Hyperparameter optimization results:
                  * Search method used
                  * Best hyperparameters found
                  * Optimization convergence
                  * Hyperparameter importance
                - Model performance analysis:
                  * Detailed metrics for best model
                  * Performance plots descriptions (ROC, confusion matrix, etc.)
                  * Feature importance ranking
                  * Error analysis summary
                - Model validation results:
                  * Test set performance
                  * Fairness assessment
                  * Calibration analysis
                  * Robustness testing results
                - Model selection recommendation:
                  * Selected model with justification
                  * Performance vs. complexity analysis
                  * Inference latency estimates
                  * Production readiness assessment
                - Model artifacts inventory:
                  * Saved model files
                  * Feature pipeline files
                  * Configuration files
                  * Experiment tracking URLs
                - Model card:
                  * Intended use
                  * Training data
                  * Performance metrics
                  * Limitations and biases
                  * Ethical considerations
            """),
            agent=agent
        )

    def deployment_task(self, agent, deployment_config, monitoring_requirements):
        """
        Task for deploying models to production

        Args:
            agent: Deployment engineer agent
            deployment_config: Deployment configuration and platform
            monitoring_requirements: Monitoring and alerting requirements
        """
        return Task(
            description=dedent(f"""
                Deploy ML model to production with comprehensive MLOps:

                Deployment Configuration: {deployment_config}
                Monitoring Requirements: {monitoring_requirements}

                Your responsibilities:

                1. Model Packaging:
                   - Serialize model with versioning
                   - Package dependencies (requirements.txt, conda env)
                   - Create model Docker container
                   - Include preprocessing pipeline
                   - Bundle model artifacts and configs

                2. Serving Infrastructure:
                   - Design serving architecture:
                     * REST API (FastAPI, Flask)
                     * Batch inference pipeline
                     * Real-time streaming (if needed)
                   - Implement prediction endpoint
                   - Add input validation
                   - Implement error handling
                   - Set up logging and tracing

                3. Deployment Strategy:
                   - Choose deployment approach:
                     * Blue-green deployment (zero downtime)
                     * Canary deployment (gradual rollout)
                     * A/B testing (compare models)
                     * Shadow mode (validate before full deploy)
                   - Create deployment pipeline
                   - Implement rollback mechanism
                   - Set up environment variables and secrets

                4. Infrastructure as Code:
                   - Create Kubernetes manifests or Terraform configs
                   - Define resource requirements (CPU, GPU, memory)
                   - Set up auto-scaling rules
                   - Configure load balancing
                   - Implement health checks

                5. CI/CD Pipeline:
                   - Set up continuous integration:
                     * Automated testing (unit, integration)
                     * Code quality checks
                     * Security scanning
                   - Configure continuous deployment:
                     * Automated model deployment
                     * Environment promotion (dev → staging → prod)
                     * Approval workflows

                6. Model Monitoring:
                   - Implement performance monitoring:
                     * Prediction latency (p50, p95, p99)
                     * Throughput (requests per second)
                     * Error rates
                     * Resource utilization
                   - Set up model quality monitoring:
                     * Prediction distribution tracking
                     * Data drift detection
                     * Concept drift detection
                     * Model performance degradation alerts
                   - Configure business metrics monitoring:
                     * Conversion rates
                     * Revenue impact
                     * User engagement

                7. Alerting and Incident Response:
                   - Define alert thresholds and SLOs
                   - Set up alerting channels (PagerDuty, Slack)
                   - Create runbooks for common issues
                   - Implement automated remediation where possible
                   - Define escalation procedures

                8. Model Governance:
                   - Implement model versioning
                   - Set up model registry (MLflow Model Registry)
                   - Define model approval workflow
                   - Track model lineage and provenance
                   - Ensure compliance and auditability
                   - Document model changes and updates

                9. Documentation:
                   - Create deployment documentation
                   - Write API documentation (OpenAPI/Swagger)
                   - Provide usage examples
                   - Create troubleshooting guide
                   - Document monitoring and alerting setup

                Provide comprehensive deployment plan and operations guide.
            """),
            expected_output=dedent("""
                A comprehensive deployment and operations plan containing:
                - Deployment architecture diagram:
                  * Infrastructure components
                  * Data flow
                  * Service dependencies
                - Model packaging details:
                  * Docker image specifications
                  * Model version
                  * Dependencies list
                  * Artifact locations
                - Serving configuration:
                  * API endpoint specifications
                  * Request/response schemas
                  * Authentication and authorization
                  * Rate limiting settings
                - Deployment strategy:
                  * Chosen approach (blue-green, canary, etc.)
                  * Rollout plan and timeline
                  * Rollback procedures
                  * Risk mitigation
                - Infrastructure specifications:
                  * Kubernetes/cloud platform configs
                  * Resource requirements and limits
                  * Auto-scaling policies
                  * Cost estimates
                - CI/CD pipeline:
                  * Pipeline stages
                  * Automated tests
                  * Deployment automation
                  * Environment promotion workflow
                - Monitoring setup:
                  * Metrics to track (with thresholds)
                  * Dashboard specifications
                  * Data drift detection methods
                  * Performance baseline
                - Alerting configuration:
                  * Alert definitions and thresholds
                  * Notification channels
                  * On-call rotation
                  * SLO/SLA targets
                - Operational procedures:
                  * Deployment checklist
                  * Runbooks for incidents
                  * Monitoring dashboard access
                  * Model update process
                - Governance framework:
                  * Model versioning scheme
                  * Approval workflow
                  * Compliance requirements
                  * Audit logging
                - Documentation links:
                  * API documentation URL
                  * Internal wiki/confluence pages
                  * Monitoring dashboards
                  * Code repositories
            """),
            agent=agent
        )
