from .base import *

DEBUG = False

ALLOWED_HOSTS = ['*']

LOGIN_REDIRECT_URL = 'http://www.syu-clubs.com'

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
