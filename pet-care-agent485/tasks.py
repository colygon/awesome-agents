"""
CrewAI Tasks for Pet Care Assistant - Agent 485
"""

from crewai import Task


def create_health_guidance_task(agent, health_query):
    """
    Task for health advisor to provide wellness guidance
    """
    return Task(
        description=f"""Provide comprehensive pet health and wellness guidance:

        Health Query: {health_query}

        Your task:
        1. Assess the health concern or wellness question
        2. Provide information about:
           - Symptoms and potential causes (if health issue)
           - Nutrition recommendations (diet, portions, frequency)
           - Exercise requirements for breed/age/size
           - Preventive care (vaccinations, parasite control)
           - Dental care and hygiene
           - Grooming needs and frequency
           - Age-appropriate care (puppy/kitten, adult, senior)
        3. Identify when veterinary care is needed:
           - Emergency situations (immediate vet visit)
           - Concerns requiring vet check (within days)
           - Normal variations (monitor at home)
        4. Provide breed-specific health considerations
        5. Recommend health monitoring practices
        6. Suggest lifestyle improvements for wellness
        7. Include warning signs to watch for

        IMPORTANT: Always emphasize veterinary consultation for medical concerns.
        Do not diagnose or prescribe treatments.""",
        agent=agent,
        expected_output="""Comprehensive health guidance including:
        - Assessment of the concern
        - Nutrition recommendations
        - Exercise guidelines
        - Preventive care checklist
        - Grooming schedule
        - When to see a vet (urgency level)
        - Breed-specific considerations
        - Warning signs to monitor
        - Wellness improvement suggestions
        - Veterinary disclaimer"""
    )


def create_behavior_training_task(agent, behavior_issue):
    """
    Task for behavior trainer to address training needs
    """
    return Task(
        description=f"""Develop behavior modification and training strategies:

        Behavior Issue: {behavior_issue}

        Your task:
        1. Analyze the behavioral concern:
           - Identify root causes (fear, anxiety, boredom, etc.)
           - Distinguish between normal and problematic behavior
           - Consider environmental factors
        2. Create a training plan:
           - Step-by-step behavior modification approach
           - Positive reinforcement techniques
           - Consistency requirements
           - Timeline and milestones
        3. Address common issues:
           - Barking, whining, howling
           - Aggression or resource guarding
           - Separation anxiety
           - Destructive behavior
           - House training issues
           - Leash pulling
           - Recall problems
        4. Teach basic obedience (if requested):
           - Sit, stay, down, come, heel
           - Leave it, drop it
           - Crate training
           - Socialization
        5. Provide enrichment recommendations:
           - Mental stimulation activities
           - Physical exercise needs
           - Interactive toys and puzzles
        6. Include troubleshooting tips
        7. Know when to suggest professional trainer/behaviorist

        Use force-free, positive reinforcement methods only.""",
        agent=agent,
        expected_output="""Training and behavior plan including:
        - Behavior analysis and root causes
        - Step-by-step training protocol
        - Positive reinforcement techniques
        - Daily training schedule
        - Consistency tips for success
        - Environmental modifications
        - Enrichment activities
        - Progress milestones
        - Troubleshooting common setbacks
        - When to seek professional help"""
    )


def create_care_coordination_task(agent, care_needs):
    """
    Task for care coordinator to organize pet care routines
    """
    return Task(
        description=f"""Design comprehensive pet care routine and management plan:

        Care Needs: {care_needs}

        Your task:
        1. Create daily care schedule:
           - Feeding times and portions
           - Exercise and play sessions
           - Potty breaks/litter maintenance
           - Training time
           - Quiet/rest periods
        2. Establish care routines:
           - Weekly tasks (grooming, cleaning)
           - Monthly tasks (nail trims, deep cleaning)
           - Annual tasks (vet visits, vaccinations)
        3. Develop practical organization:
           - Supply checklist (food, toys, grooming, medical)
           - Budget planning for pet expenses
           - Emergency preparedness kit
           - Pet-proofing home recommendations
           - Travel planning with pets
        4. Handle multi-pet households:
           - Individual attention schedules
           - Resource management (food, toys, space)
           - Introduction protocols
        5. Plan for different life stages:
           - New pet preparation
           - Puppy/kitten care
           - Adult pet maintenance
           - Senior pet special needs
        6. Track important information:
           - Medication schedules
           - Veterinary appointment calendar
           - Health records organization
        7. Provide time-saving tips and efficiency improvements

        Create sustainable, practical care systems.""",
        agent=agent,
        expected_output="""Complete care coordination plan including:
        - Daily schedule breakdown
        - Weekly/monthly routine checklists
        - Annual care calendar
        - Essential supplies list
        - Budget breakdown (monthly/yearly)
        - Emergency preparedness plan
        - Pet-proofing checklist
        - Multi-pet management strategies
        - Record-keeping templates
        - Time-saving organization tips
        - New owner preparation guide"""
    )


def create_all_tasks(agents, pet_care_request):
    """
    Create all tasks for the pet care crew

    Args:
        agents: Dictionary of created agents
        pet_care_request: Can be dict with 'health', 'behavior', 'care_routine'
                         or string for general pet care inquiry
    """
    # Handle both dict and string inputs
    if isinstance(pet_care_request, dict):
        health = pet_care_request.get('health', 'General health and wellness')
        behavior = pet_care_request.get('behavior', 'Training and behavior guidance')
        care = pet_care_request.get('care_routine', 'Daily care and routines')
    else:
        health = behavior = care = pet_care_request

    return [
        create_health_guidance_task(agents['health_advisor'], health),
        create_behavior_training_task(agents['behavior_trainer'], behavior),
        create_care_coordination_task(agents['care_coordinator'], care)
    ]
