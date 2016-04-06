#include <stdio.h>
#include <math.h>

double f_to_eval(double x, double y)
{
	// f(x)
	// Can be changed for different functions
	return sqrt(1 + x * pow(M_E, -y));
}

void find_midpoint_sum(int num_squares)
{
	// number of squares per side
	double divisions = sqrt(num_squares);
	// side length of each square division
	double side_length = 1/divisions;
	// midpoint value for square
	double midpoint = side_length/2;

	double x, y;
	double sum = 0;
	// Here we want to sum the function at each midpoint,
	// so we iterate over each square in both x & y direction
	// we know that the midpoint values for each square are 
	// one side length from the last midpoint, so we can add
	// square number of side lengths to the midpoint to get 
	// the midpoint value of each square on its iteration
	for(x = 0; x < divisions; x++)
		for(y = 0; y < divisions; y++)
			sum += f_to_eval(midpoint + (side_length * x), midpoint + (side_length * y));

	// the estimate is the side length squared times the sum we got
	double estimate = side_length * side_length * sum;
	printf("Midpoint estimate for %d is %0.6lf\n", num_squares, estimate);
}

int main(int argc, char *argv[])
{
	int i;
	// find the midpoint estimate for 1, 4, 16, 64, 256, 1024
	// change the loop constraints to find more/less estimates
	for(i = 1; i <= 1024; i *= 4)
		find_midpoint_sum(i);


	return 0;
}
