#!/bin/sh

/usr/sbin/crond -b

cd /usr/src/app && python manage.py migrate --noinput

touch /tmp/youtube_cronjob.log

while ! nc -z $SQL_HOST $SQL_PORT; do
  sleep 0.1
done

exec "$@"