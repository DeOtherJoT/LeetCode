# 1323. Maximum 69 Number

## Problem Description
You are given a positive integer `num` consisting only of digits `6` and `9`.

Return the maximum number you can get by changing at most one digit (`6` becomes `9`, and `9` becomes `6`).

---
**Example 1:**

**Input:** `num` = 9669

**Output:** 9969

**Explanation:**
- Changing the first digit results in `6669`.
- Changing the second digit results in `9969`.
- Changing the third digit results in `9699`.
- Changing the fourth digit results in `9666`.

The maximum number is `9969`.

---
**Example 2:**

**Input:** `num` = 9996

**Output:** 9999

---
**Example 3:**

**Input:** `num` = 9999

**Output:** 9999

---

**Constraints:**
- `1 <= num <= 104`
- `num` consists of only `6` and `9` digits.


## Approach

The number will be converted to a string and then traversed from left to right. The first `6` is then changed to a `9` which will result in the expected answer. If there are no `6`'s, then the number is already the largest it can be.

```
Pseudocode :

START
    CONVERT num to string
    FOR char IN string
        IF char == 6
            REPLACE char = 9
        BREAK
    CONVERT string to int
    RETURN int
END
```

### Solution Benchmark

![Python3 Solution](images/py_result.png "Python3 Solution")