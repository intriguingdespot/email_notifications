web: gunicorn email_notifications.wsgi --log-file -
worker: celery -A email_notifications worker -l info
beat: celery -A email_notifications beat -l info
