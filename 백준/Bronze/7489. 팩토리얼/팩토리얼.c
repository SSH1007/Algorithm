#include <stdio.h>

int main() {
    int T;
    scanf("%d", &T);
    while (T--) {
        int N;
        scanf("%d", &N);
        int a = 1;
        for (int n = 1; n <= N; n++) {
            a *= n;
            while (a % 10 == 0) {
                a /= 10;
            }
            a %= 10000;
        }
        printf("%d\n", a % 10);
    }
    return 0;
}