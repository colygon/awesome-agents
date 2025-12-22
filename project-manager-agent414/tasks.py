"""
Project Manager Agent CrewAI Tasks
Defines the workflow for comprehensive project management
"""

from crewai import Task
from agents import (
    project_planner,
    task_breakdown_specialist,
    resource_allocator,
    risk_manager,
    timeline_scheduler,
    documentation_specialist
)


def create_tasks(project_info: dict):
    """
    Create tasks for project management workflow

    Args:
        project_info: Dictionary containing:
            - name: Project name
            - description: Project description
            - goals: Project goals
            - team_size: Number of team members
            - budget: Budget constraints
            - timeline: Desired timeline
            - methodology: Agile, Waterfall, or Hybrid

    Returns:
        List of Task objects
    """

    project_name = project_info.get('name', 'Project')
    description = project_info.get('description', '')
    timeline = project_info.get('timeline', 'Not specified')

    # Task 1: Create Project Plan
    create_plan_task = Task(
        description=f"""Create a comprehensive project plan for: {project_name}

        Project Information:
        {description}

        Goals: {project_info.get('goals', 'Not specified')}
        Timeline: {timeline}
        Budget: {project_info.get('budget', 'Not specified')}
        Team Size: {project_info.get('team_size', 'Not specified')}
        Methodology: {project_info.get('methodology', 'Agile')}

        Develop a project plan including:

        1. PROJECT CHARTER:
           - Project name and description
           - Business justification
           - Project objectives (SMART format)
           - Success criteria
           - High-level requirements
           - Assumptions and constraints

        2. SCOPE DEFINITION:
           - In-scope deliverables
           - Out-of-scope items
           - Acceptance criteria
           - Scope boundaries

        3. STAKEHOLDER ANALYSIS:
           - Key stakeholders (internal/external)
           - Stakeholder interests and influence
           - Communication needs
           - Management strategy for each stakeholder

        4. METHODOLOGY SELECTION:
           - Recommended approach (Agile/Waterfall/Hybrid)
           - Justification for methodology choice
           - Sprint/phase structure (if applicable)
           - Ceremonies and rituals

        5. HIGH-LEVEL PHASES:
           - Major project phases
           - Phase objectives
           - Phase deliverables
           - Estimated phase duration

        Create a clear, actionable project plan that sets the foundation.""",
        agent=project_planner,
        expected_output="""Comprehensive project plan including:
        - Project charter with objectives
        - Scope definition (in/out of scope)
        - Stakeholder analysis
        - Methodology recommendation
        - High-level project phases"""
    )

    # Task 2: Break Down Work Structure
    breakdown_task = Task(
        description=f"""Create detailed work breakdown structure (WBS) for {project_name}.

        Based on the project plan, create a comprehensive WBS:

        1. HIERARCHICAL TASK STRUCTURE:
           - Level 1: Major deliverables/phases
           - Level 2: Key components
           - Level 3: Detailed tasks (actionable items)
           - Level 4: Sub-tasks (if needed)

        2. FOR EACH TASK PROVIDE:
           - Task ID and name
           - Description (clear, specific)
           - Estimated effort (hours/days)
           - Required skills/expertise
           - Dependencies (prerequisite tasks)
           - Priority level (Critical/High/Medium/Low)
           - Deliverable/output

        3. DEPENDENCY MAPPING:
           - Identify critical path tasks
           - Map task dependencies (finish-to-start, start-to-start, etc.)
           - Flag tasks that can run in parallel
           - Identify bottleneck tasks

        4. TASK CATEGORIES:
           - Planning tasks
           - Development/execution tasks
           - Testing/QA tasks
           - Documentation tasks
           - Deployment/delivery tasks

        Aim for 50-100 detailed tasks depending on project complexity.
        Ensure tasks are:
        - Specific and actionable
        - Measurable (clear completion criteria)
        - Appropriately sized (1-5 days each)
        - Assigned to logical categories""",
        agent=task_breakdown_specialist,
        expected_output="""Work Breakdown Structure including:
        - Hierarchical task structure (3-4 levels)
        - 50-100 detailed tasks with estimates
        - Task dependencies and critical path
        - Priority assignments
        - Clear deliverables for each task""",
        context=[create_plan_task]
    )

    # Task 3: Allocate Resources
    resource_allocation_task = Task(
        description=f"""Allocate resources for {project_name}.

        Team Size: {project_info.get('team_size', 'Not specified')}
        Budget: {project_info.get('budget', 'Not specified')}

        Create resource allocation plan:

        1. TEAM STRUCTURE:
           - Recommended team roles (based on team size)
           - Role responsibilities
           - Required skills for each role
           - Reporting structure

        2. TASK ASSIGNMENTS:
           - Assign tasks to roles (from WBS)
           - Balance workload across team members
           - Identify over-allocation risks
           - Suggest task redistribution if needed

        3. BUDGET ALLOCATION:
           - Personnel costs
           - Tools and software
           - Infrastructure/hosting
           - Contingency (10-20%)
           - By phase breakdown

        4. RESOURCE CALENDAR:
           - Team availability assumptions
           - Holiday/vacation considerations
           - Part-time vs full-time allocation
           - External resource needs

        5. CAPACITY PLANNING:
           - Total team capacity (person-hours)
           - Capacity vs demand analysis
           - Over/under allocation periods
           - Scaling recommendations

        Provide realistic resource plan within budget constraints.""",
        agent=resource_allocator,
        expected_output="""Resource allocation plan including:
        - Team structure and roles
        - Task-to-role assignments
        - Budget breakdown by category
        - Resource calendar
        - Capacity analysis""",
        context=[create_plan_task, breakdown_task]
    )

    # Task 4: Conduct Risk Analysis
    risk_analysis_task = Task(
        description=f"""Conduct comprehensive risk analysis for {project_name}.

        Identify and assess potential risks:

        1. RISK IDENTIFICATION (20-30 risks):
           Categories to consider:
           - Technical risks (technology, architecture, integration)
           - Resource risks (availability, skill gaps, turnover)
           - Schedule risks (delays, dependencies, estimation errors)
           - Budget risks (cost overruns, scope creep)
           - External risks (vendor, regulatory, market)
           - Quality risks (defects, performance issues)

        2. RISK ASSESSMENT:
           For each risk, evaluate:
           - Probability (Low/Medium/High)
           - Impact (Low/Medium/High)
           - Risk score (Probability × Impact)
           - Timing (when risk might occur)

        3. RISK PRIORITIZATION:
           - Critical risks (High probability × High impact)
           - Important risks (High probability OR High impact)
           - Monitor risks (Medium probability/impact)
           - Low priority risks

        4. MITIGATION STRATEGIES:
           For top 10-15 risks:
           - Prevention actions (reduce probability)
           - Mitigation actions (reduce impact)
           - Contingency plans (if risk occurs)
           - Responsibility (who monitors/manages)
           - Budget/time allocation for mitigation

        5. RISK MONITORING PLAN:
           - Key risk indicators (KRIs)
           - Monitoring frequency
           - Escalation triggers
           - Review process

        Create actionable risk register.""",
        agent=risk_manager,
        expected_output="""Risk analysis including:
        - 20-30 identified risks with assessments
        - Prioritized risk list
        - Mitigation strategies for top 10-15 risks
        - Risk monitoring plan
        - Risk register template""",
        context=[create_plan_task, breakdown_task, resource_allocation_task]
    )

    # Task 5: Create Project Schedule
    create_schedule_task = Task(
        description=f"""Create detailed project schedule for {project_name}.

        Target timeline: {timeline}

        Develop comprehensive schedule:

        1. MILESTONE PLANNING:
           - Key project milestones (8-12)
           - Milestone dates
           - Milestone deliverables
           - Success criteria for each milestone

        2. DETAILED SCHEDULE:
           - Task start and end dates
           - Duration for each task
           - Dependencies reflected in schedule
           - Critical path highlighted
           - Buffer time included

        3. GANTT CHART:
           - Visual timeline representation
           - Phase breakdown
           - Parallel work streams
           - Key milestones marked
           - Resource allocation shown

        4. SPRINT/ITERATION PLAN (if Agile):
           - Sprint duration
           - Number of sprints
           - Sprint goals
           - Velocity assumptions

        5. SCHEDULE OPTIMIZATION:
           - Critical path analysis
           - Schedule compression opportunities
           - Fast-tracking possibilities
           - Resource leveling suggestions

        6. SCHEDULE RISKS:
           - Tasks with high uncertainty
           - Dependency-driven risks
           - Resource bottlenecks
           - Recommended buffers

        Create realistic schedule that accounts for:
        - Task dependencies
        - Resource availability
        - Risk buffers
        - Stakeholder deadlines""",
        agent=timeline_scheduler,
        expected_output="""Project schedule including:
        - 8-12 key milestones with dates
        - Detailed task schedule with dependencies
        - Gantt chart representation
        - Critical path analysis
        - Schedule risks and buffers
        - Sprint/iteration plan (if Agile)""",
        context=[create_plan_task, breakdown_task, resource_allocation_task, risk_analysis_task]
    )

    # Task 6: Create Project Documentation
    documentation_task = Task(
        description=f"""Create comprehensive project documentation for {project_name}.

        Develop essential project artifacts:

        1. PROJECT CHARTER (Executive Summary):
           - One-page overview
           - Business case
           - Objectives and success metrics
           - Stakeholder sign-off section

        2. COMMUNICATION PLAN:
           - Stakeholder communication matrix
           - Meeting schedule (standups, reviews, retrospectives)
           - Reporting structure and frequency
           - Communication channels
           - Escalation procedures

        3. STATUS REPORT TEMPLATE:
           - Weekly/bi-weekly format
           - Key sections: accomplishments, planned work, blockers
           - RAG status indicators
           - Metrics dashboard

        4. CHANGE MANAGEMENT PROCESS:
           - Change request form
           - Approval workflow
           - Impact assessment criteria
           - Change log template

        5. QUALITY MANAGEMENT PLAN:
           - Quality standards
           - Review processes
           - Testing approach
           - Acceptance criteria

        6. PROJECT CLOSEOUT TEMPLATE:
           - Lessons learned format
           - Success evaluation
           - Final deliverables checklist
           - Team recognition

        7. QUICK REFERENCE GUIDE:
           - One-page project summary
           - Key contacts
           - Important dates
           - Critical success factors

        Create practical, usable documentation (not bureaucratic overhead).""",
        agent=documentation_specialist,
        expected_output="""Project documentation package including:
        - Project charter (1-page)
        - Communication plan
        - Status report template
        - Change management process
        - Quality management plan
        - Project closeout template
        - Quick reference guide""",
        context=[
            create_plan_task,
            breakdown_task,
            resource_allocation_task,
            risk_analysis_task,
            create_schedule_task
        ]
    )

    return [
        create_plan_task,
        breakdown_task,
        resource_allocation_task,
        risk_analysis_task,
        create_schedule_task,
        documentation_task
    ]
