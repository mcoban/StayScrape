from django.shortcuts import render
from django.http import HttpResponse
import json, pprint

def home(request):
	return render(request, "home.html")
