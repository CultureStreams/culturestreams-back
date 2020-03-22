#!/bin/sh

/code/manage.py migrate
/code/manage.py collectstatic --noinput

/usr/local/bin/uwsgi --http-auto-chunked \
                     --http-keepalive \
                     --wsgi-file /code/culturestreams/wsgi.py \
                     --master \
                     --pythonpath /code \
                     --threads 4 \
                     --http 0.0.0.0:8000 \
                     --static-map /static=/code/static-collected
