1.	started with Database (summary TDL)

2.	Django Backend:
Start with installations:
    1.	py -m venv env
    2.	env/scripts/activate
    3.	pip install django
    4.	pip install djangorestframework
    5.	pip install mysqlclient
    6.	django-admin startproject store src (create src folder first)
    7.	cd src
    8.	py manage.py startapp api (this is a way to create apps in Django instead of api write your app name)
    9.	pip install django-cors-headers
    10.	pip install python-dotenv
    11.	pip freeze > requirements.txt

Configure Settings:
    1. add the apps you downloaded to installed apps.
    2. connect the database{
        a. create utils>appConfig to store the keys.
        b. store the values in .env for privacy.
    }

Create Models and Serializers:
    1. create models for your tables - don't forget to add
    class Meta to your model.
    2. then create serializers for your models (converts to json).

Make Migrations:
    py manage.py makemigrations
    py manage.py migrate api
    note: if you already created your tables in mySQL workbench,
    you might need different steps. like fake migrations. google
    your errors.

Create Views:
    its Django rest framework (DRF) thingy to 
    fetch data from client => save to Database.

Create URLs:
    1. create urls for api.
    2. add api urls to main app urls.

Run App =D :
    cd .. (get out of src)
    py src/manage.py runserver 8001
    now go to http://127.0.0.1:8001/api/yourURL 
     
