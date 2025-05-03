#include <stdio.h>
#include <stdlib.h>

int compare(const void *a, const void *b) {
    return *(int *)b - *(int *)a;
}

int main() {
    int N;
    scanf("%d", &N);
    int L[N];
    for (int i = 0; i < N; i++) {
        scanf("%d", &L[i]);
    }
    qsort(L, N, sizeof(int), compare);
    int lvs[] = {60, 100, 140, 200, 250};
    int hap = 0, up = 0;
    for (int i = 0; i < 42 && i < N; i++) {
        for (int j = 0; j < 5; j++) {
            if (L[i] >= lvs[j]) {
                up++;
            }
        }
        hap += L[i];
    }
    printf("%d %d\n", hap, up);
    return 0;
}