#include <stdio.h>

int fibonacci(int x) {
	if (x < 2) {
		return x;
	}
	return fibonacci(x-1) + fibonacci(x-2);
}

int main(){
	printf("%i",fibonacci(5));
	return 0;
}

