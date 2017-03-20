import json
import math
from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings

from .models import Rental, Relations
from destinations.models import Place


def index(request):
	return HttpResponse('Rentals Index Page')	

def showRental(request, id):
	rental = Rental.objects.get(pk=id)
	regions = json.loads(rental.longJSON)['listing']['regions']
	for region in regions:
		place = region['name']

	place = Place.objects.get(name=place)
	relateds = Relations.objects.filter(place_id=place.id)
	featureds = Rental.objects.filter(id__in=[related.rental_id for related in relateds])[:30]
	if rental:
		shortJSON = json.loads(rental.shortJSON)
		longJSON = json.loads(rental.longJSON)
		return render(request, "rentals/detail.html", {
			"settings": settings,
			"rental": rental,
			"json": shortJSON,
			"detail_json": longJSON,
			"featureds": featureds
		})

	return HttpResponse('yok')




def villas(request):
	return render(request, "listing/all.html")


def listVillas(request, place):
	try:
		place = Place.objects.get(slug=place)
		try:
			page = int(request.GET.get('page')) if request.GET.get('page') and request.GET.get('page').isnumeric() and int(request.GET.get('page')) > 1 else 1
			if (page - 1) * settings.COUNT_PER_PAGE > int(place.count):
				return HttpResponse("küçük")

			start = (page - 1) * settings.COUNT_PER_PAGE
			relateds = Relations.objects.filter(place_id=place.id)
			rentals = Rental.objects.filter(id__in=[related.rental_id for related in relateds])[start:start + settings.COUNT_PER_PAGE]
			
			for rental in rentals:
				rental.longJSON = json.loads(rental.longJSON)

			pagination = {
				"page": page,
				"page_count": math.ceil(place.count / settings.COUNT_PER_PAGE),
				"start": start + 1, 
				"end": start + settings.COUNT_PER_PAGE
			}

			if page > 1:
				pagination["prev"] = "%s/villas/%s?page=%d" % (settings.SITE_URL, place.slug, page - 1)

			if page * settings.COUNT_PER_PAGE < int(place.count):
				pagination["next"] = "%s/villas/%s?page=%d" % (settings.SITE_URL, place.slug, page + 1)
			
			return render(request, "listing/filter.html",{
				"settings": settings,
				"place": place,
				"rentals": rentals,
				"pagination": pagination
			})
		except Rental.DoesNotExist:
			return HttpResponse("yok")
	except Place.DoesNotExist:
		return HttpResponse("Place does not exists")
