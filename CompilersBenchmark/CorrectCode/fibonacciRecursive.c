
#include <stdio.h>

int f(int a) {
	if (a<2) {
		return a;
	}
	else {
		return f(a-1) + f(a-2);
	}
	return 0;
}

// Recursive fibonnaci
int main(){
	int n;
    //printf("Enter a number:");
	//scanf("%d",&n);
	n = 10;
	int i = 1;
	while(i <= n){
		printf("%s", "fib(");
		printf("%i", i);
		printf("%s", ") = ");
		printf("%i", f(i));
		printf("%s", "; ");
		i = i+1;
	}
	return 0;
}
