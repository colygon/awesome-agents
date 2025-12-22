from crewai import Task
from textwrap import dedent

class DataVisualizationTasks:
    def analyze_data_task(self, agent, dataset):
        return Task(
            description=dedent(f"""
                Analyze the dataset to understand structure and patterns.

                Dataset: {dataset}

                Steps:
                1. Load and inspect the data
                2. Identify data types and dimensions
                3. Calculate basic statistics
                4. Detect patterns and correlations
                5. Identify outliers and anomalies
            """),
            agent=agent,
            expected_output="Comprehensive data analysis with statistics and patterns"
        )

    def design_visualization_task(self, agent, data_analysis, purpose):
        return Task(
            description=dedent(f"""
                Design appropriate visualizations for the data.

                Data Analysis: {data_analysis}
                Purpose: {purpose}

                Steps:
                1. Review data characteristics
                2. Select appropriate chart types
                3. Design visual hierarchy
                4. Choose color palettes
                5. Plan layout and composition
            """),
            agent=agent,
            expected_output="Visualization design plan with chart types and styling"
        )

    def generate_charts_task(self, agent, design_plan, data):
        return Task(
            description=dedent(f"""
                Generate charts and graphs based on design plan.

                Design Plan: {design_plan}
                Data: {data}

                Steps:
                1. Prepare data for visualization
                2. Create individual charts
                3. Apply styling and formatting
                4. Add labels and annotations
                5. Ensure clarity and accuracy
            """),
            agent=agent,
            expected_output="Generated charts with proper formatting and labels"
        )

    def build_dashboard_task(self, agent, charts, purpose):
        return Task(
            description=dedent(f"""
                Build a comprehensive dashboard with multiple visualizations.

                Charts: {charts}
                Purpose: {purpose}

                Steps:
                1. Design dashboard layout
                2. Arrange visualizations effectively
                3. Add titles and descriptions
                4. Include interactive elements
                5. Ensure cohesive design
            """),
            agent=agent,
            expected_output="Complete dashboard with integrated visualizations"
        )

    def extract_insights_task(self, agent, visualizations):
        return Task(
            description=dedent(f"""
                Extract and communicate insights from visualizations.

                Visualizations: {visualizations}

                Steps:
                1. Analyze visualizations for patterns
                2. Identify key trends and outliers
                3. Formulate actionable insights
                4. Prioritize by importance
                5. Create clear summaries
            """),
            agent=agent,
            expected_output="List of actionable insights with supporting evidence"
        )
