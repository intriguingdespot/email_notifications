web: gunicorn email_notifications.wsgi --log-file -
worker:celery -A email_notifications beat -l info --scheduler django_celery_beat.schedulers:DatabaseScheduler
worker:celery -A email_notifications worker -l info
