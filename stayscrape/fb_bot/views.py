from django.shortcuts import render
from django.http import HttpResponse
import json, pprint


def messenger_callback(request):

	if request.GET.get('hub.verify_token') == 'mcoban':
		return HttpResponse(request.GET.get('hub.challenge'))

	#pprint.pprint(request.body)

	if request.body:
		incomming_message = json.loads(request.body.decode('utf-8'))
		for entry in incomming_message['entry']:
			for message in entry['messaging']:
				if 'message' in message:
					pprint.pprint(message)
					post_facebook_message(message['sender']['id'], message['message']['text'])
	
	return HttpResponse('ok')




def post_facebook_message(request, fbid, received_message):
	
	post_message_url = 'https://graph.facebook.com/v2.6/me/messages?access_token=EAAWlzMdpex0BANZBsHoZCi8icR6VSOPpyL9oA2cryN4Tlv2h0UnZAzgiVX0c6fG895fBBaqhdXT5jiGLmVwuFXK2HhW0qCB4L0NZAj6BZA41pe1wePIrn2iyfXbuNagRZB9EMXSnD2Fb02dxV3af7RcH2XGZA2ZCJb2hGFT3SEQ68gZDZD'
	response_msg = json.dumps({ "recepient": { "id": fbid }, "message": { "text": received_message }})
	status = request.post(post_message_url, headers={ "Content-Type": "application/json" }, data=response_msg)
	pprint.pprint(status.json())