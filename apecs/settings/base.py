"""
Django settings for the APECS website.
"""

from pathlib import Path
import os
from apecs.settings.util import get_env_read_file

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


ALLOWED_HOSTS = []


# Application definition
INSTALLED_APPS = [
    'apecs.core',
    'apecs.auth',
    'apecs.cms',

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
    "django.middleware.security.SecurityMiddleware",
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
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
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

# Internationalization

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


AWS_ACCESS_KEY_ID = get_env_read_file("APECS_S3_ACCESS_KEY")
AWS_SECRET_ACCESS_KEY = get_env_read_file("APECS_S3_SECRET_KEY")

AWS_STORAGE_BUCKET_NAME = 'apecs-s1'
AWS_S3_ENDPOINT_URL = 'https://fra1.digitaloceanspaces.com'
AWS_S3_REGION_NAME = 'fra1'

AWS_LOCATION = 'files'

AWS_PUBLIC_MEDIA_LOCATION = f'{AWS_LOCATION}/media/public'
AWS_PRIVATE_MEDIA_LOCATION = f'{AWS_LOCATION}/media/private'

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
PRIVATE_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'mediafiles'

STATIC_ROOT = os.path.join(BASE_DIR, 'static/whitenoise')
STATIC_URL = 'static/'
STATICFILES_DIRS = [BASE_DIR / "static/dist"]


# Default primary key field type

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Wagtail
# https://docs.wagtail.org/en/stable/reference/settings.html#settings
WAGTAIL_SITE_NAME = 'APECS Website'
