 web: gunicorn email_notifications.wsgi --log-file -

 worker: celery -A email_notifications worker --beat
