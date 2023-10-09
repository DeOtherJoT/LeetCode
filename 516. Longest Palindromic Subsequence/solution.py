def longestPalindromeSubseq(s: str) -> int:
	grid = [[0 for _ in s] for _ in s]

	for i in range(len(s)):
		grid[i][i] = 1

	for i in range(1, len(s)):
		row = 0
		for col in range(i, len(s)):
			if (s[row] == s[col]):
				grid[row][col] = 2 + grid[row + 1][col - 1]
			else:
				grid[row][col] = max(grid[row][col - 1], grid[row + 1][col])
			row += 1

	return (grid[0][-1])

print(longestPalindromeSubseq("acbbbab"))