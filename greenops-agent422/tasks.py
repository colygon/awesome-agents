from crewai import Task
from textwrap import dedent

class GreenOpsTasks:
    def analyze_environmental_impact(self, agent, infrastructure_data):
        return Task(
            description=dedent(f"""
                Analyze the environmental impact of current IT infrastructure
                and cloud operations.

                Infrastructure Data: {infrastructure_data}

                Your analysis should include:
                1. Carbon footprint measurement
                2. Energy consumption patterns
                3. Power Usage Effectiveness (PUE) calculations
                4. Identification of high-impact areas
                5. Comparison with industry benchmarks
            """),
            expected_output="""A detailed environmental impact analysis containing:
                - Total carbon emissions (metric tons CO2e)
                - Energy consumption breakdown by service
                - PUE metrics and efficiency scores
                - High-impact services and resources
                - Benchmark comparisons
                - Priority areas for improvement""",
            agent=agent
        )

    def optimize_green_infrastructure(self, agent, current_setup):
        return Task(
            description=dedent(f"""
                Optimize infrastructure configuration for minimal environmental
                impact while maintaining performance requirements.

                Current Setup: {current_setup}

                Your optimization should address:
                1. Resource allocation efficiency
                2. Geographic region selection for green energy
                3. Workload distribution optimization
                4. Right-sizing recommendations
                5. Auto-scaling configurations
            """),
            expected_output="""An infrastructure optimization plan with:
                - Resource utilization improvements
                - Recommended green regions for migration
                - Workload distribution strategy
                - Right-sizing recommendations with potential savings
                - Auto-scaling configuration for efficiency
                - Expected carbon reduction percentage""",
            agent=agent
        )

    def maximize_renewable_energy(self, agent, workload_profile):
        return Task(
            description=dedent(f"""
                Develop a strategy to maximize renewable energy usage for
                computing workloads.

                Workload Profile: {workload_profile}

                Your strategy should include:
                1. Renewable energy availability by region and time
                2. Workload scheduling for green hours
                3. Geographic load balancing for renewable energy
                4. Carbon-aware scaling policies
                5. Renewable energy usage tracking
            """),
            expected_output="""A renewable energy maximization strategy with:
                - Regional renewable energy availability schedules
                - Workload scheduling recommendations
                - Geographic distribution plan
                - Carbon-aware policies and thresholds
                - Renewable energy percentage targets
                - Implementation timeline""",
            agent=agent
        )

    def generate_sustainability_report(self, agent):
        return Task(
            description=dedent("""
                Generate a comprehensive sustainability report integrating
                all analyses and optimizations.

                Your report should include:
                1. Executive summary of environmental performance
                2. Carbon emissions metrics and trends
                3. Energy efficiency improvements
                4. Renewable energy usage statistics
                5. Cost savings from green initiatives
                6. ESG compliance status
                7. Recommendations for continuous improvement
            """),
            expected_output="""A comprehensive sustainability report containing:
                - Executive summary for stakeholders
                - Key performance indicators (KPIs)
                - Carbon emissions data and trends
                - Energy efficiency metrics
                - Renewable energy percentage
                - Cost-benefit analysis
                - ESG compliance assessment
                - Action plan for improvements
                - Industry certifications achieved/targeted""",
            agent=agent
        )
