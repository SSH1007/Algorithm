#include <stdio.h>

int main() {
    int N, K;
    char mascot[8];

    scanf("%d", &N);
    scanf("%s", mascot);
    scanf("%d", &K);

    if (strcmp(mascot, "induck") == 0) {
        if (K % 2 == 0) {
            printf("%d\n", K);
        } else {
            if (K + 1 > N) {
                printf("%d\n", K - 1);
            } else {
                printf("%d\n", K + 1);
            }
        }
    } else {
        if (K % 2 == 1) {
            printf("%d\n", K);
        } else {
            if (K + 1 > N) {
                printf("%d\n", K - 1);
            } else {
                printf("%d\n", K + 1);
            }
        }
    }

    return 0;
}
