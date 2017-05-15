from django.conf.urls import url
from . import views


rentals_urls = [
    url(r'^$', views.index),
    url(r'^(?P<id>[0-9]+)$', views.showRental),
    #url(r'^(?P<id>[0-9]+)/(?P<slug>[-\w]+)$', views.showRental)
    url(r'^(?P<slug>[-\w]+)$', views.showRental)
]

villas_urls = [
    url(r'^$', views.villas),
    url(r'^(?P<place>[-\w]+)$', views.listVillas)
]

villa_redirect_urls = [
    url(r'^(?P<id>[0-9]+)$', views.redirectRental),
    url(r'^(?P<id>[0-9]+)/(?P<slug>[-\w]+)$', views.redirectRental)
]