# n8n Generative AI Agent Project

## Overview
This project demonstrates using n8n as an orchestration layer for generative AI agents that process natural language queries, connect to databases, maintain conversation history, and make intelligent decisions based on available data.

The system allows generative AI agents to interact with a Django backend storing warehouse equipment data and conversation history.

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

## Prerequisites
- VS Code with Dev Containers extension
- Docker and Docker Compose

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/n8n_agents.git
cd n8n_agents
```

### 2. Open in VS Code with Dev Container
- Open the project in VS Code
- Click the green button in the bottom-left corner or run the "Dev Containers: Open Folder in Container" command
- VS Code will build and start the development container

### 3. Install Venv Poetry 
```bash
# Install dependencies
poetry install
```

### 4. Set Up Environment Variables
```bash
# Copy the example .env file
cp n8n_agents/.env.example n8n_agents/.env

# Edit the .env file with your settings
# Especially update your superuser credentials
```

### 5. Start PostgreSQL and Create Database
```bash
# Start PostgreSQL if not running
sudo service postgresql start

# Create the database
createdb -U postgres n8n_agents
```

### 6. Apply Migrations and Create Superuser
```bash
cd /workspaces/n8n_agents
poetry shell
python n8n_agents/manage.py migrate
python n8n_agents/manage.py create_superuser
```

### 7. Run the Development Server
```bash
python n8n_agents/manage.py runserver
```

## Project Structure
```
n8n_agents/
├── n8n_agents/            # Django project root
│   ├── apps/              # Django applications
│   │   ├── accounts/      # Custom user model
│   │   ├── warehouse/     # Warehouse equipment models
│   │   └── conversations/ # Conversation history models
│   ├── core/              # Project settings
│   └── .env               # Environment variables
├── pyproject.toml         # Project dependencies
└── poetry.toml            # Poetry configuration
```

## Usage
Once the server is running, you can:

- Access the Django admin interface at http://localhost:8000/admin/
- Use the REST API endpoints to interact with warehouse data
- Connect n8n workflows to the Django backend

## License
MIT