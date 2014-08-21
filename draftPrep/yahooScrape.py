import requests
import urllib2
from bs4 import BeautifulSoup

#response = requests.get('http://games.espn.go.com/ffl/leaders?sortMap=AAAAARgAAAAHAQAMc3RhdFNlYXNvbklkAwAAB90BAAhjYXRlZ29yeQMAAAACAQAJZGlyZWN0aW9uA%2F%2F%2F%2F%2F8BAAZjb2x1bW4D%2F%2F%2F%2F%2FQEAC3NwbGl0VHlwZUlkAwAAAAABABBzdGF0U291cmNlVHlwZUlkAwAAAAABAAtzdGF0UXVlcnlJZAMAAAABA&startIndex=0')
#soup = BeautifulSoup(response.text)

#links = soup.find_all('tr')


### Found peyton and his points
"""
first = links[3]
rows = first.find_all('td')

print rows[0].text, rows[20].text
"""

for j in range(11):
	response = requests.get('http://football.fantasysports.yahoo.com/f1/9334/players?status=ALL&pos=O&cut_type=9&stat1=S_S_2013&myteam=0&sort=PTS&sdir=1&count=' + str(25*j))
	soup = BeautifulSoup(response.text)

	tableRow = soup.find_all('tr')

	w = open('data','a')

	for i in range(28)[3:]:
		data = tableRow[i].find_all('td')
		newlineIndex = data[1].text[2:].index('\n')+3
		hyphenIndex = data[1].text[20:].index('-') +25
		
		w.write(data[1].text[newlineIndex:hyphenIndex] + ', ' + data[4].text + '\n')


	w.close()