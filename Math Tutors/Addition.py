import random

var = raw_input("Do you want to become a Math geek? Well do you? (Y or N)")

if(var == "N"):
	print "Fine, I bet you would suck at it anyways..."
	
else:
	print "Well alright, let's get started"

	score = 0

	for i in range(3):
		var1 = random.randint(1,40)
		var2 = random.randint(1,40)
		var4 = var1 + var2
		var3 = raw_input("What is " + str(var1) + " plus " +str(var2)+" ?      \n>>  ")	
		if (float(var4) == float(var3)):
			print "That'a boy!"
			score += 1
		else:
			print "Oh, too bad, the answer is " + str(var1 + var2) + " let's try again"
print score
percent = float(int((float(score)/3)*10000))/100
print "Wow! you scored " + str(float(percent)) + " percent congrats!!!" 

