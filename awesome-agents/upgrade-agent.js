#!/usr/bin/env node

import fs from 'node:fs/promises';
import path from 'node:path';
import { spawn } from 'child_process';
import sqlite3 from 'sqlite3';

// Parse command line arguments
function parseArgs(argv) {
  const args = {};
  for (let i = 2; i < argv.length; i += 2) {
    const key = argv[i].replace('--', '');
    const value = argv[i + 1];
    args[key] = value;
  }
  return args;
}

const args = parseArgs(process.argv);
const { appId, githubUrl, title, category } = args;

console.log(`[Upgrade Agent] Starting upgrade for app ${appId}: ${title}`);
console.log(`[Upgrade Agent] GitHub URL: ${githubUrl}`);
console.log(`[Upgrade Agent] Category: ${category}`);

// Extract owner/repo from GitHub URL
function parseGithubUrl(url) {
  const match = url.match(/github\.com\/([^\/]+)\/([^\/]+)/);
  if (!match) return null;
  return { owner: match[1], repo: match[2].replace('.git', '') };
}

const repoInfo = parseGithubUrl(githubUrl);
if (!repoInfo) {
  console.error('[Upgrade Agent] Invalid GitHub URL');
  process.exit(1);
}

// Create directory name
const dirName = `${repoInfo.repo}-agent${appId}`;
const targetDir = path.join('/Users/colinlowenberg/crew', dirName);

console.log(`[Upgrade Agent] Target directory: ${targetDir}`);

