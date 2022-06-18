MegaPictureUploadREST -
=====================

### Your own upload picture website in Django/REST

![alt text](http://marcin86.pythonanywhere.com/static/MegaUploadpic.PNG)

Overview
--------

MegaPictureUploadREST is an open-source webiste for upload pictures. 
Django/REST technology is used for permission and authorization.
We have few group for specyfic users/clients:

* **Basic group** for newcomers for free 200x200 picture

* **Premium group** for clients that require orginal pictures, 200x200 and 400x400

* **Special Enterprise group** for clients that require expire links counted in time (30-30000)

* **Special Custom group** for clients that require special size of thumbs e.g. 123x123

Requirements:
-------------

	Python 3.8.x (3.9.1 working in Docker)
	Django 3.2.12
	Djangorestframework 3.13.x

Installation:
-------------


	Create new folder "MegaPictureUploadREST" and open it:
	git clone https://github.com/marcin86junior/MegaPictureUploadREST.git .
	python -m venv myvenv
	.\myvenv\Scripts\activate
	pip install -r requirements.txt
	cd django_rest_imageupload_backend\
	python manage.py migrate
	python manage.py migrate --run-syncdb
	python manage.py loaddata group.json users.json data.json
	python .\manage.py runserver
	*python manage.py createsuperuser (marcin/123)


Testing:
--------

	python manage.py test
	coverage run --source='.' --omit='*migrations*,*init*,*wsgi*,*asgi*,*urls*,*manage*,*admin*,*apps*,*settings*,*test*,*seriali*' manage.py test
	coverage report (or) coverage html


Docker:
-------

	Create new folder "MegaPictureUploadREST" and open it:
	git clone https://github.com/marcin86junior/MegaPictureUploadREST.git .
	cd django_rest_imageupload_backend\
	"Open Doker Desktop"
	docker-compose run web python3 manage.py migrate
	docker-compose run web python3 manage.py migrate --run-syncdb
	docker-compose run web python3 manage.py loaddata group.json users.json data.json
	docker-compose up
	Test:
	docker-compose run web python3 manage.py test


Fixtures
--------


	Data included in fixtures:
	User / Password / Group:
	b1 / 123 / Basic
	p2 / 123 / Premium
	e3 / 123 / Enterprice
	c4 / 123 / Custom
	+ for all users added 2 diffrent data pictures (without pictures)


Issues
------


	At the moment there are few issuse:

	- docker have differnt PATH so it crash after upload pictures (one test is E), so it's
	  better to copy to local folder and run it
	- In enterprise and custom group we don't have expire links but we have expire time.
	  Django Expiring Token we will be added in future

