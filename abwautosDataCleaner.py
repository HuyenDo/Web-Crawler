import os
class DataCleaner(object):
	
	def __init__(self, soup, filename):
		self.soup = soup
		self.rawData = soup.find_all("div", class_ ="inventoryListItem")
		if os.path.isfile(filename):
			os.remove(filename)
		self.f = open(filename, 'w')
		self.filename = filename

	def generateTextFile(self):
		print "Processing: ", self.filename
		header = ["ID", "Make_and_Model", "Exterior", "Interior", "Transmission ", 
				 "Engine", "VIN" ,"Mileage", "Price", "URL"]
		self.f.write('{:<16} {:<40} {:<10} {:<30} {:<15} {:<10} {:<20} {:<20} {:<10} {:>30} \n\n'.format(*header))
		car_cointainer = []
		for data in self.rawData:
			car_info = []
			try:
				ID = data.contents[1].get('id')
			except Exception, e:
				ID = ""
			try:
				Make_and_Model = data.contents[1].find('h1').text
			except Exception, e:
				Make_and_Model = ""
			
			for li in data.contents[1].find("div",class_ = "column1").find_all("li"):
				try:
					car_info.append(li.find('label').next_sibling)
				except Exception, e:
					car_cointainer.append("")
			
			[Exterior, Interior, Transmission, Engine, VIN, Mileage] = car_info
			try:
				Price = data.contents[1].find("div", class_ = "column3").find('h5').next_sibling.replace('\n','').replace('\t','')
			except Exception, e:
				Price = ""
			try:
				URL = data.contents[1].find("img").get('src')
			except Exception, e:
				URL = ""

			aCar_details = [ID.encode('ascii', 'ignore') ,  Make_and_Model.encode('ascii', 'ignore') , Exterior.encode('ascii', 'ignore') ,
						  Interior.encode('ascii', 'ignore') ,Transmission.encode('ascii', 'ignore') , Engine.encode('ascii', 'ignore') ,
						  VIN.encode('ascii', 'ignore') , Mileage.encode('ascii', 'ignore') , Price.encode('ascii', 'ignore') , URL.encode('ascii', 'ignore') ]
			car_cointainer.append(aCar_details)
			
		for car in car_cointainer:
			self.f.write('{:<16} {:<40} {:<10} {:<30} {:<15} {:<10} {:<20} {:<20} {:<10} {:>30} \n\n'.format(*car))

		print "Done !!!"
	