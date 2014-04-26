""" 

Getting stats for your face

1. Best Average Score
2. Personal Average Score
3. Fastest Average Time
4. Personal Average Time

"""

def bestAverageScoreAddition():
	w = open('SCORE_BOARD')
	scores = w.readlines()
	w.close()

	w = open('USER_NAMES')
	users = w.readlines()
	w.close()
	users.pop(0)

	#This code isolates the user names, at the end users will contain the users 
	new = []
	for i in users:
		x=len(i)
		new.append(i[3:x-1])
	users = new

	#these pops get rid of some useless information in the text doc at the top.
	scores.pop(0)
	scores.pop(0)
	scores.pop(0)

	noUsers = len(users)

	tally=[] #Empty list to store averages

	#This does, for each user obtain their average score.
	for i in users:
		count = 0 # Keeps track of number of attempts made
		score = 0 # Keeps track of total number of averages collected.
		for j in scores:
			x = j.index(',') #find the end of our user name
			if (i == j[0:x] and j[60:] == 'Addition,\n'): # If the user name from SCORE_BOARD matches the username pulled from USER_NAMES and the subject is Addtion then...
				x = j[40:].index(',') #Grab the index number for a comma after the first 40 chars
				count += 1 # Up tick count because this is an attempt from our user
				score += float(j[40:x+40]) #add the percent to score 
		if count == 0: #to avoid no attempts made
			tally.append(str(i)+', '+'0')
		else:
			tally.append(str(i)+', '+str(score/count)) #place both username and their average into the tally list.

	top = [] 

	# Peel just the scores from tally
	for i in tally:
		x = i.index(',')
		top.append(float(i[x+1:]))

	ordered = []
	leng = len(top)
	#order our scores

	for i in range(leng):
		ordered.append(max(top))
		top.pop(top.index(max(top)))

	#take the top three scores
	ordered = ordered[0:3]

	#For each item in tally (Users with their averages) check to see if they're in the top three, if so, add their name (and a padding of spaces) to ordered (a list containing the top three scores)
	for i in tally:
		x = i.index(',')
		num = float(i[x+1:])
		space = ''
		for j in range(20-x):
			space += ' '

		if ordered.count(num) >= 1:
			p = ordered.index(num)
			ordered[p] = str(i[0:x])+space+'||     '+str(num)+'%'

	#Print the bitches
	print 'Best Average Scores for Addition\n********************************\n\n'
	for i in ordered:
		print i
	print '\n\n'

def bestAverageScoreMultiplication():
	w = open('SCORE_BOARD')
	scores = w.readlines()
	w.close()

	w = open('USER_NAMES')
	users = w.readlines()
	w.close()
	users.pop(0)

	#This code isolates the user names, at the end users will contain the users 
	new = []
	for i in users:
		x=len(i)
		new.append(i[3:x-1])
	users = new

	#these pops get rid of some useless information in the text doc at the top.
	scores.pop(0)
	scores.pop(0)
	scores.pop(0)

	noUsers = len(users)

	tally=[] #Empty list to store averages

	#This does, for each user obtain their average score.
	for i in users:
		count = 0 # Keeps track of number of attempts made
		score = 0 # Keeps track of total number of averages collected.
		for j in scores:
			x = j.index(',') #find the end of our user name
			if (i == j[0:x] and j[60:] == 'Multiplication,\n'): # If the user name from SCORE_BOARD matches the username pulled from USER_NAMES and the subject matches...
				x = j[40:].index(',') #Grab the index number for a comma after the first 40 chars
				count += 1 # Up tick count because this is an attempt from our user
				score += float(j[40:x+40]) #add the percent to score 
		if count == 0: #to avoid no attempts made
			tally.append(str(i)+', '+'0')
		else:
			tally.append(str(i)+', '+str(score/count)) #place both username and their average into the tally list.

	top = [] 

	# Peel just the scores from tally
	for i in tally:
		x = i.index(',')
		top.append(float(i[x+1:]))

	ordered = []
	leng = len(top)

	#order our scores

	for i in range(leng):
		ordered.append(max(top))
		top.pop(top.index(max(top)))

	#take the top three scores
	ordered = ordered[0:3]

	#For each item in tally (Users with their averages) check to see if they're in the top three, if so, add their name (and a padding of spaces) to ordered (a list containing the top three scores)
	for i in tally:
		x = i.index(',')
		num = float(i[x+1:])
		space = ''
		for j in range(20-x):
			space += ' '

		if ordered.count(num) >= 1:
			p = ordered.index(num)
			ordered[p] = str(i[0:x])+space+'||     '+str(num)+'%'

	#Print the bitches
	print 'Best Average Scores for Multiplication\n**************************************\n\n'
	for i in ordered:
		print i
	print '\n\n'

