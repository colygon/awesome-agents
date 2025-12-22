import { sql } from '@vercel/postgres';

// Vercel Postgres connection
// Uses environment variables: POSTGRES_URL, POSTGRES_PRISMA_URL, etc.
// These are automatically set when you create a Postgres database in Vercel

export async function getApps(filters = {}) {
  const { search, category } = filters;

  let query = 'SELECT * FROM apps WHERE 1=1';
  const params = [];
  let paramIndex = 1;

  if (search) {
    query += ` AND (title ILIKE $${paramIndex} OR description ILIKE $${paramIndex} OR tags ILIKE $${paramIndex})`;
    params.push(`%${search}%`);
    paramIndex++;
  }

  if (category) {
    query += ` AND category = $${paramIndex}`;
    params.push(category);
    paramIndex++;
  }

  query += ' ORDER BY id DESC';

  const result = await sql.query(query, params);
  return result.rows;
}

export async function getAppById(id) {
  const result = await sql.query('SELECT * FROM apps WHERE id = $1', [id]);
  return result.rows[0];
}

export async function createApp(app) {
  const {
    title,
    description,
    github_url,
    tags,
    watchers = 0,
    views = 0,
    image_url = '',
    has_crewai = 0,
    category = null
  } = app;

  const result = await sql.query(
    `INSERT INTO apps (title, description, github_url, tags, watchers, views, image_url, has_crewai, category)
     VALUES ($1, $2, $3, $4, $5, $6, $7, $8, $9)
     RETURNING *`,
    [title, description, github_url, tags, watchers, views, image_url, has_crewai, category]
  );

  return result.rows[0];
}

export async function updateApp(id, updates) {
  const fields = [];
  const values = [];
  let paramIndex = 1;

  Object.entries(updates).forEach(([key, value]) => {
    fields.push(`${key} = $${paramIndex}`);
    values.push(value);
    paramIndex++;
  });

  values.push(id);

  const query = `UPDATE apps SET ${fields.join(', ')} WHERE id = $${paramIndex} RETURNING *`;
  const result = await sql.query(query, values);

  return result.rows[0];
}

export async function deleteApp(id) {
  await sql.query('DELETE FROM apps WHERE id = $1', [id]);
}

// Initialize database schema
export async function initDatabase() {
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
}

export default { getApps, getAppById, createApp, updateApp, deleteApp, initDatabase };
