import sys

sys.argv = ['crawler.py','http://www.abwautos.com/', r'vehicles?Page=#', 'output', 'abwautosDataCleaner', '7' ]
print ("Scrapping website http://www.abwautos.com/")
execfile('crawler.py')

print ("\n********************************\n")
print ("Scrapping website http://www.yellowpages.com/")
sys.argv = ['crawler.py','http://www.yellowpages.com/', r'search?search_terms=restaurant&geo_location_terms=Waipahu%2C%20HI&page=#', 'yellowpagesOutput', 'yellowpagesDataCleaner', '5']
execfile('crawler.py')

print ("\n********************************\n")
print ("Scrapping website http://stackoverflow.com/")
sys.argv = ['crawler.py','http://stackoverflow.com/', r'questions?page=#&sort=newest', 'stackoverflowOutput', 'stackoverflowDataCleaner.py', '4']
execfile('crawler.py')