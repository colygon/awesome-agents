"""SalesShortcut SDR Tasks"""

from crewai import Task
from agents import lead_researcher, personalization_specialist, email_copywriter, sequence_designer, objection_handler, performance_optimizer


def create_tasks(campaign_info: dict):
    """Create SDR campaign tasks"""

    target_industry = campaign_info.get('industry', 'SaaS')
    product = campaign_info.get('product', 'Software')

    research_task = Task(
        description=f"""Research leads for {product} in {target_industry} industry.

        Research:
        1. Ideal customer profile (ICP)
        2. Company research (size, revenue, tech stack)
        3. Decision maker identification
        4. Pain points and challenges
        5. Buying signals and triggers
        6. Competitor intel

        Create detailed lead profiles with:
        - Company overview
        - Key contacts (name, title, LinkedIn)
        - Relevant news/triggers
        - Pain points to address
        - Personalization angles""",
        agent=lead_researcher,
        expected_output="Qualified lead profiles with research insights"
    )

    personalize_task = Task(
        description=f"""Create personalization strategy for {target_industry} prospects.

        Develop:
        1. Industry-specific pain points
        2. Company-specific research points
        3. Personalization frameworks
        4. Reference points (news, events, posts)
        5. Value propositions for different personas

        For each prospect type, identify:
        - What to mention
        - How to demonstrate research
        - Relevant case studies or examples""",
        agent=personalization_specialist,
        expected_output="Personalization playbook",
        context=[research_task]
    )

    write_emails_task = Task(
        description=f"""Write sales email templates for {product} targeting {target_industry}.

        Create 5-7 email variations:
        1. Cold outreach email (first touch)
        2. Follow-up emails (2-3 versions)
        3. Value-add email (sharing insights)
        4. Breakup email (final attempt)
        5. Re-engagement email

        For each email:
        - Compelling subject line (3 options)
        - Opening hook with personalization
        - Problem/pain point identification
        - Value proposition
        - Social proof if relevant
        - Clear, low-friction CTA
        - Keep under 125 words

        Include merge fields for personalization.""",
        agent=email_copywriter,
        expected_output="Complete email template library",
        context=[research_task, personalize_task]
    )

    design_sequence_task = Task(
        description=f"""Design outreach sequence for {target_industry} SDR campaign.

        Create multi-touch sequence:
        1. Day 1: Initial email
        2. Day 3: LinkedIn connection request
        3. Day 5: Follow-up email
        4. Day 8: LinkedIn message (if connected)
        5. Day 11: Value-add email (share resource)
        6. Day 15: Phone call attempt
        7. Day 18: Breakup email
        8. Day 45: Re-engagement

        For each touchpoint:
        - Channel (email/LinkedIn/phone)
        - Message/script
        - Goal of touchpoint
        - Success criteria

        Include:
        - Optimal send times
        - A/B testing suggestions
        - Cadence rationale""",
        agent=sequence_designer,
        expected_output="Complete outreach sequence",
        context=[research_task, personalize_task, write_emails_task]
    )

    handle_objections_task = Task(
        description=f"""Prepare objection handling guide for {product} SDRs.

        Common objections to address:
        1. "Not interested" / "Not the right time"
        2. "Too expensive" / "No budget"
        3. "Happy with current solution"
        4. "Send me information"
        5. "Call me later" / "Not a priority"
        6. "Already tried something similar"

        For each objection:
        - Empathetic acknowledgment
        - Reframe/question technique
        - Value-focused response
        - Path to next step
        - Example dialogue

        Include:
        - When to push vs when to nurture
        - How to pivot conversations
        - Discovery questions to ask""",
        agent=objection_handler,
        expected_output="Objection handling playbook",
        context=[research_task, personalize_task]
    )

    optimize_task = Task(
        description=f"""Create performance optimization framework for SDR campaign.

        Define KPIs to track:
        1. Email metrics (open rate, reply rate, bounce rate)
        2. LinkedIn metrics (connection rate, response rate)
        3. Phone metrics (contact rate, conversation rate)
        4. Meeting booking rate
        5. Qualified opportunity rate

        Create optimization plan:
        1. A/B test plan (subject lines, CTAs, timing)
        2. Performance benchmarks
        3. Review cadence
        4. Improvement recommendations
        5. Reporting dashboard structure

        Include:
        - What to track daily/weekly/monthly
        - When to iterate messaging
        - Success criteria for campaign""",
        agent=performance_optimizer,
        expected_output="Performance optimization framework",
        context=[design_sequence_task, write_emails_task]
    )

    return [research_task, personalize_task, write_emails_task, design_sequence_task, handle_objections_task, optimize_task]
