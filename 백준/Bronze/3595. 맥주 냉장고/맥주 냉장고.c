#include <stdio.h>
#include <float.h>

int main() {
    int N;
    scanf("%d", &N);
    double dap = FLT_MAX; 
    int a = 0, b = 0, c = 0;

    for (int n = 1; n <= N; n++) {
        if (N % n == 0) {
            for (int m = 1; m <= N / n; m++) {
                if ((N / n) % m == 0) {
                    int o = N / n / m;
                    double current = 2 * (n * m + m * o + n * o);
                    if (dap > current) {
                        dap = current;
                        a = n;
                        b = m;
                        c = o;
                    }
                }
            }
        }
    }
    printf("%d %d %d\n", a, b, c);
    return 0;
}