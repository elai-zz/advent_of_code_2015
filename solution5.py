import re

def parseFile():
	listOfStrings = []
	f = open("input5.txt", "r")
	line = f.readline().rstrip()

	while line != "":
		listOfStrings.append(line)
		line = f.readline().rstrip()

	return listOfStrings

def isNice(input):

	if len(re.findall('[aeiou]', input)) < 3:
		return False
		
	# TODO: sdkjfhsdkfhskjdfhsdf BLAHHH
	if re.findall('aa|bb|cc|dd|ee|ff|gg|hh|ii|jj|kk|ll|mm|nn|oo|pp|qq|rr|ss|tt|uu|vv|ww|xx|yy|zz', input) == []:
	 	return False
	if re.findall('ab|cd|pq|xy', input) != []:
		return False

	return True

if __name__ == "__main__":
	nice = 0
	listOfStrings = parseFile()
	for string in listOfStrings:
		if isNice(string):
			nice += 1
	print nice