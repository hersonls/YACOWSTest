#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

import sys

sys.path.insert(0, '.')


DEBUG = True
TEMPLATE_DEBUG = DEBUG

PROJECT_PATH = os.path.abspath(os.path.dirname(__file__))

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(PROJECT_PATH, 'yacows_test.db'),
    }
}

SITE_ID = 1
USE_I18N = True
USE_L10N = True
USE_TZ = False

MEDIA_URL = '/m/'

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

SECRET_KEY = '8=#&amp;5-4@j#54=!(nwo5q8$y9i%y5c384jnp6pf7@m*q&amp;#71xc1'

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.core.context_processors.request",
    'opps.channels.context_processors.channel_context',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.contrib.redirects.middleware.RedirectFallbackMiddleware',
    # Used in Multi-Site
    'opps.core.middleware.DynamicSiteMiddleware',
    # Used in Multi-Site
    'opps.core.middleware.MobileDetectionMiddleware',
    'johnny.middleware.LocalStoreClearMiddleware',
    'johnny.middleware.QueryCacheMiddleware',
)

TEMPLATE_DIRS = (os.path.join(PROJECT_PATH, 'src', 'templates'),)
TEMPLATE_DIRS_WEB = TEMPLATE_DIRS
TEMPLATE_DIRS_MOBILE = (os.path.join(PROJECT_PATH, 'src', 'templates',
                                     'mobile'),)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.redirects',
    'django.contrib.admin',

    'apps.page',

    'opps.core',
    'opps.boxes',
    'opps.channels',
    'opps.sources',
    'opps.articles',
    'opps.images',
    'opps.sitemaps',
    'opps.flatpages',

    'south',
    'taggit',
)

OPPS_CHECK_MOBILE = True

TEST_RUNNER = 'django_coverage.coverage_runner.CoverageRunner'

CACHES = {'default': {
    'BACKEND': 'django.core.cache.backends.dummy.DummyCache'}}
JOHNNY_MIDDLEWARE_KEY_PREFIX = 'opps_yacows_test'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

STATIC_URL = '/static/'
ROOT_URLCONF = 'yacows_test.urls'
