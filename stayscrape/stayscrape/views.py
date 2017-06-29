from django.shortcuts import render
from django.http import HttpResponse
import json

def home(request):
	return render(request, "home.html")

def messenger_callback(request):

	if request.GET.get('hub.verify_token') == 'mcoban':
		return HttpResponse(request.GET.get('hub.challenge'))

	if request.POST:
		print(request.body)