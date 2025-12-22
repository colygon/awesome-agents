# Weather Advisor - CrewAI Edition

## Overview

The Weather Advisor is a multi-agent weather analysis and planning system built with CrewAI that provides comprehensive weather guidance through three specialized agents:

1. **Weather Analyst** - Interprets weather data, forecasts, and patterns
2. **Activity Planner** - Recommends activities based on weather conditions
3. **Preparation Advisor** - Provides clothing, gear, and safety recommendations

## Features

- Detailed weather analysis and forecast interpretation
- Hour-by-hour and 7-day weather outlooks
- Activity recommendations matched to weather conditions
- Clothing and gear suggestions for any weather
- Safety alerts and severe weather warnings
- Optimal timing recommendations for activities
- Indoor and outdoor activity alternatives
- Travel and event planning guidance

## Architecture

### CrewAI Agents

#### 1. Weather Analysis Specialist
- **Role**: Analyze weather conditions and forecasts
- **Expertise**: Meteorology, pattern recognition, forecast interpretation
- **Output**: Detailed weather analysis with timing and trends

#### 2. Weather-Based Activity Advisor
- **Role**: Suggest weather-appropriate activities
- **Expertise**: Outdoor activities, event planning, comfort optimization
- **Output**: Activity recommendations with timing and alternatives

#### 3. Weather Preparedness Expert
- **Role**: Provide preparation and safety guidance
- **Expertise**: Clothing selection, safety protocols, gear recommendations
- **Output**: Detailed preparation checklist and safety tips

### Process Flow

```
Weather Request (Location + Date + Activity)
        ↓
Weather Analyst → Forecast Analysis
        ↓
Activity Planner → Activity Recommendations
        ↓
Preparation Advisor → Gear & Safety Guide
        ↓
Complete Weather Advisory
```

## Setup and Installation

### Prerequisites

- Python 3.10+
- OpenAI API key
- Optional: OpenWeather API key (for real weather data)

### Installation

1. **Navigate to directory**

```bash
cd weather-advisor-agent484
```

2. **Create virtual environment**

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Configure environment**

```bash
cp .env.example .env
# Edit .env and add your OpenAI API key
# Optionally add OpenWeather API key for real data
```

## Usage

### Interactive Mode

```bash
python main.py
```

### Programmatic Usage

```python
from main import get_weather_advice

weather_request = {
    "location": "Denver, CO",
    "date": "This weekend (Sat-Sun)",
    "activity": "Planning a hiking trip to Rocky Mountain National Park",
    "concerns": ["Temperature swings", "Afternoon thunderstorms", "Trail conditions"]
}

result = get_weather_advice(weather_request)
print(result)
```

### Example Output

The system produces:

1. **Weather Analysis**
   - Current conditions
   - Hour-by-hour forecast (24-48 hours)
   - 7-day outlook
   - Precipitation timing
   - Temperature trends
   - Wind conditions
   - Weather alerts

2. **Activity Recommendations**
   - Best activities for the weather
   - Optimal timing windows
   - Location suggestions
   - Indoor alternatives
   - Backup plans

3. **Preparation Guide**
   - Clothing layers to wear
   - Essential gear to bring
   - Safety precautions
   - What to pack checklist
   - Emergency preparations

## Use Cases

### Event Planning

```python
request = {
    "location": "Austin, TX",
    "date": "Next Saturday, 2-8 PM",
    "activity": "Outdoor wedding reception for 100 guests",
    "concerns": ["Heat", "Sudden storms", "Guest comfort"]
}
```

### Travel Planning

```python
request = {
    "location": "Yellowstone National Park",
    "date": "June 15-20",
    "activity": "Week-long camping and hiking trip",
    "concerns": ["Packing list", "Trail conditions", "Wildlife activity"]
}
```

### Sports and Recreation

```python
request = {
    "location": "San Diego, CA",
    "date": "Tomorrow morning",
    "activity": "Beach volleyball tournament",
    "concerns": ["Wind conditions", "UV index", "Tide timing"]
}
```

