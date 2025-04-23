#include <stdio.h>

int main() {
    int N;
    scanf("%d", &N);
    int As[N], Bs[N];
    for (int i = 0; i < N; i++) {
        scanf("%d", &As[i]);
    }
    for (int i = 0; i < N; i++) {
        scanf("%d", &Bs[i]);
    }
    int totalSum = 0;
    for (int i = 0; i < N; i++) {
        totalSum += As[i];
    }
    printf("%d\n", totalSum);
    int tmp = 0;
    for (int i = 0; i < N; i++) {
        tmp += ((Bs[i] ^ 1) * As[i]);
    }
    printf("%d\n", tmp);
    return 0;
}