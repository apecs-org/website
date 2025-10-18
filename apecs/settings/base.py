"""
Django settings for the APECS website.
"""

from pathlib import Path
import os

from apecs.settings.util import get_env_read_file
from apecs import __version__

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

APECS_VERSION = __version__

ALLOWED_HOSTS = []

USE_X_FORWARDED_HOST = True
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

# Application definition
INSTALLED_APPS = [
    'apecs.core',
    'apecs.auth',
    'apecs.cms',
    'apecs.compass',

    'wagtail.contrib.forms',
    'wagtail.contrib.redirects',
    'wagtail.embeds',
    'wagtail.sites',
    'wagtail.users',
    'wagtail.snippets',
    'wagtail.documents',
    'wagtail.images',
    'wagtail.search',
    'wagtail.admin',
    'wagtail',
    'taggit',
    'modelcluster',
    'storages',
    'wagtail_modeladmin',

    'django_celery_beat',
    'django_celery_results',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'whitenoise.runserver_nostatic',
    'django.contrib.staticfiles',

    'django_htmx',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'wagtail.contrib.redirects.middleware.RedirectMiddleware',
    'django_htmx.middleware.HtmxMiddleware',
]

ROOT_URLCONF = 'apecs.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'apecs.wsgi.application'

# Database

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': get_env_read_file('POSTGRES_DB', 'apecs'),
        'USER': get_env_read_file('POSTGRES_USER', 'apecsuser'),
        'PASSWORD': get_env_read_file('POSTGRES_PASSWORD', 'admin'),
        'HOST': get_env_read_file('POSTGRES_HOST', 'localhost'),
        'PORT': get_env_read_file('POSTGRES_PORT', '5432'),
    }
}

STORAGES = {
    "default": {
        "BACKEND": "storages.backends.s3.S3Storage",
        "OPTIONS": {
        },
    },
    "media": {
        "BACKEND": "storages.backends.s3.S3Storage",
        "OPTIONS": {
        },
    },
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
    },
}

# Password validation

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

AUTH_USER_MODEL = 'apecsauth.User'

# INTERNATIONALIZATION

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# S3 OBJECT STORAGE

AWS_ACCESS_KEY_ID = get_env_read_file("APECS_S3_ACCESS_KEY") # SECRET
AWS_SECRET_ACCESS_KEY = get_env_read_file("APECS_S3_SECRET_KEY") # SECRET

AWS_STORAGE_BUCKET_NAME = 'apecs-s3b1'
AWS_S3_REGION_NAME = 'fsn1'
AWS_S3_URL = 'your-objectstorage.com'

AWS_S3_ENDPOINT_URL = f"https://{AWS_S3_REGION_NAME}.{AWS_S3_URL}"
AWS_S3_CUSTOM_DOMAIN = f"{AWS_STORAGE_BUCKET_NAME}.{AWS_S3_REGION_NAME}.{AWS_S3_URL}"

AWS_LOCATION = 'files'

AWS_PUBLIC_MEDIA_LOCATION = f'{AWS_LOCATION}/media/public'
AWS_PRIVATE_MEDIA_LOCATION = f'{AWS_LOCATION}/media/private'

DEFAULT_FILE_STORAGE = 'apecs.storages.PublicMediaStorage'
PRIVATE_FILE_STORAGE = 'apecs.storages.PrivateMediaStorage'

# MEDIA AND STATIC FILES

MEDIA_URL = f"https://{AWS_S3_CUSTOM_DOMAIN}/{AWS_PUBLIC_MEDIA_LOCATION}/"
PRIVATE_MEDIA_URL = f"https://{AWS_S3_CUSTOM_DOMAIN}/{AWS_PRIVATE_MEDIA_LOCATION}/"
MEDIA_ROOT = BASE_DIR / 'mediafiles'

STATIC_ROOT = os.path.join(BASE_DIR, 'static/whitenoise')
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / "static/dist"]

# Default primary key field type

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# WAGTAIL
# https://docs.wagtail.org/en/stable/reference/settings.html#settings
WAGTAIL_SITE_NAME = 'APECS Website'

# REDIS CONFIGURATION
REDIS_HOST = os.getenv("APECS_REDIS_HOST", "localhost")
REDIS_URL = f"redis://{REDIS_HOST}:6379/0"

CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.redis.RedisCache",
        "LOCATION": REDIS_URL,
    }
}

# CELERY CONFIGURATION
CELERY_BROKER_URL = os.environ.get('CELERY_BROKER_URL', REDIS_URL)
CELERY_RESULT_BACKEND = 'django-db'
CELERY_CACHE_BACKEND = 'django-cache'
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TIMEZONE = TIME_ZONE
CELERY_BEAT_SCHEDULER = 'django_celery_beat.schedulers:DatabaseScheduler'
CELERY_RESULT_EXTENDED = True
