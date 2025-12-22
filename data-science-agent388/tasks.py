"""
Data Science Tasks
CrewAI task definitions for analytics and modeling workflows
"""

from crewai import Task
from textwrap import dedent


class DataScienceTasks:
    """Task definitions for data science workflow"""

    def exploratory_analysis_task(self, agent, dataset_description, analysis_objectives):
        """
        Task for performing exploratory data analysis

        Args:
            agent: Data analyst agent
            dataset_description: Description of the dataset
            analysis_objectives: Specific analysis goals
        """
        return Task(
            description=dedent(f"""
                Perform comprehensive exploratory data analysis on the following dataset:

                Dataset: {dataset_description}
                Objectives: {analysis_objectives}

                Your responsibilities:

                1. Data Overview:
                   - Examine dataset structure and dimensions
                   - Review data types and schema
                   - Identify target variable(s) and features
                   - Check for data quality issues

                2. Descriptive Statistics:
                   - Calculate summary statistics (mean, median, std, min, max)
                   - Analyze distributions for numerical features
                   - Examine frequency distributions for categorical features
                   - Identify skewness, kurtosis, and outliers

                3. Data Quality Assessment:
                   - Calculate missing value percentages
                   - Identify duplicate records
                   - Detect anomalies and outliers
                   - Flag data quality issues

                4. Feature Analysis:
                   - Analyze correlation between features
                   - Identify highly correlated features
                   - Detect multicollinearity
                   - Analyze feature importance signals

                5. Target Variable Analysis:
                   - Examine target distribution
                   - Check for class imbalance (classification)
                   - Analyze target-feature relationships
                   - Identify potential predictors

                6. Visualization Plan:
                   - Histograms for numerical distributions
                   - Box plots for outlier detection
                   - Correlation heatmaps
                   - Scatter plots for relationships
                   - Bar charts for categorical features

                7. Initial Insights:
                   - Identify patterns and trends
                   - Highlight interesting findings
                   - Suggest features for modeling
                   - Flag potential challenges

                Provide a comprehensive EDA report with findings and visualizations.
            """),
            expected_output=dedent("""
                A comprehensive exploratory data analysis report containing:
                - Dataset overview (rows, columns, data types)
                - Summary statistics table
                - Missing value analysis
                - Distribution analysis for key features
                - Correlation analysis with heatmap description
                - Outlier detection results
                - Target variable analysis
                - Key patterns and trends identified
                - Recommended features for modeling
                - Data quality issues and recommendations
                - Visualization descriptions (what to plot)
                - Initial hypotheses for testing
            """),
            agent=agent
        )

    def model_building_task(self, agent, problem_type, model_requirements):
        """
        Task for building and training ML models

        Args:
            agent: Model builder agent
            problem_type: Type of ML problem (regression, classification, clustering)
            model_requirements: Specific modeling requirements and constraints
        """
        return Task(
            description=dedent(f"""
                Build and train machine learning models for the following problem:

                Problem Type: {problem_type}
                Requirements: {model_requirements}

                Your responsibilities:

                1. Feature Engineering:
                   - Create new features from existing ones
                   - Encode categorical variables (one-hot, label encoding)
                   - Scale/normalize numerical features
                   - Handle missing values (imputation strategies)
                   - Create interaction features if beneficial
                   - Apply dimensionality reduction if needed (PCA, t-SNE)

                2. Data Preparation:
                   - Split data into train/validation/test sets
                   - Handle class imbalance (SMOTE, class weights)
                   - Create cross-validation folds
                   - Prepare feature matrices and target vectors

                3. Model Selection:
                   - Identify candidate algorithms appropriate for the problem
                   - For Classification: Logistic Regression, Random Forest, XGBoost, SVM, Neural Networks
                   - For Regression: Linear Regression, Ridge, Lasso, Random Forest, XGBoost, Neural Networks
                   - For Clustering: K-Means, DBSCAN, Hierarchical
                   - Consider ensemble methods

                4. Model Training:
                   - Train baseline models
                   - Implement cross-validation
                   - Train advanced models
                   - Create ensemble models if beneficial

                5. Hyperparameter Tuning:
                   - Define hyperparameter search spaces
                   - Apply Grid Search or Random Search
                   - Use Bayesian Optimization for complex models
                   - Optimize for specified metric

                6. Model Evaluation:
                   - Calculate performance metrics:
                     * Classification: Accuracy, Precision, Recall, F1, ROC-AUC
                     * Regression: RMSE, MAE, R², MAPE
                     * Clustering: Silhouette Score, Davies-Bouldin Index
                   - Analyze confusion matrix (classification)
                   - Plot ROC curves and precision-recall curves
                   - Examine feature importance
                   - Assess overfitting/underfitting

                7. Model Comparison:
                   - Compare all trained models
                   - Select best model based on validation performance
                   - Analyze trade-offs (accuracy vs interpretability)
                   - Document model selection rationale

                8. Final Model Testing:
                   - Evaluate best model on test set
                   - Generate predictions
                   - Analyze error patterns
                   - Document model limitations

                Provide a comprehensive modeling report with results and recommendations.
            """),
            expected_output=dedent("""
                A comprehensive machine learning modeling report containing:
                - Feature engineering summary (new features created)
                - Data preparation details (train/val/test split sizes)
                - List of models trained with brief descriptions
                - Hyperparameter tuning results (best parameters found)
                - Model performance comparison table (all models with metrics)
                - Best model selection with justification
                - Detailed performance metrics for best model
                - Feature importance analysis
                - Test set performance results
                - Model strengths and limitations
                - Overfitting/underfitting analysis
                - Recommendations for model improvement
                - Model deployment readiness assessment
            """),
            agent=agent
        )

    def insights_generation_task(self, agent, business_context):
        """
        Task for generating business insights and recommendations

        Args:
            agent: Insights generator agent
            business_context: Business context and decision-making requirements
        """
        return Task(
            description=dedent(f"""
                Generate actionable business insights and recommendations based on the analysis:

                Business Context: {business_context}

                Your responsibilities:

                1. Key Findings Summary:
                   - Summarize most important analytical findings
                   - Highlight statistical significance of results
                   - Translate technical metrics into business terms
                   - Prioritize findings by business impact

                2. Business Impact Analysis:
                   - Quantify potential business impact
                   - Estimate ROI of implementing recommendations
                   - Identify affected business processes
                   - Assess implementation feasibility

                3. Actionable Recommendations:
                   - Provide specific, actionable recommendations
                   - Prioritize recommendations by impact and effort
                   - Define success metrics for each recommendation
                   - Outline implementation steps

                4. Risk Assessment:
                   - Identify risks and limitations
                   - Discuss model uncertainty and confidence
                   - Highlight data quality concerns
                   - Document assumptions made

                5. Stakeholder Communication:
                   - Create executive summary (non-technical)
                   - Explain methodology in simple terms
                   - Use business language and metrics
                   - Provide visual aids descriptions

                6. Next Steps:
                   - Recommend additional analyses
                   - Suggest data collection improvements
                   - Propose A/B testing strategies
                   - Outline model monitoring plan

                7. Success Metrics:
                   - Define KPIs to track
                   - Set baseline measurements
                   - Establish target improvements
                   - Create monitoring dashboard plan

                Generate a comprehensive insights and recommendations report.
            """),
            expected_output=dedent("""
                A comprehensive business insights report containing:
                - Executive Summary (1-2 paragraphs, non-technical)
                - Top 5 Key Findings (with business impact)
                - Detailed Insights:
                  * What the data shows
                  * Why it matters
                  * Statistical confidence
                - Business Impact Quantification:
                  * Estimated revenue impact
                  * Cost savings potential
                  * Efficiency improvements
                - Prioritized Recommendations (with rationale):
                  1. High impact, low effort (quick wins)
                  2. High impact, high effort (strategic)
                  3. Low impact, low effort (nice to have)
                - Implementation Roadmap:
                  * Phase 1: Immediate actions (0-30 days)
                  * Phase 2: Short-term (1-3 months)
                  * Phase 3: Long-term (3-12 months)
                - Risk and Limitations:
                  * Model limitations
                  * Data quality concerns
                  * Assumptions made
                - Success Metrics and KPIs:
                  * Metrics to track
                  * Baseline values
                  * Target improvements
                - Next Steps and Future Work
                - Appendix: Technical Details (for reference)
            """),
            agent=agent
        )
