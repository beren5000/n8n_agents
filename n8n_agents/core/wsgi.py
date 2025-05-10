"""
WSGI config for core project.
"""
import os
import sys

# Add project path to Python path
sys.path.insert(0, '/var/www/n8n_agents')
sys.path.insert(0, '/var/www/n8n_agents/n8n_agents')

# Apply timezone patch before importing Django
try:
    from core.timezone_patch import TimezonePatch
    sys.modules['django.utils.timezone'] = TimezonePatch('django.utils.timezone')
except ImportError:
    pass

# Set Django settings module
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")

# Import Django WSGI application
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
