from django.contrib import admin

from apecs.cms.models import Project


class DjangoProjectAdmin(admin.ModelAdmin):
    filter_horizontal = ('staff',)


admin.site.register(Project, DjangoProjectAdmin)
