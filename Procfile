web: gunicorn email_notifications.wsgi --log-file -
worker1:celery -A email_notifications beat -l info --scheduler django_celery_beat.schedulers:DatabaseScheduler
worker2:celery -A email_notifications worker -l info
