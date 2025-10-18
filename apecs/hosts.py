from django_hosts import patterns, host
from django.conf import settings

host_patterns = patterns('apecs',
    host(r'compass', 'compass.urls', name='compass'),
    host(r'(www.apecs.local|apecs.local)', settings.ROOT_URLCONF, name='www'),
)