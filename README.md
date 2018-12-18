# Panda Chat Server

## Requirements

  - Python 3.7.1+
  - (Recommended) Set up a virtual environment for the project using venv or whatever tool you prefer.
    - Preferably put your virtual environment in /env/ or /.venv/ since those directories are already excluded via .gitignore.
  - Install other dependencies using pip.
    - `pip install -r requirements`
  - Install PostgreSQL 11.1+
  - Add user to PostgreSQL named `django` with password `6NdYI42&E43ZIA@pcBw@`

## Running it

  - Run migrations.
    - `python manage.py migrate`
  - Start the server.
    - `python manage.py runserver`