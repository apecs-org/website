from apecs.settings.base import * # noqa
from apecs.settings.util import get_env_read_file

import sentry_sdk
import posthog

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = get_env_read_file("DJANGO_SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = get_env_read_file("DJANGO_DEBUG", default=False)

try:
    ALLOWED_HOSTS = os.environ.get("APECS_ALLOWED_HOSTS").split(",")
except AttributeError:
    # An attribute error is raised because no value was provided and
    # None has no attribute (i.e. method) called 'split'
    raise ValueError(
        "The 'APECS_ALLOWED_HOSTS' environment variable has to be specified"
    )

PREFERRED_SCHEME = "https"
CSRF_TRUSTED_ORIGINS = [f"{PREFERRED_SCHEME}://{host}" for host in ALLOWED_HOSTS]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "USER": get_env_read_file("APECS_DB_USER"),
        "NAME": get_env_read_file("APECS_DB_NAME"),
        "PASSWORD": get_env_read_file("APECS_DB_PASSWORD"),
        "HOST": get_env_read_file("APECS_DB_HOST"),
        "PORT": get_env_read_file("APECS_DB_PORT", default=5432),
    },
}

# Wagtail
WAGTAILADMIN_BASE_URL = []

# SENTRY CONFIGURATION
sentry_sdk.init(
    dsn= get_env_read_file("APECS_SENTRY_DSN"),
    send_default_pii=True,
    traces_sample_rate=1.0,
    release=APECS_VERSION,
)

# POSTHOG CONFIGURATION
posthog.api_key = get_env_read_file("APECS_POSTHOG_API_KEY")
posthog.host = 'https://eu.posthog.com'

# LOGGING

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'root': {
        'level': 'WARNING',
        'handlers': ['sentry'],
    },
    'formatters': {
        'verbose': {
            'format': '{levelname} {asctime} {module} {message}',
            'style': '{',
        },
    },
    'handlers': {
        'sentry': {
            'level': 'WARNING',  # Only send WARNING and above
            'class': 'sentry_sdk.integrations.logging.EventHandler',
        },
        'console': {
            'level': 'INFO',  # Local console output for dev
            'class': 'logging.StreamHandler',
            'formatter': 'verbose',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console', 'sentry'],
            'level': 'WARNING',
            'propagate': False,
        },
        'django.request': {
            'handlers': ['console', 'sentry'],
            'level': 'ERROR',
            'propagate': False,
        },
        # Optional: catch all other warnings/errors
        '': {
            'handlers': ['console', 'sentry'],
            'level': 'WARNING',
        },
    },
}
