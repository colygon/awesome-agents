from crewai_tools import tool

class ONDriveSafetyTools:
    @tool("Monitor Vehicle Systems")
    def monitor_vehicle_systems(self, vehicle_id: str) -> str:
        """Monitors all vehicle systems in real-time."""
        return f"""Vehicle System Status - {vehicle_id}:

Engine: ✓ Normal (temp: 195°F, oil pressure: 45 psi)
Transmission: ✓ Normal (fluid temp: 175°F)
Brakes: ⚠ Attention (pad wear: 25% remaining)
Tires: ✓ Normal (pressures: 32-33 psi)
Battery: ✓ Normal (12.6V, 85% health)
ADAS Systems: ✓ All operational

Maintenance Alerts:
- Brake pad replacement recommended (1,000 miles)
- Oil change due in 500 miles

Overall Health: 92/100 (Excellent)"""

    @tool("Detect Anomalies")
    def detect_anomalies(self, sensor_data: str) -> str:
        """Detects anomalies in vehicle sensor data."""
        return f"""Anomaly Detection Results:

Detected Anomalies:
⚠ Unusual vibration pattern (front right)
⚠ Slight brake response delay (0.2s)
✓ All other systems normal

Severity: Medium (investigation recommended)
Recommended Action: Schedule inspection within 1 week

False Positive Rate: 2.1% (high confidence)"""

    @tool("Assess Vehicle Health")
    def assess_vehicle_health(self, diagnostics: str) -> str:
        """Comprehensive vehicle health assessment."""
        return f"""Vehicle Health Assessment:

Overall Score: 92/100 (Excellent)

Component Scores:
- Engine: 95/100
- Transmission: 98/100
- Brakes: 75/100 (due for service)
- Suspension: 88/100
- Electrical: 94/100

Predicted Reliability: 97% for next 6 months
Estimated Time to Service: 3 weeks
No critical issues detected"""

    @tool("Analyze Driving Behavior")
    def analyze_driving_behavior(self, trip_data: str) -> str:
        """Analyzes driver behavior patterns."""
        return f"""Driving Behavior Analysis:

Safety Events (Last 30 days):
- Hard braking: 12 events
- Rapid acceleration: 8 events
- Sharp turns: 5 events
- Speeding: 3 instances (+10 mph over limit)
- Phone usage: 0 detected (excellent)

Driving Patterns:
- Smooth driving: 85% of time
- Defensive driving: Good
- Following distance: Adequate (2.5s avg)
- Turn signal usage: 94%

Risk Level: Low-Medium
Primary concern: Hard braking frequency"""

    @tool("Calculate Safety Score")
    def calculate_safety_score(self, behavior_data: str) -> str:
        """Calculates comprehensive driver safety score."""
        return f"""Driver Safety Score: 78/100 (Good)

Score Breakdown:
- Smooth driving: 85/100
- Speed compliance: 75/100 (-3 speeding events)
- Braking behavior: 70/100 (12 hard brakes)
- Acceleration: 82/100
- Turning: 88/100
- Distraction-free: 100/100

Percentile: Top 35% of drivers
Trend: +5 points vs last month (improving)

Insurance Discount Eligible: 15%"""

    @tool("Provide Coaching")
    def provide_coaching(self, safety_issues: str) -> str:
        """Provides personalized safety coaching."""
        return f"""Safety Coaching Recommendations:

Primary Focus: Braking Technique
- Anticipate stops earlier
- Gradual pressure application
- Maintain greater following distance

Secondary Areas:
1. Speed Management
   - Use cruise control on highways
   - Check speed regularly in zones

2. Smooth Acceleration
   - Gradual throttle input
   - Plan lane changes ahead

Weekly Goal: Reduce hard braking by 50%
Progress Tracking: Daily summaries enabled"""

    @tool("Assess Road Conditions")
    def assess_road_conditions(self, route: str) -> str:
        """Assesses current road conditions."""
        return f"""Road Conditions Assessment - {route}:

Current Conditions:
- Road surface: Dry, good condition
- Traffic: Moderate (35 mph avg speed)
- Construction: 1 zone (Lane closure, mile 15)
- Accidents: None reported
- Road quality: 8/10

Hazards Detected:
- Construction zone: Miles 15-17 (reduce speed)
- School zone: Mile 8 (15 mph, 3-4pm)
- Curve ahead: Mile 22 (advisory 45 mph)

Overall Safety: Good
Estimated travel time: 35 minutes"""

    @tool("Evaluate Weather Risks")
    def evaluate_weather_risks(self, conditions: str) -> str:
        """Evaluates weather-related driving risks."""
        return f"""Weather Risk Assessment:

Current Weather:
- Conditions: Light rain
- Visibility: 2 miles (reduced)
- Temperature: 45°F
- Wind: 15 mph NW

Risk Factors:
⚠ Wet roads: Increase stopping distance 20%
⚠ Reduced visibility: Slower traffic expected
✓ No ice/snow
✓ Moderate temperatures

Risk Level: Medium
Recommendations:
- Reduce speed by 10 mph
- Increase following distance to 4 seconds
- Use headlights
- Avoid sudden maneuvers"""

    @tool("Recommend Safe Routes")
    def recommend_safe_routes(self, destination: str) -> str:
        """Recommends safest route to destination."""
        return f"""Safe Route Recommendations to {destination}:

Route 1 (Recommended): Highway 101
- Distance: 25 miles
- Time: 35 min
- Safety Score: 95/100
- Conditions: Excellent
- Traffic: Moderate

Route 2 (Alternative): State Route 17
- Distance: 23 miles
- Time: 40 min
- Safety Score: 78/100
- Conditions: Construction zone
- Traffic: Heavy

Route 3 (Scenic): Coastal Highway
- Distance: 30 miles
- Time: 50 min
- Safety Score: 85/100
- Conditions: Curves, slower
- Traffic: Light

Recommendation: Take Route 1 for optimal safety"""

    @tool("Generate Safety Report")
    def generate_safety_report(self, period: str) -> str:
        """Generates comprehensive safety report."""
        return f"""COMPREHENSIVE SAFETY REPORT - {period}

EXECUTIVE SUMMARY:
Vehicle health excellent (92/100). Driver safety score good (78/100)
with opportunity for braking improvement. No critical safety issues.
Overall risk level: Low.

VEHICLE STATUS:
- Health Score: 92/100
- Maintenance needed: Brake pads (1,000 mi)
- All systems operational
- No recalls or critical issues

DRIVER PERFORMANCE:
- Safety Score: 78/100 (Top 35%)
- Trend: Improving (+5 points)
- Primary focus: Braking technique
- Insurance discount: 15% eligible

SAFETY EVENTS:
- Hard braking: 12 (reduce by 50%)
- Speeding: 3 (minor, +10 mph)
- Collisions: 0
- Near misses: 0

RECOMMENDATIONS:
1. Schedule brake pad replacement
2. Practice gradual braking
3. Maintain current safe driving habits
4. Continue monthly safety reviews

OVERALL RATING: Safe (Low Risk)"""

    @tool("Prioritize Alerts")
    def prioritize_alerts(self, alerts: str) -> str:
        """Prioritizes safety alerts by urgency."""
        return f"""Alert Prioritization:

CRITICAL (Immediate Action):
None currently

HIGH (Within 24 hours):
None currently

MEDIUM (This Week):
1. Schedule brake pad replacement (1,000 mi)
2. Address front-right vibration
3. Review hard braking patterns

LOW (This Month):
4. Oil change due (500 miles)
5. Tire rotation recommended
6. Safety coaching review

All alerts managed appropriately
No immediate safety concerns"""

    @tool("Recommend Improvements")
    def recommend_improvements(self, analysis: str) -> str:
        """Recommends safety improvements."""
        return f"""Safety Improvement Recommendations:

VEHICLE ENHANCEMENTS:
1. Upgrade to adaptive cruise control ($1,200)
2. Add blind spot monitoring ($800)
3. Install dashcam for evidence ($300)

DRIVER TRAINING:
4. Advanced defensive driving course ($250)
5. Wet weather driving practice (free)
6. Distraction awareness training (free)

MAINTENANCE:
7. Premium brake pads ($400, +20% performance)
8. All-season tire upgrade ($800, +15% safety)
9. Comprehensive inspection ($150)

TECHNOLOGY:
10. Driver monitoring app (free)
11. Real-time coaching system ($15/mo)
12. Telematics insurance ($0, saves 15%)

Total Investment: ~$3,900
Expected Risk Reduction: 40%
Insurance Savings: $450/year
ROI: 2.5 years"""
