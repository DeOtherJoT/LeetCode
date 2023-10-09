#include <stdlib.h>
#include <string.h>
#include <stdio.h>

char	*mergeAlternately(char *word1, char *word2){
	char    *ret;
	int     num_char = strlen(word1) + strlen(word2);

	ret = malloc(sizeof(char) * (num_char + 1));
	for (int i = 0; i < num_char; i++){
		if (*word1)
			*ret++ = *word1++;
		if (*word2)
			*ret++ = *word2++;
	}
	*ret = '\0';
	return (ret - num_char);
}

int	main(void)
{
	char	*res = mergeAlternately("abcde", "opq");

	printf("Result: %s\n", res);

	free(res);
	return (0);
}