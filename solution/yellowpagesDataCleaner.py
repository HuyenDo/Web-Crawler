import os
import requests
from bs4 import BeautifulSoup

class DataCleaner(object):
	
	def __init__(self, soup, filename):
		self.soup = soup
		self.rawData = soup.find("div", class_ ="search-results organic").find_all("div", class_="result")
		if os.path.isfile(filename):
			os.remove(filename)
		self.f = open(filename, 'w')
		self.filename = filename

	def generateTextFile(self):
		print "Processing: ", self.filename
		header = ["Restaurant", "Address", "Telephone", "Categories", "Website"]
		self.f.write('{:<50} {:<100} {:<15} {:<40} {:<10} \n\n'.format(*header))
		restaurant_cointainer = []
		for data in self.rawData:
			try:
				div_info = data.find("div", class_= "info")
			except Exception, e:
				continue
			try:
			 	name = div_info.contents[0].text.encode('ascii', 'ignore')
			except Exception, e:
			 	name = ""
			try:
				address_contact_info = div_info.contents[1].find("p", attrs={"itemprop":"address"})
				street_address = address_contact_info.contents[0].text.encode('ascii', 'ignore')
				address_locality = address_contact_info.contents[1].text.encode('ascii', 'ignore')
				address_region = address_contact_info.contents[2].text.encode('ascii', 'ignore')
				address_postalcode = address_contact_info.find("span", attrs={"itemprop":"postalCode"}).text.encode('ascii', 'ignore')
				address_string = street_address + ', ' + address_locality + ' ' + address_region + ', ' + address_postalcode
				
			except Exception, e:
				address_string = ""
			
			try:
				telephone = div_info.find("div", class_="phones phone primary").text.encode('ascii', 'ignore')
				
			except Exception, e:
				telephone = ""
			
			categories = ""
			website = ""
			try:
				extra_info = div_info.find("div", class_="info-section info-secondary")
				categories_info = extra_info.find("div", class_="categories").find_all("a")
				for category in categories_info:
					categories += category.text.encode('ascii', 'ignore')
				website = extra_info.find("div", class_="links").contents[0].get("href").encode('ascii', 'ignore')

			except Exception, e:
				pass

			aRestaurant_details = [unicode(name), unicode(address_string), unicode(telephone), unicode(categories), unicode(website)]
			
			restaurant_cointainer.append(aRestaurant_details)
		for restaurant in restaurant_cointainer:
			self.f.write('{:<50} {:<100} {:<15} {:<40} {:<10} \n\n'.format(*restaurant))
		print "Done !!!"
