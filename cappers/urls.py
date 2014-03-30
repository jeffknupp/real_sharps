from django.conf.urls import patterns, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'pick/(?P<pk>\d+)$', 'cappers.views.pick_detail', name='pick_detail'),
    url(r'capper/(?P<pk>\d+)$', 'cappers.views.capper_list_view', name='capper_list'),
    url(r'sport/(?P<pk>\d+)$', 'cappers.views.sport_list_view', name='sport_list'),
    url(r'$', 'cappers.views.pick_list_view', name='pick_list'),
    url(r'charge$', 'cappers.views.charge', name='charge'),
)
