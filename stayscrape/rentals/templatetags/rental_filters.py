from django import template
import math

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
