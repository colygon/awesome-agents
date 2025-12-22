"""
YouTube Thumbnail CrewAI Tasks
Defines the workflow for thumbnail analysis and design
"""

from crewai import Task
from agents import thumbnail_analyst, design_strategist, optimization_expert

def create_tasks(video_topic: str, target_audience: str = "general", existing_thumbnail_url: str = None):
    """
    Create tasks for YouTube thumbnail workflow

    Args:
        video_topic: Topic or title of the YouTube video
        target_audience: Target audience description
        existing_thumbnail_url: Optional URL of existing thumbnail to analyze

    Returns:
        List of Task objects
    """

    # Task 1: Analyze thumbnail landscape and competitors
    analyze_landscape_task = Task(
        description=f"""Analyze the YouTube thumbnail landscape for videos about: {video_topic}

        Target audience: {target_audience}
        {f"Existing thumbnail to analyze: {existing_thumbnail_url}" if existing_thumbnail_url else ""}

        Your objectives:
        1. Research successful thumbnails in this niche
        2. Identify common patterns and trends
        3. Analyze what makes top-performing thumbnails effective:
           - Color schemes and contrast
           - Facial expressions and emotions
           - Text usage (size, placement, wording)
           - Visual elements and composition
           - Curiosity triggers and hooks
        4. Identify what to avoid (overused tropes, ineffective patterns)
        5. {f"Analyze the existing thumbnail and provide critique" if existing_thumbnail_url else "Note gaps and opportunities"}
        6. Understand platform requirements (dimensions, text safety zones)
        7. Consider mobile vs desktop viewing experience

        Provide a comprehensive analysis including:
        - Top 5 thumbnail patterns that work in this niche
        - Common effective elements (colors, emotions, layouts)
        - What successful creators are doing
        - Mistakes to avoid
        - {f"Strengths and weaknesses of existing thumbnail" if existing_thumbnail_url else "Opportunities for differentiation"}
        - Mobile optimization considerations""",
        agent=thumbnail_analyst,
        expected_output="""A detailed analysis report containing:
        - List of 5+ successful thumbnail patterns in this niche
        - Analysis of effective visual elements (colors, emotions, text styles)
        - Competitor insights and trends
        - List of elements to avoid
        - Platform requirements and constraints
        - Mobile vs desktop considerations
        {f"- Critique of existing thumbnail with specific improvements" if existing_thumbnail_url else "- Opportunities for standing out"}"""
    )

    # Task 2: Create thumbnail design concepts
    create_designs_task = Task(
        description=f"""Based on the thumbnail landscape analysis, create 3-5 compelling
        thumbnail design concepts for a video about: {video_topic}

        Target audience: {target_audience}

        Your objectives:
        1. Generate 3-5 distinct thumbnail concepts, each with:
           - Main visual elements (images, faces, objects)
           - Color scheme and contrast strategy
           - Text overlay (headline, supporting text)
           - Composition and layout
           - Emotional hook or curiosity trigger
           - Design rationale
        2. Ensure each concept:
           - Stands out from competitors while fitting the niche
           - Creates curiosity or emotional response
           - Is clearly readable on mobile devices
           - Accurately represents the video content
           - Uses proven psychological triggers
        3. Vary approaches:
           - Different emotional angles
           - Different visual styles
           - Different text strategies
        4. Include specific design specifications:
           - Dimensions: 1280x720 pixels (16:9 ratio)
           - File format: JPG or PNG, under 2MB
           - Text size recommendations
           - Safe zones for mobile viewing

        For each concept provide:
        - Concept name and core idea
        - Detailed visual description
        - Text elements (exact wording)
        - Color palette (hex codes)
        - Design rationale and psychology
        - Expected impact on click-through rate""",
        agent=design_strategist,
        expected_output="""3-5 detailed thumbnail design concepts, each including:
        - Concept name and core hook
        - Complete visual description (layout, images, elements)
        - Exact text overlay with font size recommendations
        - Color palette with specific hex codes
        - Emotional/psychological strategy
        - Technical specifications (dimensions, file size)
        - Rationale for why this will perform well
        - Predicted audience response""",
        context=[analyze_landscape_task]
    )

    # Task 3: Optimize and create A/B testing variations
    optimize_designs_task = Task(
        description=f"""Based on the thumbnail design concepts, optimize and create
        A/B testing variations for: {video_topic}

        Your objectives:
        1. Select the 2 most promising concepts from the designs
        2. For each concept, create 2-3 variations for A/B testing:
           - Vary text wording or placement
           - Test different color schemes
           - Try different facial expressions or emotions
           - Adjust composition or focal points
        3. Ensure all variations:
           - Meet YouTube's technical requirements
           - Are optimized for mobile viewing
           - Maintain brand consistency (if applicable)
           - Are accessible (consider color blindness, readability)
        4. Create a testing strategy:
           - Which variations to test against each other
           - Key metrics to track (CTR, watch time impact)
           - Hypothesis for each variation
           - Sample size recommendations
        5. Provide implementation guidelines:
           - Tools and software recommendations
           - Step-by-step creation process
           - Quality checklist
           - Upload and testing procedures

        Deliver:
        - 2 primary concepts, each with 2-3 variations (4-6 total thumbnails)
        - Detailed specifications for each variation
        - A/B testing strategy and implementation plan
        - Success metrics and evaluation criteria
        - Timeline for testing and iteration""",
        agent=optimization_expert,
        expected_output="""A comprehensive optimization package including:
        - 2 primary thumbnail concepts
        - 2-3 variations per concept (4-6 total designs)
        - Detailed specifications for each variation
        - A/B testing strategy with hypotheses
        - Implementation guide (tools, steps, checklist)
        - Metrics and KPIs to track
        - Testing timeline and decision framework
        - Mobile optimization checklist
        - Accessibility considerations""",
        context=[analyze_landscape_task, create_designs_task]
    )

    return [analyze_landscape_task, create_designs_task, optimize_designs_task]
