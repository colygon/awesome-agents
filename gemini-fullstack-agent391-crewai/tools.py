"""
Gemini Fullstack Multi-Agent System - CrewAI Tools
Tools for frontend, backend, database, and integration development.
"""

from crewai_tools import tool
from typing import Dict, List

# ============================================================================
# FRONTEND DEVELOPMENT TOOLS
# ============================================================================

@tool("UI Generator Tool")
def ui_generator_tool(requirements: str, framework: str = "React") -> str:
    """
    Generate user interface code based on requirements and chosen framework.

    Args:
        requirements: Description of the UI requirements
        framework: Frontend framework (React, Vue, Angular, Svelte)

    Returns:
        Generated UI code
    """
    template = f"""
// Generated {framework} Component
import React, {{ useState, useEffect }} from 'react';
import './styles.css';

const {requirements.split()[0].title()}Component = () => {{
  const [data, setData] = useState([]);
  const [loading, setLoading] = useState(false);

  useEffect(() => {{
    // Fetch data from API
    fetchData();
  }}, []);

  const fetchData = async () => {{
    setLoading(true);
    try {{
      const response = await fetch('/api/data');
      const result = await response.json();
      setData(result);
    }} catch (error) {{
      console.error('Error fetching data:', error);
    }} finally {{
      setLoading(false);
    }}
  }};

  return (
    <div className="container">
      <h1>{requirements}</h1>
      {{loading ? (
        <div>Loading...</div>
      ) : (
        <div className="content">
          {{/* Component content based on requirements */}}
        </div>
      )}}
    </div>
  );
}};

export default {requirements.split()[0].title()}Component;
"""
    return template


@tool("Component Creator Tool")
def component_creator_tool(component_name: str, component_type: str) -> str:
    """
    Create reusable component templates.

    Args:
        component_name: Name of the component
        component_type: Type (button, form, card, modal, etc.)

    Returns:
        Component code template
    """
    templates = {
        "button": "// Reusable Button Component\nconst Button = ({ onClick, children, variant = 'primary' }) => (\n  <button className={`btn btn-${variant}`} onClick={onClick}>\n    {children}\n  </button>\n);",
        "form": "// Reusable Form Component\nconst Form = ({ onSubmit, fields }) => (\n  <form onSubmit={onSubmit}>\n    {fields.map(field => (\n      <input key={field.name} name={field.name} type={field.type} placeholder={field.placeholder} />\n    ))}\n    <button type='submit'>Submit</button>\n  </form>\n);",
        "card": "// Reusable Card Component\nconst Card = ({ title, content, image }) => (\n  <div className='card'>\n    {image && <img src={image} alt={title} />}\n    <h3>{title}</h3>\n    <p>{content}</p>\n  </div>\n);"
    }

    return templates.get(component_type.lower(), f"// {component_name} Component\nconst {component_name} = () => <div>{component_name}</div>;")


@tool("CSS Styling Tool")
def css_styling_tool(component: str, design_system: str = "modern") -> str:
    """
    Generate CSS styles for components.

    Args:
        component: Component to style
        design_system: Design system (modern, classic, minimal)

    Returns:
        CSS styles
    """
    styles = f"""
/* Styles for {component} */
.container {{
  max-width: 1200px;
  margin: 0 auto;
  padding: 2rem;
}}

.btn {{
  padding: 0.75rem 1.5rem;
  border: none;
  border-radius: 0.5rem;
  cursor: pointer;
  font-weight: 600;
  transition: all 0.3s ease;
}}

.btn-primary {{
  background-color: #3b82f6;
  color: white;
}}

.btn-primary:hover {{
  background-color: #2563eb;
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(59, 130, 246, 0.3);
}}

.card {{
  background: white;
  border-radius: 0.75rem;
  padding: 1.5rem;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}}

.card:hover {{
  transform: translateY(-4px);
  box-shadow: 0 8px 24px rgba(0, 0, 0, 0.15);
}}

/* Responsive design */
@media (max-width: 768px) {{
  .container {{
    padding: 1rem;
  }}
}}
"""
    return styles


