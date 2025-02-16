#include <stdio.h>
#include <string.h>

int main() {
    int N;
    scanf("%d", &N);
    getchar();

    while (N--) {
        char S[1001];
        fgets(S, 1001, stdin);
        
        int alpha[26] = {0};
        
        for (int i = 0; S[i] != '\0'; i++) {
            if (S[i] != ' ') {
                alpha[S[i] - 'a']++;
            }
        }
        
        int maxN = 0;
        for (int i = 0; i < 26; i++) {
            if (alpha[i] > maxN) {
                maxN = alpha[i];
            }
        }

        int cnt = 0;
        for (int i = 0; i < 26; i++) {
            if (alpha[i] == maxN) {
                cnt++;
            }
        }

        if (cnt > 1) {
            printf("?\n");
        } else {
            for (int i = 0; i < 26; i++) {
                if (alpha[i] == maxN) {
                    printf("%c\n", i + 'a');
                    break;
                }
            }
        }
    }
    return 0;
}