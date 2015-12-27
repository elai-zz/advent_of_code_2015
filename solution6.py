import re

class ChristmasLights():
	def __init__(self):
		self.lightGrid = {}
		for row in range(0, 1000):
			for col in range(0, 1000):
				self.lightGrid[(row, col)] = 0

	def switchOn(self, x, y):
		self.lightGrid[(x,y)] = 1

	def switchOff(self, x, y):
		self.lightGrid[(x,y)] = 0

	def toggle(self, x, y):
		if self.lightGrid[(x,y)] == 0:
			self.lightGrid[(x,y)] = 1
		else:
			self.lightGrid[(x,y)] = 0

	def action(self, function, pair0, pair1):
		x1 = pair0[0]
		y1 = pair0[1]

		x2 = pair1[0]
		y2 = pair1[1]

		for row in (range(x1, x2+1) ):
			for col in (range(y1, y2+1) ):
				function(row, col)

	def countOn(self):
		number = 0
		for k, v in self.lightGrid.iteritems():
			if v == 1:
				number += 1
		return number

def extractPairs(input):
	temp = input.split(" ")

	if temp[0] == "toggle":
		action = "toggle"
	elif temp[1] == "on":
		action = "on"
	else:
		action = "off"

	pair1 = map(int, temp[-3].split(','))
	pair2 = map(int, temp[-1].split(','))
	return (action, [pair1, pair2])

if __name__ == "__main__":
	f = open("input6.txt", "r")
	christmasLights = ChristmasLights()
	line = f.readline().rstrip()
	while line != "":
		(action, pairs) = extractPairs(line)
		if action == "toggle":
			christmasLights.action(christmasLights.toggle, pairs[0], pairs[1])
		elif action == "on":
			christmasLights.action(christmasLights.switchOn, pairs[0], pairs[1])
		else:
			christmasLights.action(christmasLights.switchOff, pairs[0], pairs[1])
		line = f.readline().rstrip()

	print christmasLights.countOn()