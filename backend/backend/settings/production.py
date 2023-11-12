from .base import *


DEBUG = False

ALLOWED_HOSTS = get_external_value(f'{BASE_DIR}/backend/.secrets/host.json', 'production')

CORS_ORIGIN_WHITELIST = get_external_value(f'{BASE_DIR}/backend/.secrets/cors_whitelist.json', 'production')
CSRF_TRUSTED_ORIGINS = CORS_ORIGIN_WHITELIST

SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True


# Database

db = get_external_value(f'{BASE_DIR}/backend/.secrets/db.json', 'production')
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


# AWS S3

IMAGE_URL = get_external_value(f'{BASE_DIR}/backend/.secrets/s3.json', 'url')

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
AWS_S3_SECURE_URLS = False
AWS_QUERYSTRING_AUTH = False

AWS_S3_ACCESS_KEY_ID = get_external_value(f'{BASE_DIR}/backend/.secrets/s3.json', 'access_key_id')
AWS_S3_SECRET_ACCESS_KEY = get_external_value(f'{BASE_DIR}/backend/.secrets/s3.json', 'secret_access_key')
AWS_STORAGE_BUCKET_NAME = 'pitapatcampus'
