from crewai import Agent
from tools import GreenOpsTools

class GreenOpsAgents:
    def __init__(self):
        self.tools = GreenOpsTools()

    def sustainability_analyst(self):
        return Agent(
            role='Sustainability Operations Analyst',
            goal='Analyze and optimize environmental impact of cloud and IT operations',
            backstory="""You are an expert in sustainable IT operations and green computing.
            You specialize in measuring carbon footprints, analyzing energy consumption,
            and identifying opportunities to reduce environmental impact while maintaining
            operational efficiency.""",
            tools=[
                self.tools.measure_carbon_footprint,
                self.tools.analyze_energy_consumption,
                self.tools.calculate_pue
            ],
            verbose=True,
            allow_delegation=False
        )

    def infrastructure_optimizer(self):
        return Agent(
            role='Green Infrastructure Optimizer',
            goal='Optimize infrastructure for minimal environmental impact and maximum efficiency',
            backstory="""You are a cloud infrastructure expert focused on sustainable practices.
            You excel at optimizing resource utilization, selecting green regions,
            and implementing energy-efficient architectures.""",
            tools=[
                self.tools.optimize_resource_allocation,
                self.tools.recommend_green_regions,
                self.tools.analyze_workload_efficiency
            ],
            verbose=True,
            allow_delegation=False
        )

    def renewable_energy_coordinator(self):
        return Agent(
            role='Renewable Energy Coordinator',
            goal='Maximize use of renewable energy sources for IT operations',
            backstory="""You specialize in aligning computing workloads with renewable energy
            availability. You understand regional energy grids, renewable energy patterns,
            and how to schedule workloads for maximum green energy usage.""",
            tools=[
                self.tools.check_renewable_energy_availability,
                self.tools.schedule_green_workloads,
                self.tools.track_renewable_energy_usage
            ],
            verbose=True,
            allow_delegation=False
        )

    def sustainability_reporter(self):
        return Agent(
            role='Sustainability Reporting Specialist',
            goal='Generate comprehensive sustainability reports and compliance documentation',
            backstory="""You are an expert in environmental reporting and compliance.
            You compile sustainability metrics, generate reports for stakeholders,
            and ensure compliance with environmental regulations and standards.""",
            tools=[
                self.tools.generate_sustainability_report,
                self.tools.calculate_carbon_credits,
                self.tools.assess_esg_compliance
            ],
            verbose=True,
            allow_delegation=True
        )
