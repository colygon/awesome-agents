import db from './db.js';

db.serialize(() => {
  db.run('ALTER TABLE apps ADD COLUMN watchers INTEGER DEFAULT 0');
  db.run('ALTER TABLE apps ADD COLUMN views INTEGER DEFAULT 0');
  db.run('ALTER TABLE apps ADD COLUMN image_url TEXT');
  db.run('ALTER TABLE apps ADD COLUMN created_at DATETIME DEFAULT CURRENT_TIMESTAMP');
  console.log('Schema updated');
});
