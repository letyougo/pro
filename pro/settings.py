"""
Django settings for pro project.

Generated by 'django-admin startproject' using Django 2.0.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os
import logging
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'x^s86fwdh=sq^u5_qu=2t$8_xa3zj1$+6&h@#a$=7c%esjhb@y'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False



ALLOWED_HOSTS = [
    '101.200.129.112',
    'localhost',
    '127.0.0.1',
    'fe.dongnaoedu.com',
    '222.249.132.10'
]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'exam',
]

MIDDLEWARE = [
    # 'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'pro.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
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

WSGI_APPLICATION = 'pro.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases


DATABASES = {
       'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'exam',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '3306',
        },
    # 'default': {
    #     'ENGINE': 'django.db.backends.mysql',
    #     'NAME': 'exam',
    #     'USER': 'root',
    #     'PASSWORD': '',
    #     'HOST': 'localhost',
    #     'PORT': '3306',
    # }
}



# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    # {
    #     'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    # },
    # {
    #     'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    # },
    # {
    #     'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    # },
    # {
    #     'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    # },
]


# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/


LOGIN_URL = '/login/'

STATIC_URL = '/static/'
# STATIC_ROOT = os.path.join(BASE_DIR, 'static')

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),

)
APPEND_SLASH=False



PAGE_SIZE = 10
PAGE_NUM = 1






if DEBUG:
    pass
   # INTERNAL_IPS = ('127.0.0.1', 'localhost',)
#    MIDDLEWARE+= (
#        'debug_toolbar.middleware.DebugToolbarMiddleware',
#    )

#    INSTALLED_APPS += (
#        'debug_toolbar',
#    )

#    DEBUG_TOOLBAR_PANELS = [
#        'debug_toolbar.panels.versions.VersionsPanel',
#        'debug_toolbar.panels.timer.TimerPanel',
#        'debug_toolbar.panels.settings.SettingsPanel',
#        'debug_toolbar.panels.headers.HeadersPanel',
#        'debug_toolbar.panels.request.RequestPanel',
#        'debug_toolbar.panels.sql.SQLPanel',
#        'debug_toolbar.panels.staticfiles.StaticFilesPanel',
#        'debug_toolbar.panels.templates.TemplatesPanel',
#        'debug_toolbar.panels.cache.CachePanel',
#        'debug_toolbar.panels.signals.SignalsPanel',
#        'debug_toolbar.panels.logging.LoggingPanel',
#        'debug_toolbar.panels.redirects.RedirectsPanel',
#    ]

#    DEBUG_TOOLBAR_CONFIG = {
#        'INTERCEPT_REDIRECTS': False,
#    }

   # log = logging.getLogger('django.db.backends')
   # log.setLevel(logging.DEBUG)
   # log.addHandler(logging.StreamHandler())

#    LOGGING = {
#     'version': 1,
#     'disable_existing_loggers': False,
#     'handlers': {
#         'console': {
#             'class': 'logging.StreamHandler',
#         },
#     },
#     'loggers': {
#         'django.db.backends': {
#             'handlers': ['console'],
#             'level': 'DEBUG' if DEBUG else 'INFO',
#         },
#         },
#     }



