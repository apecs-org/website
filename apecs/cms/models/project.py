from django.db import models

from apecs.auth.models import User


class Project(models.Model):
    name = models.CharField(max_length=200, default='')
    short_name = models.CharField(max_length=60, default='')
    staff = models.ManyToManyField(User, related_name='project_staff', blank=True)
    logo = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='project_logo'
    )

    def __str__(self):
        return self.short_name
