#include <stdio.h>
#include <string.h>

int main(void){
  int N;
  scanf("%d", &N);
  int n = 0, c = 0;
  
  while (1) {
    n += 1;
    c += 1;
    if (n == N){
      printf("%d\n", c);
      break;
    }

    char numStr[20];
    sprintf(numStr, "%d", n);
    if (strstr(numStr, "50") != NULL){
      c += 1;
    }
  }

  return 0;
}