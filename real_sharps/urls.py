from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'cappers.views.index_view', name='home'),
    url(r'^products/', include('cappers.urls')),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^forum/', include('pybb.urls', namespace='pybb')),
    url(r'^faq/', TemplateView.as_view(template_name='faq.html'), name='faq'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^payments/', include('djstripe.urls', namespace="djstripe")),
)
