"""
Django settings for apiary project.

Generated by 'django-admin startproject' using Django 1.11.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os


# Environment Variables
APIARY_SECRET_KEY = os.environ.get('APIARY_SECRET_KEY') or 'changeme'
APIARY_DEBUG = os.environ.get('APIARY_DEBUG') or False
APIARY_DB_NAME = os.environ.get('APIARY_DB_NAME') or 'postgres'
APIARY_DB_USER = os.environ.get('APIARY_DB_USER') or 'postgres'
APIARY_DB_PASSWORD = os.environ.get('APIARY_DB_PASSWORD') or 'password'
APIARY_DB_HOST = os.environ.get('APIARY_DB_HOST') or '127.0.0.1'
APIARY_DB_PORT = os.environ.get('APIARY_DB_PORT') or '5432'


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = APIARY_SECRET_KEY

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = APIARY_DEBUG

ALLOWED_HOSTS = [
    "apiary-env.us-east-1.elasticbeanstalk.com", 
    "apiary.plenar.io"
]


# Application definition

INSTALLED_APPS = [
    'apiary',
    'rest_framework',
    'rest_framework_gis',
    'django.contrib.admin',
    'registration',
    'django.contrib.auth',
    'organizations',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.gis'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'apiary.urls'

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

WSGI_APPLICATION = 'apiary.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': APIARY_DB_NAME,
        'USER': APIARY_DB_USER,
        'PASSWORD': APIARY_DB_PASSWORD,
        'HOST': APIARY_DB_HOST,
        'PORT': APIARY_DB_PORT,
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = 'static'


# Global settings for REST Framework
# http://www.django-rest-framework.org/#example

REST_FRAMEWORK = {
    'PAGE_SIZE': 10,
    'EXCEPTION_HANDLER': 'rest_framework_json_api.exceptions.exception_handler',
    'DEFAULT_PAGINATION_CLASS':
        'rest_framework_json_api.pagination.PageNumberPagination',
    'DEFAULT_PARSER_CLASSES': [
        'rest_framework.parsers.FormParser',
        'rest_framework.parsers.MultiPartParser',
        'rest_framework_json_api.parsers.JSONParser'
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticatedOrReadOnly',
    ],
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.BrowsableAPIRenderer',
        'rest_framework_json_api.renderers.JSONRenderer'
    ],
    'DEFAULT_METADATA_CLASS': 'rest_framework_json_api.metadata.JSONAPIMetadata',
}


# Global settings for registration framework
# http://django-registration-redux.readthedocs.io/en/latest/

ACCOUNT_ACTIVATION_DAYS = 7


# Global serttings for organization framework
# https://github.com/bennylope/django-organizations/#auto-slug-field

ORGS_SLUGFIELD = 'django_extensions.db.fields.AutoSlugField'
