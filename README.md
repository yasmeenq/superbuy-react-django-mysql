# Project Overview

## 1. MySQL Workbench -Database:
(Summary TDL)

## 2. Django -Backend:

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

### Run App 😃:
```sh
cd ..  # (get out of src)
py src/manage.py runserver 8001
```
Now go to [http://127.0.0.1:8001/api/yourURL](http://127.0.0.1:8001/api/yourURL)

**Note:** you can test it in Postman 


## 3. React-Typescript -Frontend: 

### Start with Installations:
```sh
#installing react 
>npm create vite@latest <name> –template react-ts #for js it's just react
>npm install
>npm run dev

#installing and creating components
>npm i -g react-cli-snippets #(only ts for js u have to create them manually)
>create fc <name> –module #(only ts for js u have to create them manually)

#installing router
>npm i react-router-dom #(js)
>npm i react-router-dom @types/react-router-dom  #(ts)

#installing redux
>npm install @reduxjs/toolkit

#install axios
>npm i axios 

```

### Clear Up your files:
delete whats not needed like App.tsx and the code inside index.css

### Create Components: 
1. create LayoutArea: 
    -Create Layout Component
    -Create Header Component
    -Create Footer Component
2. create Router Component:
    create a router function and use it in Layout.

### Added Notify Library:
for this project I used react-hot-toast, follow the documentations to use.
[https://www.npmjs.com/package/react-hot-toast](https://www.npmjs.com/package/react-hot-toast) 

### Create Models for Databases:
>create model ProductModel

### Create AppConfig:
>create util AppConfig (store it inside util)
we'll use it to store all API's urls  

### Create Service: 
>create service ProductService 
fetching and requesting from API's.
Handling databases.
>npm i axios 