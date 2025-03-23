#include <stdio.h>

int main() {
    int M, N, K;
    scanf("%d %d %d", &M, &N, &K);
    for (int i = 0; i < M; i++) {
        char S[12];
        scanf("%s", S);
        for (int j = 0; j < K; j++) {
            for (int k = 0; S[k] != '\0'; k++) {
                for (int l = 0; l < K; l++) {
                    printf("%c", S[k]);
                }
            }
            printf("\n");
        }
    }
    return 0;
}