@tool("Accessibility Checker Tool")
def accessibility_checker_tool(component_code: str) -> str:
    """
    Check component for accessibility issues.

    Args:
        component_code: Component code to check

    Returns:
        Accessibility report
    """
    issues = []
    recommendations = []

    if "alt=" not in component_code and "<img" in component_code:
        issues.append("Missing alt attributes on images")
        recommendations.append("Add descriptive alt text to all images")

    if "aria-" not in component_code:
        issues.append("No ARIA attributes found")
        recommendations.append("Add appropriate ARIA labels for screen readers")

    if "role=" not in component_code and "button" not in component_code.lower():
        recommendations.append("Consider adding role attributes for semantic clarity")

    report = "Accessibility Report:\n"
    if issues:
        report += "\nIssues Found:\n" + "\n".join(f"- {issue}" for issue in issues)
    if recommendations:
        report += "\n\nRecommendations:\n" + "\n".join(f"- {rec}" for rec in recommendations)
    if not issues:
        report += "\n✓ No critical accessibility issues found!"

    return report


# ============================================================================
# BACKEND DEVELOPMENT TOOLS
# ============================================================================

@tool("API Generator Tool")
def api_generator_tool(resource: str, methods: str = "GET,POST,PUT,DELETE") -> str:
    """
    Generate RESTful API endpoints for a resource.

    Args:
        resource: Resource name (e.g., users, products, orders)
        methods: HTTP methods to support (comma-separated)

    Returns:
        API endpoint code
    """
    code = f"""
// {resource.title()} API Endpoints
const express = require('express');
const router = express.Router();

// GET all {resource}
router.get('/{resource}', async (req, res) => {{
  try {{
    const {resource} = await db.{resource}.findAll();
    res.json({{ success: true, data: {resource} }});
  }} catch (error) {{
    res.status(500).json({{ success: false, error: error.message }});
  }}
}});

// GET single {resource.rstrip('s')}
router.get('/{resource}/:id', async (req, res) => {{
  try {{
    const item = await db.{resource}.findById(req.params.id);
    if (!item) return res.status(404).json({{ success: false, error: 'Not found' }});
    res.json({{ success: true, data: item }});
  }} catch (error) {{
    res.status(500).json({{ success: false, error: error.message }});
  }}
}});

// POST create {resource.rstrip('s')}
router.post('/{resource}', async (req, res) => {{
  try {{
    const new{resource.rstrip('s').title()} = await db.{resource}.create(req.body);
    res.status(201).json({{ success: true, data: new{resource.rstrip('s').title()} }});
  }} catch (error) {{
    res.status(400).json({{ success: false, error: error.message }});
  }}
}});

// PUT update {resource.rstrip('s')}
router.put('/{resource}/:id', async (req, res) => {{
  try {{
    const updated = await db.{resource}.update(req.params.id, req.body);
    res.json({{ success: true, data: updated }});
  }} catch (error) {{
    res.status(400).json({{ success: false, error: error.message }});
  }}
}});

// DELETE {resource.rstrip('s')}
router.delete('/{resource}/:id', async (req, res) => {{
  try {{
    await db.{resource}.delete(req.params.id);
    res.json({{ success: true, message: 'Deleted successfully' }});
  }} catch (error) {{
    res.status(500).json({{ success: false, error: error.message }});
  }}
}});

module.exports = router;
"""
    return code


@tool("Endpoint Creator Tool")
def endpoint_creator_tool(endpoint_name: str, method: str, description: str) -> str:
    """
    Create custom API endpoint.

    Args:
        endpoint_name: Endpoint path
        method: HTTP method
        description: What the endpoint does

    Returns:
        Endpoint code
    """
    code = f"""
// {description}
router.{method.lower()}('{endpoint_name}', async (req, res) => {{
  try {{
    // {description}
    const result = await processRequest(req.body || req.params);

    res.json({{
      success: true,
      data: result,
      message: '{description} completed successfully'
    }});
  }} catch (error) {{
    console.error('{endpoint_name} error:', error);
    res.status(500).json({{
      success: false,
      error: error.message
    }});
  }}
}});
"""
    return code


