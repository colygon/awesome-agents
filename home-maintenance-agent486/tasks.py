"""
CrewAI Tasks for Home Maintenance - Agent 486
"""

from crewai import Task


def create_repair_task(agent, repair_issue):
    """
    Task for repair advisor to diagnose and provide fix guidance
    """
    return Task(
        description=f"""Diagnose the home repair issue and provide solution guidance:

        Repair Issue: {repair_issue}

        Your task:
        1. Diagnose the problem:
           - Identify likely causes
           - Ask clarifying questions if needed
           - Assess severity and urgency
        2. Provide repair guidance:
           - Step-by-step DIY instructions (if appropriate)
           - Tools and materials needed
           - Estimated time and difficulty level
           - Safety precautions and warnings
           - Common mistakes to avoid
        3. Know when to call a professional:
           - Electrical work requiring permit
           - Plumbing beyond simple fixes
           - Structural issues
           - Specialized equipment needed
           - Safety concerns
        4. Estimate costs:
           - DIY materials cost
           - Professional service range
           - Urgency impact on pricing
        5. Provide temporary fixes if needed
        6. Recommend prevention for future

        ALWAYS prioritize safety and proper building codes.""",
        agent=agent,
        expected_output="""Comprehensive repair guidance including:
        - Problem diagnosis
        - DIY instructions (if safe/appropriate)
        - Tools and materials list
        - Difficulty rating (1-10)
        - Time estimate
        - Safety warnings
        - When to call professional
        - Cost estimates (DIY vs professional)
        - Temporary fix options
        - Prevention recommendations
        - Code compliance notes"""
    )


def create_maintenance_schedule_task(agent, home_info):
    """
    Task for maintenance planner to create upkeep schedule
    """
    return Task(
        description=f"""Create a comprehensive home maintenance schedule:

        Home Information: {home_info}

        Your task:
        1. Design maintenance schedule by frequency:
           MONTHLY tasks:
           - HVAC filter changes
           - Garbage disposal cleaning
           - Range hood filter cleaning
           - Test GFCI outlets
           - Inspect fire extinguishers

           QUARTERLY tasks:
           - Gutter cleaning
           - Dryer vent cleaning
           - Water heater flush
           - Inspect weatherstripping

           SEASONAL tasks:
           - Spring: AC service, outdoor prep
           - Summer: Deck/patio maintenance
           - Fall: Heating service, winterization
           - Winter: Prevent frozen pipes, check insulation

           ANNUAL tasks:
           - Chimney inspection
           - Septic tank pumping
           - Roof inspection
           - Deep carpet cleaning
           - Power wash exterior

        2. Organize by system:
           - Plumbing
           - Electrical
           - HVAC
           - Exterior (roof, siding, foundation)
           - Interior (floors, walls, appliances)
           - Landscaping/yard

        3. Provide for each task:
           - What to do
           - Why it's important
           - How to do it (brief instructions)
           - Estimated cost/time
           - DIY vs professional

        4. Create tracking system and reminders
        5. Prioritize by criticality
        6. Budget for annual maintenance costs

        Help prevent problems through proactive care.""",
        agent=agent,
        expected_output="""Complete maintenance schedule including:
        - Monthly task checklist
        - Quarterly task list
        - Seasonal maintenance by season
        - Annual big tasks
        - System-by-system breakdown
        - Task instructions and importance
        - DIY vs professional recommendations
        - Time and cost estimates
        - Tracking template/calendar
        - Annual budget estimate
        - Priority levels (critical/important/nice-to-have)
        - Reminder schedule"""
    )


def create_improvement_project_task(agent, project_details):
    """
    Task for improvement consultant to plan home projects
    """
    return Task(
        description=f"""Guide the home improvement project from planning to execution:

        Project Details: {project_details}

        Your task:
        1. Project planning:
           - Define scope and objectives
           - Space planning and design considerations
           - Permit and code requirements
           - Timeline estimate
           - Project phases

        2. Budget development:
           - Materials cost estimates
           - Labor costs (if hiring)
           - Permit/inspection fees
           - Contingency (10-20%)
           - Financing options

        3. Material selection:
           - Recommend quality tiers (budget/mid/premium)
           - Durability and maintenance considerations
           - Aesthetic options
           - Energy efficiency where applicable
           - Where to source materials

        4. DIY vs Professional assessment:
           - Which tasks are DIY-friendly
           - Where professionals are essential
           - How to hire contractors
           - How to get quotes
           - Contract considerations

        5. ROI and value analysis:
           - Resale value impact
           - Energy savings (if applicable)
           - Quality of life improvements
           - Payback period

        6. Project execution guidance:
           - Step-by-step phases
           - Preparation requirements
           - Living during construction
           - Quality checkpoints

        7. Common pitfalls and how to avoid them

        Provide realistic, actionable project guidance.""",
        agent=agent,
        expected_output="""Complete project plan including:
        - Scope and objectives statement
        - Detailed budget breakdown
        - Timeline with phases
        - Permit requirements checklist
        - Material recommendations with options
        - DIY vs professional breakdown
        - Contractor hiring guide
        - ROI analysis
        - Phase-by-phase execution plan
        - Quality checkpoints
        - Common mistakes to avoid
        - Resource list (where to buy, who to hire)
        - Contingency planning"""
    )


def create_all_tasks(agents, home_request):
    """
    Create all tasks for the home maintenance crew

    Args:
        agents: Dictionary of created agents
        home_request: Can be dict with 'repair', 'maintenance', 'improvement'
                     or string for general home inquiry
    """
    # Handle both dict and string inputs
    if isinstance(home_request, dict):
        repair = home_request.get('repair', 'General home repair guidance')
        maintenance = home_request.get('maintenance', 'Home type and systems')
        improvement = home_request.get('improvement', 'Home improvement project')
    else:
        repair = maintenance = improvement = home_request

    return [
        create_repair_task(agents['repair_advisor'], repair),
        create_maintenance_schedule_task(agents['maintenance_planner'], maintenance),
        create_improvement_project_task(agents['improvement_consultant'], improvement)
    ]
