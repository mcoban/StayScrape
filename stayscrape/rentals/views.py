import json
import math
from slugify import slugify
from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from django.conf import settings

from .models import Rental, Relations
from destinations.models import Place


def index(request):
	return HttpResponse('Rentals Index Page')	



def update_featured_pictures(request):
	rentals = Rental.objects.filter(picturesArray="")[:50]
	return render(request, "update-pictures.html", {
		"rentals": rentals
	})


def redirectRental(request, id, slug=None):
	try:
		rental = Rental.objects.get(pk=id)
		shortJSON = json.loads(rental.shortJSON)
		longJSON = json.loads(rental.longJSON)
		regions = longJSON['listing']['regions']
		
		return redirect("%s/rental/%s-villa-%d" % (settings.SITE_URL, rental.slug, rental.id))

		return HttpResponse('yok')
	except Rental.DoesNotExist:
		raise Http404("Rental does not exists")

def redirectRental2(request, id):
	try:
		rental = Rental.objects.get(pk=id)
		shortJSON = json.loads(rental.shortJSON)
		longJSON = json.loads(rental.longJSON)
		regions = longJSON['listing']['regions']
		
		return redirect("%s/rental/%s-villa-%d" % (settings.SITE_URL, rental.slug, rental.id))

		return HttpResponse('yok')
	except Rental.DoesNotExist:
		raise Http404("Rental does not exists")




# def showRental(request, id, slug=None):
def showRental(request, slug):

	id = slug.split('-').pop()
	slug = '-'.join(slug.split('-')[:-1])

	if not id.isdigit():
		return HttpResponse(":)")

	try:
		rental = Rental.objects.get(pk=id)
		
		if slug != rental.slug:
			return redirect("%s/rental/%s-%d" % (settings.SITE_URL, rental.slug, rental.id))

		rental.shortJSON = json.loads(rental.shortJSON)
		rental.longJSON = json.loads(rental.longJSON)
		regions = rental.longJSON['listing']['regions']
		
		for region in regions:
			try:
				place = Place.objects.get(slug=slugify(region['name']))
			except:
				pass

		relateds = Relations.objects.filter(place_id=place.id)
		featureds = Rental.objects.filter(id__in=[related.rental_id for related in relateds]).exclude(id=rental.id)[:8]
		for featured in featureds:
			featured.longJSON = json.loads(featured.longJSON)
			featured.shortJSON = json.loads(featured.shortJSON)
		
		return render(request, "rentals/detail.html", {
			"settings": settings,
			"rental": rental,
			"json": rental.shortJSON,
			"detail_json": rental.longJSON,
			"featureds": featureds
		})

		return HttpResponse('404')
	except Rental.DoesNotExist:
		raise Http404("Rental does not exists")




def villas(request):
	return render(request, "listing/all.html")


def listVillas(request, place):
	try:
		place = Place.objects.get(slug=place)
		try:
			page = int(request.GET.get('page')) if request.GET.get('page') and request.GET.get('page').isnumeric() and int(request.GET.get('page')) > 1 else 1
			orderby = request.GET.get('orderby')
			if (page - 1) * settings.COUNT_PER_PAGE > int(place.count):
				return HttpResponse("küçük")

			start = (page - 1) * settings.COUNT_PER_PAGE

			order_obj = {
				"price_low": "price",
				"price_high": "-price",
				"sleeps_low": "sleeps",
				"sleeps_high": "-sleeps"
			}
			
			try:
				relateds = Relations.objects.filter(place_id=place.id).order_by(order_obj[orderby])
				rentals = Rental.objects.filter(id__in=[related.rental_id for related in relateds]).order_by(order_obj[orderby])[start:start + settings.COUNT_PER_PAGE]
			except KeyError:
				relateds = Relations.objects.filter(place_id=place.id)
				rentals = Rental.objects.filter(id__in=[related.rental_id for related in relateds])[start:start + settings.COUNT_PER_PAGE]

			
			for rental in rentals:
				rental.json = json.loads(rental.shortJSON)
				rental.longJSON = json.loads(rental.longJSON)

			pagination = {
				"page": page,
				"page_count": math.ceil(place.count / settings.COUNT_PER_PAGE),
				"start": start + 1, 
				"end": start + settings.COUNT_PER_PAGE
			}

			if page > 1:
				pagination["prev"] = "%s/villas/%s?page=%d" % (settings.SITE_URL, place.slug, page - 1)
				if orderby:
					pagination["prev"] = "%s/villas/%s?orderby=%s&page=%d" % (settings.SITE_URL, place.slug, orderby, page - 1)

			if page * settings.COUNT_PER_PAGE < int(place.count):
				pagination["next"] = "%s/villas/%s?page=%d" % (settings.SITE_URL, place.slug, page + 1)
				if orderby:
					pagination["next"] = "%s/villas/%s?orderby=%s&page=%d" % (settings.SITE_URL, place.slug, orderby, page + 1)
			
			return render(request, "listing/filter.html",{
				"settings": settings,
				"place": place,
				"rentals": rentals,
				"pagination": pagination,
				"orderby": orderby
			})
		except Rental.DoesNotExist:
			return HttpResponse("yok")
	except Place.DoesNotExist:
		raise Http404("Place does not exists")
