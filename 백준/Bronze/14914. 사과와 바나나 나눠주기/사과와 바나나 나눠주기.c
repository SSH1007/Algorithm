#include <stdio.h>

int main() {
    int a, b;
    scanf("%d %d", &a, &b);
    int c = (a < b) ? a : b;
    
    for (int i = 1; i <= c; i++) {
        if (a % i == 0 && b % i == 0) {
            printf("%d %d %d\n", i, a / i, b / i);
        }
    }
    return 0;
}