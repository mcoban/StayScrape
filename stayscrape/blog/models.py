from django.db import models
from slugify import slugify

class Post(models.Model):
	title = models.CharField(max_length=200, unique=True)
	short = models.CharField(max_length=120, blank=True)
	slug = models.SlugField(max_length=200, unique=True)
	body = models.TextField()
	posted_date = models.DateTimeField(db_index=True, auto_now_add=True)
	thumbnail_url = models.CharField(max_length=250, blank=True)
	featured_picture_url = models.CharField(max_length=250, blank=True)
	category = models.ManyToManyField("Category", related_name="blog_category")

	def __unicode__(self):
		return self.title


class Category(models.Model):
	title = models.CharField(max_length=200, db_index=True)
	slug = models.SlugField(max_length=200, db_index=True)

	def __unicode__(self):
		return self.title
