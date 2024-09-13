def	xorQueries(arr: list[int], queries: list[list[int]]) -> list[int]:
	# initialise pre-sum array
	pre_sum = [0]
	base = 0
	for x in arr:
		base = base ^ x
		pre_sum.append(base)
	# print(pre_sum)
	
	# go through queries, and form answer.
	ans = []
	for q in queries:
		ans.append(pre_sum[q[0]] ^ pre_sum[q[1] + 1])
	return ans

ans = xorQueries([1, 3, 4 ,8], [[0,1],[1,2],[0,3],[3,3]])

print(ans)