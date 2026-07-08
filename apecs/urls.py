from django.contrib import admin
from django.urls import path, include

from wagtail.admin import urls as wagtailadmin_urls
from wagtail.documents import urls as wagtaildocs_urls

from django.urls import path
from wagtail import urls as wagtail_urls

urlpatterns = [
    # wagtail
    path('admin/cms/', include(wagtailadmin_urls)),
    path('documents/', include(wagtaildocs_urls)),

    # django
    path('admin/db/', admin.site.urls),

    # apecs
    path('auth/', include('apecs.auth.urls')),
    path('', include('apecs.cms.urls')),
    path('compass/', include('apecs.compass.urls', namespace="compass")),

    # api
    path('api/v1/', include('apecs.api.urls', namespace="v1")),

]

urlpatterns += [
    path('', include(wagtail_urls)),
]