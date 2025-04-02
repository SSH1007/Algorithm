#include <stdio.h>
#include <string.h>

int main() {
    char N[20];
    scanf("%s", N);
    int L = strlen(N);
    long num = 0;
    long dap = 0;
    for (int i = 0; i < L; i++) {
        num = num * 10 + (N[i] - '0');
    }
    for (int i = 0; i < L; i++) {
        long a = num % 10;
        long b = num / 10;
        long powerOfTen = 1;
        for (int j = 0; j < L - 1; j++) {
            powerOfTen *= 10;
        }
        num = b + a * powerOfTen;
        dap += b + a * powerOfTen;
    }
    printf("%ld\n", dap);
    return 0;
}