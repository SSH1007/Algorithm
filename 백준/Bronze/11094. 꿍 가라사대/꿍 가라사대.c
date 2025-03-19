#include <stdio.h>
#include <string.h>

int main() {
    int N;
    scanf("%d\n", &N);
    char S[102];  
    for (int i = 0; i < N; i++) {
        fgets(S, sizeof(S), stdin);
        if (strncmp(S, "Simon says", 10) == 0) {
            printf("%s", S + 10);
        }
    }
    return 0;
}