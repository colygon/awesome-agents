"""
Custom Tools for Short Movie Agents
Provides scriptwriting, storyboarding, and creative development tools
"""

from crewai_tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field


class ScriptWritingInput(BaseModel):
    """Input schema for ScriptWritingTool"""
    scene_description: str = Field(..., description="Description of the scene to write")
    characters: str = Field(..., description="Characters in the scene")


class ScriptWritingTool(BaseTool):
    name: str = "Script Writing Tool"
    description: str = """Helps format and structure screenplay scenes with proper formatting.
    Provides screenplay formatting guidelines and scene structure templates."""
    args_schema: Type[BaseModel] = ScriptWritingInput

    def _run(self, scene_description: str, characters: str) -> str:
        """Provide screenplay formatting guidelines"""

        template = f"""Screenplay Formatting Guide:

Scene: {scene_description}
Characters: {characters}

Standard Format:
```
INT./EXT. LOCATION - TIME

Action description in present tense. Describe what we see and hear.
Visual, cinematic language. Each paragraph = separate action.

CHARACTER NAME
(parenthetical if needed)
Dialogue goes here. Natural speech.
Each line of dialogue separate.

More action description...

CHARACTER NAME
Response dialogue.
```

Key Formatting Rules:
- Scene headings: ALL CAPS, INT. or EXT., location, day/night
- Action: Present tense, double-spaced, visual descriptions
- Character names: ALL CAPS when first introduced, caps before dialogue
- Dialogue: Centered, natural speech patterns
- Parentheticals: Use sparingly for crucial delivery notes
- Transitions: FADE IN:, CUT TO:, FADE OUT: (right-aligned)

Remember: Show, don't tell. Write visually. Keep it concise."""

        return template


class DialogueInput(BaseModel):
    """Input schema for DialogueTool"""
    character: str = Field(..., description="Character speaking")
    situation: str = Field(..., description="Dramatic situation")
    emotion: str = Field(..., description="Emotional state")


class DialogueTool(BaseTool):
    name: str = "Dialogue Tool"
    description: str = """Provides guidance for writing effective dialogue that reveals
    character and advances the story. Helps with subtext and natural speech patterns."""
    args_schema: Type[BaseModel] = DialogueInput

    def _run(self, character: str, situation: str, emotion: str) -> str:
        """Provide dialogue writing guidelines"""

        guidelines = f"""Dialogue Writing Guidelines:

Character: {character}
Situation: {situation}
Emotional State: {emotion}

Effective Dialogue Principles:

1. Subtext: Characters don't always say what they mean
   - What's said vs. what's meant
   - Tension between words and body language

2. Natural Speech:
   - Use contractions
   - Incomplete sentences
   - Interruptions and overlaps
   - Pauses and hesitations
   - Unique speech patterns per character

3. Purpose:
   - Reveals character
   - Advances plot
   - Creates conflict or builds relationships
   - Provides necessary information (subtly)

4. Avoid:
   - On-the-nose dialogue (too direct)
   - Unnecessary exposition
   - All characters sounding the same
   - Overly formal or literary speech

5. Character Voice:
   - Education level
   - Regional background
   - Age and generation
   - Personality traits
   - Current emotional state

Make every line count. Cut unnecessary words."""

        return guidelines


class StoryboardInput(BaseModel):
    """Input schema for StoryboardTool"""
    scene: str = Field(..., description="Scene to storyboard")


class StoryboardTool(BaseTool):
    name: str = "Storyboard Tool"
    description: str = """Helps create detailed storyboard descriptions with shot types,
    camera angles, composition, and visual elements."""
    args_schema: Type[BaseModel] = StoryboardInput

    def _run(self, scene: str) -> str:
        """Provide storyboarding guidelines"""

        guide = f"""Storyboard Guide for Scene:
{scene}

Shot Types:
- ECU (Extreme Close-Up): Very tight on detail
- CU (Close-Up): Face, object detail
- MCU (Medium Close-Up): Head and shoulders
- MS (Medium Shot): Waist up
- MLS (Medium Long Shot): Knees up
- LS (Long Shot): Full body
- ELS (Extreme Long Shot): Wide, establishing

Camera Angles:
- Eye Level: Neutral, natural
- High Angle: Looking down, diminishes subject
- Low Angle: Looking up, empowers subject
- Bird's Eye: Directly overhead
- Dutch Angle: Tilted, creates unease
- POV: Character's perspective

Camera Movements:
- Static: Fixed camera
- Pan: Horizontal rotation
- Tilt: Vertical rotation
- Dolly/Track: Camera moves on rails
- Handheld: Shaky, intimate, documentary feel
- Steadicam: Smooth moving shots
- Crane/Jib: Sweeping vertical movement

Composition:
- Rule of Thirds: Place subjects on intersection points
- Leading Lines: Guide eye through frame
- Depth: Foreground, midground, background
- Symmetry vs. Asymmetry
- Headroom and Look Space
- Balance and Visual Weight

Lighting Moods:
- High Key: Bright, minimal shadows (comedy, optimistic)
- Low Key: Dark, dramatic shadows (thriller, mystery)
- Natural: Realistic lighting
- Motivated: Lighting from visible source
- Practical: Actual lights in scene

For each shot, consider:
1. What information must be conveyed?
2. What emotion should viewer feel?
3. How does it connect to previous/next shot?
4. Is it visually interesting?"""

        return guide


class SceneDescriptionInput(BaseModel):
    """Input schema for SceneDescriptionTool"""
    action: str = Field(..., description="Action happening in scene")
    mood: str = Field(..., description="Mood/atmosphere")


class SceneDescriptionTool(BaseTool):
    name: str = "Scene Description Tool"
    description: str = """Helps write cinematic scene descriptions with strong visual
    imagery and proper screenplay format."""
    args_schema: Type[BaseModel] = SceneDescriptionInput

    def _run(self, action: str, mood: str) -> str:
        """Provide scene description writing guidelines"""

        guidelines = f"""Scene Description Guidelines:

Action: {action}
Mood: {mood}

Effective Scene Description:

1. Write in Present Tense:
   ✓ "She walks into the room."
   ✗ "She walked into the room."

2. Be Visual and Specific:
   ✓ "Rain hammers against the window. Lightning flashes."
   ✗ "It's raining outside."

3. Show, Don't Tell:
   ✓ "His hands tremble as he reaches for the phone."
   ✗ "He is nervous."

4. Use Active Voice:
   ✓ "The door slams shut."
   ✗ "The door is slammed shut."

5. Keep It Concise:
   - Short paragraphs (3-4 lines max)
   - Each paragraph = one action or beat
   - White space = easier to read

6. Cinematic Language:
   - Write what the camera sees/hears
   - Avoid internal thoughts (unless voiceover)
   - Focus on observable details

7. Sensory Details:
   - What we see (visual)
   - What we hear (audio)
   - Atmosphere and mood
   - Physical sensations when relevant

8. Rhythm and Pacing:
   - Short sentences = fast pace, tension
   - Longer sentences = slower, contemplative
   - Match description rhythm to scene energy

9. Character Introduction:
   - ALL CAPS first time
   - Age and brief striking description
   - Reveal character through action

10. Only Include What's Filmable:
    - No camera directions (that's director's job)
    - No editing notes
    - Focus on story and character

Current Mood: {mood}
- Choose words that reinforce this mood
- Sensory details that create atmosphere
- Pacing that matches emotional tone"""

        return guidelines
