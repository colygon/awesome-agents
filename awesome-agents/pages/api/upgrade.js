import db from '../../db.js';

export default async function handler(req, res) {
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

  // Note: Background agent spawning is disabled on serverless environments
  // This feature works only in local development
  if (process.env.VERCEL) {
    res.status(501).json({
      error: 'Upgrade feature is not available on serverless deployments',
      message: 'Please run the upgrade locally using the CLI or contact the maintainer',
      github_url,
      appId
    });
    return;
  }

  // For local development only
  try {
    const { spawn } = await import('child_process');
    const path = await import('path');

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
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
}
