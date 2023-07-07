import requests
from bs4 import BeautifulSoup
def scrapeWeb(host, site):
	hosts = host
	sites = site
	time = 'time'
	scrape_url = f'http://{hosts}/{sites}/check_mk/login.py'
	response = requests.get(scrape_url)

	soup = BeautifulSoup(response.content, 'html.parser')

	remaining_time_elements = soup.find_all(class_="remaining_time")

	remaining_times = [element.get_text() for element in remaining_time_elements]
	
	for remaining_time in remaining_times: #saves into remaining_time
		remaining_time = remaining_time
		with open(time, 'w') as file:
				file.write(remaining_time)
				return remaining_time