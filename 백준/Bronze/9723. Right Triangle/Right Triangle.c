#include <stdio.h>
#include <stdlib.h>

int compare(const void *a, const void *b){
  return (*(int*)a-*(int*)b);
}

int main(void){
  int N;
  scanf("%d", &N);
  for (int i = 1; i <= N; i++){
    int a, b, c;
    scanf("%d %d %d", &a, &b, &c);
    int arr[3] = {a, b, c};
    qsort(arr, 3, sizeof(int), compare);
    a = arr[0];
    b = arr[1];
    c = arr[2];
    printf("Case #%d: ", i);
    if (c*c == a*a+b*b){
      printf("YES\n");
    } else {
      printf("NO\n");
    }
  }
  return 0;
}