import { useState, useEffect } from 'react';

export default function Home() {
  const [apps, setApps] = useState([]);
  const [sortBy, setSortBy] = useState('views');

  useEffect(() => {
    fetch('/api/apps')
      .then(res => res.json())
      .then(data => setApps(data));
  }, []);

  const sortedApps = [...apps].sort((a, b) => {
    if (sortBy === 'views') {
      return b.views - a.views;
    } else if (sortBy === 'recent') {
      return new Date(b.created_at) - new Date(a.created_at);
    }
    return 0;
  });

  return (
    <div>
      <h1>Streamlit Gallery Clone</h1>
      <div style={{ marginBottom: '20px' }}>
        <a href="/submit" style={{ padding: '10px 15px', backgroundColor: '#28a745', color: 'white', textDecoration: 'none', borderRadius: '5px' }}>
          Submit Your App
        </a>
      </div>
      <div className="sort-buttons">
        <button onClick={() => setSortBy('views')}>Sort by Most Viewed</button>
        <button onClick={() => setSortBy('recent')}>Sort by Most Recent</button>
      </div>
      <div className="gallery">
        {sortedApps.map(app => (
          <div key={app.id} className="app">
            <img src={app.image_url} alt={app.title} className="app-image" />
            <h2>{app.title}</h2>
            <p>{app.description}</p>
            <p>Watchers: {app.watchers} | Views: {app.views}</p>
            <a href={app.github_url} target="_blank" rel="noopener noreferrer">GitHub</a>
            {app.tags && <p className="tags">Tags: {app.tags.split(',').map(tag => <span key={tag.trim()} className="tag">{tag.trim()}</span>)}</p>}
          </div>
        ))}
      </div>
    </div>
  );
}
