import sqlite3 from 'sqlite3';

const db = new sqlite3.Database('./apps.db');

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
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
  )`);
});

export default db;
