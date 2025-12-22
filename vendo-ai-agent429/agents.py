from crewai import Agent
from tools import VendoAITools

class VendoAIAgents:
    def __init__(self):
        self.tools = VendoAITools()

    def product_specialist(self):
        return Agent(
            role='AI Product Specialist',
            goal='Provide intelligent product recommendations and sales assistance',
            backstory="""Expert sales assistant with deep product knowledge who
            provides personalized recommendations and answers customer questions.""",
            tools=[
                self.tools.recommend_products,
                self.tools.answer_product_questions,
                self.tools.compare_products
            ],
            verbose=True,
            allow_delegation=False
        )

    def customer_insights_analyst(self):
        return Agent(
            role='Customer Insights Analyst',
            goal='Analyze customer behavior and preferences for personalization',
            backstory="""Data analyst specializing in customer behavior, purchase
            patterns, and personalization strategies for improved sales.""",
            tools=[
                self.tools.analyze_customer_behavior,
                self.tools.predict_preferences,
                self.tools.segment_customers
            ],
            verbose=True,
            allow_delegation=False
        )

    def sales_optimizer(self):
        return Agent(
            role='Sales Optimization Specialist',
            goal='Optimize sales strategies and increase conversion rates',
            backstory="""Sales strategy expert who optimizes pricing, promotions,
            upselling, and cross-selling for maximum revenue.""",
            tools=[
                self.tools.optimize_pricing,
                self.tools.create_promotions,
                self.tools.suggest_upsells
            ],
            verbose=True,
            allow_delegation=False
        )

    def vendo_coordinator(self):
        return Agent(
            role='Vendo AI Coordinator',
            goal='Coordinate all sales AI functions for optimal customer experience',
            backstory="""Senior AI coordinator managing product recommendations,
            customer insights, and sales optimization for complete solution.""",
            tools=[
                self.tools.generate_sales_report,
                self.tools.calculate_conversion_metrics,
                self.tools.recommend_strategies
            ],
            verbose=True,
            allow_delegation=True
        )
