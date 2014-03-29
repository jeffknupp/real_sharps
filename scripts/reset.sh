#!/bin/bash

dropdb application
createdb application

python manage.py --noinput syncdb
python manage.py migrate
