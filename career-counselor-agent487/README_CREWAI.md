# Career Counselor - CrewAI Edition

## Overview

The Career Counselor is a multi-agent career guidance system built with CrewAI that provides comprehensive support through three specialized agents:

1. **Career Development Specialist** - Career path guidance and planning
2. **Resume & Interview Coach** - Application materials and interview preparation
3. **Job Search Strategist** - Search strategy, networking, and personal branding

## Features

- Personalized career path recommendations
- Skills gap analysis and development plans
- Resume and cover letter optimization (ATS-friendly)
- Interview preparation with STAR method
- Salary research and negotiation strategies
- LinkedIn profile optimization
- Networking and personal branding guidance
- Job search strategy and organization
- Industry insights and market trends
- Career transition support

## Architecture

### CrewAI Agents

#### 1. Career Development Specialist
- **Role**: Guide career exploration and planning
- **Expertise**: Career paths, industry trends, skill development
- **Output**: Career roadmap with action plan

#### 2. Resume & Interview Coach
- **Role**: Create compelling application materials
- **Expertise**: Resume writing, ATS optimization, interview techniques
- **Output**: Resume template, interview prep guide

#### 3. Job Search Strategist
- **Role**: Design effective job search plans
- **Expertise**: Networking, LinkedIn, personal branding, job market
- **Output**: Search strategy, networking plan, branding guide

### Process Flow

```
Career Request (Situation + Goals)
        ↓
Career Advisor → Career Path Guidance
        ↓
Resume/Interview Coach → Application Materials
        ↓
Job Search Strategist → Search Strategy
        ↓
Complete Career Package
```

## Setup and Installation

### Prerequisites

- Python 3.10+
- OpenAI API key

### Installation

1. **Navigate to directory**

```bash
cd career-counselor-agent487
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
from main import get_career_guidance

request = {
    "career_situation": """Software engineer with 5 years experience in backend.
                          Want to transition to machine learning/AI roles.""",
    "application_needs": "Need ML-focused resume and interview prep for FAANG",
    "search_parameters": "Targeting ML Engineer roles at big tech, remote OK"
}

result = get_career_guidance(request)
print(result)
```

### Example Output

The system produces:

1. **Career Guidance**
   - Career path recommendations
   - Skills to develop
   - Education/certifications needed
   - Industry insights
   - Action plan with timeline

2. **Application Package**
   - ATS-optimized resume template
   - Cover letter framework
   - 15-20 interview questions
   - Salary negotiation guide
   - Follow-up templates

3. **Job Search Strategy**
   - Target company list
   - LinkedIn optimization
   - Networking action plan
   - Personal brand statement
   - Weekly activity goals

## Common Use Cases

### Career Change

```python
request = {
    "career_situation": "Teacher for 10 years, want to transition to corporate training/L&D",
    "application_needs": "Translate teaching experience to corporate language",
    "search_parameters": "Breaking into corporate world without corporate experience"
}
```

### New Graduate

```python
request = {
    "career_situation": "Recent CS graduate, internship at startup, looking for first full-time role",
    "application_needs": "Entry-level resume with limited experience",
    "search_parameters": "Campus recruiting vs general applications"
}
```

### Mid-Career Advancement

```python
request = {
    "career_situation": "Senior Analyst wanting to move to Manager level",
    "application_needs": "Show leadership readiness on resume",
    "search_parameters": "Internal promotion vs external opportunities"
}
```

### Return to Workforce

```python
request = {
    "career_situation": "3-year career gap for family, previously in project management",
    "application_needs": "Address employment gap positively",
    "search_parameters": "Re-entering job market, update skills and network"
}
```

### Remote Work Search

```python
request = {
    "career_situation": "Want to transition from office to fully remote role",
    "application_needs": "Highlight remote work capabilities",
    "search_parameters": "Finding legitimate remote opportunities"
}
```

## Career Stages Supported

- **Entry-Level** - First job, internship to full-time
- **Early Career** - 1-3 years, building foundation
- **Mid-Career** - 4-10 years, advancement and specialization
- **Senior** - 10+ years, leadership and strategy
- **Executive** - C-suite, board roles
- **Career Change** - Industry/function pivots
- **Return to Work** - After career breaks

