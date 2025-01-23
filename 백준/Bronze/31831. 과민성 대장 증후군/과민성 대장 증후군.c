#include <stdio.h>
#include <stdlib.h>

int main(void){
  int N, M;
  scanf("%d %d", &N, &M);
  int *As = (int *)malloc(N*sizeof(int));
  for(int i = 0; i<N; i++){
    scanf("%d", &As[i]);
  }
  int s = 0, dap = 0;
  for(int i = 0; i<N; i++){
    s = (s + As[i] > 0) ? s+As[i] : 0;
    if (s >= M){
      dap ++;
    }
  }
  printf("%d\n", dap);
  free(As);
  return 0;
}