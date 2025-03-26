#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <stdbool.h>

bool check(int n) {
    if (n % 2 == 0) {
        return false;
    }
    for (int i = 3; i <= sqrt(n); i += 2) {
        if (n % i == 0) {
            return false;
        }
    }
    return true;
}

int main() {
    char O[7], N[2];
    scanf("%s %s", O, N);
    char *endptr;
    int iO = strtol(O, &endptr, 10);
    char N_O[9];
    snprintf(N_O, sizeof(N_O), "%s%s", N, O);
    int iNO = strtol(N_O, &endptr, 10);

    bool A = check(iO);
    bool B = check(iNO);
    if (A == B) {
        printf("Yes\n");
    } else {
        printf("No\n");
    }
    return 0;
}