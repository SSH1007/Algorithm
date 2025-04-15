#include <stdio.h>
#include <string.h>

int main() {
    char S[1001];
    fgets(S, sizeof(S), stdin);
    size_t len = strlen(S);
    if (S[len - 1] == '\n') {
        S[len - 1] = '\0';
        len--;
    }
    int hasA = 0, hasB = 0, hasC = 0;
    for (size_t i = 0; i < len; i++) {
        if (S[i] == 'A') {
            hasA = 1;
            break;
        } else if (S[i] == 'B') {
            hasB = 1;
        } else if (S[i] == 'C') {
            hasC = 1;
        }
    }
    if (hasA) {
        for (size_t i = 0; i < len; i++) {
            if (S[i] == 'B' || S[i] == 'C' || S[i] == 'D' || S[i] == 'F') {
                S[i] = 'A';
            }
        }
    } else if (hasB) {
        for (size_t i = 0; i < len; i++) {
            if (S[i] == 'C' || S[i] == 'D' || S[i] == 'F') {
                S[i] = 'B';
            }
        }
    } else if (hasC) {
        for (size_t i = 0; i < len; i++) {
            if (S[i] == 'D' || S[i] == 'F') {
                S[i] = 'C';
            }
        }
    } else {
        for (size_t i = 0; i < len; i++) {
            S[i] = 'A';
        }
    }
    printf("%s\n", S);
    return 0;
}