from django.db import models


class ResourceType(models.Model):
    name = models.CharField(
        max_length=100,
        unique=True,
    )

    display_name = models.CharField(
        max_length=200,
        default="",
    )

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.display_name


class ResourceCategory(models.Model):
    name = models.CharField(
        max_length=255,
        default="",
    )

    slug = models.CharField(
        max_length=100,
        unique=True,
        null=True,
        blank=True,
    )

    description = models.TextField(
        blank=True,
    )

    def __str__(self):
        return self.name


class ResourceRegion(models.Model):
    name = models.CharField(
        max_length=255,
        default="",
    )

    slug = models.CharField(
        max_length=100,
        unique=True,
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.name


class ResourceEnvironment(models.Model):
    name = models.CharField(
        max_length=255,
        default="",
    )

    slug = models.CharField(
        max_length=100,
        unique=True,
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.name


class ResourceKeyword(models.Model):
    name = models.CharField(
        max_length=100,
        unique=True,
    )

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Resource(models.Model):
    title = models.CharField(
        max_length=255,
    )

    resource_type = models.ForeignKey(
        ResourceType,
        on_delete=models.PROTECT,
        related_name="resources",
    )

    categories = models.ManyToManyField(
        "ResourceCategory",
        related_name="resources",
        blank=True,
    )

    keywords = models.ManyToManyField(
        "ResourceKeyword",
        related_name="resources",
        blank=True,
    )

    regions = models.ManyToManyField(
        "ResourceRegion",
        related_name="resources",
        blank=True,
    )

    environments = models.ManyToManyField(
        "ResourceEnvironment",
        related_name="resources",
        blank=True,
    )

    author = models.CharField(
        max_length=255,
    )

    url = models.URLField(
        max_length=500,
    )

    is_active = models.BooleanField(
        default=True,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    updated_at = models.DateTimeField(
        auto_now=True,
    )

    class Meta:
        ordering = ["title"]

    def __str__(self):
        return self.title
