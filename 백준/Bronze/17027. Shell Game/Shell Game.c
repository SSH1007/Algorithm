#include <stdio.h>

int main() {
    int N;
    scanf("%d", &N);
    int lst[N][3];
    for (int i = 0; i < N; i++) {
        scanf("%d %d %d", &lst[i][0], &lst[i][1], &lst[i][2]);
    }
    int dap = 0;
    for (int i = 1; i <= 3; i++) { 
        int tmp = 0;
        int current = i;
        for (int n = 0; n < N; n++) {
            int a = lst[n][0];
            int b = lst[n][1];
            int g = lst[n][2];
            if (current == a) {
                current = b;
            } else if (current == b) {
                current = a;
            }
            if (current == g) {
                tmp++;
            }
        }
        if (dap < tmp) {
            dap = tmp;
        }
    }
    printf("%d\n", dap);
    return 0;
}