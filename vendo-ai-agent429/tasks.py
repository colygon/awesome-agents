from crewai import Task
from textwrap import dedent

class VendoAITasks:
    def assist_customer(self, agent, customer_query):
        return Task(
            description=dedent(f"""
                Assist customer with product recommendations and questions.
                Customer Query: {customer_query}
                Include: product recommendations, Q&A, comparisons.
            """),
            expected_output="""Customer assistance with product recommendations,
                detailed answers, product comparisons, and purchase guidance.""",
            agent=agent
        )

    def analyze_customers(self, agent, customer_data):
        return Task(
            description=dedent(f"""
                Analyze customer behavior and generate insights.
                Customer Data: {customer_data}
                Include: behavior analysis, preference prediction, segmentation.
            """),
            expected_output="""Customer insights with behavior patterns, preferences,
                segments, and personalization opportunities.""",
            agent=agent
        )

    def optimize_sales(self, agent, current_performance):
        return Task(
            description=dedent(f"""
                Optimize sales strategies for better conversion.
                Current Performance: {current_performance}
                Include: pricing optimization, promotions, upsell/cross-sell.
            """),
            expected_output="""Sales optimization plan with pricing strategies,
                promotion recommendations, and upsell/cross-sell opportunities.""",
            agent=agent
        )

    def generate_solution(self, agent):
        return Task(
            description=dedent("""
                Generate comprehensive Vendo AI solution and strategy.
                Include: integrated recommendations, metrics, strategic plan.
            """),
            expected_output="""Complete Vendo AI solution with customer assistance,
                insights, optimization strategies, and performance metrics.""",
            agent=agent
        )
