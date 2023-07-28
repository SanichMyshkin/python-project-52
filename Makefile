install:
	poetry install

test:
	python manage.py test

dev:
	python manage.py runserver



migrate:
	python manage.py migrate

start:
	# poetry run python manage.py runserver
	gunicorn task_manager.wsgi

lint:
	poetry run flake8 task_manager --exclude migrations







pu:
	git add .
	git commit -m "Some fix"
	git push

pid: # Для поиска пида занимающего порт 8000 (необходим для разработки)
	sudo lsof -i :8000

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
