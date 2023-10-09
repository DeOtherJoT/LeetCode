# 516.  Longest Palindromic Subsequence

## Problem Description

Given a string  `s`, find  _the longest palindromic  **subsequence**'s length in_  `s`.

A  **subsequence**  is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements.

---
**Example 1:**

**Input:** s = "bbbab"

**Output:** 4

**Explanation:** One possible longest palindromic subsequence is "bbbb".

---
**Example 2:**

**Input:** s = "cbbd"

**Output:** 2

**Explanation:** One possible longest palindromic subsequence is "bb".

---
**Constraints:**

-   `1 <= s.length <= 1000`
-   `s`  consists only of lowercase English letters.

## Approach

This is a well-known Dynamic Programming Problem since it possesses the properties of a DPP, which are :
1. Optimal Substructure
2. Overlapping Subproblems

My solution makes use of a 2D array to keep track of the palindrome subsequences between two characters in the string. 

```
Pseudocode:

START
	Initialise 2D array, grid
	Fill in a digonal of 1s, from the top left to bottom right
	FOR i IN range(1, len(input))
		row = 0
		FOR col IN range(i, len(input))
			IF (input[row] == input[col])
				grid[row][col] = 2 + grid[row + 1][col - 1]
			ELSE
				grid[row][col] = max(grid[row][col - 1], grid[row + 1][col])
			INCREMENT row
	RETURN grid[0][-1]
END
```


## Solution Benchmark
![Python3 Solution](images/py_result.png  "Python3 Solution")