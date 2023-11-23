#!/usr/bin/env bash
# exit on error
set -o errexit

poetry install

python manage.py collectstatic --no-input
python manage.py migrate

python manage.py shell -c "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('database2', 'kuanysh.drk@gmail.com', 'geekuk951A') if not User.objects.filter(username='database2').exists() else None"