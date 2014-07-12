import MySQLdb
import urllib2
from bs4 import BeautifulSoup

 # change to whatever your url is

def insert(x):
	db = MySQLdb.connect(host='localhost',
					user = 'root',
					passwd='root',
					db = 'nhl')

	cur = db.cursor()

	insertStatment = 'insert into nhlData (player, team, pos, gamesPlayed, goals, assists, points, plusMinus, pim, ppg, ppp, shg, shp, gw, ot, shots, shotPercent, toiPerGoal, shiftPerGoal, faceOffPercentage, year) values (' + x +'\'2010-2011\')'

	#print insertStatment
	cur.execute(insertStatment)
	db.commit()

	cur.close()
	db.close()

for num in range(31)[1:]:
	url = "http://www.nhl.com/ice/playerstats.htm?fetchKey=20112ALLSASALL&viewName=summary&sort=points&pg=" + str(num) 
	
	page = urllib2.urlopen(url).read()
	soup = BeautifulSoup(page)


	rows = soup.find_all('tr')[10:]

	for row in rows:
		new=row.find_all('td')
		string=''
		print len(row)
		for i in new[1:]:
			try :
				num = (i.text).index('\'')
				new = i.text[:num] + '\\'+ i.text[num:]
				string += '\'' + new + '\'' +','
			except:
				string += '\'' + str(i.text) + '\'' +','
		insert(string)




"""	
head_row = soup.find_all('tr')[6]

	head_data = head_row.find_all('th')

	for i in head_data:
		print i.text.text, tds[2].text)
"""