from django.conf.urls import url
from . import views


rentals_urls = [
    url(r'^$', views.index),
    url(r'^(?P<id>[0-9]+)$', views.showRental)
]

villas_urls = [
    url(r'^$', views.villas),
    url(r'^(?P<place>[-\w]+)$', views.listVillas)
]
