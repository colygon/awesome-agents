import { execSync } from 'child_process';
import fs from 'fs';
import path from 'path';

const REPOS_DIR = './selected-app-repos';
const selectedApps = JSON.parse(fs.readFileSync('./selected_apps_for_upgrade.json', 'utf-8'));

// Ensure repos directory exists
if (!fs.existsSync(REPOS_DIR)) {
  fs.mkdirSync(REPOS_DIR, { recursive: true });
}

console.log(`\n🔍 Analyzing ${selectedApps.length} selected Streamlit apps...\n`);

selectedApps.forEach((app, index) => {
  console.log(`\n[${ index + 1}/${selectedApps.length}] ${app.title}`);
  console.log(`   GitHub: ${app.github_url}`);
  console.log(`   Priority: ${app.priority}`);
  console.log(`   Strategy: ${app.upgrade_strategy}`);

  const repoName = app.github_url.split('/').slice(-2).join('_');
  const repoPath = path.join(REPOS_DIR, repoName);

  try {
    // Clone if not exists
    if (!fs.existsSync(repoPath)) {
      console.log(`   → Cloning repository...`);
      execSync(`git clone --depth 1 ${app.github_url} ${repoPath}`, {
        stdio: 'pipe',
        timeout: 30000
      });
      console.log(`   ✓ Cloned successfully`);
    } else {
      console.log(`   ⊙ Already cloned`);
    }

    // Quick analysis
    const pythonFiles = execSync(`find ${repoPath} -name "*.py" -type f | grep -v node_modules | grep -v .git`, {
      encoding: 'utf-8',
      stdio: 'pipe'
    }).split('\n').filter(f => f);

    console.log(`   📄 Python files: ${pythonFiles.length}`);

    // Check for key dependencies
    let hasCrewAI = false;
    let hasLangChain = false;
    let hasLlamaIndex = false;
    let hasOpenAI = false;

    pythonFiles.forEach(file => {
      try {
        const content = fs.readFileSync(file, 'utf-8').toLowerCase();
        if (content.includes('crewai')) hasCrewAI = true;
        if (content.includes('langchain')) hasLangChain = true;
        if (content.includes('llama_index') || content.includes('llama-index')) hasLlamaIndex = true;
        if (content.includes('openai')) hasOpenAI = true;
      } catch (err) {}
    });

    console.log(`   📦 Dependencies:`);
    console.log(`      CrewAI: ${hasCrewAI ? '✅' : '❌'}`);
    console.log(`      LangChain: ${hasLangChain ? '✅' : '❌'}`);
    console.log(`      LlamaIndex: ${hasLlamaIndex ? '✅' : '❌'}`);
    console.log(`      OpenAI: ${hasOpenAI ? '✅' : '❌'}`);

    app.analysis = {
      cloned: true,
      pythonFiles: pythonFiles.length,
      hasCrewAI,
      hasLangChain,
      hasLlamaIndex,
      hasOpenAI,
      status: hasCrewAI ? 'ALREADY_HAS_CREWAI' : (hasLangChain || hasLlamaIndex ? 'REPLACE_AGENTS' : 'ADD_CREWAI')
    };

  } catch (error) {
    console.log(`   ✗ Error: ${error.message}`);
    app.analysis = { error: error.message };
  }
});

// Save updated analysis
fs.writeFileSync('./selected_apps_analysis.json', JSON.stringify(selectedApps, null, 2));

console.log('\n' + '='.repeat(70));
console.log('📊 SUMMARY');
console.log('='.repeat(70));

const summary = {
  alreadyHasCrewAI: selectedApps.filter(a => a.analysis?.status === 'ALREADY_HAS_CREWAI').length,
  needsReplacement: selectedApps.filter(a => a.analysis?.status === 'REPLACE_AGENTS').length,
  needsAddition: selectedApps.filter(a => a.analysis?.status === 'ADD_CREWAI').length,
  errors: selectedApps.filter(a => a.analysis?.error).length
};

console.log(`✅ Already has CrewAI: ${summary.alreadyHasCrewAI}`);
console.log(`🔄 Replace with CrewAI: ${summary.needsReplacement}`);
console.log(`➕ Add CrewAI: ${summary.needsAddition}`);
console.log(`⚠️  Errors: ${summary.errors}`);
console.log('='.repeat(70));

console.log(`\n💾 Analysis saved to: selected_apps_analysis.json`);
console.log(`\n✅ Ready to start upgrading!\n`);
