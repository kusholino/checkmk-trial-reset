import requests
from bs4 import BeautifulSoup
from colors import red, green, yellow

def scrapeWeb(host, site): #fetches remaining time
	hosts = host
	sites = site
	time = 'time'
	scrape_url = f'http://{hosts}/{sites}/check_mk/login.py' #url for the login page to be scraped for infos
	response = requests.get(scrape_url)

	soup = BeautifulSoup(response.content, 'html.parser')

	remaining_time_elements = soup.find_all(class_="remaining_time") #searches for the class remaining_time

	remaining_times = [element.get_text() for element in remaining_time_elements]
	
	for remaining_time in remaining_times: #saves into remaining_time
		remaining_time = remaining_time
		with open(time, 'w') as file:	#writing time to file for the service to use
			file.write(remaining_time)
		numeric_part = ''.join(filter(str.isdigit, remaining_time))	#searches for digits in the string and saves them used for comparison
		number = int(numeric_part)

		if number >=20:		#visuals for printouts
			return green+remaining_time
		elif number <20 & number >= 10:
			return yellow+remaining_time
		elif number < 10:
			return red+remaining_time

def scrapeVers(host, site):	#fetches version
	hosts = host
	sites = site
	scrape_url = f'http://{hosts}/{sites}/check_mk/login.py' #login page to scrape
	response = requests.get(scrape_url)

	soup = BeautifulSoup(response.content, 'html.parser')

	foot_element = soup.find(id = "foot")	#search for the id foot

	if foot_element:
		foot_text = foot_element.get_text()	#extract the text
		version = foot_text.split(':')[1].split('-')[0].strip() #strip the part i want 
		return version