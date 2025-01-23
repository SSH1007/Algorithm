#include <stdio.h>
#include <string.h>
#include <ctype.h>

int main(void){
  int N;
  char S[100001];
  scanf("%d", &N);
  getchar();
  fgets(S, sizeof(S), stdin);
  
  int alp[26] = {0};
  for (int i = 0; i < N; i++){
    char c = S[i];
    if (isalpha(c)){
      alp[tolower(c)-'a']++;
    }
  }
  int maxIndex = 0;
  for (int i=1; i<26; i++){
    if (alp[i] > alp[maxIndex]){
      maxIndex = i;
    }
  }
  printf("%d\n", alp[maxIndex]);

  return 0;
}