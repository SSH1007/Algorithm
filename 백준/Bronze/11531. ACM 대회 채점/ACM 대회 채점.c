#include <stdio.h>
#include <string.h>

int main() {
    int lst[2][26] = {0};
    int m, idx;
    char nme[10], res[10];
    while (1) {
        if (scanf("%d", &m) != 1) break;
        if (m == -1) break;
        scanf("%s %s", nme, res);
        idx = nme[0] - 'A';
        if (strcmp(res, "right") == 0) {
            lst[1][idx] = 1;
            lst[0][idx] += m;
        } else {
            lst[0][idx] += 20;
        }
    }
    int dap = 0, sum = 0;
    for (int i = 0; i < 26; i++) {
        if (lst[1][i] == 1) {
            dap += lst[0][i];
            sum++;
        }
    }
    printf("%d %d\n", sum, dap);
    return 0;
}