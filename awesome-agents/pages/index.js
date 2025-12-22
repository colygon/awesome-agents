import { useState, useEffect } from 'react';

export default function Home() {
  const [apps, setApps] = useState([]);
  const [sortBy, setSortBy] = useState('views');
  const [searchQuery, setSearchQuery] = useState('');
  const [selectedCategory, setSelectedCategory] = useState('');
  const [categories, setCategories] = useState([]);
  const [showCrewAIOnly, setShowCrewAIOnly] = useState(false);
  const [upgradingApps, setUpgradingApps] = useState(new Set());

  useEffect(() => {
    // Build query parameters
    const params = new URLSearchParams();
    if (searchQuery) params.append('search', searchQuery);
    if (selectedCategory) params.append('category', selectedCategory);

    const queryString = params.toString();
    const url = queryString ? `/api/apps?${queryString}` : '/api/apps';

    fetch(url)
      .then(res => res.json())
      .then(data => {
        setApps(data);

        // Extract unique categories
        const uniqueCategories = [...new Set(data.map(app => app.category).filter(Boolean))];
        setCategories(uniqueCategories.sort());
      });
  }, [searchQuery, selectedCategory]);

  const filteredApps = showCrewAIOnly ? apps.filter(app => app.has_crewai === 1) : apps;

  const sortedApps = [...filteredApps].sort((a, b) => {
    if (sortBy === 'views') {
      return b.views - a.views;
    } else if (sortBy === 'recent') {
      return new Date(b.created_at) - new Date(a.created_at);
    }
    return 0;
  });

  const handleUpgrade = async (app) => {
    setUpgradingApps(prev => new Set(prev).add(app.id));

    try {
      const response = await fetch('/api/upgrade', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          appId: app.id,
          title: app.title,
          github_url: app.github_url,
          category: app.category
        })
      });

      const data = await response.json();

      if (!response.ok) {
        if (response.status === 501) {
          alert(`Upgrade feature is not available on this deployment.\n\nTo upgrade "${app.title}":\n1. Clone the repository: ${app.github_url}\n2. Run the upgrade locally\n3. Submit a PR to the gallery`);
        } else {
          throw new Error(data.error || 'Upgrade request failed');
        }
      } else {
        alert(`Upgrade agent launched for "${app.title}"! The upgrade will happen in the background.`);
      }
    } catch (error) {
      console.error('Upgrade error:', error);
      alert(`Failed to launch upgrade agent: ${error.message}`);
    } finally {
      setUpgradingApps(prev => {
        const next = new Set(prev);
        next.delete(app.id);
        return next;
      });
    }
  };

  return (
    <div>
      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '30px' }}>
        <h1 style={{ margin: 0 }}>Awesome Agents</h1>
        <a href="/submit" style={{
          padding: '12px 24px',
          backgroundColor: '#28a745',
          color: 'white',
          textDecoration: 'none',
          borderRadius: '8px',
          fontWeight: 'bold',
          boxShadow: '0 2px 4px rgba(0,0,0,0.1)',
          transition: 'all 0.2s',
          cursor: 'pointer'
        }}>
          + Submit Your App
        </a>
      </div>

      {/* Search and Filter Section */}
      <div style={{ marginBottom: '20px', display: 'flex', gap: '10px', flexWrap: 'wrap', alignItems: 'center' }}>
        <input
          type="text"
          placeholder="Search apps by title, description, or tags..."
          value={searchQuery}
          onChange={(e) => setSearchQuery(e.target.value)}
          style={{
            flex: '1',
            minWidth: '300px',
            padding: '10px',
            fontSize: '16px',
            border: '2px solid #ddd',
            borderRadius: '5px'
          }}
        />
        <select
          value={selectedCategory}
          onChange={(e) => setSelectedCategory(e.target.value)}
          style={{
            padding: '10px',
            fontSize: '16px',
            border: '2px solid #ddd',
            borderRadius: '5px',
            minWidth: '150px'
          }}
        >
          <option value="">All Categories</option>
          {categories.map(cat => (
            <option key={cat} value={cat}>{cat}</option>
          ))}
        </select>
        {(searchQuery || selectedCategory) && (
          <button
            onClick={() => {
              setSearchQuery('');
              setSelectedCategory('');
            }}
            style={{
              padding: '10px 15px',
              backgroundColor: '#dc3545',
              color: 'white',
              border: 'none',
              borderRadius: '5px',
              cursor: 'pointer'
            }}
          >
            Clear Filters
          </button>
        )}
      </div>

      <div className="sort-buttons" style={{ display: 'flex', gap: '10px', alignItems: 'center', flexWrap: 'wrap' }}>
        <button onClick={() => setSortBy('views')}>Sort by Most Viewed</button>
        <button onClick={() => setSortBy('recent')}>Sort by Most Recent</button>
        <button
          onClick={() => setShowCrewAIOnly(!showCrewAIOnly)}
          style={{
            backgroundColor: showCrewAIOnly ? '#28a745' : '#6c757d',
            color: 'white',
            padding: '10px 15px',
            border: 'none',
            borderRadius: '5px',
            cursor: 'pointer',
            fontWeight: 'bold'
          }}
        >
          {showCrewAIOnly ? '🤖 Showing CrewAI Apps' : '🤖 Show CrewAI Apps Only'}
        </button>
      </div>

      {/* Results count */}
      <div style={{ marginBottom: '15px', color: '#666' }}>
        Showing {sortedApps.length} app{sortedApps.length !== 1 ? 's' : ''}
        {selectedCategory && ` in "${selectedCategory}"`}
        {searchQuery && ` matching "${searchQuery}"`}
      </div>
      <div className="gallery">
        {sortedApps.map(app => (
          <div key={app.id} className="app">
            <img src={app.image_url} alt={app.title} className="app-image" />
            <div style={{ display: 'flex', gap: '8px', marginBottom: '8px', flexWrap: 'wrap' }}>
              {app.category && (
                <span style={{
                  display: 'inline-block',
                  padding: '4px 8px',
                  backgroundColor: '#007bff',
                  color: 'white',
                  borderRadius: '3px',
                  fontSize: '12px'
                }}>
                  {app.category}
                </span>
              )}
              {app.has_crewai === 1 && (
                <span style={{
                  display: 'inline-block',
                  padding: '4px 8px',
                  backgroundColor: '#28a745',
                  color: 'white',
                  borderRadius: '3px',
                  fontSize: '12px',
                  fontWeight: 'bold',
                  boxShadow: '0 2px 4px rgba(0,0,0,0.1)'
                }}>
                  🤖 CrewAI
                </span>
              )}
            </div>
            <h2>{app.title}</h2>
            <p>{app.description}</p>
            <p>Watchers: {app.watchers} | Views: {app.views}</p>
            <a href={app.github_url} target="_blank" rel="noopener noreferrer">GitHub</a>
            {app.has_crewai !== 1 && (
              <button
                onClick={() => handleUpgrade(app)}
                disabled={upgradingApps.has(app.id)}
                style={{
                  marginTop: '10px',
                  padding: '8px 16px',
                  backgroundColor: upgradingApps.has(app.id) ? '#6c757d' : '#ff6b6b',
                  color: 'white',
                  border: 'none',
                  borderRadius: '5px',
                  cursor: upgradingApps.has(app.id) ? 'not-allowed' : 'pointer',
                  fontWeight: 'bold',
                  width: '100%',
                  fontSize: '14px'
                }}
              >
                {upgradingApps.has(app.id) ? '⏳ Upgrading...' : '⚡ Upgrade to CrewAI'}
              </button>
            )}
            {app.tags && <p className="tags">Tags: {app.tags.split(',').map(tag => <span key={tag.trim()} className="tag">{tag.trim()}</span>)}</p>}
          </div>
        ))}
      </div>
    </div>
  );
}
