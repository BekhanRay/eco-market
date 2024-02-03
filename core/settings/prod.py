
from pathlib import Path

import config

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

DATABASES = {
   'default': {
       'ENGINE': 'django.db.backends.postgresql',
       'NAME': config.POSTGRES_DB,
       'USER': config.POSTGRES_USER,
       'PASSWORD': config.POSTGRES_PASSWORD,
       'HOST': config.POSTGRES_HOST,
       'PORT': config.POSTGRES_PORT,
    }
}

# CSRF
CSRF_USE_SESSIONS = True
# CSRF_TRUSTED_ORIGINS = []



# Cors

CORS_ALLOW_ALL_ORIGINS = True
CORS_ALLOW_CREDENTIALS = True
CORS_ALLOW_PRIVATE_NETWORK = True
CORS_ALLOWED_ALL_CREDENTIALS = True

CORS_ALLOW_METHODS = [
    'DELETE',
    'GET',
    'OPTIONS',
    'PATCH',
    'POST',
    'PUT',
]

CORS_ALLOW_HEADERS = [
    'accept',
    'accept-encoding',
    'authorization',
    'content-type',
    'dnt',
    'origin',
    'user-agent',
    'x-csrftoken',
    'x-requested-with',
]
