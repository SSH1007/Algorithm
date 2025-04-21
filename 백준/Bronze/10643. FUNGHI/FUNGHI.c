#include <stdio.h>

int main() {
    int pizza[8];
    for (int i = 0; i < 8; i++) {
        scanf("%d", &pizza[i]);
    }
    int dap = 0;
    for (int i = 0; i < 8; i++) {
        int tmp = 0;
        for (int j = 0; j < 4; j++) {
            int index = (i + j) % 8;
            tmp += pizza[index];
        }
        if (tmp > dap) {
            dap = tmp;
        }
    }
    printf("%d\n", dap);
    return 0;
}