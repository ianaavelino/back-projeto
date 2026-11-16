#!/usr/bin/env bash
set -o errexit

export DJANGO_SETTINGS_MODULE=gerenciamento.settings.prod

pip install -r requirements.txt

python manage.py check
python manage.py collectstatic --noinput
python manage.py migrate