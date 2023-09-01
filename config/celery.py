import os

from celery import Celery
from celery.schedules import crontab

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
app = Celery("config")

app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'update_database': {
        'task': 'apps.contacts.tasks.update_database',
        'schedule':  crontab(minute='*/30'),
        'kwargs': {},
    }
}
