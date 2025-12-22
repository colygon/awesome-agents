#!/usr/bin/env node

import fs from 'node:fs/promises';
import path from 'node:path';
import axios from 'axios';
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
const { startId, endId, batchName } = args;

console.log(`[Review Agent ${batchName}] Processing apps ${startId} to ${endId}`);

const DB_PATH = '/Users/colinlowenberg/crew/awesome-agents/apps.db';

// Helper to run DB queries
function dbAll(db, query, params = []) {
  return new Promise((resolve, reject) => {
    db.all(query, params, (err, rows) => {
      if (err) reject(err);
      else resolve(rows);
    });
  });
}

function dbRun(db, query, params = []) {
  return new Promise((resolve, reject) => {
    db.run(query, params, function(err) {
      if (err) reject(err);
      else resolve(this);
    });
  });
}

// Check if GitHub URL is valid
async function validateGitHubUrl(url) {
  if (!url) return { valid: false, reason: 'No URL provided' };

  try {
    const match = url.match(/github\.com\/([^\/]+)\/([^\/]+)/);
    if (!match) return { valid: false, reason: 'Not a GitHub URL' };

    const owner = match[1];
    const repo = match[2].replace('.git', '').split('/')[0];

    // Try to fetch the repo
    const response = await axios.get(`https://api.github.com/repos/${owner}/${repo}`, {
      headers: {
        'User-Agent': 'awesome-agents-review/1.0',
        'Accept': 'application/vnd.github+json'
      },
      timeout: 10000,
      validateStatus: (status) => status < 500
    });

    if (response.status === 404) {
      return { valid: false, reason: 'Repository not found (404)', owner, repo };
    }

    if (response.status === 200) {
      return {
        valid: true,
        owner,
        repo,
        repoData: response.data
      };
    }

    return { valid: true, owner, repo }; // Assume valid for other statuses
  } catch (error) {
    console.warn(`[Review Agent ${batchName}] Error validating URL ${url}:`, error.message);
    return { valid: true, reason: 'Unable to verify, assuming valid' };
  }
}

// Find the upgraded directory for a CrewAI app
async function findUpgradedDirectory(appId, title, category) {
  const crewDir = '/Users/colinlowenberg/crew';

  try {
    const entries = await fs.readdir(crewDir, { withFileTypes: true });

    // Look for directory ending with -agent{appId}
    const dirPattern = `-agent${appId}`;
    const matchingDir = entries.find(entry =>
      entry.isDirectory() && entry.name.endsWith(dirPattern)
    );

    if (matchingDir) {
      const dirPath = path.join(crewDir, matchingDir.name);

      // Check if it has CrewAI files
      const files = await fs.readdir(dirPath);
      const hasCrewAI = files.includes('agents.py') ||
                        files.includes('README_CREWAI.md') ||
                        files.includes('main.py');

      if (hasCrewAI) {
        // Try to find GitHub URL in README_CREWAI.md
        try {
          const readmePath = path.join(dirPath, 'README_CREWAI.md');
          const readme = await fs.readFile(readmePath, 'utf8');
          const githubMatch = readme.match(/\*\*Original Repository:\*\* (https:\/\/github\.com\/[^\s\)]+)/);

          return {
            found: true,
            directory: matchingDir.name,
            path: dirPath,
            originalGitHub: githubMatch ? githubMatch[1] : null,
            upgradedGitHub: `https://github.com/colygon/${matchingDir.name}` // Assuming this pattern
          };
        } catch {
          return {
            found: true,
            directory: matchingDir.name,
            path: dirPath,
            originalGitHub: null,
            upgradedGitHub: `https://github.com/colygon/${matchingDir.name}`
          };
        }
      }
    }

    return { found: false };
  } catch (error) {
    console.warn(`[Review Agent ${batchName}] Error finding upgraded directory:`, error.message);
    return { found: false };
  }
}

// Generate image URL based on GitHub repo
function generateImageUrl(githubUrl, repoData) {
  if (!githubUrl) return null;

  const match = githubUrl.match(/github\.com\/([^\/]+)\/([^\/]+)/);
  if (!match) return null;

  const owner = match[1];
  const repo = match[2].replace('.git', '').split('/')[0];

  // Use OpenGraph image
  return `https://opengraph.githubassets.com/1/${owner}/${repo}`;
}

