from __future__ import absolute_import, unicode_literals
import os
from celery import Celery



os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'MaintenanceLog.settings')

app = Celery('MaintenanceLog')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.conf.beat_schedule = {
    'send-email-brush-update' : {
        'task' : 'app.tasks.sendBrushUpdateEmail',
        # 1800 seconds = half hour 
        'schedule' : 1800, 
        # function args go below 
        #'args' : ('dfinley5656@gmail.com',)
    }
}

app.autodiscover_tasks()