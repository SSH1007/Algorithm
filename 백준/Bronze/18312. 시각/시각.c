#include <stdio.h>
#include <stdbool.h>

bool F(int num, int target) {
    return num / 10 == target || num % 10 == target;
}

int main() {
    int N, K;
    scanf("%d %d", &N, &K);
    int dap = 0;
    for (int i = 0; i <= N; i++) {
        if (F(i, K)) {
            dap += 3600;
            continue;
        }
        for (int j = 0; j < 60; j++) {
            if (F(j, K)) {
                dap += 60;
                continue;
            }
            for (int k = 0; k < 60; k++) {
                if (F(k, K)) {
                    dap++;
                }
            }
        }
    }
    printf("%d\n", dap);
    return 0;
}