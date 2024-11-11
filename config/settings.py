"""
Django settings for config project.

Generated by 'django-admin startproject' using Django 5.0.6.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

from pathlib import Path
import ssl
import smtplib
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
#
# with open(os.path.join(BASE_DIR, '.env')) as f:
#     SECRET_KEY = f.read().strip()

with open(os.path.join(BASE_DIR, '.env')) as f:
    for line in f:
        if line.startswith("SECRET_KEY="):
            SECRET_KEY = line.split("=", 1)[1].strip()
            break

CORS_ALLOW_ALL_ORIGINS = True

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST_USER = 'allayorovbobur22@gmail.com'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_SSL = True
EMAIL_PORT = 465
EMAIL_HOST_PASSWORD = 'kamnidznwuphfoep'

ALLOWED_HOSTS = ["*"]

SITE_ID = 2

AUTHENTICATION_BACKENDS = [
    'allauth.account.auth_backends.AuthenticationBackend',
    'django.contrib.auth.backends.ModelBackend',
]

LOGIN_REDIRECT_URL = "/api/home/"
LOGOUT_REDIRECT_URL = "/api/home/"

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',

    'rest_framework',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    # 'allauth.socialaccount.providers.github',
    'allauth.socialaccount.providers.google',
    'allauth.socialaccount.providers.facebook',
    'allauth.socialaccount.providers.apple',
    "crispy_forms",
    "crispy_bootstrap5",
    'django_filters',
    'mptt',

    'olx',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    "allauth.account.middleware.AccountMiddleware",
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR / 'templates'
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.request',
            ],
        },
    },
]

with open(os.path.join(BASE_DIR, '.env')) as f:
    for line in f:
        if line.startswith("client_id="):
            client_id = line.split("=", 1)[1].strip()
        if line.startswith("secret="):
            secret = line.split("=", 1)[1].strip()
            break

print(client_id, secret)

SOCIALACCOUNT_PROVIDERS = {
    # 'github': {
    #     'APP': {
    #         'client_id': 'Ov23liFu9zG5QCYh95ld',
    #         'secret': 'd581f0448382e7746d23d78c3dbc48009d8b25bb',
    #         'key': ''
    #     }
    # },
    'google': {
        'SCOPE': {
            'profile',
            'email'
        },
        'APP': {
            'client_id': client_id,
            'secret': secret,
        },
        'AUTH_PARAMS': {'access_type': 'online', },
    },
    # 'facebook': {
    #     'METHOD': 'oauth2',
    #     'SCOPE': {
    #         'profile',
    #         'email'
    #     },
    #     'AUTH_PARAMS': {'auth_type': 'reauthenticate'},
    #     'APP': {
    #         'client_id': '1005068070788125',
    #         'secret': 'a9028aab5986b1a30f03b9565afa71b2',
    #     },
    # },
    "apple": {
        "APPS": [{
            "client_id": "your.service.id",

            "secret": "KEYID",

            "key": "MEMAPPIDPREFIX",

            "settings": {
                # The certificate you downloaded when generating the key.
                "certificate_key":
                    """
                        s3cr3ts3cr3ts3cr3ts3cr3ts3cr3ts3cr3ts3cr3ts3cr3ts3cr3ts3cr3ts3cr
                        3ts3cr3ts3cr3ts3cr3ts3cr3ts3cr3ts3cr3ts3cr3ts3cr3ts3cr3ts3cr3ts3
                        c3ts3cr3t
                    """
            }
        }]
    }

}

WSGI_APPLICATION = 'config.wsgi.application'

# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = False

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'

STATIC_ROOT = BASE_DIR / 'static'

MEDIA_URL = 'media/'

MEDIA_ROOT = BASE_DIR / 'media'

STATICFILES_DIRS = BASE_DIR / 'assets',

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

REST_FRAMEWORK = {
    # 'DEFAULT_AUTHENTICATION_CLASSES': (
    #     'rest_framework_simplejwt.authentication.JWTAuthentication',
    # ),
    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend'],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 10

}

CRISPY_TEMPLATE_PACK = "bootstrap5"
