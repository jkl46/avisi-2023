import pygame
import requests
import json

GRID_WIDTH = GRID_HEIGHT = 100

url = "https://cc-gekleurde-vakjes-4xdpz6dd6q-ez.a.run.app/api"

fieldType = {'UNKNOWN': 0, 'PATH':1, 'MOUNTAIN':2, 'FINISH': 3, 'ELECTRIC' : 4, 'WATER' : 5, 'FIRE' : 6, 'ICE' : 7, 'RUBBER': 8} #kut python heb geen enums
statusTypes = ['ELECTRIFIED', 'COLD', 'HOT', 'WET']
startPos = (25, 49)
endPos = (0, 49)
class Solver:
	def __init__(self):
		self.finished = False
		self.grid = [[0 for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]
		self.path = [startPos]
		self.cPos = startPos
		self.statuses = { d: False for d in statusTypes}

		self.grid[self.cPos[1]][self.cPos[0]] = fieldType['PATH']
		self.grid[endPos[1]][endPos[0]] = fieldType['FINISH']

	def setSurrounding(self):
		x = self.cPos[0]
		y = self.cPos[1]
		d = "UP"
		for d in ["UP", "DOWN", "LEFT", "RIGHT"]:
			res = requests.get(f"{url}/look?currentX={x}&currentY={y}&direction={d}")
			if (res.status_code == 400):
				continue

			data = json.loads(res.text)
			try:
				c = fieldType[data['type']]
				if c != 1 and c != 2:
					print(f'FOUND {data["type"]} AT ({data["x"]},{data["y"]})')
			except Exception:
				print(f"FOUND {data['type']} at ({data['x']},{data['y']})")
				c = fieldType['UNKNOWN']

			self.grid[data['y']][data['x']] = c

	def walk(self, key): # Walk and update statuses, (walk resonse text)
		newPos = ()
		match key:
			case pygame.K_UP:
				newPos = (self.cPos[0], self.cPos[1]+1)
			case pygame.K_DOWN:
				newPos = (self.cPos[0], self.cPos[1]-1)
			case pygame.K_LEFT:
				newPos = (self.cPos[0]-1, self.cPos[1])
			case pygame.K_RIGHT:
				newPos = (self.cPos[0]+1, self.cPos[1])

		payload = '['
		for p in self.path:
			payload += '{"x":%d, "y":%d},' % (p[0],p[1])
		payload += '{"x":%d, "y":%d}' % (newPos[0],newPos[1])
		payload += ']'

		r = requests.post(f"{url}/walk", json = json.loads(payload))

		if r.status_code != 200:
			print("Unable to walk in direction, retry!")
			print(r.text)
		else:
			print("successfully walked!")
			foo = json.loads(r.text)
			self.cPos = newPos
			self.path.append(newPos)

			for s in ['ELECTRIFIED', 'COLD', 'HOT', 'WET']: # update statuses
				if foo[s] != self.statuses[s]:
					self.statuses[s] = foo[s]



if __name__ == "__main__": 
	s = Solver()
	s.setSurrounding()
