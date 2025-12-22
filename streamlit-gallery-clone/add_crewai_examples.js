import db from './db.js';

// CrewAI Examples data organized by category
const crewaiExamples = [
  // Flows (Advanced Orchestration)
  {
    title: 'Content Creator Flow',
    description: 'Multi-crew content generation system for blogs, LinkedIn posts, and research reports',
    github_url: 'https://github.com/crewAIInc/crewAI-examples',
    tags: 'crewai,flows,content-generation,multi-crew',
    category: 'flows'
  },
  {
    title: 'Email Auto Responder Flow',
    description: 'Automated email monitoring and response generation',
    github_url: 'https://github.com/crewAIInc/crewAI-examples',
    tags: 'crewai,flows,email,automation',
    category: 'flows'
  },
  {
    title: 'Lead Score Flow',
    description: 'Lead qualification with human-in-the-loop review',
    github_url: 'https://github.com/crewAIInc/crewAI-examples',
    tags: 'crewai,flows,sales,lead-scoring',
    category: 'flows'
  },
  {
    title: 'Meeting Assistant Flow',
    description: 'Meeting notes processing with Trello/Slack integration',
    github_url: 'https://github.com/crewAIInc/crewAI-examples',
    tags: 'crewai,flows,meetings,productivity,trello,slack',
    category: 'flows'
  },
  {
    title: 'Self Evaluation Loop Flow',
    description: 'Iterative content improvement with self-review',
    github_url: 'https://github.com/crewAIInc/crewAI-examples',
    tags: 'crewai,flows,self-evaluation,content-improvement',
    category: 'flows'
  },
  {
    title: 'Write a Book with Flows',
    description: 'Automated book writing with parallel chapter generation',
    github_url: 'https://github.com/crewAIInc/crewAI-examples',
    tags: 'crewai,flows,writing,book-generation',
    category: 'flows'
  },

  // Crews - Content Creation & Marketing
  {
    title: 'Game Builder Crew',
    description: 'Multi-agent team that designs and builds Python games',
    github_url: 'https://github.com/crewAIInc/crewAI-examples',
    tags: 'crewai,crews,game-development,python',
    category: 'crews'
  },
  {
    title: 'Instagram Post Creator',
    description: 'Creative social media content generation',
    github_url: 'https://github.com/crewAIInc/crewAI-examples',
    tags: 'crewai,crews,social-media,instagram,content-creation',
    category: 'crews'
  },
  {
    title: 'Landing Page Generator',
    description: 'Full landing page creation from concepts',
    github_url: 'https://github.com/crewAIInc/crewAI-examples',
    tags: 'crewai,crews,web-development,landing-pages,marketing',
    category: 'crews'
  },
  {
    title: 'Marketing Strategy Crew',
    description: 'Comprehensive marketing campaign development',
    github_url: 'https://github.com/crewAIInc/crewAI-examples',
    tags: 'crewai,crews,marketing,strategy,campaigns',
    category: 'crews'
  },
  {
    title: 'Screenplay Writer',
    description: 'Convert text/emails into screenplay format',
    github_url: 'https://github.com/crewAIInc/crewAI-examples',
    tags: 'crewai,crews,writing,screenplay,creative',
    category: 'crews'
  },

  // Crews - Business & Productivity
  {
    title: 'Job Posting Creator',
    description: 'Automated job description creation',
    github_url: 'https://github.com/crewAIInc/crewAI-examples',
    tags: 'crewai,crews,hr,recruitment,job-descriptions',
    category: 'crews'
  },
  {
    title: 'Prep for a Meeting',
    description: 'Meeting preparation research and strategy',
    github_url: 'https://github.com/crewAIInc/crewAI-examples',
    tags: 'crewai,crews,meetings,preparation,research',
    category: 'crews'
  },
  {
    title: 'Recruitment Crew',
    description: 'Automated candidate sourcing and evaluation',
    github_url: 'https://github.com/crewAIInc/crewAI-examples',
    tags: 'crewai,crews,hr,recruitment,hiring',
    category: 'crews'
  },
  {
    title: 'Stock Analysis Crew',
    description: 'Financial analysis with SEC data integration',
    github_url: 'https://github.com/crewAIInc/crewAI-examples',
    tags: 'crewai,crews,finance,stock-analysis,sec',
    category: 'crews'
  },

  // Crews - Data & Research
  {
    title: 'Industry Agents',
    description: 'Industry-specific agent implementations',
    github_url: 'https://github.com/crewAIInc/crewAI-examples',
    tags: 'crewai,crews,industry,specialized-agents',
    category: 'crews'
  },
  {
    title: 'Match Profile to Positions',
    description: 'CV-to-job matching with vector search',
    github_url: 'https://github.com/crewAIInc/crewAI-examples',
    tags: 'crewai,crews,recruitment,cv-matching,vector-search',
    category: 'crews'
  },
  {
    title: 'Meta Quest Knowledge',
    description: 'PDF-based Q&A system',
    github_url: 'https://github.com/crewAIInc/crewAI-examples',
    tags: 'crewai,crews,pdf,qa,knowledge-base',
    category: 'crews'
  },
  {
    title: 'Markdown Validator',
    description: 'Automated markdown validation and correction',
    github_url: 'https://github.com/crewAIInc/crewAI-examples',
    tags: 'crewai,crews,markdown,validation,documentation',
    category: 'crews'
  },

  // Crews - Travel & Planning
  {
    title: 'Surprise Trip Planner',
    description: 'Personalized surprise travel planning',
    github_url: 'https://github.com/crewAIInc/crewAI-examples',
    tags: 'crewai,crews,travel,planning,surprise',
    category: 'crews'
  },
  {
    title: 'Trip Planner',
    description: 'Destination comparison and itinerary optimization',
    github_url: 'https://github.com/crewAIInc/crewAI-examples',
    tags: 'crewai,crews,travel,planning,itinerary',
    category: 'crews'
  },

  // Crews - Templates
  {
    title: 'Starter Template',
    description: 'Basic template for new CrewAI projects',
    github_url: 'https://github.com/crewAIInc/crewAI-examples',
    tags: 'crewai,crews,template,starter',
    category: 'crews'
  },

  // Integrations
  {
    title: 'CrewAI-LangGraph Integration',
    description: 'Integration with LangGraph framework',
    github_url: 'https://github.com/crewAIInc/crewAI-examples',
    tags: 'crewai,integrations,langgraph,framework',
    category: 'integrations'
  },
  {
    title: 'Azure Model Integration',
    description: 'Using CrewAI with Azure OpenAI',
    github_url: 'https://github.com/crewAIInc/crewAI-examples',
    tags: 'crewai,integrations,azure,openai',
    category: 'integrations'
  },
  {
    title: 'NVIDIA Models Integration',
    description: 'Integration with NVIDIA AI ecosystem',
    github_url: 'https://github.com/crewAIInc/crewAI-examples',
    tags: 'crewai,integrations,nvidia,models',
    category: 'integrations'
  },

  // Notebooks
  {
    title: 'CrewAI Jupyter Notebooks',
    description: 'Interactive Jupyter notebook examples for exploring CrewAI features',
    github_url: 'https://github.com/crewAIInc/crewAI-examples',
    tags: 'crewai,notebooks,jupyter,tutorial',
    category: 'notebooks'
  }
];

