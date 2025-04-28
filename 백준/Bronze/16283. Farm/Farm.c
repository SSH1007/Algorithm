#include <stdio.h>

int main() {
    int a, b, n, w;
    scanf("%d %d %d %d", &a, &b, &n, &w);
    int lst_x = -1, lst_y = -1;
    int cnt = 0;
    for (int x = 1; x < n; x++) {
        if (w == a * x + b * (n - x)) {
            lst_x = x;
            lst_y = n - x;
            cnt++;
        }
    }
    if (cnt != 1) {
        printf("-1\n");
    } else {
        printf("%d %d\n", lst_x, lst_y);
    }
    return 0;
}