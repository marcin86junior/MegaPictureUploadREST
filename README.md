MegaPictureUploadREST
=====================

### Your own upload picture website in Django/REST

![alt text](http://marcin86.pythonanywhere.com/static/MegaUploadpic.PNG)

Overview
--------

* **Freedom to build what you want**  MegaPictureUploadREST is an open-source 
webiste for upload pictures..............

* **Diffrent groups for users**  MegaPictureUploadREST lets you to chose groups
for clients/users to generate specyfic thumb........ We have 4 groups: ......

* **Special group entrprise** MegaPictureUploadREST is designed to fit a wide
range of uses 

* **Cross platform** MegaPictureUploadREST runs on Windows, macOS and Linux
operating systems.

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


	To report an issue please:
	- First post to forum to verify the issue; 
	- Link forum thread to bug tracker ticket and vice-a-versa; 
	- Use the most updated stable or development versions of FreeCAD; 
	- Post version info from eg. `Help > About FreeCAD > Copy to clipboard`; 
	- Post a Step-By-Step explanation on how to recreate the issue; 
	- Upload an example file to demonstrate problem. 

