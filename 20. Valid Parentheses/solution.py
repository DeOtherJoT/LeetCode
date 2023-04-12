def	isValid(s: str) -> bool:

	def isPair(stack_c, str_c) -> bool:
		temp_val = ord(str_c) - ord(stack_c)
		if (temp_val == 1 or temp_val == 2):
			return (True)
		else:
			return (False)

	stack = []

	for char in s:
		if (char in '([{'):
			stack.append(char)
		else:
			if (len(stack) > 0 and isPair(stack[-1], char) == True):
				stack.pop()
			else:
				return (False)
	
	if (len(stack) != 0):
		return (False)
	else:
		return (True)

# Testing

test_cases = ["()", "(){}[]", "((){}[()])", "(", "([)]", "]"]

for i in test_cases:
	print("------------------")
	print("Test case	: " + i)
	print("Result		: " + str(isValid(i)))