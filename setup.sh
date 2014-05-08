#!/bin/bash

virtualenv venv --distribute --no-site-packages
source venv/bin/activate
pip install -r requirements.txt
python manage.py syncdb && python manage.py migrate
