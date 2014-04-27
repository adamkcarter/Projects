import database as d
import MySQLdb

db = d.connect()
cur = db.cursor()

lookUpStatement = 'SELECT * FROM users'

cur.execute(lookUpStatement)

results = cur.fetchall()

for i in results:
	if (i[1]>9):
		print str(i[1]) + ' ' + str(i[0])
	else:
		print str(i[1]) + '  ' + str(i[0])

cur.close()
db.close()