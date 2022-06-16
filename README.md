MegaPictureUploadREST
===========

![alt text](http://marcin86.pythonanywhere.com/static/MegaUploadpic.PNG)

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
	python manage.py createsuperuser (marcin/123)
	python .\manage.py runserver
	
	-> Use link below to create users/passwords/groups:
	-> turn on #path('', views.create_users) in django_rest_imageupload_backend.urls
	http://127.0.0.1:8000/setup/  
	It will create next users and groups:
	b1 (pass:123) --> Basic group
	p2 (pass:123) --> Premium group
	e3 (pass:123) --> Enterprice group
	c4 (pass:123) --> CustomXX500x500 group
	###python manage.py loaddata eMenu\fixtures\data.json --app eMenu
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
	docker-compose run web python3 python manage.py migrate --run-syncdb
	docker-compose run web python3 manage.py loaddata group.json
	docker-compose run web python3 manage.py loaddata users.json
	docker-compose run web python3 manage.py loaddata data.json
	Run app:
	docker-compose up
	Test:
	docker-compose run web python3 manage.py test
