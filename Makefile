install:
	poetry install

lint:
	poetry run flake8 task_manager

dev:
	python manage.py runserver

start:
	poetry run python manage.py runserver

d_install:
	poetry run django-admin version
	django-admin startproject task_manager .