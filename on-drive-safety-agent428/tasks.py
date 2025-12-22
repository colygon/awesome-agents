from crewai import Task
from textwrap import dedent

class ONDriveSafetyTasks:
    def monitor_vehicle(self, agent, vehicle_data):
        return Task(
            description=dedent(f"""
                Monitor vehicle systems and detect safety issues.
                Vehicle Data: {vehicle_data}
                Include: system diagnostics, anomaly detection, health assessment.
            """),
            expected_output="""Vehicle monitoring report with system status,
                detected issues, health score, and immediate actions needed.""",
            agent=agent
        )

    def analyze_driver(self, agent, driving_data):
        return Task(
            description=dedent(f"""
                Analyze driving behavior and provide safety coaching.
                Driving Data: {driving_data}
                Include: behavior analysis, safety scoring, personalized coaching.
            """),
            expected_output="""Driver analysis with safety score, behavior patterns,
                risk areas, and coaching recommendations.""",
            agent=agent
        )

    def assess_risks(self, agent, route_data):
        return Task(
            description=dedent(f"""
                Assess environmental and road safety risks.
                Route Data: {route_data}
                Include: road conditions, weather risks, safe route recommendations.
            """),
            expected_output="""Risk assessment with road conditions, weather analysis,
                hazard identification, and optimized safe routes.""",
            agent=agent
        )

    def coordinate_safety(self, agent):
        return Task(
            description=dedent("""
                Coordinate all safety systems and generate comprehensive report.
                Include: integrated safety analysis, priority alerts, improvement plan.
            """),
            expected_output="""Complete safety report with integrated analysis,
                prioritized alerts, safety score, and improvement recommendations.""",
            agent=agent
        )
