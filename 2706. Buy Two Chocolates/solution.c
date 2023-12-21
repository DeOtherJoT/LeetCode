#include <stdio.h>

int	buyChoco(int *prices, int prices_size, int money)
{
	int	min1 = 100;
	int	min2 = 100;

	for (int i = 0; i < prices_size; i++)
	{
		if (prices[i] < min1)
		{
			min2 = min1;
			min1 = prices[i];
		}
		else if (prices[i] < min2)
			min2 = prices[i];
	}
	if ((min1 + min2) > money)
		return (money);
	else
		return (money - (min1 + min2));
}

int	main(void)
{
	int	prices[] = {2, 2, 1, 1};
	int	pricesSize = 4;
	int	money = 3;

	printf("%d\n", buyChoco(prices, pricesSize, money));
}