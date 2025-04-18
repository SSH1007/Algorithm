#include <stdio.h>

int F(int n) {
    int res = 0;
    while (n > 0) {
        res = res * 10 + (n % 10);
        n /= 10;
    }
    return res;
}

int main() {
    int N;
    scanf("%d", &N);
    for (int i = 0; i < N; i++) {
        int A, B;
        scanf("%d %d", &A, &B);
        int revA = F(A);
        int revB = F(B);
        int sum = revA + revB;
        printf("%d\n", F(sum));
    }
    return 0;
}