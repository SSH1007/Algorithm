#include <stdio.h>
#include <string.h>
#include <math.h>

int main(void){
  int a, b, c;
  scanf("%d %d %d", &a, &b, &c);
  if (a == 0){
    printf("%d\n", (int) pow(c, 2)-b);
  }
  else if (b == 0){
    printf("%d\n", (int) pow(c, 2)-a);
  }
  else {
    printf("%d\n", (int) sqrt(a+b));
  }

  return 0;
}