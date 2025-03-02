#include <stdio.h>
#include <stdlib.h>

void F(int *arr, int size) {
    for (int i = 0; i < size - 1; i++) {
        for (int j = i + 1; j < size; j++) {
            if (arr[i] > arr[j]) {
                int temp = arr[i];
                arr[i] = arr[j];
                arr[j] = temp;
            }
        }
    }

    for (int i = 0; i < size; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");
}

int main() {
    int N, P;
    while (1) {
        if (scanf("%d %d", &N, &P) != 2) {
            break;
        }
        if (N == 0 && P == 0) {
            break;
        }

        int n = N / 2;
        int p = (P + 1) / 2;
        int dap[4];
        int size = 0;
        dap[size++] = 2 * p - 1;
        dap[size++] = 2 * p;
        dap[size++] = 2 * (n - p + 1);
        dap[size++] = 2 * (n - p + 1) - 1;
        int f_dap[4];
        int f_size = 0;
        for (int i = 0; i < size; i++) {
            if (dap[i] != P) {
                f_dap[f_size++] = dap[i];
            }
        }
        F(f_dap, f_size);
    }
    return 0;
}