# Panda Chat Server

## Requirements

  - Docker and Docker Compose

## Running it

  - Run migrations.
    - `docker-compose run web python manage.py migrate`
  - If using Windows, you might need to install pypiwin32.
    -  (untested) `docker-compose run web pip install pypiwin32`
  - Start the server.
    - `docker-compose up`
