#include <stdio.h>


int fibonacci(int x) {
    if (x < 2) {
        return x;
    }
    return fibonacci(x-1) + fibonacci(x-2);
}

int main() {
    int c = fibonacci(5);
    printf("%i", c);
    return 0;
}