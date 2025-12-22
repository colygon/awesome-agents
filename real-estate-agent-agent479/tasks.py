from crewai import Task
from textwrap import dedent

class RealEstateAgentTasks:
    def search_properties(self, agent, criteria):
        return Task(
            description=dedent(f"""
                Search for properties: {criteria}

                Tasks: Search listings, filter by criteria, identify matches,
                rank properties, prepare viewing list.
            """),
            agent=agent,
            expected_output="List of matching properties with details and viewing recommendations"
        )

    def analyze_market(self, agent, location):
        return Task(
            description=dedent(f"""
                Analyze real estate market: {location}

                Tasks: Research market trends, analyze pricing, identify opportunities,
                assess investment potential, provide insights.
            """),
            agent=agent,
            expected_output="Market analysis report with trends, pricing, and recommendations"
        )

    def prepare_offer(self, agent, property_details):
        return Task(
            description=dedent(f"""
                Prepare offer strategy: {property_details}

                Tasks: Determine fair price, prepare offer terms, develop negotiation
                strategy, identify leverage points.
            """),
            agent=agent,
            expected_output="Offer strategy with pricing recommendations and negotiation tactics"
        )

    def guide_client(self, agent, transaction_stage):
        return Task(
            description=dedent(f"""
                Guide client through: {transaction_stage}

                Tasks: Explain process, provide timeline, identify requirements,
                answer questions, coordinate next steps.
            """),
            agent=agent,
            expected_output="Client guide with process explanation, timeline, and action items"
        )
