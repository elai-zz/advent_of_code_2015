aunts = {}
possibleAunts = set()
info = {
	"children": 3,
	"cats": 7,
	"samoyeds": 2,
	"pomeranians": 3,
	"akitas": 0,
	"vizslas": 0,
	"goldfish": 5,
	"trees": 3,
	"cars": 2,
	"perfumes": 1
}

def insertIntoAunts(line, i):
	auntDictionary = {}
	split = line.split(" ")

	firstAttr = split[2][:-1]
	firstCount = int(split[3][:-1])

	secondAttr = split[4][:-1]
	secondCount = int(split[5][:-1])

	thirdAttr = split[6][:-1]
	thirdCount = int(split[7])

	auntDictionary[firstAttr] = firstCount
	auntDictionary[secondAttr] = secondCount
	auntDictionary[thirdAttr] = thirdCount

	aunts[i] = auntDictionary
	possibleAunts.add(i)

def findMatch(possibleAunts):
	while len(possibleAunts) > 1:
		auntsToRemove = set()
		for auntNumber in possibleAunts:
			if not isPossibleMatch(auntNumber):
				auntsToRemove.add(auntNumber)
		possibleAunts = possibleAunts - auntsToRemove
	return possibleAunts.pop()

def isPossibleMatch(auntNumber):
	auntInfo = aunts[auntNumber]
	for k, v in info.iteritems():
		if k in auntInfo and auntInfo[k] != v:
			return False

	return True


if __name__ == "__main__":
	f = open("input16.txt", "r")
	line = f.readline().rstrip()
	i = 1
	while line != "":
		insertIntoAunts(line, i)
		i += 1
		line = f.readline().rstrip()
	print findMatch(possibleAunts)
