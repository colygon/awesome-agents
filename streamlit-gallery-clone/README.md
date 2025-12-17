# streamlit-gallery-clone

A small Next.js app that displays a Streamlit Gallery-style grid backed by a local SQLite DB (`apps.db`).

## Local setup

```zsh
npm install
```

## Sync app listings into SQLite

1) Copy the example config and edit it:

```zsh
cp sync.config.example.json sync.config.json
```

2) (Optional) set a GitHub token to avoid rate limits:

```zsh
export GITHUB_TOKEN="..."
```

3) Sync:

```zsh
npm run sync
```

Notes:
- `streamlit_official_gallery` pulls from `https://streamlit.io/gallery`.
- `streamlit_community_explore` pulls from Streamlit Community Cloud’s public JSON API.
- Add more lists by appending new objects in `sync.config.json` under `feeds` (e.g. `github_repos`).

## Run the web app

```zsh
npm run dev
```

Then open `http://localhost:3000`.
