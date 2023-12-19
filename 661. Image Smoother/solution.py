def imageSmoother(img: list[list[int]]) -> list[list[int]]:
	col_len = len(img[0])
	row_len = len(img)
	result = [[0] * col_len for _ in range(row_len)]
	# print(f"columns: {col_len}\nrows: {row_len}")
	for x in range(row_len):
		for y in range(col_len):
			total = 0
			count = 0

			for i in range(max(0, x - 1), min(row_len, x + 2)):
				for j in range(max(0, y - 1), min(col_len, y + 2)):
					total += img[i][j]
					count += 1
			
			result[x][y] = total // count
	
	return (result)


grid = [
	[100, 200, 100],
	[200, 50, 200],
	[100, 200, 100]
]

print(imageSmoother(grid))