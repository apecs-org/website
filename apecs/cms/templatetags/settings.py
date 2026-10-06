from typing import Any

from django import template
from django.conf import settings as django_settings

register = template.Library()


@register.simple_tag
def settings(name: str, default="") -> Any:
    """Get settings from a template.

    Example usage:

        {% settings "DEBUG" %}

    With default value:

        {% settings "SOME_MISSING_SETTING" default="foo" %}

    """
    return getattr(django_settings, name, default)