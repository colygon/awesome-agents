# Job Interview Agent - CrewAI Edition

## Overview

The Job Interview Agent is a comprehensive AI-powered interview preparation system that helps candidates prepare for job interviews through multi-agent collaboration. The system analyzes resumes, researches companies, generates relevant questions, provides model answers, and conducts mock interview preparation.

## Features

1. **Resume Analysis** - Extracts and analyzes key skills, experience, and achievements
2. **Company Research** - Gathers information about company culture, values, and recent news
3. **Question Generation** - Creates relevant behavioral, technical, and role-specific questions
4. **Answer Coaching** - Provides model answers and STAR-method frameworks
5. **Mock Interview Prep** - Offers practice plans and confidence-building strategies

## Architecture

### CrewAI Agents

1. **Resume Analyzer Agent** (`resume_analyzer`)
   - Analyzes candidate background and qualifications
   - Identifies strengths and areas for improvement
   - Tools: ResumeAnalysisTool

2. **Company Researcher Agent** (`company_researcher`)
   - Researches target company comprehensively
   - Identifies culture fit talking points
   - Tools: CompanyResearchTool

3. **Question Generator Agent** (`question_generator`)
   - Creates role-specific interview questions
   - Covers behavioral, technical, and situational categories
   - Tools: QuestionGeneratorTool

4. **Answer Coach Agent** (`answer_coach`)
   - Provides model answers using STAR method
   - Offers communication and delivery tips
   - No specific tools (uses LLM reasoning)

5. **Mock Interviewer Agent** (`mock_interviewer`)
   - Conducts mock interview preparation
   - Provides practice plans and feedback frameworks
   - No specific tools (uses LLM reasoning)

### Custom Tools

1. **ResumeAnalysisTool**
   - Supports PDF, DOCX, and TXT formats
   - Extracts structured information via LLM
   - Returns: skills, experience, strengths, gaps

2. **CompanyResearchTool**
   - Integrates with Serper API for web research
   - Searches company news, culture, and interview info
   - Returns: comprehensive company profile

3. **QuestionGeneratorTool**
   - Generates 40-50 questions across categories
   - Tailored to role and experience level
   - Returns: categorized question list

## Setup and Installation

### Prerequisites

- Python 3.10+
- OpenAI API key
- (Optional) Serper API key for automated company research

### Installation

1. **Navigate to directory**

```bash
cd job-interview-agent411
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

Optional (for company research):
```
SERPER_API_KEY=...
```

## Usage

### Interactive Mode

```bash
python main.py
```

Follow the prompts to enter:
- Resume file path (PDF, DOCX, or TXT)
- Job title/role
- Company name

### Example Session

```
Welcome! I will help you prepare for your job interview.

I can help you:
  • Analyze your resume and identify key strengths
  • Research the target company
  • Generate relevant interview questions
  • Provide model answers and coaching
  • Conduct mock interview preparation

Resume file path (PDF/DOCX/TXT): /path/to/resume.pdf
Job title/role: Senior Software Engineer
Company name: Google

Starting interview preparation workflow...

[Agent execution logs...]

INTERVIEW PREPARATION COMPLETE
================================================================================

[Comprehensive preparation guide with questions, answers, and tips]
```

## Output

The system provides:

1. **Resume Analysis**
   - Key skills and competencies
   - Notable achievements
   - Strengths for target role
   - Areas to address

2. **Company Research**
   - Company mission and values
   - Recent news and developments
   - Culture insights
   - 8-10 thoughtful questions to ask

3. **Interview Questions** (40-50 total)
   - 12-15 behavioral (STAR method)
   - 12-15 technical
   - 8-10 role-specific
   - 6-8 culture fit
   - 6-8 situational

4. **Model Answers**
   - 3-5 detailed STAR answers
   - Technical answer frameworks
   - Personalization tips
   - Delivery guidance

5. **Mock Interview Guide**
   - Interview structure overview
   - Opening/closing strategies
   - Practice plan
   - Preparation checklist

## Use Cases

### For Job Seekers
- Prepare for upcoming interviews
- Identify resume strengths and gaps
- Practice common interview questions
- Research target companies effectively

### For Career Coaches
- Help clients prepare systematically
- Generate customized question sets
- Provide structured preparation plans

### For Recruiters
- Understand candidate preparation needs
- Create interview question banks
- Align questions with company values

## Customization

### Adjusting Experience Level

Edit `main.py` to add experience level:

```python
tasks = create_tasks(resume_path, job_title, company_name, experience_level="senior")
```

### Adding New Question Categories

Edit `tools.py` QuestionGeneratorTool to add categories:

```python
6. DOMAIN-SPECIFIC QUESTIONS (5-8 questions):
   - Industry knowledge
   - Regulatory awareness
   - Market trends
```

### Changing LLM Models

Edit tool files to use different models:

```python
llm = ChatOpenAI(model="gpt-4", temperature=0)  # Use GPT-4
```

## Best Practices

1. **Resume Quality** - Use well-formatted resumes for better analysis
2. **Specific Roles** - Be specific about job titles (e.g., "Senior Backend Engineer" vs "Engineer")
3. **Company Research** - Add SERPER_API_KEY for automated research
4. **Practice** - Use generated questions for actual practice sessions
5. **Customization** - Adapt model answers to your personal experiences

## Limitations

1. **Resume Parsing** - Works best with standard resume formats
2. **Company Info** - Automated research requires SERPER_API_KEY
3. **Generic Answers** - Model answers need personalization
4. **No Video** - Cannot assess video interview performance

## Troubleshooting

### "Error analyzing resume"
- Ensure file is readable (not password-protected)
- Check file format (PDF, DOCX, TXT)
- Verify file path is correct

### "Company research incomplete"
- Add SERPER_API_KEY for automated research
- Use manual research guidance provided
- Check internet connectivity

### "Questions too generic"
- Be more specific about job title
- Add company context in inputs
- Customize generated questions manually

## Future Enhancements

1. **Video Practice** - Integration with video recording/analysis
2. **Industry Templates** - Pre-built question sets by industry
3. **Salary Negotiation** - Add compensation discussion coaching
4. **Interview Scheduling** - Integration with calendar tools
5. **Performance Tracking** - Track practice sessions and improvement
6. **LinkedIn Integration** - Pull profile data automatically

## License

This CrewAI implementation is provided as-is for interview preparation purposes.

## Credits

- **Framework:** CrewAI
- **LLM:** OpenAI GPT-4o-mini
- **Implementation:** Claude Code

---

**Created:** December 2025
**Version:** 1.0.0
**Python:** 3.10+
