"""
Django settings for eventosv project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""



# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'e#r8-left^^2gw#v#__ox)alpv5b)r!z=&r5!@)dp3f0ixbi4+'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'eventosv.apps.evento',
    'eventosv.apps.juegoplataforma',
    'eventosv.apps.userprofile',
    'eventosv.apps.venta',

    'social.apps.django_app.default',

    'eventosv.apps.webServices',

)



MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

)

AUTHENTICATION_BACKENDS =(
    'social.backends.facebook.FacebookAppOAuth2',
    'social.backends.facebook.FacebookOAuth2',
    'social.backends.twitter.TwitterOAuth',
    'social.backends.open_id.OpenIdAuth',
    'social.backends.google.GoogleOAuth2',
    'social.backends.google.GoogleOAuth',
    'social.backends.google.GoogleOpenId',
    'django.contrib.auth.backends.ModelBackend',
    )

SOCIAL_AUTH_LOGIN_REDIRECT_URL = '/'

SOCIAL_AUTH_FACEBOOK_KEY = '379652592187774'
SOCIAL_AUTH_FACEBOOK_SECRET = 'b796e495205a0a820311bc5aa2a1c5e1'
SOCIAL_AUTH_TWITTER_KEY = 'Ssl3IocQOJH3DAj3cVdAyg0rX'
SOCIAL_AUTH_TWITTER_SECRET = 'bzzYAmMCNQpPbDaPgEYhribSZ03iFFR6UjG2yxNJbMkYlm54c3'
GOOGLE_OAUTH2_CLIENT_ID = '444090714566-c8ojrcekvm6emkha97ico6tb6gn0qpfp.apps.googleusercontent.com'
GOOGLE_OAUTH2_CLIENT_SECRET = '23fRUb1whmTNixRGUjL55_tB'

ROOT_URLCONF = 'eventosv.urls'

WSGI_APPLICATION = 'eventosv.wsgi.application'

# from django.core.urlresolvers import reverse_lazy
# LOGIN_URL=reverse_lazy('/accounts/login')
# LOGIN_REDIRECT_URL = reverse_lazy('/')
# LOGOUT_URL=reverse_lazy('/accounts/logout')
# LOGOUT_REDIRECT_URL = reverse_lazy('/accounts/login')


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Mexico/BajaNorte'

USE_I18N = True

USE_L10N = True

USE_TZ = True

PROJECT_DIR = os.path.dirname(__file__)
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'

# Directorios estaticos 
STATICFILES_DIRS = (
    os.path.join(PROJECT_DIR,'static/bootstrap',),
    os.path.join(PROJECT_DIR,'static/css',),
    os.path.join(PROJECT_DIR,'static/js',),
    os.path.join(PROJECT_DIR,'static/font-awesome',),
    os.path.join(PROJECT_DIR,'media/',),
)
# Media Files
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.normpath(os.path.join(PROJECT_DIR,'media/'))

# Directorio de plantillas
TEMPLATE_DIRS = (
    os.path.join(PROJECT_DIR, "templates"),
)