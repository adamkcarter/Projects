# Welcome to math tutors!

# cd desktop/coding/projects/'math tutors'

'''''''''''''''''''''''''''''''''''''''
This is where the program comes to life.
'''''''''''''''''''''''''''''''''''''''


import user as u
import time
import drills
import stats as s
import database as d

def title():
	print "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n***********************************************\n	Welcome To Math Tutors! \n***********************************************\n\n"
def gettingStarted():
	response = 0
	while (response == 0):
		title()
		print 'Let\'s sign in to get started\n'
		print '1. Sign in\n2. New? Sign Up\n'

		response = raw_input("\n\n>> ")
		if (int(response) > 3 or int(response) < 0):
			print 'Please try again'
			time.sleep(2)
			response = 0

	while (response == '1'):
		
		title()
		
		print "Please type the number next to your user name.\n\n"
		
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


		userNumber = int((raw_input('>> ')))
		
		title()
		
		user = u.findUser(userNumber)
		
		s = raw_input("\n\n\n\nAre you %s? (Y or N)\n\n>> " % (user))
		
		if s == 'Y' or s == 'y':
			start(user)
			response = 0
		else:
			print 'Let\'s try again'
			time.sleep(2)

	while(response == '2'):
			title()
			print 'Please enter your desired username!'	

			user = raw_input('\n\n>> ')
			if (not u.uniqueUser(user)):
				title()
				print 'I\'m sorry, that username is taken. Please try a new name'
				time.sleep(2)
			else: 
				resp = raw_input('Are you sure you want your user name to be: %s? (Y or N)\n\n>> ' % (user))
				if (resp == 'Y' or resp == 'y'):
					title()
					print 'Thank you, your user name is now: %s.' % (user)
					#store user name
					u.signUp(user)
					response = 0
					start(user)
				else:
					print 'Okay, let\'s try again'


def start(user):
	response = 0
	while True:
		title()
		print 'Hello %s, would you like to practice math or look at stats?' % (user)
		print '\n\n1. Pratice Math\n2. Review Stats\n\n'
		response = raw_input('>> ')

		if response == '1':
			while True:
				title()
				print 'What math would you like to practice?\n\n'
				print '1. Addition\n2. Subtraction\n3. Multiplication\n4. Quit'

				response = raw_input('\n\n\n\n>> ')

				if response == '1':
					drills.Addition(user)
					break;
				elif response == '2':
					drills.Subtraction(user)
					break;
				elif response == '3':
					drills.Multiplication(user)
					break;
				elif response == '4':
					break;
				else:
					print 'Sorry, I didn\'t get that. Please try again'
					time.sleep(2)

			title()
			response = raw_input('\n\nWould you like to practice some more?(Y or N)\n\n>> ')
			if (response == 'Y' or response == 'y'):
				title()
				print 'Wow, you\'re a real go getter!'
				time.sleep(2)
			else:
				title()
				print 'Thank you %s!\n\n\n\n\n\n\n\n\n' % (user)
				time.sleep(2)
				break;
		
		elif response == '2':
			while (True):
				title()
				print 'Welcome to the stats page, what would you like to see?'

				print '1. Best Average Scores\n2. Personal Averages'

				response = raw_input('\n\n>> ')

				if response =='1':
					title()
					s.bestAverageScoreAddition()
					s.bestAverageScoreSubtraction()
					s.bestAverageScoreMultiplication()
					print "\n\nType q to return to the main page"
					response = raw_input('\n\n>> ')
				elif response == '2':
					title()
					s.personalAverageScoreAddition(user)
					s.personalAverageScoreSubtraction(user)
					s.personalAverageScoreMultiplication(user)
					print "\n\nType q to return to the main page"
					response = raw_input('\n>> ')

				if response == 'q':
					break;


gettingStarted()