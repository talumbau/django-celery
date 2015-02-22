web: gunicorn mysite.wsgi --log-file -
worker: celery -A adder.tasks worker --loglevel=info
