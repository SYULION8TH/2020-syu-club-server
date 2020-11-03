from .base import *

DEBUG = False

ALLOWED_HOSTS = ['*']

SITE_ID = 1

LOGIN_REDIRECT_URL = 'http://syu-clubs.com'

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
