from .base import *

DEBUG = False

ALLOWED_HOSTS = ['*']

LOGIN_REDIRECT_URL = 'http://syu-clubs.com'

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
