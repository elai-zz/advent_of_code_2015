def lookandsay(string):
	lastChar = ""
	numSeen = 0
	output = ""
	for char in string:
		if char == lastChar:
			numSeen += 1
		else:
			output += str(numSeen) 
			output += lastChar
			lastChar = char
			numSeen = 1
	output += str(numSeen) 
	output += lastChar

	return output[1:]


iteration = 0
string = "1113122113"
while (iteration < 40):
	string = lookandsay(string)
	iteration += 1

print len(string)

