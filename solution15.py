import itertools
from operator import mul

ingredients = {}
iList = []
total = 0

def parseIngredients(l):
	parsed = l.split(" ")
	name = parsed[0][:-1]
	capacity = int(parsed[2][:-1])
	durability = int(parsed[4][:-1])
	flavor = int(parsed[6][:-1])
	texture = int(parsed[8][:-1])

	ingredients[name] = [capacity, durability, flavor, texture]
	iList.append(name)

def getHighest(numberOfDividers):
	highest = 0
	dividers = list(itertools.combinations(range(0, total), numberOfDividers))
	for divider in dividers:
		score = getScore(divider)
		if score > highest:
			highest = score

	return highest

def getScore(divider):
	tuples = []
	lastIndex = 0
	stuff = [0, 0, 0, 0]

	for index in divider:
	 	tuples.append((lastIndex, index))
	 	lastIndex = index

	tuples.append((lastIndex, total))

	for i in range(len(tuples)) :
		tu = tuples[i]
		units = tu[1] - tu[0] #number of stuff
		currIngredient = iList[i]

		stuff[0] += units * ingredients[currIngredient][0]
		stuff[1] += units * ingredients[currIngredient][1]
		stuff[2] += units * ingredients[currIngredient][2]
		stuff[3] += units * ingredients[currIngredient][3]

	for i in range(len(stuff)):
		if stuff[i] < 0:
			stuff[i] = 0

	return reduce(mul, stuff, 1)

if __name__ == "__main__":
	f = open("input15.txt", "r")
	line = f.readline().rstrip()
	total = 100
	while line != "":
		parseIngredients(line)
		line = f.readline().rstrip()

	print getHighest(3)

