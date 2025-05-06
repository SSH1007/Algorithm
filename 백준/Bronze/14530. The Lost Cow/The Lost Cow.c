#include <stdio.h>
#include <stdlib.h>

int main() {
    int x, y;
    scanf("%d %d", &x, &y);
    int dap = 0;
    int dir = 1;
    int move = 1;
    int cur = x;
    while (1) {
        int next = x + dir * move;
        if ((x <= y && y <= next) || (next <= y && y <= x)) {
            dap += abs(y - cur);
            break;
        } else {
            dap += abs(next - cur);
            cur = next;
            move *= 2;
            dir *= -1;
        }
    }
    printf("%d\n", dap);
    return 0;
}