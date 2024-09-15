from django.contrib import admin
from django.utils.translation import gettext_lazy

class APECSAdmin(admin.AdminSite):
    site_header = gettext_lazy("APECS administration")
    site_title = gettext_lazy("APECS site admin")