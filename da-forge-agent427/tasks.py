from crewai import Task
from textwrap import dedent

class DAForgeTasks:
    def analyze_data(self, agent, dataset_info):
        return Task(
            description=dedent(f"""
                Perform exploratory data analysis on the dataset.
                Dataset: {dataset_info}
                Include: summary statistics, patterns, correlations, and anomalies.
            """),
            expected_output="""Data analysis report with statistics, patterns,
                correlations, quality assessment, and initial insights.""",
            agent=agent
        )

    def build_ml_models(self, agent, problem_type):
        return Task(
            description=dedent(f"""
                Build and train machine learning models.
                Problem: {problem_type}
                Include: model selection, training, hyperparameter tuning, evaluation.
            """),
            expected_output="""ML model report with architecture, performance metrics,
                feature importance, and deployment recommendations.""",
            agent=agent
        )

    def create_visualizations(self, agent, insights):
        return Task(
            description=dedent(f"""
                Create visualizations and dashboards.
                Insights: {insights}
                Include: charts, graphs, interactive dashboards, and reports.
            """),
            expected_output="""Visualization package with charts, dashboards,
                and presentation-ready reports.""",
            agent=agent
        )

    def deliver_solution(self, agent):
        return Task(
            description=dedent("""
                Integrate all analyses and deliver comprehensive data science solution.
                Include: executive summary, findings, models, visualizations, recommendations.
            """),
            expected_output="""Complete data science solution with integrated analysis,
                model documentation, visualizations, and actionable recommendations.""",
            agent=agent
        )
