#!/bin/sh
python manage.py migrate
python manage.py collectstatic --noinput
gunicorn mysite.wsgi:application -w 4 -k gthread -b 0.0.0.0:8010 --chdir=/app