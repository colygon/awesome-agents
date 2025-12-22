# Data Science Workflow - CrewAI Implementation

**Agent ID:** 388
**Category:** Data Science
**Framework:** CrewAI
**Migration:** Google ADK → CrewAI

## Overview

A comprehensive data science workflow system built with CrewAI framework, featuring three specialized agents that handle exploratory data analysis, model building, and business insights generation. Migrated from Google ADK to demonstrate modern multi-agent orchestration for analytics and machine learning workflows.

## Architecture

### Agents

1. **Data Analyst**
   - Performs exploratory data analysis (EDA)
   - Statistical analysis and hypothesis testing
   - Data visualization planning
   - Pattern and trend identification

2. **Machine Learning Model Builder**
   - Feature engineering and selection
   - Model training and hyperparameter tuning
   - Cross-validation and performance evaluation
   - Model comparison and selection

3. **Insights and Recommendations Generator**
   - Translates technical results to business insights
   - Generates actionable recommendations
   - Creates executive summaries
   - Defines success metrics and KPIs

### Workflow

```
Data → EDA & Analysis → Model Building → Business Insights → Recommendations
```

The agents work sequentially, with each agent building upon the previous agent's output to create a complete data science workflow.

## Features

### Exploratory Data Analysis
- Comprehensive statistical summaries
- Distribution analysis and visualization
- Correlation analysis and multicollinearity detection
- Missing value and outlier analysis
- Target variable analysis
- Feature importance signals

### Machine Learning Modeling
- Automated feature engineering
- Support for classification, regression, and clustering
- Multiple algorithm comparison:
  - **Classification**: Logistic Regression, Random Forest, XGBoost, SVM, Neural Networks
  - **Regression**: Linear, Ridge, Lasso, Random Forest, XGBoost, Neural Networks
  - **Clustering**: K-Means, DBSCAN, Hierarchical
- Hyperparameter tuning (Grid Search, Random Search, Bayesian Optimization)
- Cross-validation and ensemble methods
- Comprehensive performance metrics
- Feature importance analysis

### Business Insights
- Executive summaries in non-technical language
- Quantified business impact analysis
- Prioritized recommendations (impact vs. effort matrix)
- Implementation roadmap with phases
- Risk assessment and limitations
- Success metrics and KPI definitions
- ROI estimation

## Installation

```bash
# Clone or download this directory
cd data-science-agent388

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Configure environment
cp .env.example .env
# Edit .env and add your OPENAI_API_KEY
```

## Configuration

Edit the `.env` file:

```env
OPENAI_API_KEY=sk-your-openai-api-key-here
```

## Usage

### Basic Usage

```bash
python main.py
```

This runs the example workflow with customer churn prediction.

### Custom Workflow

```python
from main import run_data_science_workflow

result = run_data_science_workflow(
    dataset_description="Your dataset description with features and target",
    analysis_objectives="What you want to discover and analyze",
    problem_type="Classification/Regression/Clustering",
    model_requirements="Performance metrics, constraints, interpretability needs",
    business_context="Business problem, stakeholders, decision requirements"
)
```

### Example Output

```
================================================================================
DATA SCIENCE WORKFLOW - CREWAI
================================================================================

Dataset: Customer Churn Dataset - 10,000 records
Problem Type: Binary Classification (Churn Prediction)

Starting data science workflow...

[Data Analyst] Performing exploratory data analysis...
[Data Analyst] Dataset: 10,000 rows, 20 features
[Data Analyst] Target distribution: 80% No Churn, 20% Churn (imbalanced)
[Data Analyst] Key correlations found: contract_type, tenure, monthly_charges
[Data Analyst] Missing values: <5% in 3 features

[Model Builder] Engineering features...
[Model Builder] Training models: Logistic Regression, Random Forest, XGBoost
[Model Builder] Best model: XGBoost with F1=0.82, Recall=0.78
[Model Builder] Top features: tenure, contract_type, customer_service_calls

[Insights Generator] Generating business insights...
[Insights Generator] Top finding: Month-to-month contracts have 3x churn rate
[Insights Generator] Recommendation: Target month-to-month customers for upgrades
[Insights Generator] Estimated impact: Reduce churn by 6% → Save $600K annually

================================================================================
WORKFLOW EXECUTION COMPLETE
================================================================================
```

## Use Cases