## Resume Best Practices

### Format
- Clean, ATS-friendly (no images/graphics)
- Chronological (most common) or combination
- 1 page for <10 years experience, 2 pages for 10+
- Consistent formatting and fonts
- Standard section headers

### Content
- Achievement-focused bullets (not task lists)
- Quantified results (numbers, percentages, $)
- STAR method for accomplishments
- Keywords from job description
- Professional summary at top
- Skills section with relevant tools

### ATS Optimization
- Use standard section headers
- Include exact keywords from job posting
- List skills explicitly
- Avoid headers/footers, tables, columns
- Save as .docx or PDF (check job posting)
- Use standard fonts (Arial, Calibri, Times)

## Interview Preparation

### STAR Method
- **Situation**: Set the context
- **Task**: Describe the challenge
- **Action**: What YOU did (be specific)
- **Result**: Outcome with metrics

### Common Questions
- "Tell me about yourself"
- "Why are you interested in this role?"
- "Tell me about a time you failed"
- "Where do you see yourself in 5 years?"
- "Why are you leaving your current role?"
- "What's your greatest weakness?"

### Company Research
- Company mission and values
- Recent news and achievements
- Products/services and competitors
- Company culture (Glassdoor, LinkedIn)
- Interviewer backgrounds (LinkedIn)

### Questions to Ask
- Team structure and dynamics
- Success metrics for the role
- Onboarding and training
- Career growth opportunities
- Company challenges and goals
- Next steps in process

## LinkedIn Optimization

### Profile Sections

**Headline** (120 characters)
- More than job title
- Value proposition
- Keywords for searchability
- Example: "Product Manager | SaaS | Helping teams build products users love"

**About** (2000 characters)
- Personal story and passion
- Key achievements
- What you're looking for
- Call to action
- Readable paragraphs (not wall of text)

**Experience**
- Achievement-focused bullets
- Quantified results
- Keywords naturally integrated
- Rich media (presentations, articles)

**Skills**
- Top 3 match target role
- 50 skills maximum
- Get endorsements
- Take skill assessments

**Recommendations**
- 3-5 quality recommendations
- From managers, colleagues, clients
- Recent (last 2-3 years)
- Specific to your skills

### Profile Optimization
- Professional photo (headshot, smiling)
- Custom background banner
- Custom URL (linkedin.com/in/yourname)
- Featured section (portfolio, articles)
- Open to Work (if actively searching)
- Creator mode (if sharing content)

## Networking Strategies

### Informational Interviews
- Reach out to people in target roles
- 20-30 minute coffee chats
- Ask about their path and advice
- Don't ask for job directly
- Follow up and stay in touch

### Networking Events
- Industry conferences
- Meetups and workshops
- Alumni events
- Professional associations
- Virtual networking (LinkedIn)

### Email Templates

**Informational Interview Request:**
```
Subject: [Mutual connection] suggested I reach out

Hi [Name],

I'm a [your role] interested in [their field/company].
[Mutual connection] suggested I reach out to you.

Would you have 20 minutes for a brief chat about your
experience at [company]? I'm particularly interested in
[specific topic].

I'm flexible on timing and happy to work around your schedule.

Thanks,
[Your name]
```

**Follow-up After Interview:**
```
Subject: Thank you - [Position] interview

Hi [Interviewer name],

Thank you for taking the time to speak with me today about
the [Position] role. I enjoyed learning about [specific topic
discussed] and am excited about the opportunity to [value you'd bring].

Our conversation reinforced my interest in [company/role] because
[specific reason based on conversation].

Please let me know if you need any additional information from me.

Best regards,
[Your name]
```

## Salary Negotiation

### Research Phase
- Use Glassdoor, levels.fyi, PayScale
- Consider location, company size, industry
- Account for total compensation (base + bonus + equity + benefits)
- Know your walk-away number

