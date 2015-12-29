allDeer = []
measuredTime = 2503

def parseReindeer(line):
	parsed = line.split(" ")
	name = parsed[0]
	speed = int(parsed[3])
	time = int(parsed[6])
	stop = int(parsed[-2])
	distances = getDistances(speed, time, stop)
	allDeer.append(distances)


def getDistances(speed, time, stop):
	distances = []
	actionTime = 0
	while len(distances) < measuredTime:
		distances += [speed] * time + [0] * stop

	print sum(distances[:measuredTime])
	return sum(distances[:measuredTime])

if __name__ == "__main__":
	f = open("input14.txt", "r")
	line = f.readline().rstrip()

	while line != "":
		parseReindeer(line)
		line = f.readline().rstrip()

	print max(allDeer)
