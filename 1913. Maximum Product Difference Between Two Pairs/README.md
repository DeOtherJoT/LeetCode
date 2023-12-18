# 1913. Maximum Product Difference Between Pairs

## Problem Description

The product difference between two pairs `(a, b)` and `(c, d)` is defined as `(a * b) - (c * d)`.

For example, the product difference between `(5, 6)` and `(2, 7)` is `(5 * 6) - (2 * 7) = 16`.
Given an integer array `nums`, choose four distinct indices `w`, `x`, `y`, and `z` such that the product difference between pairs `(nums[w], nums[x])` and `(nums[y], nums[z])` is maximized.

Return _the **maximum** such product difference_.

---

**Example 1:**

**Input:** nums = [5,6,2,7,4]

**Output:** 34

**Explanation:** We can choose indices 1 and 3 for the first pair (6, 7) and indices 2 and 4 for the second pair (2, 4).
The product difference is (6 _ 7) - (2 _ 4) = 34.

---

**Example 2:**

**Input:** nums = [4,2,5,9,7,4,8]

**Output:** 64

**Explanation:** We can choose indices 3 and 6 for the first pair (9, 8) and indices 1 and 5 for the second pair (2, 4).
The product difference is (9 _ 8) - (2 _ 4) = 64.

---

**Constraints:**

- `4 <= nums.length <= 104`
- `1 <= nums[i] <= 104`

## Approach

The two solutions here use different approaches.

The first one is to first sort the `nums` array, then getting the final answer from subtracting the product of the first two elements of `nums` from the product of the last two elements of `nums`. This is not a very optimised approach, as depending on the sorting algorithm you will use more resources/time than necessary. The props of this method is that its a no brainer, and simple and easy to understand.

```
Pseudocode:

START
	Sort nums array
	Return (product of last two elements) - (product of first two elements)
END
```

The next solution keeps track of four numbers (we can do this safely as the constraints guarantee at least 4 numbers in `nums`) using an array, and then iterate through the `nums` array and determine if that number belongs in one of the four spots.

```
Pseudocode:

START
	Init array res[MAX_INT, MAX_INT, MIN_INT, MIN_INT] corresponding as [smallest value, small value, large value, largest value]
	Iterate through number in nums
		IF number < res[0]
			Replace res[1] with res[0]
			Replace res[0] with number
		ELSE IF number < res[1]
			Replace res[1] with number
		IF number > res[3]
			Replace res[2] with res[3]
			Replace res[3] with number
		ELSE IF number > res[2]
			Replace res[2] with number
	Return (res[2] * res[3]) - (res[0] * res[1])
```

## Solution Benchmark

![C Solution](images/c_result.png "C solution")

![Python3 solution](images/py_result.png "Python3 solution")
