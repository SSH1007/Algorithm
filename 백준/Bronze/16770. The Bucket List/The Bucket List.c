#include <stdio.h>

int main() {
    int N;
    scanf("%d", &N);
    int buckets[1001] = {0};
    for (int n = 0; n < N; n++) {
        int s, t, b;
        scanf("%d %d %d", &s, &t, &b);
        for (int i = s; i <= t; i++) {
            buckets[i] += b;
        }
    }
    int max = 0;
    for (int i = 0; i < 1001; i++) {
        if (buckets[i] > max) {
            max = buckets[i];
        }
    }
    printf("%d\n", max);
    return 0;
}