// Insert all examples into the database
db.serialize(() => {
  const stmt = db.prepare(`
    INSERT INTO apps (title, description, github_url, tags, category)
    VALUES (?, ?, ?, ?, ?)
  `);

  let inserted = 0;
  let errors = 0;

  crewaiExamples.forEach((example) => {
    stmt.run(
      example.title,
      example.description,
      example.github_url,
      example.tags,
      example.category,
      function(err) {
        if (err) {
          console.error(`Error inserting ${example.title}:`, err.message);
          errors++;
        } else {
          inserted++;
          console.log(`✓ Inserted: ${example.title} (${example.category})`);
        }
      }
    );
  });

  stmt.finalize(() => {
    console.log('\n================================');
    console.log(`Total examples: ${crewaiExamples.length}`);
    console.log(`Successfully inserted: ${inserted}`);
    console.log(`Errors: ${errors}`);
    console.log('================================\n');

    // Show category breakdown
    db.all(`
      SELECT category, COUNT(*) as count
      FROM apps
      GROUP BY category
      ORDER BY count DESC
    `, [], (err, rows) => {
      if (err) {
        console.error('Error getting category counts:', err.message);
      } else {
        console.log('Apps by category:');
        rows.forEach((row) => {
          console.log(`  ${row.category}: ${row.count}`);
        });
      }
      db.close();
    });
  });
});
