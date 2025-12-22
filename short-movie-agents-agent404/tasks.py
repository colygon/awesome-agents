"""
Short Movie Agents CrewAI Tasks
Defines the workflow for short film development
"""

from crewai import Task
from agents import (
    story_developer,
    screenwriter,
    storyboard_artist,
    character_developer,
    directors_vision
)


def create_tasks(concept: str, genre: str = "drama", duration: int = 10):
    """
    Create tasks for short film development workflow

    Args:
        concept: The initial story concept or prompt
        genre: Film genre (drama, comedy, thriller, etc.)
        duration: Target duration in minutes

    Returns:
        List of Task objects
    """

    # Task 1: Develop Story Concept
    concept_task = Task(
        description=f"""Develop a compelling story concept for a short film.

        Initial Concept/Prompt: {concept}
        Genre: {genre}
        Target Duration: {duration} minutes

        Create a detailed story concept that includes:
        1. Logline: One-sentence summary of the story
        2. Synopsis: 2-3 paragraph overview of the complete story
        3. Three-Act Structure:
           - Act 1 (Setup): Introduce world, characters, and conflict
           - Act 2 (Confrontation): Develop conflict and challenges
           - Act 3 (Resolution): Resolve conflict and conclude story
        4. Core Theme: The deeper meaning or message
        5. Emotional Arc: The emotional journey of the protagonist
        6. Key Plot Points: Major story beats and turning points
        7. Setting: Time period and locations
        8. Target Audience: Who this film is for

        Ensure the story is achievable within {duration} minutes and has a clear,
        impactful narrative suitable for short film format.""",
        agent=story_developer,
        expected_output="""A comprehensive story concept document containing:
        - Logline
        - Detailed synopsis
        - Three-act structure breakdown
        - Theme and emotional arc
        - Key plot points
        - Setting description
        - Target audience"""
    )

    # Task 2: Develop Characters
    character_task = Task(
        description="""Based on the story concept, develop rich, believable characters.

        Create detailed character profiles for:
        1. Protagonist: Main character
        2. Antagonist: If applicable (could be internal conflict, situation, or person)
        3. Supporting Characters: 1-3 key supporting roles

        For each character, provide:
        - Name and Age
        - Physical Description
        - Personality Traits (5-7 key traits)
        - Background/Backstory
        - Motivation: What they want
        - Need: What they actually need (may differ from want)
        - Character Arc: How they change through the story
        - Relationships: How they relate to other characters
        - Distinctive Voice: Speech patterns, vocabulary, mannerisms
        - Key Strengths and Flaws

        Characters should feel authentic, serve the story, and be distinct from each other.""",
        agent=character_developer,
        expected_output="""Character profiles for all major characters including:
        - Complete character details (name, age, description)
        - Personality and background
        - Motivations and needs
        - Character arcs
        - Relationships and distinctive voices""",
        context=[concept_task]
    )

    # Task 3: Write Screenplay
    screenplay_task = Task(
        description=f"""Write a complete screenplay for the short film.

        Based on:
        - Story concept
        - Character profiles

        Create a properly formatted screenplay ({duration} minute film ≈ {duration} pages) that includes:

        1. Title Page: Film title, "Written by [Your Name]", date
        2. Proper Screenplay Format:
           - Scene headings (INT./EXT., LOCATION, TIME)
           - Action lines (present tense, visual descriptions)
           - Character names (centered, ALL CAPS)
           - Dialogue (centered below character name)
           - Parentheticals (for delivery/action during dialogue)
           - Transitions (CUT TO:, FADE IN:, etc.)

        3. Story Elements:
           - Strong opening that hooks the audience
           - Clear character introductions
           - Rising tension and conflict
           - Emotional moments
           - Satisfying resolution
           - Visual storytelling (show, don't tell)

        4. Technical Considerations:
           - Realistic dialogue that reveals character
           - Efficient pacing
           - Cinematic descriptions
           - Feasible for production

        Write in a visual, engaging style that brings the story to life.""",
        agent=screenwriter,
        expected_output="""A complete, properly formatted screenplay including:
        - Title page
        - Full script with correct formatting
        - Scene headings, action, dialogue
        - Approximately {duration} pages
        - Visual, cinematic writing""",
        context=[concept_task, character_task]
    )

    # Task 4: Create Storyboard
    storyboard_task = Task(
        description="""Create detailed storyboard descriptions for key scenes and shots.

        Based on the screenplay, develop visual storyboards that describe:

        For 10-15 key shots/scenes:
        1. Scene/Shot Number
        2. Scene Description: What's happening
        3. Shot Type: Close-up, medium shot, wide shot, etc.
        4. Camera Angle: Eye-level, high angle, low angle, POV, etc.
        5. Camera Movement: Static, pan, tilt, dolly, tracking, handheld
        6. Composition: Frame composition, rule of thirds, leading lines
        7. Lighting: Mood, key lighting approach (soft, hard, natural, etc.)
        8. Key Visual Elements: Important props, costume details, set elements
        9. Color Palette: Dominant colors and mood
        10. Audio Notes: Important sound elements or music cues
        11. Emotional Impact: What feeling this shot should evoke

        Focus on:
        - Opening shot (sets tone)
        - Character introduction shots
        - Key dramatic moments
        - Climax
        - Closing shot

        Provide enough detail that a director and cinematographer can visualize
        each shot clearly.""",
        agent=storyboard_artist,
        expected_output="""Detailed storyboard descriptions for 10-15 key shots including:
        - Shot specifications (type, angle, movement)
        - Composition and framing details
        - Lighting and color notes
        - Audio elements
        - Emotional impact for each shot""",
        context=[screenplay_task]
    )

    # Task 5: Director's Vision Statement
    vision_task = Task(
        description=f"""Create a comprehensive director's vision statement for the film.

        Based on all the development work (story, characters, script, storyboard),
        articulate the creative vision for this {duration}-minute short film.

        Your vision statement should cover:

        1. Artistic Vision:
           - Overall tone and mood
           - Visual style and aesthetic
           - Thematic focus

        2. Storytelling Approach:
           - How to interpret the script
           - Pacing and rhythm
           - Emotional beats to emphasize

        3. Visual Style:
           - Cinematography approach
           - Color palette and lighting strategy
           - Shot selection philosophy

        4. Performance Direction:
           - Character interpretation guidance
           - Emotional authenticity approach
           - Key performance moments

        5. Production Design:
           - Setting and location approach
           - Key props and costume elements
           - Overall production design aesthetic

        6. Sound Design:
           - Music approach and style
           - Sound effects philosophy
           - Use of silence and audio dynamics

        7. Editing Style:
           - Pacing approach
           - Transition style
           - Rhythm and flow

        8. Audience Experience:
           - Intended emotional journey
           - What viewers should feel and think
           - Key takeaways

        Create a cohesive vision that ties all elements together and guides the
        production team.""",
        agent=directors_vision,
        expected_output="""A comprehensive director's vision statement including:
        - Artistic vision and tone
        - Visual and cinematography approach
        - Performance direction
        - Production design guidance
        - Sound and editing philosophy
        - Intended audience experience
        - Cohesive creative direction""",
        context=[concept_task, character_task, screenplay_task, storyboard_task]
    )

    return [concept_task, character_task, screenplay_task, storyboard_task, vision_task]
