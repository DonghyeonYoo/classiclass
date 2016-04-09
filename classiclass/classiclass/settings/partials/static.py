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

# classiclass.css > classiclass.230534623.css
STATICFILES_STORAGE = 'pipeline.storage.PipelineCachedStorage'

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'pipeline.finders.PipelineFinder',
)

PIPELINE = {
    'STYLESHEETS': {
        'vendor': {
            'source_filenames': (
                'css/vendor/*.css',
            ),
            'output_filename': 'css/vendor/vendor.css',
        },
        'style': {
            'source_filenames': (
                'css/*.css',
            ),
            'output_filename': 'css/style.css',
        },
    },
    'JAVASCRIPT': {
        'vendor': {
            'source_filenames': (
                'js/vendor/jquery-2.2.3.min.js',
                'js/vendor/bootstrap.min.js',
                'js/vendor/materialize.js',
                'js/vendor/summernote-ko-KR.js',
            ),
            'output_filename': 'js/vendor/vendor.js',
        },
        'classiclass': {
            'source_filenames': (
                'js/*.js',
            ),
            'output_filename': 'js/classiclass.js',
        }
    }
}
