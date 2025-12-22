# Education Path Advisor for India - CrewAI Edition

## Overview

The Education Path Advisor is a comprehensive AI-powered guidance system designed specifically for Indian students. It provides personalized career counseling, stream selection advice, college recommendations, and detailed educational roadmaps considering the unique aspects of the Indian education system.

## Features

1. **Student Profile Analysis** - Analyzes academic performance, interests, and aptitudes
2. **Career Path Research** - Identifies 10-12 suitable careers with Indian job market insights
3. **Education System Navigation** - Guides through entrance exams, colleges, and admission processes
4. **Stream Selection Advice** - Helps choose between Science, Commerce, Arts/Humanities after 10th
5. **Actionable Roadmap** - Creates timeline with milestones, resources, and backup plans

## Indian Education Context

This system understands and addresses:
- Multiple education boards (CBSE, ICSE, State boards)
- Entrance exams (JEE, NEET, CLAT, CAT, CUET, GATE, etc.)
- Institution tiers (IITs, NITs, IIMs, Central/State universities)
- Reservation policies and quotas
- Scholarship opportunities (NSP, minority, merit-based)
- Budget constraints and education loans
- Regional variations in opportunities

## Architecture

### CrewAI Agents

1. **Student Analyst Agent** (`student_analyst`)
   - Analyzes academic performance and interests
   - Identifies aptitudes and strengths
   - Tools: StudentProfileAnalyzer

2. **Career Researcher Agent** (`career_researcher`)
   - Researches Indian job market
   - Provides salary ranges and growth prospects
   - Tools: CareerPathResearcher

3. **Education Expert Agent** (`education_expert`)
   - Navigates Indian education system
   - Provides institution and exam details
   - Tools: IndianEducationSystemTool

4. **Stream Advisor Agent** (`stream_advisor`)
   - Recommends academic streams after 10th
   - Suggests subject combinations
   - No specific tools (uses LLM reasoning)

5. **Roadmap Creator Agent** (`roadmap_creator`)
   - Creates detailed educational roadmap
   - Provides timelines and milestones
   - No specific tools (uses LLM reasoning)

### Custom Tools

1. **StudentProfileAnalyzer**
   - Analyzes academic strengths and aptitudes
   - Identifies learning style and competitive readiness
   - Returns: comprehensive profile assessment

2. **CareerPathResearcher**
   - Researches careers in Indian context
   - Provides salary ranges in lakhs per annum
   - Returns: 10-12 career options with details

3. **IndianEducationSystemTool**
   - Provides entrance exam and institution info
   - Includes scholarship and financial planning
   - Returns: education pathway guide

## Setup and Installation

### Prerequisites

- Python 3.10+
- OpenAI API key
- (Optional) Serper API key for enhanced research

### Installation

1. **Navigate to directory**

```bash
cd education-path-advisor-agent412
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

4. **Configure environment variables**

```bash
cp .env.example .env
# Edit .env and add your API keys
```

Required:
```
OPENAI_API_KEY=sk-...
```

## Usage

### Interactive Mode

```bash
python main.py
```

Follow the prompts to enter:
- Student name
- Current grade (10th, 12th, etc.)
- Education board
- Academic performance
- Interests and activities
- Location and budget

### Example Session

```
Welcome! I will help you plan your educational journey.

Please provide student information:

Student name: Rahul Sharma
Current grade: 10th
Education board: CBSE

Academic Performance:
Current subjects: Maths, Science, Social Science, English, Hindi
Overall percentage: 85%, Strong in Maths (92%) and Science (88%)

Interests and Activities:
Areas of interest: Technology, robotics, problem-solving
Extracurricular activities: Coding club, Science Olympiad (State rank 15)

Practical Information:
City/State: Bangalore, Karnataka
Education budget: Moderate (₹5-10 lakhs for 4 years)

Analyzing your profile and creating personalized education roadmap...

[Agent execution logs...]

EDUCATION GUIDANCE COMPLETE
================================================================================

