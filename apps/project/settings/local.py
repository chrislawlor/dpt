from .base import *

DEBUG = TEMPLATE_DEBUG = True


# Send emails to the console
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

DEBUG_APPS = (
    'debug_toolbar',
    'django_extensions',
)
INTERNAL_IPS = ('127.0.0.1',)
MIDDLEWARE_CLASSES += ('debug_toolbar.middleware.DebugToolbarMiddleware',)


INSTALLED_APPS += DEBUG_APPS