import os
from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['aptitude.biotektools.org','aptitude-db.com','aptitude-refa.com']

SITE_URL = 'http://aptitude.biotektools.org/'


MEDIA_ROOT = '/home/serendipity/webapps/aptitude_media/'
MEDIA_URL = '/media/'

STATIC_ROOT = '/home/serendipity/webapps/aptitude_static/'
STATIC_URL = '/static/'
STATICFILES_DIRS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.contrib.gis.db.backends.postgis',
#         'NAME': os.environ.get('DB_NAME', 'omicsmap'),
#         'USER': os.environ.get('DB_USER', 'onconet'),
#         'PASSWORD': os.environ.get('DB_PASSWORD', 'onc0n3t'),
#         'HOST': os.environ.get('DB_HOST', 'localhost'),
#     }
# }

CORS_ORIGIN_ALLOW_ALL = True

# e-mail configuration

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'zarevnal@gmail.com'
EMAIL_HOST_PASSWORD = 'rasput1n'

# account activation

ACCOUNT_ACTIVATION_DAYS = 7 # One-week activation window; you may, of course, use a different value.
REGISTRATION_AUTO_LOGIN = False # Automatically log the user in.

ACCOUNT_AUTHENTICATED_REGISTRATION_REDIRECTS = False
REGISTRATION_USE_SITE_EMAIL = False
REGISTRATION_SITE_USER_EMAIL = "info"
REGISTRATION_DEFAULT_FROM_EMAIL = "info@aptitude.com"
REGISTRATION_EMAIL_HTML = True

REGISTRATION_ADMINS = [('Alberto Labarga', 'alberto.labarga@gmail.com'), ]


