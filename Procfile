 web: gunicorn email_notifications.wsgi --log-file -

celery -A email_notifications worker -l info
celery -A email_notifications beat -l info --scheduler django_celery_beat.schedulers:DatabaseScheduler
