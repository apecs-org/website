import os
from django.core.wsgi import get_wsgi_application
from whitenoise import WhiteNoise

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'apecs.settings.dev')

application = get_wsgi_application()

STATIC_ROOT = os.path.join(os.path.dirname(__file__), 'static/whitenoise')
application = WhiteNoise(application, root=STATIC_ROOT)