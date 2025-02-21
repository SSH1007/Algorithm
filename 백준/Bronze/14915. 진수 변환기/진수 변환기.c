#include <stdio.h>

int main() {
    int m, n;
    scanf("%d %d", &m, &n);

    if (m == 0) {
        printf("0\n");
        return 0;
    }

    int lst[32];
    int idx = 0;
    while (m > 1) {
        lst[idx++] = m % n;
        m /= n;
    }
    if (m > 0) {
        lst[idx++] = m;
    }

    for (int i = idx - 1; i >= 0; i--) {
        if (lst[i] > 9) {
            printf("%c", lst[i] + 55);
        } else {
            printf("%d", lst[i]);
        }
    }
    printf("\n");
    return 0;
}