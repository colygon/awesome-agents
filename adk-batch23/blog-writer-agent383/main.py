#!/usr/bin/env python3
"""
Blog Writer CrewAI Agent
Converts Google ADK Blog Writer to CrewAI implementation
"""

import os
from crewai import Agent, Task, Crew, Process
from crewai_tools import SerperDevTool
from langchain_openai import ChatOpenAI
import datetime

# Initialize OpenAI LLM (replacing Gemini)
llm = ChatOpenAI(
    model="gpt-4o",
    temperature=0.7,
    api_key=os.getenv("OPENAI_API_KEY")
)

# Initialize search tool
search_tool = SerperDevTool()

# Define Agents (converted from ADK sub-agents)

# 1. Research & Planning Agent (from robust_blog_planner)
researcher = Agent(
    role="Technical Content Strategist",
    goal="Research topics and create comprehensive blog post outlines",
    backstory="""You are an expert technical content strategist who specializes in
    creating well-structured blog post outlines. You conduct thorough research and
    organize information in a clear, logical flow suitable for technical audiences.""",
    verbose=True,
    allow_delegation=False,
    tools=[search_tool],
    llm=llm
)

# 2. Writer Agent (from robust_blog_writer)
writer = Agent(
    role="Expert Technical Writer",
    goal="Write high-quality, in-depth technical blog posts",
    backstory="""You are an expert technical writer crafting articles for a
    sophisticated audience similar to 'Towards Data Science' and 'freeCodeCamp'.
    You dive deep into technical details, use code snippets extensively, and
    explain the 'how' and 'why' behind concepts.""",
    verbose=True,
    allow_delegation=False,
    tools=[search_tool],
    llm=llm
)

# 3. Editor Agent (from blog_editor)
editor = Agent(
    role="Professional Technical Editor",
    goal="Polish and refine blog posts to ensure clarity and quality",
    backstory="""You are a meticulous technical editor who reviews blog posts for
    clarity, accuracy, technical depth, and readability. You ensure the content
    meets professional standards and resonates with technical audiences.""",
    verbose=True,
    allow_delegation=False,
    llm=llm
)

def create_blog_post(topic: str, codebase_path: str = None) -> dict:
    """
    Create a complete blog post on the given topic

    Args:
        topic: The blog post topic
        codebase_path: Optional path to analyze codebase

    Returns:
        dict with outline, draft, final_post
    """

    # Analyze codebase if provided
    codebase_context = ""
    if codebase_path and os.path.exists(codebase_path):
        # Simple codebase analysis
        files = []
        for root, dirs, filenames in os.walk(codebase_path):
            for filename in filenames:
                if filename.endswith(('.py', '.js', '.ts', '.java', '.go')):
                    files.append(os.path.join(root, filename))
        codebase_context = f"\nCodebase contains {len(files)} code files in {codebase_path}"

    current_date = datetime.datetime.now().strftime("%Y-%m-%d")

    # Task 1: Research and Create Outline
    research_task = Task(
        description=f"""Research and create a comprehensive blog post outline for:
        Topic: {topic}
        {codebase_context}

        The outline should include:
        1. An engaging title
        2. Introduction with hook and thesis
        3. Main body with 3-5 detailed sections
        4. Code examples (if applicable)
        5. Conclusion with call to action

        Use Google Search to find relevant information and examples.
        Current date: {current_date}

        Output the outline in clear Markdown format.""",
        agent=researcher,
        expected_output="A well-structured blog post outline in Markdown format"
    )

    # Task 2: Write Blog Post
    writing_task = Task(
        description=f"""Based on the approved outline, write a high-quality technical blog post.

        Requirements:
        - Write for technical audience (similar to Towards Data Science)
        - Dive deep into technical details
        - Use code snippets to illustrate points
        - Include examples and real-world applications
        - Use Google Search for additional context and examples
        - Write in an engaging, authoritative tone
        {codebase_context}

        Output the complete blog post in Markdown format (no code blocks wrapping).""",
        agent=writer,
        expected_output="A complete, in-depth technical blog post in Markdown format",
        context=[research_task]
    )

    # Task 3: Edit and Polish
    editing_task = Task(
        description="""Review and polish the blog post to ensure:
        - Technical accuracy
        - Clear explanations
        - Proper structure and flow
        - Engaging introduction and conclusion
        - Correct grammar and style
        - Code snippets are properly formatted

        Make necessary revisions and output the final polished version.""",
        agent=editor,
        expected_output="A polished, publication-ready blog post in Markdown format",
        context=[writing_task]
    )

    # Create and run crew
    crew = Crew(
        agents=[researcher, writer, editor],
        tasks=[research_task, writing_task, editing_task],
        process=Process.sequential,
        verbose=True
    )

    result = crew.kickoff()

    return {
        "outline": research_task.output.raw if hasattr(research_task, 'output') else "",
        "draft": writing_task.output.raw if hasattr(writing_task, 'output') else "",
        "final_post": str(result),
        "metadata": {
            "topic": topic,
            "date": current_date,
            "codebase_analyzed": bool(codebase_context)
        }
    }

def save_blog_post(content: str, filename: str):
    """Save blog post to file"""
    if not filename.endswith('.md'):
        filename += '.md'

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"\nBlog post saved to: {filename}")

if __name__ == "__main__":
    print("Blog Writer CrewAI Agent")
    print("=" * 50)

    # Example usage
    topic = input("\nEnter blog post topic: ").strip()
    if not topic:
        topic = "Introduction to Large Language Models and Their Applications"

    codebase = input("Enter codebase path to analyze (optional, press Enter to skip): ").strip()
    codebase = codebase if codebase else None

    print(f"\nCreating blog post about: {topic}")
    if codebase:
        print(f"Analyzing codebase: {codebase}")

    # Create blog post
    result = create_blog_post(topic, codebase)

    # Display result
    print("\n" + "=" * 50)
    print("FINAL BLOG POST")
    print("=" * 50)
    print(result["final_post"])

    # Save option
    save = input("\n\nSave blog post to file? (y/n): ").strip().lower()
    if save == 'y':
        filename = input("Enter filename (without .md extension): ").strip()
        if filename:
            save_blog_post(result["final_post"], filename)
