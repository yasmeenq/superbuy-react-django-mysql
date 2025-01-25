# Project Overview

## 1. Started with Database (Summary TDL)

## 2. Django Backend

### Start with Installations:
```sh
py -m venv env
env/scripts/activate
pip install django
pip install djangorestframework
pip install mysqlclient
django-admin startproject store src  # (create src folder first)
cd src
py manage.py startapp api  # (this is a way to create apps in Django, instead of 'api', write your app name)
pip install django-cors-headers
pip install python-dotenv
pip freeze > requirements.txt
```

### Configure Settings:
1. Add the apps you downloaded to `INSTALLED_APPS`.
2. Connect the database:
   - Create `utils/appConfig` to store the keys.
   - Store the values in `.env` for privacy.

### Create Models and Serializers:
1. Create models for your tables - don't forget to add `class Meta` to your model.
2. Then create serializers for your models (converts to JSON).

### Make Migrations:
```sh
py manage.py makemigrations
py manage.py migrate api
```
> **Note:** If you already created your tables in MySQL Workbench, you might need different steps like fake migrations. Google your errors.

### Create Views:
Django REST Framework (DRF) is used to fetch data from the client and save it to the database.

### Create URLs:
1. Create URLs for `api`.
2. Add `api` URLs to the main app URLs.

### Run App 🚀:
```sh
cd ..  # (get out of src)
py src/manage.py runserver 8001
```
Now go to [http://127.0.0.1:8001/api/yourURL](http://127.0.0.1:8001/api/yourURL)