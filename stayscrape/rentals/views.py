import json
from django.shortcuts import render
from django.http import HttpResponse

from .models import Rental


rental_types = [
	{ 'id': 1,  'name': 'villa', 'title': 'Villa' },
	{ 'id': 2,  'name': 'house', 'title': 'House' },
	{ 'id': 3,  'name': 'apartment', 'title': 'Apartment' },
	{ 'id': 4,  'name': 'cottage', 'title': 'Cottage' },
	{ 'id': 5,  'name': 'condo', 'title': 'Condo' },
	{ 'id': 6,  'name': 'resort', 'title': 'Resort' },
	{ 'id': 7,  'name': 'townhome', 'title': 'Townhome' },
	{ 'id': 8,  'name': 'mobile-home', 'title': 'Mobile Home' },
	{ 'id': 9,  'name': 'studio', 'title': 'Studio' },
	{ 'id': 10, 'name': 'estate', 'title': 'Estate' },
	{ 'id': 11, 'name': 'bungalow', 'title': 'Bungalow' }
]

def checkType(type):
	for t in rental_types:
		if type == t['name']:
			return type
	return None

def index(request):
	return HttpResponse('Rentals Index Page')

def showRental(request, type, id):
	tpye = checkType(type)
	if type:
		# return HttpResponse(type)
		rental = Rental.objects.get(pk=id)
		featureds = Rental.objects.filter(regionArray=rental.regionArray)[:15]
		if rental:
			shortJSON = json.loads(rental.shortJSON)
			longJSON = json.loads(rental.longJSON)
			return render(request, "rentals/detail.html", {
				"rental": rental,
				"json": shortJSON,
				"detail_json": longJSON,
				"featureds": featureds
			})

	return HttpResponse('yok')