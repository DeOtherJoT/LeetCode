def maxWidthOfVerticalArea(points: list[list[int]]) -> int:
	def sort_key(e):
		return e[0]
	
	points.sort(key=sort_key)
	print(points)
	widest_dist = 0
	for x in range(len(points) - 1):
		curr_dist = points[x + 1][0] - points[x][0]
		widest_dist = max(widest_dist, curr_dist)
	return widest_dist


points = [[8,7],[9,9],[7,4],[9,7]]

print(maxWidthOfVerticalArea(points))