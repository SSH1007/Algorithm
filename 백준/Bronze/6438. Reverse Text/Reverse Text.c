#include <stdio.h>
#include <string.h>

int main() {
    int N;
    scanf("%d", &N);
    getchar();
    
    for (int i = 0; i < N; i++) {
        char S[80];
        fgets(S, sizeof(S), stdin);
        
        S[strcspn(S, "\n")] = '\0';
        
        int len = strlen(S);
        for (int j = len - 1; j >= 0; j--) {
            printf("%c", S[j]);
        }
        printf("\n");
    }

    return 0;
}
