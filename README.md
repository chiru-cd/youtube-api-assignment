# Project Goal

To make an API to fetch latest videos sorted in reverse chronological order of their publishing date-time from YouTube for a given tag/search query in a paginated response.

## Method

Cron Jobs [django_cron](https://django-cron.readthedocs.io/en/latest/introduction.html) was used to fetch videos after every 5 minutes using [Youtube Data Api](https://developers.google.com/youtube/v3/docs/search/list) and save it to the PostgreSQL database.

## Setup
- Setup `docker` and `docker-compose` for the current user.
- Clone the project
- Configure the project by adding API Keys to the `key.toml` file. You can also configure the query string in this file.
- Configure the database credentials in the `.env.dev` and `docker-compose.yml` files. 
- Use `docker-compose` to start the `db`(postgres) and `web` microservices. You can use as many workers for the `web` microservice.
- Now visit - `http://localhost:8000`.

## APIs

- The Django Model API can be found at: `http://localhost:8000/videos`
- The Filter API can be found at: `http://localhost:8000/filtered_videos/?search=querystring`