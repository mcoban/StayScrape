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
			json_data = json.loads(rental.shortJSON)
			return render(request, "rentals/detail.html", {
				"rental": rental,
				"json": json_data
			})

	return HttpResponse('yok')