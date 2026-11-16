from .base import *
from decouple import config, Csv
import dj_database_url

DEBUG = False

ALLOWED_HOSTS = config(
    'ALLOWED_HOSTS',
    cast=Csv()
)

DATABASES = {
    'default': dj_database_url.config(
        # Replace this value with your local database's connection string.
        default='postgresql://fic:8q3EPgE3DBEF9LVciW2oNSvi0zB09r5K@dpg-dbp1m1rbc2fs73dqssbg-a/fic_wma2',
        conn_max_age=600
    )
}

ROOT_URLCONF = 'gerenciamento.urls'

WSGI_APPLICATION = 'gerenciamento.wsgi.application'
ASGI_APPLICATION = 'gerenciamento.asgi.application'

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'

STORAGES = {
    'default': {
        'BACKEND': 'django.core.files.storage.FileSystemStorage',
    },
    'staticfiles': {
        'BACKEND': 'whitenoise.storage.CompressedManifestStaticFilesStorage',
    },
}

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True