#include <stdio.h>

int main() {
    int N, M;
    scanf("%d %d", &N, &M);
    
    int bulb[N];
    for (int i = 0; i < N; i++) {
        scanf("%d", &bulb[i]);
    }

    for (int i = 0; i < M; i++) {
        int a, b, c;
        scanf("%d %d %d", &a, &b, &c);
        b--;
        if (a == 1) {
            bulb[b] = c;
        } else if (a == 2) {
            for (int j = b; j < c; j++) {
                bulb[j] = (bulb[j] + 1) % 2;
            }
        } else if (a == 3) {
            for (int j = b; j < c; j++) {
                bulb[j] = 0;
            }
        } else {
            for (int j = b; j < c; j++) {
                bulb[j] = 1;
            }
        }
    }

    for (int i = 0; i < N; i++) {
        printf("%d ", bulb[i]);
    }
    printf("\n");
    return 0;
}