"""
WSGI config for h3d project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/wsgi/
"""

import os
import sys
sys.path.append('/home/john/had')
sys.path.append('/home/john/had/h3d')

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'h3d.settings')

application = get_wsgi_application()
