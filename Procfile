web: gunicorn email_notifications.wsgi --log-file -
celery: celery worker -A email_notifications -l info -c 4
