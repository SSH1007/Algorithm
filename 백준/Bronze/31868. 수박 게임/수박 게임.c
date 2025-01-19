#include <stdio.h>

int main(void){
  int N, K;
  scanf("%d %d", &N, &K);
  int cnt = 1;
  while (1) {
    if (cnt == N) {
      printf("%d", K);
      break;
    }
    K /= 2;
    cnt += 1;
  }
  return 0;
}