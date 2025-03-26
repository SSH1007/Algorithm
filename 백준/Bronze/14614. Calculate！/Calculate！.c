#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() {
    long long A, B;
    char C[102];
    scanf("%lld %lld %s", &A, &B, C);
    if (C[strlen(C) - 1] % 2 == 0) {
        printf("%lld\n", A);
    } else {
        printf("%lld\n", A ^ B);
    }
    return 0;
}