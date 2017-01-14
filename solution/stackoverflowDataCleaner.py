import os
import requests
from bs4 import BeautifulSoup

class DataCleaner(object):
	
	def __init__(self, soup, filename):
		self.soup = soup
		
		self.rawData = soup.find(id="mainbar").find(id="questions").find_all("div", class_="question-summary")
		if os.path.isfile(filename):
			os.remove(filename)
		self.f = open(filename, 'w')
		self.filename = filename

	def generateTextFile(self):
		print "Processing: ", self.filename
		header = ["Question","Author", "Votes", "Answers", "Views"]
		self.f.write('{:<110} {:<25} {:<10} {:<10} {:<10} \n\n'.format(*header))
		post_cointainer = []
		
		for data in self.rawData:
			try:
				[Votes,Answers] =  [item.text.encode('ascii', 'ignore') for item in data.find("div", class_="stats").find_all("strong")]
				Views = data.find("div", class_="views").get("title").strip(" views").encode('ascii', 'ignore')
				Question = data.find("div", class_="summary").contents[1].text.encode('ascii', 'ignore')
				Author = data.find("div", class_="user-details").contents[1].text.encode('ascii', 'ignore')
				aPost = [Question, Author, Votes, Answers, Views]
				post_cointainer.append(aPost)
			except Exception, e:
				continue

		for post in post_cointainer:
			self.f.write('{:<110} {:<25} {:<10} {:<10} {:<10} \n\n'.format(*post))
		print "Done !!!"