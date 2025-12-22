"""Energy Agent AI Tasks"""

from crewai import Task
from agents import energy_auditor, renewable_energy_advisor, cost_optimizer, sustainability_advisor, implementation_planner


def create_tasks(property_info: dict):
    """Create energy management tasks"""

    property_type = property_info.get('type', 'Residential')
    location = property_info.get('location', 'Unknown')

    audit_task = Task(
        description=f"""Conduct energy audit for {property_type} property in {location}.

        Analyze:
        1. Current energy consumption patterns
        2. Major energy consumers (HVAC, lighting, appliances)
        3. Inefficiencies and waste areas
        4. Seasonal variations
        5. Benchmark against similar properties""",
        agent=energy_auditor,
        expected_output="Energy audit report with findings"
    )

    renewable_task = Task(
        description=f"""Assess renewable energy options for {property_type} in {location}.

        Evaluate:
        1. Solar potential (roof area, orientation, shading)
        2. Wind potential (if applicable)
        3. Battery storage options
        4. System sizing and costs
        5. Incentives and rebates
        6. ROI and payback period""",
        agent=renewable_energy_advisor,
        expected_output="Renewable energy feasibility report",
        context=[audit_task]
    )

    optimize_cost_task = Task(
        description=f"""Optimize energy costs for {property_type}.

        Analyze:
        1. Current tariff structure
        2. Alternative tariff options
        3. Peak/off-peak usage optimization
        4. Demand management strategies
        5. Potential savings""",
        agent=cost_optimizer,
        expected_output="Cost optimization recommendations",
        context=[audit_task]
    )

    sustainability_task = Task(
        description=f"""Develop sustainability roadmap for {property_type}.

        Calculate:
        1. Current carbon footprint
        2. Emission reduction targets
        3. Sustainability strategies
        4. Green certification opportunities
        5. ESG reporting framework""",
        agent=sustainability_advisor,
        expected_output="Sustainability roadmap",
        context=[audit_task, renewable_task]
    )

    implementation_task = Task(
        description=f"""Create implementation plan for energy initiatives.

        Develop:
        1. Prioritized action items (quick wins vs long-term)
        2. Timeline and milestones
        3. Budget and ROI projections
        4. Resource requirements
        5. Success metrics""",
        agent=implementation_planner,
        expected_output="Implementation plan with timeline and ROI",
        context=[audit_task, renewable_task, optimize_cost_task, sustainability_task]
    )

    return [audit_task, renewable_task, optimize_cost_task, sustainability_task, implementation_task]
