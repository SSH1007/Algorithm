#include <stdio.h>

int main() {
    int N, i = 1;
    scanf("%d", &N);
    while (N > i) {
        N -= i;
        i++;
    }
    printf("%d %d\n", i + 1 - N, N);
    return 0;
}