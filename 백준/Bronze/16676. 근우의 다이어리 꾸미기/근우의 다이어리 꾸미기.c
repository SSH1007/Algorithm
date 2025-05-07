#include <stdio.h>

int main() {
    int std = 11;
    int dap = 1;
    int N;
    scanf("%d", &N);
    while (1) {
        if (N < std) {
            printf("%d\n", dap);
            break;
        } else {
            std = std * 10 + 1;
            dap += 1;
        }
    }
    return 0;
}