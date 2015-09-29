from .settings import *


DEBUG = False

ALLOWED_HOSTS = ['52.16.36.133', 'benchserv']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.getenv('DATABASE_NAME', 'bench'),
        'USER': os.getenv('DATABASE_USER', 'bench'),
        'PASSWORD': os.getenv('DATABASE_PASSWORD', 'mark'),
        'HOST': os.getenv('DATABASE_HOST', '127.0.0.1'),
        'PORT': os.getenv('DATABASE_PORT', '5432'),
    }
}