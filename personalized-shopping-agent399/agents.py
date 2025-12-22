from crewai import Agent
from textwrap import dedent
from tools import ShoppingTools, PreferenceTools, RecommendationTools

class PersonalizedShoppingAgents:
    def preference_analyst(self):
        return Agent(
            role='Shopping Preference Analyst',
            goal='Understand customer preferences, style, and shopping behavior',
            backstory=dedent("""\
                You are an expert in understanding customer preferences and
                shopping behavior. You can analyze past purchases, browsing
                history, and stated preferences to build comprehensive customer
                profiles. You excel at identifying patterns and predicting what
                customers will love."""),
            tools=[
                PreferenceTools.analyze_preferences,
                PreferenceTools.build_profile,
                ShoppingTools.analyze_purchase_history
            ],
            verbose=True,
            allow_delegation=False
        )

    def product_researcher(self):
        return Agent(
            role='Product Research Specialist',
            goal='Find and evaluate products that match customer preferences',
            backstory=dedent("""\
                You are a skilled product researcher who knows how to find
                the best products across multiple retailers. You understand
                product features, quality indicators, and pricing. You can
                compare similar products and identify the best value. You
                stay updated on new releases and trending products."""),
            tools=[
                ShoppingTools.search_products,
                ShoppingTools.compare_products,
                ShoppingTools.check_availability
            ],
            verbose=True,
            allow_delegation=False
        )

    def deal_finder(self):
        return Agent(
            role='Deal and Discount Expert',
            goal='Find the best prices, deals, and promotions',
            backstory=dedent("""\
                You are a master at finding deals, discounts, and the best
                prices. You know where to look for coupons, seasonal sales,
                and price drops. You can track price history and predict when
                items will go on sale. You help customers save money while
                getting exactly what they want."""),
            tools=[
                ShoppingTools.find_deals,
                ShoppingTools.track_prices,
                ShoppingTools.apply_coupons
            ],
            verbose=True,
            allow_delegation=False
        )

    def style_consultant(self):
        return Agent(
            role='Personal Style Consultant',
            goal='Provide personalized style advice and product recommendations',
            backstory=dedent("""\
                You are a fashion and style expert who can provide
                personalized recommendations based on customer preferences,
                body type, lifestyle, and current trends. You understand
                color coordination, style combinations, and how to build
                versatile wardrobes. You can recommend products that work
                together and match the customer's aesthetic."""),
            tools=[
                RecommendationTools.recommend_products,
                RecommendationTools.suggest_combinations,
                RecommendationTools.create_outfit
            ],
            verbose=True,
            allow_delegation=False
        )

    def shopping_coordinator(self):
        return Agent(
            role='Personal Shopping Coordinator',
            goal='Orchestrate personalized shopping experiences and compile recommendations',
            backstory=dedent("""\
                You are an expert personal shopper who can coordinate all
                aspects of the shopping experience. You understand how to
                balance preferences, budget, and value. You create curated
                shopping lists and provide detailed recommendations with
                reasoning. You ensure customers have all the information
                they need to make confident purchase decisions."""),
            tools=[RecommendationTools.create_shopping_list],
            verbose=True,
            allow_delegation=False
        )
