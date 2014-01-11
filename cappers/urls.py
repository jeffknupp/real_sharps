from django.conf.urls import patterns, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'/pick/(?P<slug>[\w-]+)$', 'cappers.views.pick_product_detail', name='pick_product_view'),
    url(r'/pickset/(?P<slug>[\w-]+)$', 'cappers.views.pickset_product_detail', name='pickset_product_view'),
    url(r'$', 'cappers.views.product_list', name='product_list'),
    url(r'/charge$', 'cappers.views.charge', name='charge'),
)