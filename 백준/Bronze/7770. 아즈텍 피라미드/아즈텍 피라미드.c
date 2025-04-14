#include <stdio.h>

int main() {
    long n;
    scanf("%ld", &n);  
    long blocks = 0;
    long x = 0;
    long y = 1;  
    int cnt = 0;
    while (1) {
        blocks += (x * x + y * y);
        if (n < blocks) {
            break;
        }
        x += 1;
        y += 1;
        cnt += 1;
    }
    printf("%d\n", cnt);
    return 0;
}