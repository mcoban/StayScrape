from django.contrib import admin
from .models import Country, City, District

@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
	list_display = ('name', )


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
	list_display = ('name', 'country')


@admin.register(District)
class DistrictAdmin(admin.ModelAdmin):
	list_display = ('name', 'city')