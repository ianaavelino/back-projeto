
from .base import *
from decouple import config, Csv

DEBUG = config('DEBUG', default=True, cast=bool)

ROOT_URLCONF = 'gerenciamento.urls'

ALLOWED_HOSTS = config(
    'ALLOWED_HOSTS',
    default='127.0.0.1,localhost',
    cast=Csv()
)
