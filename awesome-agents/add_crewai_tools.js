import db from './db.js';

// CrewAI Tools data - comprehensive list from the repository
const crewaiTools = [
  // AI & Model Integration
  {
    title: 'Model Context Protocol (MCP) Server Adapter',
    description: 'Integrates with hundreds of MCP servers to access thousands of additional community-built tools',
    github_url: 'https://github.com/crewAIInc/crewAI-tools',
    tags: 'crewai,tools,mcp,integration,protocol',
    category: 'tools'
  },
  {
    title: 'DALL-E Tool',
    description: 'Generate images using OpenAI DALL-E model',
    github_url: 'https://github.com/crewAIInc/crewAI-tools',
    tags: 'crewai,tools,dalle,image-generation,ai',
    category: 'tools'
  },
  {
    title: 'Vision Tool',
    description: 'Computer vision capabilities for image analysis and processing',
    github_url: 'https://github.com/crewAIInc/crewAI-tools',
    tags: 'crewai,tools,vision,image-analysis,ai',
    category: 'tools'
  },
  {
    title: 'AI Mind Tool',
    description: 'AI-powered cognitive processing and reasoning tool',
    github_url: 'https://github.com/crewAIInc/crewAI-tools',
    tags: 'crewai,tools,ai,cognitive,reasoning',
    category: 'tools'
  },
  {
    title: 'Code Interpreter Tool',
    description: 'Secure Python sandbox for executing code with enhanced logging',
    github_url: 'https://github.com/crewAIInc/crewAI-tools',
    tags: 'crewai,tools,code,python,interpreter,sandbox',
    category: 'tools'
  },
  {
    title: 'LlamaIndex Tool',
    description: 'Integration with LlamaIndex for data framework capabilities',
    github_url: 'https://github.com/crewAIInc/crewAI-tools',
    tags: 'crewai,tools,llamaindex,data-framework',
    category: 'tools'
  },

  // RAG (Retrieval Augmented Generation) Tools
  {
    title: 'RAG Adapter',
    description: 'Retrieval Augmented Generation adapter for enhanced AI responses',
    github_url: 'https://github.com/crewAIInc/crewAI-tools',
    tags: 'crewai,tools,rag,retrieval,generation',
    category: 'tools'
  },
  {
    title: 'CrewAI RAG Adapter',
    description: 'Native CrewAI implementation of RAG capabilities',
    github_url: 'https://github.com/crewAIInc/crewAI-tools',
    tags: 'crewai,tools,rag,retrieval,native',
    category: 'tools'
  },

  // Database Tools
  {
    title: 'PostgreSQL Search Tool',
    description: 'Search and query PostgreSQL databases with RAG capabilities',
    github_url: 'https://github.com/crewAIInc/crewAI-tools',
    tags: 'crewai,tools,postgresql,database,search',
    category: 'tools'
  },
  {
    title: 'MySQL Search Tool',
    description: 'Search and query MySQL databases with RAG capabilities',
    github_url: 'https://github.com/crewAIInc/crewAI-tools',
    tags: 'crewai,tools,mysql,database,search',
    category: 'tools'
  },
  {
    title: 'MongoDB Vector Search Tool',
    description: 'Vector search operations in MongoDB with proper serialization',
    github_url: 'https://github.com/crewAIInc/crewAI-tools',
    tags: 'crewai,tools,mongodb,vector-search,database',
    category: 'tools'
  },
  {
    title: 'Qdrant Vector Search Tool',
    description: 'Query and search Qdrant vector database',
    github_url: 'https://github.com/crewAIInc/crewAI-tools',
    tags: 'crewai,tools,qdrant,vector-search,database',
    category: 'tools'
  },
  {
    title: 'Weaviate Tool',
    description: 'Hybrid search capabilities with Weaviate vector database',
    github_url: 'https://github.com/crewAIInc/crewAI-tools',
    tags: 'crewai,tools,weaviate,vector-search,hybrid-search',
    category: 'tools'
  },
  {
    title: 'LanceDB Tool',
    description: 'Integration with LanceDB for vector storage and retrieval',
    github_url: 'https://github.com/crewAIInc/crewAI-tools',
    tags: 'crewai,tools,lancedb,vector-database',
    category: 'tools'
  },
  {
    title: 'Couchbase Tool',
    description: 'Search and query Couchbase NoSQL database',
    github_url: 'https://github.com/crewAIInc/crewAI-tools',
    tags: 'crewai,tools,couchbase,nosql,database',
    category: 'tools'
  },
  {
    title: 'SingleStore Search Tool',
    description: 'Query SingleStore distributed SQL database',
    github_url: 'https://github.com/crewAIInc/crewAI-tools',
    tags: 'crewai,tools,singlestore,sql,database',
    category: 'tools'
  },
  {
    title: 'Snowflake Search Tool',
    description: 'Query and search Snowflake data warehouse',
    github_url: 'https://github.com/crewAIInc/crewAI-tools',
    tags: 'crewai,tools,snowflake,data-warehouse,database',
    category: 'tools'
  },
  {
    title: 'Databricks Query Tool',
    description: 'Execute queries on Databricks platform',
    github_url: 'https://github.com/crewAIInc/crewAI-tools',
    tags: 'crewai,tools,databricks,query,analytics',
    category: 'tools'
  },
  {
    title: 'NL2SQL Tool',
    description: 'Natural language to SQL query conversion',
    github_url: 'https://github.com/crewAIInc/crewAI-tools',
    tags: 'crewai,tools,nl2sql,natural-language,sql',
    category: 'tools'
  },

  // File & Document Tools
  {
    title: 'File Read Tool',
    description: 'Read and extract content from files with start line support',
    github_url: 'https://github.com/crewAIInc/crewAI-tools',
    tags: 'crewai,tools,file,read,io',
    category: 'tools'
  },
  {
    title: 'File Writer Tool',
    description: 'Write content to files with modern Python standards',
    github_url: 'https://github.com/crewAIInc/crewAI-tools',
    tags: 'crewai,tools,file,write,io',
    category: 'tools'
  },
  {
    title: 'Files Compressor Tool',
    description: 'Compress files and subdirectories into archives',
    github_url: 'https://github.com/crewAIInc/crewAI-tools',
    tags: 'crewai,tools,compression,archive,file',
    category: 'tools'
  },
  {
    title: 'Directory Read Tool',
    description: 'Read and list directory contents',
    github_url: 'https://github.com/crewAIInc/crewAI-tools',
    tags: 'crewai,tools,directory,read,filesystem',
    category: 'tools'
  },
  {
    title: 'Directory Search Tool',
    description: 'Search through directory contents with RAG capabilities',
    github_url: 'https://github.com/crewAIInc/crewAI-tools',
    tags: 'crewai,tools,directory,search,rag',
    category: 'tools'
  },
  {
    title: 'PDF Search Tool',
    description: 'Search and extract content from PDF files using RAG',
    github_url: 'https://github.com/crewAIInc/crewAI-tools',
    tags: 'crewai,tools,pdf,search,rag',
    category: 'tools'
  },
  {
    title: 'PDF Text Writing Tool',
    description: 'Write and generate PDF documents with text content',
    github_url: 'https://github.com/crewAIInc/crewAI-tools',
    tags: 'crewai,tools,pdf,write,generation',
    category: 'tools'
  },
  {
    title: 'DOCX Search Tool',
    description: 'Search through Word documents with RAG capabilities',
    github_url: 'https://github.com/crewAIInc/crewAI-tools',
    tags: 'crewai,tools,docx,word,search,rag',
    category: 'tools'
  },
  {
    title: 'CSV Search Tool',
    description: 'Search and query CSV files with native RAG adapter',
    github_url: 'https://github.com/crewAIInc/crewAI-tools',
    tags: 'crewai,tools,csv,search,rag',
    category: 'tools'
  },
  {
    title: 'TXT Search Tool',
    description: 'Search through text files with RAG capabilities',
    github_url: 'https://github.com/crewAIInc/crewAI-tools',
    tags: 'crewai,tools,txt,text,search,rag',
    category: 'tools'
  },
  {
    title: 'JSON Search Tool',
    description: 'Search and query JSON files with RAG adapter',
    github_url: 'https://github.com/crewAIInc/crewAI-tools',
    tags: 'crewai,tools,json,search,rag',
    category: 'tools'
  },
  {
    title: 'XML Search Tool',
    description: 'Search through XML files with RAG capabilities',
    github_url: 'https://github.com/crewAIInc/crewAI-tools',
    tags: 'crewai,tools,xml,search,rag',
    category: 'tools'
  },
  {
    title: 'MDX Search Tool',
    description: 'Search through MDX (Markdown + JSX) files with RAG',
    github_url: 'https://github.com/crewAIInc/crewAI-tools',
    tags: 'crewai,tools,mdx,markdown,search,rag',
    category: 'tools'
  },
  {
    title: 'OCR Tool',
    description: 'Optical Character Recognition for extracting text from images',
    github_url: 'https://github.com/crewAIInc/crewAI-tools',
    tags: 'crewai,tools,ocr,image,text-extraction',
    category: 'tools'
  },

  // Web Scraping & Browsing Tools
  {
    title: 'Scrape Website Tool',
    description: 'Extract content from websites with Embedchain support',
    github_url: 'https://github.com/crewAIInc/crewAI-tools',
    tags: 'crewai,tools,scraping,web,extraction',
    category: 'tools'
  },
  {
    title: 'Scrape Element from Website',
    description: 'Extract specific elements from web pages',
    github_url: 'https://github.com/crewAIInc/crewAI-tools',
    tags: 'crewai,tools,scraping,web,element-extraction',
    category: 'tools'
  },
  {
    title: 'Website Search Tool',
    description: 'Search website content with RAG capabilities',
    github_url: 'https://github.com/crewAIInc/crewAI-tools',
    tags: 'crewai,tools,website,search,rag',
    category: 'tools'
  },
  {
    title: 'Selenium Scraping Tool',
    description: 'Browser-based web scraping with Selenium automation',
    github_url: 'https://github.com/crewAIInc/crewAI-tools',
    tags: 'crewai,tools,selenium,scraping,browser',
    category: 'tools'
  },
  {
    title: 'Browserbase Load Tool',
    description: 'Load and interact with web pages using Browserbase',
    github_url: 'https://github.com/crewAIInc/crewAI-tools',
    tags: 'crewai,tools,browserbase,web,loading',
    category: 'tools'
  },
  {
    title: 'Hyperbrowser Load Tool',
    description: 'Advanced browser automation and loading capabilities',
    github_url: 'https://github.com/crewAIInc/crewAI-tools',
    tags: 'crewai,tools,hyperbrowser,browser,automation',
    category: 'tools'
  },
  {
    title: 'Stagehand Tool',
    description: 'Browser automation and interaction with improved functionality',
    github_url: 'https://github.com/crewAIInc/crewAI-tools',
    tags: 'crewai,tools,stagehand,browser,automation',
    category: 'tools'
  },
  {
    title: 'Firecrawl Scrape Website Tool',
    description: 'Scrape websites using Firecrawl service',
    github_url: 'https://github.com/crewAIInc/crewAI-tools',
    tags: 'crewai,tools,firecrawl,scraping,web',
    category: 'tools'
  },
  {
    title: 'Firecrawl Crawl Website Tool',
    description: 'Crawl entire websites using Firecrawl service',
    github_url: 'https://github.com/crewAIInc/crewAI-tools',
    tags: 'crewai,tools,firecrawl,crawling,web',
    category: 'tools'
  },
  {
    title: 'Firecrawl Search Tool',
    description: 'Search web content using Firecrawl service',
    github_url: 'https://github.com/crewAIInc/crewAI-tools',
    tags: 'crewai,tools,firecrawl,search,web',
    category: 'tools'
  },
  {
    title: 'Jina Scrape Website Tool',
    description: 'Scrape websites using Jina AI service',
    github_url: 'https://github.com/crewAIInc/crewAI-tools',
    tags: 'crewai,tools,jina,scraping,web',
    category: 'tools'
  },
  {
    title: 'Spider Tool',
    description: 'Web spider for crawling and scraping websites',
    github_url: 'https://github.com/crewAIInc/crewAI-tools',
    tags: 'crewai,tools,spider,crawling,scraping',
    category: 'tools'
  },
  {
    title: 'ScrapeGraph Tool',
    description: 'Graph-based web scraping using ScrapeGraph service',
    github_url: 'https://github.com/crewAIInc/crewAI-tools',
    tags: 'crewai,tools,scrapegraph,graph,scraping',
    category: 'tools'
  },
  {
    title: 'Scrapfly Scrape Website Tool',
    description: 'Scrape websites using Scrapfly service',
    github_url: 'https://github.com/crewAIInc/crewAI-tools',
    tags: 'crewai,tools,scrapfly,scraping,web',
    category: 'tools'
  },
  {
    title: 'BrightData Tool',
    description: 'Web scraping with BrightData proxy network',
    github_url: 'https://github.com/crewAIInc/crewAI-tools',
    tags: 'crewai,tools,brightdata,scraping,proxy',
    category: 'tools'
  },
  {
    title: 'Oxylabs Amazon Product Scraper',
    description: 'Scrape Amazon product data using Oxylabs',
    github_url: 'https://github.com/crewAIInc/crewAI-tools',
    tags: 'crewai,tools,oxylabs,amazon,scraping,ecommerce',
    category: 'tools'
  },
  {
    title: 'Oxylabs Amazon Search Scraper',
    description: 'Scrape Amazon search results using Oxylabs',
    github_url: 'https://github.com/crewAIInc/crewAI-tools',
    tags: 'crewai,tools,oxylabs,amazon,search,scraping',
    category: 'tools'
  },
  {
    title: 'Oxylabs Google Search Scraper',
    description: 'Scrape Google search results using Oxylabs',
    github_url: 'https://github.com/crewAIInc/crewAI-tools',
    tags: 'crewai,tools,oxylabs,google,search,scraping',
    category: 'tools'
  },
  {
    title: 'Oxylabs Universal Scraper',
    description: 'Universal web scraping tool using Oxylabs',
    github_url: 'https://github.com/crewAIInc/crewAI-tools',
    tags: 'crewai,tools,oxylabs,universal,scraping',
    category: 'tools'
  },

  // Search & Research Tools
  {
    title: 'Serper API Tool',
    description: 'Web search using Serper API service',
    github_url: 'https://github.com/crewAIInc/crewAI-tools',
    tags: 'crewai,tools,serper,search,api',
    category: 'tools'
  },
  {
    title: 'Serper Scrape Website Tool',
    description: 'Extract clean content from URLs using Serper',
    github_url: 'https://github.com/crewAIInc/crewAI-tools',
    tags: 'crewai,tools,serper,scraping,content',
    category: 'tools'
  },
  {
    title: 'SerpAPI Tool',
    description: 'Search engine results using SerpAPI',
    github_url: 'https://github.com/crewAIInc/crewAI-tools',
    tags: 'crewai,tools,serpapi,search,serp',
    category: 'tools'
  },
  {
    title: 'Serply API Tool',
    description: 'Search capabilities using Serply API',
    github_url: 'https://github.com/crewAIInc/crewAI-tools',
    tags: 'crewai,tools,serply,search,api',
    category: 'tools'
  },
  {
    title: 'EXA Tools',
    description: 'Search and discovery using EXA with base URL configuration',
    github_url: 'https://github.com/crewAIInc/crewAI-tools',
    tags: 'crewai,tools,exa,search,discovery',
    category: 'tools'
  },
  {
    title: 'Brave Search Tool',
    description: 'Privacy-focused search using Brave Search API',
    github_url: 'https://github.com/crewAIInc/crewAI-tools',
    tags: 'crewai,tools,brave,search,privacy',
    category: 'tools'
  },
  {
    title: 'Tavily Search Tool',
    description: 'AI-optimized search using Tavily API',
    github_url: 'https://github.com/crewAIInc/crewAI-tools',
    tags: 'crewai,tools,tavily,search,ai',
    category: 'tools'
  },
  {
    title: 'Tavily Extractor Tool',
    description: 'Extract and structure content using Tavily',
    github_url: 'https://github.com/crewAIInc/crewAI-tools',
    tags: 'crewai,tools,tavily,extraction,content',
    category: 'tools'
  },
  {
    title: 'LinkUp Tool',
    description: 'Link discovery and management capabilities',
    github_url: 'https://github.com/crewAIInc/crewAI-tools',
    tags: 'crewai,tools,linkup,links,discovery',
    category: 'tools'
  },
  {
    title: 'Parallel Search Tool',
    description: 'Execute multiple searches in parallel using Search API v1beta',
    github_url: 'https://github.com/crewAIInc/crewAI-tools',
    tags: 'crewai,tools,parallel,search,concurrent',
    category: 'tools'
  },
  {
    title: 'ArXiv Paper Tool',
    description: 'Search and retrieve academic papers from ArXiv',
    github_url: 'https://github.com/crewAIInc/crewAI-tools',
    tags: 'crewai,tools,arxiv,research,papers',
    category: 'tools'
  },

  // Code & Development Tools
  {
    title: 'Code Docs Search Tool',
    description: 'Search through code documentation with native RAG adapter',
    github_url: 'https://github.com/crewAIInc/crewAI-tools',
    tags: 'crewai,tools,code,docs,search,rag',
    category: 'tools'
  },
  {
    title: 'GitHub Search Tool',
    description: 'Search GitHub repositories and code with RAG',
    github_url: 'https://github.com/crewAIInc/crewAI-tools',
    tags: 'crewai,tools,github,search,code,rag',
    category: 'tools'
  },

  // Cloud & Infrastructure Tools
  {
    title: 'AWS Bedrock Tool',
    description: 'Integration with AWS Bedrock AI services',
    github_url: 'https://github.com/crewAIInc/crewAI-tools',
    tags: 'crewai,tools,aws,bedrock,cloud,ai',
    category: 'tools'
  },
  {
    title: 'AWS S3 Tool',
    description: 'Interact with AWS S3 storage buckets',
    github_url: 'https://github.com/crewAIInc/crewAI-tools',
    tags: 'crewai,tools,aws,s3,storage,cloud',
    category: 'tools'
  },

  // Integration & Automation Tools
  {
    title: 'Zapier Adapter',
    description: 'Integrate with Zapier for workflow automation',
    github_url: 'https://github.com/crewAIInc/crewAI-tools',
    tags: 'crewai,tools,zapier,automation,integration',
    category: 'tools'
  },
  {
    title: 'Zapier Action Tool',
    description: 'Execute Zapier actions and workflows',
    github_url: 'https://github.com/crewAIInc/crewAI-tools',
    tags: 'crewai,tools,zapier,actions,automation',
    category: 'tools'
  },
  {
    title: 'Composio Tool',
    description: 'Integration platform for connecting multiple services',
    github_url: 'https://github.com/crewAIInc/crewAI-tools',
    tags: 'crewai,tools,composio,integration,platform',
    category: 'tools'
  },
  {
    title: 'Apify Actors Tool',
    description: 'Run Apify actors for web automation and scraping',
    github_url: 'https://github.com/crewAIInc/crewAI-tools',
    tags: 'crewai,tools,apify,actors,automation',
    category: 'tools'
  },
  {
    title: 'MultiOn Tool',
    description: 'Browser automation and multi-step web interactions',
    github_url: 'https://github.com/crewAIInc/crewAI-tools',
    tags: 'crewai,tools,multion,browser,automation',
    category: 'tools'
  },

  // ContextualAI Tools
  {
    title: 'ContextualAI Create Agent Tool',
    description: 'Create ContextualAI agents with async functionality',
    github_url: 'https://github.com/crewAIInc/crewAI-tools',
    tags: 'crewai,tools,contextualai,agent,async',
    category: 'tools'
  },
  {
    title: 'ContextualAI Parse Tool',
    description: 'Parse content using ContextualAI with async support',
    github_url: 'https://github.com/crewAIInc/crewAI-tools',
    tags: 'crewai,tools,contextualai,parse,async',
    category: 'tools'
  },
  {
    title: 'ContextualAI Query Tool',
    description: 'Query ContextualAI services with async functionality',
    github_url: 'https://github.com/crewAIInc/crewAI-tools',
    tags: 'crewai,tools,contextualai,query,async',
    category: 'tools'
  },
  {
    title: 'ContextualAI Rerank Tool',
    description: 'Rerank results using ContextualAI with async support',
    github_url: 'https://github.com/crewAIInc/crewAI-tools',
    tags: 'crewai,tools,contextualai,rerank,async',
    category: 'tools'
  },

  // CrewAI Platform Tools
  {
    title: 'CrewAI Enterprise Tools',
    description: 'Enterprise-level tools for CrewAI Platform',
    github_url: 'https://github.com/crewAIInc/crewAI-tools',
    tags: 'crewai,tools,enterprise,platform',
    category: 'tools'
  },
  {
    title: 'CrewAI Platform Tools',
    description: 'Platform tools with schema property handling',
    github_url: 'https://github.com/crewAIInc/crewAI-tools',
    tags: 'crewai,tools,platform,schema',
    category: 'tools'
  },
  {
    title: 'Generate CrewAI Automation Tool',
    description: 'Generate automations for CrewAI Studio',
    github_url: 'https://github.com/crewAIInc/crewAI-tools',
    tags: 'crewai,tools,automation,generation,studio',
    category: 'tools'
  },
  {
    title: 'Invoke CrewAI Automation Tool',
    description: 'Invoke external crew APIs for automation',
    github_url: 'https://github.com/crewAIInc/crewAI-tools',
    tags: 'crewai,tools,automation,invoke,api',
    category: 'tools'
  },

  // Evaluation & Testing Tools
  {
    title: 'Patronus Eval Tool',
    description: 'Evaluate AI outputs using Patronus AI',
    github_url: 'https://github.com/crewAIInc/crewAI-tools',
    tags: 'crewai,tools,patronus,evaluation,testing',
    category: 'tools'
  },

  // Video & Media Tools
  {
    title: 'YouTube Channel Search Tool',
    description: 'Search YouTube channel content with RAG',
    github_url: 'https://github.com/crewAIInc/crewAI-tools',
    tags: 'crewai,tools,youtube,channel,search,rag',
    category: 'tools'
  },
  {
    title: 'YouTube Video Search Tool',
    description: 'Search YouTube video content with RAG capabilities',
    github_url: 'https://github.com/crewAIInc/crewAI-tools',
    tags: 'crewai,tools,youtube,video,search,rag',
    category: 'tools'
  }
];

// Insert all tools into the database
db.serialize(() => {
  const stmt = db.prepare(`
    INSERT INTO apps (title, description, github_url, tags, category)
    VALUES (?, ?, ?, ?, ?)
  `);

  let inserted = 0;
  let errors = 0;

  crewaiTools.forEach((tool) => {
    stmt.run(
      tool.title,
      tool.description,
      tool.github_url,
      tool.tags,
      tool.category,
      function(err) {
        if (err) {
          console.error(`Error inserting ${tool.title}:`, err.message);
          errors++;
        } else {
          inserted++;
          console.log(`✓ Inserted: ${tool.title}`);
        }
      }
    );
  });

  stmt.finalize(() => {
    console.log('\n================================');
    console.log(`Total tools: ${crewaiTools.length}`);
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
