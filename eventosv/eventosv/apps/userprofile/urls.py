from django.conf.urls import patterns, include, url
from eventosv.apps.userprofile.views import *
from eventosv.apps.userprofile.forms import *

urlpatterns = patterns('eventosv.apps.userprofile.views',
    # Examples:

    url(r'^accounts/register/$', SignUpView.as_view(), name='signup'),
    url(r'^accounts/login/$', LoginView.as_view(), name='login'),
    url(r'^accounts/logout/$', LogoutView.as_view(), name='logout'),

    url(r'accounts/profile/(?P<pk>\d+)/$', UserUpdate.as_view(),name='profile_update'),

    )


