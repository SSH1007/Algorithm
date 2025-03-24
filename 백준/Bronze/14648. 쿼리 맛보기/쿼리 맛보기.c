#include <stdio.h>

#define MAX_N 1000
long y[MAX_N]; 

int main() {
    int n, q;
    scanf("%d %d", &n, &q);
    for (int i = 0; i < n; i++) {
        scanf("%ld", &y[i]);
    }
    while (q--) {
        int type;
        scanf("%d", &type);
        if (type == 1) {
            int l, r;
            scanf("%d %d", &l, &r);
            l--; r--;
            long sum = 0;
            for (int i = l; i <= r; i++) {
                sum += y[i];
            }
            printf("%ld\n", sum);
            long temp = y[l];
            y[l] = y[r];
            y[r] = temp;
        } else {
            int l1, r1, l2, r2;
            scanf("%d %d %d %d", &l1, &r1, &l2, &r2);
            l1--; r1--; l2--; r2--;
            long sum1 = 0, sum2 = 0;
            for (int i = l1; i <= r1; i++) {
                sum1 += y[i];
            }
            for (int i = l2; i <= r2; i++) {
                sum2 += y[i];
            }
            printf("%ld\n", sum1 - sum2);
        }
    }
    return 0;
}