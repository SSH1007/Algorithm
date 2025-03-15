#include <stdio.h>

int main() {
    double N, B, M;
    while (1) {
        if (scanf("%lf %lf %lf", &N, &B, &M) == EOF) {
            break;
        }

        int year = 0;
        while (N <= M) {
            N += N * B / 100;
            year++;
        }
        printf("%d\n", year);
    }
    return 0;
}