from .base import *


DEBUG = True

ALLOWED_HOSTS = get_external_value(f'{BASE_DIR}/backend/.secrets/host.json', 'local')

CORS_ORIGIN_WHITELIST = get_external_value(f'{BASE_DIR}/backend/.secrets/cors_whitelist.json', 'local')
CSRF_TRUSTED_ORIGINS = CORS_ORIGIN_WHITELIST

SECURE_SSL_REDIRECT = False
SESSION_COOKIE_SECURE = False
CSRF_COOKIE_SECURE = False
SECURE_HSTS_INCLUDE_SUBDOMAINS = False
SECURE_HSTS_PRELOAD = False


# Database

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

# Media

MEDIA_URL = 'media/'
MEDIA_ROOT = BASE_DIR / 'media'
