from crewai import Agent
from tools import ONDriveSafetyTools

class ONDriveSafetyAgents:
    def __init__(self):
        self.tools = ONDriveSafetyTools()

    def vehicle_monitor(self):
        return Agent(
            role='Vehicle Safety Monitor',
            goal='Monitor vehicle systems and detect safety issues in real-time',
            backstory="""Expert in vehicle safety systems, sensor monitoring, and
            real-time diagnostics for autonomous and connected vehicles.""",
            tools=[
                self.tools.monitor_vehicle_systems,
                self.tools.detect_anomalies,
                self.tools.assess_vehicle_health
            ],
            verbose=True,
            allow_delegation=False
        )

    def driver_behavior_analyst(self):
        return Agent(
            role='Driver Behavior Analyst',
            goal='Analyze driving patterns and provide safety recommendations',
            backstory="""Specialist in driver behavior analysis, safety scoring,
            and personalized coaching for safer driving habits.""",
            tools=[
                self.tools.analyze_driving_behavior,
                self.tools.calculate_safety_score,
                self.tools.provide_coaching
            ],
            verbose=True,
            allow_delegation=False
        )

    def risk_assessor(self):
        return Agent(
            role='Road Safety Risk Assessor',
            goal='Assess road conditions and environmental risks for safe driving',
            backstory="""Expert in road safety analysis, environmental risk assessment,
            and route optimization for maximum safety.""",
            tools=[
                self.tools.assess_road_conditions,
                self.tools.evaluate_weather_risks,
                self.tools.recommend_safe_routes
            ],
            verbose=True,
            allow_delegation=False
        )

    def safety_coordinator(self):
        return Agent(
            role='Safety Operations Coordinator',
            goal='Coordinate safety systems and ensure comprehensive vehicle protection',
            backstory="""Senior safety coordinator managing all aspects of vehicle
            safety, driver assistance, and risk mitigation.""",
            tools=[
                self.tools.generate_safety_report,
                self.tools.prioritize_alerts,
                self.tools.recommend_improvements
            ],
            verbose=True,
            allow_delegation=True
        )
