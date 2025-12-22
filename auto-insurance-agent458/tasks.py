"""
Auto Insurance CrewAI Tasks
"""

from crewai import Task
from agents import membership_specialist, claims_handler, roadside_coordinator, rewards_advisor

def create_tasks(request_type: str, member_id: str = None, details: dict = None):
    details = details or {}

    if request_type == "membership":
        return [Task(
            description=f"""Register new member with details: {details}

Steps:
- Collect required information (name, address, vehicle info)
- Confirm details with member
- Create new member ID
- Provide registration instructions""",
            agent=membership_specialist,
            expected_output="New member ID and registration confirmation"
        )]

    elif request_type == "claim":
        return [Task(
            description=f"""Process claim for member {member_id}

Details: {details}

Steps:
- Acknowledge the stressful situation
- Gather incident details (accident type, injuries, damage, location)
- Verify vehicle information
- Create claim ID
- Explain next steps""",
            agent=claims_handler,
            expected_output="Claim ID and follow-up instructions"
        )]

    elif request_type == "roadside":
        return [Task(
            description=f"""Dispatch roadside assistance for member {member_id}

Service needed: {details.get('service_type', 'towing')}
Location: {details.get('location', 'unknown')}

Steps:
- Confirm service type needed
- Get precise location
- Dispatch nearest provider
- Provide ETA""",
            agent=roadside_coordinator,
            expected_output="Dispatch confirmation with ETA"
        )]

    elif request_type == "rewards":
        return [Task(
            description=f"""Find rewards for member {member_id}

Location: {details.get('location', 'current location')}

Steps:
- Get member location
- Search for nearby offers
- Present available rewards""",
            agent=rewards_advisor,
            expected_output="List of nearby reward offers"
        )]

    return []
