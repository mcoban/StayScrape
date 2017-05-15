import json
import math
from django import template
from slugify import slugify
from django.conf import settings

register = template.Library()

@register.filter
def rating_stars(value):
	li = ""
	for i in range (0, int(value)):
		li += "<li class='full'></li>"
	if value > int(value):
		li += "<li class='half'></li>"
	for i in range(0, 5 - math.ceil(value)):
		li += "<li class='empty'></li>"
	return li


@register.filter
def rental_title(title):
	return title.strip().title()


@register.filter
def rental_breadcrumb(location):
	li = ""
	count = 0
	for l in location:
		count = count + 1
		li += "<li itemprop='itemListElement' itemscope itemtype='http://schema.org/ListItem'><a itemprop='item' href='%s/villas/%s'><span itemprop='name'>%s</span></a><meta itemprop='position' content='%d' /></li>" % (settings.SITE_URL, slugify(l['name']), l['name'], count)
	return li

@register.filter
def slug_this(name):
	return slugify(name)


@register.filter
def get_district(place):
	return place.split(",")[0]


@register.filter
def get_title(rental):
	longJSON = rental.longJSON
	try:
		if rental.title_preffix:
			return "%s Villa #%d to Rent in %s %s" % (rental.title_preffix, rental.id, longJSON['listing']['address']['city'], longJSON['listing']['address']['stateProvince'])
		else:
			return "%s Villa #%d to Rent in %s %s" % (get_district(longJSON['listing']['primaryLocation']['description']), rental.id, longJSON['listing']['address']['city'], longJSON['listing']['address']['stateProvince'] )
	except KeyError:
		return "%s Villa #%d to Rent in %s" % (get_district(longJSON['listing']['address']['city']), rental.id, longJSON['listing']['address']['stateProvince'] )