from django.contrib import admin
from django.urls import path, include

from wagtail.admin import urls as wagtailadmin_urls
from wagtail.documents import urls as wagtaildocs_urls

urlpatterns = [
    # django
    path('admin/db/', admin.site.urls),

    # wagtail
    path('admin/cms/', include(wagtailadmin_urls)),
    path('documents/', include(wagtaildocs_urls)),

    # apecs
    path('', include('apecs.auth.urls')),
    path('', include('apecs.core.urls')),

    # api
    #path('api/v1/', include('apecs.api.urls', namespace="v1")),
]