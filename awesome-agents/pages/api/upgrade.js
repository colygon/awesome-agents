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

  // Note: Upgrade feature is not available on Vercel serverless deployments
  // This feature only works in local development environments
  res.status(501).json({
    error: 'Upgrade feature is not available on serverless deployments',
    message: 'This feature requires a stateful server environment. To upgrade an app, please run the gallery locally or contact the maintainer.',
    github_url,
    appId,
    instructions: {
      step1: `Clone the repository: ${github_url}`,
      step2: 'Run the upgrade script locally',
      step3: 'Submit a pull request with your CrewAI implementation'
    }
  });
}
