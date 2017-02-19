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
	shortJSON = models.TextField()