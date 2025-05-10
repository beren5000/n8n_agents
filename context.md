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
                ┌─────────────┐     ┌──────────────────────┐
                │Generative AI│     │Database (PostgreSQL )│
                └─────────────┘     └──────────────────────┘
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
```

## Implementation Plan
1. [x] Set up Django project with custom User model
2. [x] Configure PostgreSQL database connection
3. [x] Set up environment variables management
4. [x] Create custom management commands
5. [x] Implement warehouse equipment models
6. [x] Implement conversation history models
7. [ ] Implement Django REST API endpoints
8. [ ] Create Python tools for direct database access
9. [ ] Build n8n workflows for processing user queries
10. [ ] Develop stress testing framework
11. [ ] Conduct tests and optimize performance

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
- [x] Initial setup complete
- [x] Custom User model implemented
- [x] Database connection configured
- [x] Implementation of data models complete
- [ ] REST API implementation pending
- [ ] n8n workflow implementation pending

## Technical Notes
- Django REST Framework for API development
- PostgreSQL for database
- Custom User model with email authentication
- Environment variables for configuration
- n8n self-hosted instance
- Python for custom tools and testing framework
- GitHub Actions potential for deployment automation

## Endpoints
- we need to create two endpoints on equipment
   1. list equipment: list all equipmnet and filter by name, user__name, type, location; can order by last_updated
   2. create equipment: post with all the fields and a email to assign to an user 