def bestAverageScoreSubtraction():
	w = open('SCORE_BOARD')
	scores = w.readlines()
	w.close()

	w = open('USER_NAMES')
	users = w.readlines()
	w.close()
	users.pop(0)

	#This code isolates the user names, at the end users will contain the users 
	new = []
	for i in users:
		x=len(i)
		new.append(i[3:x-1])
	users = new

	#these pops get rid of some useless information in the text doc at the top.
	scores.pop(0)
	scores.pop(0)
	scores.pop(0)

	noUsers = len(users)

	tally=[] #Empty list to store averages

	#This does, for each user obtain their average score.
	for i in users:
		count = 0 # Keeps track of number of attempts made
		score = 0 # Keeps track of total number of averages collected.
		for j in scores:
			x = j.index(',') #find the end of our user name
			if (i == j[0:x] and j[60:] == 'Subtraction,\n'): # If the user name from SCORE_BOARD matches the username pulled from USER_NAMES and the subject matches...
				x = j[40:].index(',') #Grab the index number for a comma after the first 40 chars
				count += 1 # Up tick count because this is an attempt from our user
				score += float(j[40:x+40]) #add the percent to score 
		if count == 0: #to avoid no attempts made
			tally.append(str(i)+', '+'0')
		else:
			tally.append(str(i)+', '+str(score/count)) #place both username and their average into the tally list.

	top = [] 

	# Peel just the scores from tally
	for i in tally:
		x = i.index(',')
		top.append(float(i[x+1:]))

	ordered = []
	leng = len(top)

	#order our scores

	for i in range(leng):
		ordered.append(max(top))
		top.pop(top.index(max(top)))

	#take the top three scores
	ordered = ordered[0:3]

	#For each item in tally (Users with their averages) check to see if they're in the top three, if so, add their name (and a padding of spaces) to ordered (a list containing the top three scores)
	for i in tally:
		x = i.index(',')
		num = float(i[x+1:])
		space = ''
		for j in range(20-x):
			space += ' '

		if ordered.count(num) >= 1:
			p = ordered.index(num)
			ordered[p] = str(i[0:x])+space+'||     '+str(num)+'%'

	#Print the bitches
	print 'Best Average Scores for Subtraction\n***********************************\n\n'
	for i in ordered:
		print i
	print '\n\n'

def personalAverageScoreAddition(user):
	w = open('SCORE_BOARD')
	scores = w.readlines()
	w.close()
	leng = len(user)
	space = ''

	for i in range(20-leng):
		space += ' '

	scores.pop(0)
	scores.pop(0)
	scores.pop(0)

	count = 0
	totPercent = 0
	for i in scores:
		if i[0:leng] == user and i[60:] == 'Addition,\n':
			count += 1
			totPercent += float(i[40:((i[40:].index(','))+40)])

	print "Personal Average Score for Addition\n***********************************"
	print str(user) + space + '||       ' + str(totPercent/count)
	print '\n\n'

def personalAverageScoreSubtraction(user):
	w = open('SCORE_BOARD')
	scores = w.readlines()
	w.close()
	leng = len(user)
	space = ''

	for i in range(20-leng):
		space += ' '

	scores.pop(0)
	scores.pop(0)
	scores.pop(0)

	count = 0
	totPercent = 0
	for i in scores:
		if i[0:leng] == user and i[60:] == 'Subtraction,\n':
			count += 1
			totPercent += float(i[40:((i[40:].index(','))+40)])

	print "Personal Average Score for Subtraction\n**************************************"
	print str(user) + space + '||       ' + str(totPercent/count)
	print '\n\n'

def personalAverageScoreMultiplication(user):
	w = open('SCORE_BOARD')
	scores = w.readlines()
	w.close()
	leng = len(user)
	space = ''

	for i in range(20-leng):
		space += ' '

	scores.pop(0)
	scores.pop(0)
	scores.pop(0)

	count = 0
	totPercent = 0
	for i in scores:
		if i[0:leng] == user and i[60:] == 'Multiplication,\n':
			count += 1
			totPercent += float(i[40:((i[40:].index(','))+40)])

	print "Personal Average Score for Multiplication\n*****************************************"
	print str(user) + space + '||       ' + str(totPercent/count)
	print '\n\n'