@tool("Middleware Builder Tool")
def middleware_builder_tool(middleware_type: str) -> str:
    """
    Create middleware for API (auth, logging, validation, etc.).

    Args:
        middleware_type: Type of middleware (auth, logging, validation, cors, rate-limit)

    Returns:
        Middleware code
    """
    middlewares = {
        "auth": """
// Authentication Middleware
const authMiddleware = async (req, res, next) => {
  try {
    const token = req.headers.authorization?.split(' ')[1];
    if (!token) throw new Error('No token provided');

    const decoded = await verifyToken(token);
    req.user = decoded;
    next();
  } catch (error) {
    res.status(401).json({ success: false, error: 'Unauthorized' });
  }
};
""",
        "logging": """
// Request Logging Middleware
const loggingMiddleware = (req, res, next) => {
  const start = Date.now();
  res.on('finish', () => {
    const duration = Date.now() - start;
    console.log(`${req.method} ${req.path} - ${res.statusCode} - ${duration}ms`);
  });
  next();
};
""",
        "validation": """
// Request Validation Middleware
const validationMiddleware = (schema) => {
  return (req, res, next) => {
    const { error } = schema.validate(req.body);
    if (error) {
      return res.status(400).json({
        success: false,
        error: error.details[0].message
      });
    }
    next();
  };
};
""",
        "cors": """
// CORS Middleware
const corsMiddleware = (req, res, next) => {
  res.header('Access-Control-Allow-Origin', '*');
  res.header('Access-Control-Allow-Headers', 'Origin, X-Requested-With, Content-Type, Accept, Authorization');
  res.header('Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE, OPTIONS');
  if (req.method === 'OPTIONS') {
    return res.sendStatus(200);
  }
  next();
};
"""
    }

    return middlewares.get(middleware_type.lower(), f"// {middleware_type} Middleware\nconst {middleware_type}Middleware = (req, res, next) => next();")


@tool("Auth Handler Tool")
def auth_handler_tool(auth_type: str = "JWT") -> str:
    """
    Generate authentication handler code.

    Args:
        auth_type: Authentication type (JWT, OAuth, API Key)

    Returns:
        Authentication code
    """
    code = f"""
// {auth_type} Authentication Handler
const jwt = require('jsonwebtoken');
const bcrypt = require('bcryptjs');

// User registration
const register = async (req, res) => {{
  try {{
    const {{ email, password, username }} = req.body;

    // Hash password
    const hashedPassword = await bcrypt.hash(password, 10);

    // Create user
    const user = await db.users.create({{
      email,
      username,
      password: hashedPassword
    }});

    // Generate token
    const token = jwt.sign(
      {{ userId: user.id, email: user.email }},
      process.env.JWT_SECRET,
      {{ expiresIn: '7d' }}
    );

    res.status(201).json({{
      success: true,
      token,
      user: {{ id: user.id, email: user.email, username: user.username }}
    }});
  }} catch (error) {{
    res.status(400).json({{ success: false, error: error.message }});
  }}
}};

// User login
const login = async (req, res) => {{
  try {{
    const {{ email, password }} = req.body;

    // Find user
    const user = await db.users.findByEmail(email);
    if (!user) throw new Error('Invalid credentials');

    // Verify password
    const validPassword = await bcrypt.compare(password, user.password);
    if (!validPassword) throw new Error('Invalid credentials');

    // Generate token
    const token = jwt.sign(
      {{ userId: user.id, email: user.email }},
      process.env.JWT_SECRET,
      {{ expiresIn: '7d' }}
    );

    res.json({{
      success: true,
      token,
      user: {{ id: user.id, email: user.email, username: user.username }}
    }});
  }} catch (error) {{
    res.status(401).json({{ success: false, error: error.message }});
  }}
}};

// Token verification
const verifyToken = (token) => {{
  return new Promise((resolve, reject) => {{
    jwt.verify(token, process.env.JWT_SECRET, (err, decoded) => {{
      if (err) reject(err);
      else resolve(decoded);
    }});
  }});
}};

module.exports = {{ register, login, verifyToken }};
"""
    return code


# ============================================================================
# DATABASE TOOLS
# ============================================================================

