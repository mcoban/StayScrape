import json
import MySQLdb
from slugify import slugify


rental_types = [
	{ 'id': 1,  'name': 'villa', 'title': 'Villa' },
	{ 'id': 2,  'name': 'house', 'title': 'House' },
	{ 'id': 3,  'name': 'apartment', 'title': 'Apartment' },
	{ 'id': 4,  'name': 'cottage', 'title': 'Cottage' },
	{ 'id': 5,  'name': 'condo', 'title': 'Condo' },
	{ 'id': 6,  'name': 'resort', 'title': 'Resort' },
	{ 'id': 7,  'name': 'townhome', 'title': 'Townhome' },
	{ 'id': 8,  'name': 'mobile-home', 'title': 'Mobile Home' },
	{ 'id': 9,  'name': 'studio', 'title': 'Studio' },
	{ 'id': 10, 'name': 'estate', 'title': 'Estate' },
	{ 'id': 11, 'name': 'bungalow', 'title': 'Bungalow' },
	{ 'id': 12, 'name': 'farmhouse', 'title': 'Farmhouse' },
	{ 'id': 13, 'name': 'barn', 'title': 'Barn' },
	{ 'id': 14, 'name': 'chalet', 'title': 'Chalet' },
	{ 'id': 15, 'name': 'chateau-country-house', 'title': 'Chateau / Country House' },
	{ 'id': 16, 'name': 'house-boat', 'title': 'House Boat' },
	{ 'id': 17, 'name': 'guest-house', 'title': 'Guest House' },
	{ 'id': 18, 'name': 'lodge', 'title': 'Lodge' },
	{ 'id': 19, 'name': 'castle', 'title': 'Castle' }
]

db = MySQLdb.connect("127.0.0.1", "root", "condor", "stayscrape")
cursor = db.cursor()


def updatePropertyTypes():
	cursor.execute("SELECT * FROM rentals_rental where propertyType = 0")
	results = cursor.fetchall()

	for result in results:
		try:
			json_data = json.loads(result[10])
			propertyType = slugify(json_data['propertyType'])
			for rental_type in rental_types:
				if propertyType == rental_type['name']:
					print(propertyType)
					cursor.execute("update rentals_rental set propertyType = %d where id = %d" %(rental_type['id'], result[0]))
					db.commit()
		
		except Exception as e:
			print("hata")
			pass

# updatePropertyTypes()

