from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '^j=omww9y21hh&v8mtm*jz2uyfn^zpfc436yj_aebtcf8g@1%+'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'testdb',
        'USER': 'admin',
        'PASSWORD': 'admin',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
