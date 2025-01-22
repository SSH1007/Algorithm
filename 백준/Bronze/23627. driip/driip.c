#include <stdio.h>
#include <string.h>

int main(void){
  char S[1000];
  scanf("%s", &S);
  int len = strlen(S);
  if (len >= 5 && strcmp(S+len-5, "driip")==0){
    printf("cute\n");
  } else {
    printf("not cute\n");
  }

  return 0;
}