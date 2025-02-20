#include <stdio.h>
#include <math.h>

int main() {
    int C, K;
    scanf("%d %d", &C, &K);
    int t = C % (int)pow(10, K);
    if (t >= pow(10, K)/2){
        C += (int)pow(10, K);
    }
    C -= t;
    printf("%d\n", C);
    return 0;
}