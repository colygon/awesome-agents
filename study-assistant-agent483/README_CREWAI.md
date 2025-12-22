# Study Assistant - CrewAI Edition

## Overview

The Study Assistant is a multi-agent academic support system built with CrewAI that helps students learn effectively through three specialized agents:

1. **Content Explainer** - Breaks down complex topics into understandable concepts
2. **Study Planner** - Creates effective study schedules using evidence-based techniques
3. **Test Prep Coach** - Develops exam preparation strategies and practice materials

## Features

- Clear explanations of complex academic topics across all subjects
- Evidence-based study schedules with spaced repetition
- Practice questions and mock exams
- Test-taking strategies and anxiety management
- Personalized learning approaches
- Time management and prioritization
- Progress tracking and milestone planning
- Review schedules optimized for retention

## Architecture

### CrewAI Agents

#### 1. Academic Content Specialist
- **Role**: Explain complex topics clearly
- **Expertise**: Teaching techniques, analogies, step-by-step reasoning
- **Output**: Comprehensive explanations with examples and practice problems

#### 2. Study Strategy Expert
- **Role**: Design effective study plans
- **Expertise**: Spaced repetition, active recall, time management
- **Output**: Detailed study schedules with evidence-based techniques

#### 3. Test Preparation Coach
- **Role**: Prepare students for exams
- **Expertise**: Practice materials, test strategies, anxiety management
- **Output**: Practice questions, mock exams, and test-taking guides

### Process Flow

```
Study Request (Topic + Schedule + Exam Info)
        ↓
Content Explainer → Topic Explanation
        ↓
Study Planner → Study Schedule
        ↓
Test Prep Coach → Practice Materials
        ↓
Complete Study Package
```

## Setup and Installation

### Prerequisites

- Python 3.10+
- OpenAI API key

### Installation

1. **Navigate to directory**

```bash
cd study-assistant-agent483
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
from main import get_study_help

study_request = {
    "topic": "Quadratic equations - completing the square and quadratic formula",

    "schedule_needs": """Algebra 2 exam in 10 days. Can study 1 hour per day.
                        Also need to review linear equations and polynomials.""",

    "exam_details": """50 minute exam with 20 problems. Mix of multiple choice
                      and show-your-work. Teacher emphasizes problem-solving."""
}

result = get_study_help(study_request)
print(result)
```

### Example Output

The system produces:

1. **Topic Explanation**
   - Core concepts broken down
   - Examples and analogies
   - Step-by-step solutions
   - Practice problems with answers
   - Common misconceptions

2. **Study Schedule**
   - Week-by-week plan
   - Daily study sessions
   - Spaced repetition schedule
   - Active recall exercises
   - Progress checkpoints

3. **Test Prep Package**
   - Practice questions (10-20)
   - Mock exam section
   - Test-taking strategies
   - Time management plan
   - Quick reference materials

## Subjects Supported

The system can help with any academic subject:

- **Mathematics**: Algebra, Geometry, Calculus, Statistics
- **Sciences**: Biology, Chemistry, Physics, Earth Science
- **Humanities**: History, Literature, Philosophy, Languages
- **Social Sciences**: Psychology, Sociology, Economics, Political Science
- **Computer Science**: Programming, Algorithms, Data Structures
- **Standardized Tests**: SAT, ACT, GRE, GMAT, MCAT, LSAT

## Evidence-Based Learning Techniques

### Spaced Repetition
- Review material at increasing intervals
- Combats forgetting curve
- Optimal retention with less time

### Active Recall
- Practice retrieving information
- More effective than re-reading
- Strengthens memory pathways

### Interleaving
- Mix different topics in one session
- Improves discrimination and transfer
- Prevents interference

### Pomodoro Technique
- 25 min focused study
- 5 min break
- Maintains concentration and prevents burnout

### Feynman Technique
- Explain concept in simple terms
- Identify knowledge gaps
- Deepen understanding

## Customization

### Adjust Explanation Depth

```python
study_request = {
    "topic": "Photosynthesis",
    "depth": "detailed",  # or "overview", "comprehensive"
    "grade_level": "high school"  # or "middle school", "college"
}
```

### Change Study Duration

```python
schedule_needs = {
    "subjects": ["Biology", "Chemistry", "English"],
    "daily_hours": 2,
    "duration_weeks": 4,
    "exam_dates": {
        "Biology": "2024-03-15",
        "Chemistry": "2024-03-18",
        "English": "2024-03-20"
    }
}
```

### Customize Practice Questions

```python
exam_details = {
    "format": "mixed",
    "question_types": ["multiple_choice", "short_answer", "essay"],
    "practice_count": 15,
    "difficulty": "medium"
}
```

## Integration Options

### Learning Management Systems
- Canvas LMS integration
- Google Classroom
- Moodle

### Note-Taking Apps
- Notion
- Obsidian
- Evernote

### Calendar Integration
- Google Calendar (study blocks)
- Outlook Calendar
- Apple Calendar

### Flashcard Apps
- Anki (spaced repetition)
- Quizlet
- RemNote

## Best Practices

### Effective Studying

