def scrapeWeb():
	scrape_url = f'http://{host}/{site}/check_mk/login.py'
	response = requests.get(scrape_url)

	soup = BeautifulSoup(response.content, 'html.parser')

	remaining_time_elements = soup.find_all(class_="remaining_time")

	remaining_times = [element.get_text() for element in remaining_time_elements]
	
	for remaining_time in remaining_times: #saves into remaining_time
	
	with open(time, 'w') as file:
		file.write(remaining_time)

	soup = BeautifulSoup(response.content, 'html.parser')

	foot_element = soup.find(id="foot")

	if foot_element:
    foot_text = foot_element.get_text() #saves into foot_text