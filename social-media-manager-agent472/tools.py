from crewai_tools import tool
import json
from typing import Dict, List, Any
from datetime import datetime, timedelta

class ContentCreationTools:
    @tool("Generate Post Ideas")
    def generate_post_ideas(topic: str) -> str:
        """
        Generates creative social media post ideas for a given topic.
        Useful for brainstorming content.
        """
        post_types = [
            "Educational tip or how-to",
            "Behind-the-scenes glimpse",
            "User-generated content feature",
            "Poll or question to drive engagement",
            "Industry news or trend commentary",
            "Inspirational quote or story",
            "Product showcase or demo",
            "Team member spotlight",
            "Customer testimonial",
            "Infographic or data visualization"
        ]

        ideas = {
            "topic": topic,
            "post_ideas": [
                {
                    "type": post_type,
                    "example": f"{post_type} related to {topic}",
                    "best_platform": ["Instagram", "LinkedIn"] if "Professional" in post_type else ["Instagram", "Twitter", "Facebook"]
                }
                for post_type in post_types[:5]
            ]
        }

        return json.dumps(ideas, indent=2)

    @tool("Write Social Copy")
    def write_social_copy(brief: str) -> str:
        """
        Writes engaging social media copy based on a brief.
        Useful for creating platform-specific content.
        """
        platforms = {
            "Instagram": {
                "max_length": 2200,
                "sample": "✨ [Attention-grabbing opening]\n\n[Main message with emojis]\n\n[Call to action]\n\n#Hashtag1 #Hashtag2 #Hashtag3"
            },
            "Twitter": {
                "max_length": 280,
                "sample": "[Compelling hook] [Main point] [CTA] #Hashtag"
            },
            "LinkedIn": {
                "max_length": 3000,
                "sample": "[Professional opening]\n\n[Value proposition]\n\n[Supporting details]\n\n[Question or CTA]"
            },
            "Facebook": {
                "max_length": 63206,
                "sample": "[Friendly opening]\n\n[Story or message]\n\n[Call to action]\n\nLink: [URL]"
            }
        }

        return json.dumps({
            "brief": brief,
            "platform_copy": platforms,
            "tips": [
                "Use active voice",
                "Include clear CTA",
                "Add relevant emojis",
                "Keep it conversational",
                "Front-load key information"
            ]
        }, indent=2)

    @tool("Create Hashtag Strategy")
    def create_hashtag_strategy(topic: str) -> str:
        """
        Creates a strategic hashtag mix for social media posts.
        Useful for improving discoverability.
        """
        hashtag_categories = {
            "branded": [f"#{topic.replace(' ', '')}Brand", f"#{topic.replace(' ', '')}Community"],
            "popular": [f"#{topic.replace(' ', '')}", "#trending", "#viral"],
            "niche": [f"#{topic.replace(' ', '')}Tips", f"#{topic.replace(' ', '')}Expert"],
            "location": ["#YourCity", "#Local"],
            "campaign": ["#CampaignName", "#SpecialOffer"]
        }

        return json.dumps({
            "topic": topic,
            "hashtag_strategy": hashtag_categories,
            "recommended_count": {
                "Instagram": "8-15 hashtags",
                "Twitter": "1-3 hashtags",
                "LinkedIn": "3-5 hashtags",
                "Facebook": "2-3 hashtags"
            },
            "tips": [
                "Mix popular and niche hashtags",
                "Research competitor hashtags",
                "Create branded hashtags",
                "Check hashtag popularity before using",
                "Avoid banned or spammy hashtags"
            ]
        }, indent=2)

    @tool("Optimize Post Timing")
    def optimize_post_timing(platform: str) -> str:
        """
        Provides optimal posting times for different platforms.
        Useful for maximizing reach and engagement.
        """
        timing_data = {
            "Instagram": {
                "best_days": ["Tuesday", "Wednesday", "Thursday"],
                "best_times": ["11:00 AM", "1:00 PM", "7:00 PM"],
                "avoid": ["Early morning (before 6 AM)", "Late night (after 10 PM)"]
            },
            "Twitter": {
                "best_days": ["Wednesday", "Friday"],
                "best_times": ["9:00 AM", "12:00 PM", "5:00 PM"],
                "avoid": ["Weekends after 3 PM"]
            },
            "LinkedIn": {
                "best_days": ["Tuesday", "Wednesday", "Thursday"],
                "best_times": ["7:00 AM", "12:00 PM", "5:00 PM"],
                "avoid": ["Weekends", "Early morning"]
            },
            "Facebook": {
                "best_days": ["Thursday", "Friday"],
                "best_times": ["1:00 PM", "3:00 PM"],
                "avoid": ["Saturday mornings"]
            }
        }

        platform_data = timing_data.get(platform, timing_data["Instagram"])

        return json.dumps({
            "platform": platform,
            "timing_recommendations": platform_data,
            "general_tips": [
                "Test different times with your audience",
                "Consider timezone differences",
                "Post consistently",
                "Monitor analytics to refine timing"
            ]
        }, indent=2)


