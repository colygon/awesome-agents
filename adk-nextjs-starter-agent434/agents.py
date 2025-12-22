"""
ADK Next.js Starter - CrewAI Agent Definitions
Multi-Agent Next.js Application Development System

This module defines three specialized agents:
1. Architecture Planner - Plans application architecture
2. Full-Stack Developer - Implements frontend and backend
3. Performance Optimizer - Optimizes performance and SEO
"""

from crewai import Agent
from textwrap import dedent


def create_architecture_planner() -> Agent:
    return Agent(
        role="Architecture Planner",
        goal="Design scalable Next.js application architecture",
        backstory=dedent("""
            You are a senior software architect with 15+ years of experience designing
            web applications, particularly with React and Next.js. You understand the
            Next.js App Router, Server Components, data fetching patterns, authentication
            strategies, and deployment best practices.

            Your expertise includes project structure, state management, API design,
            database schema planning, authentication flows, and CI/CD setup.
        """),
        verbose=True,
        allow_delegation=False,
        memory=True
    )


def create_fullstack_developer() -> Agent:
    return Agent(
        role="Full-Stack Developer",
        goal="Implement robust Next.js applications with modern best practices",
        backstory=dedent("""
            You are an expert Next.js developer with deep knowledge of React, TypeScript,
            Server Components, Server Actions, tRPC, Prisma, and modern web development.
            You write clean, type-safe code following Next.js conventions and best practices.

            Your skills include component architecture, API routes, database integration,
            authentication implementation, form handling, and testing.
        """),
        verbose=True,
        allow_delegation=False,
        memory=True
    )


def create_performance_optimizer() -> Agent:
    return Agent(
        role="Performance Optimizer",
        goal="Optimize Next.js applications for performance, SEO, and user experience",
        backstory=dedent("""
            You are a performance optimization specialist focused on Next.js applications.
            You understand Core Web Vitals, image optimization, code splitting, caching
            strategies, SEO best practices, and accessibility standards.

            Your expertise includes bundle analysis, performance profiling, SEO optimization,
            progressive enhancement, and Core Web Vitals improvement.
        """),
        verbose=True,
        allow_delegation=False,
        memory=True
    )
