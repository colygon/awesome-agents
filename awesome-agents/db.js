import sqlite3 from 'sqlite3';
import { fileURLToPath } from 'url';
import { dirname, join } from 'path';
import fs from 'fs';

const __filename = fileURLToPath(import.meta.url);
const __dirname = dirname(__filename);

// Use /tmp for Vercel serverless or local path
const dbPath = process.env.VERCEL ? '/tmp/apps.db' : join(__dirname, 'apps.db');

const db = new sqlite3.Database(dbPath);

db.serialize(() => {
  db.run(`CREATE TABLE IF NOT EXISTS apps (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    description TEXT,
    github_url TEXT,
    tags TEXT,
    watchers INTEGER DEFAULT 0,
    views INTEGER DEFAULT 0,
    image_url TEXT,
    has_crewai INTEGER DEFAULT 0,
    category TEXT,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
  )`);
});

export default db;
