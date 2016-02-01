class Grid():
	def __init__(self):
		self.grid = []

	def parseLine(self, line):
		lineList = []
		for char in line:
			lineList.append(char)
		self.grid.append(lineList)

	def findOn(self):
		counter = 0
		for row in self.grid:
			for item in row:
				if item == "#":
					counter += 1
		return counter

	def takeStep(self):
		nextStep = []
		for row in range(len(self.grid)):
			nextStep.append([])
			for col in range(len(self.grid[row])):

				light = self.grid[row][col]
				neighborsOn = self.getOnNeighbors(row, col)

				if light == "#":
					if neighborsOn == 2 or neighborsOn == 3:
						nextStep[row].append("#")
					else:
						nextStep[row].append(".")

				else:
					if neighborsOn == 3:
						nextStep[row].append("#")
					else:
						nextStep[row].append(".")

		self.grid = nextStep

	def getOnNeighbors(self, r, c):
		neighbors = [(r-1, c-1), (r-1, c), (r-1, c+1), (r, c-1), (r, c+1), (r+1, c-1), (r+1, c), (r+1, c+1)]
		on = 0
		for neighbor in neighbors:
			if neighbor[0] > -1 and neighbor[0] < len(self.grid[0]):
				if neighbor[1] > -1 and neighbor[1] < len(self.grid[0]):
					nr = neighbor[0]
					nc = neighbor[1]
					if self.grid[nr][nc] == "#":
						on += 1

		return on

	def printGrid(self):
		for i in self.grid:
			print i
		print

if __name__ == "__main__":
	f = open("input18.txt", "r")
	grid = Grid()
	line = f.readline().rstrip()
	while line != "":
		grid.parseLine(line)
		line = f.readline().rstrip()

	for i in range(100):	
		grid.takeStep()
	print grid.findOn()

