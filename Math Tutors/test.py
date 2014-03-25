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
			#num = float(i[40:comma])
			print comma
			lst.append(i[40:comma+40])

	print lst

getBestScore('Adam Carter')