from django.conf.urls import patterns, include, url
from eventosv.apps.juegoplataforma.views import *
from eventosv.apps.juegoplataforma.forms import *

from django.contrib.auth.decorators import login_required, permission_required

urlpatterns = patterns('eventosv.apps.juegoplataforma.views',
    # Examples:


    url(r'juego/add/$', JuegoCreate.as_view(), name='juego_add'),
	url(r'juego/update/(?P<pk>\d+)/$', JuegoUpdate.as_view(),name='juego_update'),
	url(r'juego/delete/(?P<pk>\d+)/$', JuegoDelete.as_view(), name='juego_delete'),
	url(r'juego/list/$', JuegoListView.as_view(), name='juego_list'),
	url(r'juego/detail/(?P<pk>[-_\w]+)/$', JuegoDetailView.as_view(), name='juego_detail'),
	   
	url(r'juego/completos/$',CompletosView.as_view(), name = 'Completos_view'),
	url(r'juego/mods/$',ModsView.as_view(), name = 'Mods_view'),


    url(r'plataforma/add/$', PlataformaCreate.as_view(), name='plataforma_add'),
	url(r'plataforma/update/(?P<pk>\d+)/$', PlataformaUpdate.as_view(),name='plataforma_update'),
	url(r'plataforma/delete/(?P<pk>\d+)/$', PlataformaDelete.as_view(), name='plataforma_delete'),
	url(r'plataforma/list/$', PlataformaListView.as_view(), name='plataforma_list'),
	url(r'plataforma/detail/(?P<pk>[-_\w]+)/$', PlataformaDetailView.as_view(), name='plataforma_detail'),






	url(r'opinion/add/(?P<pk>\d+)/$', OpinionCreate.as_view(), name='opinion_add'),
	   
 )


