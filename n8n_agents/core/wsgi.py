"""
WSGI config for core project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""

import os
import sys

# Handle zoneinfo compatibility before Django imports
if sys.version_info >= (3, 9):
    try:
        import zoneinfo
    except ImportError:
        pass
else:
    try:
        import backports.zoneinfo
    except ImportError:
        pass

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")

application = get_wsgi_application()