def fastestTimeAddition():
	w = open('SCORE_BOARD')
	scores = w.readlines()
	w.close()

	w = open('USER_NAMES')
	users = w.readlines()
	w.close()
	users.pop(0)

	#This code isolates the user names, at the end users will contain the users 
	new = []
	for i in users:
		x=len(i)
		new.append(i[3:x-1])
	users = new

	#these pops get rid of some useless information in the text doc at the top.
	scores.pop(0)
	scores.pop(0)
	scores.pop(0)

	noUsers = len(users)

	tally = []

	for i in users:
		time = 0
		for j in scores:
			if i == j[:j.index(',')] and j[60:] == 'Addition,\n' and float(j[40:j[40:].index(',')+40]) >0:
				curTime = float(j[20:j[20:].index(',')+20])
				if time == 0:
					time = curTime
				elif time > curTime:
					time = curTime
		if time == 0:
			tally.append(str(i)+', '+'100')
		else:
			tally.append(str(i)+', '+str(time))
	top=[]

	for i in tally:
		x = i.index(',')
		top.append(float(i[x+1:]))

	ordered = []
	leng = len(top)
	#order our scores

	for i in range(leng):
		ordered.append(min(top))
		top.pop(top.index(min(top)))

	#take the top three scores
	ordered = ordered[0:3]

	#For each item in tally (Users with their averages) check to see if they're in the top three, if so, add their name (and a padding of spaces) to ordered (a list containing the top three scores)
	for i in tally:
		x = i.index(',')
		num = float(i[x+1:])
		space = ''
		for j in range(20-x):
			space += ' '
		if ordered.count(num) >= 1:
			p = ordered.index(num)
			ordered[p] = str(i[0:x])+space+'||     '+str(num)+' sec'


	print 'Fastest Completion times for Addition\n*************************************\n\n'
	for i in ordered:
		if not (i[27:30] == '100'):
			print i
	print '\n\n'

def fastestTimeSubtraction():
	w = open('SCORE_BOARD')
	scores = w.readlines()
	w.close()

	w = open('USER_NAMES')
	users = w.readlines()
	w.close()
	users.pop(0)

	#This code isolates the user names, at the end users will contain the users 
	new = []
	for i in users:
		x=len(i)
		new.append(i[3:x-1])
	users = new

	#these pops get rid of some useless information in the text doc at the top.
	scores.pop(0)
	scores.pop(0)
	scores.pop(0)

	noUsers = len(users)

	tally = []

	for i in users:
		time = 0
		for j in scores:
			if i == j[:j.index(',')] and j[60:] == 'Subtraction,\n' and float(j[40:j[40:].index(',')+40]) >0:
				curTime = float(j[20:j[20:].index(',')+20])
				if time == 0:
					time = curTime
				elif time > curTime:
					time = curTime
		if time == 0:
			tally.append(str(i)+', '+'100')
		else:
			tally.append(str(i)+', '+str(time))
	top=[]

	for i in tally:
		x = i.index(',')
		top.append(float(i[x+1:]))

	ordered = []
	leng = len(top)
	#order our scores

	for i in range(leng):
		ordered.append(min(top))
		top.pop(top.index(min(top)))

	#take the top three scores
	ordered = ordered[0:3]

	#For each item in tally (Users with their averages) check to see if they're in the top three, if so, add their name (and a padding of spaces) to ordered (a list containing the top three scores)
	for i in tally:
		x = i.index(',')
		num = float(i[x+1:])
		space = ''
		for j in range(20-x):
			space += ' '
		if ordered.count(num) >= 1:
			p = ordered.index(num)
			ordered[p] = str(i[0:x])+space+'||     '+str(num)+' sec'


	print 'Fastest Completion times for Subtraction\n****************************************\n\n'
	for i in ordered:
		if not (i[27:30] == '100'):
			print i
	print '\n\n'

def fastestTimeMultiplication():
	w = open('SCORE_BOARD')
	scores = w.readlines()
	w.close()

	w = open('USER_NAMES')
	users = w.readlines()
	w.close()
	users.pop(0)

	#This code isolates the user names, at the end users will contain the users 
	new = []
	for i in users:
		x=len(i)
		new.append(i[3:x-1])
	users = new

	#these pops get rid of some useless information in the text doc at the top.
	scores.pop(0)
	scores.pop(0)
	scores.pop(0)

	noUsers = len(users)

	tally = []

	for i in users:
		time = 0
		for j in scores:
			if i == j[:j.index(',')] and j[60:] == 'Multiplication,\n' and float(j[40:j[40:].index(',')+40]) >0:
				curTime = float(j[20:j[20:].index(',')+20])
				if time == 0:
					time = curTime
				elif time > curTime:
					time = curTime
		if time == 0:
			tally.append(str(i)+', '+'100')
		else:
			tally.append(str(i)+', '+str(time))
	top=[]

	for i in tally:
		x = i.index(',')
		top.append(float(i[x+1:]))

	ordered = []
	leng = len(top)
	#order our scores

	for i in range(leng):
		ordered.append(min(top))
		top.pop(top.index(min(top)))

	#take the top three scores
	ordered = ordered[0:3]

	#For each item in tally (Users with their averages) check to see if they're in the top three, if so, add their name (and a padding of spaces) to ordered (a list containing the top three scores)
	for i in tally:
		x = i.index(',')
		num = float(i[x+1:])
		space = ''
		for j in range(20-x):
			space += ' '
		if ordered.count(num) >= 1:
			p = ordered.index(num)
			ordered[p] = str(i[0:x])+space+'||     '+str(num)+' sec'


	print 'Fastest Completion times for Multiplication\n*******************************************\n\n'
	for i in ordered:
		if not (i[27:30] == '100'):
			print i

	print '\n\n'