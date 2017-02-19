from django.shortcuts import render
from django.http import HttpResponse

rentals = [
	'villas', 'homes'
]

def index(request):
	return HttpResponse('Rentals Index Page')

def showRentals(request, type):
	if type in rentals:
		return HttpResponse(type)
	return HttpResponse('yok')