MegaPictureUploadREST
===========

![alt text](https://github.com/marcin86junior/EmenuRESTAPI/blob/main/readme.PNG?raw=true)

Requirements:

	Python 3.8.x
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
	python manage.py createsuperuser
	-> marcin / pass:123
	-> create groups 3: Basic, Premium and Enterprise
	-> add tomek / pass: tomektomek
	-> add tomek to Basic group in admin
	#python manage.py loaddata eMenu\fixtures\data.json --app eMenu
	python manage.py runserver 

#Testing:

	python manage.py test eMenu
	coverage run --source='.' --omit='*migrations*,*init*,*wsgi*,*asgi*,*urls*,*manage*,*admin*,*apps*,*settings*,*test*,*seriali*' manage.py test eMenu
	coverage html

Docker:

	Create new folder "MegaPictureUploadREST" and open it:
	git clone https://github.com/marcin86junior/MegaPictureUploadREST.git .
	cd myproject
	Open Doker Desktop:
	docker-compose run web python3 manage.py migrate
	#docker-compose run web python3 manage.py loaddata data.json --app eMenu
	Run app:
	docker-compose up
	#Test:
	#docker-compose run web python3 manage.py test eMenu
