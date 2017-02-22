import json
from django.db import models

class Rental(models.Model):
	regionId = models.IntegerField(default=0)
	referer = models.CharField(max_length=50, default="")
	regionArray = models.CharField(max_length=250, default="")
	headline = models.CharField(max_length=100)
	price = models.IntegerField(default=0)
	sleeps = models.IntegerField(default=0)
	bathrooms = models.IntegerField(default=0)
	bedrooms = models.IntegerField(default=0)
	detailPageUrl = models.CharField(max_length=250, unique=True)
	galleryUrl = models.CharField(max_length=250, default="")
	geoCode = models.CharField(max_length=50, default="")
	shortJSON = models.TextField(default="")
	longJSON = models.TextField(default="")
	is_checked = models.BooleanField(default=False)

	def __str__(self):
		return self.headline

	def thumbnail(self):
		return '<img src="%s" height="90" />' % self.galleryUrl
	thumbnail.allow_tags = True

	def view(self):
		return '<a href="http://127.0.0.1:8000/rental/villa/%s" target="_blank">View</a>' % self.id
	view.allow_tags = True

	def external(self):
		return '<a href="%s" target="_blank">Referer</a>' % self.detailPageUrl
	external.allow_tags = True