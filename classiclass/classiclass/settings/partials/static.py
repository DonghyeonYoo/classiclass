import os

from .application import PROJECT_ROOT_DIR
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

# css, js ,image resourece
STATIC_URL = '/static/'
# file, pdf, image from user
MEDIA_URL = '/media/'
# 미디어에는 유저가올린거
MEDIA_ROOT = os.path.join(PROJECT_ROOT_DIR, "dist", "media")
# 스태틱에는 개발자가올린거 즉 css pdf 파일등
STATIC_ROOT = os.path.join(PROJECT_ROOT_DIR, "dist", "static")
