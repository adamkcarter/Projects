"""
This is a simple muliplication tutor, the upper and lower bounds can be changed to any numbers you desire. We use two modules and draw from another file holding some useful functions.
"""

import random
import user as u
from time import *

# Set the lower and upper bounds on the numbers you will be asked to mutiply together

lowerBound = 10
upperBound = 40

# Ask if the user has signed up before

user = raw_input("\n\nDo you have a user name?\n\n>> ")

if user == 'y':
	while True:
		print '\nPlease type the number associated to your Username\n'
		w = open('USER_NAMES')
		print w.read()
		w.close()
		find = raw_input('\n>> ')
		user = str(u.findUser(find))
		if user == 'None':
			print '\n\nI\'m sory, we couldn\'t find you\n\n'
		else:
			you = raw_input('\nAre you ' + user + '\n>> ')
			if you == 'y':
				print '\n\nGreat, let\'s get started\n'
				break;		
			else: 
				ans = raw_input('\n\nTry again?\n>> ')
				if ans == 'n':
					break;
else:
	print "\n\nIf this is your first time, you should sign up to keep your stats. Do you want to sign up?\n"
	ans = raw_input('>> ')

	if ans == 'y':
		user = u.signUp()
	else: 
		print "\n\nOkay, no problem. You can always sign up later\n\n"

print "\n\nWe're going to do some multiplication drills! Get ready!\n"

sleep(1)
print 'Ready\n'
sleep(1)
print 'Set\n'
sleep(1)
print 'GO!!\n'

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
if user != 'n':
	u.keepScore(user,elapsed,percent)


