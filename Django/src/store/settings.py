from pathlib import Path
from utils.appConfig import AppConfig

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-t(+lcqz!-o$$cv&kcf_54=)oic7odpz#&%#*ao@-t2b$h^*3sp'
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
ALLOWED_HOSTS = ["*"]



INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    #register Django REST Framework
    "rest_framework",
    
    #register api app that we created with: >py manage.py startapp api
    "api.apps.ApiConfig", 
    "store",

    # Register django-cors-headers:
    "corsheaders", # >pip install django-cors-headers
]

MIDDLEWARE = [
    # Enable CORS (need to be as high as possible):
    "corsheaders.middleware.CorsMiddleware",

    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


# Configure CORS:
CORS_ALLOW_ALL_ORIGINS = True # Enable all websites. To enable specific websites instead: CORS_ALLOWED_ORIGINS = ["http://mysite.com", "http://another-site.com"]
CORS_ALLOW_CREDENTIALS = True # Allow sending Cookies in CORS (needed for maintaining server-side sessions)


ROOT_URLCONF = 'store.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'store.wsgi.application'


# Configure MySQL database:
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'HOST': AppConfig.mysql_host,
        'USER': AppConfig.mysql_user,
        'PASSWORD': AppConfig.mysql_password,
        'NAME': AppConfig.mysql_database,
        'PORT': '3306',
        'OPTIONS': {
            'charset': 'utf8mb4'
        }
    }
}


AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

STATIC_URL = 'static/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
