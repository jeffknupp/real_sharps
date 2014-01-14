from django.conf.urls import patterns, url
from django.contrib import admin
from cappers.views import PickListView, CapperListView, SportListView

admin.autodiscover()

urlpatterns = patterns('',
    url(r'pick/(?P<pk>\d+)$', 'cappers.views.pick_detail', name='pick_detail'),
    url(r'capper/(?P<pk>\d+)$', CapperListView.as_view(), name='capper_list'),
    url(r'sport/(?P<pk>\d+)$', SportListView.as_view(), name='sport_list'),
    url(r'$', PickListView.as_view(), name='pick_list'),
    url(r'charge$', 'cappers.views.charge', name='charge'),
)