class SchedulingTools:
    @tool("Create Posting Schedule")
    def create_posting_schedule(duration_days: int) -> str:
        """
        Creates a balanced posting schedule across platforms.
        Useful for planning content distribution.
        """
        schedule = []
        start_date = datetime.now()

        for day in range(duration_days):
            current_date = start_date + timedelta(days=day)
            day_schedule = {
                "date": current_date.strftime("%Y-%m-%d"),
                "day": current_date.strftime("%A"),
                "posts": []
            }

            # Sample posting pattern
            if current_date.weekday() < 5:  # Weekdays
                day_schedule["posts"] = [
                    {"time": "09:00", "platform": "LinkedIn", "type": "Professional content"},
                    {"time": "13:00", "platform": "Instagram", "type": "Visual content"},
                    {"time": "17:00", "platform": "Twitter", "type": "Quick update"}
                ]
            else:  # Weekends
                day_schedule["posts"] = [
                    {"time": "11:00", "platform": "Instagram", "type": "Lifestyle content"},
                    {"time": "15:00", "platform": "Facebook", "type": "Community engagement"}
                ]

            schedule.append(day_schedule)

        return json.dumps({
            "schedule": schedule[:7],  # First week
            "total_posts": sum(len(day["posts"]) for day in schedule),
            "posting_frequency": f"{duration_days} days"
        }, indent=2)

    @tool("Schedule Post")
    def schedule_post(post_details: str) -> str:
        """
        Schedules a social media post for publishing.
        Useful for automating content distribution.
        """
        scheduled = {
            "post_id": f"POST_{datetime.now().strftime('%Y%m%d%H%M%S')}",
            "status": "scheduled",
            "details": post_details,
            "scheduled_time": (datetime.now() + timedelta(hours=2)).strftime("%Y-%m-%d %H:%M:%S"),
            "platforms": ["Instagram", "Twitter", "LinkedIn"],
            "approval_required": False
        }

        return json.dumps(scheduled, indent=2)


class AnalyticsTools:
    @tool("Track Engagement")
    def track_engagement(post_id: str) -> str:
        """
        Tracks engagement metrics for a social media post.
        Useful for measuring content performance.
        """
        metrics = {
            "post_id": post_id,
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "engagement": {
                "likes": 342,
                "comments": 28,
                "shares": 56,
                "saves": 89,
                "total_engagement": 515
            },
            "reach": {
                "impressions": 12500,
                "reach": 8900,
                "reach_rate": "71.2%"
            },
            "engagement_rate": "5.79%",
            "best_performing_aspect": "Visual content",
            "peak_engagement_time": "2:00 PM - 4:00 PM"
        }

        return json.dumps(metrics, indent=2)

    @tool("Analyze Audience")
    def analyze_audience(platform: str) -> str:
        """
        Analyzes audience demographics and behavior.
        Useful for targeting content effectively.
        """
        audience_data = {
            "platform": platform,
            "total_followers": 15420,
            "demographics": {
                "age_groups": {
                    "18-24": "15%",
                    "25-34": "42%",
                    "35-44": "28%",
                    "45+": "15%"
                },
                "gender": {
                    "female": "58%",
                    "male": "40%",
                    "other": "2%"
                },
                "top_locations": [
                    {"city": "New York", "percentage": "18%"},
                    {"city": "Los Angeles", "percentage": "12%"},
                    {"city": "Chicago", "percentage": "8%"}
                ]
            },
            "behavior": {
                "most_active_days": ["Tuesday", "Wednesday", "Thursday"],
                "most_active_times": ["12:00 PM - 1:00 PM", "6:00 PM - 8:00 PM"],
                "avg_session_duration": "3m 24s"
            },
            "interests": ["Technology", "Lifestyle", "Business", "Travel"]
        }

        return json.dumps(audience_data, indent=2)

    @tool("Generate Performance Report")
    def generate_performance_report(time_period: str) -> str:
        """
        Generates a comprehensive performance report for social media accounts.
        Useful for understanding overall performance trends.
        """
        report = {
            "time_period": time_period,
            "summary": {
                "total_posts": 48,
                "total_engagement": 12540,
                "avg_engagement_rate": "4.8%",
                "follower_growth": "+342 (2.3%)",
                "reach": 145000,
                "impressions": 230000
            },
            "platform_breakdown": {
                "Instagram": {
                    "posts": 20,
                    "engagement_rate": "5.2%",
                    "best_post": "Product launch video"
                },
                "Twitter": {
                    "posts": 15,
                    "engagement_rate": "3.1%",
                    "best_post": "Industry news commentary"
                },
                "LinkedIn": {
                    "posts": 13,
                    "engagement_rate": "6.4%",
                    "best_post": "Thought leadership article"
                }
            },
            "top_performing_content": [
                {"type": "Video", "avg_engagement": "7.2%"},
                {"type": "Carousel", "avg_engagement": "6.1%"},
                {"type": "Image", "avg_engagement": "4.5%"}
            ],
            "recommendations": [
                "Increase video content frequency",
                "Post more during peak engagement times",
                "Experiment with carousel posts on Instagram",
                "Focus on educational content themes"
            ]
        }

        return json.dumps(report, indent=2)
