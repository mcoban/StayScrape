from django.db import models
from autoslug import AutoSlugField

class Country(models.Model):
	name = models.CharField(max_length=50)
	slug = AutoSlugField(populate_from="name", always_update=True)
	page_title = models.CharField(max_length=150, blank=True, null=True)
	description = models.TextField(blank=True, null=True)
	meta_title = models.CharField(max_length=150, blank=True, null=True)
	meta_description = models.CharField(max_length=250, blank=True, null=True)

	def __str__(self):
		return self.name


class City(models.Model):
	country = models.ForeignKey(Country)
	name = models.CharField(max_length=50)
	slug = AutoSlugField(populate_from="name", always_update=True)

	def __str__(self):
		return self.name