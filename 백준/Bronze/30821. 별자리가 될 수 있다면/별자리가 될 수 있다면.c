#include <stdio.h>

int main(void){
  int N;
  long long tmp = 1;
  
  scanf("%d", &N);
  for (int i = N - 4; i <= N; i++) {
    tmp *= i;
  }
  printf("%lld\n", tmp/120);

  return 0;
}