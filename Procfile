release: python3 manage.py migrate
web: python manage.py collectstatic --no-input; gunicorn inventario.wsgi --log-file - --log-level debug
