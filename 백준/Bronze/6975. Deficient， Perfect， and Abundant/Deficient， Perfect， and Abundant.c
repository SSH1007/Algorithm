#include <stdio.h>

int F(int X) {
    int sum = 0;
    for (int i = 1; i <= X / 2; i++) {
        if (X % i == 0) {
            sum += i;
        }
    }
    return sum;
}

int main() {
    int N;
    scanf("%d", &N); 
    for (int n = 0; n < N; n++) {
        if (n > 0) {
            printf("\n"); 
        }
        int X;
        scanf("%d", &X);
        int sum = F(X);
        if (sum > X) {
            printf("%d is an abundant number.\n", X);
        } else if (sum == X) {
            printf("%d is a perfect number.\n", X);
        } else {
            printf("%d is a deficient number.\n", X);
        }
    }
    return 0;
}