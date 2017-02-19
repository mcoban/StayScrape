from django.contrib import admin
from .models import Rental

@admin.register(Rental)
class RentalAdmin(admin.ModelAdmin):
	list_display = ('headline', 'regionId', 'price', 'sleeps', 'bedrooms', 'bathrooms')