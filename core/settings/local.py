from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 't80himqmf4q_u^*xcpl@0%(xcr28$04w^6s+)4_lo7n3dbp(g8'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'property management arkandha',
        'USER': 'postgres',
        'PASSWORD': 'newpassword',
        'HOST': '127.0.0.1',
        'DATABASE_PORT': '5432'
    }
}


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'



