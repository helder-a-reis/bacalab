from .base import *

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'bacalab',
        'USER': os.environ.get('DB_USER'),
        'PASSWORD': os.environ.get('DB_PWD'),
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}
