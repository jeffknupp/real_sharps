from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'cappers.views.index_view', name='home'),
    url(r'^products/', include('cappers.urls')),
    url(r'^accounts/', include('allauth.urls')),
#    url(r'^attachments/', include('attachments.urls')),
#    url(r'^for', include('lbforum.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
