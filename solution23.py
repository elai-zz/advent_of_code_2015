instructions = []

def run():
	a = 0
	b = 0
	i = 0
	while i < len(instructions):
		instruction = instructions[i]
		verb = instruction[0]
		register = instruction[1]
		other = None
		print i
		if len(instruction) > 2:
			other = instruction[2]

		if verb == "inc":
			if register == "a":
				a +=1
			else:
				b += 1
		elif verb == "tpl":
			if register == "a":
				a *= 3
			else:
				b *= 3
		elif verb == "hlf":
			if register == "a":
				a = a/2
			else:
				b = b/2

		elif verb == "jmp":
			target = int(register)
			if not checkOK(i, target):
				return b
			else:
				i = i + target
				continue

		elif verb == "jie":
			if register == "a," and a%2 == 0:
				target = int(other[1:])
				if checkOK(i, target):
					i = i + target
					continue
				else:
					return b

		else:
			if register == "a," and a == 1:
				target = int(other[1:])
				if checkOK(i, target):
					i = i + target 
					continue
				else:
					return b
		i += 1
	print b


def checkOK(i, target):
	return not ((i + target > len(instructions)) or (i + target < 0))

if __name__ == "__main__":
	f = open("input23.txt", "r")
	line = f.readline().rstrip()
	while line != "":
		split = line.split(" ")
		instructions.append(split)
		line = f.readline().rstrip()

	run()

