from django.contrib import admin

from apecs.compass.models.article import Article
from apecs.compass.models.guidebook import Guidebook, Chapter

from wagtail_modeladmin.options import ModelAdmin, modeladmin_register


class WagtailArticleAdmin(ModelAdmin):
    model = Article
    menu_label = "Articles"
    menu_icon = "doc-full-inverse"  # Use a Wagtail icon
    add_to_settings_menu = False
    exclude_from_explorer = False
    list_display = ("title", "first_published_at", "live")
    search_fields = ("title",)


class DjangoArticleAdmin(admin.ModelAdmin):
    filter_horizontal = ('authors', 'editors')
    readonly_fields = ['body', 'path', 'depth', 'numchild', 'content_type',
                       'owner']


modeladmin_register(WagtailArticleAdmin)

admin.site.register(Article, DjangoArticleAdmin)
admin.site.register(Guidebook)
admin.site.register(Chapter)
