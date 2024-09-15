from apecs.settings.base import * # noqa
from apecs.settings.util import get_env_read_file


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
