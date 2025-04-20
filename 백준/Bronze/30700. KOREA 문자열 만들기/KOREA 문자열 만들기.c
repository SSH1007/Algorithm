#include <stdio.h>
#include <string.h>

int main() {
    char S[1001];
    scanf("%s", S);
    char K[] = {'K', 'O', 'R', 'E', 'A'};
    int j = 0;
    int count = 0;
    for (int i = 0; S[i] != '\0'; i++) {
        if (S[i] == K[j]) {
            count++;
            j = (j + 1) % 5;
        }
    }
    printf("%d\n", count);
    return 0;
}