### Timing
- Don't discuss salary until offer stage
- If asked early: "I'm flexible and want to learn more about the role first"
- When they ask your expectations: Give a range based on research

### Negotiation Tips
- Wait for written offer
- Take 24-48 hours to consider
- Negotiate total package (not just salary)
- Be professional and grateful
- Have specific reasons for your ask
- Be prepared to walk away

### What to Negotiate
- Base salary
- Sign-on bonus
- Performance bonus
- Equity/stock options
- Vacation time
- Remote work flexibility
- Professional development budget
- Relocation assistance
- Start date

## Job Search Timeline

### Month 1: Preparation
- Update resume and LinkedIn
- Research target companies
- Build networking list
- Prepare interview stories
- Set up job alerts

### Month 2: Active Search
- Apply to 10-15 jobs per week
- 5-10 networking conversations
- Attend 1-2 networking events
- Track all applications
- Follow up on applications

### Month 3: Interviewing
- Multiple interview processes
- Continue applying to new roles
- Negotiate offers
- Make decision

### Weekly Activities
- 10-15 job applications
- 3-5 networking contacts
- 2-3 informational interviews
- LinkedIn engagement (daily)
- Skills development (courses, projects)

## Customization

### Industry-Specific Guidance

```python
industry_focus = {
    "tech": "Technical skills, GitHub, system design",
    "finance": "Certifications (CFA, CPA), quantitative skills",
    "healthcare": "Licenses, clinical experience, patient care",
    "creative": "Portfolio, visual work samples, creative process"
}
```

### Career Level Adjustments

```python
level_focus = {
    "entry": "Education, internships, projects, potential",
    "mid": "Achievements, impact, team collaboration",
    "senior": "Leadership, strategy, business impact",
    "executive": "Vision, P&L, organizational transformation"
}
```

## Troubleshooting

### "Not getting interviews"

Checklist:
- [ ] Resume ATS-optimized
- [ ] Tailoring resume to each job
- [ ] Using keywords from job posting
- [ ] Applying within 48 hours of posting
- [ ] Leveraging network for referrals
- [ ] LinkedIn profile complete and active

### "Bombing interviews"

Common issues:
- Insufficient company research
- Not using STAR method
- Talking too much or too little
- Focusing on tasks not achievements
- Not asking good questions
- Poor body language/energy

Practice:
- Record mock interviews
- Get feedback from others
- Prepare 5-7 core stories
- Practice out loud (not just in head)

### "Offers below expectations"

Strategies:
- Know your market value
- Have multiple offers if possible
- Negotiate professionally
- Consider total compensation
- Understand company constraints
- Be willing to walk away

## Future Enhancements

Potential improvements:
1. **Resume builder** - Interactive resume creation
2. **Mock interviews** - AI-powered interview practice
3. **Application tracker** - Track all applications and follow-ups
4. **Networking CRM** - Manage professional relationships
5. **Skills assessment** - Identify strengths and gaps
6. **Career path simulator** - Project career scenarios
7. **Salary calculator** - Real-time market data
8. **Job matching** - AI-powered job recommendations

## Resources

### Job Boards
- LinkedIn (best for networking)
- Indeed (volume)
- Glassdoor (company reviews + jobs)
- AngelList (startups)
- Built In (tech)
- Industry-specific sites

### Career Development
- Coursera, Udemy (online courses)
- LinkedIn Learning
- Professional certifications
- Industry conferences
- Mentorship programs

### Networking
- LinkedIn (primary)
- Alumni networks
- Professional associations
- Meetup.com
- Industry Slack/Discord communities

### Salary Research
- levels.fyi (tech)
- Glassdoor
- PayScale
- Salary.com
- Bureau of Labor Statistics

## License

Apache 2.0

## Support

For issues or questions:
- Review example use cases
- Check troubleshooting section
- Adjust parameters for your situation

---

**CrewAI Version:** 0.86.0+
**Python Version:** 3.10+
**Agent 487** - Career Counselor

**Career Guidance Note**: This tool provides educational career guidance. Career decisions should be made based on your individual circumstances, goals, and professional advice from licensed career counselors when appropriate.
