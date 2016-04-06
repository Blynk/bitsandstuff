#include <stdio.h>

#define t 2015

int gcd(int a, int b)
{
	if(b == 0)
		return a;
	else
		return gcd(b, a%b);
}

int main(void)
{
	int i, counter = 0;
	for(i = 1; i <= t; i++)
		if(gcd(i, t) == 1)
		{
			printf("%d\n", i);
			counter++;
		}
	printf("There are %d integers that are coprime to %d\n", counter, t);

	return 0;
}
