import re

f = open("input12.json", "r")
line = f.readline().rstrip()
total = 0
while line != "":
	number = re.findall(r'-?[0-9]+', line)
	for num in number:
		total += int(num)
	line = f.readline().rstrip()

print total


