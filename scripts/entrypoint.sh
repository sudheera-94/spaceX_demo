#!/bin/sh

set -e

python manage.py collectstatic --noinput

uwsgi --http :8000 --master --enable-threads --module spaceX_starlink_add.wsgi
