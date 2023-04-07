from typing import List

class Solution:
	def numEnclaves(self, grid: List[List[int]]) -> int:
		def propogate(x, y):
			if ((x < 0 or x > row_len - 1) or
				(y < 0 or y > col_len - 1) or
				grid[x][y] == 0):
				return
			grid[x][y] = 0
			propogate(x - 1, y)
			propogate(x + 1, y)
			propogate(x, y + 1)
			propogate(x, y - 1)

		row_len = len(grid)
		col_len = len(grid[0])

		for i in range(row_len):
			for j in range(col_len):
				if ((i == 0 or j == 0 or i == (row_len - 1) or j == (col_len - 1)) and grid[i][j] == 1):
					propogate(i, j)

		return sum(sum(row) for row in grid)