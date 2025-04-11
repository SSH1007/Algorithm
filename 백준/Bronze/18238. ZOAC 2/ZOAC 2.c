#include <stdio.h>

int main() {
    char input[101];
    scanf("%s", input);
    int start = 0;
    int acc = 0;
    for (int i = 0; input[i] != '\0'; i++) {
        int c = input[i] - 'A';
        int m = (start - c + 26) % 26;
        int n = 26 - m;
        acc += (m < n) ? m : n;
        start = c;
    }
    printf("%d\n", acc);
    return 0;
}