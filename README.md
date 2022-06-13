EmenuRESTAPI 
===========

![alt text](https://github.com/marcin86junior/EmenuRESTAPI/blob/main/readme.PNG?raw=true)

Requirements:

	Python 3.8.x
	Django 3.0.7

Installation:

	Create new folder "EmenuREST" and open it:
	git clone https://github.com/marcin86junior/EmenuRESTAPI .
	python -m venv myvenv
	.\myvenv\Scripts\activate
	pip install -r requirements.txt
	cd myproject\
	python manage.py migrate
	python manage.py createsuperuser
	python  manage.py loaddata eMenu\fixtures\data.json --app eMenu
	python manage.py runserver 

Testing:

	python manage.py test eMenu
	coverage run --source='.' --omit='*migrations*,*init*,*wsgi*,*asgi*,*urls*,*manage*,*admin*,*apps*,*settings*,*test*,*seriali*' manage.py test eMenu
	coverage html

Docker:

	Create new folder "EmenuREST" and open it:
	git clone https://github.com/marcin86junior/EmenuRESTAPI .
	cd myproject
	Open Doker Desktop:
	docker-compose run web python3 manage.py migrate
	docker-compose run web python3 manage.py loaddata data.json --app eMenu
	Run app:
	docker-compose up
	Test:
	docker-compose run web python3 manage.py test eMenu
