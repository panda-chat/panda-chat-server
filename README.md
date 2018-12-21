# Panda Chat Server

## Requirements

  - Python 3.7.1+
  - (Recommended) Set up a virtual environment for the project using venv or whatever tool you prefer.
    - Preferably put your virtual environment in /env/ or /.venv/ since those directories are already excluded via .gitignore.
  - Install other dependencies using pip.
    - `pip install -r requirements`
  - If using Windows, also `pip install pypiwin32`.
  - Install PostgreSQL 11.1+ and set-up database/user.
    - `CREATE DATABASE chatserver;`
    - `CREATE USER django WITH PASSWORD '6NdYI42&E43ZIA@pcBw@';`
    - `GRANT ALL PRIVILEGES ON DATABASE chatserver TO django;`

## Running it

  - Run migrations.
    - `python manage.py migrate`
  - Start the server.
    - `python manage.py runserver`
