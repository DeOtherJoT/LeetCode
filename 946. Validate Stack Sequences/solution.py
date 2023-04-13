from typing import List

def validateStackSequences(pushed: List[int], popped: List[int]) -> bool:
	stack = []
	if (pushed == popped or pushed == popped[::-1]):
		return (True)

	for elem in pushed:
		stack.append(elem)
		while (len(stack) > 0 and stack[-1] == popped[0]):
			stack.pop()
			popped.pop(0)

	if (stack == popped[::-1]):
		return (True)
	else:
		return (False)

pushed = [1,2,3,4,5]
popped = [1,2,4,5,4]

print("Result : " + str(validateStackSequences(pushed, popped)))