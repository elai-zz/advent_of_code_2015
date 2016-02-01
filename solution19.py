inputString = "CRnSiRnCaPTiMgYCaPTiRnFArSiThFArCaSiThSiThPBCaCaSiRnSiRnTiTiMgArPBCaPMgYPTiRnFArFArCaSiRnBPMgArPRnCaPTiRnFArCaSiThCaCaFArPBCaCaPTiTiRnFArCaSiRnSiAlYSiThRnFArArCaSiRnBFArCaCaSiRnSiThCaCaCaFYCaPTiBCaSiThCaSiThPMgArSiRnCaPBFYCaCaFArCaCaCaCaSiThCaSiRnPRnFArPBSiThPRnFArSiRnMgArCaFYFArCaSiRnSiAlArTiTiTiTiTiTiTiRnPMgArPTiTiTiBSiRnSiAlArTiTiRnPMgArCaFYBPBPTiRnSiRnMgArSiThCaFArCaSiThFArPRnFArCaSiRnTiBSiThSiRnSiAlYCaFArPRnFArSiThCaFArCaCaSiThCaCaCaSiRnPRnCaFArFYPMgArCaPBCaPBSiRnFYPBCaFArCaSiAl"

inputString2 = "HOH"

seenSet = set()
dictionary = {}


def insertLineIntoDict(line):
	split = line.split(" ")
	key = split[0]
	value = split[2]

	if key in dictionary:
		dictionary[key] = dictionary[key] + [value]
	else:
		dictionary[key] = [value]



def makeReplacements(inputS):
	currIndex = 0
	while currIndex < len(inputS):
		possibleKey = inputS[currIndex]
		possibleKey2 = inputS[currIndex:2 + currIndex] #do some indexing check


		if possibleKey in dictionary:
			for replacement in dictionary[possibleKey]:
				stringBefore = inputS[0:currIndex]
				stringAfter = inputS[currIndex + 1 :]
				seenSet.add(stringBefore + replacement + stringAfter)
			currIndex += 1
		elif possibleKey2 in dictionary:
			for replacement in dictionary[possibleKey2]:
				stringBefore = inputS[0:currIndex]
				stringAfter = inputS[currIndex + 2 :]
				seenSet.add(stringBefore + replacement + stringAfter)
			currIndex += 2
		else:
			currIndex += 1
			

if __name__ == "__main__":
	f = open("input19.txt", "r")
	line = f.readline().rstrip()
	while line != "":
		insertLineIntoDict(line)
		line = f.readline().rstrip()

	makeReplacements(inputString)
	print len(seenSet)
