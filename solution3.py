class SantaClaus():
	def __init__(self):
		self.x = 0
		self.y = 0
		self.visited = {(0,0):1}

	def moveUp(self):
		self.y += 1
		self.addToVisited()

	def moveDown(self):
		self.y -= 1
		self.addToVisited()

	def moveLeft(self):
		self.x -= 1
		self.addToVisited()

	def moveRight(self):
		self.x += 1
		self.addToVisited()

	def addToVisited(self):
		if (self.x, self.y) in self.visited:
			self.visited[(self.x, self.y)] += 1
		else:
			self.visited[(self.x, self.y)] = 1

	def readInstructions(self, instr):
		for dir in instr:
			if dir == "^":
				self.moveUp()
			elif dir == ">":
				self.moveRight()
			elif dir == "<":
				self.moveLeft()
			else:
				self.moveDown()

	def houseVisited(self):
		return len(self.visited)


f = open("input3.txt", "r")
instructions = f.readline().rstrip()

santa = SantaClaus()
santa.readInstructions(instructions)
print santa.houseVisited()
