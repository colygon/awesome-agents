from crewai import Agent
from tools import AgriFlowTools

class AgriFlowAgents:
    def __init__(self):
        self.tools = AgriFlowTools()

    def crop_analyst(self):
        return Agent(
            role='Agricultural Crop Analyst',
            goal='Analyze crop health, predict yields, and optimize growing conditions',
            backstory="""You are an expert in precision agriculture and crop science.
            You analyze crop data, monitor health, predict yields, and provide
            recommendations for optimal growing conditions.""",
            tools=[
                self.tools.analyze_crop_health,
                self.tools.predict_yield,
                self.tools.recommend_fertilizer
            ],
            verbose=True,
            allow_delegation=False
        )

    def iot_data_processor(self):
        return Agent(
            role='Agricultural IoT Data Processor',
            goal='Process and analyze data from farm IoT sensors and devices',
            backstory="""You specialize in agricultural IoT systems and sensor data analysis.
            You process data from soil sensors, weather stations, and drone imagery
            to provide actionable farming insights.""",
            tools=[
                self.tools.process_sensor_data,
                self.tools.analyze_weather_patterns,
                self.tools.process_drone_imagery
            ],
            verbose=True,
            allow_delegation=False
        )

    def farm_optimizer(self):
        return Agent(
            role='Farm Operations Optimizer',
            goal='Optimize farm operations for maximum efficiency and sustainability',
            backstory="""You are an expert in farm management and operational optimization.
            You design irrigation schedules, pest management strategies, and resource
            allocation plans for sustainable and profitable farming.""",
            tools=[
                self.tools.optimize_irrigation,
                self.tools.plan_pest_management,
                self.tools.allocate_resources
            ],
            verbose=True,
            allow_delegation=False
        )

    def agri_coordinator(self):
        return Agent(
            role='Agricultural Operations Coordinator',
            goal='Coordinate all farm operations and generate comprehensive farm management plans',
            backstory="""You oversee complete farm operations, integrating crop analysis,
            IoT data, and optimization strategies into actionable farm management plans.""",
            tools=[
                self.tools.generate_farm_plan,
                self.tools.calculate_roi,
                self.tools.create_sustainability_report
            ],
            verbose=True,
            allow_delegation=True
        )
