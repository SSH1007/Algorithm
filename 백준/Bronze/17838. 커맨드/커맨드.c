#include <stdio.h>
#include <string.h>

int F(const char *S) {
    if (strlen(S) != 7) {
        return 0;
    }
    if (S[0] == S[1] && S[1] == S[4] &&
        S[2] == S[3] && S[3] == S[5] && S[5] == S[6] &&
        S[0] != S[2]) {
        return 1;
    }
    return 0;
}

int main() {
    int T;
    scanf("%d", &T);
    getchar(); 
    for (int i = 0; i < T; ++i) {
        char S[10002];
        fgets(S, sizeof(S), stdin);
        int len = strlen(S);
        if (S[len - 1] == '\n') {
            S[len - 1] = '\0';
        }
        printf("%d\n", F(S));
    }
    return 0;
}