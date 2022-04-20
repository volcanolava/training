#include <stdio.h>

extern unsigned int _fibonacci(int);

int main() {
	int fib_ind;
	printf("Enter Fibonacci index: ");
	scanf("%d", &fib_ind);

	int fib = _fibonacci(fib_ind);
	printf("Fibonnaci at %d is: %d\n", fib_ind, fib);
}