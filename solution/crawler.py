import requests
from bs4 import BeautifulSoup
import sys

print sys.argv

[_,base_url, next_page_url_info, filename, data_cleaner_class, num_page] = sys.argv

if ".py" in data_cleaner_class:
	data_cleaner_class = data_cleaner_class.replace(".py", "")

module = __import__(data_cleaner_class)

url = base_url

for i in range(1,int(num_page)+1):
	
	url = base_url + next_page_url_info.replace('#',str(i))
	
	req = requests.get(url)

	if req.status_code == 200:
		soup = BeautifulSoup(req.content, "html.parser")

		data_cleaner = module.DataCleaner(soup, filename + str(i) + ".txt")
		data_cleaner.generateTextFile()
	else:
		print "Cannot make a 'GET' request on url: " + url 
		print "Error code: " + str(req.status_code)
		print "Program Terminated !!!"
		break