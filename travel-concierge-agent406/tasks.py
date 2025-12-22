"""Travel Concierge Agent CrewAI Tasks"""

from crewai import Task
from agents import destination_expert, flight_coordinator, accommodation_specialist, itinerary_planner, travel_coordinator


def create_tasks(travel_request: str, budget: str = "moderate", dates: str = "flexible"):
    """Create tasks for travel planning workflow"""

    destination_task = Task(
        description=f"""Research and recommend destinations.

        Request: {travel_request}
        Budget: {budget}
        Dates: {dates}

        Provide 3-5 destination recommendations with reasons.""",
        agent=destination_expert,
        expected_output="Destination recommendations with details"
    )

    flight_task = Task(
        description="""Find flight options for recommended destinations.

        Research flight routes, prices, and timing options.""",
        agent=flight_coordinator,
        expected_output="Flight options with prices and schedules",
        context=[destination_task]
    )

    accommodation_task = Task(
        description="""Find accommodation options for each destination.

        Research hotels, rentals, and lodging matching budget and preferences.""",
        agent=accommodation_specialist,
        expected_output="Accommodation recommendations with pricing",
        context=[destination_task]
    )

    itinerary_task = Task(
        description="""Create detailed day-by-day itineraries.

        Design daily schedules with activities, dining, and logistics.""",
        agent=itinerary_planner,
        expected_output="Complete itinerary with daily breakdown",
        context=[destination_task, accommodation_task]
    )

    coordination_task = Task(
        description="""Coordinate all elements into comprehensive travel plan.

        Synthesize recommendations into complete, bookable travel package.""",
        agent=travel_coordinator,
        expected_output="Complete travel plan with all bookings and details",
        context=[destination_task, flight_task, accommodation_task, itinerary_task]
    )

    return [destination_task, flight_task, accommodation_task, itinerary_task, coordination_task]
