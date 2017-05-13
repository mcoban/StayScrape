from django.shortcuts import render
from slugify import slugify
from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from django.conf import settings
from .models import Post, Category


def index(request):
	articles = Post.objects.filter(category__slug="article")
	return render(request, "blog/index.html", {
		"articles": articles
	})


def showArticle(request, slug):
	
	id = slug.split('-').pop()
	slug = '-'.join(slug.split('-')[:-1])
	
	if id.isdigit():
		try:
			article = Post.objects.get(id=id)
			if article.slug != slug:
				return redirect("%s/blog/%s-%d" % (settings.SITE_URL, article.slug, article.id) )
			else:
				return render(request, "blog/article.html", {
					"article": article
				})
		except Post.DoesNotExist:
			raise Http404("Article does not exists")
	
	else:
		return HttpResponse("değil")