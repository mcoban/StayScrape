from django.contrib import admin
from .models import Rental, PropertyType

@admin.register(Rental)
class RentalAdmin(admin.ModelAdmin):
	list_display = ('thumbnail', 'regionId', 'price', 'sleeps', 'bedrooms', 'bathrooms', 'view', 'external', 'is_checked')
	list_filter = ('regionId', )


@admin.register(PropertyType)
class PropertyTypeAdmin(admin.ModelAdmin):
	list_display = ('propertyName', 'propertyDescription')