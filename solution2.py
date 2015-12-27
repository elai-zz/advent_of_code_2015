def parseFile():
	listOfDims = []
	f = open("input2.txt", "r")
	line = f.readline().rstrip()

	while line != "":
		listOfDims.append(map(int, line.split("x")))
		line = f.readline().rstrip()

	return listOfDims

def calculate(l, w, h):
	smallestSide = min (l*w, w*h, h*l)
	return 2*l*w + 2*w*h + 2*h*l + smallestSide

if __name__ == "__main__":
	listOfDimensions = parseFile()
	acc = 0
	for dim in listOfDimensions:
		acc += calculate(dim[0], dim[1], dim[2])
	print acc
