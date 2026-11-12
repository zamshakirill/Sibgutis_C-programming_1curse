#include <stdio.h>

int deg2(int n);

int main()
{
	int n;
	printf("Введите число: ");
	scanf("%d", &n);
	int number = deg2(n);
	if (number > 0) {
		printf("это 2 в степени %d\n", number);
	} else {
		printf("это не степень двойки\n");
	}
	return 0;
}

int deg2(int n)
{
	int k = 1;
	while (n > 2)
	{
		if ((n & 1) == 0) {
			k = k + 1;
			n = n >> 1;
		} else {
			return 0;
		}
	}
	return k;
}