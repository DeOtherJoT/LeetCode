from typing import List

def maxProductDifference(nums: List[int]) -> int:
	nums.sort()
	temp = len(nums)
	return ((nums[temp - 1] * nums[temp - 2]) - (nums[0] * nums[1]))

print(maxProductDifference([5,6,2,7,4]))