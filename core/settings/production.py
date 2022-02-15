
from .base import *

import dj_database_url 
from decouple import config

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 't80himqmf4q_u^*xcpl@0%(xcr28$04w^6s+)4_lo7n3dbp(g8'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['*']


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': dj_database_url.config(
        default=config('DATABASE_URL')
    )
}


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'