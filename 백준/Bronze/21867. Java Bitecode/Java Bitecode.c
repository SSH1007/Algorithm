#include <stdio.h>
#include <string.h>

int main() {
    int N;
    char S[200002];
    scanf("%d", &N);
    getchar();
    fgets(S, sizeof(S), stdin);
    char result[200002];
    int resultIndex = 0;
    for (int n = 0; n < N; n++) {
        char ch = S[n];
        if (ch != 'J' && ch != 'A' && ch != 'V') {
            result[resultIndex++] = ch;
        }
    }
    if (resultIndex > 0) {
        result[resultIndex] = '\0';
        printf("%s\n", result);
    } else {
        printf("nojava\n");
    }
    return 0;
}