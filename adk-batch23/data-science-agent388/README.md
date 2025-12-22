# Data Science Agent - CrewAI Implementation

End-to-end data science workflow automation using CrewAI multi-agent system.

## Overview

A comprehensive data science platform powered by CrewAI with five specialized agents that collaborate through the complete data science workflow, from exploratory analysis to model deployment planning.

### Agents

1. **Senior Data Analyst**
   - Role: Exploratory data analysis and insight discovery
   - Capabilities: Statistical analysis, pattern detection, data quality assessment
   - Tools: File reading, directory exploration
   - Output: Comprehensive EDA report

2. **ML Feature Engineering Specialist**
   - Role: Design and create effective ML features
   - Capabilities: Feature creation, transformation, selection, preprocessing
   - Tools: File reading
   - Output: Detailed feature engineering plan

3. **Machine Learning Engineer**
   - Role: Build and optimize ML models
   - Capabilities: Algorithm selection, training strategy, hyperparameter tuning
   - Tools: Web search for best practices
   - Output: Complete model development strategy

4. **ML Model Evaluation Specialist**
   - Role: Evaluate model performance
   - Capabilities: Metrics selection, validation, comparison, deployment assessment
   - Tools: None (focuses on evaluation)
   - Output: Comprehensive evaluation framework

5. **Data Science Communications Specialist**
   - Role: Translate technical findings to business insights
   - Capabilities: Executive summaries, visualization planning, ROI analysis
   - Tools: None (focuses on communication)
   - Output: Executive-level project summary

## Features

- **Complete DS workflow**: From EDA to deployment planning
- **Multi-agent collaboration**: Five specialized experts working together
- **Project type flexibility**: Classification, regression, clustering
- **Business-focused**: Executive summaries and ROI analysis
- **Best practices**: Current ML techniques and methodologies
- **Code examples**: Implementation guidance throughout
- **Production-ready**: Deployment and monitoring considerations

## Installation

```bash
# Install dependencies
pip install -r requirements.txt

# Set up environment variables
cp .env.example .env
# Edit .env and add your API keys
```

## Configuration

Required API keys:
- `OPENAI_API_KEY`: OpenAI API key for GPT-4

Optional:
- `SERPER_API_KEY`: Serper API key for web search

## Usage

### Command Line

```bash
python main.py
```

Follow the prompts to:
1. Define your problem statement
2. Describe available data
3. Select project type (classification/regression/clustering)
4. Specify target variable (if applicable)
5. Review complete data science workflow
6. Save project summary

### Python API

```python
from main import run_data_science_project, save_project_output

# Run data science project
result = run_data_science_project(
    problem_statement="Predict customer churn to improve retention",
    data_description="2 years of customer transaction, demographic, and engagement data",
    target_variable="churned",
    project_type="classification"
)

# Access individual components
print(result["eda_report"])
print(result["feature_engineering"])
print(result["model_strategy"])
print(result["evaluation_framework"])
print(result["executive_summary"])

# Save executive summary
save_project_output(result["executive_summary"], "churn-prediction-summary.md")
```

## Data Science Workflow

### Phase 1: Exploratory Data Analysis
**Agent**: Senior Data Analyst

Comprehensive analysis including:
- Dataset structure and size
- Variable types and distributions
- Missing values analysis
- Data quality assessment
- Descriptive statistics
- Correlation analysis
- Distribution analysis
- Outlier detection
- Pattern and trend identification
- Initial hypotheses

### Phase 2: Feature Engineering
**Agent**: ML Feature Engineering Specialist

Feature engineering plan covering:
- **Feature Creation**: Derived features, interactions, domain-specific
- **Transformation**: Encoding, scaling, distribution handling
- **Feature Selection**: Importance ranking, dimensionality reduction
- **Preprocessing**: Missing values, outliers, train/test split

### Phase 3: Model Development
**Agent**: Machine Learning Engineer

Model strategy including:
- **Algorithm Selection**: 3-5 candidate models with justification
- **Training Strategy**: Cross-validation, splits, metrics, baseline
- **Hyperparameter Tuning**: Key parameters, search strategy
- **Implementation**: Pipeline, serialization, reproducibility

### Phase 4: Model Evaluation
**Agent**: ML Model Evaluation Specialist

Evaluation framework covering:
- **Metrics**: Primary, secondary, and business metrics
- **Validation**: Cross-validation, overfitting detection, learning curves
- **Comparison**: Model comparison framework, statistical testing
- **Deployment**: Performance expectations, monitoring, maintenance

### Phase 5: Business Communication
**Agent**: Data Science Communications Specialist

Executive summary including:
- Problem and business impact
- Key data insights
- Model performance in business terms
- Implementation roadmap
- Expected ROI and success criteria

## Project Types

### Classification
Predict categorical outcomes (binary or multi-class)
- Customer churn prediction
- Fraud detection
- Sentiment analysis
- Disease diagnosis
- Quality control

### Regression
Predict continuous values
- Sales forecasting
- Price prediction
- Demand estimation
- Risk scoring
- Performance prediction

### Clustering
Group similar observations
- Customer segmentation
- Anomaly detection
- Document clustering
- Product recommendation
- Market basket analysis

## Example Projects

### Customer Churn Prediction
```python
result = run_data_science_project(
    problem_statement="Predict customer churn to improve retention strategies",
    data_description="Customer transaction history, demographics, support interactions over 2 years",
    target_variable="churned",
    project_type="classification"
)
```

