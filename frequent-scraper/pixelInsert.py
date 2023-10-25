ifName = 'out.txt'

data = [x.rstrip() for x in open(ifName, 'r')]

f = len(data)

firstIt = True

newOut = open('correctRGB.txt', 'w')

lastTimeInSecs = 0

timeThreshold = 0.9
foo = 0.5

getRGB = lambda x : x[28:]
lastRGB = None

for idx, line in enumerate(data):
	hour = int(line[11:13])
	minute = int(line[14:16])
	sec = int(line[17:19])
	mills = float(f'0.{line[20:26]}')
	timeInSecs = (hour*3600) + (minute*60) + sec + mills

	if firstIt:
		firstIt = False
		lastTimeInSecs = timeInSecs
		lastRGB = getRGB(line)
		continue

	if timeInSecs > lastTimeInSecs + timeThreshold:
		delta = timeInSecs - lastTimeInSecs
		extraPixels = round(delta / foo) - 1

		for _ in range(extraPixels):
			newOut.write(lastRGB)
			newOut.write('\n')

	newOut.write(getRGB(line))
	newOut.write('\n')
	lastRGB = getRGB(line)
	lastTimeInSecs = timeInSecs

newOut.close();





