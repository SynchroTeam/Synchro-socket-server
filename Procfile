release: python manage.py migrate
release: export DJANGO_SETTINGS_MODULE=Django.settings
web: daphne Django.asgi:application --port $PORT --bind 0.0.0.0 -v2
worker: python manage.py runworker channels --settings=Django.settings -v2