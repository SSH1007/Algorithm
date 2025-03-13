#include <stdio.h>
#include <string.h>

int main() {
    char lst[] = {'r', 's', 'e', 'f', 'a', 'q', 't', 'd', 'w', 'c', 'z', 'x', 'v', 'g'};
    int N;
    scanf("%d", &N);
    char S[32];
    scanf("%s", S);
    char l_chr = S[strlen(S) - 1];
    int found = 0;
    for (int i = 0; i < 14; i++) {
        if (lst[i] == l_chr) {
            found = 1;
            break;
        }
    }
    if (found) {
        printf("1\n");
    } else {
        printf("0\n");
    }
    return 0;
}