#!/bin/sh

echo "Waiting for postgres..."

while ! nc -z $DB_HOST $DB_PORT; do
  sleep 0.1
done

echo "PostgreSQL started"

echo "django maintain"
python manage.py makemigrations
python manage.py migrate
python manage.py migrate --run-syncdb

echo "populate db"
python manage.py runscript add_initial_data
python manage.py runscript create_api_user_and_key

exec "$@"
