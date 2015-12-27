import itertools

class Map():
	def __init__ (self):
		self.map = {}
		self.cities = set()
		self.citiesList = []
		self.distances = []

	def insertIntoMap(self, string):
		split = string.split(" ")
		origin = split[0]
		dest = split[2]
		dist = split[-1]
		self.map[(origin, dest)] = int(dist)
		self.map[(dest, origin)] = int(dist)
		self.cities.add(dest)
		self.cities.add(origin)

	def convertSetToList(self):
		self.citiesList = list(self.cities)

	def getShortest(self):
		shortest = 50000
		perms = list(itertools.permutations(self.citiesList))

		for perm in perms:
			dist = self.getDistance(perm)
			if dist == False:
				self.distances.append(50000)
			else:
				self.distances.append(dist)
		return min(self.distances)

	def getDistance(self, aList):
		index = 0
		dist = 0
		while index < len(aList) - 1:
			origin = aList[index]
			destination = aList[index+1]
			if (origin,destination) in self.map:
				dist += self.map[(origin,destination)]
				index += 1
			else:
				print (origin, destination)
				return False
		return dist

if __name__ == "__main__":
	f = open("input9.txt", "r")
	line = f.readline().rstrip()
	aMap = Map()

	while line != "":
		aMap.insertIntoMap(line)
		line = f.readline().rstrip()

	aMap.convertSetToList()
	print aMap.getShortest()

