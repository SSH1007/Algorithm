#include <stdio.h>

int main() {
    int a, m;
    scanf("%d %d", &a, &m);
    int x = 1;
    while (1) {
        if ((a * x) % m == 1) {
            break;
        }
        x++;
    }
    printf("%d\n", x);
    return 0;
}