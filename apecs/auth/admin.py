from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin

from apecs.auth.models import User


class CustomDjangoUserAdmin(DjangoUserAdmin):
    fieldsets = DjangoUserAdmin.fieldsets + (
        (None, {'fields': ('affiliation', 'profile_picture')}),
    )


admin.site.register(User, CustomDjangoUserAdmin)
