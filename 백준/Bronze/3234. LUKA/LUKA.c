#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() {
    int X, Y, K;
    char S[100001];
    int x = 0, y = 0;
    int lst[100001];
    int lst_size = 0;
    scanf("%d %d", &X, &Y);
    scanf("%d", &K);
    getchar();  
    fgets(S, sizeof(S), stdin);
    if (abs(X - x) <= 1 && abs(Y - y) <= 1) {
        lst[lst_size++] = 0;
    }
    for (int k = 0; k < K; k++) {
        char c = S[k];
        if (c == 'I') {
            x += 1;
        } else if (c == 'S') {
            y += 1;
        } else if (c == 'Z') {
            x -= 1;
        } else {
            y -= 1;
        }
        if (abs(X - x) <= 1 && abs(Y - y) <= 1) {
            lst[lst_size++] = k + 1;
        }
    }
    if (lst_size == 0) {
        printf("-1\n");
    } else {
        for (int i = 0; i < lst_size; i++) {
            printf("%d\n", lst[i]);
        }
    }
    return 0;
}