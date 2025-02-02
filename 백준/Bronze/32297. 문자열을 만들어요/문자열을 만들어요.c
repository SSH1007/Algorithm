#include <stdio.h>
#include <string.h>

int main() {
    int N;
    char S[11]; 
    char g[] = "gori";
    
    scanf("%d", &N);
    scanf("%s", S);
    
    for (int n = 0; n <= N - 4; n++) {
        if (strncmp(&S[n], g, 4) == 0) {
            printf("YES\n");
            return 0;
        }
    }
    
    printf("NO\n");
    return 0;
}