from morsePattern import morsePattern

def morseToText(inFile, outFile):
	open(outFile, 'w').write(''.join([morsePattern[x] for x in open(inFile, 'r').read().split(" ")]))


if __name__ == "__main__":
	for idx in range(81):
		morseToText(f"morse/morse_{idx}.txt", f"morseText/text{idx}.txt")

