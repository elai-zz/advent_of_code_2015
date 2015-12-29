import itertools

setOfDistances = {}
peopleSet = set()
people = []

def insertIntoSet(line):
	parsed = line.split(" ")
	origin = parsed[0]
	destin = parsed[-1]
	sign = parsed[2]
	unit = parsed[3]

	if sign == "lose":
		setOfDistances[(origin, destin[:-1])] = -1 * int(unit)
	else:
		setOfDistances[(origin, destin[:-1])] = int(unit)

	peopleSet.add(origin)
	peopleSet.add(destin[:-1])

def getHappiest():
	people = list(peopleSet)
	perms = list(itertools.permutations(people))
	happiest = 0
	for perm in perms:
		dist = findDist(perm)
		if dist > happiest:
			happiest = dist
	return happiest

def findDist(permutation):

	acc = 0
	people = list(peopleSet)
	numPeeps = len(people)
	for i in range(0, numPeeps-1):
		origin = permutation[i]
		dest = permutation[i+1]
		acc += setOfDistances[(origin, dest)]
		acc += setOfDistances[(dest, origin)]

	acc += setOfDistances[(permutation[0], permutation[-1])]
	acc += setOfDistances[(permutation[-1], permutation[0])]

	return acc

if __name__ == "__main__":
	f = open("input13.txt", "r")
	line = f.readline().rstrip()

	while line != "":
		insertIntoSet(line)
		line = f.readline().rstrip()

	print getHappiest()

