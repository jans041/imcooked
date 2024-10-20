import os
from django.core.wsgi import get_wsgi_application

# Set the default settings module for the 'myproject' Django application.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'demo.settings')

application = get_wsgi_application()
