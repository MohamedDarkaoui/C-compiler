#include <stdio.h>

int a[2];

// Should print the numbers 1 2 3



int main(){
	int x = 3;
	a[0] = 1;
	a[1] = 2;
	printf("%d", a[0]);
    printf("%s", "; ");
    printf("%d", a[1]);
    printf("%s", "; ");
    printf("%d", x);
    printf("%s", "; ");
	return 1;
}
