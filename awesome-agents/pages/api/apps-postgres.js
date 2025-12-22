import { sql } from '@vercel/postgres';

export default async function handler(req, res) {
  if (req.method === 'GET') {
    const { search, category } = req.query;

    try {
      let query = 'SELECT * FROM apps WHERE 1=1';
      const params = [];
      let paramIndex = 1;

      // Add search filter
      if (search) {
        query += ` AND (title ILIKE $${paramIndex} OR description ILIKE $${paramIndex} OR tags ILIKE $${paramIndex})`;
        params.push(`%${search}%`);
        paramIndex++;
      }

      // Add category filter
      if (category) {
        query += ` AND category = $${paramIndex}`;
        params.push(category);
        paramIndex++;
      }

      query += ' ORDER BY id DESC';

      const result = await sql.query(query, params);
      res.status(200).json(result.rows);
    } catch (error) {
      console.error('Database error:', error);
      res.status(500).json({ error: error.message });
    }
  } else if (req.method === 'POST') {
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
    } = req.body;

    if (!title || !description || !github_url) {
      res.status(400).json({ error: 'Title, description, and GitHub URL are required' });
      return;
    }

    try {
      const result = await sql.query(
        `INSERT INTO apps (title, description, github_url, tags, watchers, views, image_url, has_crewai, category)
         VALUES ($1, $2, $3, $4, $5, $6, $7, $8, $9)
         RETURNING *`,
        [title, description, github_url, tags, watchers, views, image_url, has_crewai, category]
      );

      res.status(201).json(result.rows[0]);
    } catch (error) {
      console.error('Database error:', error);
      res.status(500).json({ error: error.message });
    }
  } else {
    res.setHeader('Allow', ['GET', 'POST']);
    res.status(405).end(`Method ${req.method} Not Allowed`);
  }
}
