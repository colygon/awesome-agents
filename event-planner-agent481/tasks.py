"""
CrewAI Tasks for Event Planner - Agent 481
"""

from crewai import Task


def create_venue_task(agent, event_details):
    """
    Task for venue coordinator to find and evaluate venues
    """
    return Task(
        description=f"""Analyze the event requirements and recommend suitable venues:

        Event Details: {event_details}

        Your task:
        1. Identify 3-5 potential venues that match the requirements
        2. Evaluate each venue based on:
           - Location and accessibility
           - Capacity and layout suitability
           - Available amenities (AV equipment, WiFi, parking, etc.)
           - Catering options and restrictions
           - Pricing and availability
           - Backup options (outdoor/indoor alternatives)
        3. Provide pros and cons for each venue
        4. Rank venues by overall suitability
        5. Include practical considerations (setup time, vendor access, etc.)

        Deliver a comprehensive venue analysis with clear recommendations.""",
        agent=agent,
        expected_output="""A detailed venue recommendation report including:
        - 3-5 venue options with complete details
        - Evaluation matrix comparing all venues
        - Top recommendation with justification
        - Alternative options and backup plans
        - Practical logistics considerations
        - Estimated venue costs"""
    )


def create_schedule_task(agent, event_details):
    """
    Task for schedule planner to create event timeline
    """
    return Task(
        description=f"""Create a comprehensive event schedule and timeline:

        Event Details: {event_details}

        Your task:
        1. Design a minute-by-minute event timeline including:
           - Pre-event setup and preparation
           - Guest arrival and registration
           - Main event activities and segments
           - Meal service (if applicable)
           - Entertainment or presentations
           - Networking or break periods
           - Closing activities and teardown
        2. Account for transitions between activities
        3. Include buffer time for delays
        4. Coordinate vendor schedules (caterers, AV, entertainment)
        5. Plan for contingencies and backup timing
        6. Ensure optimal pacing and guest engagement

        Create a detailed rundown that event staff can follow.""",
        agent=agent,
        expected_output="""A comprehensive event schedule including:
        - Minute-by-minute timeline for entire event
        - Pre-event setup schedule
        - Guest-facing schedule overview
        - Detailed vendor coordination timeline
        - Critical milestones and checkpoints
        - Contingency plans for delays
        - Post-event cleanup timeline"""
    )


def create_budget_task(agent, event_details):
    """
    Task for budget manager to create financial plan
    """
    return Task(
        description=f"""Develop a detailed budget plan for the event:

        Event Details: {event_details}

        Your task:
        1. Create itemized budget breakdown including:
           - Venue rental and deposits
           - Catering (food, beverages, service)
           - Entertainment and speakers
           - Decorations and ambiance
           - Audio/visual equipment
           - Staffing and personnel
           - Marketing and invitations
           - Insurance and permits
           - Contingency fund (10-15%)
        2. Provide cost estimates for each category
        3. Identify potential cost savings
        4. Suggest value-optimization strategies
        5. Track payment schedules and deadlines
        6. Calculate per-person costs

        Deliver a transparent, actionable budget plan.""",
        agent=agent,
        expected_output="""A complete budget plan including:
        - Detailed line-item budget breakdown
        - Total estimated cost with ranges
        - Per-person cost analysis
        - Payment schedule and deadlines
        - Cost-saving recommendations
        - Value optimization strategies
        - Contingency allocation
        - Budget tracking template"""
    )


def create_all_tasks(agents, event_details):
    """
    Create all tasks for the event planning crew
    """
    return [
        create_venue_task(agents['venue_coordinator'], event_details),
        create_schedule_task(agents['schedule_planner'], event_details),
        create_budget_task(agents['budget_manager'], event_details)
    ]
