# Стандартный файл WSGI для деплоя на традиционных серверах (Gunicorn, uWSGI).

"""
WSGI config for personal_notes_project project.

It exposes the WSGI callable as a module-level variable named `application`.
"""

import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'personal_notes_project.settings')

application = get_wsgi_application()

