"""
<<<<<<< HEAD
ASGI config for esr21 project.
=======
ASGI config for asr21 project.
>>>>>>> 115f5bab974d56b8bf402fd081c3ec923bd46c57

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'esr21.settings')

application = get_asgi_application()