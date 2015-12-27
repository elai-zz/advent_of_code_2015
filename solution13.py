if __name__ == "__main__":
	f = open("input9.txt", "r")
	line = f.readline().rstrip()
	aMap = Map()

	while line != "":
		aMap.insertIntoMap(line)
		line = f.readline().rstrip()

	aMap.convertSetToList()
	print aMap.getShortest()