from django.db import models
from autoslug import AutoSlugField

class Country(models.Model):
	name = models.CharField(max_length=50)
	slug = AutoSlugField(populate_from="name", always_update=True)

	def __str__(self):
		return self.name


class City(models.Model):
	country = models.ForeignKey(Country)
	name = models.CharField(max_length=50)
	slug = AutoSlugField(populate_from="name", always_update=True)

	def __str__(self):
		return self.name


class District(models.Model):
	country = models.ForeignKey(Country)
	city = models.ForeignKey(City)
	name = models.CharField(max_length=50)

	def __str__(self):
		return self.name