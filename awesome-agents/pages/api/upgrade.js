import { spawn } from 'child_process';
import path from 'path';
import db from '../../db.js';

export default function handler(req, res) {
  if (req.method !== 'POST') {
    res.setHeader('Allow', ['POST']);
    res.status(405).end(`Method ${req.method} Not Allowed`);
    return;
  }

  const { appId, title, github_url, category } = req.body;

  if (!appId || !github_url) {
    res.status(400).json({ error: 'App ID and GitHub URL are required' });
    return;
  }

  // Launch an upgrade agent in the background
  const agentProcess = spawn('node', [
    path.join(process.cwd(), 'upgrade-agent.js'),
    '--appId', String(appId),
    '--githubUrl', github_url,
    '--title', title || 'Untitled',
    '--category', category || 'unknown'
  ], {
    detached: true,
    stdio: 'ignore'
  });

  agentProcess.unref();

  // Mark the app as "upgrading" in the database
  db.run(
    'UPDATE apps SET tags = CASE WHEN tags IS NULL OR tags = "" THEN "upgrading" ELSE tags || ", upgrading" END WHERE id = ?',
    [appId],
    function(err) {
      if (err) {
        res.status(500).json({ error: err.message });
        return;
      }
      res.status(200).json({
        message: 'Upgrade agent launched successfully',
        appId,
        status: 'upgrading'
      });
    }
  );
}
