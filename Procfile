 web: gunicorn email_notifications.wsgi --log-file -

 worker: celery -A email_notifications worker -events -loglevel info
 beat: celery -A email_notifications beat 
