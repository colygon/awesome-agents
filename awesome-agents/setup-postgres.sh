#!/bin/bash

set -e

echo "=========================================="
echo "Awesome Agents - Vercel Postgres Setup"
echo "=========================================="
echo ""

# Check if we're in the right directory
if [ ! -f "package.json" ]; then
    echo "❌ Error: Must run from awesome-agents directory"
    exit 1
fi

echo "Step 1: Creating Vercel Postgres database..."
echo "Please create the database manually in Vercel Dashboard:"
echo ""
echo "1. Visit: https://vercel.com/dablclub/awesome-agents/stores"
echo "2. Click 'Create Database'"
echo "3. Select 'Postgres'"
echo "4. Name: awesome-agents-db"
echo "5. Region: Washington, D.C., USA (iad1)"
echo "6. Click 'Create'"
echo ""
read -p "Press ENTER when database is created..."

echo ""
echo "Step 2: Pulling environment variables..."
vercel env pull .env.local

if [ ! -f ".env.local" ]; then
    echo "❌ Error: Failed to pull environment variables"
    exit 1
fi

echo "✅ Environment variables pulled"
echo ""

echo "Step 3: Importing data to Postgres..."
node import-to-postgres.js

echo ""
echo "Step 4: Updating API routes..."

# Backup existing SQLite API
if [ -f "pages/api/apps.js" ]; then
    cp pages/api/apps.js pages/api/apps-sqlite.js.backup
    echo "✅ Backed up SQLite API to apps-sqlite.js.backup"
fi

# Replace with Postgres version
cp pages/api/apps-postgres.js pages/api/apps.js
echo "✅ Replaced API route with Postgres version"

echo ""
echo "Step 5: Committing changes..."
git add .
git commit -m "Complete Vercel Postgres migration - persistent storage enabled"
git push origin crewai-upgrade

echo ""
echo "Step 6: Deploying to Vercel..."
vercel --prod --yes

echo ""
echo "=========================================="
echo "✅ Migration Complete!"
echo "=========================================="
echo ""
echo "Your gallery now has persistent storage!"
echo ""
echo "Test it:"
echo "  curl https://awesome-agents-rc5fca3w3-dablclub.vercel.app/api/apps | jq '. | length'"
echo ""
echo "Expected: 425 apps"
echo ""
