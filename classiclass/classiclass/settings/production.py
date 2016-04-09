from .partials import *


DEBUG = False

ALLOWED_HOSTS = [
    "localhost:8000"
]


INSTALLED_APPS += [
    'raven.contrib.django.raven_compat',
]


AVEN_CONFIG = {
    'dsn': 'https://b796b923ff314cba8f55ab78c16c4584:61c165e026514687ab5e14e2d9482332@app.getsentry.com/72871',
}
