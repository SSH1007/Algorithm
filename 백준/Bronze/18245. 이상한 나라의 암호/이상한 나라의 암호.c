#include <stdio.h>
#include <string.h>

int main() {
    char S[10001];
    int t = 1;
    while (1) {
        scanf("%[^\n]%*c", S); 
        if (strcmp(S, "Was it a cat I saw?") == 0) {
            break;
        }
        for (int i = 0; i < strlen(S); i += t + 1) {
            putchar(S[i]);
        }
        putchar('\n');
        t++;
    }
    return 0;
}