#!/bin/bash

# Collect static files
echo "Collect static files"
python manage.py collectstatic --noinput

# Apply database migrations
echo "Apply database migrations"
python manage.py migrate

python manage.py migrate --run-syncdb 

python manage.py loaddata group.json users.json data.json

python manage.py runserver 0.0.0.0:8000
