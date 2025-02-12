from django.contrib import admin
from .models import Place

@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
	list_display = ('name', 'page_title', 'meta_title')
	search_fields = ('name', )