class Password():
	def __init__(self, pw):
		self.password = pw

	def getNextLetter(self, letter):
		if letter == "z":
			return "a"
		else: 
			return chr(ord(letter) + 1)

	def getBetterNextLetter(self, letter):
		if letter == "z":
			return "a"
		elif letter == "h":
			return "j"
		elif letter == "n":
			return "p"
		elif letter == "k":
			return "m"
		else: 
			return chr(ord(letter) + 1)

	def increment(self):
		passwordToList = list(self.password)
		currIndex = len(self.password) - 1
		needToAdd = True

		while needToAdd and currIndex > -1:
			
			passwordToList[currIndex] = self.getBetterNextLetter(passwordToList[currIndex])

			if passwordToList[currIndex] != "a":
				needToAdd = False
			else:
				needToAdd = True
				currIndex = currIndex - 1

		self.password = "".join(passwordToList)

	def countPairs(self):
		counter = 0
		pairsSeen = 0

		while counter < len(self.password) - 1:
			if self.password[counter] == self.password[counter+1]:
				pairsSeen += 1
				counter += 2
			else:
				counter += 1

		return pairsSeen > 1

	def findContinuous(self):
		continuousCount = 0
		counter = 0

		while counter < len(self.password) - 2:
			currLetter = self.password[counter]
			nextLetter = self.password[counter + 1]
			nextNextLetter = self.password[counter + 2]
			if self.getNextLetter(currLetter) == nextLetter and nextNextLetter == self.getNextLetter(nextLetter):
				continuousCount += 1
			counter += 1

		return continuousCount > 0

	def getNextValid(self):
		valid = False
		while not valid:
			self.increment()
			if self.countPairs() and self.findContinuous():
				valid = True
		

if __name__ == "__main__":
	password = Password("hxbxwxba")
	password.getNextValid()
	print password.password