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
			rating = (json_data['averageRating'])
			review = (json_data['reviewCount'])
			cursor.execute("update rentals_rental set averageRating = %s, reviewCount = %s where id = %d" %(rating, review, result[0]))
			db.commit()
			print(rating, review)
			
		
		except Exception as e:
			print("hata")
			pass

updateRateAndReviews()