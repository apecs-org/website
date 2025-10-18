__all__ = ["APECSAdminAppConfig"]

from django.contrib.admin.apps import AdminConfig


class APECSAdminAppConfig(AdminConfig):
    default_site = "apecs.admin.sites.APECSAdmin"