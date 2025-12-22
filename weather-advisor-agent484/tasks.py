"""
CrewAI Tasks for Weather Advisor - Agent 484
"""

from crewai import Task


def create_weather_analysis_task(agent, weather_query):
    """
    Task for weather analyst to interpret conditions and forecast
    """
    return Task(
        description=f"""Analyze the weather conditions and provide detailed forecast insights:

        Weather Query: {weather_query}

        Your task:
        1. Analyze current weather conditions:
           - Temperature (actual and feels-like)
           - Precipitation (type, amount, timing)
           - Wind (speed, direction, gusts)
           - Humidity and dew point
           - Cloud cover and visibility
           - Air pressure trends
        2. Interpret the forecast:
           - Hourly breakdown for next 24 hours
           - Daily forecast for next 7 days
           - Precipitation probability and timing
           - Temperature trends
           - Wind pattern changes
        3. Identify significant weather events:
           - Storms or severe weather
           - Temperature extremes
           - Heavy precipitation
           - High winds
           - Poor air quality
        4. Explain weather patterns and causes
        5. Highlight best and worst weather windows
        6. Note any weather alerts or warnings

        Provide clear, accurate weather analysis.""",
        agent=agent,
        expected_output="""A comprehensive weather analysis including:
        - Current conditions summary
        - Hour-by-hour forecast (24 hours)
        - 7-day outlook
        - Precipitation timing and amounts
        - Temperature range and trends
        - Wind conditions
        - Significant weather events
        - Weather alerts or warnings
        - Best/worst time windows"""
    )


def create_activity_planning_task(agent, activity_request):
    """
    Task for activity planner to suggest weather-appropriate activities
    """
    return Task(
        description=f"""Recommend activities based on weather conditions:

        Activity Request: {activity_request}

        Your task:
        1. Assess weather suitability for planned activities:
           - Outdoor vs indoor appropriateness
           - Timing optimization
           - Location considerations
           - Safety factors
        2. Suggest weather-appropriate activities:
           - If weather is favorable: outdoor options
           - If weather is poor: indoor alternatives
           - Shoulder weather: flexible options
        3. Provide activity-specific guidance:
           - Best time of day for the activity
           - Location recommendations
           - Duration suggestions
           - Group size considerations
        4. Consider comfort and enjoyment:
           - Temperature comfort zones
           - Sun/shade preferences
           - Wind sensitivity
           - Precipitation impact
        5. Offer backup plans and alternatives
        6. Include practical tips for each activity

        Recommend enjoyable, weather-appropriate activities.""",
        agent=agent,
        expected_output="""Activity recommendations including:
        - 3-5 suggested activities matched to weather
        - Best timing for each activity
        - Location recommendations
        - Weather suitability rating
        - Backup plans for weather changes
        - Practical tips for each activity
        - Indoor alternatives if needed
        - Duration and scheduling suggestions"""
    )


def create_preparation_task(agent, preparation_needs):
    """
    Task for preparation advisor to provide weather readiness guidance
    """
    return Task(
        description=f"""Provide weather preparation and safety recommendations:

        Preparation Needs: {preparation_needs}

        Your task:
        1. Recommend appropriate clothing and gear:
           - Base layers and insulation
           - Outer layers (rain, wind, cold protection)
           - Footwear selection
           - Accessories (hat, gloves, sunglasses, etc.)
           - Activity-specific gear
        2. Provide safety guidelines:
           - Severe weather precautions
           - Heat/cold safety
           - Lightning safety
           - Flood or storm preparation
           - Air quality considerations
        3. Suggest practical preparations:
           - What to bring/pack
           - Vehicle preparation (if traveling)
           - Home preparation (if storms expected)
           - Emergency supplies
        4. Include timing recommendations:
           - When to start preparations
           - When to avoid certain activities
           - Optimal departure times
        5. Consider specific scenarios:
           - Commuting needs
           - Event planning
           - Travel preparation
           - Outdoor work
        6. Provide layering strategies for changing conditions

        Help people be comfortable, safe, and prepared.""",
        agent=agent,
        expected_output="""Preparation guidance including:
        - Detailed clothing recommendations
        - Layering strategy for conditions
        - Essential gear and equipment
        - Safety precautions and warnings
        - What to bring checklist
        - Home/vehicle preparation steps
        - Emergency supplies (if needed)
        - Timing and scheduling advice
        - Scenario-specific tips"""
    )


def create_all_tasks(agents, weather_request):
    """
    Create all tasks for the weather advisor crew

    Args:
        agents: Dictionary of created agents
        weather_request: Can be dict with 'location', 'activity', 'date'
                        or string for general weather inquiry
    """
    # Handle both dict and string inputs
    if isinstance(weather_request, dict):
        location = weather_request.get('location', 'Current location')
        date = weather_request.get('date', 'today and upcoming days')
        activity = weather_request.get('activity', 'general activities')

        weather_query = f"Location: {location}, Date: {date}"
        activity_request = f"{activity} in {location} on {date}"
        prep_needs = f"Preparing for {activity} in {location} on {date}"
    else:
        weather_query = weather_request
        activity_request = weather_request
        prep_needs = weather_request

    return [
        create_weather_analysis_task(agents['weather_analyst'], weather_query),
        create_activity_planning_task(agents['activity_planner'], activity_request),
        create_preparation_task(agents['preparation_advisor'], prep_needs)
    ]