1. **Customer Churn Prediction**: Identify at-risk customers and retention strategies
2. **Sales Forecasting**: Predict future sales and optimize inventory
3. **Fraud Detection**: Identify fraudulent transactions and patterns
4. **Customer Segmentation**: Group customers for targeted marketing
5. **Price Optimization**: Determine optimal pricing strategies
6. **Demand Forecasting**: Predict product demand for planning
7. **Risk Assessment**: Evaluate credit risk or insurance risk
8. **A/B Test Analysis**: Analyze experiment results and recommendations

## ADK to CrewAI Migration

This application was migrated from Google Agent Development Kit (ADK) to CrewAI framework:

### Key Changes

1. **Agent Definition**: ADK agents → CrewAI Agent class with role/goal/backstory
2. **Task Structure**: ADK tasks → CrewAI Task with description/expected_output
3. **Orchestration**: ADK workflow → CrewAI Crew with Process.sequential
4. **LLM Backend**: Google Gemini → OpenAI GPT-4 via LangChain

### Migration Benefits

- More structured agent definitions with explicit roles and goals
- Better task output specifications for each workflow stage
- Improved orchestration with sequential process
- Ecosystem compatibility with LangChain and scikit-learn
- Active community and regular updates
- Better separation of concerns (analysis → modeling → insights)

## Architecture Diagram

```
┌─────────────────────────────────────────────────────────────┐
│                   Data Science Workflow                      │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
                    ┌──────────────────┐
                    │   Input Data     │
                    │  - Customer data │
                    │  - Transactions  │
                    │  - Features      │
                    └──────────────────┘
                              │
                              ▼
           ┌─────────────────────────────────────┐
           │       Data Analyst Agent            │
           │  - Exploratory Data Analysis        │
           │  - Statistical Summaries            │
           │  - Correlation Analysis             │
           │  - Visualization Planning           │
           └─────────────────────────────────────┘
                              │
                              ▼
           ┌─────────────────────────────────────┐
           │    ML Model Builder Agent           │
           │  - Feature Engineering              │
           │  - Model Training                   │
           │  - Hyperparameter Tuning            │
           │  - Model Evaluation                 │
           └─────────────────────────────────────┘
                              │
                              ▼
           ┌─────────────────────────────────────┐
           │  Insights Generator Agent           │
           │  - Business Impact Analysis         │
           │  - Actionable Recommendations       │
           │  - Executive Summaries              │
           │  - Success Metrics Definition       │
           └─────────────────────────────────────┘
                              │
                              ▼
                    ┌──────────────────┐
                    │ Business Actions │
                    │  - Strategies    │
                    │  - Roadmap       │
                    │  - KPIs          │
                    └──────────────────┘
```

## Output Structure

### 1. EDA Report
- Dataset overview
- Statistical summaries
- Distribution analysis
- Correlation insights
- Data quality assessment
- Recommended features

### 2. Modeling Report
- Feature engineering summary
- Model comparison table
- Best model selection
- Performance metrics
- Feature importance
- Overfitting analysis

### 3. Business Insights Report
- Executive summary
- Key findings (top 5)
- Business impact quantification
- Prioritized recommendations
- Implementation roadmap
- Success metrics
- Risk assessment

## Requirements

- Python 3.10+
- OpenAI API key
- CrewAI >= 0.86.0
- LangChain OpenAI >= 0.3.0
- scikit-learn >= 1.3.0
- pandas >= 2.0.0
- numpy >= 1.24.0

## Next Steps

### Recommended Enhancements
1. Integrate actual ML model training with scikit-learn
2. Add automated visualization generation (matplotlib, seaborn, plotly)
3. Implement model persistence (joblib, pickle)
4. Create Streamlit dashboard for interactive analysis
5. Add MLflow for experiment tracking
6. Implement automated model monitoring
7. Add support for deep learning (TensorFlow, PyTorch)
8. Create API endpoints for model serving

### Deployment Options
1. **Jupyter Notebook**: Interactive analysis environment
2. **Streamlit**: Web-based analytics dashboard
3. **Docker**: Containerized deployment
4. **MLflow**: Model registry and serving
5. **AWS SageMaker**: Cloud ML platform integration
6. **Airflow**: Scheduled workflow execution

## License

MIT License - See source repository for details

## Credits

Migrated from Google ADK samples to CrewAI framework
Generated with Claude Code
Co-Authored-By: Claude Sonnet 4.5 <noreply@anthropic.com>
