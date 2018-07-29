"""
Django settings for onken project.

Generated by 'django-admin startproject' using Django 2.0.6.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os
import raven

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', ')kdrzd%8yp1sd_p9^*u@x$0&a+!bf$uy0-*v%z@bt$^$1zm3eu')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get('DJANGO_DEBUG', True)

ALLOWED_HOSTS = [os.environ.get('DJANGO_ALLOWED_HOST', '*')]

# Application definition

SHARED_APPS = (
    'django_tenants',
    'onken.public',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_cas_ng',
    'ddtrace.contrib.django',
    'raven.contrib.django.raven_compat',
    'rest_framework'
)

TENANT_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'onken.workspace',
)

INSTALLED_APPS = list(SHARED_APPS) + [app for app in TENANT_APPS if app not in SHARED_APPS]

TENANT_MODEL = 'public.Workspace'

TENANT_DOMAIN_MODEL = "public.Domain"

MIDDLEWARE = [
    'raven.contrib.django.raven_compat.middleware.SentryResponseErrorIdMiddleware',
    'raven.contrib.django.raven_compat.middleware.Sentry404CatchMiddleware',
    'django_tenants.middleware.main.TenantMainMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

AUTHENTICATION_BACKENDS = [
    'django_cas_ng.backends.CASBackend',
]

PUBLIC_SCHEMA_URLCONF = 'onken.public.urls'

ROOT_URLCONF = 'onken.workspace.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'onken.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django_tenants.postgresql_backend',
        'NAME': os.environ.get('DJANGO_DATABASE_NAME'),
        'USER': os.environ.get('DJANGO_DATABASE_USER'),
        'PASSWORD': os.environ.get('DJANGO_DATABASE_PASSWORD'),
        'HOST': 'localhost',
        'PORT': '',
    }
}

DATABASE_ROUTERS = {
    'django_tenants.routers.TenantSyncRouter',
}


# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = []


# Internationalization
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(BASE_DIR, 'static')


# Test report generation for CircleCI
TEST_RUNNER = 'xmlrunner.extra.djangotestrunner.XMLTestRunner'

TEST_OUTPUT_DIR = 'test-reports'


# CAS configuration
CAS_SERVER_URL = 'http://localhost:3004'

CAS_VERSION = '3'

CAS_FORCE_CHANGE_USERNAME_CASE = 'lower'

CAS_APPLY_ATTRIBUTES_TO_USER = True

CAS_RENAME_ATTRIBUTES = {
    'sn': 'last_name',
    'givenName': 'first_name',
    'email_primary': 'email',
}

CAS_RETRY_LOGIN = False


# Datadog configuration
DATADOG_TRACE = {
    'DEFAULT_SERVICE': 'onken',
    'TAGS': {'env': 'dev'},
}

# DRF configuration
REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissions'
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.SessionAuthentication',
    ),
    'DEFAULT_VERSIONING_CLASS': 'rest_framework.versioning.NamespaceVersioning'
}


LOGIN_URL = '/login'

LOGIN_REDIRECT_URL = '/'


AUTH_USER_MODEL = 'public.User'
