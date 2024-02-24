web: gunicorn drf_fanzone.wsgi
web: serve -s build
release: python manage.py makemigrations && python manage.py migrate