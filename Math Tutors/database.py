import MySQLdb

def connect(database):
	db = MySQLdb.connect(host='localhost',
						user = 'root',
						passwd='root',
						db = database)
	cur=db.cusor()

	return cur
