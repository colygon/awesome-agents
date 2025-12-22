from crewai import Task
from textwrap import dedent

class TravelPlannerTasks:
    def research_destination_task(self, agent, preferences):
        return Task(
            description=dedent(f"""
                Research and recommend travel destinations based on preferences.

                Preferences: {preferences}

                Steps:
                1. Analyze traveler preferences and interests
                2. Research suitable destinations
                3. Consider seasonal factors and weather
                4. Evaluate attractions and activities
                5. Recommend top 3 destinations with rationale
            """),
            agent=agent,
            expected_output="Detailed destination recommendations with pros/cons"
        )

    def search_flights_task(self, agent, destination, dates, budget):
        return Task(
            description=dedent(f"""
                Find optimal flight options for the trip.

                Destination: {destination}
                Dates: {dates}
                Budget: {budget}

                Steps:
                1. Search for available flights
                2. Compare prices and routes
                3. Evaluate connection times and duration
                4. Consider airline reputation
                5. Recommend best flight options
            """),
            agent=agent,
            expected_output="Flight recommendations with prices and schedules"
        )

    def find_accommodation_task(self, agent, destination, dates, preferences):
        return Task(
            description=dedent(f"""
                Find suitable accommodation options.

                Destination: {destination}
                Dates: {dates}
                Preferences: {preferences}

                Steps:
                1. Search for hotels/accommodations
                2. Filter by location and amenities
                3. Compare prices and reviews
                4. Check availability for dates
                5. Recommend top accommodation options
            """),
            agent=agent,
            expected_output="Accommodation recommendations with details and pricing"
        )

    def create_itinerary_task(self, agent, destination, duration, interests):
        return Task(
            description=dedent(f"""
                Create a detailed day-by-day itinerary.

                Destination: {destination}
                Duration: {duration}
                Interests: {interests}

                Steps:
                1. Research activities and attractions
                2. Plan daily schedules with balance
                3. Include meal suggestions
                4. Add transportation details
                5. Create comprehensive itinerary
            """),
            agent=agent,
            expected_output="Complete day-by-day itinerary with activities and logistics"
        )

    def calculate_budget_task(self, agent, trip_details):
        return Task(
            description=dedent(f"""
                Calculate comprehensive travel budget.

                Trip Details: {trip_details}

                Steps:
                1. Sum major expenses (flights, hotels)
                2. Estimate daily spending
                3. Include activity costs
                4. Add buffer for contingencies
                5. Provide detailed budget breakdown
            """),
            agent=agent,
            expected_output="Detailed budget breakdown with cost estimates and tips"
        )
