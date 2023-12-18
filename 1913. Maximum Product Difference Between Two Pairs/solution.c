#include <stdio.h>
#include <limits.h>

int maxProductDifference(int* nums, int numsSize) {
	int	res[] = {INT_MAX, INT_MAX, INT_MIN, INT_MIN};

	for (int i = 0; i < numsSize; i++) {
		if (nums[i] < res[0]) {
			res[1] = res[0];
			res[0] = nums[i];
		}
		else if (nums[i] < res[1]) {
			res[1] = nums[i];
		}

		if (nums[i] > res[3]) {
			res[2] = res[3];
			res[3] = nums[i];
		}
		else if (nums[i] > res[2]) {
			res[2] = nums[i];
		}
	}

	return ((res[2] * res[3]) - (res[0] * res[1]));
}

int nums[] = {4,2,5,9,7,4,8};

int	main(void)
{
	printf("%d\n", maxProductDifference(nums, 7));
	return (0);
}