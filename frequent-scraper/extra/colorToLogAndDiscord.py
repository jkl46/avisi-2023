import requests
import time
from discordwebhook import Discord

timeStart = time.time()
logTimeInterval = 100

index = 0
f = open(f'log{index}.txt', 'w')
if __name__ == "__main__":
	url = "https://cc-frequent-scraping-4xdpz6dd6q-ez.a.run.app/"
	botUrl = 'https://discord.com/api/webhooks/1164637448513536072/3gLaVjPLqTuelLhb1z6bDv0GXz6lb6I-UMmITi_PBXkYSMAP_cNFufL8F_LBNv6XZkHB'

	discord = Discord(url=botUrl)

	last_body = ''
	a = True

	while a:
		r = requests.get(url)	
		body = r.text.split('\n')[4].strip()[18:]

		if body != last_body:
			last_body = body
			o = tuple(map(int, body[4:-2].split(',')))
			f.write(str(o)[1:-1])
			f.write('\n')
			discord.post(content=f"setblock {o[0]} {o[1]} {o[2]} minecraft:redstone_lamp")

		if time.time() > timeStart + logTimeInterval:
			timeStart = time.time()
			f.close()
			index += 1
			f = open(f'log{index}.txt', 'w')
