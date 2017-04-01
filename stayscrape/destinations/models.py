from django.db import models
from autoslug import AutoSlugField

class Place(models.Model):
	name = models.CharField(max_length=100, unique=True)
	slug = AutoSlugField(populate_from="name", always_update=True)
	search_term = models.CharField(max_length=100, blank=True, null=True)
	page_title = models.CharField(max_length=200, blank=True, null=True)
	meta_title = models.CharField(max_length=150, blank=True, null=True)
	meta_description = models.CharField(max_length=200, blank=True, null=True)
	description = models.TextField(blank=True, null=True)
	count = models.IntegerField(default=0)

	def __str__(self):
		return self.name
