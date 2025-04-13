#include <stdio.h>

int main() {
    int N, X, Y, tmp = 0;
    scanf("%d", &N);
    int As[N];
    for (int i = 0; i < N; i++) {
        scanf("%d", &As[i]);
    }
    scanf("%d %d", &X, &Y);
    for (int i = 0; i < N; i++) {
        if (As[i] >= Y) {
            tmp++;
        }
    }
    printf("%d %d\n", (N * X) / 100, tmp);
    return 0;
}