// Main review function
async function reviewApp(db, app) {
  console.log(`\n[Review Agent ${batchName}] Reviewing app ${app.id}: ${app.title}`);

  const updates = {};
  let needsUpdate = false;

  // Step 1: Validate GitHub URL
  console.log(`  Validating GitHub URL...`);
  const validation = await validateGitHubUrl(app.github_url);

  if (!validation.valid) {
    console.warn(`  ⚠️  Invalid GitHub URL: ${validation.reason}`);
  } else {
    console.log(`  ✓ GitHub URL is valid`);
  }

  // Step 2: Check if app has been upgraded to CrewAI
  if (app.has_crewai === 1) {
    console.log(`  Checking for upgraded directory...`);
    const upgraded = await findUpgradedDirectory(app.id, app.title, app.category);

    if (upgraded.found) {
      console.log(`  ✓ Found upgraded directory: ${upgraded.directory}`);

      // Check if GitHub URL should point to upgraded version
      const currentUrl = app.github_url || '';
      const upgradedUrl = upgraded.upgradedGitHub;

      // If the app is pointing to the original, consider updating
      // But keep original if it's already a CrewAI repo
      if (upgraded.originalGitHub && currentUrl === upgraded.originalGitHub) {
        console.log(`  ℹ️  App points to original repo, upgraded version exists at local directory`);
        // Don't change URL - keep pointing to original source
      }
    } else {
      console.log(`  ℹ️  No upgraded directory found for agent${app.id}`);
    }
  }

  // Step 3: Check and generate image if missing
  if (!app.image_url || app.image_url.trim() === '') {
    console.log(`  ⚠️  Missing image, generating...`);

    if (validation.valid && validation.owner && validation.repo) {
      const imageUrl = generateImageUrl(app.github_url, validation.repoData);
      updates.image_url = imageUrl;
      needsUpdate = true;
      console.log(`  ✓ Generated image URL: ${imageUrl}`);
    } else {
      console.log(`  ⚠️  Cannot generate image without valid GitHub URL`);
    }
  } else {
    console.log(`  ✓ Image exists: ${app.image_url}`);
  }

  // Step 4: Apply updates if needed
  if (needsUpdate && Object.keys(updates).length > 0) {
    const setClauses = Object.keys(updates).map(key => `${key} = ?`).join(', ');
    const values = [...Object.values(updates), app.id];

    await dbRun(db, `UPDATE apps SET ${setClauses} WHERE id = ?`, values);
    console.log(`  ✓ Updated app ${app.id} with new data`);
  } else {
    console.log(`  ✓ No updates needed for app ${app.id}`);
  }

  return {
    id: app.id,
    title: app.title,
    validation,
    updates,
    needsUpdate
  };
}

// Main execution
async function main() {
  const db = new sqlite3.Database(DB_PATH);

  try {
    // Fetch apps in the specified range
    const apps = await dbAll(
      db,
      'SELECT * FROM apps WHERE id >= ? AND id <= ? ORDER BY id',
      [parseInt(startId), parseInt(endId)]
    );

    console.log(`[Review Agent ${batchName}] Found ${apps.length} apps to review`);

    const results = [];
    for (const app of apps) {
      try {
        const result = await reviewApp(db, app);
        results.push(result);

        // Small delay to avoid rate limiting
        await new Promise(resolve => setTimeout(resolve, 200));
      } catch (error) {
        console.error(`[Review Agent ${batchName}] Error reviewing app ${app.id}:`, error);
        results.push({
          id: app.id,
          title: app.title,
          error: error.message
        });
      }
    }

    // Summary
    console.log(`\n[Review Agent ${batchName}] ========== SUMMARY ==========`);
    console.log(`Total apps reviewed: ${results.length}`);
    console.log(`Apps updated: ${results.filter(r => r.needsUpdate).length}`);
    console.log(`Apps with errors: ${results.filter(r => r.error).length}`);
    console.log(`Invalid GitHub URLs: ${results.filter(r => r.validation && !r.validation.valid).length}`);
    console.log(`[Review Agent ${batchName}] Complete!`);

  } catch (error) {
    console.error(`[Review Agent ${batchName}] Fatal error:`, error);
    process.exit(1);
  } finally {
    await new Promise(resolve => db.close(resolve));
  }
}

main();
