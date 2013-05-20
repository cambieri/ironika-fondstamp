import os
import django.core.handlers.wsgi

os.environ['DJANGO_SETTINGS_MODULE'] = 'fondstamp.settings.sites.default.prod.stage'
application = django.core.handlers.wsgi.WSGIHandler()