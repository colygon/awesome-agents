from crewai_tools import tool

class LucillaGameStudioTools:
    @tool("Design Game Mechanics")
    def design_game_mechanics(self, game_type: str) -> str:
        """
        Designs core game mechanics and gameplay systems for the specified game type.

        Args:
            game_type: Type of game being designed

        Returns:
            Detailed game mechanics design
        """
        return f"""Game Mechanics Design for {game_type}:

        CORE MECHANICS:

        1. Primary Gameplay Loop:
           - Explore → Encounter → Combat/Puzzle → Reward → Progress
           - Session length: 15-30 minutes per loop
           - Variety: 8 different encounter types
           - Escalation: Difficulty increases with progression

        2. Combat System:
           - Turn-based tactical combat
           - Action points: 3 per turn
           - Skills: 20+ unique abilities
           - Combos: Chain actions for bonuses
           - Strategy: Rock-paper-scissors element relationships

        3. Resource Management:
           - Health, Mana, Stamina mechanics
           - Currency: Gold, Gems, Crafting materials
           - Inventory: 50 slots, upgradeable
           - Crafting: Combine materials for items

        4. Character Progression:
           - Level system: 1-50
           - Skill trees: 3 specializations, 15 skills each
           - Equipment: 6 slots, rarities from Common to Legendary
           - Stats: Strength, Agility, Intelligence, Vitality

        5. Exploration Mechanics:
           - Open world with 12 distinct regions
           - Hidden areas and secrets
           - Environmental puzzles
           - Fast travel unlock system

        BALANCING:
        - Early game: Tutorial, forgiving difficulty
        - Mid game: Challenge ramps up, strategic depth
        - End game: High difficulty, mastery required
        - Difficulty options: Easy, Normal, Hard, Expert
        """

    @tool("Create Narrative Structure")
    def create_narrative_structure(self, theme: str) -> str:
        """
        Creates narrative structure and story framework for the game.

        Args:
            theme: Game theme or story concept

        Returns:
            Narrative structure and story design
        """
        return f"""Narrative Structure for {theme}:

        STORY FRAMEWORK:

        Act 1 - Introduction (Hours 0-5):
        - Inciting incident: Ancient evil awakens
        - Character motivation: Personal loss drives hero
        - World establishment: Fantasy realm under threat
        - Tutorial integration: Learn mechanics through story
        - Key NPCs introduced: Mentor, rival, allies

        Act 2 - Rising Action (Hours 5-20):
        - Quest chain: Gather ancient artifacts
        - Character growth: Unlock new abilities
        - Plot twists: Betrayal by trusted ally
        - World expansion: Explore 8 regions
        - Side quests: 30+ optional missions

        Act 3 - Climax (Hours 20-25):
        - Final preparation: Ultimate weapon/power
        - Confrontation: Face the ancient evil
        - Resolution: Save or doom the world
        - Player choice: Multiple endings (3 main paths)

        NARRATIVE TECHNIQUES:
        - Environmental storytelling
        - Audio logs and documents
        - Dynamic NPC reactions
        - Player-driven narrative branches
        - Moral choice system (7 major decisions)

        CHARACTERS:
        - Protagonist: Customizable, voiced
        - Companions: 6 recruitable characters
        - Antagonist: Complex villain with motivations
        - NPCs: 50+ named characters with stories
        """

    @tool("Design Progression System")
    def design_progression_system(self, game_length: str) -> str:
        """
        Designs player progression and reward systems.

        Args:
            game_length: Expected game length/playtime

        Returns:
            Progression system design
        """
        return f"""Progression System Design ({game_length}):

        LEVELING SYSTEM:
        - Max Level: 50
        - XP Curve: Exponential, balanced for playtime
        - XP Sources: Combat (60%), Quests (30%), Exploration (10%)
        - Level rewards: Skill points, stat increases, new abilities

        SKILL PROGRESSION:
        - Skill Points: 2 per level (100 total)
        - Skill Trees: Warrior, Mage, Rogue
        - Active Skills: 15 per tree
        - Passive Skills: 10 per tree
        - Ultimate Skills: 1 per tree (unlocked at level 30)

        EQUIPMENT PROGRESSION:
        - Tiers: 10 equipment tiers
        - Rarities: Common, Uncommon, Rare, Epic, Legendary
        - Set Bonuses: 8 complete sets
        - Enchanting: Upgrade system
        - Transmog: Appearance customization

        ACHIEVEMENT SYSTEM:
        - Total Achievements: 100
        - Categories: Combat, Exploration, Collection, Story
        - Rewards: Cosmetics, titles, special items
        - Hidden Achievements: 20 secret discoveries

        ENDGAME PROGRESSION:
        - Prestige System: Reset for bonuses
        - Legendary Quests: Post-game content
        - Challenge Modes: Harder difficulties
        - Seasonal Content: Time-limited events
        """

    @tool("Generate Level Layouts")
    def generate_level_layouts(self, level_type: str) -> str:
        """
        Generates procedural level layouts using algorithms.

        Args:
            level_type: Type of level to generate

        Returns:
            Level generation specifications
        """
        return f"""Level Generation System for {level_type}:

        GENERATION ALGORITHM:
        - Method: BSP (Binary Space Partitioning) + Wave Function Collapse
        - Grid Size: 100x100 tiles
        - Room Count: 8-15 rooms per level
        - Connectivity: All rooms accessible, multiple paths
        - Seed-based: Reproducible levels

        ROOM TYPES:
        - Entrance (1): Starting point
        - Combat (40%): Enemy encounters
        - Puzzle (20%): Logic challenges
        - Treasure (15%): Loot rooms
        - Story (10%): Narrative moments
        - Boss (10%): Major encounters
        - Exit (5%): Level completion

        LAYOUT FEATURES:
        - Corridors: Variable width, branching paths
        - Secrets: 2-5 hidden areas per level
        - Shortcuts: Unlockable passages
        - Environmental hazards: Traps, obstacles
        - Interactive elements: Levers, doors, gates

        BIOME VARIATION:
        - Forest: Dense vegetation, natural obstacles
        - Dungeon: Stone walls, narrow passages
        - Cave: Irregular shapes, vertical elements
        - Castle: Symmetrical rooms, grand halls
        - Ruins: Broken structures, gaps

        DIFFICULTY SCALING:
        - Early levels: Simple, linear layouts
        - Mid levels: Complex, multiple paths
        - Late levels: Maze-like, challenging navigation
        - Density: Increase encounters with depth

        SAMPLE OUTPUT:
        Level seed: 12345
        Rooms: 12 (4 combat, 3 puzzle, 2 treasure, 2 story, 1 boss)
        Size: 87x94 tiles
        Secrets: 3 hidden rooms
        Estimated completion: 25 minutes
        """

    @tool("Create Quests")
    def create_quests(self, quest_theme: str) -> str:
        """
        Generates quests and missions procedurally.

        Args:
            quest_theme: Theme or context for quests

        Returns:
            Quest generation system and examples
        """
        return f"""Quest Generation System - {quest_theme}:

        QUEST STRUCTURE TEMPLATES:

        1. Fetch Quest:
           - Objective: Retrieve [item] from [location]
           - Obstacles: [enemy type] guards
           - Reward: [gold + item]
           - Variations: 15 templates

        2. Elimination Quest:
           - Objective: Defeat [number] [enemy type]
           - Location: [region/dungeon]
           - Bonus: Time limit or combo challenges
           - Variations: 12 templates

        3. Escort Quest:
           - Objective: Protect [NPC] to [destination]
           - Threats: [enemy ambushes]
           - Failure: NPC death
           - Variations: 8 templates

        4. Investigation Quest:
           - Objective: Gather [clues/items]
           - Method: Exploration and dialogue
           - Revelation: Story unlock
           - Variations: 10 templates

        5. Boss Hunt:
           - Objective: Track and defeat [boss name]
           - Preparation: Gather intel, upgrade gear
           - Reward: Legendary loot
           - Variations: 6 templates

        QUEST GENERATION PARAMETERS:
        - Difficulty: Scales with player level
        - Location: Based on player progression
        - Rewards: Balanced for time investment
        - Narrative: Connects to main story or world lore
        - Variety: No duplicate quests in sequence

        SAMPLE GENERATED QUEST:
        Title: "The Lost Artifact of Eldoria"
        Type: Investigation + Fetch
        Objective: Find 3 clues about artifact location, retrieve artifact
        Location: Ancient Library → Forgotten Tomb
        Enemies: Skeleton Guards (Level 15)
        Puzzles: Decode ancient text
        Reward: 500 gold, Rare staff, 1000 XP
        Estimated time: 35 minutes
        Narrative hook: Ties to main story Act 2
        """

    @tool("Generate Dialogue")
    def generate_dialogue(self, context: str) -> str:
        """
        Generates dynamic dialogue for NPCs and story moments.

        Args:
            context: Dialogue context or scenario

        Returns:
            Dialogue generation system and samples
        """
        return f"""Dialogue Generation System - {context}:

        DIALOGUE SYSTEM ARCHITECTURE:

        1. Context-Aware Generation:
           - Player state: Level, alignment, progress
           - NPC state: Relationship, mood, knowledge
           - World state: Story events, faction standings
           - History: Previous conversations remembered

        2. Dialogue Templates:
           - Greetings: 20 variations by relationship
           - Information: Quest hints, lore, rumors
           - Reactions: To player choices/actions
           - Emotional: Joy, anger, fear, surprise
           - Farewells: Context-dependent

        3. Branching Options:
           - Player choices: 2-5 options per dialogue node
           - Skill checks: Persuasion, intimidation, deception
           - Alignment impact: Good, neutral, evil choices
           - Relationship changes: +/- reputation

        SAMPLE DIALOGUE TREE:

        NPC: "You there! I need your help urgently."

        Player Options:
        [1] "What's the problem?" (Helpful)
        [2] "I'm listening..." (Neutral)
        [3] "Make it worth my while." (Greedy)
        [4] [Intimidation] "Watch your tone." (Aggressive)

        Branch 1 (Helpful):
        NPC: "Bandits took my family heirloom! Please recover it."
        → Quest offered: "The Stolen Heirloom"
        → Relationship: +10

        Branch 2 (Neutral):
        NPC: "Bandits raided my home. I'll pay for its recovery."
        → Quest offered with standard reward

        Branch 3 (Greedy):
        NPC: "I'll double the usual reward if you succeed."
        → Quest offered: +50% reward, Relationship: -5

        Branch 4 (Aggressive - requires Intimidation 5):
        NPC: "F-forgive me! I'll add my savings to the reward!"
        → Quest offered: +80% reward, Relationship: -15, Alignment: -10

        DYNAMIC ELEMENTS:
        - Voice: Personality traits affect word choice
        - Memory: NPCs remember past interactions
        - Rumors: Share procedurally generated gossip
        - Emergent: React to player reputation/actions
        - Localization: Support for multiple languages
        """

    @tool("Design NPC Behaviors")
    def design_npc_behaviors(self, npc_role: str) -> str:
        """
        Designs AI behavior patterns for NPCs.

        Args:
            npc_role: Role or type of NPC

        Returns:
            NPC behavior system design
        """
        return f"""NPC Behavior Design - {npc_role}:

        BEHAVIOR TREE ARCHITECTURE:

        Root: NPC State Machine
        ├─ Idle Behaviors
        │  ├─ Wander (60%)
        │  ├─ Socialize (25%)
        │  └─ Work/Activity (15%)
        ├─ Alert Behaviors
        │  ├─ Investigate sound
        │  ├─ Search area
        │  └─ Call for help
        └─ Combat Behaviors
           ├─ Assess threat
           ├─ Choose tactics
           ├─ Execute combat
           └─ Retreat if overwhelmed

        IDLE BEHAVIORS:

        Wandering:
        - Random walk within territory
        - Pause at points of interest
        - Return to home/post after time
        - Avoid hazards and obstacles

        Socializing:
        - Approach other NPCs
        - Context-appropriate animations
        - Dialogue snippets
        - Group behaviors

        Activities:
        - Role-specific: Blacksmith hammers, merchant sells
        - Day/night cycle awareness
        - Schedules: Work, eat, sleep
        - Reactivity: Stop for major events

        COMBAT BEHAVIORS:

        Warrior:
        - Aggressive: Close distance
        - Tactics: Flank, shield bash, power attacks
        - Group: Protect allies, coordinate
        - Retreat: <30% health

        Archer:
        - Defensive: Maintain distance
        - Tactics: Kite, aimed shots, traps
        - Positioning: High ground preference
        - Retreat: When cornered

        Mage:
        - Tactical: Medium range
        - Tactics: AOE spells, buffs, debuffs
        - Resource: Manage mana efficiently
        - Retreat: <40% mana or health

        ADVANCED AI:
        - Learning: Adapt to player tactics
        - Memory: Remember previous encounters
        - Coordination: Team-based strategies
        - Morale: Flee if allies defeated
        - Personality: Affects risk-taking

        REACTIVITY:
        - Player reputation: Friendly/hostile
        - Faction standing: Allied/enemy
        - World events: React to story changes
        - Time: Different behaviors day/night
        """

    @tool("Create NPC Personalities")
    def create_npc_personalities(self, character_count: str) -> str:
        """
        Generates NPC personality systems and character traits.

        Args:
            character_count: Number of NPCs to characterize

        Returns:
            NPC personality system
        """
        return f"""NPC Personality System ({character_count} characters):

        PERSONALITY TRAIT SYSTEM:

        Big Five Traits (0-10 scale):
        - Openness: Creativity, curiosity
        - Conscientiousness: Organization, reliability
        - Extraversion: Social, energetic
        - Agreeableness: Friendly, cooperative
        - Neuroticism: Emotional stability

        ARCHETYPES:
        1. The Mentor: Wise, patient, guiding
        2. The Rival: Competitive, skilled, challenging
        3. The Comic Relief: Humorous, lighthearted
        4. The Tragic Hero: Noble but flawed
        5. The Trickster: Deceptive, unpredictable
        6. The Guardian: Protective, loyal
        7. The Scholar: Intellectual, curious
        8. The Warrior: Brave, aggressive

        SAMPLE NPC PROFILES:

        Eldric the Wise (Mentor):
        - Traits: Openness 9, Conscientious 8, Extravert 4
        - Personality: Patient, knowledgeable, cryptic
        - Speech pattern: Formal, uses metaphors
        - Motivation: Guide hero to destiny
        - Quirk: Speaks in riddles when stressed
        - Relationship: Starts at +50 (trusted advisor)

        Raven Shadowstrike (Rival):
        - Traits: Openness 6, Conscientious 7, Extravert 8
        - Personality: Confident, competitive, honorable
        - Speech pattern: Direct, challenging
        - Motivation: Prove superiority to player
        - Quirk: Always arrives dramatically
        - Relationship: Starts at 0 (neutral competition)

        Pip Merryfoot (Comic Relief):
        - Traits: Openness 8, Conscientious 3, Extravert 10
        - Personality: Optimistic, clumsy, loyal
        - Speech pattern: Jokes, malapropisms
        - Motivation: Adventure and friendship
        - Quirk: Accidentally causes chaos
        - Relationship: Starts at +30 (friendly)

        DYNAMIC PERSONALITY:
        - Growth: Characters evolve through story
        - Reactions: Traits affect responses
        - Relationships: Change based on player actions
        - Consistency: Maintain core personality
        - Surprises: Occasional out-of-character moments
        """

    @tool("Implement Dynamic Dialogue")
    def implement_dynamic_dialogue(self, scenario: str) -> str:
        """
        Implements dynamic, context-aware dialogue systems.

        Args:
            scenario: Dialogue scenario or situation

        Returns:
            Dynamic dialogue implementation
        """
        return f"""Dynamic Dialogue System - {scenario}:

        CONTEXT VARIABLES:

        Player State:
        - Level: 1-50
        - Alignment: -100 (evil) to +100 (good)
        - Reputation: Per faction/NPC
        - Inventory: Quest items affect dialogue
        - Appearance: Equipped gear recognized

        World State:
        - Story progress: Act 1/2/3
        - Faction standings: Allied/neutral/hostile
        - Completed quests: NPCs acknowledge
        - World events: Major story beats
        - Time: Day/night, seasons

        Relationship State:
        - Affection: -100 to +100
        - Trust: 0-100
        - Fear: 0-100
        - Respect: 0-100
        - History: Conversation memory

        ADAPTIVE DIALOGUE:

        Greeting Example:
        If relationship > 50:
          "My friend! It's wonderful to see you again!"
        If relationship 0-50:
          "Hello there. How can I help you?"
        If relationship < 0:
          "You... What do you want?"
        If player helped NPC before:
          "I still remember your kindness. Welcome!"

        Quest Context:
        If player has quest item:
          "Is that... the ancient amulet? You found it!"
        If quest time-sensitive:
          "Hurry! We're running out of time!"
        If quest failed:
          "I'm... disappointed. I expected better."

        Reputation Impact:
        If player is hero:
          "The legendary [player name]! An honor!"
        If player is villain:
          "[Nervously] I want no trouble..."
        If player is mysterious:
          "I've heard whispers about you..."

        PROCEDURAL GENERATION:

        Template System:
        - Base: "I need [item] from [location]"
        - Variations: 15 different phrasings
        - Personality: Adjusted for NPC traits
        - Emotion: Current mood affects tone

        Rumor Generation:
        - Sources: Nearby quests, events, lore
        - Accuracy: NPCs may be misinformed
        - Personality: How they share info
        - Value: Some rumors lead to secrets

        IMPLEMENTATION:
        - Engine: Dialogue graph with conditions
        - Variables: 50+ tracked per conversation
        - Memory: Last 20 player choices saved
        - Branching: Up to 10 options per node
        - Voice: Text-to-speech with emotion
        """

    @tool("Analyze Player Engagement")
    def analyze_player_engagement(self, game_data: str) -> str:
        """
        Analyzes and predicts player engagement metrics.

        Args:
            game_data: Game design data for analysis

        Returns:
            Player engagement analysis
        """
        return f"""Player Engagement Analysis:

        ENGAGEMENT METRICS:

        Core Loop Strength: 8.5/10
        - Addictive: Clear goals → action → reward
        - Variety: 8 different gameplay modes
        - Pacing: Good balance of action and rest
        - Feedback: Clear progress indicators

        Retention Projections:
        - Day 1: 85% (strong tutorial)
        - Day 7: 58% (typical for genre)
        - Day 30: 32% (above average)
        - Day 90: 18% (core audience)

        Session Length:
        - Average: 45 minutes
        - Hardcore: 2+ hours
        - Casual: 15-20 minutes
        - Save points: Every 5-10 minutes

        ENGAGEMENT DRIVERS:

        Progression (High):
        - Constant unlocks and upgrades
        - Clear advancement path
        - Sense of becoming powerful
        - Risk: May feel grindy at mid-game

        Story (Medium-High):
        - Compelling narrative hooks
        - Player choices matter
        - Mystery and revelations
        - Risk: Side content may distract

        Social (Medium):
        - No multiplayer currently
        - Leaderboards for challenges
        - Share achievements
        - Opportunity: Add co-op mode

        Collection (High):
        - 100+ unique items
        - Achievement hunting
        - Completionist appeal
        - Risk: Overwhelming for some

        Mastery (High):
        - Skill-based combat
        - Strategic depth
        - Challenge modes
        - Risk: May alienate casual players

        PAIN POINTS:

        Identified Issues:
        - Tutorial too long (30 min → reduce to 15)
        - Difficulty spike at level 15
        - Inventory management tedious
        - Fast travel unlocks too late

        Recommendations:
        - Streamline tutorial, add skip option
        - Smooth difficulty curve at mid-game
        - Auto-sort inventory feature
        - Unlock fast travel earlier (level 10 → 5)

        MONETIZATION POTENTIAL:
        - Cosmetic DLC: High appeal
        - Expansion packs: Strong story hooks
        - Season pass: Ongoing content
        - Free-to-play: Not recommended (narrative focus)
        """

    @tool("Balance Game Difficulty")
    def balance_game_difficulty(self, difficulty_curve: str) -> str:
        """
        Analyzes and balances game difficulty progression.

        Args:
            difficulty_curve: Current difficulty curve data

        Returns:
            Difficulty balancing recommendations
        """
        return f"""Difficulty Balancing Analysis:

        CURRENT DIFFICULTY CURVE:

        Early Game (Levels 1-10):
        - Challenge: Low (intentional)
        - Deaths: <2 per hour
        - Learning curve: Gentle
        - Status: ✓ Well balanced

        Mid Game (Levels 11-30):
        - Challenge: Medium
        - Deaths: 3-5 per hour
        - Spike at level 15: ⚠ Too steep
        - Status: Needs adjustment

        Late Game (Levels 31-50):
        - Challenge: High
        - Deaths: 5-8 per hour
        - Mastery required: Yes
        - Status: ✓ Appropriate

        DIFFICULTY MODES:

        Easy:
        - Player damage: +50%
        - Enemy damage: -30%
        - Resources: +100%
        - Target: Casual players, story focus

        Normal (Recommended):
        - Baseline values
        - Balanced challenge
        - Fair but requires skill
        - Target: General audience

        Hard:
        - Player damage: -20%
        - Enemy damage: +40%
        - Resources: -30%
        - Target: Experienced players

        Expert:
        - Player damage: -40%
        - Enemy damage: +80%
        - Resources: -50%
        - Permadeath option
        - Target: Hardcore fans

        BALANCING ADJUSTMENTS:

        Combat:
        - Enemy HP: Scale with player level
        - Enemy damage: Increase gradually
        - Boss HP: 3-5× regular enemies
        - Boss mechanics: Unique per boss

        Resources:
        - Healing items: Ensure availability
        - Mana potions: Balanced for mage builds
        - Currency: Enough for progression
        - Crafting: Materials not too rare

        Puzzles:
        - Hint system: Optional hints
        - Difficulty range: Easy to expert
        - Skip option: After 3 failures
        - Balance: 30% easy, 50% medium, 20% hard

        ADAPTIVE DIFFICULTY:

        Dynamic Adjustment:
        - Track player deaths
        - Adjust enemy stats slightly
        - Offer difficulty change after deaths
        - Transparency: Inform player of changes

        Rubber-banding:
        - Prevent frustration spirals
        - Reward streaks with challenge
        - Balance risk and reward
        - Player agency: Can disable

        RECOMMENDATIONS:
        - Reduce level 15 enemy damage by 15%
        - Add checkpoint before difficulty spike
        - Improve player power curve 10-20
        - Add more healing items mid-game
        """

    @tool("Generate Game Documentation")
    def generate_game_documentation(self, game_title: str) -> str:
        """
        Generates comprehensive game design documentation.

        Args:
            game_title: Title of the game

        Returns:
            Complete game documentation
        """
        return f"""GAME DESIGN DOCUMENT: {game_title}

        EXECUTIVE SUMMARY:
        {game_title} is an AI-generated action RPG featuring procedural content,
        dynamic NPCs, and adaptive storytelling. Players explore a fantasy world,
        complete quests, battle enemies, and shape the narrative through choices.

        TARGET AUDIENCE:
        - Primary: Ages 18-35, RPG enthusiasts
        - Secondary: Casual gamers seeking narrative experiences
        - Platform: PC, Console (next-gen)
        - ESRB: T for Teen (fantasy violence)

        CORE PILLARS:
        1. Infinite Replayability: Procedural generation ensures unique playthroughs
        2. Living World: AI-driven NPCs with personalities and memories
        3. Player Agency: Choices impact story, world, and relationships
        4. Strategic Combat: Skill-based, tactical encounters

        GAME OVERVIEW:
        - Genre: Action RPG
        - Perspective: Third-person
        - Play time: 25-30 hours (main story), 50+ hours (100% completion)
        - Setting: High fantasy with dark undertones
        - Art style: Stylized realism

        TECHNICAL SPECIFICATIONS:
        - Engine: Unreal Engine 5
        - Min specs: RTX 2060, 16GB RAM, SSD
        - Resolution: Up to 4K
        - Frame rate: 60 FPS target
        - Storage: 50GB

        DEVELOPMENT ROADMAP:

        Pre-production (3 months):
        - Finalize design documents
        - Prototype core mechanics
        - Art style establishment
        - Technical pipeline setup

        Production (18 months):
        - Months 1-6: Core systems implementation
        - Months 7-12: Content creation
        - Months 13-18: Polish and optimization

        Post-production (3 months):
        - Beta testing
        - Bug fixing
        - Performance optimization
        - Marketing preparation

        MONETIZATION:
        - Base game: $49.99
        - DLC expansions: $19.99 each (2 planned)
        - Cosmetic packs: $4.99-$9.99
        - Season pass: $39.99 (includes all DLC)

        COMPETITIVE ANALYSIS:
        vs. Skyrim: More focused narrative, better AI
        vs. Divinity: Faster combat, procedural content
        vs. Witcher 3: More player choice, emergent stories
        Unique selling point: Fully AI-driven content and NPCs

        RISK ASSESSMENT:
        - Technical: Procedural generation complexity (High)
        - Market: Saturated RPG market (Medium)
        - Creative: AI-generated content quality (Medium)
        - Budget: Scope creep potential (Medium)

        SUCCESS METRICS:
        - Sales: 500K units year one
        - Reviews: 80+ Metacritic
        - Retention: 30% at day 30
        - Community: Active modding scene
        """
