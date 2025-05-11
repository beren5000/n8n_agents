"""
WSGI config for core project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os
import sys
from pathlib import Path

# Add the Django project directory to sys.path
project_path = Path(__file__).resolve().parent.parent
if str(project_path) not in sys.path:
    sys.path.insert(0, str(project_path))

# Load environment variables from .env file
from dotenv import load_dotenv
env_path = project_path / '.env'
load_dotenv(dotenv_path=env_path)

# Set Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

# Import Django WSGI app
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
