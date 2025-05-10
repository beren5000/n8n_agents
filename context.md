# n8n Generative AI Agent Project

## Project Overview
This prototype demonstrates using n8n as an orchestration layer for generative AI agents that can:
- Process natural language queries from users
- Connect to existing databases/applications to retrieve information
- Maintain conversation history
- Make decisions based on user input and available data

## Architecture
```
┌──────────┐    ┌─────────────┐    ┌───────────────┐
│  Client  │───>│  n8n Agent  │───>│ Django Backend│
└──────────┘    └─────────────┘    └───────────────┘
                       │                    │
                       ▼                    ▼
                ┌─────────────┐     ┌─────────────────┐
                │Generative AI│     │Database (SQLite)│
                └─────────────┘     └─────────────────┘
```

## Requirements
1. **Django Backend**
   - Database models for warehouse equipment management
   - Database models for conversation history
   - REST API endpoints for data access

2. **Python Tools for n8n**
   - Custom Python scripts to access the database
   - Functions to query warehouse information
   - Functions to retrieve user conversation history

3. **n8n Workflows**
   - Integration with Generative AI
   - Decision-making logic
   - API connections to Django backend

4. **Stress Testing Framework**
   - Simulate multiple concurrent users
   - Compare API endpoint vs direct database access
   - Measure response times and correctness

## Database Schema
```
Equipment
- id (PK)
- name
- type
- quantity
- location
- last_updated

ConversationHistory
- id (PK)
- user_id
- timestamp
- query
- response
- related_equipment_id (FK, optional)
```

## Implementation Plan
1. Set up Django project with models and admin interface
2. Implement Django REST API endpoints
3. Create Python tools for direct database access
4. Build n8n workflows for:
   - Processing user queries
   - Retrieving information from database
   - Generating responses with AI
5. Develop stress testing framework
6. Conduct tests and optimize performance

## n8n Workflow Design
- **Input Node**: Receives user queries
- **AI Processing Node**: Uses generative AI to understand query
- **Decision Node**: Determines if query needs database information
- **Database Query Node**: Retrieves relevant data
- **Response Generation Node**: Creates response combining AI and data
- **History Recording Node**: Logs conversation to database

## Testing Strategy
- Unit tests for Django models and API endpoints
- Workflow tests for n8n integrations
- Stress tests to measure:
  - Response time under load
  - Accuracy of responses
  - System stability

## Project Status
- Initial planning and design phase
- Implementation pending

## Technical Notes
- Django REST Framework for API development
- SQLite for development, can be migrated to PostgreSQL for production
- n8n self-hosted instance
- Python for custom tools and testing framework