### House Price Prediction
```python
result = run_data_science_project(
    problem_statement="Predict house prices for real estate valuation",
    data_description="Property features, location data, historical sales, neighborhood statistics",
    target_variable="sale_price",
    project_type="regression"
)
```

### Customer Segmentation
```python
result = run_data_science_project(
    problem_statement="Segment customers for targeted marketing campaigns",
    data_description="Customer purchase history, browsing behavior, demographics, preferences",
    target_variable=None,
    project_type="clustering"
)
```

## ML Algorithm Recommendations

### Classification
- Logistic Regression (baseline, interpretable)
- Random Forest (robust, feature importance)
- Gradient Boosting (XGBoost, LightGBM, CatBoost)
- Neural Networks (complex patterns)
- Support Vector Machines (small datasets)

### Regression
- Linear Regression (baseline, interpretable)
- Ridge/Lasso Regression (regularization)
- Random Forest Regressor (non-linear)
- Gradient Boosting Regressor (high performance)
- Neural Networks (complex relationships)

### Clustering
- K-Means (spherical clusters)
- DBSCAN (arbitrary shapes, noise handling)
- Hierarchical Clustering (dendrogram visualization)
- Gaussian Mixture Models (probabilistic)
- Agglomerative Clustering (hierarchical)

## Evaluation Metrics

### Classification
- **Accuracy**: Overall correctness
- **Precision**: Positive prediction accuracy
- **Recall**: True positive rate
- **F1-Score**: Harmonic mean of precision/recall
- **ROC-AUC**: Classification performance across thresholds
- **Confusion Matrix**: Detailed error analysis

### Regression
- **MAE**: Mean Absolute Error
- **RMSE**: Root Mean Squared Error
- **R²**: Coefficient of determination
- **MAPE**: Mean Absolute Percentage Error
- **Residual Analysis**: Error patterns

### Clustering
- **Silhouette Score**: Cluster quality
- **Davies-Bouldin Index**: Cluster separation
- **Calinski-Harabasz Index**: Cluster density
- **Inertia**: Within-cluster sum of squares
- **Visual Inspection**: Cluster plots

## Best Practices

### Data Preparation
1. Start with data quality assessment
2. Handle missing values appropriately
3. Detect and handle outliers
4. Ensure proper train/test split
5. Avoid data leakage

### Feature Engineering
1. Create domain-specific features
2. Handle categorical variables properly
3. Scale features when needed
4. Remove multicollinear features
5. Document feature engineering logic

### Model Development
1. Start with simple baseline models
2. Use cross-validation for robust estimates
3. Tune hyperparameters systematically
4. Prevent overfitting (regularization, early stopping)
5. Document model decisions

### Model Evaluation
1. Use multiple evaluation metrics
2. Analyze error patterns
3. Test on held-out data
4. Compare against baseline
5. Consider business context

## Migration from ADK

### Key Changes

| ADK Component | CrewAI Equivalent |
|---------------|-------------------|
| Data analyzer | Senior Data Analyst agent |
| Feature engineer | ML Feature Engineering Specialist |
| Model builder | Machine Learning Engineer |
| Evaluator | ML Model Evaluation Specialist |
| Reporter | Data Science Communications Specialist |
| Gemini model | OpenAI GPT-4 |

### Architecture Differences

- **ADK**: Sequential task execution
- **CrewAI**: Multi-agent collaboration with context sharing
- **LLM**: Migrated from Google Gemini to OpenAI GPT-4
- **Tools**: CrewAI tools for file and directory access

## Output Structure

The system produces comprehensive documentation:

1. **EDA Report**: Statistical analysis and insights
2. **Feature Engineering Plan**: Transformation and selection strategy
3. **Model Strategy**: Algorithm selection and training approach
4. **Evaluation Framework**: Metrics and validation plan
5. **Executive Summary**: Business-focused project overview

## Production Considerations

### Before Deployment
- Validate on recent data
- Test edge cases
- Measure inference time
- Check resource requirements
- Document model assumptions

### Monitoring
- Track model performance metrics
- Monitor data drift
- Log predictions for audit
- Set up alerts for anomalies
- Plan retraining schedule

### Maintenance
- Regular model retraining
- Feature store management
- Version control for models
- A/B testing new models
- Performance benchmarking

## Limitations

- Does not execute actual code or train models
- Requires manual implementation of recommendations
- Limited by training data knowledge cutoff
- Cannot access proprietary datasets
- Recommendations may need customization

## Future Enhancements

- Integration with AutoML platforms
- Automated code generation
- Real-time model training
- Experiment tracking (MLflow, Weights & Biases)
- Model serving integration
- Feature store integration
- Automated hyperparameter tuning
- Ensemble model recommendations
- Explainability analysis (SHAP, LIME)

## Resources

### Learning Resources
- Scikit-learn documentation
- TensorFlow/PyTorch tutorials
- Kaggle competitions
- Machine Learning Mastery
- Towards Data Science

### Tools & Frameworks
- **Data Processing**: pandas, numpy, dask
- **Visualization**: matplotlib, seaborn, plotly
- **ML Libraries**: scikit-learn, xgboost, lightgbm
- **Deep Learning**: TensorFlow, PyTorch, Keras
- **Experiment Tracking**: MLflow, Weights & Biases
- **Model Serving**: FastAPI, TensorFlow Serving

## Original ADK Agent

Based on: Google Agent Development Kit (ADK) Data Science sample

## License

Apache License 2.0
