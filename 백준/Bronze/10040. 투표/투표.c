#include <stdio.h>

int main() {
    int N, M;
    scanf("%d %d", &N, &M);
    int lst0[N];
    int lst1[N];

    for (int i = 0; i < N; i++) {
        scanf("%d", &lst0[i]);
        lst1[i] = 0;
    }
    for (int i = 0; i < M; i++) {
        int B;
        scanf("%d", &B);
        for (int j = 0; j < N; j++) {
            if (B >= lst0[j]) {
                lst1[j]++;
                break;
            }
        }
    }
    int dap = 0;
    int maxVote = 0;
    for (int i = 0; i < N; i++) {
        if (lst1[i] > maxVote) {
            maxVote = lst1[i];
            dap = i;
        }
    }
    printf("%d\n", dap + 1);
    return 0;
}