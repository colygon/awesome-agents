import fs from 'node:fs/promises';
import path from 'node:path';
import axios from 'axios';
import sqlite3 from 'sqlite3';

const DEFAULT_CONFIG_PATH = './sync.config.json';

function parseArgs(argv) {
  const args = { config: DEFAULT_CONFIG_PATH };
  for (let i = 2; i < argv.length; i += 1) {
    const token = argv[i];
    if (token === '--config' || token === '-c') {
      args.config = argv[i + 1];
      i += 1;
      continue;
    }
    if (token === '--help' || token === '-h') {
      args.help = true;
      continue;
    }
  }
  return args;
}

function printHelp() {
  console.log(`Usage: node sync.js [--config path/to/sync.config.json]\n\nConfig example: sync.config.example.json\n\nEnv:\n  GITHUB_TOKEN  Optional, increases GitHub API rate limits\n`);
}

async function readJson(filePath) {
  const raw = await fs.readFile(filePath, 'utf8');
  return JSON.parse(raw);
}

function openDb(dbPath) {
  return new sqlite3.Database(dbPath);
}

function dbRun(db, sql, params = []) {
  return new Promise((resolve, reject) => {
    db.run(sql, params, function onRun(err) {
      if (err) reject(err);
      else resolve(this);
    });
  });
}

function normalizeGithubUrl(url) {
  if (!url || typeof url !== 'string') return null;
  try {
    const parsed = new URL(url);
    parsed.hash = '';
    parsed.search = '';
    parsed.pathname = parsed.pathname.replace(/\/$/, '');
    if (parsed.hostname.toLowerCase() === 'www.github.com') parsed.hostname = 'github.com';
    return parsed.toString();
  } catch {
    return null;
  }
}

function parseGithubRepoFullName(githubUrl) {
  const normalized = normalizeGithubUrl(githubUrl);
  if (!normalized) return null;
  try {
    const url = new URL(normalized);
    if (url.hostname !== 'github.com') return null;
    const parts = url.pathname.split('/').filter(Boolean);
    if (parts.length < 2) return null;
    return `${parts[0]}/${parts[1]}`;
  } catch {
    return null;
  }
}

function normalizeTags(tags) {
  const uniq = new Map();
  for (const tag of tags) {
    const cleaned = String(tag ?? '').trim();
    if (!cleaned) continue;
    const key = cleaned.toLowerCase();
    if (!uniq.has(key)) uniq.set(key, cleaned);
  }
  return Array.from(uniq.values());
}

function stableHashInt(input) {
  let hash = 0x811c9dc5;
  for (let i = 0; i < input.length; i += 1) {
    hash ^= input.charCodeAt(i);
    hash = (hash * 0x01000193) >>> 0;
  }
  return hash;
}

function computeViews({ streamlitViews, stargazers, watchers, seed }) {
  if (Number.isFinite(streamlitViews) && streamlitViews > 0) return Math.round(streamlitViews);
  const base = (Number(stargazers) || 0) * 200 + (Number(watchers) || 0) * 50;
  const jitter = (seed % 2000) + 250;
  return Math.max(0, Math.round(base + jitter));
}

function limitConcurrency(concurrency) {
  let active = 0;
  const queue = [];
  const next = () => {
    if (active >= concurrency) return;
    const job = queue.shift();
    if (!job) return;
    active += 1;
    job().finally(() => {
      active -= 1;
      next();
    });
  };
  return async fn => new Promise((resolve, reject) => {
    queue.push(async () => {
      try {
        resolve(await fn());
      } catch (err) {
        reject(err);
      }
    });
    next();
  });
}

function pickLargestAppsArray(nextData) {
  const visited = new Set();
  let best = [];

  function visit(node) {
    if (!node || typeof node !== 'object') return;
    if (visited.has(node)) return;
    visited.add(node);

    if (Array.isArray(node)) {
      const looksLikeApps = node.length > 0 && node.every(item => item && typeof item === 'object' && ('gitHubUrl' in item || 'githubUrl' in item || 'github_url' in item) && ('title' in item));
      if (looksLikeApps && node.length > best.length) best = node;
      for (const item of node) visit(item);
      return;
    }

    for (const value of Object.values(node)) visit(value);
  }

  visit(nextData);
  return best;
}

