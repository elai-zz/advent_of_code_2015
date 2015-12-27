import re
hexAlpha = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "a", "b", "c", "d", "e", "f"]

def escape(string):
	numEsc = 0
	counter = 0
	while counter < len(string):
		char = string[counter]
		if char == "\\":
			if string[counter+1] == "\"" or string[counter+1] == "\\":
				numEsc += 1
				counter += 2
			else:
				counter += 1
		else:
			counter += 1
	return numEsc

def findHex(string):
	numHex = 0
	counter = 0
	while counter < len(string):
		char = string[counter]
		if char == "\\":
			if string[counter+1] == "x":
				if string[counter+2] in hexAlpha and string[counter+3] in hexAlpha:
					numHex += 1
		counter += 1

	return numHex

if __name__ == "__main__":
	naturalLength = []
	actualChar = []

	f = open("input8.txt", "r")
	line = f.readline().rstrip()

	while line != "":

		naturalLength.append(len(line))
		actualChar.append(len(line) - escape(line) - 3*(findHex(line)) - 2)
		line = f.readline().rstrip()

	print sum(naturalLength)
	print sum(actualChar)