#include <stdio.h>

int main() {
    int N, C;
    scanf("%d %d", &N, &C);
    int A = N, B = N;
    for (int i = 0; i < C; i++) {
        int X, Y;
        scanf("%d %d", &X, &Y);
        if (X >= A || Y >= B) {
            continue;
        }
        int horizonCut = X * B;
        int verticalCut = Y * A;
        if (horizonCut >= verticalCut) {
            A = X;
        } else {
            B = Y;
        }
    }
    printf("%d\n", A * B);
    return 0;
}