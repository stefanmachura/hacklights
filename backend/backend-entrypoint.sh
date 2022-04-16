#!/bin/bash

set -e

wait-for-it -h hacklights-db -p 5432

python manage.py makemigrations

python manage.py migrate

python manage.py runserver 0.0.0.0:8000
