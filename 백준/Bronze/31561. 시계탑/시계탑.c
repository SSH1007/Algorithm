#include <stdio.h>

int main(void){
  int M;
  scanf("%d", &M);
  if (M <= 30){
    printf("%.1f\n", M/2.0);
  }
  else {
    printf("%.1f\n", 15+(M-30)*(3/2.0));
  }
  
  return 0;
}