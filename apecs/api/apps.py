from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class APECSAPIAppConfig(AppConfig):
    name = "apecs.api"
    label = "apecsapi"
    verbose_name = _("APECS API")