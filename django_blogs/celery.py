import os
from celery import Celery

# Set the default Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_blogs.settings')

app = Celery('django_blogs')

# Load task modules from all registered Django apps.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Look for tasks.py in Django apps
app.autodiscover_tasks()