### Daily Commute

```python
request = {
    "location": "Chicago, IL",
    "date": "This week (Mon-Fri)",
    "activity": "Daily bike commute to work",
    "concerns": ["Rain timing", "Temperature", "What to wear"]
}
```

### Construction/Outdoor Work

```python
request = {
    "location": "Portland, OR",
    "date": "Next 5 days",
    "activity": "Roofing project",
    "concerns": ["Rain delays", "Wind safety", "Temperature for materials"]
}
```

## Weather Data Integration

### Using OpenWeather API

```python
# In tools.py, add real weather data fetching
import requests
from pyowm import OWM

def fetch_real_weather(location, api_key):
    owm = OWM(api_key)
    mgr = owm.weather_manager()

    # Current weather
    observation = mgr.weather_at_place(location)
    weather = observation.weather

    # Forecast
    forecast = mgr.forecast_at_place(location, '3h')

    return {
        "current": {
            "temp": weather.temperature('fahrenheit')['temp'],
            "conditions": weather.detailed_status,
            "humidity": weather.humidity,
            "wind": weather.wind()['speed']
        },
        "forecast": forecast.forecast
    }
```

### Using Weather.gov API (US Only)

```python
def fetch_weather_gov(lat, lon):
    # Get forecast office
    points_url = f"https://api.weather.gov/points/{lat},{lon}"
    response = requests.get(points_url)
    data = response.json()

    # Get detailed forecast
    forecast_url = data['properties']['forecast']
    forecast_response = requests.get(forecast_url)

    return forecast_response.json()
```

## Customization

### Add Custom Activity Types

```python
# In tasks.py, customize activity categories
activity_categories = {
    "outdoor_sports": ["hiking", "cycling", "running", "golf"],
    "water_activities": ["swimming", "kayaking", "fishing"],
    "events": ["wedding", "concert", "festival", "picnic"],
    "work": ["construction", "landscaping", "photography"],
    "travel": ["road_trip", "camping", "sightseeing"]
}
```

### Adjust Weather Thresholds

```python
# Define comfort zones
weather_thresholds = {
    "ideal_temp": (65, 75),  # Fahrenheit
    "too_hot": 90,
    "too_cold": 32,
    "high_wind": 25,  # mph
    "heavy_rain": 0.5,  # inches per hour
    "high_uv": 6  # UV index
}
```

### Custom Clothing Recommendations

```python
def get_clothing_for_temp(temp_f):
    if temp_f < 32:
        return "Heavy winter gear: insulated jacket, thermal layers, winter boots"
    elif temp_f < 50:
        return "Cool weather: jacket, long sleeves, jeans"
    elif temp_f < 70:
        return "Mild: light layers, long or short sleeves"
    elif temp_f < 85:
        return "Warm: t-shirt, shorts, sunscreen"
    else:
        return "Hot: light clothing, sun protection, hydration"
```

## Integration Options

### Calendar Integration
- Google Calendar (add weather to events)
- Outlook Calendar
- Apple Calendar

### Notification Services
- Email alerts for weather changes
- SMS via Twilio
- Push notifications

### Smart Home
- Adjust thermostat based on forecast
- Close smart blinds for hot days
- Send alerts for severe weather

## Best Practices

### Checking Weather

- **Check regularly** - Weather changes, update plans accordingly
- **Look at trends** - Don't rely on single forecast
- **Consider timing** - Hour-by-hour can be more useful than daily
- **Check multiple sources** - Compare forecasts for accuracy
- **Watch for updates** - Forecasts improve as date approaches

### Activity Planning

- **Have backup plans** - Indoor alternatives for outdoor activities
- **Be flexible** - Adjust timing based on weather windows
- **Consider comfort** - Temperature feels-like, not just actual
- **Check alerts** - Don't ignore weather warnings
- **Plan around extremes** - Avoid peak heat/cold/wind times

### Safety First

