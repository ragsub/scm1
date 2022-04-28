web: gunicorn SCM.wsgi --log-file -
worker: celery -A SCM.celery worker -l INFO
ps:scale worker=1