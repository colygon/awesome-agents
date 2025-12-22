# Pet Care Assistant - CrewAI Edition

## Overview

The Pet Care Assistant is a multi-agent system built with CrewAI that provides comprehensive pet care guidance through three specialized agents:

1. **Pet Health & Wellness Specialist** - Health guidance, nutrition, and preventive care
2. **Pet Behavior & Training Expert** - Training plans and behavior modification
3. **Pet Care Coordinator** - Daily routines, schedules, and practical management

## Features

- Health and wellness guidance for multiple species
- Nutrition recommendations and feeding schedules
- Behavior modification and training protocols
- Daily care routines and schedules
- Emergency symptom assessment (with vet referral)
- Breed-specific care information
- Positive reinforcement training methods
- Multi-pet household management
- Travel planning with pets
- Budget planning for pet expenses

## Architecture

### CrewAI Agents

#### 1. Pet Health & Wellness Specialist
- **Role**: Provide health and nutrition guidance
- **Expertise**: Veterinary knowledge, nutrition, preventive care
- **Output**: Health assessment, nutrition plan, wellness recommendations

#### 2. Pet Behavior & Training Expert
- **Role**: Address training and behavior issues
- **Expertise**: Animal behavior, positive reinforcement training
- **Output**: Training protocols, behavior modification plans

#### 3. Pet Care Coordinator
- **Role**: Organize care routines and logistics
- **Expertise**: Care scheduling, budgeting, practical management
- **Output**: Daily schedules, checklists, organizational systems

### Process Flow

```
Pet Care Request (Pet Info + Questions)
        ↓
Health Advisor → Health & Wellness Guidance
        ↓
Behavior Trainer → Training Plan
        ↓
Care Coordinator → Care Routine
        ↓
Complete Pet Care Package
```

## Setup and Installation

### Prerequisites

- Python 3.10+
- OpenAI API key

### Installation

1. **Navigate to directory**

```bash
cd pet-care-agent485
```

2. **Create virtual environment**

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Configure environment**

```bash
cp .env.example .env
# Edit .env and add your OpenAI API key
```

## Usage

### Interactive Mode

```bash
python main.py
```

### Programmatic Usage

```python
from main import get_pet_care_advice

pet_request = {
    "pet_info": {
        "species": "cat",
        "breed": "Domestic Shorthair",
        "age": "3 years",
        "weight": "10 lbs",
        "name": "Luna"
    },
    "health": "Luna seems lethargic and not eating much for 2 days",
    "behavior": "Scratching furniture and meowing excessively at night",
    "care_routine": "Need help with litter box maintenance and playtime schedule"
}

result = get_pet_care_advice(pet_request)
print(result)
```

### Example Output

The system produces:

1. **Health & Wellness Guidance**
   - Symptom assessment (with vet urgency level)
   - Nutrition recommendations
   - Exercise requirements
   - Preventive care checklist
   - Breed-specific health tips

2. **Training & Behavior Plan**
   - Behavior analysis
   - Step-by-step training protocol
   - Positive reinforcement techniques
   - Enrichment activities
   - Progress milestones

3. **Care Coordination**
   - Daily schedule
   - Weekly/monthly routines
   - Supply checklists
   - Budget breakdown
   - Emergency preparedness

## Supported Species

- **Dogs** - All breeds, sizes, and ages
- **Cats** - Domestic and purebred
- **Small Mammals** - Rabbits, guinea pigs, hamsters, ferrets
- **Birds** - Parrots, canaries, finches
- **Reptiles** - Turtles, lizards, snakes
- **Other** - Fish, exotic pets

## Common Use Cases

### New Pet Owner

```python
request = {
    "pet_info": {"species": "puppy", "breed": "Labrador", "age": "8 weeks"},
    "health": "What vaccinations and vet visits are needed?",
    "behavior": "How to start house training and basic obedience?",
    "care_routine": "Complete setup guide for new puppy - what do I need?"
}
```

