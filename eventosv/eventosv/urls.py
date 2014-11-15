from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

from django.contrib import admin


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'modelos2.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'',include('social.apps.django_app.urls',namespace='social')),
    url(r'^',include('eventosv.apps.evento.urls')),
    url(r'^',include('eventosv.apps.juegoplataforma.urls')),
    url(r'^',include('eventosv.apps.userprofile.urls')),
    # url(r'^',include('eventosv.apps.venta.urls')),
    url(r'^$', TemplateView.as_view(template_name = 'index.html')),

    url(r'^',include('eventosv.apps.webServices.urls')),
)