async function createCrewAIImplementation() {
  try {
    // Check if directory already exists
    try {
      await fs.access(targetDir);
      console.log(`[Upgrade Agent] Directory ${dirName} already exists. Checking for agents.py...`);

      try {
        await fs.access(path.join(targetDir, 'agents.py'));
        console.log(`[Upgrade Agent] agents.py already exists. Skipping upgrade.`);
        return;
      } catch {
        console.log(`[Upgrade Agent] No agents.py found. Proceeding with upgrade...`);
      }
    } catch {
      // Directory doesn't exist, create it
      await fs.mkdir(targetDir, { recursive: true });
      console.log(`[Upgrade Agent] Created directory: ${targetDir}`);
    }

    // Clone the repository to inspect it
    console.log(`[Upgrade Agent] Cloning repository...`);
    const cloneProcess = spawn('git', ['clone', '--depth', '1', githubUrl, targetDir], {
      stdio: 'inherit'
    });

    await new Promise((resolve, reject) => {
      cloneProcess.on('close', (code) => {
        if (code === 0) resolve();
        else reject(new Error(`git clone failed with code ${code}`));
      });
    });

    // Create CrewAI implementation files
    console.log(`[Upgrade Agent] Creating CrewAI implementation files...`);

    // agents.py
    const agentsContent = `from crewai import Agent
from tools import create_tools

def create_agents():
    """
    Create CrewAI agents for ${title}

    This is an upgraded version of the original ${category} app.
    """

    researcher = Agent(
        role='Research Analyst',
        goal='Analyze and research information from the original app',
        backstory='''You are an expert research analyst who can understand and
        extract insights from various data sources and applications.''',
        tools=create_tools(),
        verbose=True,
        allow_delegation=True
    )

    developer = Agent(
        role='Developer',
        goal='Implement and enhance functionality from the original app',
        backstory='''You are a skilled developer who can take existing applications
        and improve them with modern multi-agent architectures.''',
        tools=create_tools(),
        verbose=True,
        allow_delegation=False
    )

    coordinator = Agent(
        role='Workflow Coordinator',
        goal='Coordinate tasks and ensure smooth operation of the multi-agent system',
        backstory='''You are an experienced project coordinator who excels at
        managing complex workflows and ensuring all agents work together efficiently.''',
        verbose=True,
        allow_delegation=True
    )

    return [researcher, developer, coordinator]
`;

    await fs.writeFile(path.join(targetDir, 'agents.py'), agentsContent);

    // tasks.py
    const tasksContent = `from crewai import Task

def create_tasks(agents):
    """
    Create CrewAI tasks for ${title}

    This defines the workflow for the upgraded multi-agent system.
    """

    researcher, developer, coordinator = agents

    research_task = Task(
        description='''Analyze the original ${category} application and identify
        its core functionality, key features, and potential improvements.''',
        expected_output='A comprehensive analysis report of the original application',
        agent=researcher
    )

    development_task = Task(
        description='''Based on the research analysis, implement the core functionality
        using CrewAI's multi-agent architecture. Enhance the original features and
        add new capabilities where appropriate.''',
        expected_output='Working implementation with CrewAI agents',
        agent=developer,
        context=[research_task]
    )

    coordination_task = Task(
        description='''Coordinate the research and development phases, ensure proper
        integration of all components, and validate the final implementation.''',
        expected_output='Final validated multi-agent system ready for deployment',
        agent=coordinator,
        context=[research_task, development_task]
    )

    return [research_task, development_task, coordination_task]
`;

    await fs.writeFile(path.join(targetDir, 'tasks.py'), tasksContent);

    // tools.py
    const toolsContent = `from crewai_tools import (
    FileReadTool,
    DirectoryReadTool,
    SerperDevTool,
    WebsiteSearchTool
)
import os

def create_tools():
    """
    Create tools for ${title} agents

    Configure and return the tools needed for the multi-agent system.
    """

    tools = []

    # Add file and directory tools
    tools.append(FileReadTool())
    tools.append(DirectoryReadTool())

    # Add search tool if API key is available
    if os.getenv('SERPER_API_KEY'):
        tools.append(SerperDevTool())

    # Add web search tool
    tools.append(WebsiteSearchTool())

    return tools
`;

    await fs.writeFile(path.join(targetDir, 'tools.py'), toolsContent);

    // main.py
    const mainContent = `#!/usr/bin/env python3
"""
${title} - CrewAI Upgraded Version

This is a multi-agent implementation upgraded from the original ${category} app.
Repository: ${githubUrl}
"""

import os
from dotenv import load_dotenv
from crewai import Crew, Process
from agents import create_agents
from tasks import create_tasks

# Load environment variables
load_dotenv()

def main():
    """
    Main entry point for ${title}
    """

    print("\\n" + "="*50)
    print("${title}")
    print("CrewAI Multi-Agent System")
    print("="*50 + "\\n")

    # Create agents
    print("Creating agents...")
    agents = create_agents()

    # Create tasks
    print("Creating tasks...")
    tasks = create_tasks(agents)

    # Create crew
    print("Assembling crew...")
    crew = Crew(
        agents=agents,
        tasks=tasks,
        process=Process.sequential,
        verbose=True
    )

    # Run the crew
    print("\\nStarting workflow...\\n")
    result = crew.kickoff()

    print("\\n" + "="*50)
    print("WORKFLOW COMPLETE")
    print("="*50)
    print(f"\\n{result}\\n")

    return result

if __name__ == "__main__":
    main()
`;

    await fs.writeFile(path.join(targetDir, 'main.py'), mainContent);

    // requirements.txt
    const requirementsContent = `crewai>=0.28.0
crewai-tools>=0.2.0
python-dotenv>=1.0.0
`;

    await fs.writeFile(path.join(targetDir, 'requirements.txt'), requirementsContent);

    // .env.example
    const envContent = `# ${title} Environment Variables

# OpenAI API Key (required)
OPENAI_API_KEY=your_openai_api_key_here

# Serper API Key (optional - for web search)
SERPER_API_KEY=your_serper_api_key_here

# Original repository: ${githubUrl}
`;

    await fs.writeFile(path.join(targetDir, '.env.example'), envContent);

    // README_CREWAI.md
    const readmeContent = `# ${title} - CrewAI Edition

**Original Repository:** ${githubUrl}
**Category:** ${category}
**Upgraded:** ${new Date().toISOString().split('T')[0]}

## Overview

This is a CrewAI-powered upgrade of the original ${title} application. The upgrade transforms the original ${category} app into a multi-agent system using CrewAI's orchestration capabilities.

## Architecture

### Agents

1. **Research Analyst**
   - Analyzes and researches information from the original app
   - Tools: File reading, directory scanning, web search
   - Can delegate tasks to other agents

2. **Developer**
   - Implements and enhances functionality
   - Tools: File operations, web search
   - Focused execution without delegation

3. **Workflow Coordinator**
   - Coordinates tasks across agents
   - Ensures smooth operation and integration
   - Can delegate to optimize workflow

### Tasks

1. **Research Phase**: Analyze original application functionality
2. **Development Phase**: Implement with CrewAI architecture
3. **Coordination Phase**: Validate and finalize implementation

## Installation

\`\`\`bash
# Clone this repository
cd ${dirName}

# Install dependencies
pip install -r requirements.txt

# Set up environment
cp .env.example .env
# Edit .env and add your API keys
\`\`\`

## Configuration

Required environment variables:

- \`OPENAI_API_KEY\`: Your OpenAI API key (required)
- \`SERPER_API_KEY\`: Your Serper API key for web search (optional)

## Usage

\`\`\`bash
python main.py
\`\`\`

The system will:
1. Initialize all agents
2. Create and assign tasks
3. Execute the workflow sequentially
4. Return the final result

## Files

- \`agents.py\`: Agent definitions and configurations
- \`tasks.py\`: Task definitions and workflow
- \`tools.py\`: Tool setup and configuration
- \`main.py\`: Entry point and crew orchestration
- \`requirements.txt\`: Python dependencies
- \`.env.example\`: Environment variable template

## Comparison with Original

The CrewAI upgrade adds:

- **Multi-agent architecture**: Specialized agents for different concerns
- **Task orchestration**: Structured workflow with dependencies
- **Tool integration**: Enhanced capabilities through CrewAI tools
- **Scalability**: Easy to add new agents and tasks
- **Observability**: Built-in verbose logging and monitoring

## Original Repository

For the original implementation, visit:
${githubUrl}

## License

Follows the license of the original repository.
`;

    await fs.writeFile(path.join(targetDir, 'README_CREWAI.md'), readme Content);

    console.log(`[Upgrade Agent] Successfully created CrewAI implementation files`);

    // Update database to mark as upgraded
    const db = new sqlite3.Database('/Users/colinlowenberg/crew/awesome-agents/apps.db');

    await new Promise((resolve, reject) => {
      db.run(
        'UPDATE apps SET has_crewai = 1, tags = REPLACE(tags, ", upgrading", "") WHERE id = ?',
        [appId],
        (err) => {
          if (err) reject(err);
          else resolve();
        }
      );
    });

    await new Promise((resolve) => db.close(resolve));

    console.log(`[Upgrade Agent] Updated database: marked app ${appId} as having CrewAI`);
    console.log(`[Upgrade Agent] Upgrade complete for ${title}!`);

  } catch (error) {
    console.error(`[Upgrade Agent] Error during upgrade:`, error);
    process.exit(1);
  }
}

createCrewAIImplementation();
