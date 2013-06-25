from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic.base import TemplateView

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^i18n/', include('django.conf.urls.i18n')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', TemplateView.as_view(template_name="index.html")),
    url(r'^azienda$', TemplateView.as_view(template_name="azienda.html", get_context_data=lambda: {'pagina': 'azienda'})),
    url(r'^modelli$', TemplateView.as_view(template_name="modelli.html", get_context_data=lambda: {'pagina': 'modelli'})),
    url(r'^ghisa$', TemplateView.as_view(template_name="ghisa.html", get_context_data=lambda: {'pagina': 'ghisa'})),
    url(r'^acciaio$', TemplateView.as_view(template_name="acciaio.html", get_context_data=lambda: {'pagina': 'acciaio'})),
    url(r'^meccanica$', TemplateView.as_view(template_name="meccanica.html", get_context_data=lambda: {'pagina': 'meccanica'})),
    url(r'^laboratorio$', TemplateView.as_view(template_name="laboratorio.html", get_context_data=lambda: {'pagina': 'laboratorio'})),
)

# static media
if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    )

# handler500 = 'main.views.nondefault_500_error'
