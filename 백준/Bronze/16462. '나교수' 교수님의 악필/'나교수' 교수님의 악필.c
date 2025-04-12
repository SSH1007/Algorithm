#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <math.h>

int main() {
    int N;
    scanf("%d", &N);
    getchar();
    double x = 0;
    char Q[101];
    for (int i = 0; i < N; i++) {
        fgets(Q, sizeof(Q), stdin);
        size_t len = strlen(Q);
        if (Q[len - 1] == '\n') {
            Q[len - 1] = '\0';
        }
        char s[101];
        for (int j = 0; Q[j] != '\0'; j++) {
            if (Q[j] == '0' || Q[j] == '6' || Q[j] == '9') {
                s[j] = '9';
            } else {
                s[j] = Q[j];
            }
        }
        s[strlen(Q)] = '\0';
        int num = atoi(s);
        if (num > 100) num = 100;
        x += num;
    }
    x /= N;
    int result = (x - (int)x >= 0.5) ? (int)x + 1 : (int)x;
    printf("%d\n", result);
    return 0;
}