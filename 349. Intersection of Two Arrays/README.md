# 349. Intersection of Two Arrays

## Problem Description

Given two integer arrays `nums1` and `nums2`, return an array of their intersection. Each element in the result **must be unique** and you may return the result **in any order**.

---

**Example 1:**

**Input:** nums1 = [1,2,2,1], nums2 = [2,2]

**Output:** [2]

---

**Example 2:**

**Input:** nums1 = [4,9,5], nums2 = [9,4,9,8,4]

**Output:** [9,4]

**Note:** [4,9] is also accepted.

---

**Constraints:**

- `1 <= nums1.length, nums2.length <= 1000`
- `0 <= nums1[i], nums2[i] <= 1000`

## Approach

For the Python solution, there is no need to reinvent the wheel. Just make the lists into sets, and then use the in-built `intersection` method to find the result. The result has to be casted back as a list just before returning it.

For the C solution, took a more hands-on approach. Not the best memory-wise, but I was not gonna do a whole hash table or dynamic linked list approach for this. Simply mark whether or not an element in `nums1` exists in a temporary array using it as the index, and then reference this temporary array when looking through nums2. If the number exists in both arrays, save it in the array to be returned. The return array does not have to contain the intersection numbers only, so this inefficient memory approach is possible.
