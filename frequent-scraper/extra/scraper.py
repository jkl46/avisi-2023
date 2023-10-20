import requests
import time
import datetime
import os

logDir = './logs/'
if not os.path.exists(logDir):
    os.makedirs(logDir)

timeStart = time.time()
logTimeInterval = 5

index = 0
f = open(f'logs\\log{index}.txt', 'w')
if __name__ == "__main__":
	url = "https://cc-frequent-scraping-4xdpz6dd6q-ez.a.run.app/"

	last_body = ''
	a = True

	while a:
		r = requests.get(url)	
		body = r.text.split('\n')[4].strip()[18:]

		if body != last_body:
			last_body = body
			o = tuple(map(int, body[4:-2].split(',')))
			outString = str(datetime.datetime.now())
			outString += '; '
			outString += str(o)[1:-1]
			outString += '\n'
			f.write(outString)

		if time.time() > timeStart + logTimeInterval:
			timeStart = time.time()
			f.close()
			index += 1
			f = open(f'./logs/log{index}.txt', 'w')