### Behavior Problems

```python
request = {
    "pet_info": {"species": "dog", "age": "2 years"},
    "behavior": """Dog has separation anxiety - destroys furniture when alone,
                   barks excessively. Need training plan and management strategies."""
}
```

### Health Concerns

```python
request = {
    "pet_info": {"species": "cat", "age": "senior (12 years)"},
    "health": """Cat drinking more water than usual, losing weight.
                What could this be and do I need a vet visit?"""
}
```

### Multi-Pet Household

```python
request = {
    "pet_info": {"pets": ["2 dogs", "1 cat"]},
    "care_routine": """Managing feeding schedules, preventing resource guarding,
                       creating individual attention time for each pet."""
}
```

## Important Disclaimers

### Medical Advice
- This system provides **educational information only**
- **NOT a substitute** for professional veterinary care
- Always consult a licensed veterinarian for medical concerns
- Emergency symptoms require **immediate vet attention**

### Training Guidance
- Uses **force-free, positive reinforcement** methods only
- Serious aggression issues require professional behaviorist
- Training takes time, patience, and consistency
- Every pet is an individual - adjust methods as needed

## Customization

### Add Custom Pet Profiles

```python
# Save pet profiles for quick access
pet_profiles = {
    "Max": {
        "species": "dog",
        "breed": "Golden Retriever",
        "age": "8 months",
        "allergies": ["chicken"],
        "medications": []
    }
}
```

### Adjust Training Methodology

```python
# Customize training approach
training_preferences = {
    "method": "clicker_training",  # or "lure_reward", "capture"
    "session_length": "5-10 minutes",
    "frequency": "3 times daily",
    "treat_type": "high_value"
}
```

### Create Care Templates

```python
# Template for specific pet types
puppy_care_template = {
    "feeding": "4 meals per day until 6 months",
    "exercise": "5 min per month of age, twice daily",
    "training": "Daily socialization and basic commands",
    "vet": "Every 3-4 weeks for vaccinations"
}
```

## Integration Options

### Veterinary Software
- Vet appointment reminders
- Vaccination tracking
- Medical record storage

### Pet Apps
- Rover (pet sitting/walking)
- Wag! (dog walking)
- Chewy (supplies ordering)

### Smart Devices
- Automatic feeders
- Pet cameras
- GPS trackers
- Smart toys

## Best Practices

### Health Monitoring
- **Regular vet visits** - Annual wellness exams
- **Know normal baseline** - Eating, drinking, energy levels
- **Watch for changes** - Behavior, appetite, elimination
- **Keep records** - Vaccinations, medications, health history
- **Pet insurance** - Consider for unexpected costs

### Training Success
- **Consistency** - Same commands, rules, and rewards
- **Positive reinforcement** - Reward good behavior
- **Short sessions** - 5-10 minutes, end on success
- **Patience** - Learning takes time
- **All family members** - Everyone follows same rules

### Daily Care
- **Routine** - Same feeding/walk times daily
- **Exercise** - Mental and physical stimulation
- **Enrichment** - Toys, puzzles, new experiences
- **Grooming** - Regular brushing, nail trims, dental care
- **Quality time** - Bonding and attention

## Troubleshooting

### "My pet's symptoms sound serious"

**Immediate vet visit needed for:**
- Difficulty breathing
- Seizures
- Severe bleeding
- Suspected poisoning
- Trauma/accident
- Bloated abdomen (dogs)
- Not eating/drinking for 24+ hours

**Call vet for advice:**
- Persistent vomiting/diarrhea
- Limping or pain
- Behavioral changes
- Skin issues
- Eye problems

### "Training isn't working"

Common issues:
- **Inconsistency** - All family members must use same methods
- **Unclear communication** - Pet doesn't understand what you want
- **Insufficient practice** - Need more repetitions
- **Distractions** - Start in quiet environment
- **Wrong motivation** - Find what motivates your pet
- **Too fast** - Break skills into smaller steps

