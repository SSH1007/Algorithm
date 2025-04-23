#include <stdio.h>
#include <ctype.h>
#include <string.h>

const char* dic(char c) {
    switch(c) {
        case 'B': return "v";
        case 'E': return "ye";
        case 'H': return "n";
        case 'P': return "r";
        case 'C': return "s";
        case 'Y': return "u";
        case 'X': return "h";
        default: {
            static char str[2];
            str[0] = tolower(c);
            str[1] = '\0';
            return str;
        }
    }
}

int main() {
    char S[101];
    fgets(S, sizeof(S), stdin);
    S[strcspn(S, "\n")] = '\0';
    for (int i = 0; S[i] != '\0'; i++) {
        printf("%s", dic(S[i]));
    }
    printf("\n");
    return 0;
}