run:
	python manage.py runserver

d_install:
	poetry run django-admin version
	django-admin startproject task_manager .