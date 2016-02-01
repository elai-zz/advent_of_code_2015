houses = [0] * 1000001

def populateHouses():
	for elf in xrange(1, 1000001):
		for i in xrange(1, 1000001, elf):
			houses[i] += 10 * elf


def findFirstHouse():
	for i in range(len(houses)):
		if houses[i] >= 36000000:
			return i+1
				

populateHouses()
houses.pop(0)
houses.pop(0)
print findFirstHouse()
