from django.contrib import admin

from apecs.compass.models.article import Article
from apecs.compass.models.guidebook import Guidebook, Chapter
from apecs.compass.models.resource import (
    Resource,
    ResourceType,
    ResourceCategory,
    ResourceKeyword,
    ResourceEnvironment,
    ResourceRegion,
)

from wagtail_modeladmin.options import ModelAdmin, modeladmin_register


class WagtailArticleAdmin(ModelAdmin):
    model = Article
    menu_label = "Articles"
    menu_icon = "doc-full-inverse"
    add_to_settings_menu = False
    exclude_from_explorer = False
    list_display = (
        "title",
        "first_published_at",
        "live",
    )
    search_fields = (
        "title",
    )


class DjangoArticleAdmin(admin.ModelAdmin):
    filter_horizontal = (
        "authors",
        "editors",
    )
    readonly_fields = [
        "body",
        "path",
        "depth",
        "numchild",
        "content_type",
        "owner",
    ]


@admin.register(ResourceType)
class ResourceTypeAdmin(admin.ModelAdmin):
    list_display = (
        "name",
    )

    search_fields = (
        "name",
    )


@admin.register(ResourceCategory)
class ResourceCategoryAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "slug",
        "description",
    )

    search_fields = (
        "name",
        "slug",
        "description",
    )

    prepopulated_fields = {
        "slug": ("name",),
    }


@admin.register(ResourceRegion)
class ResourceRegionAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "slug",
    )

    search_fields = (
        "name",
        "slug",
    )

    prepopulated_fields = {
        "slug": ("name",),
    }


@admin.register(ResourceEnvironment)
class ResourceEnvironmentAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "slug",
    )

    search_fields = (
        "name",
        "slug",
    )

    prepopulated_fields = {
        "slug": ("name",),
    }


@admin.register(ResourceKeyword)
class ResourceKeywordAdmin(admin.ModelAdmin):
    list_display = (
        "name",
    )

    search_fields = (
        "name",
    )


@admin.register(Resource)
class ResourceAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "resource_type",
        "author",
        "is_active",
        "updated_at",
    )

    list_filter = (
        "resource_type",
        "categories",
        "is_active",
    )

    search_fields = (
        "title",
        "author",
    )

    list_editable = (
        "is_active",
    )

    autocomplete_fields = (
        "resource_type",
    )

    filter_horizontal = (
        "categories",
        "keywords",
    )

    @admin.display(description="Categories")
    def display_categories(self, obj):
        return ", ".join(
            category.name
            for category in obj.categories.all()
        )

    @admin.display(description="Keywords")
    def display_keywords(self, obj):
        return ", ".join(
            keyword.name
            for keyword in obj.keywords.all()
        )

    @admin.display(description="Regions")
    def display_regions(self, obj):
        return ", ".join(
            keyword.name
            for keyword in obj.regions.all()
        )

    @admin.display(description="Environments")
    def display_environments(self, obj):
        return ", ".join(
            keyword.name
            for keyword in obj.environments.all()
        )


modeladmin_register(WagtailArticleAdmin)

admin.site.register(Article, DjangoArticleAdmin)
admin.site.register(Guidebook)
admin.site.register(Chapter)