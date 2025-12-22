import db from '../../db.js';

export default function handler(req, res) {
  if (req.method === 'GET') {
    const { search, category } = req.query;

    let query = 'SELECT * FROM apps WHERE 1=1';
    const params = [];

    // Add search filter
    if (search) {
      query += ' AND (title LIKE ? OR description LIKE ? OR tags LIKE ?)';
      const searchPattern = `%${search}%`;
      params.push(searchPattern, searchPattern, searchPattern);
    }

    // Add category filter
    if (category) {
      query += ' AND category = ?';
      params.push(category);
    }

    query += ' ORDER BY id DESC';

    db.all(query, params, (err, rows) => {
      if (err) {
        res.status(500).json({ error: err.message });
        return;
      }
      res.status(200).json(rows);
    });
  } else if (req.method === 'POST') {
    const { title, description, github_url, tags, watchers = 0, views = 0, image_url = '', has_crewai = 0 } = req.body;
    if (!title || !description || !github_url) {
      res.status(400).json({ error: 'Title, description, and GitHub URL are required' });
      return;
    }
    db.run('INSERT INTO apps (title, description, github_url, tags, watchers, views, image_url, has_crewai) VALUES (?, ?, ?, ?, ?, ?, ?, ?)',
      [title, description, github_url, tags, watchers, views, image_url, has_crewai], function(err) {
        if (err) {
          res.status(500).json({ error: err.message });
          return;
        }
        res.status(201).json({ id: this.lastID });
      });
  } else {
    res.setHeader('Allow', ['GET', 'POST']);
    res.status(405).end(`Method ${req.method} Not Allowed`);
  }
}
