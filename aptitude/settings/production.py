from .base import *
import os

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['resources.onconet-sudoe.eu']

SITE_URL = 'http://resources.onconet-sudoe.eu/'
STATIC_URL = '/static/'
STATIC_ROOT = '/home/serendipity/webapps/oncomap_static/'
STATICFILES_DIRS = [

]

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': os.environ.get('DB_NAME', 'omicsmap'),
        'USER': os.environ.get('DB_USER', 'onconet'),
        'PASSWORD': os.environ.get('DB_PASSWORD', 'onc0n3t'),
        'HOST': os.environ.get('DB_HOST', 'localhost'),
    }
}

CORS_ORIGIN_ALLOW_ALL = True   

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'


EMAIL_HOST = 'smtp.webfaction.com'
EMAIL_HOST_USER = 'onconet'
EMAIL_HOST_PASSWORD = 'onc0net'
DEFAULT_FROM_EMAIL = 'info@resources.onconet-sudoe.eu'
SERVER_EMAIL = 'info@resources.onconet-sudoe.eu'

#EMAIL_HOST = 'smtp.gmail.com'
#EMAIL_PORT = 587
#EMAIL_USE_TLS = True


# Optional SMTP authentication information for EMAIL_HOST.
#EMAIL_HOST_USER = 'zarevnal@gmail.com'
#EMAIL_HOST_PASSWORD = 'rasput1n'

ACCOUNT_ACTIVATION_DAYS = 5

LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'