### "Can't afford vet care"

Options:
- **Pet insurance** - Get before issues arise
- **Payment plans** - Ask vet about CareCredit
- **Low-cost clinics** - ASPCA, Humane Society
- **Veterinary schools** - Discounted care
- **Emergency fund** - Save monthly for pet care

## Performance Optimization

### Reduce API Costs

```python
# Use GPT-3.5-turbo for routine questions
agents = create_all_agents(model="gpt-3.5-turbo", temperature=0.7)

# Use GPT-4 for complex medical/behavioral issues
health_advisor = create_health_advisor_agent(
    ChatOpenAI(model="gpt-4", temperature=0.5)
)
```

### Batch Requests

Process multiple questions:
```python
requests = [
    "Feeding schedule for puppy",
    "House training tips",
    "Socialization plan"
]

for question in requests:
    result = get_pet_care_advice(question)
```

## Advanced Features

### Life Stage Planning

```python
# Plan for pet's entire life
life_stages = {
    "puppy": {"age": "0-1 year", "focus": "socialization, training, growth"},
    "young_adult": {"age": "1-3 years", "focus": "maintain training, energy management"},
    "adult": {"age": "3-7 years", "focus": "health maintenance, enrichment"},
    "senior": {"age": "7+ years", "focus": "joint care, diet changes, vet monitoring"}
}
```

### Multi-Pet Dynamics

```python
request = {
    "household": {
        "pets": [
            {"species": "dog", "age": "5", "temperament": "dominant"},
            {"species": "cat", "age": "3", "temperament": "shy"}
        ]
    },
    "concern": "Introducing new kitten to existing dog and cat"
}
```

### Emergency Preparedness

```python
emergency_kit = {
    "medical_records": "Vaccination records, medical history",
    "medications": "Current prescriptions, dosages",
    "vet_contact": "Primary and emergency vet numbers",
    "supplies": "3-day food/water, first aid kit, carrier",
    "evacuation_plan": "Pet-friendly hotels, transport arrangements"
}
```

## Pet Care Metrics

Track your pet's wellbeing:

- **Weight**: Regular weigh-ins (monthly)
- **Body Condition Score**: Visual assessment (1-9 scale)
- **Exercise**: Minutes of activity daily
- **Training Progress**: Skills mastered, behaviors improved
- **Health Events**: Vet visits, symptoms, medications
- **Behavioral Changes**: Mood, appetite, energy

## Resources

### Veterinary Organizations
- AVMA (American Veterinary Medical Association)
- ASPCA Animal Poison Control
- Pet Poison Helpline

### Training Resources
- APDT (Association of Professional Dog Trainers)
- Karen Pryor Clicker Training
- Fear Free Pets

### General Pet Care
- AKC (American Kennel Club)
- CFA (Cat Fanciers' Association)
- House Rabbit Society
- Various breed-specific clubs

## Future Enhancements

Potential improvements:
1. **Symptom photo analysis** - Visual assessment of conditions
2. **Medication reminders** - Schedule and tracking
3. **Vet appointment scheduling** - Integration with vet systems
4. **Pet health dashboard** - Track weight, meds, visits
5. **Training video library** - Visual demonstrations
6. **Community forum** - Connect with other pet owners
7. **Pet expense tracker** - Budget management
8. **DNA breed analysis** - Integration with Embark, Wisdom Panel

## License

Apache 2.0

## Support

For issues or questions:
- Review example use cases
- Check troubleshooting section
- Remember: Always consult your veterinarian for medical concerns

---

**CrewAI Version:** 0.86.0+
**Python Version:** 3.10+
**Agent 485** - Pet Care Assistant

**Medical Disclaimer**: This tool provides educational information only and is not a substitute for professional veterinary advice, diagnosis, or treatment. Always seek the advice of your veterinarian with any questions you may have regarding your pet's health.
