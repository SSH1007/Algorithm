#include <stdio.h>
int main() {
    int N, A, B;
    int dap = 0;
    scanf("%d", &N);
    for (int i = 1; i <= N; i ++){
        scanf("%d %d", &A, &B);
        dap += A;
        dap -= B;
        printf("%d\n", dap);
    }
    return 0;
}