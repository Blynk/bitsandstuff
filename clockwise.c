#include <stdio.h>
#include <stdlib.h>

#define FORWARD 0
#define BACKWARD 1

int size;
int total;
int *matrix;

void printClockwise(int start, int end, int direction, int *matrix)
{
	int i, j;
	int max = size * size;
	if(total == max)
		return;
	if(!direction)	//going L to R then Up to Down
	{	
		for(i = start; i < end && total < max; i++)
		{
			printf("[%d, %d]: %d ", start, i, matrix[start * size + i]);
			total++;
		}
		printf("\n");
		for(j = start + 1; j < end && total < max; j++)
		{
			printf("[%d, %d]: %d ", j, end - 1, matrix[j * size + end - 1]);
			total++;
		}
		printf("\n");

		return printClockwise(end - 1, start, BACKWARD, matrix);
	}
	else	// going R to L then Down to Up
	{
		for(i = start - 1; i >= end && total < max; i--)
		{
			printf("[%d, %d]: %d ", start, i, matrix[start * size + i]);
			total++;
		}
		printf("\n");
		for(j = start - 1; j > end && total < max; j--)
		{
			printf("[%d, %d]: %d ", j, end, matrix[j * size + end]);
			total++;
		}
		printf("\n");

		return printClockwise(end + 1, start, FORWARD, matrix);
	}
}

int main(void)
{
	printf("Enter matrix size (nxn)\n");
	scanf("%d", &size);
	printf("\n");
	matrix = malloc(sizeof(int) * size * size);

	printf("Initializing matrix... \n\n");
	//initialize then print matrix as is -->
	int i, j;
	for(i = 0; i < size; i++)
	{
		for(j = 0; j < size; j++)
		{
			int offset = i * size + j;
			matrix[offset] = i + j + 1;
			if(matrix[offset] < 10)
				printf("  %d  ", matrix[offset]);
			else
				printf(" %d  ", matrix[offset]);
		}
		printf("\n");
	}
	total = 0;
	// now print in clockwise direction
	printClockwise(0, size, FORWARD, matrix);

	return 0;
}
