#!/bin/bash -x

python manage.py migrate --noinput
python manage.py makemigrations class_management
python manage.py migrate --noinput
#python manage.py loaddata db.json

exec "$@"