import os
import raven
from .partials import *


DEBUG = False

ALLOWED_HOSTS = [
    "localhost:8000"
]

INSTALLED_APPS += [
    'raven.contrib.django.raven_compat',
]


RAVEN_CONFIG = {
    'dsn': 'https://e17419867f4349bd8aa4557a1659608f:b46ab1f463c04daeba896efa99ccaa87@app.getsentry.com/72890',
}


STATICFILES_STORAGE = 'classiclass.storage.S3PipelineCachedStorage'
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'

AWS_ACCESS_KEY_ID = os.environ.get("AWS_ACCESS_KEY_ID")
AWS_STORAGE_BUCKET_NAME = os.environ.get("AWS_STORAGE_BUCKET_NAME")
AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY")
AWS_S3_CUSTOM_DOMAIN = 'd9naji6jb4nd.cloudfront.net'

AWS_S3_URL_PROTOCOL = 'https'

STATIC_URL = "https://d9naji6jb4nd.cloudfront.net/"
