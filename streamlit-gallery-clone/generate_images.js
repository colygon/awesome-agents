import db from './db.js';
import axios from 'axios';
import fs from 'fs';
import https from 'https';
import path from 'path';
import { fileURLToPath } from 'url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

// Create images directory if it doesn't exist
const imagesDir = path.join(__dirname, 'public', 'generated-images');
if (!fs.existsSync(imagesDir)) {
  fs.mkdirSync(imagesDir, { recursive: true });
}

// OpenAI API configuration
const OPENAI_API_KEY = process.env.OPENAI_API_KEY;

if (!OPENAI_API_KEY) {
  console.error('Error: OPENAI_API_KEY environment variable is not set.');
  console.error('Please set it with: export OPENAI_API_KEY=your_api_key');
  process.exit(1);
}

// Function to generate a placeholder image URL using a service
// We'll use picsum.photos which provides random placeholder images
function generatePlaceholderImage(app, index) {
  // Use a deterministic seed based on the app ID to get consistent images
  const seed = app.id || index;

  // Return a placeholder image URL
  // You could also use: https://via.placeholder.com/400x300/0066cc/ffffff?text=${encodeURIComponent(app.title)}
  return `https://picsum.photos/seed/${seed}/400/300`;
}

// Function to generate image based on category
function generateCategoryImage(app) {
  const categoryColors = {
    'tools': '4A90E2',      // Blue
    'crews': '7ED321',      // Green
    'flows': 'F5A623',      // Orange
    'integrations': 'BD10E0', // Purple
    'notebooks': '50E3C2',   // Teal
    'streamlit': 'FF6B6B'    // Red
  };

  const color = categoryColors[app.category] || '4A90E2';
  const textColor = 'FFFFFF';

  // Create a nice placeholder with category color and title
  const title = encodeURIComponent(app.title.substring(0, 30));

  return `https://via.placeholder.com/400x300/${color}/${textColor}?text=${title}`;
}

// Function to generate AI image using DALL-E
async function generateAIImage(app) {
  try {
    // Create a descriptive prompt based on the app
    const categoryThemes = {
      'tools': 'professional software tool interface with modern design',
      'crews': 'collaborative team of AI agents working together',
      'flows': 'flowing workflow diagram with connected nodes',
      'integrations': 'connected systems and APIs with data flowing between them',
      'notebooks': 'interactive coding notebook with data visualizations',
      'streamlit': 'modern data science dashboard with charts'
    };

    const categoryTheme = categoryThemes[app.category] || 'modern software application';

    // Create a concise prompt focusing on the essence of the app
    const baseDescription = app.description.substring(0, 100);
    const prompt = `A professional, modern icon or illustration representing ${app.title}. ${baseDescription}. Style: ${categoryTheme}, clean design, vibrant colors, isometric view, digital art style, technology themed`;

    console.log(`  → Generating AI image with DALL-E...`);
    console.log(`     Prompt: ${prompt.substring(0, 80)}...`);

    const response = await axios.post(
      'https://api.openai.com/v1/images/generations',
      {
        model: 'dall-e-3',
        prompt: prompt,
        n: 1,
        size: '1024x1024',
        quality: 'standard',
        style: 'vivid'
      },
      {
        headers: {
          'Authorization': `Bearer ${OPENAI_API_KEY}`,
          'Content-Type': 'application/json'
        },
        timeout: 60000
      }
    );

    if (response.data && response.data.data && response.data.data[0]) {
      const imageUrl = response.data.data[0].url;

      // Download and save the image locally
      const filename = `${app.id}-${app.title.replace(/[^a-z0-9]/gi, '-').toLowerCase()}.png`;
      const localPath = path.join(imagesDir, filename);

      await downloadImage(imageUrl, localPath);

      // Return the local path that will be accessible via /generated-images/
      return `/generated-images/${filename}`;
    }
  } catch (error) {
    console.error(`  ✗ DALL-E error: ${error.message}`);
    if (error.response?.data) {
      console.error(`     API response:`, JSON.stringify(error.response.data).substring(0, 200));
    }
  }

  return null;
}

// Function to download and save image locally
async function downloadImage(url, filepath) {
  return new Promise((resolve, reject) => {
    const file = fs.createWriteStream(filepath);
    https.get(url, (response) => {
      response.pipe(file);
      file.on('finish', () => {
        file.close();
        resolve();
      });
    }).on('error', (err) => {
      fs.unlink(filepath, () => {}); // Delete incomplete file
      reject(err);
    });
  });
}

// Main function to update images
async function updateImages() {
  return new Promise((resolve, reject) => {
    db.all('SELECT * FROM apps WHERE image_url IS NULL OR image_url = ""', async (err, rows) => {
      if (err) {
        reject(err);
        return;
      }

      console.log(`Found ${rows.length} apps without images\n`);

      let updated = 0;
      let errors = 0;

      for (let i = 0; i < rows.length; i++) {
        const app = rows[i];

        try {
          let imageUrl = null;

          console.log(`[${i + 1}/${rows.length}] Processing: ${app.title}`);

          // Generate AI image using DALL-E
          imageUrl = await generateAIImage(app);

          // If AI generation failed, use category-based placeholder
          if (!imageUrl) {
            console.log(`  → Using category-based placeholder as fallback`);
            imageUrl = generateCategoryImage(app);
          }

          // Update database
          await new Promise((resolve, reject) => {
            db.run(
              'UPDATE apps SET image_url = ? WHERE id = ?',
              [imageUrl, app.id],
              (err) => {
                if (err) reject(err);
                else resolve();
              }
            );
          });

          updated++;
          console.log(`  ✓ Updated: ${app.title}\n`);

          // Delay to avoid rate limiting (DALL-E has rate limits)
          await new Promise(resolve => setTimeout(resolve, 1000));

        } catch (error) {
          errors++;
          console.error(`  ✗ Error updating ${app.title}: ${error.message}\n`);
        }
      }

      console.log('\n================================');
      console.log(`Total apps processed: ${rows.length}`);
      console.log(`Successfully updated: ${updated}`);
      console.log(`Errors: ${errors}`);
      console.log('================================\n');

      resolve({ updated, errors });
    });
  });
}

// Run the script
updateImages()
  .then(() => {
    console.log('Image update complete!');
    db.close();
    process.exit(0);
  })
  .catch((error) => {
    console.error('Fatal error:', error);
    db.close();
    process.exit(1);
  });
