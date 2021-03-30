# pull official base image
FROM python:3.8.3-alpine

RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev

# set work directory
WORKDIR /usr/src/app

# copy cron file and set permisssions
COPY django-cron /etc/cron.d/django-cron
RUN chmod 0644 /etc/cron.d/django-cron
RUN /usr/bin/crontab /etc/cron.d/django-cron

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY . .

# set the entrypoint
COPY entrypoint.sh /
ENTRYPOINT ["/entrypoint.sh"]
