#include <stdio.h>

//	OUR COMPILER DOESNT SUPPORT FORWARD DECLARATIONS
//void f();

//void g();

void f(){
	printf("%s","Hello ");
	return;
}

void g(){
	printf("%s","World; ");
	f();
	printf("%s", "World");
	return;
}

int main(){
    // Should print "hello world" twice
	f();
	g();
	return 1;
}
