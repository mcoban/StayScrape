import json
import pymysql as mdb
from slugify import slugify


connection = mdb.connect(
	host='localhost',
	user='root',
	password='condor',
	db='stayscrape',
	charset='utf8'
)
cursor = connection.cursor(mdb.cursors.DictCursor)


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
					connection.commit()
		
		except Exception as e:
			print("hata")
			pass


def updateLocation():
	cursor.execute("SELECT * FROM rentals_rental where location = '' and longJSON <> ''")
	results = cursor.fetchall()

	for result in results:
		try:
			json_data = json.loads(result[13])
			location = (json_data['listing']['primaryLocation']['description'])
			cursor.execute("update rentals_rental set location = '%s' where id = %d" %(location, result[0]))
			connection.commit()
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
			connection.commit()
			print(rating, review)
			
		
		except Exception as e:
			print("hata")
			cursor.execute("update rentals_rental set is_checked=0 where id = %d" % result[0])
			connection.commit()
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
						connection.commit()
						print(cursor.lastrowid)
				except Exception as e:
					print("hata", result[0])
		except Exception as e:
			print("Breadcrumb Yok", result[0])
			cursor.execute("UPDATE rentals_rental SET is_checked=2 WHERE id = %s" % result[0])
			connection.commit()



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
			connection.commit()



def updatePlaceCount():
	cursor.execute("SELECT * FROM destinations_place")
	places = cursor.fetchall()

	for place in places:
		cursor.execute("SELECT count(*) FROM rentals_relations WHERE place_id = %s" % place[0])
		count = cursor.fetchone()[0]
		cursor.execute("UPDATE destinations_place SET count = %s WHERE id = %s" % (count, place[0]))
		print(place[0], count)
	connection.commit()



def generateSitemap():
	root = "https://stayscrape.com"
	cursor.execute("SELECT * FROM destinations_place")
	places = cursor.fetchall()

	content = ""

	for place in places:
		item = """
			<url>
				<loc>%s/villas/%s</loc>
				<priority>1</priority>
			</url>
		""" % (root, place["slug"])
		content += item

	cursor.execute("SELECT * FROM rentals_rental")
	rentals = cursor.fetchall()

	for rental in rentals:
		try:
			rental["longJSON"] = json.loads(rental["longJSON"])
			item = """
				<url>
					<loc>%s/rental/%s-villa-%d</loc>
				</url>
			""" % (root, slugify(rental["longJSON"]["listing"]["primaryLocation"]["description"]), rental["id"])
			content += item
		except:
			pass

	sitemap_body = """
<?xml version="1.0" encoding="UTF-8"?>

<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">

   %s

</urlset> 
	""" % content

	f = open("templates/sitemap.xml", "w")
	f.write(sitemap_body)
	f.close()
	print("Sitemap is OK!")



def updateSlugs():
	cursor.execute("SELECT * FROM rentals_rental WHERE slug=''")
	rentals = cursor.fetchall()

	for rental in rentals:
		try:
			rental["longJSON"] = json.loads(rental["longJSON"])
			slug = ("%s-villa" % slugify(rental["longJSON"]["listing"]["primaryLocation"]["description"]))
			# slug = ("%s-villa" % slugify(rental["longJSON"]["listing"]["geography"]["description"]))
			cursor.execute("UPDATE rentals_rental SET slug='%s' WHERE id=%d" % (slug, rental["id"]))
			connection.commit()
			print(slug)
		except:
			pass

updateSlugs()