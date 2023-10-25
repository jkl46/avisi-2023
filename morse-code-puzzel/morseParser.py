DATA_OFFSET = 44

zeroThreshold = 1000
seperatorThreshold = 3 # in seconds

def parseMorse(inFile, outFile):
	f = open(inFile, 'rb')

	f.seek(24)
	sampleRate = int.from_bytes(f.read(4), "little")
	getSample = lambda : int.from_bytes(f.read(2))
	getFP = lambda: f.tell()*2

	f.seek(0,2)
	EOFPosition = f.tell()
	f.seek(DATA_OFFSET)

	morse = ""
	lastMorse = 0
	while f.tell() < EOFPosition:
		sample = getSample()

		if sample != 0:
			s = getFP()

			if (s - lastMorse) / 48000 > seperatorThreshold:
				morse += " "

			while True:
				if sum([getSample() for _ in range(zeroThreshold)]) == 0:
					t = (getFP() - s) / sampleRate
					lastMorse = getFP()
					if t < 0.8:
						morse += "."
					else:
						morse += "-"
					break
	f.close()
	with open(outFile, 'w') as outF:
		outF.write(morse)

if __name__ == "__main__":
	for idx in range(81):
		parseMorse(f'soundfiles/wav/audio_{idx}.wav', f'morse/morse_{idx}.txt')
		print(idx)