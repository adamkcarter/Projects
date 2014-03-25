def getNumberOfUsers():
	w = open('USER_NAMES')
	lst = w.readlines()
	return (len(lst)-1)
	w.close()

def signUp():
		name = raw_input("\n\nOkay, let's get started by getting your name.\n>> ")
		noUsers = getNumberOfUsers()
		w = open('USER_NAMES','a')
		w.write(str(noUsers+1) + '. ' + name+'\n')
		w.close()
		print "\n\nGreat, here is your User Name: "+str(name)+". You are user number " + str(noUsers+1) + " Thank you for signing up\n"
		return name

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

def keepScore(name,time,percent):
	w = open('SCORE_BOARD','a')
	lenName = len(name)
	lenTime = len(str(time))
	lenPercent = len(str(percent))

	w.write(str(name)+',')
	for i in range(20-(lenName+1)):
		w.write(' ')

	w.write(str(time)+',')
	for i in range(20-(lenTime+1)):
		w.write(' ')

	w.write(str(percent)+',')
	for i in range(20-(lenPercent+1)):
		w.write(' ')

	w.write('\n')
	w.close()