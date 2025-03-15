#include <stdio.h>

int main() {
    int T, k;
    scanf("%d", &T);
    for (int i = 0; i < T; i++) {
        scanf("%d", &k);
        printf("%d\n", k * 23);
    }
    return 0;
}