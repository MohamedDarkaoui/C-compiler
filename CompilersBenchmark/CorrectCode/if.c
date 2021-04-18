#include <stdio.h>


int main(){
	int x = 5;
	if (x < 5){
		printf("%s","Something went wrong"); // Should not print
	}
	if (x >= 5){
		printf("%s","Hello world! "); // Should print
	}
	if (x == 5){
		if (x != 4){
			printf("%s","Hello world! "); // Should print
		}
	}
	return 1;
}
