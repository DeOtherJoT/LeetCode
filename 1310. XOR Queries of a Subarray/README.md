# 1310. XOR Queries of a Subarray

## Problem Description
You are given an array `arr` of positive integers. You are also given the array `queries` where `queries[i] = [first_i, last_i]`.

For each query `i` compute the **XOR** of elements from `arr[first_i]` to `arr[last_i]` (that is, `arr[first_i] XOR arr[first_i + 1] XOR ... XOR arr[last_i]`).

Return an array `answer` where `answer[i]` is the answer to the `ith` query.

---

**Example 1:**

**Input:** arr = [1,3,4,8], queries = [[0,1],[1,2],[0,3],[3,3]]  
**Output:** [2,7,14,8]  
**Explanation:**  
The binary representation of the elements in the array are:  
1 = 0001  
3 = 0011  
4 = 0100  
8 = 1000  
The XOR values for queries are:  
[0,1] = 1 xor 3 = 2   
[1,2] = 3 xor 4 = 7   
[0,3] = 1 xor 3 xor 4 xor 8 = 14  
[3,3] = 8

---

**Example 2:**

**Input:** arr = [4,8,2,10], queries = [[2,3],[1,3],[0,0],[0,3]]  
**Output:** [8,0,4,4]

---

**Constraints**
- `1 <= arr.length, queries.length <= 3 * 104`
- `1 <= arr[i] <= 109`
- `queries[i].length == 2`
- `0 <= first_i <= last_i < arr.length`

## Approach
I had to re-read the problem statement three times to understand what was asked. Here, I modified the real statement to reflect my understanding of it better. Anyways, when the question is understood, then it is not hard to think of a naive solution.

### Naive Approach
In this approach, it will be possible to just brute force it with two for loops. It gets the job done, however you will get TLE. Nonetheless, below is the pseudocode;
```
START
    Initialise empty answer array
    FOR query in queries
        XOR elements in arr between index query[0] and query[1], inclusive
        Append result to answer array
    RETURN answer array
END
```
As mentioned earlier, the naive approach gets Time Limit Exceeded. Hence, we need to get smart about this.

### Improved Approach
In order to optimise this solution, it is necessary to know the properties of a XOR instruction. Namely,
- A ⊕ (B ⊕ C) = (A ⊕ B) ⊕ C
- A ⊕ B = B ⊕ A
- A ⊕ A = 0

Once we know this, it then becomes possible to break down the equation of a XOR query of a subarray. Consider the following breakdown;
```
arr = [a, b, c, d, e]

c ⊕ d ⊕ e
= (a ⊕ a) ⊕ (b ⊕ b) ⊕ (c ⊕ d ⊕ e) 
= (a ⊕ b) ⊕ (a ⊕ b ⊕ c ⊕ d ⊕ e)
```
From above, we have broken down the XOR of the subarray [c, d, e] to the XOR of the subarrays [a, b] and [a, b, c, d, e].

Therefore, if we create a prefix_sum XOR subarray made up of the cumulative elements in the main array, it would then be able to swap out the values of the broken down equation to arrive to a final answer.
```
arr = [a, b, c, d, e]

prefix_sum = [
    a,
    a ⊕ b,
    a ⊕ b ⊕ c,
    a ⊕ b ⊕ c ⊕ d,
    a ⊕ b ⊕ c ⊕ d ⊕ e
]

query[2, 4] = c ⊕ d ⊕ e
            = (a ⊕ b) ⊕ (a ⊕ b ⊕ c ⊕ d ⊕ e)
            = prefix_sum[1] ⊕ prefix_sum[4]

query[0, 2] = a ⊕ b ⊕ c
            = prefix_sum[2]
```
And with that, we have arrived at the main idea of the optimised solution.
```
START
    Initialise prefix_sum array
    FOR element in arr
        Fill prefix_sum array with cumulative XOR of elements
    Initialise answer array
    FOR query in queries
        IF query[0] == 0
            Append the result of prefix_sum[last_i] to answer array
        ELSE
            XOR elements in prefix_sum array with index first_i - 1 and last_i
            Append result to answer array
    RETURN answer array
END
```

**Note**: With the above implementation, we need to be wary in the case of `first_i` being a 0. However, this is easy to circumvent, since if `first_i == 0`, then we are simply returning the results of XOR every element until `last_i`, which is just the element in `prefix_sum[last_i]`.

## Solution Benchmark
![Python3 Solution](images/py_result.png "Python3 Solution")