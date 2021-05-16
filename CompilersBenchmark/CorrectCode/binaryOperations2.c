#include <stdio.h>

//WORKS

// This should print the number 10 for nested expressions
int main(){
        printf("%d", 2*(2+3));
        printf("%s", "; ");
        printf("%d", 2*4+2);
        printf("%s", "; ");
        printf("%d", 10/2+10/2);
        printf("%s", "; ");
        printf("%d", ((100-80)/2)+(5-5));
        printf("%s", "; ");

        return 1;
}
