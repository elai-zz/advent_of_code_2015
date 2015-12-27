import re

class Instructions():
	def __init__(self):
		self.variables = {}
		self.memoization = {}

	def insertInstruction(self, instr):
		temp = instr.split("->")
		if temp[0].rstrip().isdigit():
			self.variables[temp[1].lstrip()] = int(temp[0])
			self.memoization[temp[1].lstrip()] = int(temp[0])
		else:
			self.variables[temp[1].lstrip()] = temp[0].rstrip()

	def execute(self):
		while len(self.memoization) < len(self.variables):
			print self.memoization
			for value, instruction in self.variables.iteritems():
				if not value in self.memoization:
					if isinstance(instruction, int):
						self.memoization[value] = int(instruction)
					elif self.isInstruction(instruction):
						if self.canEvaluate(instruction):
							self.memoization[value] = self.evaluate(instruction)
						else:
							print instruction

	def isInstruction(self, instruction):
		action = re.findall("OR|AND|NOT|RSHIFT|LSHIFT", instruction)
		if action == []:
			if instruction.isdigit():
				return False
			else:
				return True
		else:
			return True

	def canEvaluate(self, instruction):
		parsed = instruction.split(" ")
		if len(parsed) == 1 and parsed[0] in self.memoization:
			return True
		elif len(parsed) == 2 and parsed[1] in self.memoization:
			return True
		elif len(parsed) == 3:
			if parsed[0] in self.memoization and parsed[2] in self.memoization:
				return True
			elif parsed[0] in self.memoization and parsed[2].isdigit():
				return True
			elif parsed[2] in self.memoization and parsed[0].isdigit():
				return True
		else:
			return False

	def evaluate(self, instruction):
		parsed = instruction.split(" ")
		if len(parsed) == 1:
			return self.memoization[parsed[0]]

		elif len(parsed) == 2:
			return 65535 - int(self.memoization[parsed[1]])

		else:
			lhs = self.getValue(parsed[0])
			rhs = self.getValue(parsed[2])

			if parsed[1] == "RSHIFT":
				return lhs >> rhs
			elif parsed[1] == "LSHIFT":
				return lhs << rhs
			elif parsed[1] == "OR":
				return lhs | rhs
			else:
				return lhs & rhs

	def getValue(self, value):
		if value.isdigit():
			return int(value)
		else:
			return self.memoization[value]

if __name__ == "__main__":
	f = open("input7.txt", "r")
	instructions = Instructions()
	line = f.readline().rstrip()

	while line != "":
		instructions.insertInstruction(line)
		line = f.readline().rstrip()

	instructions.execute()
	print instructions.memoization['a']