async function fetchOfficialGallery(url) {
  const response = await axios.get(url, {
    headers: {
      'User-Agent': 'awesome-agents/1.0 (+sync.js)',
      Accept: 'text/html,application/xhtml+xml'
    },
    timeout: 30_000
  });

  const html = String(response.data);
  const match = html.match(/<script[^>]+id=\"__NEXT_DATA__\"[^>]*>([\s\S]*?)<\/script>/i);
  if (!match) throw new Error(`Could not find __NEXT_DATA__ on ${url}`);

  const nextData = JSON.parse(match[1]);
  const apps = pickLargestAppsArray(nextData);

  return apps
    .map(item => ({
      title: String(item.title ?? '').trim(),
      github_url: normalizeGithubUrl(item.gitHubUrl ?? item.githubUrl ?? item.github_url),
      categories: Array.isArray(item.categories) ? item.categories : [],
      image_url: item.image ?? null,
      streamlit_views: Number.isFinite(Number(item.weight)) ? Number(item.weight) : null,
      source: 'official'
    }))
    .filter(app => Boolean(app.github_url));
}

async function fetchCommunityExplore() {
  const base = 'https://share.streamlit.io/api/v2/gallery';
  const categoriesResponse = await axios.get(`${base}/categories`, {
    headers: { 'User-Agent': 'streamlit-gallery-clone/1.0 (+sync.js)', Accept: 'application/json' },
    timeout: 30_000
  });

  const categories = Array.isArray(categoriesResponse.data?.data) ? categoriesResponse.data.data : [];
  const byGithub = new Map();

  for (const category of categories) {
    const slug = category?.name;
    const pretty = category?.prettyName || slug;
    if (!slug) continue;

    const limit = 200;
    for (let offset = 0; offset < 50_000; offset += limit) {
      const url = `${base}/search?category=${encodeURIComponent(slug)}&limit=${limit}&offset=${offset}`;
      const response = await axios.get(url, {
        headers: { 'User-Agent': 'streamlit-gallery-clone/1.0 (+sync.js)', Accept: 'application/json' },
        timeout: 30_000
      });

      const apps = Array.isArray(response.data?.apps) ? response.data.apps : [];
      if (apps.length === 0) break;

      for (const item of apps) {
        const github_url = normalizeGithubUrl(item.gitHubUrl);
        if (!github_url) continue;

        const existing = byGithub.get(github_url);
        const merged = {
          title: String(item.title ?? '').trim() || existing?.title || '',
          github_url,
          categories: normalizeTags([...(existing?.categories || []), pretty]),
          image_url: item.image || existing?.image_url || null,
          streamlit_views: Number.isFinite(Number(item.views)) ? Number(item.views) : existing?.streamlit_views ?? null,
          source: 'community'
        };
        byGithub.set(github_url, merged);
      }
    }
  }

  return Array.from(byGithub.values());
}

async function fetchGithubReposFeed(repos) {
  const out = [];
  for (const repo of repos || []) {
    const github_url = normalizeGithubUrl(repo);
    if (!github_url) continue;
    out.push({
      title: '',
      github_url,
      categories: [],
      image_url: null,
      streamlit_views: null,
      source: 'custom'
    });
  }
  return out;
}

async function fetchGithubRepoMeta(fullName, tokenEnvVar) {
  const token = tokenEnvVar ? process.env[tokenEnvVar] : process.env.GITHUB_TOKEN;
  const headers = {
    'User-Agent': 'streamlit-gallery-clone/1.0 (+sync.js)',
    Accept: 'application/vnd.github+json',
    'X-GitHub-Api-Version': '2022-11-28'
  };
  if (token) headers.Authorization = `Bearer ${token}`;
  const response = await axios.get(`https://api.github.com/repos/${fullName}`, { headers, timeout: 20_000 });
  return response.data;
}

function mergeByGithub(apps) {
  const byGithub = new Map();
  for (const app of apps) {
    if (!app.github_url) continue;
    const existing = byGithub.get(app.github_url);
    if (!existing) {
      byGithub.set(app.github_url, { ...app, categories: normalizeTags(app.categories || []) });
      continue;
    }

    const preferred = existing.source === 'official' ? existing : app.source === 'official' ? app : existing;
    preferred.title = preferred.title || app.title || existing.title;
    preferred.image_url = preferred.image_url || app.image_url || existing.image_url;
    preferred.streamlit_views = Number.isFinite(preferred.streamlit_views) ? preferred.streamlit_views : app.streamlit_views;
    preferred.categories = normalizeTags([...(existing.categories || []), ...(app.categories || [])]);
    byGithub.set(app.github_url, preferred);
  }
  return Array.from(byGithub.values());
}

async function enrichWithGithub(apps, { tokenEnvVar, concurrency }) {
  const schedule = limitConcurrency(Math.max(1, Number(concurrency) || 4));
  let lookups = 0;
  let failures = 0;

  await Promise.all(
    apps.map(app =>
      schedule(async () => {
        const repoFullName = parseGithubRepoFullName(app.github_url);
        const seed = stableHashInt(repoFullName ?? app.github_url);

        let repoMeta = null;
        if (repoFullName) {
          try {
            lookups += 1;
            repoMeta = await fetchGithubRepoMeta(repoFullName, tokenEnvVar);
          } catch {
            failures += 1;
          }
        }

        const topics = Array.isArray(repoMeta?.topics) ? repoMeta.topics : [];
        const watchers = Number.isFinite(repoMeta?.subscribers_count)
          ? repoMeta.subscribers_count
          : Number.isFinite(repoMeta?.watchers_count)
            ? repoMeta.watchers_count
            : 0;
        const stargazers = Number.isFinite(repoMeta?.stargazers_count) ? repoMeta.stargazers_count : 0;

        const tags = normalizeTags([
          app.source === 'official' ? 'official' : app.source === 'community' ? 'community' : 'custom',
          ...(app.categories || []),
          ...topics
        ]);

        app.title = app.title || (repoMeta?.name ? String(repoMeta.name) : 'Untitled');
        app.description = (repoMeta?.description && String(repoMeta.description).trim())
          ? String(repoMeta.description).trim()
          : app.source === 'official'
            ? 'Official Streamlit demo app.'
            : app.source === 'community'
              ? 'Streamlit Community Cloud app.'
              : 'Synced from a custom list.';

        app.tags = tags.join(', ');
        app.watchers = Number(watchers) || 0;
        app.views = computeViews({ streamlitViews: app.streamlit_views, stargazers, watchers, seed });

        if (!app.image_url && repoFullName) {
          app.image_url = `https://opengraph.githubassets.com/1/${repoFullName}`;
        }
      })
    )
  );

  return { lookups, failures };
}

async function writeToDb(dbPath, apps, { resetBeforeInsert }) {
  const db = openDb(dbPath);
  try {
    await dbRun(
      db,
      `CREATE TABLE IF NOT EXISTS apps (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        description TEXT,
        github_url TEXT,
        tags TEXT,
        watchers INTEGER DEFAULT 0,
        views INTEGER DEFAULT 0,
        image_url TEXT,
        created_at DATETIME DEFAULT CURRENT_TIMESTAMP
      )`
    );

    if (resetBeforeInsert) {
      await dbRun(db, 'DELETE FROM apps');
    }

    const insertSql = 'INSERT INTO apps (title, description, github_url, tags, watchers, views, image_url) VALUES (?, ?, ?, ?, ?, ?, ?)';
    for (const app of apps) {
      await dbRun(db, insertSql, [app.title, app.description, app.github_url, app.tags, app.watchers, app.views, app.image_url]);
    }
  } finally {
    await new Promise(resolve => db.close(resolve));
  }
}

async function run() {
  const args = parseArgs(process.argv);
  if (args.help) {
    printHelp();
    return;
  }

  const configPath = path.resolve(process.cwd(), args.config);
  const config = await readJson(configPath);

  const dbPath = config.dbPath || './apps.db';
  const resetBeforeInsert = config.resetBeforeInsert !== false;
  const githubConfig = {
    tokenEnvVar: config.github?.tokenEnvVar || 'GITHUB_TOKEN',
    concurrency: config.github?.concurrency ?? 6
  };

  const feeds = Array.isArray(config.feeds) ? config.feeds : [];
  if (feeds.length === 0) throw new Error('Config has no feeds. Add at least one feed in config.feeds.');

  const collected = [];
  for (const feed of feeds) {
    if (feed?.type === 'streamlit_official_gallery') {
      const url = feed.url || 'https://streamlit.io/gallery';
      console.log(`Sync: streamlit_official_gallery (${url})…`);
      collected.push(...(await fetchOfficialGallery(url)));
      continue;
    }

    if (feed?.type === 'streamlit_community_explore') {
      console.log('Sync: streamlit_community_explore (API)…');
      collected.push(...(await fetchCommunityExplore()));
      continue;
    }

    if (feed?.type === 'github_repos') {
      console.log(`Sync: github_repos (${feed.name || 'unnamed'})…`);
      collected.push(...(await fetchGithubReposFeed(feed.repos)));
      continue;
    }

    throw new Error(`Unknown feed type: ${feed?.type}`);
  }

  const merged = mergeByGithub(collected);
  console.log(`Collected ${collected.length} entries; de-duped to ${merged.length} unique GitHub repos`);

  const { lookups, failures } = await enrichWithGithub(merged, githubConfig);
  console.log(`GitHub enrich: lookups=${lookups} failures=${failures} (set ${githubConfig.tokenEnvVar} to reduce failures/rate-limits)`);

  await writeToDb(dbPath, merged, { resetBeforeInsert });
  console.log(`Wrote ${merged.length} apps to ${dbPath}`);
}

run().catch(err => {
  console.error(err);
  process.exitCode = 1;
});
