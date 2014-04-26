import user as u
import MySQLdb


def insert(name):
	db = MySQLdb.connect(host='localhost',
					user = 'root',
					passwd='root',
					db = 'mathTutors')
	
	cur=db.cursor()

	insertStatement = 'INSERT INTO users (username) VALUES ("%s")' % (name)
	print insertStatement
	usernamess = cur.execute(insertStatement)
	print name
	db.commit()

username = 'camel'

if u.uniqueUser(username):
	print 'get ready for sign up'
	u.signUp(username)
else:
	print 'sorry that exists'
#u.uniqueUser('a')
