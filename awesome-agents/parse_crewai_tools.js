// Script to parse CrewAI tools and add them to the database

import sqlite3 from 'better-sqlite3';
import path from 'path';
import { fileURLToPath } from 'url';

const __dirname = path.dirname(fileURLToPath(import.meta.url));

const dbPath = path.join(__dirname, 'apps.db');
const db = sqlite3(dbPath);

// CrewAI Tools extracted from the HTML
const crewaiTools = [
  {
    name: 'AIMindTool',
    description: 'A wrapper around AI-Minds. Useful for when you need answers to questions from your data, stored in data sources including PostgreSQL, MySQL, MariaDB, ClickHouse, Snowflake and Google BigQuery.',
    docs_url: 'https://docs.crewai.com/tools/ai-ml/aimindtool',
    github_url: 'https://github.com/crewAIInc/crewAI-tools',
    tags: 'Tools, AI/ML, Database, Data Query'
  },
  {
    name: 'ArxivPaperTool',
    description: 'Fetches metadata from Arxiv based on a search query and optionally downloads PDFs. Perfect for academic research and paper retrieval.',
    docs_url: 'https://arxiv.org',
    github_url: 'https://github.com/crewAIInc/crewAI-tools',
    tags: 'Tools, Research, Academic, PDF'
  },
  {
    name: 'BraveSearchTool',
    description: 'A tool that can be used to search the internet with a search_query using Brave Search API. Supports customizable result counts and country-specific searches.',
    docs_url: 'https://docs.crewai.com/tools/search-research/bravesearchtool',
    github_url: 'https://github.com/crewAIInc/crewAI-tools',
    tags: 'Tools, Search, Web Search, Research'
  },
  {
    name: 'BrightDataDatasetTool',
    description: 'Scrapes structured data using Bright Data Dataset API from a URL and optional input parameters. Ideal for web scraping and data collection.',
    docs_url: 'https://brightdata.com',
    github_url: 'https://github.com/crewAIInc/crewAI-tools',
    tags: 'Tools, Web Scraping, Data Collection'
  },
  {
    name: 'BrightDataSearchTool',
    description: 'Tool to perform web search using Bright Data SERP API. Returns structured results from search engines like Google or Bing.',
    docs_url: 'https://brightdata.com',
    github_url: 'https://github.com/crewAIInc/crewAI-tools',
    tags: 'Tools, Search, SERP, Web Search'
  },
  {
    name: 'BrightDataWebUnlockerTool',
    description: 'Tool to perform web scraping using Bright Data Web Unlocker. Bypasses bot protection, CAPTCHA, and geo-restrictions.',
    docs_url: 'https://brightdata.com',
    github_url: 'https://github.com/crewAIInc/crewAI-tools',
    tags: 'Tools, Web Scraping, Anti-Bot'
  },
  {
    name: 'BrowserbaseLoadTool',
    description: 'Load webpages in a headless browser using Browserbase and return the contents. Perfect for dynamic web scraping.',
    docs_url: 'https://docs.crewai.com/tools/web-scraping/browserbaseloadtool',
    github_url: 'https://github.com/crewAIInc/crewAI-tools',
    tags: 'Tools, Web Scraping, Headless Browser'
  },
  {
    name: 'CSVSearchTool',
    description: 'A tool that can be used to semantic search a query from a CSV\'s content. Perfect for searching financial data, analytics, and structured datasets.',
    docs_url: 'https://docs.crewai.com/tools/file-document/csvsearchtool',
    github_url: 'https://github.com/crewAIInc/crewAI-tools',
    tags: 'Tools, CSV, Data Analysis, Search'
  },
  {
    name: 'CodeDocsSearchTool',
    description: 'A tool that can be used to semantic search a query from Code Docs content. Ideal for documentation search and code reference.',
    docs_url: 'https://docs.crewai.com/tools/search-research/codedocssearchtool',
    github_url: 'https://github.com/crewAIInc/crewAI-tools',
    tags: 'Tools, Documentation, Code, Search'
  },
  {
    name: 'CodeInterpreterTool',
    description: 'Interprets Python3 code strings with a final print statement. Executes code in isolated Docker containers for safety.',
    docs_url: 'https://docs.crewai.com/tools/ai-ml/codeinterpretertool',
    github_url: 'https://github.com/crewAIInc/crewAI-tools',
    tags: 'Tools, Code Execution, Python, AI/ML'
  },
  {
    name: 'ComposioTool',
    description: 'Wrapper for composio tools. Enables automation and integration with various external services.',
    docs_url: 'https://docs.crewai.com/tools/automation/composiotool',
    github_url: 'https://github.com/crewAIInc/crewAI-tools',
    tags: 'Tools, Automation, Integration'
  }
];

console.log('Adding CrewAI Tools to database...\n');

let added = 0;
let skipped = 0;

for (const tool of crewaiTools) {
  // Check if tool already exists
  const existing = db.prepare('SELECT id FROM apps WHERE title = ? AND category = ?')
    .get(tool.name, 'Tools');

  if (existing) {
    console.log(`⏭️  Skipping ${tool.name} (already exists)`);
    skipped++;
    continue;
  }

  // Insert the tool
  const result = db.prepare(`
    INSERT INTO apps (title, description, github_url, tags, category, watchers, views)
    VALUES (?, ?, ?, ?, ?, ?, ?)
  `).run(
    tool.name,
    tool.description,
    tool.github_url,
    tool.tags,
    'Tools',
    0,
    0
  );

  console.log(`✅ Added ${tool.name} (ID: ${result.lastInsertRowid})`);
  added++;
}

console.log(`\n📊 Summary:`);
console.log(`   Added: ${added} tools`);
console.log(`   Skipped: ${skipped} tools (already existed)`);
console.log(`   Total: ${added + skipped} tools processed`);

db.close();
