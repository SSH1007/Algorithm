#include <stdio.h>

int main() {
    int N, M;
    scanf("%d %d", &N, &M);

    int friend[N];
    for (int i = 0; i < N; i++) {
        friend[i] = 0;
    }
    int target[M];
    for (int i = 0; i < M; i++) {
        scanf("%d", &target[i]);
    }

    for (int m = 0; m < M; m++) {
        int miss = 0;
        int lst[N];
        for (int n = 0; n < N; n++) {
            scanf("%d", &lst[n]);
            if (lst[n] == target[m]) {
                friend[n]++;
            } else {
                miss++;
            }
        }
        friend[target[m] - 1] += miss;
    }
    for (int i = 0; i < N; i++) {
        printf("%d\n", friend[i]);
    }
    return 0;
}