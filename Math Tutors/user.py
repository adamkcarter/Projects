import MySQLdb

def getNumberOfUsers():
	w = open('USER_NAMES')
	lst = w.readlines()
	return (len(lst)-1)
	w.close()

def uniqueUser(user):
	db = MySQLdb.connect(host='localhost',
						user = 'root',
						passwd='root',
						db = 'mathTutors')
	cur=db.cursor()

	sqlStatement = 'SELECT * FROM users'

	cur.execute(sqlStatement)

	usernames = cur.fetchall()

	for row in usernames:
		if user == row[0]:
			return False

	return True

def signUp(user):
	#This function will take a user name and write it to the file USER_NAMES
	db = MySQLdb.connect(host='localhost',user='root',passwd='root',db='mathTutors')

	cur = db.cursor()

	sqlStatement = 'INSERT INTO users (username) VALUES ("%s")' % (user)

	cur.execute(sqlStatement)
	db.commit()
	print 'Thank you for signing up'



def findUser(x):
	w = open('USER_NAMES')
	char = w.read(1)
	while char != '':
		if char == str(x):
			w.seek(2,1)
			lst = w.readline()
			leng = len(lst)
			return lst[0:(leng-1)]
			w.close()
		else:
			char = w.read(1)
	w.close()

def keepScore(name,time,percent, subject):
	w = open('SCORE_BOARD','a')
	lenName = len(name)
	lenTime = len(str(time))
	lenPercent = len(str(percent))
	lenSubject = len(subject)

	w.write(str(name)+',')
	for i in range(20-(lenName+1)):
		w.write(' ')

	w.write(str(time)+',')
	for i in range(20-(lenTime+1)):
		w.write(' ')

	w.write(str(percent)+',')
	for i in range(20-(lenPercent+1)):
		w.write(' ')

	w.write(subject + ',')

	w.write('\n')
	w.close()

def userUnique(x):
	w = open('USER_NAMES')
	lst = w.readlines()
	w.close()
	lst2 = []

	for i in lst:
		lst2.append(i.count(x))

	if sum(lst2) > 0:
		return False
	else:
		return True
