from django.utils.version import get_version
from .celery import app as celery_app

__all__ = ('celery_app',)

VERSION = (0, 0, 1, "alpha", 4)
__version__ = get_version(VERSION)