#include <stdio.h>

int main(){
    // Should print the numbers from 0 to 9
	for(int a = 0; a < 10; a = a+1){
		printf("%d", a);
		printf("%s", "; ");
	}
	return 0;
}
