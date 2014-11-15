from django.conf.urls import patterns, include, url
from eventosv.apps.webServices.views import *

urlpatterns = patterns('eventosv.apps.webServices.views',
    # Examples:
    # url(r'^$', 'demo.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^webService/invitaciones/$', wsInvitaciones_view, name = 'wsInvitaciones_vista'),

    url(r'^webService/eventos/$', wsEventos_view, name = 'wsEventos_vista'),
    


    )