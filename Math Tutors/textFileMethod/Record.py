""" Getting your best results and an average score"""

def getAverageTime(x):
	w = open("SCORE_BOARD")
	s = w.readlines()
	w.close()
	leng = len(x)
	lst = []
	counter = 0
	for i in s:
		if i.count(x) == 1:
			tlst = i[20:]
			comma = tlst.index(',')
			num = float(i[20:comma+20])
			lst.append(num)

	print sum(lst)/len(lst)

def getAverageScore(x):
	w = open("SCORE_BOARD")
	s = w.readlines()
	w.close()
	leng = len(x)
	lst = []
	counter = 0
	for i in s:
		if i.count(x) == 1:
			tlst = i[40:]
			comma = tlst.index(',')
			num = float(i[40:comma+40])
			lst.append(num)

	print sum(lst)/len(lst)

def getBestScore(x):
	w = open("SCORE_BOARD")
	s = w.readlines()
	w.close()
	leng = len(x)
	lst = []
	counter = 0
	for i in s:
		if i.count(x) == 1:
			tlst = i[40:]
			comma = tlst.index(',')
			num = float(i[40:comma+40])
			lst.append(num)

	print max(lst)

def getLowestTime(x):
	w = open("SCORE_BOARD")
	s = w.readlines()
	w.close()
	leng = len(x)
	lst = []
	counter = 0
	for i in s:
		if i.count(x) == 1:
			tlst = i[20:]
			comma = tlst.index(',')
			num = float(i[20:comma+20])
			lst.append(num)

	print min(lst)