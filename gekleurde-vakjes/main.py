from solver import GRID_WIDTH, Solver, fieldType, statusTypes
import requests
import pygame

TEXTSPACING = 40

BLOCKS = 10
WIDTH = HEIGHT = GRID_WIDTH * BLOCKS
clock = pygame.time.Clock()
win = pygame.display.set_mode((WIDTH, HEIGHT))
FPS = 30
POSTTEXTMARGIN = 10

WIDTH = HEIGHT = GRID_WIDTH * BLOCKS

COLORS = {'BLACK': (0,0,0),
	'WHITE': (255,255,255),
	'RED':(255,0,0),
	'GREEN':(0,255,0),
	'BLUE':(0,0,255),
	'GREY': (10,10,10),
	'BROWN' : (102,34,0),
	'ELECTRIFIED': (255,255, 0),
	'COLD': (102,255,255),
	'HOT' : (255,65,0),
	'WET' : (141,255,141),
	'BACKGROUND' : (100,100,100),
	}
pygame.font.init()
font = pygame.font.SysFont('Arial', 30)
endPosScreen = font.render('Eind x: 0, y: 49', True, COLORS['BLACK'])
def drawOverlay(win, solver): 
	asd = lambda x : "True" if x else "False"
	for idx, s in enumerate(statusTypes):
		win.blit(font.render(F"{s} = {asd(solver.statuses[s])}", True, COLORS[s]), (0, idx*TEXTSPACING))

	posScreen = font.render(f"Positie x:{solver.cPos[0]}, y: {solver.cPos[1]}", True, COLORS['BLACK'])
	win.blit(posScreen, (WIDTH - posScreen.get_width() - POSTTEXTMARGIN, 0))
	win.blit(endPosScreen, (WIDTH - endPosScreen.get_width() - POSTTEXTMARGIN, posScreen.get_height() + POSTTEXTMARGIN))


def drawScreen(win, solver):
	win.fill(COLORS['BACKGROUND'])
	for y, row in enumerate(solver.grid):
		for x, cell in enumerate(row):
			if cell == 0:
				continue

			if cell == fieldType['PATH']: # Match: case fieldType['type'] werk niet! kut python
				c = COLORS['WHITE']
			elif cell == fieldType['MOUNTAIN']:
				c = COLORS['BLUE']
			elif cell == fieldType['WATER']:
				c = COLORS['WET']
			elif cell == fieldType ['FIRE']:
				c = COLORS['HOT']
			elif cell == fieldType['ELECTRIC']:
				c = COLORS['ELECTRIFIED']
			elif cell == fieldType['ICE']:
				c = COLORS['COLD']
			elif cell == fieldType['RUBBER']:
				c = COLORS['BROWN']
			else:
				c = COLORS['BLACK']
			pygame.draw.rect(win, c, (x*BLOCKS, y*BLOCKS, BLOCKS, BLOCKS))

	pygame.draw.rect(win, COLORS['RED'], (BLOCKS*solver.cPos[0], BLOCKS*solver.cPos[1], BLOCKS, BLOCKS))
	drawOverlay(win, solver)

if __name__ == "__main__":
	solver = Solver()
	solver.setSurrounding()
	running = True
	while running:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					running = False
				elif event.key in [pygame.K_UP, pygame.K_DOWN, pygame.K_RIGHT, pygame.K_LEFT]:
					solver.walk(event.key)
					solver.setSurrounding()

		drawScreen(win, solver)
		pygame.display.update()
		clock.tick(FPS)