@tool("Schema Designer Tool")
def schema_designer_tool(entity: str, fields: str) -> str:
    """
    Design database schema for an entity.

    Args:
        entity: Entity name (e.g., User, Product, Order)
        fields: Comma-separated fields (e.g., "name:string,email:string,age:number")

    Returns:
        Database schema definition
    """
    field_list = [f.strip() for f in fields.split(',')]

    # SQL schema
    sql_schema = f"""
-- SQL Schema for {entity}
CREATE TABLE {entity.lower()}s (
  id SERIAL PRIMARY KEY,
  """

    for field in field_list:
        name, ftype = field.split(':')
        sql_type = {
            'string': 'VARCHAR(255)',
            'text': 'TEXT',
            'number': 'INTEGER',
            'float': 'DECIMAL(10,2)',
            'boolean': 'BOOLEAN',
            'date': 'TIMESTAMP'
        }.get(ftype, 'VARCHAR(255)')

        sql_schema += f"{name} {sql_type},\n  "

    sql_schema += """created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Indexes
CREATE INDEX idx_{0}_id ON {0}s(id);
""".format(entity.lower())

    # MongoDB schema
    mongo_schema = f"""
// MongoDB Schema for {entity}
const {entity}Schema = new Schema({{
"""
    for field in field_list:
        name, ftype = field.split(':')
        mongo_type = {
            'string': 'String',
            'text': 'String',
            'number': 'Number',
            'float': 'Number',
            'boolean': 'Boolean',
            'date': 'Date'
        }.get(ftype, 'String')

        mongo_schema += f"  {name}: {{ type: {mongo_type}, required: true }},\n"

    mongo_schema += """}, {
  timestamps: true
});

const {0} = mongoose.model('{0}', {0}Schema);
""".format(entity)

    return f"SQL Schema:\n{sql_schema}\n\nMongoDB Schema:\n{mongo_schema}"


@tool("Query Builder Tool")
def query_builder_tool(operation: str, table: str, conditions: str = "") -> str:
    """
    Build database queries.

    Args:
        operation: Operation type (SELECT, INSERT, UPDATE, DELETE)
        table: Table name
        conditions: Query conditions

    Returns:
        Generated query
    """
    operations = {
        "SELECT": f"SELECT * FROM {table} {f'WHERE {conditions}' if conditions else ''};",
        "INSERT": f"INSERT INTO {table} (column1, column2) VALUES (value1, value2);",
        "UPDATE": f"UPDATE {table} SET column1 = value1 {f'WHERE {conditions}' if conditions else ''};",
        "DELETE": f"DELETE FROM {table} {f'WHERE {conditions}' if conditions else ''};"
    }

    return operations.get(operation.upper(), f"-- Query for {operation} on {table}")


@tool("Index Optimizer Tool")
def index_optimizer_tool(table: str, query_patterns: str) -> str:
    """
    Suggest index optimizations based on query patterns.

    Args:
        table: Table name
        query_patterns: Common query patterns

    Returns:
        Index recommendations
    """
    recommendations = f"""
-- Index Optimization Recommendations for {table}

-- Primary key index (automatic)
-- CREATE INDEX idx_{table}_id ON {table}(id);

-- Composite index for common query patterns
CREATE INDEX idx_{table}_composite ON {table}(column1, column2);

-- Covering index for frequently accessed columns
CREATE INDEX idx_{table}_covering ON {table}(column1, column2, column3);

-- Partial index for filtered queries
CREATE INDEX idx_{table}_active ON {table}(status) WHERE status = 'active';

-- Full-text search index
CREATE INDEX idx_{table}_search ON {table} USING GIN(to_tsvector('english', search_field));

-- Performance monitoring queries
EXPLAIN ANALYZE SELECT * FROM {table} WHERE column1 = 'value';
"""
    return recommendations


@tool("Migration Generator Tool")
def migration_generator_tool(migration_type: str, details: str) -> str:
    """
    Generate database migration scripts.

    Args:
        migration_type: Migration type (create_table, add_column, modify_column, drop_table)
        details: Migration details

    Returns:
        Migration script
    """
    timestamp = "20240101000000"
    script = f"""
-- Migration: {timestamp}_{migration_type}
-- Description: {details}

-- UP Migration
BEGIN;

-- {details}
-- Add your migration SQL here

COMMIT;

-- DOWN Migration (Rollback)
BEGIN;

-- Rollback {details}
-- Add your rollback SQL here

COMMIT;
"""
    return script


