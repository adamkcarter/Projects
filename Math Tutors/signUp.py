def getNumberOfUsers():
	w = open('USER_NAMES')
	for i in range(100):
		if w.readline() == '':
			return i
			w.close()
			break;

def signUp():
	ans1 = raw_input("Do you want to sign up to keep your stats? Y or N\n>> ")
	if (ans1 == 'Y' or ans1 == 'y' or ans1 == 'yes'):
		name = raw_input("Okay, let's get started by getting your name.\n>> ")
		noUsers = getNumberOfUsers()
		w = open('USER_NAMES','a')
		w.write(str(noUsers) + '. ' + name + '\n')
		w.close()
		print "Great, here is your User Name: "+str(name)+". You are user number " + str(noUsers) + " Thank you for signing up"
	else:
		print "Okay, let's get started"