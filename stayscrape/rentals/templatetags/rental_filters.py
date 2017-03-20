import json
import math
from django import template

register = template.Library()

@register.filter
def rating_stars(value):
	li = ""
	for i in range (0, int(value)):
		li += "<li class='full'></li>"
	if value > int(value):
		li += "<li class='half'></li>"
	for i in range(0, 5 - math.ceil(value)):
		li += "<li class='empty'></li>"
	return li


@register.filter
def rental_title(title):
	return title.strip().title()


@register.filter
def rental_breadcrumb(location):
	li = ""
	for l in location:
		li += "<li><a href='#'>%s</a></li>" % l['name']
	return li
