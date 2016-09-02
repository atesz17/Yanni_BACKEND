from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = get_env_variable("YANNI_SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': get_env_variable("YANNI_DB_NAME"),
        'USER': get_env_variable("YANNI_DB_USER"),
        'PASSWORD': get_env_variable("YANNI_DB_PASSWORD"),
        'HOST': get_env_variable("YANNI_DB_HOST"),
        'PORT': get_env_variable("YANNI_DB_PORT"),
    }
}

reminder_for_myself = """
    Check out base.py and https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/ before going to production
    """

raise ImproperlyConfigured(reminder_for_myself)