from math import floor
from sudoku import Sudoku

def solveSudoku(inp, target, pprint = False):
	grid = [[0 for _ in range(9)] for _ in range(9)]

	for cord in inp:
		pos = cord[0]
		val = cord[1]

		y = floor(pos/9)
		x = pos%9
		grid[y][x] = val

	if pprint:
		for row in grid:
			print(row)
	
	solved = Sudoku(3, 3, board=grid).solve()
	result = solved.board[floor(target/9)][target%9]
	return result
		

if __name__ == "__main__":
	solutions = []
	for x in range(81):
		file = f"morseText/text{x}.txt"
		inp = []
		for x in open(file, 'r').read()[1:-1].split('),('):
			inp.append(tuple(int(n) for n in x.split(',') if n != '?'))

		target = inp.pop(-1)[0]
		# solutions.append((target, solveSudoku(inp, target)))
		solutions.append(solveSudoku(inp, target))

	print(solutions)