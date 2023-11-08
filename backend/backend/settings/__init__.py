"""
Django settings for backend project.

Generated by 'django-admin startproject' using Django 4.1.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

import json
from pathlib import Path
from django.core.exceptions import ImproperlyConfigured
import pymysql

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = str(Path(__file__).resolve().parent.parent.parent)


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
def get_external_value(filename: str, key: str):
    try:
        with open(filename, encoding='utf-8') as file:
            json_value = json.loads(file.read())
    except FileNotFoundError as error:
        raise ImproperlyConfigured(f'file \'{filename}\' not found') from error
    try:
        return json_value[key]
    except KeyError as error:
        raise ImproperlyConfigured(f'key \'{key}\' does not exist') from error


SECRET_KEY = get_external_value(f'{BASE_DIR}/backend/.secrets/secret_key.json', 'secret_key')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Application definition
INSTALLED_APPS = [
    'corsheaders',
    'daphne',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework.authtoken',
    'dj_rest_auth',
    'drf_yasg',
    'storages',
    'pitapat',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'backend.urls'

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

WSGI_APPLICATION = 'backend.wsgi.application'
ASGI_APPLICATION = 'backend.asgi.application'
CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels_redis.core.RedisChannelLayer",
        "CONFIG": {
            "hosts": [("127.0.0.1", 6379)],
        },
    },
}


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

pymysql.install_as_MySQLdb()

db = get_external_value(f'{BASE_DIR}/backend/.secrets/db.json', 'local')

DATABASES = {
    'default': {
        'ENGINE': db['ENGINE'],
        'HOST': db['HOST'],
        'PORT': db['PORT'],
        'USER': db['USER'],
        'PASSWORD': db['PASSWORD'],
        'NAME': db['NAME'],
    }
}


# Authentication
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_USER_MODEL = 'pitapat.User'

AUTH_PASSWORD_VALIDATORS = [
    # {
    #     'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    # },
    # {
    #     'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    # },
    # {
    #     'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    # },
    # {
    #     'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    # },
]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.TokenAuthentication',
    ],
}


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_ROOT = f'{BASE_DIR}/static'
STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'pitapat.models.custom_field.unsigned_auto_field.UnsignedAutoField'

# AWS S3

IMAGE_URL = get_external_value(f'{BASE_DIR}/backend/.secrets/s3.json', 'url')

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
AWS_S3_SECURE_URLS = False
AWS_QUERYSTRING_AUTH = False

AWS_S3_ACCESS_KEY_ID = get_external_value(f'{BASE_DIR}/backend/.secrets/s3.json', 'access_key_id')
AWS_S3_SECRET_ACCESS_KEY = get_external_value(f'{BASE_DIR}/backend/.secrets/s3.json', 'secret_access_key')
AWS_STORAGE_BUCKET_NAME = 'pitapatcampus'

CORS_ORIGIN_WHITELIST = []
CSRF_TRUSTED_ORIGINS = CORS_ORIGIN_WHITELIST

SECURE_HSTS_SECONDS = 31536000

# Email Verification

EMAIL_BACKEND = get_external_value(f'{BASE_DIR}/backend/.secrets/email.json', 'EMAIL_BACKEND')
EMAIL_HOST = get_external_value(f'{BASE_DIR}/backend/.secrets/email.json', 'EMAIL_HOST')
EMAIL_PORT = get_external_value(f'{BASE_DIR}/backend/.secrets/email.json', 'EMAIL_PORT')
EMAIL_HOST_USER = get_external_value(f'{BASE_DIR}/backend/.secrets/email.json', 'EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = get_external_value(f'{BASE_DIR}/backend/.secrets/email.json', 'EMAIL_HOST_PASSWORD')
EMAIL_USE_TLS = get_external_value(f'{BASE_DIR}/backend/.secrets/email.json', 'EMAIL_USE_TLS')
DEFAULT_FROM_EMAIL = get_external_value(f'{BASE_DIR}/backend/.secrets/email.json', 'DEFAULT_FROM_EMAIL')

CRYPTO_KEY = get_external_value(f'{BASE_DIR}/backend/.secrets/aes.json', 'key')
CRYPTO_IV = get_external_value(f'{BASE_DIR}/backend/.secrets/aes.json', 'iv')
