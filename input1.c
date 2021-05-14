
#include <stdio.h>

int main() {
   for (int i = 0; i < 10; i = i+1) {
      for (int x = 0; x < 10; x = x+1) {
         printf("%i", x*i);
         printf("%s", "   ");
      }
      printf("%s", "\n");

   }
}
