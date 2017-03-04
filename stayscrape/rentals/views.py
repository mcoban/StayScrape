import json
from django.shortcuts import render
from django.http import HttpResponse

from .models import Rental
from destinations.models import Country, City


def index(request):
	return HttpResponse('Rentals Index Page')	

def showRental(request, id):
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




def villas(request):
	return render(request, "listing/all.html")


def listVillas(request, country, city=None):
	#country = Country.objects.get()
	return render(request, "listing/country.html")
