#!/bin/bash

pip install django-oscar-accounts
python manage.py migrate oscar_accounts
python manage.py oscar_accounts_init
