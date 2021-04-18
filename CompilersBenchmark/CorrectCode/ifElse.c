#include <stdio.h>


int main(){
	int x = 5;
	if (x < 5){
		printf("%s","Something went wrong"); // Should not print
	} else {
		printf("%s","Hello world!\n"); // Should print
	}
	if (x == 5){
		if (x == 5){
			printf("%s","Hello world!\n"); // Should print
		} else {
			printf("%s","Something went wrong"); // Should not print
		}
	}
	return 1;
}
