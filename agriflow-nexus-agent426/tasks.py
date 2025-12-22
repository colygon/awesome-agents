from crewai import Task
from textwrap import dedent

class AgriFlowTasks:
    def analyze_crops(self, agent, farm_data):
        return Task(
            description=dedent(f"""
                Analyze crop health and predict yields based on current conditions.

                Farm Data: {farm_data}

                Include: crop health assessment, yield predictions, growing
                recommendations, and nutrient management advice.
            """),
            expected_output="""Crop analysis report with health scores, yield forecasts,
                growth stage assessments, and fertilizer recommendations.""",
            agent=agent
        )

    def process_iot_data(self, agent, sensor_data):
        return Task(
            description=dedent(f"""
                Process IoT sensor data and environmental monitoring information.

                Sensor Data: {sensor_data}

                Include: soil analysis, weather impact, drone imagery insights,
                and environmental trends.
            """),
            expected_output="""IoT data analysis with soil conditions, weather patterns,
                crop imagery analysis, and environmental recommendations.""",
            agent=agent
        )

    def optimize_operations(self, agent, current_practices):
        return Task(
            description=dedent(f"""
                Optimize farm operations for efficiency and sustainability.

                Current Practices: {current_practices}

                Include: irrigation optimization, pest management, resource
                allocation, and sustainable farming practices.
            """),
            expected_output="""Operations optimization plan with irrigation schedules,
                pest management strategy, resource allocation, and sustainability measures.""",
            agent=agent
        )

    def create_farm_plan(self, agent):
        return Task(
            description=dedent("""
                Create comprehensive farm management plan integrating all analyses.

                Include: executive summary, integrated recommendations, ROI
                projections, sustainability goals, and implementation timeline.
            """),
            expected_output="""Complete farm management plan with actionable recommendations,
                financial projections, sustainability metrics, and implementation roadmap.""",
            agent=agent
        )
