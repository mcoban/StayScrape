from django.shortcuts import render
from django.http import HttpResponse

def home(request):
	return render(request, "home.html")

def messenger_callback(request):
	return HttpResponse(request.GET.get('hub.challenge'))