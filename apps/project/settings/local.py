from .base import *

DEBUG = TEMPLATE_DEBUG = True


# Send emails to the console
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# or, use GMail
#EMAIL_USE_TLS = True
#EMAIL_HOST = 'smtp.gmail.com'
#EMAIL_PORT = 587
#EMAIL_HOST_USER = 'USERNAME@gmail.com'
#EMAIL_HOST_PASSWORD = 'PASSWORD'

DEBUG_APPS = (
    'debug_toolbar',
    'django_extensions',
)
INTERNAL_IPS = ('127.0.0.1',)
MIDDLEWARE_CLASSES += ('debug_toolbar.middleware.DebugToolbarMiddleware',)

# Don't show DDT in the admin
import re
def show_toolbar(request):
    uri = request.get_full_path()
    if re.match(r'/admin/', uri):
        return False
    return True
 
DEBUG_TOOLBAR_CONFIG = {
    'SHOW_TOOLBAR_CALLBACK': show_toolbar,
    #'INTERCEPT_REDIRECTS': False
}


INSTALLED_APPS += DEBUG_APPS