# ============================================================================
# INTEGRATION TOOLS
# ============================================================================

@tool("API Connector Tool")
def api_connector_tool(frontend_framework: str, api_endpoint: str) -> str:
    """
    Generate code to connect frontend to backend API.

    Args:
        frontend_framework: Frontend framework (React, Vue, Angular)
        api_endpoint: API endpoint to connect

    Returns:
        API connection code
    """
    code = f"""
// API Connection Layer for {frontend_framework}
import axios from 'axios';

const API_BASE_URL = process.env.REACT_APP_API_URL || 'http://localhost:3000/api';

// Create axios instance with default config
const api = axios.create({{
  baseURL: API_BASE_URL,
  timeout: 10000,
  headers: {{
    'Content-Type': 'application/json'
  }}
}});

// Request interceptor for auth token
api.interceptors.request.use(
  (config) => {{
    const token = localStorage.getItem('authToken');
    if (token) {{
      config.headers.Authorization = `Bearer ${{token}}`;
    }}
    return config;
  }},
  (error) => Promise.reject(error)
);

// Response interceptor for error handling
api.interceptors.response.use(
  (response) => response.data,
  (error) => {{
    if (error.response?.status === 401) {{
      // Handle unauthorized - redirect to login
      localStorage.removeItem('authToken');
      window.location.href = '/login';
    }}
    return Promise.reject(error);
  }}
);

// API service methods
export const apiService = {{
  get: (endpoint) => api.get(endpoint),
  post: (endpoint, data) => api.post(endpoint, data),
  put: (endpoint, data) => api.put(endpoint, data),
  delete: (endpoint) => api.delete(endpoint)
}};

export default apiService;
"""
    return code


@tool("Service Integrator Tool")
def service_integrator_tool(service_name: str, service_type: str) -> str:
    """
    Integrate third-party services (payment, email, storage, etc.).

    Args:
        service_name: Service name (Stripe, SendGrid, AWS S3, etc.)
        service_type: Service type (payment, email, storage, analytics)

    Returns:
        Integration code
    """
    integrations = {
        "payment": """
// Stripe Payment Integration
const stripe = require('stripe')(process.env.STRIPE_SECRET_KEY);

const createPaymentIntent = async (amount, currency = 'usd') => {
  try {
    const paymentIntent = await stripe.paymentIntents.create({
      amount: amount * 100, // Convert to cents
      currency,
      automatic_payment_methods: { enabled: true }
    });
    return { success: true, clientSecret: paymentIntent.client_secret };
  } catch (error) {
    return { success: false, error: error.message };
  }
};
""",
        "email": """
// SendGrid Email Integration
const sgMail = require('@sendgrid/mail');
sgMail.setApiKey(process.env.SENDGRID_API_KEY);

const sendEmail = async (to, subject, html) => {
  try {
    await sgMail.send({
      to,
      from: process.env.FROM_EMAIL,
      subject,
      html
    });
    return { success: true };
  } catch (error) {
    return { success: false, error: error.message };
  }
};
""",
        "storage": """
// AWS S3 Storage Integration
const AWS = require('aws-sdk');
const s3 = new AWS.S3({
  accessKeyId: process.env.AWS_ACCESS_KEY,
  secretAccessKey: process.env.AWS_SECRET_KEY
});

const uploadFile = async (file, fileName) => {
  try {
    const params = {
      Bucket: process.env.S3_BUCKET,
      Key: fileName,
      Body: file,
      ACL: 'public-read'
    };
    const result = await s3.upload(params).promise();
    return { success: true, url: result.Location };
  } catch (error) {
    return { success: false, error: error.message };
  }
};
"""
    }

    return integrations.get(service_type.lower(), f"// {service_name} Integration\n// Add integration code here")