1. **Start Early** - Don't cram; spread learning over time
2. **Active Learning** - Practice problems over passive reading
3. **Test Yourself** - Regular self-quizzing
4. **Teach Others** - Best way to solidify understanding
5. **Take Breaks** - Rest improves retention
6. **Stay Consistent** - Regular short sessions beat long marathons

### Study Environment

- Quiet, well-lit space
- Minimize distractions (phone away)
- Have all materials ready
- Comfortable but alert seating
- Good ventilation and temperature

### Time Management

- Schedule specific study times
- Block calendar for study sessions
- Use timers for focus
- Track actual time spent
- Adjust schedule based on progress

## Troubleshooting

### "Explanations too complex"

Request simpler language:
```python
study_request = {
    "topic": "Quantum mechanics",
    "style": "ELI5",  # Explain Like I'm 5
    "use_analogies": True
}
```

### "Not enough practice problems"

Request more:
```python
exam_details = {
    "topic": "Calculus derivatives",
    "practice_count": 30,
    "include_solutions": True
}
```

### "Study schedule too intense"

Adjust parameters:
```python
schedule_needs = {
    "daily_hours": 1,  # Reduced from 2
    "break_frequency": "every 25 min",
    "weekend_study": False  # Take weekends off
}
```

## Performance Optimization

### Reduce API Costs

```python
# Use GPT-3.5-turbo for practice questions
agents = create_all_agents(model="gpt-3.5-turbo", temperature=0.7)

# Use GPT-4 only for complex explanations
explainer = create_content_explainer_agent(
    ChatOpenAI(model="gpt-4", temperature=0.7)
)
```

### Batch Processing

Process multiple topics:
```python
topics = [
    "Photosynthesis",
    "Cellular respiration",
    "DNA replication"
]

for topic in topics:
    result = get_study_help({"topic": topic})
```

## Advanced Features

### Multi-Subject Planning

```python
multi_subject_request = {
    "subjects": {
        "Math": {"exam_date": "2024-03-10", "priority": "high"},
        "History": {"exam_date": "2024-03-12", "priority": "medium"},
        "English": {"exam_date": "2024-03-15", "priority": "medium"}
    },
    "daily_hours": 3,
    "current_understanding": {
        "Math": "struggling",
        "History": "confident",
        "English": "moderate"
    }
}
```

### Learning Style Adaptation

```python
study_request = {
    "topic": "French Revolution",
    "learning_style": "visual",  # or "auditory", "kinesthetic"
    "preferences": {
        "examples": "historical",
        "format": "timeline and diagrams"
    }
}
```

### Adaptive Difficulty

```python
# System tracks performance and adjusts
practice_session = {
    "topic": "Algebra word problems",
    "adaptive": True,
    "starting_difficulty": "medium",
    "target_accuracy": 0.80  # Adjusts to maintain 80% success rate
}
```

## Study Metrics

Track progress with key metrics:

- **Study Time**: Hours spent per subject
- **Practice Accuracy**: Percentage correct on practice problems
- **Retention Rate**: Performance on spaced repetition reviews
- **Progress to Goal**: Percentage through study plan
- **Confidence Level**: Self-assessed understanding

## Example Use Cases

### High School Student

```python
request = {
    "topic": "AP Calculus - Integration techniques",
    "schedule_needs": "AP exam in 6 weeks, 1 hour per day",
    "exam_details": "Multiple choice + free response, need 70% for college credit"
}
```

### College Exam Prep

```python
request = {
    "topic": "Organic Chemistry - Reaction mechanisms",
    "schedule_needs": "Midterm in 2 weeks, 2-3 hours daily",
    "exam_details": "Cumulative exam, 25 mechanisms to know"
}
```

### Standardized Test

```python
request = {
    "topic": "GRE Quantitative - Geometry and Data Analysis",
    "schedule_needs": "Test in 3 months, 10 hours per week",
    "exam_details": "Computer adaptive, need 160+ score"
}
```

### Adult Learner

```python
request = {
    "topic": "Python programming basics",
    "schedule_needs": "Self-paced, 30 min per day",
    "exam_details": "No exam, building portfolio projects"
}
```

## Future Enhancements

Potential improvements:
1. **AI Tutor Chat** - Real-time Q&A with follow-ups
2. **Video Explanations** - Generate or curate video content
3. **Progress Dashboard** - Visual tracking of learning
4. **Peer Study Matching** - Connect with other learners
5. **Adaptive Learning Paths** - Personalized based on performance
6. **Gamification** - Achievements and rewards
7. **Mobile App** - Study on the go
8. **Handwriting Recognition** - Scan and analyze written work

## Study Resources

Recommended external resources:

### Free Resources
- Khan Academy (all subjects)
- Coursera (university courses)
- MIT OpenCourseWare
- Crash Course (YouTube)
- Paul's Online Math Notes

### Practice Problems
- Art of Problem Solving
- Brilliant.org
- LeetCode (programming)
- Project Euler (math/CS)

### Flashcards
- Anki (spaced repetition)
- Quizlet
- RemNote

## License

Apache 2.0

## Support

For issues or questions:
- Review example use cases
- Check troubleshooting section
- Adjust agent parameters for better explanations

---

**CrewAI Version:** 0.86.0+
**Python Version:** 3.10+
**Agent 483** - Study Assistant
