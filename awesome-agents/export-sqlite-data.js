#!/usr/bin/env node

import sqlite3 from 'sqlite3';
import fs from 'fs/promises';

const db = new sqlite3.Database('./apps.db');

async function exportData() {
  return new Promise((resolve, reject) => {
    db.all('SELECT * FROM apps ORDER BY id', [], (err, rows) => {
      if (err) {
        reject(err);
        return;
      }
      resolve(rows);
    });
  });
}

async function main() {
  console.log('Exporting data from SQLite database...');

  const data = await exportData();

  console.log(`Exported ${data.length} apps`);

  // Save as JSON
  await fs.writeFile('./apps-export.json', JSON.stringify(data, null, 2));
  console.log('Saved to apps-export.json');

  // Also create SQL INSERT statements for Postgres
  const sqlStatements = data.map(app => {
    const values = [
      app.id,
      app.title ? `'${app.title.replace(/'/g, "''")}'` : 'NULL',
      app.description ? `'${app.description.replace(/'/g, "''")}'` : 'NULL',
      app.github_url ? `'${app.github_url.replace(/'/g, "''")}'` : 'NULL',
      app.tags ? `'${app.tags.replace(/'/g, "''")}'` : 'NULL',
      app.watchers || 0,
      app.views || 0,
      app.image_url ? `'${app.image_url.replace(/'/g, "''")}'` : 'NULL',
      app.has_crewai || 0,
      app.category ? `'${app.category.replace(/'/g, "''")}'` : 'NULL'
    ];

    return `INSERT INTO apps (id, title, description, github_url, tags, watchers, views, image_url, has_crewai, category) VALUES (${values.join(', ')});`;
  });

  const sqlContent = `-- Exported from SQLite on ${new Date().toISOString()}
-- Total apps: ${data.length}

-- Create table (if needed)
CREATE TABLE IF NOT EXISTS apps (
  id SERIAL PRIMARY KEY,
  title TEXT,
  description TEXT,
  github_url TEXT,
  tags TEXT,
  watchers INTEGER DEFAULT 0,
  views INTEGER DEFAULT 0,
  image_url TEXT,
  has_crewai INTEGER DEFAULT 0,
  category TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Insert data
${sqlStatements.join('\n')}

-- Update sequence
SELECT setval('apps_id_seq', (SELECT MAX(id) FROM apps));
`;

  await fs.writeFile('./apps-export.sql', sqlContent);
  console.log('Saved SQL to apps-export.sql');

  // Close database
  db.close();

  console.log('\nExport complete!');
  console.log(`- JSON: apps-export.json`);
  console.log(`- SQL: apps-export.sql`);
}

main().catch(console.error);
