import MySQLdb
import database as d
#Accepts no parameter, returns the number of users that exist in the 'users' DB
def getNumberOfUsers():
	db = d.connect()

	cur = db.cursor()

	lookUpStatment = 'SELECT count(username) from users'

	cur.execute(lookUpStatment)

	return cur.fetchall()[0][0]

	cur.close()
	db.close()

#Will check the given username for it's existance in the database: mathTutors, this function returns true if the name is unique and flase otherwise.
def uniqueUser(username):
	db = d.connect()

	cur=db.cursor()

	lookUpStatement = 'SELECT username FROM users'

	cur.execute(lookUpStatement)

	usernames = cur.fetchall()

	for row in usernames:
		if username == row[0]:
			return False

	return True

	cur.close()
	db.close()


#Will insert the given username into the 'users' DB. Returns True
def signUp(username):
	#This function will take a user name and insert it into the user database in mathTutors
	db = d.connect()

	cur = db.cursor()

	lookUpStatement = 'Select max(userNo) from users'

	cur.execute(lookUpStatement)
	number = cur.fetchall()[0][0]

	if number == None:
		number = 1
	else: 
		number += 1

	sqlStatement = 'INSERT INTO users (username, userNo) VALUES ("%s", %d)' % (username, number)

	cur.execute(sqlStatement)
	db.commit()

	cur.close()
	db.close()
	return True

#Accepts a number as input and returns the name of the user associated to that number
def findUser(userNo):
	db = d.connect()

	cur = db.cursor()

	lookUpStatement= 'SELECT username from users where userNo = %d' % (userNo)

	cur.execute(lookUpStatement)

	return cur.fetchall()[0][0]

	cur.close()
	db.close()

#Accepts, username, subject, timeTaken and percent inserting all into the 'score' DB. Returns True
def keepScore(username,subject,timeTaken, percent): #CHANGED THE ARGUMENT ORDER
	db = d.connect()

	cur = db.cursor()

	####Find the user's number
	lookUpStatement = 'SELECT userNo from users where username = "%s"' % (username) 

	cur.execute(lookUpStatement)

	userNo = cur.fetchall()[0][0]
	
	###Insert the score and commit the transaction 
	insertStatement = 'INSERT INTO score (username, subject, timeTaken, percent, userNo) VALUES ("%s", "%s", %f, %f, %3.d)' % (username, subject, timeTaken, percent, userNo)

	###print '("%s", "%s", %f, %f, %d)' % (username, subject, timeTaken, percent, userNo) #DEBUGGING

	cur.execute(insertStatement)
	db.commit()

	#print 'yes' #DEBUGGING

	cur.close()
	db.close()
	return True
