#include <stdio.h>

int main(void)
{
	unsigned int i = 0;
	unsigned short j = 0;

	i++;
	j++;
	printf("i: %d\tj: %d\n", i, j);

	int k;
	for(k = 0; k < 5; k ++) {
		i--;
		j--;
		printf("i: %d\tj: %d\n", i, j);
	}

	return 0;
}
