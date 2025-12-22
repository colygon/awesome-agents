"""
Custom tools for Pet Care Assistant - Agent 485
(Tools for pet health, training, and care management)
"""

from crewai_tools import tool


@tool("Breed Information Database")
def get_breed_info(breed: str, species: str = "dog") -> str:
    """
    Get breed-specific information including health, temperament, and care needs.

    Args:
        breed: Breed name
        species: Type of pet (dog, cat, bird, etc.)

    Returns:
        Comprehensive breed information
    """
    # Placeholder implementation
    # In production, integrate with breed databases or APIs
    return f"""
    Breed information for {species} - {breed}:

    This tool would provide:
    - Size and physical characteristics
    - Temperament and personality traits
    - Energy level and exercise needs
    - Common health issues
    - Grooming requirements
    - Training difficulty and tips
    - Good with children/pets
    - Living space requirements
    - Lifespan and life stage needs

    Data sources:
    - AKC (American Kennel Club)
    - CFA (Cat Fanciers' Association)
    - Breed-specific clubs
    - Veterinary breed guides
    """


@tool("Symptom Checker")
def check_pet_symptoms(symptoms: str, species: str, urgency_level: str = "assess") -> str:
    """
    Assess pet symptoms and determine if veterinary care is needed.

    Args:
        symptoms: Description of symptoms
        species: Type of pet
        urgency_level: "emergency", "urgent", "routine", or "assess"

    Returns:
        Symptom assessment and urgency recommendation
    """
    # Placeholder implementation
    return f"""
    Symptom assessment for {species}: {symptoms}

    This tool would provide:
    - Potential causes (informational only)
    - Urgency level (emergency, soon, monitor)
    - First aid if applicable
    - What to tell the vet
    - Warning signs to monitor

    EMERGENCY symptoms (immediate vet):
    - Difficulty breathing
    - Severe bleeding
    - Seizures
    - Collapse/unconsciousness
    - Bloated abdomen (dogs)
    - Suspected poisoning
    - Trauma/accident

    URGENT (vet within 24 hours):
    - Vomiting/diarrhea (persistent)
    - Not eating for 24+ hours
    - Lethargy/depression
    - Limping/pain
    - Eye injuries

    ALWAYS recommend veterinary consultation for medical concerns.
    """


@tool("Training Exercise Library")
def get_training_exercises(skill: str, pet_type: str, difficulty: str = "beginner") -> str:
    """
    Get step-by-step training exercises for specific skills.

    Args:
        skill: Skill to train (sit, stay, recall, leash manners, etc.)
        pet_type: Type of pet
        difficulty: beginner, intermediate, advanced

    Returns:
        Detailed training protocol
    """
    # Placeholder implementation
    return f"""
    Training exercise for {pet_type} - {skill} ({difficulty} level):

    This tool would provide:
    - Prerequisites and preparation
    - Step-by-step training protocol
    - Common mistakes to avoid
    - Troubleshooting tips
    - Progression criteria
    - Practice schedule

    Training principles:
    - Positive reinforcement (treats, praise, play)
    - Short sessions (5-10 minutes)
    - Consistency and repetition
    - Gradual difficulty increase
    - End on success

    Example exercises for:
    - Basic obedience (sit, stay, down, come)
    - Leash manners (heel, loose leash)
    - Behavior modification (counter-conditioning, desensitization)
    - Tricks and enrichment
    """


@tool("Feeding Calculator")
def calculate_feeding_portions(pet_weight: float, age: str, activity_level: str, food_type: str) -> str:
    """
    Calculate appropriate feeding portions and schedule.

    Args:
        pet_weight: Weight in pounds
        age: puppy/kitten, adult, senior
        activity_level: low, moderate, high
        food_type: dry, wet, raw, homemade

    Returns:
        Feeding recommendations
    """
    # Placeholder implementation
    return f"""
    Feeding recommendations:
    Weight: {pet_weight} lbs
    Age: {age}
    Activity: {activity_level}
    Food type: {food_type}

    This tool would provide:
    - Daily calorie requirements
    - Portion sizes per meal
    - Feeding frequency (meals per day)
    - Treat allowance (max 10% of calories)
    - Weight management tips
    - Brand-specific portions

    Calculations based on:
    - Metabolic rate (age, size, activity)
    - Food calorie density
    - Body condition score
    - Life stage requirements

    Note: Consult vet for medical conditions or weight issues
    """


@tool("Vaccination Schedule")
def get_vaccination_schedule(species: str, age: str, location: str = "US") -> str:
    """
    Get recommended vaccination schedule.

    Args:
        species: dog, cat, etc.
        age: current age of pet
        location: Geographic location for regional requirements

    Returns:
        Vaccination timeline and recommendations
    """
    # Placeholder implementation
    return f"""
    Vaccination schedule for {species} (age: {age}) in {location}:

    This tool would provide:
    - Core vaccines (required/essential)
    - Non-core vaccines (based on risk factors)
    - Vaccination timeline by age
    - Booster schedule
    - Regional requirements (rabies laws)
    - Travel requirements

    Example core vaccines (dogs):
    - Rabies (required by law)
    - Distemper
    - Parvovirus
    - Adenovirus

    Example core vaccines (cats):
    - Rabies
    - Feline distemper (FVRCP)
    - Feline herpesvirus
    - Calicivirus

    Always consult with veterinarian for personalized schedule.
    """


# Export tools list for easy import
pet_care_tools = [
    get_breed_info,
    check_pet_symptoms,
    get_training_exercises,
    calculate_feeding_portions,
    get_vaccination_schedule
]
