#include <stdio.h>
#include <string.h>

int main() {
    char S[4];
    fgets(S, sizeof(S), stdin);
    
    if (strcmp(S, "(1)") == 0) {
        printf("%d", 0);
    } else if (strcmp(S, ")1(") == 0) {
        printf("%d", 2);
    } else {
        printf("%d", 1);
    }

    return 0;
}