- **Severe weather** - Don't take chances with tornadoes, lightning
- **Heat safety** - Hydration, shade breaks, heat exhaustion signs
- **Cold safety** - Frostbite risk, hypothermia prevention
- **Lightning** - 30-30 rule (30 seconds = too close)
- **Flooding** - Turn around, don't drown

## Troubleshooting

### "Forecast seems inaccurate"

Weather forecasts have inherent uncertainty:
- Next 24 hours: Most accurate
- 2-3 days: Generally reliable
- 4-7 days: Trends only
- 7+ days: Low confidence

Always check closer to your event date.

### "Too many clothing recommendations"

Simplify the request:
```python
request = {
    "location": "Boston",
    "date": "Tomorrow",
    "activity": "Morning run",
    "focus": "clothing_only"  # Skip full analysis
}
```

### "Need more detailed hourly forecast"

Request specific time windows:
```python
request = {
    "location": "Miami",
    "date": "Saturday 2-5 PM",  # Specific time range
    "activity": "Outdoor ceremony",
    "detail_level": "hourly"
}
```

## Performance Optimization

### Reduce API Costs

```python
# Use GPT-3.5-turbo for routine weather queries
agents = create_all_agents(model="gpt-3.5-turbo", temperature=0.7)

# Use GPT-4 only for complex event planning
analyst = create_weather_analyst_agent(
    ChatOpenAI(model="gpt-4", temperature=0.5)
)
```

### Batch Requests

Check weather for multiple days at once:
```python
request = {
    "location": "Portland",
    "dates": ["Monday", "Wednesday", "Friday"],
    "activity": "Weekly running schedule"
}
```

## Advanced Features

### Weather Pattern Learning

```python
# Track historical accuracy
weather_log = {
    "date": "2024-03-15",
    "forecast": "70F, sunny",
    "actual": "68F, partly cloudy",
    "accuracy": "high"
}
```

### Multi-Location Planning

```python
# Compare weather across locations
request = {
    "locations": ["Seattle", "Portland", "San Francisco"],
    "date": "Next weekend",
    "activity": "Pick best city for outdoor activities"
}
```

### Long-Range Planning

```python
# Use climate data for distant dates
request = {
    "location": "Hawaii",
    "date": "December (3 months out)",
    "activity": "Vacation planning",
    "use_climate_data": True  # Historical averages
}
```

## Weather Metrics Explained

### Temperature
- **Actual**: Thermometer reading
- **Feels Like**: Accounts for wind chill or heat index
- **Dew Point**: Humidity comfort (60+ feels muggy)

### Precipitation
- **Probability**: Chance of rain (30% = 30% chance)
- **Amount**: Expected rainfall/snowfall
- **Timing**: When precipitation likely

### Wind
- **Speed**: Sustained wind speed
- **Gusts**: Short bursts (higher than sustained)
- **Direction**: Where wind is coming from

### UV Index
- 0-2: Low
- 3-5: Moderate (protection recommended)
- 6-7: High (protection required)
- 8-10: Very High
- 11+: Extreme

## Future Enhancements

Potential improvements:
1. **Real-time radar** integration
2. **Lightning tracker** for severe weather
3. **Air quality** monitoring (AQI)
4. **Pollen count** for allergies
5. **Marine weather** for boating
6. **Aviation weather** for flying
7. **Historical comparisons** (vs normal)
8. **Climate trends** analysis

## Weather Resources

### Official Sources
- Weather.gov (NOAA/NWS - US)
- Environment Canada
- Met Office (UK)
- Local weather services

### Weather Apps
- Weather Underground
- Dark Sky / Apple Weather
- AccuWeather
- The Weather Channel

### Specialized
- Mountain Weather (hiking)
- Windy.com (wind/sailing)
- Aviation Weather (flying)
- NOAA Marine (boating)

## License

Apache 2.0

## Support

For issues or questions:
- Review example use cases
- Check troubleshooting section
- Adjust parameters for your needs

---

**CrewAI Version:** 0.86.0+
**Python Version:** 3.10+
**Agent 484** - Weather Advisor
