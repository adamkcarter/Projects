import MySQLdb

def connect():
	db = MySQLdb.connect(host='localhost',
						user = 'root',
						passwd='root',
						db = 'mathTutors')

	return db
