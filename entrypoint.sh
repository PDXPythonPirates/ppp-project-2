#!/bin/sh

if [ "$DB_HOST" = "mysql" ]
then
    echo "Waiting for mysql to boot..."

    while ! nc -z $DB_HOST $DB_PORT; do
      sleep 0.1
    done

    echo "mySQL started"
fi

# poetry run /usr/src/app/app_run.py run -h 0.0.0.0

exec "$@"