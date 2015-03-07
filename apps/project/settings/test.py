from .base import *

# Test Settings
# TEST_RUNNER = 'discover_runner.DiscoverRunner'
# TEST_DISCOVER_TOP_LEVEL = PROJECT_ROOT.child('tests')
# TEST_DISCOVER_ROOT = PROJECT_ROOT.child('tests')
# TEST_DISCOVER_PATTERN = 'test_*'


# IN-MEMORY TEST DATABASE
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": ":memory:",
        "USER": "",
        "PASSWORD": "",
        "HOST": "",
        "PORT": "",
    },
}
