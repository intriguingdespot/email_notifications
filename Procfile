web: gunicorn email_notifications.wsgi --log-file -
worker: celery -A email_notifications worker -l info -B --scheduler email_notifications.schedulers:DatabaseScheduler --without-gossip --without-mingle --without-heartbeat
