# -*- coding: utf-8 -*-
# These settings are valid for:
# - sites: all
# - environments: dev

import os
from fondstamp.settings.common import *

# Debug
DEBUG = False
TEMPLATE_DEBUG = DEBUG

# Cache
CACHES = {
        'default': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
         }
}

# Database
DATABASES = {
        'default': {
    	'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
    	'NAME': os.path.join(SITE_ROOT, 'db','dev.sqlite3'), # Or path to database file if using sqlite3.
    	'USER': '', # Not used with sqlite3.
    	'PASSWORD': '', # Not used with sqlite3.
    	'HOST': '', # Set to empty string for localhost. Not used with sqlite3.
    	'PORT': '', # Set to empty string for default. Not used with sqlite3.
    },
    
#    'default': {
#        'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
#        'NAME': 'ironika_fondstamp_devel',                      # Or path to database file if using sqlite3.
#        'USER': 'ironika_fondstamp_devel',                      # Not used with sqlite3.
#        'PASSWORD': 'devel',                  # Not used with sqlite3.
#        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
#        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
#    },
}

DEFAULT_CHARSET='utf-8'
