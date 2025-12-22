# Social Media Manager - CrewAI Implementation

A multi-agent system for managing social media content creation, scheduling, and analytics using CrewAI.

## Overview

This CrewAI implementation provides a complete social media management solution with specialized agents for content strategy, copywriting, scheduling, and performance analytics across multiple platforms.

## Agents

1. **Content Strategist**: Develops content strategies and campaign plans
2. **Social Media Copywriter**: Creates engaging platform-specific copy
3. **Scheduling Manager**: Optimizes posting schedules and manages calendars
4. **Analytics Specialist**: Tracks performance and generates insights

## Features

- Multi-platform content strategy development
- Platform-specific copywriting (Instagram, Twitter, LinkedIn, Facebook)
- Optimal posting time recommendations
- Content calendar management
- Hashtag strategy development
- Performance tracking and analytics
- Monthly reporting with actionable insights

## Installation

1. Clone this repository or navigate to the project directory
2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up environment variables:
```bash
cp .env.example .env
# Edit .env with your API keys
```

## Usage

Run the social media manager:

```bash
python main.py
```

You'll be prompted to provide:
- Brand/company name
- Industry
- Target audience
- Campaign goals

The crew will then:
1. Develop content strategy
2. Create social media posts
3. Schedule content optimally
4. Track performance metrics
5. Generate monthly reports

## Project Structure

```
social-media-manager-agent472/
├── agents.py           # Agent definitions
├── tasks.py           # Task definitions
├── tools.py           # Custom tools
├── main.py            # Main execution script
├── requirements.txt   # Dependencies
├── .env.example       # Environment template
└── README_CREWAI.md   # This file
```

## Tools

### Content Creation Tools
- **Generate Post Ideas**: Brainstorms content concepts
- **Write Social Copy**: Creates platform-specific content
- **Create Hashtag Strategy**: Develops hashtag mixes
- **Optimize Post Timing**: Recommends best posting times

### Scheduling Tools
- **Create Posting Schedule**: Plans content distribution
- **Schedule Post**: Automates post publishing

### Analytics Tools
- **Track Engagement**: Monitors post performance
- **Analyze Audience**: Studies demographics and behavior
- **Generate Performance Report**: Creates comprehensive reports

## Use Cases

- **Brand Awareness**: Building consistent brand presence
- **Lead Generation**: Driving conversions through social
- **Community Building**: Engaging with followers
- **Product Launches**: Coordinating launch campaigns
- **Content Marketing**: Distributing valuable content
- **Influencer Marketing**: Managing influencer collaborations

## Platform-Specific Best Practices

### Instagram
- Use 8-15 relevant hashtags
- Post high-quality visuals
- Engage with stories and reels
- Best times: 11 AM, 1 PM, 7 PM

### Twitter
- Keep it concise (280 characters)
- Use 1-3 hashtags
- Engage in conversations
- Best times: 9 AM, 12 PM, 5 PM

### LinkedIn
- Professional tone
- Share industry insights
- Use 3-5 hashtags
- Best times: 7 AM, 12 PM, 5 PM

### Facebook
- Mix of content types
- Use engaging visuals
- 2-3 hashtags
- Best times: 1 PM, 3 PM

## Customization

### Adding New Platforms

Extend the tools in `tools.py` to support additional platforms:

```python
"NewPlatform": {
    "best_days": ["Monday", "Wednesday"],
    "best_times": ["10:00 AM", "2:00 PM"],
    "max_length": 500
}
```

### Custom Content Types

Add new post types in `ContentCreationTools.generate_post_ideas()`.

### Brand Voice

Customize the copywriting style in `ContentCreationTools.write_social_copy()`.

## Output

The crew generates:
- Content strategy documents
- Platform-specific social posts
- Optimized posting schedules
- Performance analytics reports
- Monthly insights and recommendations

## Metrics Tracked

- Engagement (likes, comments, shares, saves)
- Reach and impressions
- Engagement rate
- Follower growth
- Click-through rate
- Conversion rate
- Best performing content types

## Best Practices

1. **Consistency**: Post regularly at optimal times
2. **Authenticity**: Maintain genuine brand voice
3. **Engagement**: Respond to comments and messages
4. **Visual Quality**: Use high-quality images and videos
5. **Value**: Provide valuable content, not just promotion
6. **Analytics**: Track metrics and adjust strategy

## Requirements

- Python 3.10+
- OpenAI API key (or other LLM provider)
- Platform-specific API keys for automation (optional)

## License

MIT License
