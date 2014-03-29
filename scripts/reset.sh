#!/bin/bash

dropdb application
createdb application

python manage.py syncdb --noinput
python manage.py migrate --noinput
