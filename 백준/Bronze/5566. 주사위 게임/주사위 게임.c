#include <stdio.h>

int main() {
    int N, M;
    scanf("%d %d", &N, &M);
    int board[N + 1];

    for (int i = 1; i <= N; i++) {
        scanf("%d", &board[i]);
    }

    int cur = 1;
    for (int j = 1; j <= M; j++) {
        int D;
        scanf("%d", &D);
        cur += D;
        if (cur >= N) {
            printf("%d\n", j);
            return 0;
        }
        cur += board[cur];
        if (cur >= N) {
            printf("%d\n", j);
            return 0;
        }
    }
    return 0;
}