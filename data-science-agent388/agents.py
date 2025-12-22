"""
Data Science Agent System
CrewAI implementation for analytics and modeling workflows
Migrated from Google ADK to CrewAI framework
"""

from crewai import Agent
from textwrap import dedent


class DataScienceAgents:
    """Data Science specialist agents for analytics and modeling"""

    def data_analyst_agent(self):
        """
        Agent responsible for exploratory data analysis and insights
        Performs statistical analysis, visualization, and hypothesis testing
        """
        return Agent(
            role="Data Analyst",
            goal="Perform comprehensive exploratory data analysis and uncover meaningful insights",
            backstory=dedent("""
                You are an expert data analyst with deep knowledge of statistics,
                data visualization, and analytical thinking. You excel at exploratory
                data analysis (EDA), identifying patterns, trends, and anomalies in data.
                You understand descriptive statistics, distributions, correlations, and
                hypothesis testing. You create compelling visualizations and translate
                complex data into actionable insights. You're proficient with pandas,
                numpy, matplotlib, seaborn, and plotly for data exploration and
                visualization.
            """),
            verbose=True,
            allow_delegation=False
        )

    def model_builder_agent(self):
        """
        Agent responsible for building and training machine learning models
        Handles feature selection, model training, hyperparameter tuning
        """
        return Agent(
            role="Machine Learning Model Builder",
            goal="Design, train, and optimize machine learning models for predictive analytics",
            backstory=dedent("""
                You are a skilled machine learning engineer with expertise in building
                and optimizing predictive models. You understand the full ML lifecycle
                from feature engineering to model deployment. You're proficient with
                scikit-learn, XGBoost, LightGBM, and deep learning frameworks like
                TensorFlow and PyTorch. You know when to use different algorithms
                (regression, classification, clustering, etc.), how to perform feature
                selection, handle imbalanced data, and prevent overfitting. You excel
                at hyperparameter tuning and model validation techniques including
                cross-validation, train-test splits, and ensemble methods.
            """),
            verbose=True,
            allow_delegation=False
        )

    def insights_generator_agent(self):
        """
        Agent responsible for generating business insights and recommendations
        Translates model results into actionable business recommendations
        """
        return Agent(
            role="Insights and Recommendations Generator",
            goal="Translate analytical findings into clear, actionable business insights and recommendations",
            backstory=dedent("""
                You are a business-savvy data scientist who bridges the gap between
                technical analysis and business strategy. You excel at interpreting
                model results, explaining complex statistical concepts in simple terms,
                and generating actionable recommendations. You understand business metrics,
                KPIs, and how data insights drive decision-making. You create executive
                summaries, impact analyses, and recommendation frameworks that
                stakeholders can act upon. You're skilled at storytelling with data,
                creating compelling narratives that highlight key findings and their
                business implications.
            """),
            verbose=True,
            allow_delegation=False
        )
