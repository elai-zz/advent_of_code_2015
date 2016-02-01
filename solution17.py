listOfTubs = [43, 3, 4, 10, 21, 44, 4, 6, 47, 41, 34, 17, 17, 44, 36, 31, 46, 9, 27, 38]
#listOfTubs = [20, 15, 10, 5, 5]

def makeTotal(tubs, weight):

	if weight == 0:
		return 1
	elif tubs == []:
		return 0
	elif tubs[0] > weight:
		return makeTotal(tubs[1:], weight)
	else:
		useIt = makeTotal(tubs[1:], weight - tubs[0])
		loseIt = makeTotal(tubs[1:], weight)
		return useIt + loseIt


print makeTotal(listOfTubs, 150)