[Comprehensive guidance with career options, stream recommendations, and roadmap]
```

## Output

The system provides:

1. **Profile Analysis**
   - Academic strengths by subject
   - Aptitude indicators (analytical, creative, technical, etc.)
   - Learning style assessment
   - Competitive exam readiness

2. **Career Options** (10-12 careers)
   - Career description and suitability
   - Educational requirements
   - Entrance exams needed
   - Top institutions in India
   - Salary ranges (in lakhs per annum)
   - Job market demand and growth
   - Pros and cons

3. **Stream Recommendations** (for 10th graders)
   - Science (PCM/PCB/PCMB) analysis
   - Commerce (with/without Maths) analysis
   - Arts/Humanities options
   - Recommended choice with justification

4. **Education Pathway**
   - Required undergraduate programs
   - Entrance exam details (pattern, syllabus, preparation)
   - Top 10-15 institutions (tier-wise)
   - Fee structures and scholarships
   - Admission timeline

5. **Actionable Roadmap**
   - Immediate actions (next 3 months)
   - Short-term goals (6-12 months)
   - Medium-term goals (1-3 years)
   - Long-term goals (3-5 years)
   - Study resources and coaching
   - Backup plans

## Use Cases

### For Students (10th/12th Standard)
- Choosing stream after 10th
- Identifying suitable careers
- Planning entrance exam preparation
- Selecting colleges and courses

### For Parents
- Understanding career options
- Evaluating education investment
- Planning financial resources
- Supporting child's decisions

### For School Counselors
- Providing structured guidance
- Researching career options
- Creating standardized advice
- Handling multiple students efficiently

### For Career Counselors
- Enhancing counseling practice
- Staying updated on opportunities
- Providing data-backed recommendations

## Customization

### Adding Regional Focus

Edit `tools.py` to add regional preferences:

```python
prompt = f"""Focus on institutions in {region} region:
- {state} state universities
- Regional engineering/medical colleges
- Local scholarship opportunities
"""
```

### Expanding Career Database

Modify `CareerPathResearcher` to include specific sectors:

```python
- Renewable Energy careers
- Healthcare technology
- Biotechnology
- Animation and VFX
- Ethical Hacking
```

### Changing Stream Options

Edit `stream_advisor` agent for specialized streams:

```python
# Add vocational streams
- Hotel Management
- Fashion Design
- Agriculture Sciences
```

## Best Practices

1. **Accurate Information** - Provide honest academic performance data
2. **Detailed Interests** - Be specific about genuine interests
3. **Realistic Budget** - Share actual budget constraints
4. **Open Mind** - Consider unconventional career suggestions
5. **Multiple Sessions** - Use for different career explorations

## Limitations

1. **Data Accuracy** - Entrance exam patterns/dates may change
2. **Fee Structures** - Institution fees are approximate and may vary
3. **Placement Data** - Based on general trends, not guaranteed
4. **Personal Factors** - Cannot assess personality through text alone
5. **Real-time Updates** - May not reflect very recent changes in education policies

## Troubleshooting

### "Generic career suggestions"
- Provide more specific interests and strengths
- Include extracurricular achievements
- Mention any unique talents or skills

### "Institution information outdated"
- Cross-verify with official college websites
- Check current year admission brochures
- Contact institutions directly

### "Budget advice unclear"
- Specify exact budget range in lakhs
- Mention if education loan is considered
- Indicate preference for government vs private

## Future Enhancements

1. **Real-time Data** - Integration with college admission APIs
2. **Psychometric Testing** - Built-in aptitude and interest tests
3. **Mentor Matching** - Connect with alumni in chosen fields
4. **Application Tracker** - Track entrance exam and college applications
5. **Regional Language Support** - Hindi, Tamil, Telugu, etc.
6. **Parent Dashboard** - Separate interface for parents
7. **Scholarship Finder** - Automated scholarship matching
8. **Virtual Campus Tours** - Integration with college virtual tours

## Specific to Indian Education System

### Streams After 10th
- **Science:** PCM (Engineering), PCB (Medical), PCMB (flexibility)
- **Commerce:** With Maths (CA, Economics), Without (BBA, Law)
- **Arts/Humanities:** Psychology, Sociology, Political Science, etc.

### Major Entrance Exams
- **Engineering:** JEE Main, JEE Advanced, BITSAT, VITEEE
- **Medical:** NEET UG, AIIMS, JIPMER
- **Law:** CLAT, AILET
- **Management:** CAT, XAT, SNAP, MAT
- **Design:** NIFT, NID, UCEED
- **General:** CUET (Central Universities)

### Institution Tiers
- **Tier 1:** IITs, NITs, IIMs, AIIMS, NLUs, IIITs
- **Tier 2:** State universities, reputable private colleges
- **Tier 3:** Other accredited institutions

## License

This CrewAI implementation is provided for educational guidance purposes.

## Credits

- **Framework:** CrewAI
- **LLM:** OpenAI GPT-4o-mini
- **Implementation:** Claude Code
- **Context:** Indian Education System

---

**Created:** December 2025
**Version:** 1.0.0
**Target Audience:** Indian students (10th-12th standard)
**Language:** English (Future: Hindi and regional languages)
