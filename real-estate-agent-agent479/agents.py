from crewai import Agent
from tools import PropertySearchTools, MarketAnalysisTools, ClientServiceTools

class RealEstateAgentAgents:
    def property_finder(self):
        return Agent(
            role='Property Finder',
            goal='Find properties matching client criteria and preferences',
            backstory="""You are an expert at finding properties that match client
            needs. You understand neighborhoods, property features, and can identify
            homes with potential.""",
            tools=[
                PropertySearchTools.search_properties,
                PropertySearchTools.filter_listings,
                PropertySearchTools.schedule_viewing
            ],
            verbose=True,
            allow_delegation=False
        )

    def market_analyst(self):
        return Agent(
            role='Market Analyst',
            goal='Analyze real estate market trends and property values',
            backstory="""You are a real estate market expert who analyzes trends,
            property values, and investment potential. You provide data-driven
            insights for buying and selling decisions.""",
            tools=[
                MarketAnalysisTools.analyze_market_trends,
                MarketAnalysisTools.estimate_property_value,
                MarketAnalysisTools.compare_properties
            ],
            verbose=True,
            allow_delegation=False
        )

    def negotiation_specialist(self):
        return Agent(
            role='Negotiation Specialist',
            goal='Negotiate best deals for clients in property transactions',
            backstory="""You are a skilled negotiator who helps clients get the
            best terms in real estate transactions. You understand pricing strategies
            and contract terms.""",
            tools=[
                ClientServiceTools.prepare_offer,
                ClientServiceTools.negotiate_terms,
                MarketAnalysisTools.estimate_property_value
            ],
            verbose=True,
            allow_delegation=False
        )

    def client_advisor(self):
        return Agent(
            role='Client Advisor',
            goal='Guide clients through the real estate buying or selling process',
            backstory="""You are a client-focused advisor who educates and guides
            clients through every step of real estate transactions, from search
            to closing.""",
            tools=[
                ClientServiceTools.create_buyer_guide,
                ClientServiceTools.explain_process,
                PropertySearchTools.schedule_viewing
            ],
            verbose=True,
            allow_delegation=False
        )
