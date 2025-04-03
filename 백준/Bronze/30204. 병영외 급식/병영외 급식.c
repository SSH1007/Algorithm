#include <stdio.h>

int main() {
    int N, X;
    scanf("%d %d", &N, &X);
    int Ps[N];
    int sum = 0;
    for (int i = 0; i < N; i++) {
        scanf("%d", &Ps[i]);
        sum += Ps[i];
    }
    if (sum % X == 0) {
        printf("1\n");
    } else {
        printf("0\n");
    }
    return 0;
}