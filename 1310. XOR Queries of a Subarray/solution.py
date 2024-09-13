# Naive approach - Just brute force it with two for loops. Problem is, Time Limit Exceeded.

# Next approach, we use the identity of a XOR function, that is;
#	x ^ y ^ x = y.

# Hence,
# if arr = [a, b, c, d, e]
#			0, 1, 2, 3, 4


# then
#	query[2, 4] = (c ^ d ^ e)
#				= (a ^ a) ^ (b ^ b) ^ (c ^ d ^ e)
#				= (a ^ b) ^ (a ^ b ^ c ^ d ^ e)

# Basically, create an pre-sum array such that
#	pre-sum = [
#		0,
#		a,
# 		a ^ b,
#		...
#		a ^ b ^ c ^ d ^ e
#]

# Then,
# query[2,4] == pre-sum[2] ^ pre-sum[5]

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