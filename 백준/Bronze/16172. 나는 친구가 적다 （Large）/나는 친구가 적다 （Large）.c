#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <string.h>
#include <ctype.h>

int main(void) {
    char N[200001], K[200001];
    scanf("%s", N);
    scanf("%s", K);
    char tmp[200001];
    int idx = 0;
    for (int i = 0; N[i] != '\0'; i++) {
        if (!isdigit(N[i])) {
            tmp[idx++] = N[i];
        }
    }
    tmp[idx] = '\0';
    printf("%d\n", strstr(tmp, K) != NULL);
    return 0;
}