import json
import MySQLdb
from slugify import slugify


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

def updateLocation():
	cursor.execute("SELECT * FROM rentals_rental where location = '' and longJSON <> ''")
	results = cursor.fetchall()

	for result in results:
		try:
			json_data = json.loads(result[13])
			location = (json_data['listing']['primaryLocation']['description'])
			cursor.execute("update rentals_rental set location = '%s' where id = %d" %(location, result[0]))
			db.commit()
			print(location)
			
		
		except Exception as e:
			print("hata")
			pass



def updateRateAndReviews():
	cursor.execute("SELECT * FROM rentals_rental where is_checked=0")
	results = cursor.fetchall()

	for result in results:
		try:
			json_data = json.loads(result[10])
			longJSON = json.loads(result[13])
			rating = (json_data['averageRating'])
			review = (json_data['reviewCount'])
			cursor.execute("update rentals_rental set is_checked=1, averageRating = %s, reviewCount = %s where id = %d" %(rating, review, result[0]))
			db.commit()
			print(rating, review)
			
		
		except Exception as e:
			print("hata")
			cursor.execute("update rentals_rental set is_checked=0 where id = %d" % result[0])
			db.commit()
			pass




def extractLocations():
	cursor.execute("SELECT id, longJSON FROM rentals_rental")
	results = cursor.fetchall()

	for result in results:
		try:
			json_data = json.loads(result[1])
			breadcrumbs = json_data['listing']['regions']
			for breadcrumb in breadcrumbs:
				try:
					name = breadcrumb['name'].replace("'", " ").replace('"', ' ')
					slug = slugify(name)
					search_term = name
					response = cursor.execute("SELECT name FROM destinations_place WHERE name='%s'" % name)
					if response != 1:
						cursor.execute("INSERT INTO `destinations_place` (`name`, `slug`, `search_term`) VALUES ('%s', '%s', '%s')" % (name, slug, search_term))
						db.commit()
						print(cursor.lastrowid)
				except Exception as e:
					print("hata", result[0])
		except Exception as e:
			print("Breadcrumb Yok", result[0])
			cursor.execute("UPDATE rentals_rental SET is_checked=2 WHERE id = %s" % result[0])
			db.commit()
#extractLocations()



def updateRelations():
	cursor.execute("truncate rentals_relations")
	cursor.execute("SELECT id, longJSON, price, sleeps, bedrooms, bathrooms FROM rentals_rental")
	results = cursor.fetchall()

	for result in results:
		try:
			json_data = json.loads(result[1])
			breadcrumbs = json_data['listing']['regions']
			for breadcrumb in breadcrumbs:
				try:
					name = breadcrumb['name'].replace("'", " ").replace('"', ' ')
					slug = slugify(name)
					cursor.execute("SELECT * FROM destinations_place WHERE name='%s'" % name)
					places = cursor.fetchall()
					for place in places:
						query = ("INSERT INTO rentals_relations (place_id, rental_id, price, sleeps, bathrooms, bedrooms) VALUES(%d,%d, %d, %d, %d, %d)" % (place[0], result[0], result[2], result[3], result[4], result[5]) )
						print(query)
						cursor.execute(query)
				except Exception as e:
					print("hata", e)
		except Exception as e:
			print("Breadcrumb Yok", result[0])
			cursor.execute("UPDATE rentals_rental SET is_checked=2 WHERE id = %s" % result[0])
			db.commit()
#updateRelations()

def updatePlaceCount():
	cursor.execute("SELECT * FROM destinations_place")
	places = cursor.fetchall()

	for place in places:
		cursor.execute("SELECT count(*) FROM rentals_relations WHERE place_id = %s" % place[0])
		count = cursor.fetchone()[0]
		cursor.execute("UPDATE destinations_place SET count = %s WHERE id = %s" % (count, place[0]))
		print(place[0], count)
	db.commit()

updatePlaceCount()