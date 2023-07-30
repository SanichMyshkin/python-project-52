install:
	poetry install

test:
	poetry run python manage.py test

dev:
	python manage.py runserver

test-coverage:
	poetry run coverage run manage.py test
	poetry run coverage xml
	poetry run coverage report

migrate:
	python manage.py migrate

start:
	# poetry run python manage.py runserver
	gunicorn task_manager.wsgi

lint:
	poetry run flake8 task_manager --exclude migrations

en:
	python manage.py makemessages -l en

ru:
	python manage.py makemessages -l ru

langcomp:
	python manage.py compilemessages

d_install:
	poetry run django-admin version
	django-admin startproject task_manager .

shell:
	python manage.py shell
