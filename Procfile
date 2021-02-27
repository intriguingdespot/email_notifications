web: gunicorn email_notifications.wsgi --log-file -
worker: celery -A email_notifications worker -c 1 --beat -l info
