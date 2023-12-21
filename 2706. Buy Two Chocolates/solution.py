def buyChoco(prices: list[int], money: int) -> int:
	prices.sort()
	if (prices[0] + prices[1]) > money:
		return (money)
	else:
		return (money - (prices[0] + prices[1]))

print(buyChoco([2,2,1,1], 3))