# Welcome to math tutors!

import user as u
import time
import drills as d

def title():
	print "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n***********************************************\n	Welcome To Math Tutors! \n***********************************************\n\n"
def gettingStarted():
	response = 0
	while (response == 0):
		title()
		print 'Let\'s sign in to get started\n'
		print '1. Sign in\n2. New? Sign Up'

		response = raw_input("\n\n>> ")

	while response == '1':
		title()
		print "Please type the number next to your user name.\n\n"
		w = open('USER_NAMES')
		print w.read() +'\n\n'
		w.close()

		userNumber = (raw_input('>> '))
		title()
		user = u.findUser(userNumber)
		s = raw_input("\n\n\n\nAre you %s? (Y or N)\n\n>> " % (user))
		if s == 'Y' or s == 'y':
			start(user)
			response = 0
		else:
			print 'Let\'s try again'
			time.sleep(2)

	while response == '2':
		title()
		print 'Please enter your desired username!'	

		user = raw_input('\n\n>> ')
		if (not u.userUnique(user)):
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
	while response == 0:
			title()
			print 'What math would you like to practice?\n\n'
			print '1. Addition\n2. Subtraction\n3. Multiplication'

			response = raw_input('\n\n\n\n>> ')

			if response == '1':
				d.Addition(user)
			elif response == '2':
				d.Subtraction(user)
			elif response == '3':
				d.Multiplication(user)

			title()
			response = raw_input('\n\nWould you like to practice some more?(Y or N)\n\n>> ')
			if (response == 'Y' or response == 'y'):
				title()
				print 'Wow, you\'re a real go getter!'
				time.sleep(2)
				response = 0
			else:
				title()
				print 'Thank you for practicing math %s!\n\n\n\n\n\n\n\n\n' % (user)
				time.sleep(2)

gettingStarted()