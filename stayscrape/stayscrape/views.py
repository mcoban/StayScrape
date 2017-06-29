from django.shortcuts import render
from django.http import HttpResponse
import json, pprint

def home(request):
	return render(request, "home.html")

def messenger_callback(request):

	if request.GET.get('hub.verify_token') == 'mcoban':
		return HttpResponse(request.GET.get('hub.challenge'))

	pprint.pprint(request.body)

	if request.POST:
		incomming_message = json.loads(request.body.decode('utf-8'))
		for entry in incomming_message['entry']:
			for message in entry['messaging']:
				if 'message' in message:
					pprint(message)
	
	return HttpResponse('ok')