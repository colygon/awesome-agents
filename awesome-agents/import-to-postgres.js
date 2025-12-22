#!/usr/bin/env node

import { sql } from '@vercel/postgres';
import fs from 'fs/promises';

async function importData() {
  console.log('Importing data to Vercel Postgres...');

  // Read exported data
  const data = JSON.parse(await fs.readFile('./apps-export.json', 'utf8'));
  console.log(`Found ${data.length} apps to import`);

  // Create table
  console.log('Creating table schema...');
  await sql.query(`
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
    )
  `);

  // Clear existing data (if any)
  console.log('Clearing existing data...');
  await sql.query('TRUNCATE TABLE apps RESTART IDENTITY');

  // Insert data in batches
  console.log('Inserting apps...');
  const batchSize = 50;

  for (let i = 0; i < data.length; i += batchSize) {
    const batch = data.slice(i, i + batchSize);

    for (const app of batch) {
      await sql.query(
        `INSERT INTO apps (id, title, description, github_url, tags, watchers, views, image_url, has_crewai, category)
         VALUES ($1, $2, $3, $4, $5, $6, $7, $8, $9, $10)`,
        [
          app.id,
          app.title,
          app.description,
          app.github_url,
          app.tags,
          app.watchers || 0,
          app.views || 0,
          app.image_url,
          app.has_crewai || 0,
          app.category
        ]
      );
    }

    console.log(`  Imported ${Math.min(i + batchSize, data.length)}/${data.length} apps`);
  }

  // Update sequence to continue from max ID
  console.log('Updating sequence...');
  await sql.query(`SELECT setval('apps_id_seq', (SELECT MAX(id) FROM apps))`);

  // Verify
  const result = await sql.query('SELECT COUNT(*) FROM apps');
  console.log(`\n✅ Import complete! Total apps in database: ${result.rows[0].count}`);
}

importData().catch(error => {
  console.error('Import failed:', error);
  process.exit(1);
});
