#include <stdio.h>

int main() {
    int A, B;
    int dap = 0;
    scanf("%d %d", &A, &B);
    
    if (A % 2 == 0) {
        dap++;
        A++;
    }
    for (int i = A; i <= B; i += 2) {
        dap++;
    }
    
    printf("%d\n", dap);
    return 0;
}
