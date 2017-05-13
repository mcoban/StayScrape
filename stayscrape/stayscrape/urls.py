"""stayscrape URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.views.generic import TemplateView
from django.contrib import admin
from rentals.urls import  rentals_urls
from rentals.urls import villas_urls, villa_redirect_urls

from . import views
from rentals import views as rentals_views

urlpatterns = [
	url(r'^$', views.home),
    url(r'^admin/', admin.site.urls),
    url(r'^villa/', include(villa_redirect_urls)),
    url(r'^rental/', include(rentals_urls)),
    url(r'^villas/', include(villas_urls)),
    url(r'^robots\.txt$', TemplateView.as_view(template_name='robots.txt', content_type='text/plain')),
    url(r'^d3cc596d48f7\.html$', TemplateView.as_view(template_name='d3cc596d48f7.html', content_type='text/html')),
    url(r'^update-pictures$', rentals_views.update_featured_pictures),
    url(r'^blog/', include('blog.urls'))
]
