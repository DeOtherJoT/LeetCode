def mergeAlternately(word1: str, word2: str) -> str:
	ret = ""
	i = 0

	for x in range(min(len(word1), len(word2))):
		ret += word1[x] + word2[x]
		i += 1
	
	ret += word1[i:] + word2[i:]
	return (ret)

str1 = "abc"
str2 = "opqrs"

print(mergeAlternately(str1, str2))