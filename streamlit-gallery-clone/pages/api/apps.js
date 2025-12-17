import db from '../../db.js';

export default function handler(req, res) {
  if (req.method === 'GET') {
    db.all('SELECT * FROM apps ORDER BY id DESC', (err, rows) => {
      if (err) {
        res.status(500).json({ error: err.message });
        return;
      }
      res.status(200).json(rows);
    });
  } else if (req.method === 'POST') {
    const { title, description, github_url, tags, watchers = 0, views = 0, image_url = '' } = req.body;
    if (!title || !description || !github_url) {
      res.status(400).json({ error: 'Title, description, and GitHub URL are required' });
      return;
    }
    db.run('INSERT INTO apps (title, description, github_url, tags, watchers, views, image_url) VALUES (?, ?, ?, ?, ?, ?, ?)',
      [title, description, github_url, tags, watchers, views, image_url], function(err) {
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
