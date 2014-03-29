from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'cappers.views.index_view', name='home'),
    url(r'^products/', include('cappers.urls')),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^forum/', include('pybb.urls', namespace='pybb')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^payments/', include('djstripe.urls', namespace="djstripe")),
)
