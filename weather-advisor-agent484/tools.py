"""
Custom tools for Weather Advisor - Agent 484
(Tools for weather data retrieval and analysis)
"""

from crewai_tools import tool


@tool("Weather Data Fetcher")
def fetch_weather_data(location: str, date: str = "today") -> str:
    """
    Fetch current weather and forecast data for a location.
    In production, integrate with weather APIs (OpenWeather, Weather.gov, etc.)

    Args:
        location: City, zip code, or coordinates
        date: Date or date range for forecast

    Returns:
        Current conditions and forecast data
    """
    # Placeholder implementation
    # In production, integrate with OpenWeather API, Weather.gov, or similar
    return f"""
    Weather data for {location} on {date}:

    This tool would fetch:
    - Current temperature, feels-like, conditions
    - Hourly forecast (next 48 hours)
    - Daily forecast (next 7-14 days)
    - Precipitation probability and timing
    - Wind speed and direction
    - Humidity, dew point, pressure
    - UV index and air quality
    - Sunrise/sunset times
    - Weather alerts and warnings

    APIs to integrate:
    - OpenWeather API (global coverage)
    - Weather.gov (US detailed forecasts)
    - AccuWeather API
    - Dark Sky API (Apple Weather)
    - Visual Crossing Weather
    """


@tool("Weather Alert Monitor")
def get_weather_alerts(location: str) -> str:
    """
    Get active weather alerts and warnings for a location.

    Args:
        location: Location to check for alerts

    Returns:
        Active weather alerts, watches, and warnings
    """
    # Placeholder implementation
    return f"""
    Weather alerts for {location}:

    This tool would provide:
    - Severe weather warnings (tornado, severe thunderstorm)
    - Watches (conditions favorable for severe weather)
    - Advisories (winter weather, heat, wind, flood)
    - Special weather statements
    - Alert severity and timing
    - Affected areas
    - Safety recommendations

    Alert types:
    - Tornado Warning/Watch
    - Severe Thunderstorm Warning
    - Flash Flood Warning
    - Winter Storm Warning
    - Heat Advisory
    - Air Quality Alert
    """


@tool("Activity Weather Suitability")
def check_activity_suitability(activity: str, weather_conditions: str) -> str:
    """
    Assess weather suitability for specific activities.

    Args:
        activity: Type of activity (hiking, sports, event, etc.)
        weather_conditions: Current or forecasted conditions

    Returns:
        Suitability rating and recommendations
    """
    # Placeholder implementation
    return f"""
    Suitability for {activity} in {weather_conditions}:

    This tool would assess:
    - Temperature comfort zone for activity
    - Precipitation impact (can you do it in rain?)
    - Wind limitations (too windy for activity?)
    - Safety considerations
    - Optimal conditions for activity
    - Timing recommendations

    Activity categories:
    - Outdoor sports (running, cycling, golf, tennis)
    - Water activities (swimming, boating, fishing)
    - Events (picnics, weddings, concerts)
    - Work (construction, landscaping, roofing)
    - Travel (driving, flying)
    - Gardening and yard work
    """


@tool("Clothing Recommendation Engine")
def recommend_clothing(weather_conditions: str, activity: str) -> str:
    """
    Recommend appropriate clothing based on weather and activity.

    Args:
        weather_conditions: Temperature, precipitation, wind
        activity: What the person will be doing

    Returns:
        Detailed clothing and gear recommendations
    """
    # Placeholder implementation
    return f"""
    Clothing recommendations for {activity} in {weather_conditions}:

    This tool would recommend:
    - Base layer (moisture wicking, insulation)
    - Mid layer (fleece, sweater)
    - Outer layer (jacket, raincoat, windbreaker)
    - Bottoms (pants, shorts, rain pants)
    - Footwear (boots, shoes, sandals)
    - Accessories (hat, gloves, scarf, sunglasses)
    - Activity-specific gear

    Considerations:
    - Temperature ranges and layering
    - Rain/snow protection
    - Wind resistance
    - Sun protection (UV, hat)
    - Activity intensity (stay cool vs warm)
    """


@tool("UV Index Checker")
def get_uv_index(location: str, time: str) -> str:
    """
    Get UV index and sun safety recommendations.

    Args:
        location: Location to check
        time: Time of day or date

    Returns:
        UV index and sun protection guidance
    """
    # Placeholder implementation
    return f"""
    UV Index for {location} at {time}:

    This tool would provide:
    - Current UV index (0-11+)
    - UV forecast by hour
    - Peak sun hours
    - Sun protection recommendations
    - Burn time estimates

    UV Index levels:
    - 0-2: Low (minimal protection needed)
    - 3-5: Moderate (protection recommended)
    - 6-7: High (protection required)
    - 8-10: Very High (extra protection needed)
    - 11+: Extreme (avoid sun exposure)
    """


# Export tools list for easy import
weather_advisor_tools = [
    fetch_weather_data,
    get_weather_alerts,
    check_activity_suitability,
    recommend_clothing,
    get_uv_index
]
