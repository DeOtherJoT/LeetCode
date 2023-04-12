# 71. Simplify Path

## Problem Description
Given a string  `path`, which is an  **absolute path**  (starting with a slash  `'/'`) to a file or directory in a Unix-style file system, convert it to the simplified  **canonical path**.

In a Unix-style file system, a period  `'.'`  refers to the current directory, a double period  `'..'`  refers to the directory up a level, and any multiple consecutive slashes (i.e.  `'//'`) are treated as a single slash  `'/'`. For this problem, any other format of periods such as  `'...'`  are treated as file/directory names.

The  **canonical path**  should have the following format:

-   The path starts with a single slash  `'/'`.
-   Any two directories are separated by a single slash  `'/'`.
-   The path does not end with a trailing  `'/'`.
-   The path only contains the directories on the path from the root directory to the target file or directory (i.e., no period  `'.'`  or double period  `'..'`)

Return  _the simplified  **canonical path**_.

---
**Example 1:**

**Input:** path = "/home/"
**Output:** "/home"
**Explanation:** Note that there is no trailing slash after the last directory name.

---
**Example 2:**

**Input:** path = "/../"
**Output:** "/"
**Explanation:** Going one level up from the root directory is a no-op, as the root level is the highest level you can go.

---
**Example 3:**

**Input:** path = "/home//foo/"
**Output:** "/home/foo"
**Explanation:** In the canonical path, multiple consecutive slashes are replaced by a single one.

---
**Constraints:**

-   `1 <= path.length <= 3000`
-   `path`  consists of English letters, digits, period  `'.'`, slash  `'/'`  or  `'_'`.
-   `path`  is a valid absolute Unix path.

## Approach
A stack will be in use here, storing the directories as they are traversed. A few things must be handled here :

1.  A `//` will be changed to `/`
2.  A `/..` pops the last item in the stack, if the stack is not empty
3.  A `/.` changes nothing

```
Pseudocode :

START
	Split input with '/' as the delimiter (handles 1)
	Initialise empty stack
	FOR token IN split input
		IF token is .. AND stack is not empty
			stack.pop() {handles 2.}
		ELSE IF token is .
			continue {handles 3.}
		ELSE
			stack.append(token)
	RETURN joined stack, seperated with '/'
END
```

## Solution Benchmark
![Python3 Solution](images/py_result.png "Python3 Solution")