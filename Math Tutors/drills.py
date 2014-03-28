"""
This is a simple muliplication tutor, the upper and lower bounds can be changed to any numbers you desire. We use two modules and draw from another file holding some useful functions.
"""

import random
import user as u
from time import *

# Set the lower and upper bounds on the numbers you will be asked to mutiply together

def Multiplication(user):
	lowerBound = 10
	upperBound = 40
	subject = 'Multiplication'

	print "\n\nHello %s,\nWe're going to do some multiplication drills! Get ready!\n" % (user)
	print '\nYou will be given two numbers between %d and %d, good luck!' % (lowerBound, upperBound)
	print '\n\nDon\'t forget it\'s timed!\n'

	sleep(3)
	print '\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nReady\n\n\n\n\n'
	sleep(1)
	print '\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nSet\n\n\n\n\n'
	sleep(1)
	print '\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nGO!!\n\n\n\n\n'
	sleep(1)
	print '\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n'
	#Defining both score and lst to keep track of time elapsed and the percentage of correct responses.

	lst = [0,0]
	lst[0]= time()
	score = 0

	for i in range(3):
		var1 = random.randint(lowerBound,upperBound)
		var2 = random.randint(lowerBound, upperBound)
		var3 = var1 * var2
		var4 = raw_input("\nWhat is " + str(var1) + " times " +str(var2)+" ?\n      \n>> ")	
		if (float(var3) == float(var4)):
			print "\nThat'a boy!\n"
			score += 1
		else:
			if i == 2:
				print '\n\nSorry, that\'s wrong. The answer was '+str(var3) +' Better luck next time.\n'
			else:
				print "\n\nOh, too bad, the answer is \n\n" + str(var3) + "\n\nlet's try again\n\n"
	lst[1] = time()
	elapsed=lst[1]-lst[0]
	percent = float(int((float(score)/3)*10000))/100
	print "\n\nWow! you scored " + str(float(percent)) + " percent congrats!!!\n" 
	sleep(3)
	u.keepScore(user,elapsed,percent,subject)

def Addition(user):
	lowerBound = 1000
	upperBound = 8000
	subject = 'Addition'

	print "\n\nHello %s,\nWe're going to do some addition drills! Get ready!\n" % (user)
	print '\nYou will be given two numbers between %d and %d, good luck!' % (lowerBound, upperBound)
	print '\n\nDon\'t forget it\'s timed!'

	sleep(3)
	print '\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nReady\n\n\n\n\n'
	sleep(1)
	print '\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nSet\n\n\n\n\n'
	sleep(1)
	print '\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nGO!!\n\n\n\n\n'
	sleep(1)
	print '\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n'

	#Defining both score and lst to keep track of time elapsed and the percentage of correct responses.

	lst = [0,0]
	lst[0]= time()
	score = 0

	for i in range(3):
		var1 = random.randint(lowerBound,upperBound)
		var2 = random.randint(lowerBound, upperBound)
		var3 = var1 + var2
		var4 = raw_input("\nWhat is " + str(var1) + " plus " +str(var2)+" ?\n      \n>> ")	
		if (str(var3) == var4):
			print "\nThat'a boy!\n"
			score += 1
		else:
			if i == 2:
				print '\n\nSorry, that\'s wrong. The answer was '+str(var3) +' Better luck next time.\n'
			else:
				print "\n\nOh, too bad, the answer is \n\n" + str(var3) + "\n\nlet's try again\n\n"
	lst[1] = time()
	elapsed=lst[1]-lst[0]
	percent = float(int((float(score)/3)*10000))/100
	print "\n\nWow! you scored " + str(float(percent)) + " percent congrats!!!\n" 
	sleep(3)
	u.keepScore(user,elapsed,percent,subject)

def Subtraction(user):
	lowerBound = 1000
	upperBound = 8000
	subject = 'Subtraction'

	print "\n\nHello %s,\nWe're going to do some subtraction drills! Get ready!\n" % (user)
	print '\nYou will be given two numbers between %d and %d, good luck!' % (lowerBound, upperBound)
	print '\n\nDon\'t forget it\'s timed!'

	sleep(3)
	print '\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nReady\n\n\n\n\n'
	sleep(1)
	print '\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nSet\n\n\n\n\n'
	sleep(1)
	print '\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nGO!!\n\n\n\n\n'
	sleep(1)
	print '\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n'

	#Defining both score and lst to keep track of time elapsed and the percentage of correct responses.

	times = [0,0]
	times[0]= time()
	score = 0

	for i in range(3):
		lst = []
		lst.append(random.randint(lowerBound,upperBound))
		lst.append(random.randint(lowerBound, upperBound))
		var1 = max(lst)
		var2 = min(lst)
		var3 = var1 - var2
		var4 = raw_input("\nWhat is " + str(var1) + " minus " +str(var2)+" ?\n      \n>> ")	
		if (float(var3) == float(var4)):
			print "\nThat'a boy!\n"
			score += 1
		else:
			if i == 2:
				print '\n\nSorry, that\'s wrong. The answer was '+str(var3) +' Better luck next time.\n'
			else:
				print "\n\nOh, too bad, the answer is \n\n" + str(var3) + "\n\nlet's try again\n\n"
	times[1] = time()
	elapsed=times[1]-times[0]
	percent = float(int((float(score)/3)*10000))/100
	print "\n\nWow! you scored " + str(float(percent)) + " percent congrats!!!\n" 
	sleep(3)
	u.keepScore(user,elapsed,percent,subject)