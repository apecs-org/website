from apecs.settings.base import * # noqa
from apecs.settings.util import get_env_read_file

import sentry_sdk
import posthog

SECRET_KEY = 'django-insecure-i+d5_bogqa!87o_ar&bjy-insdo@-1vuf6#8h=&w3z-9ps_z*&'

DEBUG = False

ALLOWED_HOSTS = ['127.0.0.1', '0.0.0.0', 'localhost']

WAGTAILADMIN_BASE_URL = []

PREFERRED_SCHEME = "https"
CSRF_TRUSTED_ORIGINS = [f"{PREFERRED_SCHEME}://{host}" for host in ALLOWED_HOSTS]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "USER": 'postgres',
        "NAME": 'test_db',
        "PASSWORD": 'postgres',
        "PORT": 5432,
        "HOST": 'localhost',
    },
}

# Wagtail
WAGTAILADMIN_BASE_URL = []