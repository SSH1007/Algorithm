#include <stdio.h>

int main() {
    int N, Q;
    scanf("%d %d", &N, &Q);
    int balloon[N + 1];
    for (int i = 0; i <= N; i++) {
        balloon[i] = 0;
    }
    for (int q = 0; q < Q; q++) {
        int L, I;
        scanf("%d %d", &L, &I);
        for (int i = L; i <= N; i += I) {
            balloon[i] = 1;
        }
    }
    int count = 0;
    for (int i = 1; i <= N; i++) {
        if (balloon[i] == 0) {
            count++;
        }
    }
    printf("%d\n", count);
    return 0;
}