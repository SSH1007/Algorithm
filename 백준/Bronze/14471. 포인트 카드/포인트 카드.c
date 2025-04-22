#include <stdio.h>
#include <stdlib.h>

typedef struct {
    int A;
    int B;
} Pair;

int compare(const void* a, const void* b) {
    Pair* pa = (Pair*)a;
    Pair* pb = (Pair*)b;
    return pa->A - pb->A;
}

int main() {
    int N, M;
    scanf("%d %d", &N, &M);
    Pair lst[10000];
    int dap = 0, cnt = 0;
    int lstSize = 0;
    for (int i = 0; i < M; i++) {
        int A, B;
        scanf("%d %d", &A, &B);
        if (A < N) {
            lst[lstSize].A = A;
            lst[lstSize].B = B;
            lstSize++;
        } else {
            cnt++;
        }
    }
    qsort(lst, lstSize, sizeof(Pair), compare);
    while (cnt < M - 1 && lstSize > 0) {
        Pair tmp = lst[--lstSize];
        while (tmp.A < N && tmp.B > 0) {
            tmp.A++;
            tmp.B--;
            dap++;
        }
        cnt++;
    }
    printf("%d\n", dap);
    return 0;
}