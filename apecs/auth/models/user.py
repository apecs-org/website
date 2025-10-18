__all__ = ["User"]

from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    affiliation = models.CharField(max_length=200, default='')
    profile_picture = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='user_profile_picture'
    )
