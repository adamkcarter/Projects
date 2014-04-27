import user as u
import MySQLdb

user1 = 'camels'
user2 = 'adam'

#TEST1 Validates number of users
no = u.getNumberOfUsers() 
if no == 26:
	print True
else:
	print 'number of users off'

#TEST2 Validates that unique user finds an existing user
if u.uniqueUser(user2) == False:
	print True
else:
	print 'Unique test one fails'

#TEST3 Validates that uniqueUser returns true for non-existing usernames
if u.uniqueUser(user1) == True:
	print True
else: 
	print 'Unique test two fails'

#TEST4 tests that signUp works
if u.signUp('adam'):
	print True
else:
	print 'Sign up fails'

#TEST5 tests that findUser works for adam
if u.findUser(10) == 'adam':
	print True
else:
	print 'Find user test 1 fails'

#TEST6 same for Bo Jackson
if u.findUser(3) == 'cameling':
	print True
else:
	print 'Find user test 2 fails'

#TEST7 Shows that the keepScore test works fine
if u.keepScore(user2,'Multiplication',7574.33, 1.00):
	print True
else:
	print 'score test fails'