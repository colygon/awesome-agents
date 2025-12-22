# Setting Up Vercel Postgres for Awesome Agents

This guide will help you migrate from SQLite to Vercel Postgres for persistent data storage.

## Step 1: Create Vercel Postgres Database

### Via Vercel Dashboard (Recommended)

1. Go to https://vercel.com/dablclub/awesome-agents
2. Click on the "Storage" tab
3. Click "Create Database"
4. Select "Postgres"
5. Name it: `awesome-agents-db`
6. Region: `Washington, D.C., USA (iad1)` (same as your deployment)
7. Click "Create"

The database will be created and environment variables will be automatically added to your project.

### Via Vercel CLI

```bash
cd /Users/colinlowenberg/crew/awesome-agents
vercel postgres create awesome-agents-db --region iad1
```

## Step 2: Pull Environment Variables Locally

```bash
cd /Users/colinlowenberg/crew/awesome-agents
vercel env pull .env.local
```

This creates `.env.local` with your Postgres connection strings.

## Step 3: Import Data to Postgres

```bash
# Make sure you have the .env.local file with POSTGRES_URL
node import-to-postgres.js
```

This will:
- Create the `apps` table
- Import all 425 apps from the SQLite export
- Update the sequence for auto-increment IDs

## Step 4: Update API Routes

Rename the Postgres API file to replace the SQLite version:

```bash
mv pages/api/apps.js pages/api/apps-sqlite.js.backup
mv pages/api/apps-postgres.js pages/api/apps.js
```

## Step 5: Deploy to Vercel

```bash
git add .
git commit -m "Migrate to Vercel Postgres for persistent storage"
git push origin crewai-upgrade
vercel --prod
```

## Verification

After deployment, verify the migration:

```bash
# Test the API
curl https://awesome-agents-rc5fca3w3-dablclub.vercel.app/api/apps | jq '. | length'

# Should return: 425
```

## Environment Variables

The following environment variables are automatically set by Vercel Postgres:

- `POSTGRES_URL` - Main connection string (pooled)
- `POSTGRES_PRISMA_URL` - For Prisma ORM (if using)
- `POSTGRES_URL_NON_POOLING` - Direct connection (for migrations)
- `POSTGRES_USER` - Database user
- `POSTGRES_HOST` - Database host
- `POSTGRES_PASSWORD` - Database password
- `POSTGRES_DATABASE` - Database name

## File Changes

### New Files Created
- `db-postgres.js` - Postgres database module
- `export-sqlite-data.js` - Export script
- `import-to-postgres.js` - Import script
- `apps-export.json` - Exported data (JSON)
- `apps-export.sql` - Exported data (SQL)
- `pages/api/apps-postgres.js` - New Postgres API

### Files to Update
- `pages/api/apps.js` - Replace with Postgres version
- `.gitignore` - Add `.env.local` and export files

## Benefits of Postgres

✅ **Persistent Storage** - Data survives deployments
✅ **Scalable** - Handles millions of rows
✅ **ACID Compliant** - Reliable transactions
✅ **Full-Text Search** - Built-in search capabilities
✅ **Indexes** - Fast queries
✅ **Backups** - Automatic backups by Vercel
✅ **Connection Pooling** - Efficient for serverless

## Database Schema

```sql
CREATE TABLE apps (
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
);
```

## Troubleshooting

### Error: "relation apps does not exist"

Run the import script to create the table:
```bash
node import-to-postgres.js
```

### Error: "No environment variables"

Pull the environment variables from Vercel:
```bash
vercel env pull .env.local
```

### Error: "Connection timeout"

Check if the Postgres database is running in the Vercel dashboard.

## Rollback to SQLite

If you need to rollback:

```bash
mv pages/api/apps-sqlite.js.backup pages/api/apps.js
git add pages/api/apps.js
git commit -m "Rollback to SQLite"
git push origin crewai-upgrade
vercel --prod
```

## Next Steps

After migration:
1. ✅ Verify all 425 apps are accessible
2. ✅ Test search and filter functionality
3. ✅ Test POST endpoint (submit new app)
4. ⚠️ Remove SQLite database file from deployments
5. ⚠️ Update `.gitignore` to exclude `.env.local`

## Cost

Vercel Postgres pricing (as of 2024):
- **Hobby**: Free tier available (limited)
- **Pro**: $0.03/hour for compute + $0.50/GB storage
- **Enterprise**: Custom pricing

Your gallery (425 apps) should fit comfortably in the free tier initially.

## Support

- Vercel Postgres Docs: https://vercel.com/docs/storage/vercel-postgres
- Vercel Dashboard: https://vercel.com/dablclub/awesome-agents/stores

---

**Ready to migrate?** Follow the steps above in order for a smooth transition!
