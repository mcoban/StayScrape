import json
from django.shortcuts import render
from django.http import HttpResponse

from .models import Rental


rental_types = [
	'villa', 'home'
]

def index(request):
	return HttpResponse('Rentals Index Page')

def showRental(request, type, id):
	if type in rental_types:
		rental = Rental.objects.get(pk=id)
		if rental:
			shortJSON = json.loads(rental.shortJSON)
			longJSON = json.loads(rental.longJSON)
			return render(request, "rentals/detail.html", {
				"rental": rental,
				"json": shortJSON,
				"detail_json": longJSON
			})

	return HttpResponse('yok')