@tool("Deployment Orchestrator Tool")
def deployment_orchestrator_tool(platform: str, app_name: str) -> str:
    """
    Generate deployment configuration and scripts.

    Args:
        platform: Deployment platform (Docker, Kubernetes, Vercel, Heroku)
        app_name: Application name

    Returns:
        Deployment configuration
    """
    configs = {
        "docker": f"""
# Dockerfile for {app_name}
FROM node:18-alpine

WORKDIR /app

COPY package*.json ./
RUN npm install --production

COPY . .

EXPOSE 3000

CMD ["npm", "start"]

# docker-compose.yml
version: '3.8'
services:
  app:
    build: .
    ports:
      - "3000:3000"
    environment:
      - NODE_ENV=production
      - DATABASE_URL=${{DATABASE_URL}}
    depends_on:
      - db

  db:
    image: postgres:15-alpine
    environment:
      - POSTGRES_DB={app_name}
      - POSTGRES_USER=admin
      - POSTGRES_PASSWORD=${{DB_PASSWORD}}
    volumes:
      - db-data:/var/lib/postgresql/data

volumes:
  db-data:
""",
        "kubernetes": f"""
# Kubernetes Deployment for {app_name}
apiVersion: apps/v1
kind: Deployment
metadata:
  name: {app_name}
spec:
  replicas: 3
  selector:
    matchLabels:
      app: {app_name}
  template:
    metadata:
      labels:
        app: {app_name}
    spec:
      containers:
      - name: {app_name}
        image: {app_name}:latest
        ports:
        - containerPort: 3000
        env:
        - name: NODE_ENV
          value: "production"
---
apiVersion: v1
kind: Service
metadata:
  name: {app_name}-service
spec:
  selector:
    app: {app_name}
  ports:
  - protocol: TCP
    port: 80
    targetPort: 3000
  type: LoadBalancer
""",
        "vercel": f"""
# vercel.json for {app_name}
{{
  "version": 2,
  "builds": [
    {{
      "src": "package.json",
      "use": "@vercel/node"
    }}
  ],
  "routes": [
    {{
      "src": "/(.*)",
      "dest": "/"
    }}
  ],
  "env": {{
    "NODE_ENV": "production"
  }}
}}
"""
    }

    return configs.get(platform.lower(), f"# Deployment config for {app_name} on {platform}")


@tool("Testing Framework Tool")
def testing_framework_tool(test_type: str, component: str) -> str:
    """
    Generate test code for components.

    Args:
        test_type: Test type (unit, integration, e2e)
        component: Component to test

    Returns:
        Test code
    """
    tests = {
        "unit": f"""
// Unit Tests for {component}
const {{ {component} }} = require('./{component}');

describe('{component}', () => {{
  test('should exist', () => {{
    expect({component}).toBeDefined();
  }});

  test('should handle valid input', () => {{
    const result = {component}('valid input');
    expect(result).toBeTruthy();
  }});

  test('should handle invalid input', () => {{
    expect(() => {{
      {component}('');
    }}).toThrow();
  }});
}});
""",
        "integration": f"""
// Integration Tests for {component}
const request = require('supertest');
const app = require('../app');

describe('{component} Integration Tests', () => {{
  test('GET /{component} should return 200', async () => {{
    const response = await request(app)
      .get('/{component}')
      .expect('Content-Type', /json/)
      .expect(200);

    expect(response.body.success).toBe(true);
  }});

  test('POST /{component} should create resource', async () => {{
    const newData = {{ name: 'Test', value: '123' }};
    const response = await request(app)
      .post('/{component}')
      .send(newData)
      .expect(201);

    expect(response.body.data).toHaveProperty('id');
  }});
}});
""",
        "e2e": f"""
// E2E Tests for {component}
describe('{component} E2E Tests', () => {{
  beforeEach(() => {{
    cy.visit('/');
  }});

  it('should display {component}', () => {{
    cy.get('[data-testid="{component}"]').should('be.visible');
  }});

  it('should interact with {component}', () => {{
    cy.get('[data-testid="{component}"]').click();
    cy.get('[data-testid="result"]').should('contain', 'Success');
  }});
}});
"""
    }

    return tests.get(test_type.lower(), f"// {test_type} test for {component}")


# List of all tools for easy export
all_tools = [
    ui_generator_tool, component_creator_tool, css_styling_tool, accessibility_checker_tool,
    api_generator_tool, endpoint_creator_tool, middleware_builder_tool, auth_handler_tool,
    schema_designer_tool, query_builder_tool, index_optimizer_tool, migration_generator_tool,
    api_connector_tool, service_integrator_tool, deployment_orchestrator_tool, testing_framework_tool
]
