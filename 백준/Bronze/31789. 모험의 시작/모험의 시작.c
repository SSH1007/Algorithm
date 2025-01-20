#include <stdio.h>

int main(void){
  int N, X, S;
  scanf("%d", &N);
  scanf("%d %d", &X, &S);
  int dap = 0;
  for (int i = 0; i <= N; i++){
    int c, p;
    scanf("%d %d", &c, &p);
    if (c <= X && dap < p){
      dap = p;
    }
  }
  if (dap > S){
    printf("YES");
  }
  else {
    printf("NO");
  }
  return 0;
}