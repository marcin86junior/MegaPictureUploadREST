MegaPictureUploadREST
===========

![alt text](http://marcin86.pythonanywhere.com/static/MegaUploadpic.PNG)

Requirements:

	Python 3.8.x (3.9.1 working in Docker)
	Django 3.2.12
	Djangorestframework 3.13.x

Installation:

	Create new folder "MegaPictureUploadREST" and open it:
	git clone https://github.com/marcin86junior/MegaPictureUploadREST.git .
	python -m venv myvenv
	.\myvenv\Scripts\activate
	pip install -r requirements.txt
	cd django_rest_imageupload_backend\
	python manage.py migrate
	python manage.py migrate --run-syncdb
	python .\manage.py runserver
	python manage.py loaddata group.json
	python manage.py loaddata users.json
	python manage.py loaddata data.json
	python manage.py createsuperuser (marcin/123)
	python manage.py runserver 

Testing:

	python manage.py test imageupload
	--
	coverage run --source='.' --omit='*migrations*,*init*,*wsgi*,*asgi*,*urls*,*manage*,*admin*,*apps*,*settings*,*test*,*seriali*' manage.py test eMenu
	coverage html
	--

Docker:

	Create new folder "MegaPictureUploadREST" and open it:
	git clone https://github.com/marcin86junior/MegaPictureUploadREST.git .
	cd django_rest_imageupload_backend\
	"Open Doker Desktop"
	docker-compose run web python3 manage.py migrate
	docker-compose run web python3 manage.py migrate --run-syncdb
	docker-compose run web python3 manage.py loaddata group.json
	docker-compose run web python3 manage.py loaddata users.json
	docker-compose run web python3 manage.py loaddata data.json
	docker-compose up
	Test:
	docker-compose run web python3 manage.py test

Loaddata:

	User / Password / Group:
	b1 / 123 / Basic
	p2 / 123 / Premium
	e3 / 123 / Enterprice
	c4 / 123 / Custom
	+ for all users added 2 diffrent pictures

