ifName = 'log0.txt'

data = [x.rstrip() for x in open(ifName, 'r')]

f = len(data)

firstIt = True

lastTimeInSecs = 0
timeInterval = 0.6

for idx, line in enumerate(data):
	hour = int(line[11:13])
	minute = int(line[14:16])
	sec = int(line[17:19])
	mills = float(f'0.{line[20:26]}')
	timeInSecs = (hour*3600) + (minute*60) + sec + mills

	if firstIt:
		firstIt = False
		lastTimeInSecs = timeInSecs
		continue

	if timeInSecs > lastTimeInSecs + timeInterval:
		delta = timeInSecs - lastTimeInSecs
		print(data[idx-1][:26], data[idx][:26], '\n', int(delta / 0.5))
		# ok = int(delta / timeInterval)
		# print(ok)
		# for _ in range(int(delta / timeInterval)):
		# 	data.insert(idx, 'extra pixel')	

	lastTimeInSecs = timeInSecs







