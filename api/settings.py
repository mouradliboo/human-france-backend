"""
Django settings for api project.

Generated by 'django-admin startproject' using Django 5.1.4.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

from pathlib import Path
from datetime import timedelta
import cloudinary
import cloudinary.uploader
import cloudinary.api
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-sa!g#^n3-c%q+u=ypf2l+26h15)s5mn@^_=^-gyxrx21x9vjub'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True



# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
     'corsheaders',
      'cloudinary',
    'cloudinary_storage',
     'rest_framework',
    'rest_framework_simplejwt',
    'django.contrib.sessions',
    'django_filters',
    'drf_yasg',
    'django.contrib.messages',
    'django.contrib.staticfiles',
 'planning',
    'authentication',
    'users',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
      'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'api.urls'

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

WSGI_APPLICATION = 'api.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': "mediumclone_humanfrance",
        'USER': "367579_abdallah",
        'PASSWORD':"abdallah",
        'HOST': 'mysql-mediumclone.alwaysdata.net',  # Or your MySQL server's IP/hostname
        'PORT': '3306',  # Default MySQL port
         'OPTIONS': {
            'charset': 'utf8mb4',  # Ensures proper UTF-8 support
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
        }
    }
}
  
#cloud config
# settings.py


CLOUDINARY_STORAGE = {
    'cloud_name': 'dac02kjvd',
    'api_key': '673151423632799',
    'api_secret': 'C4P2uhSrZB8SsQac3BAXdnY3S74',
}
cloudinary.config(
    cloud_name=CLOUDINARY_STORAGE['cloud_name'],
    api_key=CLOUDINARY_STORAGE['api_key'],
    api_secret=CLOUDINARY_STORAGE['api_secret']
)

# Set Cloudinary as the default storage for media files
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

ALLOWED_HOSTS = ['human-france-api.up.railway.app',"web-production-e4d2d.up.railway.app", 
                 'localhost', '127.0.0.1'
                 ,"192.168.43.47"]
CORS_ALLOWED_ORIGINS = [
    'http://localhost:3000',
    'https://human-france-front-zisj.vercel.app',
    # Add other allowed domains here
]




EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')
DEFAULT_FROM_EMAIL = os.getenv('DEFAULT_FROM_EMAIL')

#jwt config 

# put on your settings.py file below INSTALLED_APPS
AUTH_USER_MODEL = 'authentication.CustomUser'

REST_FRAMEWORK = {
   
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.AllowAny',  # Allow any user to access views
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        # Optional: You can remove or comment this out if authentication is not required globally
        # 'rest_framework_simplejwt.authentication.JWTAuthentication', 
    ),
}



SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(days=1),
    'SLIDING_TOKEN_REFRESH_LIFETIME': timedelta(days=5),
    'SLIDING_TOKEN_LIFETIME': timedelta(days=30),
    'SLIDING_TOKEN_REFRESH_LIFETIME_LATE_USER': timedelta(days=1),
    'SLIDING_TOKEN_LIFETIME_LATE_USER': timedelta(days=30),
}
CSRF_TRUSTED_ORIGINS = ['https://human-france-api.up.railway.app',"https://web-production-e4d2d.up.railway.app"]


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

# settings.py

STATIC_URL = '/static/'  # Required setting





# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field


# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field



# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

#swagger 
SPECTACULAR_SETTINGS = {
    'TITLE': 'My API',
    'DESCRIPTION': 'API documentation',
    'VERSION': '1.0.0',
    'SERVERS': [
        {'url': '/api/v1', 'description': 'Base URL for API v1'},
    ],
}

