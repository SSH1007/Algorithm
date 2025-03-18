#include <stdio.h>
#include <stdlib.h>

int compare(const void *a, const void *b) {
    return (*(int*)a - *(int*)b);
}

int main() {
    int N;
    scanf("%d", &N);
    int *As = (int*)malloc(N * sizeof(int));
    for (int i = 0; i < N; i++) {
        scanf("%d", &As[i]);
    }
    int *odd = (int*)malloc(N * sizeof(int));
    int *even = (int*)malloc(N * sizeof(int));
    int odd_count = 0, even_count = 0;
    for (int i = 0; i < N; i++) {
        if (As[i] % 2 == 0) {
            even[even_count++] = As[i];
        } else {
            odd[odd_count++] = As[i];
        }
    }
    int dap = 0;
    for (int i = 0; i < even_count; i++) {
        dap += even[i];
    }
    qsort(odd, odd_count, sizeof(int), compare);
    while (odd_count > 1) {
        int a = odd[--odd_count];
        int b = odd[--odd_count];
        dap += (a + b);
    }
    printf("%d\n", dap);

    free(As);
    free(odd);
    free(even);
    return 0;
}