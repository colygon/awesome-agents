# Deployment Guide for Awesome Agents

## Deploying to Vercel

### Important: Database Consideration

This application uses SQLite, which is **not recommended for production on Vercel** because:
- Serverless functions are stateless
- Each function invocation gets a fresh filesystem
- The `/tmp` directory is ephemeral

### Recommended Production Setup

For a production deployment, you should migrate to a hosted database:

#### Option 1: Vercel Postgres (Recommended)
```bash
npm install @vercel/postgres
```

#### Option 2: PlanetScale (MySQL)
```bash
npm install @planetscale/database
```

#### Option 3: Neon (Serverless Postgres)
```bash
npm install @neondatabase/serverless
```

### Deploy to Vercel (Development/Demo)

1. **Install Vercel CLI:**
```bash
npm install -g vercel
```

2. **Login to Vercel:**
```bash
vercel login
```

3. **Deploy:**
```bash
vercel --prod
```

### Environment Variables

No environment variables are required for the demo version.

For production with a hosted database, you'll need:
- `DATABASE_URL` - Your database connection string

### Post-Deployment

After deploying, you'll need to populate the database. Since Vercel uses ephemeral storage, the database will reset on each deployment.

**Options:**
1. **Migrate to a hosted database** (recommended)
2. **Pre-populate on each cold start** (add initialization code)
3. **Use as a static site** (generate at build time)

### Build Configuration

The project is configured with:
- Framework: Next.js
- Node Version: 18.x or higher
- Build Command: `npm run build`
- Output Directory: `.next`

### Limitations of SQLite on Vercel

- ❌ Data persists only during function execution
- ❌ Each region gets its own database
- ❌ Database resets on redeployment
- ✅ Works for development/demo purposes
- ✅ Great for testing

### Migration Path

To migrate from SQLite to a production database:

1. Export your SQLite data:
```bash
sqlite3 apps.db .dump > apps.sql
```

2. Convert to your target database format

3. Update `db.js` to use your new database client

4. Update API routes to use the new connection

### Local Development

```bash
# Install dependencies
npm install

# Populate database
npm run sync

# Run development server
npm run dev
```

Then open http://localhost:3000

### Alternative: Static Export

For a completely static version:

1. Update `next.config.js`:
```js
export default {
  output: 'export',
  images: {
    unoptimized: true
  }
};
```

2. Pre-generate all data at build time
3. Deploy static files to Vercel, Netlify, or Cloudflare Pages

## GitHub Integration

The repository is already set up with:
- GitHub: https://github.com/colygon/awesome-agents
- Branch: crewai-upgrade

To keep deploying:
```bash
git push origin crewai-upgrade
```

Vercel will automatically redeploy on push if you've set up the integration.
