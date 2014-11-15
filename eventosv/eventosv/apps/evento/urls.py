from django.conf.urls import patterns, include, url
from eventosv.apps.evento.views import *
from eventosv.apps.evento.forms import *

urlpatterns = patterns('eventosv.apps.evento.views',
    # Examples:


    url(r'evento/add/$', EventoCreate.as_view(), name='evento_add'),
    url(r'evento/update/(?P<pk>\d+)/$', EventoUpdate.as_view(),name='evento_update'),
    url(r'evento/delete/(?P<pk>\d+)/$', EventoDelete.as_view(), name='evento_delete'),
    url(r'evento/list/$', EventoListView.as_view(), name='evento_list'),
	url(r'evento/detail/(?P<pk>[-_\w]+)/$', EventoDetailView.as_view(), name='evento_detail'),

	url(r'comentario/add/(?P<pk>\d+)/$', ComentarioCreate.as_view(), name='comentario_add'),

	url(r'invitacion/state/(?P<pk>\d+)/$', InvitacionUpdate.as_view(), name='invitacion_update'),

	url(r'evento/join/(?P<pk>\d+)/$', EventoJoin, name = 'evento_join'),
	   

    )


