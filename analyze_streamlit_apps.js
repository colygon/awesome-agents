import db from './streamlit-gallery-clone/db.js';
import { execSync } from 'child_process';
import fs from 'fs';
import path from 'path';

const REPOS_DIR = './streamlit-repos';
const ANALYSIS_RESULTS = './app_analysis_results.json';

// Ensure repos directory exists
if (!fs.existsSync(REPOS_DIR)) {
  fs.mkdirSync(REPOS_DIR, { recursive: true });
}

// Function to analyze a single repository
async function analyzeRepo(app) {
  const repoName = app.github_url.split('/').slice(-2).join('_');
  const repoPath = path.join(REPOS_DIR, repoName);

  const analysis = {
    id: app.id,
    title: app.title,
    github_url: app.github_url,
    has_crewai: false,
    has_langchain: false,
    has_openai: false,
    has_anthropic: false,
    has_other_agents: false,
    agent_frameworks: [],
    is_cloned: false,
    clone_error: null,
    file_count: 0,
    python_files: 0
  };

  try {
    // Clone repo if not already cloned
    if (!fs.existsSync(repoPath)) {
      console.log(`  Cloning ${app.github_url}...`);
      execSync(`git clone --depth 1 ${app.github_url} ${repoPath}`, {
        stdio: 'pipe',
        timeout: 30000
      });
    }
    analysis.is_cloned = true;

    // Search for imports and usage patterns
    const searchPatterns = {
      crewai: ['crewai', 'from crewai', 'import crewai'],
      langchain: ['langchain', 'from langchain', 'import langchain'],
      openai: ['openai', 'from openai', 'import openai', 'OpenAI('],
      anthropic: ['anthropic', 'from anthropic', 'import anthropic'],
      autogen: ['autogen', 'from autogen'],
      llamaindex: ['llama_index', 'llama-index', 'from llama_index']
    };

    // Count files
    const allFiles = execSync(`find ${repoPath} -type f`, { encoding: 'utf-8' })
      .split('\n')
      .filter(f => f && !f.includes('node_modules') && !f.includes('.git'));

    analysis.file_count = allFiles.length;

    const pythonFiles = allFiles.filter(f => f.endsWith('.py'));
    analysis.python_files = pythonFiles.length;

    // Search through Python files
    for (const file of pythonFiles) {
      try {
        const content = fs.readFileSync(file, 'utf-8').toLowerCase();

        if (searchPatterns.crewai.some(pattern => content.includes(pattern))) {
          analysis.has_crewai = true;
        }
        if (searchPatterns.langchain.some(pattern => content.includes(pattern))) {
          analysis.has_langchain = true;
          if (!analysis.agent_frameworks.includes('langchain')) {
            analysis.agent_frameworks.push('langchain');
          }
        }
        if (searchPatterns.openai.some(pattern => content.includes(pattern))) {
          analysis.has_openai = true;
        }
        if (searchPatterns.anthropic.some(pattern => content.includes(pattern))) {
          analysis.has_anthropic = true;
        }
        if (searchPatterns.autogen.some(pattern => content.includes(pattern))) {
          analysis.has_other_agents = true;
          if (!analysis.agent_frameworks.includes('autogen')) {
            analysis.agent_frameworks.push('autogen');
          }
        }
        if (searchPatterns.llamaindex.some(pattern => content.includes(pattern))) {
          analysis.has_other_agents = true;
          if (!analysis.agent_frameworks.includes('llamaindex')) {
            analysis.agent_frameworks.push('llamaindex');
          }
        }
      } catch (err) {
        // Skip files that can't be read
      }
    }

    // Determine classification
    if (analysis.has_crewai) {
      analysis.classification = 'HAS_CREWAI';
    } else if (analysis.agent_frameworks.length > 0) {
      analysis.classification = 'HAS_OTHER_AGENTS';
    } else if (analysis.has_openai || analysis.has_anthropic) {
      analysis.classification = 'HAS_LLM_NO_AGENTS';
    } else {
      analysis.classification = 'NO_AI';
    }

  } catch (error) {
    analysis.clone_error = error.message;
    analysis.classification = 'ERROR';
  }

  return analysis;
}

// Main function
async function analyzeAllApps() {
  return new Promise((resolve, reject) => {
    db.all('SELECT id, title, github_url FROM apps WHERE category = "streamlit" ORDER BY id', async (err, apps) => {
      if (err) {
        reject(err);
        return;
      }

      console.log(`\n🔍 Analyzing ${apps.length} Streamlit apps...\n`);

      const results = [];
      let processed = 0;

      for (const app of apps) {
        processed++;
        console.log(`[${processed}/${apps.length}] Analyzing: ${app.title}`);

        const analysis = await analyzeRepo(app);
        results.push(analysis);

        // Save progress every 10 apps
        if (processed % 10 === 0) {
          fs.writeFileSync(ANALYSIS_RESULTS, JSON.stringify(results, null, 2));
          console.log(`  💾 Progress saved (${processed} apps analyzed)\n`);
        }
      }

      // Final save
      fs.writeFileSync(ANALYSIS_RESULTS, JSON.stringify(results, null, 2));

      // Generate summary
      const summary = {
        total: results.length,
        has_crewai: results.filter(r => r.classification === 'HAS_CREWAI').length,
        has_other_agents: results.filter(r => r.classification === 'HAS_OTHER_AGENTS').length,
        has_llm_no_agents: results.filter(r => r.classification === 'HAS_LLM_NO_AGENTS').length,
        no_ai: results.filter(r => r.classification === 'NO_AI').length,
        errors: results.filter(r => r.classification === 'ERROR').length
      };

      console.log('\n' + '='.repeat(60));
      console.log('📊 ANALYSIS SUMMARY');
      console.log('='.repeat(60));
      console.log(`Total apps analyzed:        ${summary.total}`);
      console.log(`✅ Already has CrewAI:      ${summary.has_crewai}`);
      console.log(`🔄 Has other agents:        ${summary.has_other_agents}`);
      console.log(`➕ Has LLM, no agents:      ${summary.has_llm_no_agents}`);
      console.log(`❌ No AI:                   ${summary.no_ai}`);
      console.log(`⚠️  Errors:                  ${summary.errors}`);
      console.log('='.repeat(60));

      // Show apps by category
      console.log('\n📋 APPS BY CATEGORY:\n');

      const categories = {
        'HAS_CREWAI': '✅ Already has CrewAI',
        'HAS_OTHER_AGENTS': '🔄 Has other agents',
        'HAS_LLM_NO_AGENTS': '➕ Has LLM, no agents',
        'NO_AI': '❌ No AI',
        'ERROR': '⚠️  Error'
      };

      for (const [key, label] of Object.entries(categories)) {
        const apps = results.filter(r => r.classification === key);
        if (apps.length > 0) {
          console.log(`\n${label} (${apps.length}):`);
          apps.slice(0, 5).forEach(app => {
            console.log(`  - ${app.title}`);
            if (app.agent_frameworks.length > 0) {
              console.log(`    Frameworks: ${app.agent_frameworks.join(', ')}`);
            }
          });
          if (apps.length > 5) {
            console.log(`  ... and ${apps.length - 5} more`);
          }
        }
      }

      console.log(`\n💾 Full results saved to: ${ANALYSIS_RESULTS}\n`);

      resolve({ results, summary });
    });
  });
}

// Run the analysis
analyzeAllApps()
  .then(() => {
    console.log('✅ Analysis complete!');
    db.close();
    process.exit(0);
  })
  .catch((error) => {
    console.error('❌ Error:', error);
    db.close();
    process.exit(1);
  });
