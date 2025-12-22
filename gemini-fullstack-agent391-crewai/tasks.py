"""
Gemini Fullstack Multi-Agent System - CrewAI Tasks
Tasks for complete full-stack application development.
"""

from crewai import Task
from agents import (
    fullstack_architect,
    frontend_developer,
    backend_developer,
    database_engineer,
    integration_specialist
)

def create_fullstack_development_tasks(project_requirements: str):
    """
    Create tasks for full-stack application development.

    Args:
        project_requirements: Complete project requirements

    Returns:
        List of CrewAI tasks in execution order
    """

    # Task 1: Architect analyzes requirements and creates development plan
    task_planning = Task(
        description=f"""Analyze the project requirements and create a comprehensive development plan:

        PROJECT REQUIREMENTS:
        {project_requirements}

        Your responsibilities:
        1. Understand the complete scope of the application
        2. Identify frontend, backend, database, and integration needs
        3. Create a detailed architecture plan
        4. Define the technology stack for each layer
        5. Plan the development workflow and agent coordination
        6. Establish success criteria

        Delegate planning to specialized agents as needed.
        """,
        agent=fullstack_architect,
        expected_output="Comprehensive architecture plan with technology stack and development workflow"
    )

    # Task 2: Database Engineer designs data models
    task_database_design = Task(
        description="""Design the database schema and data models for the application.

        Based on the architecture plan:
        1. Identify all entities and their relationships
        2. Design normalized database schemas
        3. Plan indexes for query optimization
        4. Create migration scripts
        5. Define data validation rules
        6. Consider scalability and performance

        Provide complete database schema definitions ready for implementation.
        """,
        agent=database_engineer,
        expected_output="Complete database schema with tables, indexes, and migration scripts",
        context=[task_planning]
    )

    # Task 3: Backend Developer creates API and business logic
    task_backend_development = Task(
        description="""Develop the backend API and business logic.

        Your responsibilities:
        1. Create RESTful API endpoints for all required operations
        2. Implement authentication and authorization
        3. Build middleware for logging, validation, and error handling
        4. Integrate with the database schema
        5. Implement business logic and data processing
        6. Add proper error handling and logging

        Use the database schema from the Database Engineer.
        Coordinate with Frontend Developer on API contracts.
        """,
        agent=backend_developer,
        expected_output="Complete backend API with endpoints, authentication, and business logic",
        context=[task_database_design]
    )

    # Task 4: Frontend Developer creates user interface
    task_frontend_development = Task(
        description="""Design and implement the user interface.

        Your responsibilities:
        1. Create component architecture
        2. Build responsive UI components
        3. Implement state management
        4. Design user flows and navigation
        5. Ensure accessibility compliance
        6. Create beautiful, intuitive designs

        Coordinate with Backend Developer on API integration needs.
        Ensure components are ready for integration.
        """,
        agent=frontend_developer,
        expected_output="Complete frontend application with components, styling, and user flows",
        context=[task_planning, task_backend_development]
    )

    # Task 5: Integration Specialist connects all components
    task_integration = Task(
        description="""Integrate all application components into a cohesive system.

        Your responsibilities:
        1. Connect frontend to backend APIs
        2. Integrate third-party services (payment, email, storage, etc.)
        3. Set up API communication layer
        4. Implement error handling across layers
        5. Configure CORS and security headers
        6. Ensure data flows correctly through all layers

        Verify that:
        - Frontend can communicate with backend
        - Backend can access database
        - All services are properly configured
        """,
        agent=integration_specialist,
        expected_output="Fully integrated application with all components connected",
        context=[task_frontend_development, task_backend_development, task_database_design]
    )

    # Task 6: Integration Specialist performs testing
    task_testing = Task(
        description="""Implement comprehensive testing for the application.

        Create tests for:
        1. Unit tests for individual components and functions
        2. Integration tests for API endpoints
        3. End-to-end tests for critical user flows
        4. Performance and load testing
        5. Security testing

        Report any issues found and ensure all tests pass.
        """,
        agent=integration_specialist,
        expected_output="Complete test suite with passing tests and test coverage report",
        context=[task_integration]
    )

    # Task 7: Integration Specialist prepares deployment
    task_deployment = Task(
        description="""Prepare the application for deployment.

        Your responsibilities:
        1. Create Docker containers for all services
        2. Write docker-compose configuration
        3. Generate Kubernetes manifests (optional)
        4. Set up CI/CD pipeline configuration
        5. Create deployment documentation
        6. Define environment variables and secrets

        Provide deployment-ready configuration files.
        """,
        agent=integration_specialist,
        expected_output="Complete deployment configuration with Docker, CI/CD, and documentation",
        context=[task_testing]
    )

    # Task 8: Architect reviews and finalizes
    task_final_review = Task(
        description="""Review the complete application and provide final deliverables.

        Your responsibilities:
        1. Review all components developed by specialized agents
        2. Verify integration and functionality
        3. Ensure architecture goals are met
        4. Create project documentation
        5. Generate deployment instructions
        6. Provide maintenance guidelines

        Deliver a comprehensive summary of the completed fullstack application.
        """,
        agent=fullstack_architect,
        expected_output="Final project summary with documentation, deployment guide, and next steps",
        context=[task_deployment]
    )

    return [
        task_planning,
        task_database_design,
        task_backend_development,
        task_frontend_development,
        task_integration,
        task_testing,
        task_deployment,
        task_final_review
    ]


# Example task sets for common applications

def create_todo_app_tasks():
    """Tasks for building a todo list application."""
    return create_fullstack_development_tasks("""
Build a modern todo list application with the following features:

Frontend:
- Responsive design for mobile and desktop
- Add, edit, delete, and complete tasks
- Filter tasks by status (all, active, completed)
- Dark mode support

Backend:
- RESTful API for task management
- User authentication (register, login, logout)
- Task CRUD operations
- User-specific task isolation

Database:
- User table (id, email, password_hash, created_at)
- Task table (id, user_id, title, description, completed, due_date, created_at)

Integration:
- Real-time updates using WebSockets
- Deploy as Docker containers
    """)


def create_ecommerce_tasks():
    """Tasks for building an e-commerce platform."""
    return create_fullstack_development_tasks("""
Build a full-featured e-commerce platform with:

Frontend:
- Product catalog with search and filtering
- Shopping cart and checkout flow
- User account management
- Order history and tracking
- Admin dashboard for product management

Backend:
- Product API with inventory management
- Shopping cart session management
- Order processing and payment integration (Stripe)
- User authentication and authorization
- Admin APIs for product and order management

Database:
- Users (customers and admins)
- Products (with categories, images, inventory)
- Orders (with line items and status tracking)
- Shopping carts (session-based)

Integration:
- Stripe payment processing
- SendGrid email notifications
- AWS S3 for product images
- Docker deployment with load balancing
    """)


def create_dashboard_tasks():
    """Tasks for building an analytics dashboard."""
    return create_fullstack_development_tasks("""
Build an analytics dashboard application with:

Frontend:
- Interactive charts and graphs (Chart.js/D3.js)
- Real-time data visualization
- Customizable dashboard widgets
- Export data to CSV/PDF
- Responsive grid layout

Backend:
- Data aggregation APIs
- Real-time data streaming via WebSockets
- User authentication and role-based access
- Data export endpoints
- Caching for performance

Database:
- Time-series data storage
- User profiles and preferences
- Dashboard configuration
- Historical data aggregation

Integration:
- WebSocket server for real-time updates
- Redis for caching and session management
- Kubernetes deployment with horizontal scaling
- Monitoring and alerting setup
    """)
