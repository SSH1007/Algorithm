#include <stdio.h>

int hap(int n) {
    int res = 0;
    while (n > 0) {
        res += n % 10;
        n /= 10;
    }
    return res;
}

int main() {
    char S[12];
    scanf("%s", S);
    for (int i = 0; S[i] != '\0'; i++) {
        char s = S[i];
        int hapValue = hap((int) s);
        for (int j = 0; j < hapValue; j++) {
            printf("%c", s);
        }
        printf("\n");
    }
    return 0;
}